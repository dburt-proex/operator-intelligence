#!/usr/bin/env python3
"""Validate a governed Operator Intelligence field-reliability study.

The validator admits a versioned study manifest and an exact five-column ratings
CSV, then measures inter-rater agreement without mutating assessment scores.
It is a FR-001 contract control, not a field-reliability claim, publication
decision, scoring-method change, or implementation authorization.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
CRITERIA_LIBRARY = ROOT / "scoring" / "criteria-library.md"
ANCHORS = (0, 25, 50, 75, 100)
STATES = {"scored", "unknown", "blocked", "not_applicable"}
CSV_FIELDS = ("criterion_id", "category", "evaluator_id", "state", "score")
THRESHOLD_KEYS = {"exact_agreement", "adjacent_agreement", "state_agreement", "weighted_kappa"}
MANIFEST_FIELDS = {
    "schema_version", "study_id", "record_class", "protocol_version", "methodology_version",
    "criteria_version", "calculator_version", "weight_profile", "scope_ref", "evidence_snapshot_ref",
    "evidence_snapshot_sha256", "ratings_sha256", "blinding_status", "evaluator_count", "evaluator_ids",
    "independence_attestation_ref", "authority_ref", "retention_class", "retention_rule_ref",
    "threshold_profile", "reviewer_id", "decision_authority", "created_at",
}
THRESHOLD_PROFILE_FIELDS = {"profile_id", "version", "approved_by", "decision_authority", "metrics"}
RECORD_CLASSES = {"synthetic_contract_fixture", "human_field_study"}
CATEGORY_BY_PREFIX = {
    "WEB": "website", "MSG": "messaging_and_offer", "OFFER": "messaging_and_offer",
    "CONV": "conversion", "SEO": "seo", "GBP": "gbp", "TRUST": "trust", "SOC": "social",
    "AUTO": "automation", "AI": "ai_readiness", "AN": "analytics", "COMP": "competitive",
}
CRITERION_RE = re.compile(r"^OI-([A-Z]+)-\d{3}$")
STUDY_ID_RE = re.compile(r"^OI-FR-\d{4}-\d{3}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class ValidationError(ValueError):
    """Raised when a study cannot be admitted for reliability analysis."""


@dataclass(frozen=True)
class Rating:
    criterion_id: str
    category: str
    evaluator_id: str
    state: str
    score: int | None


def _require_string(data: dict[str, object], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"manifest: {key} must be a non-empty string")
    return value.strip()


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_criteria() -> set[str]:
    try:
        content = CRITERIA_LIBRARY.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValidationError(f"criteria library cannot be read: {exc}") from exc
    criteria = set(re.findall(r"\| (OI-[A-Z]+-\d{3}) \|", content))
    if not criteria:
        raise ValidationError("criteria library contains no canonical criterion IDs")
    return criteria


def _parse_score(raw: str, state: str, row_number: int) -> int | None:
    value = raw.strip()
    if state != "scored":
        if value:
            raise ValidationError(f"row {row_number}: state '{state}' must not carry a numeric score")
        return None
    if not value:
        raise ValidationError(f"row {row_number}: scored state requires a score")
    try:
        score = int(value)
    except ValueError as exc:
        raise ValidationError(f"row {row_number}: score must be an integer") from exc
    if score not in ANCHORS:
        raise ValidationError(f"row {row_number}: score {score} is outside approved anchors {ANCHORS}")
    return score


def read_ratings(rows: Iterable[dict[str, str]]) -> list[Rating]:
    ratings: list[Rating] = []
    seen: set[tuple[str, str]] = set()
    canonical = canonical_criteria()
    for row_number, row in enumerate(rows, start=2):
        if set(row) != set(CSV_FIELDS):
            raise ValidationError(f"row {row_number}: CSV fields must be exactly {list(CSV_FIELDS)}")
        criterion_id = row["criterion_id"].strip()
        category = row["category"].strip()
        evaluator_id = row["evaluator_id"].strip()
        state = row["state"].strip()
        if not criterion_id or not category or not evaluator_id:
            raise ValidationError(f"row {row_number}: criterion_id, category, and evaluator_id are required")
        match = CRITERION_RE.fullmatch(criterion_id)
        if not match or criterion_id not in canonical:
            raise ValidationError(f"row {row_number}: unknown canonical criterion '{criterion_id}'")
        expected_category = CATEGORY_BY_PREFIX.get(match.group(1))
        if category != expected_category:
            raise ValidationError(f"row {row_number}: category '{category}' does not match {criterion_id} ({expected_category})")
        if state not in STATES:
            raise ValidationError(f"row {row_number}: unsupported state '{state}'")
        key = (criterion_id, evaluator_id)
        if key in seen:
            raise ValidationError(f"row {row_number}: duplicate rating for {criterion_id}/{evaluator_id}")
        seen.add(key)
        ratings.append(Rating(criterion_id, category, evaluator_id, state, _parse_score(row["score"], state, row_number)))
    if not ratings:
        raise ValidationError("study contains no rating rows")
    return ratings


def read_ratings_csv(path: Path) -> list[Rating]:
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != list(CSV_FIELDS):
                raise ValidationError(f"CSV header must be exactly {list(CSV_FIELDS)}; got {reader.fieldnames}")
            return read_ratings(reader)
    except OSError as exc:
        raise ValidationError(f"study CSV cannot be read: {exc}") from exc


def load_manifest(path: Path, ratings_path: Path, ratings: list[Rating]) -> dict[str, object]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"manifest cannot be loaded: {exc}") from exc
    if not isinstance(data, dict) or set(data) != MANIFEST_FIELDS:
        unexpected = sorted(set(data) - MANIFEST_FIELDS) if isinstance(data, dict) else []
        missing = sorted(MANIFEST_FIELDS - set(data)) if isinstance(data, dict) else sorted(MANIFEST_FIELDS)
        raise ValidationError(f"manifest fields must be exact; missing={missing}, unexpected={unexpected}")
    if data["schema_version"] != "oi-field-reliability-study-v1":
        raise ValidationError("manifest: unsupported schema_version")
    study_id = _require_string(data, "study_id")
    if not STUDY_ID_RE.fullmatch(study_id):
        raise ValidationError("manifest: study_id must match OI-FR-YYYY-NNN")
    record_class = data["record_class"]
    if record_class not in RECORD_CLASSES:
        raise ValidationError("manifest: record_class is unsupported")
    for key in ("protocol_version", "methodology_version", "criteria_version", "calculator_version", "weight_profile", "scope_ref", "evidence_snapshot_ref", "independence_attestation_ref", "authority_ref", "retention_class", "retention_rule_ref", "reviewer_id", "decision_authority"):
        _require_string(data, key)
    for key in ("evidence_snapshot_sha256", "ratings_sha256"):
        value = _require_string(data, key)
        if not SHA256_RE.fullmatch(value):
            raise ValidationError(f"manifest: {key} must be a lowercase SHA-256 hex digest")
    if data["ratings_sha256"] != _sha256(ratings_path):
        raise ValidationError("manifest: ratings_sha256 does not match the supplied CSV")
    if data["blinding_status"] not in {"blinded", "not_blinded"}:
        raise ValidationError("manifest: blinding_status must be blinded or not_blinded")
    if record_class == "human_field_study" and data["blinding_status"] != "blinded":
        raise ValidationError("manifest: human_field_study requires blinded status")
    evaluator_ids = data["evaluator_ids"]
    if not isinstance(evaluator_ids, list) or len(evaluator_ids) < 2:
        raise ValidationError("manifest: evaluator_ids must contain at least two opaque IDs")
    if any(not isinstance(item, str) or not item.strip() for item in evaluator_ids):
        raise ValidationError("manifest: evaluator_ids must contain non-empty strings")
    evaluator_set = {item.strip() for item in evaluator_ids}
    if len(evaluator_set) != len(evaluator_ids):
        raise ValidationError("manifest: evaluator_ids must be unique")
    if not isinstance(data["evaluator_count"], int) or data["evaluator_count"] != len(evaluator_set):
        raise ValidationError("manifest: evaluator_count must equal unique evaluator_ids")
    if evaluator_set != {rating.evaluator_id for rating in ratings}:
        raise ValidationError("manifest: evaluator_ids must exactly match the CSV evaluator IDs")
    try:
        created_at = datetime.fromisoformat(_require_string(data, "created_at").replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError("manifest: created_at must be an ISO-8601 timestamp") from exc
    if created_at.tzinfo is None:
        raise ValidationError("manifest: created_at must include a timezone")
    profile = data["threshold_profile"]
    if not isinstance(profile, dict) or set(profile) != THRESHOLD_PROFILE_FIELDS:
        raise ValidationError("manifest: threshold_profile fields must be exact")
    for key in ("profile_id", "version", "approved_by", "decision_authority"):
        _require_string(profile, key)
    metrics = profile["metrics"]
    if not isinstance(metrics, dict) or not metrics:
        raise ValidationError("manifest: threshold_profile.metrics must be a non-empty object")
    if not set(metrics).issubset(THRESHOLD_KEYS):
        raise ValidationError("manifest: threshold_profile.metrics contains unsupported metric")
    for key, value in metrics.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 1:
            raise ValidationError(f"manifest: threshold {key} must be a number between 0 and 1")
    if record_class == "human_field_study" and not ({"exact_agreement", "adjacent_agreement"} & set(metrics)):
        raise ValidationError("manifest: human_field_study threshold profile must include exact_agreement or adjacent_agreement")
    return data


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
    observed_disagreement = expected_disagreement = 0.0
    denominator = float((size - 1) ** 2)
    for i in range(size):
        for j in range(size):
            weight = ((i - j) ** 2) / denominator
            observed_disagreement += weight * (observed[i][j] / count)
            expected_disagreement += weight * ((left[i] * right[j]) / (count * count))
    if math.isclose(expected_disagreement, 0.0):
        return 1.0 if math.isclose(observed_disagreement, 0.0) else None
    return 1.0 - (observed_disagreement / expected_disagreement)


def evaluate(ratings: list[Rating], manifest: dict[str, object] | None = None) -> dict[str, object]:
    by_criterion: dict[str, list[Rating]] = defaultdict(list)
    category_by_criterion: dict[str, str] = {}
    evaluators: set[str] = set()
    for rating in ratings:
        previous = category_by_criterion.setdefault(rating.criterion_id, rating.category)
        if previous != rating.category:
            raise ValidationError(f"criterion {rating.criterion_id} has conflicting categories")
        by_criterion[rating.criterion_id].append(rating)
        evaluators.add(rating.evaluator_id)
    if len(evaluators) < 2:
        raise ValidationError("at least two evaluator IDs are required")
    score_pairs: list[tuple[int, int]] = []
    state_pair_count = state_match_count = 0
    disagreements: list[dict[str, object]] = []
    category_deltas: dict[str, list[int]] = defaultdict(list)
    for criterion_id, criterion_ratings in sorted(by_criterion.items()):
        if len(criterion_ratings) < 2:
            disagreements.append({"criterion_id": criterion_id, "category": category_by_criterion[criterion_id], "type": "missing_peer_rating"})
            continue
        ordered = sorted(criterion_ratings, key=lambda item: item.evaluator_id)
        for left_index, left in enumerate(ordered):
            for right in ordered[left_index + 1 :]:
                state_pair_count += 1
                if left.state == right.state:
                    state_match_count += 1
                else:
                    disagreements.append({"criterion_id": criterion_id, "category": left.category, "type": "state_disagreement", "evaluators": [left.evaluator_id, right.evaluator_id], "values": [left.state, right.state]})
                if left.score is not None and right.score is not None:
                    score_pairs.append((left.score, right.score))
                    delta = abs(left.score - right.score)
                    category_deltas[left.category].append(delta)
                    if delta > 25:
                        disagreements.append({"criterion_id": criterion_id, "category": left.category, "type": "substantive_score_disagreement", "evaluators": [left.evaluator_id, right.evaluator_id], "values": [left.score, right.score], "delta": delta})
    if state_pair_count == 0:
        raise ValidationError("no evaluator pairs were available")
    metrics = {
        "criterion_count": len(by_criterion), "evaluator_count": len(evaluators), "state_pair_count": state_pair_count,
        "scored_pair_count": len(score_pairs), "state_agreement": state_match_count / state_pair_count,
        "exact_agreement": sum(first == second for first, second in score_pairs) / len(score_pairs) if score_pairs else None,
        "adjacent_agreement": sum(abs(first - second) <= 25 for first, second in score_pairs) / len(score_pairs) if score_pairs else None,
        "weighted_kappa": _quadratic_weighted_kappa(score_pairs),
        "category_mean_absolute_delta": {category: sum(deltas) / len(deltas) for category, deltas in sorted(category_deltas.items())},
        "disagreement_count": len(disagreements),
    }
    thresholds: dict[str, float] = dict(manifest["threshold_profile"]["metrics"]) if manifest else {}
    record_class = str(manifest["record_class"]) if manifest else "self_test"
    threshold_results = {key: metrics[key] is not None and float(metrics[key]) >= minimum for key, minimum in sorted(thresholds.items())}
    if record_class == "synthetic_contract_fixture":
        gate, reason = "REVIEW", "synthetic contract fixture validates structure only and cannot establish field reliability"
    elif not thresholds:
        gate, reason = "REVIEW", "reviewer-approved reliability thresholds are required before acceptance"
    elif metrics["scored_pair_count"] == 0:
        gate, reason = "REVIEW", "no scored evaluator pairs are available for score-agreement acceptance"
    elif all(threshold_results.values()):
        gate, reason = "ALLOW", "all reviewer-approved reliability thresholds passed"
    else:
        gate, reason = "REVIEW", "one or more reviewer-approved reliability thresholds did not pass"
    return {
        "schema_version": "oi-field-reliability-analysis-v1", "methodology_version": manifest["methodology_version"] if manifest else "commercial-v1.0",
        "record_class": record_class, "decision": gate, "decision_reason": reason, "metrics": metrics,
        "thresholds": thresholds, "threshold_results": threshold_results, "disagreements": disagreements,
        "governance_boundaries": [
            "This result evaluates inter-rater reliability only.",
            "It does not alter approved scores or authorize publication or implementation.",
            "Human evaluator independence is attested by a separately controlled authority record; this validator does not prove identity or independence.",
            "Methodology changes require separate evidence, review, and DecisionLedger approval.",
        ],
    }


def _self_test() -> None:
    rows = [
        {"criterion_id": "OI-WEB-001", "category": "website", "evaluator_id": "EV-A", "state": "scored", "score": "75"},
        {"criterion_id": "OI-WEB-001", "category": "website", "evaluator_id": "EV-B", "state": "scored", "score": "75"},
        {"criterion_id": "OI-SOC-001", "category": "social", "evaluator_id": "EV-A", "state": "unknown", "score": ""},
        {"criterion_id": "OI-SOC-001", "category": "social", "evaluator_id": "EV-B", "state": "unknown", "score": ""},
    ]
    result = evaluate(read_ratings(rows))
    assert result["decision"] == "REVIEW"
    assert result["metrics"]["exact_agreement"] == 1.0
    invalid_rows = [dict(row) for row in rows]
    invalid_rows[2]["score"] = "0"
    try:
        read_ratings(invalid_rows)
    except ValidationError:
        pass
    else:
        raise AssertionError("unknown state carrying zero was not rejected")
    print("PASS: 2 field-reliability regression cases")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study", nargs="?", type=Path, help="five-column ratings CSV")
    parser.add_argument("--study-manifest", type=Path, help="versioned study manifest JSON")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        _self_test()
        return 0
    if args.study is None or args.study_manifest is None:
        parser.error("study CSV and --study-manifest are both required unless --self-test is used")
    try:
        ratings = read_ratings_csv(args.study)
        manifest = load_manifest(args.study_manifest, args.study, ratings)
        result = evaluate(ratings, manifest)
    except ValidationError as exc:
        print(json.dumps({"schema_version": "oi-field-reliability-analysis-v1", "decision": "HALT", "validation_errors": [str(exc)]}, indent=2))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "ALLOW" else 1


if __name__ == "__main__":
    sys.exit(main())
