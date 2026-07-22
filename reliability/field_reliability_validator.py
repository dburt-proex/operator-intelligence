#!/usr/bin/env python3
"""Operator Intelligence v1.1 blinded field-reliability validator.

Purpose: compare independent evaluator records without changing approved scores.
Folder alignment: reliability/ (post-v1.1 Field Reliability Program).
Inputs: CSV rows with criterion_id, category, evaluator_id, state, and score.
Outputs: JSON metrics, disagreement records, validation errors, and a gate decision.

Governance rules:
- source records are read-only;
- unknown and blocked are states, never numeric zeroes;
- only approved 0/25/50/75/100 score anchors are admitted;
- invalid or insufficient evidence fails closed with HALT;
- ALLOW requires explicit reviewer-supplied thresholds;
- metrics support review and do not approve methodology or publication changes.

Usage:
  python reliability/field_reliability_validator.py --self-test
  python reliability/field_reliability_validator.py study.csv
  python reliability/field_reliability_validator.py study.csv \
    --threshold exact_agreement=0.70 --threshold adjacent_agreement=0.90
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ANCHORS = (0, 25, 50, 75, 100)
STATES = {"scored", "unknown", "blocked", "not_applicable"}
THRESHOLD_KEYS = {
    "exact_agreement",
    "adjacent_agreement",
    "state_agreement",
    "weighted_kappa",
}


class ValidationError(ValueError):
    """Raised when a study cannot be admitted for reliability analysis."""


@dataclass(frozen=True)
class Rating:
    criterion_id: str
    category: str
    evaluator_id: str
    state: str
    score: int | None


def _parse_score(raw: str, state: str, row_number: int) -> int | None:
    value = raw.strip()
    if state != "scored":
        if value:
            raise ValidationError(
                f"row {row_number}: state '{state}' must not carry a numeric score"
            )
        return None
    if not value:
        raise ValidationError(f"row {row_number}: scored state requires a score")
    try:
        score = int(value)
    except ValueError as exc:
        raise ValidationError(f"row {row_number}: score must be an integer") from exc
    if score not in ANCHORS:
        raise ValidationError(
            f"row {row_number}: score {score} is outside approved anchors {ANCHORS}"
        )
    return score


def read_ratings(rows: Iterable[dict[str, str]]) -> list[Rating]:
    ratings: list[Rating] = []
    seen: set[tuple[str, str]] = set()
    for row_number, row in enumerate(rows, start=2):
        missing = {
            key
            for key in ("criterion_id", "category", "evaluator_id", "state", "score")
            if key not in row
        }
        if missing:
            raise ValidationError(
                f"row {row_number}: missing columns {', '.join(sorted(missing))}"
            )
        criterion_id = row["criterion_id"].strip()
        category = row["category"].strip()
        evaluator_id = row["evaluator_id"].strip()
        state = row["state"].strip()
        if not criterion_id or not category or not evaluator_id:
            raise ValidationError(
                f"row {row_number}: criterion_id, category, and evaluator_id are required"
            )
        if state not in STATES:
            raise ValidationError(f"row {row_number}: unsupported state '{state}'")
        key = (criterion_id, evaluator_id)
        if key in seen:
            raise ValidationError(
                f"row {row_number}: duplicate rating for {criterion_id}/{evaluator_id}"
            )
        seen.add(key)
        ratings.append(
            Rating(
                criterion_id=criterion_id,
                category=category,
                evaluator_id=evaluator_id,
                state=state,
                score=_parse_score(row["score"], state, row_number),
            )
        )
    if not ratings:
        raise ValidationError("study contains no rating rows")
    return ratings


def _quadratic_weighted_kappa(pairs: list[tuple[int, int]]) -> float | None:
    if not pairs:
        return None
    size = len(ANCHORS)
    index = {score: position for position, score in enumerate(ANCHORS)}
    observed = [[0.0] * size for _ in range(size)]
    left = [0.0] * size
    right = [0.0] * size
    for first, second in pairs:
        i, j = index[first], index[second]
        observed[i][j] += 1
        left[i] += 1
        right[j] += 1
    count = float(len(pairs))
    observed_disagreement = 0.0
    expected_disagreement = 0.0
    denominator = float((size - 1) ** 2)
    for i in range(size):
        for j in range(size):
            weight = ((i - j) ** 2) / denominator
            observed_disagreement += weight * (observed[i][j] / count)
            expected_disagreement += weight * ((left[i] * right[j]) / (count * count))
    if math.isclose(expected_disagreement, 0.0):
        return 1.0 if math.isclose(observed_disagreement, 0.0) else None
    return 1.0 - (observed_disagreement / expected_disagreement)


def evaluate(
    ratings: list[Rating], thresholds: dict[str, float] | None = None
) -> dict[str, object]:
    by_criterion: dict[str, list[Rating]] = defaultdict(list)
    category_by_criterion: dict[str, str] = {}
    evaluators: set[str] = set()
    for rating in ratings:
        previous = category_by_criterion.setdefault(rating.criterion_id, rating.category)
        if previous != rating.category:
            raise ValidationError(
                f"criterion {rating.criterion_id} has conflicting categories"
            )
        by_criterion[rating.criterion_id].append(rating)
        evaluators.add(rating.evaluator_id)
    if len(evaluators) < 2:
        raise ValidationError("at least two independent evaluators are required")

    score_pairs: list[tuple[int, int]] = []
    state_pair_count = 0
    state_match_count = 0
    disagreements: list[dict[str, object]] = []
    category_deltas: dict[str, list[int]] = defaultdict(list)

    for criterion_id, criterion_ratings in sorted(by_criterion.items()):
        if len(criterion_ratings) < 2:
            disagreements.append(
                {
                    "criterion_id": criterion_id,
                    "category": category_by_criterion[criterion_id],
                    "type": "missing_peer_rating",
                }
            )
            continue
        ordered = sorted(criterion_ratings, key=lambda item: item.evaluator_id)
        for left_index, left in enumerate(ordered):
            for right in ordered[left_index + 1 :]:
                state_pair_count += 1
                if left.state == right.state:
                    state_match_count += 1
                else:
                    disagreements.append(
                        {
                            "criterion_id": criterion_id,
                            "category": left.category,
                            "type": "state_disagreement",
                            "evaluators": [left.evaluator_id, right.evaluator_id],
                            "values": [left.state, right.state],
                        }
                    )
                if left.score is not None and right.score is not None:
                    score_pairs.append((left.score, right.score))
                    delta = abs(left.score - right.score)
                    category_deltas[left.category].append(delta)
                    if delta > 25:
                        disagreements.append(
                            {
                                "criterion_id": criterion_id,
                                "category": left.category,
                                "type": "substantive_score_disagreement",
                                "evaluators": [left.evaluator_id, right.evaluator_id],
                                "values": [left.score, right.score],
                                "delta": delta,
                            }
                        )

    if state_pair_count == 0:
        raise ValidationError("no evaluator pairs were available")
    exact = (
        sum(first == second for first, second in score_pairs) / len(score_pairs)
        if score_pairs
        else None
    )
    adjacent = (
        sum(abs(first - second) <= 25 for first, second in score_pairs)
        / len(score_pairs)
        if score_pairs
        else None
    )
    metrics = {
        "criterion_count": len(by_criterion),
        "evaluator_count": len(evaluators),
        "state_pair_count": state_pair_count,
        "scored_pair_count": len(score_pairs),
        "state_agreement": state_match_count / state_pair_count,
        "exact_agreement": exact,
        "adjacent_agreement": adjacent,
        "weighted_kappa": _quadratic_weighted_kappa(score_pairs),
        "category_mean_absolute_delta": {
            category: sum(deltas) / len(deltas)
            for category, deltas in sorted(category_deltas.items())
        },
        "disagreement_count": len(disagreements),
    }

    threshold_results: dict[str, bool] = {}
    for key, minimum in sorted((thresholds or {}).items()):
        value = metrics[key]
        threshold_results[key] = value is not None and float(value) >= minimum

    if thresholds and threshold_results and all(threshold_results.values()):
        gate = "ALLOW"
        reason = "all reviewer-supplied reliability thresholds passed"
    else:
        gate = "REVIEW"
        reason = (
            "reviewer thresholds are required before acceptance"
            if not thresholds
            else "one or more reviewer-supplied reliability thresholds did not pass"
        )

    return {
        "schema_version": "oi-field-reliability-v1",
        "methodology_version": "commercial-v1.0",
        "decision": gate,
        "decision_reason": reason,
        "metrics": metrics,
        "thresholds": thresholds or {},
        "threshold_results": threshold_results,
        "disagreements": disagreements,
        "governance_boundaries": [
            "This result evaluates inter-rater reliability only.",
            "It does not alter approved scores or authorize publication or implementation.",
            "Methodology changes require separate evidence, review, and DecisionLedger approval.",
        ],
    }


def _threshold(value: str) -> tuple[str, float]:
    try:
        key, raw = value.split("=", 1)
        minimum = float(raw)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("use metric=0.00") from exc
    if key not in THRESHOLD_KEYS:
        raise argparse.ArgumentTypeError(
            f"unsupported metric '{key}'; choose from {sorted(THRESHOLD_KEYS)}"
        )
    if not 0.0 <= minimum <= 1.0:
        raise argparse.ArgumentTypeError("threshold must be between 0 and 1")
    return key, minimum


def _self_test() -> None:
    rows = [
        {"criterion_id": "OI-WEB-001", "category": "website", "evaluator_id": "A", "state": "scored", "score": "75"},
        {"criterion_id": "OI-WEB-001", "category": "website", "evaluator_id": "B", "state": "scored", "score": "75"},
        {"criterion_id": "OI-SOC-001", "category": "social", "evaluator_id": "A", "state": "unknown", "score": ""},
        {"criterion_id": "OI-SOC-001", "category": "social", "evaluator_id": "B", "state": "unknown", "score": ""},
    ]
    result = evaluate(read_ratings(rows), {"exact_agreement": 1.0, "state_agreement": 1.0})
    assert result["decision"] == "ALLOW"
    assert result["metrics"]["exact_agreement"] == 1.0
    assert result["metrics"]["state_agreement"] == 1.0

    disagreement_rows = [dict(row) for row in rows]
    disagreement_rows[1]["score"] = "25"
    result = evaluate(read_ratings(disagreement_rows))
    assert result["decision"] == "REVIEW"
    assert result["metrics"]["exact_agreement"] == 0.0
    assert result["metrics"]["disagreement_count"] == 1

    invalid_rows = [dict(row) for row in rows]
    invalid_rows[2]["score"] = "0"
    try:
        read_ratings(invalid_rows)
    except ValidationError:
        pass
    else:
        raise AssertionError("unknown state carrying zero was not rejected")

    print("PASS: 3 field-reliability regression cases")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study", nargs="?", type=Path, help="CSV study file")
    parser.add_argument("--threshold", action="append", default=[], type=_threshold)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        _self_test()
        return 0
    if args.study is None:
        parser.error("study CSV is required unless --self-test is used")
    try:
        with args.study.open(newline="", encoding="utf-8") as handle:
            ratings = read_ratings(csv.DictReader(handle))
        result = evaluate(ratings, dict(args.threshold))
    except (OSError, ValidationError) as exc:
        print(
            json.dumps(
                {
                    "schema_version": "oi-field-reliability-v1",
                    "decision": "HALT",
                    "validation_errors": [str(exc)],
                },
                indent=2,
            )
        )
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "ALLOW" else 1


if __name__ == "__main__":
    sys.exit(main())
