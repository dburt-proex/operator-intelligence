#!/usr/bin/env python3
"""Validate Leverage Engine execution receipts without third-party packages.

This is intentionally narrow. The JSON Schema remains the canonical contract; this
helper enforces the Phase 1 invariants needed in local/CI environments that do not
install a general JSON Schema implementation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

EXECUTION_ID_RE = re.compile(r"^LE-EXEC-[0-9]{4}-[0-9]{4}$")
DIRECTIVE_ID_RE = re.compile(r"^LD-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{3}$")
COMPLETION_STATES = {"completed", "partial", "blocked", "failed", "abandoned"}
GATES = {"ALLOW", "REVIEW", "HALT"}
VALIDATION_RESULTS = {"pass", "fail", "partial", "not_run"}
ACTION_RESULTS = {"completed", "partial", "blocked", "failed", "skipped"}
ACTOR_TYPES = {"human", "agent", "hybrid"}


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any, *, allow_empty: bool = True) -> bool:
    if not isinstance(value, list):
        return False
    if not allow_empty and not value:
        return False
    if not all(_nonempty_string(item) for item in value):
        return False
    return len(value) == len(set(value))


def validate_receipt(receipt: Any, schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if not isinstance(receipt, dict):
        return ["receipt must be a JSON object"]

    required = schema.get("required", [])
    for field in required:
        if field not in receipt:
            errors.append(f"missing required field: {field}")

    allowed = set(schema.get("properties", {}))
    extras = sorted(set(receipt) - allowed)
    if extras:
        errors.append(f"unexpected field(s): {', '.join(extras)}")

    execution_id = receipt.get("execution_id")
    if not _nonempty_string(execution_id) or not EXECUTION_ID_RE.fullmatch(execution_id):
        errors.append("execution_id must match LE-EXEC-YYYY-NNNN")

    directive_id = receipt.get("directive_id")
    if not _nonempty_string(directive_id) or not DIRECTIVE_ID_RE.fullmatch(directive_id):
        errors.append("directive_id must match LD-YYYY-MM-DD-NNN")

    for field in ("project_id", "started_at", "ended_at", "recorded_at"):
        if not _nonempty_string(receipt.get(field)):
            errors.append(f"{field} must be a non-empty string")

    executor = receipt.get("executor")
    if not isinstance(executor, dict):
        errors.append("executor must be an object")
    else:
        expected = {"actor_type", "actor_id", "agent", "model"}
        missing = expected - set(executor)
        extra = set(executor) - expected
        if missing:
            errors.append(f"executor missing field(s): {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"executor unexpected field(s): {', '.join(sorted(extra))}")
        if executor.get("actor_type") not in ACTOR_TYPES:
            errors.append("executor.actor_type is invalid")
        for field in ("actor_id", "agent", "model"):
            if not _nonempty_string(executor.get(field)):
                errors.append(f"executor.{field} must be a non-empty string")

    for field in (
        "context_refs",
        "evidence_refs",
        "decision_refs",
        "tools",
        "failures",
        "friction",
        "residual_risks",
        "completion_evidence",
        "gate_reasons",
    ):
        if not _string_list(receipt.get(field)):
            errors.append(f"{field} must be an array of unique non-empty strings")

    actions = receipt.get("actions")
    if not isinstance(actions, list) or not actions:
        errors.append("actions must contain at least one action")
    else:
        sequences: list[int] = []
        for index, action in enumerate(actions):
            if not isinstance(action, dict):
                errors.append(f"actions[{index}] must be an object")
                continue
            if not isinstance(action.get("sequence"), int) or action["sequence"] < 1:
                errors.append(f"actions[{index}].sequence must be a positive integer")
            else:
                sequences.append(action["sequence"])
            if not _nonempty_string(action.get("action")):
                errors.append(f"actions[{index}].action must be non-empty")
            if action.get("result") not in ACTION_RESULTS:
                errors.append(f"actions[{index}].result is invalid")
            if "evidence_refs" in action and not _string_list(action.get("evidence_refs")):
                errors.append(f"actions[{index}].evidence_refs is invalid")
        if sequences and sequences != list(range(1, len(sequences) + 1)):
            errors.append("actions.sequence must be contiguous and ordered starting at 1")

    validation = receipt.get("validation")
    if not isinstance(validation, list) or not validation:
        errors.append("validation must contain at least one validation record")
    else:
        for index, check in enumerate(validation):
            if not isinstance(check, dict):
                errors.append(f"validation[{index}] must be an object")
                continue
            for field in ("validator", "scope"):
                if not _nonempty_string(check.get(field)):
                    errors.append(f"validation[{index}].{field} must be non-empty")
            if check.get("result") not in VALIDATION_RESULTS:
                errors.append(f"validation[{index}].result is invalid")
            if not _string_list(check.get("evidence_refs")):
                errors.append(f"validation[{index}].evidence_refs is invalid")

    for field in ("operator_interventions", "review_events", "changes", "reusable_learnings"):
        if not isinstance(receipt.get(field), list):
            errors.append(f"{field} must be an array")

    for index, learning in enumerate(receipt.get("reusable_learnings", [])):
        if not isinstance(learning, dict):
            errors.append(f"reusable_learnings[{index}] must be an object")
            continue
        if not _nonempty_string(learning.get("learning")):
            errors.append(f"reusable_learnings[{index}].learning must be non-empty")
        if not _string_list(learning.get("evidence_refs")):
            errors.append(f"reusable_learnings[{index}].evidence_refs is invalid")
        if not _string_list(learning.get("reuse_scope"), allow_empty=False):
            errors.append(f"reusable_learnings[{index}].reuse_scope must be non-empty")

    completion_status = receipt.get("completion_status")
    if completion_status not in COMPLETION_STATES:
        errors.append("completion_status is invalid")

    gate_result = receipt.get("gate_result")
    if gate_result not in GATES:
        errors.append("gate_result is invalid")

    if completion_status == "completed":
        if not receipt.get("completion_evidence"):
            errors.append("completed receipts require at least one completion_evidence reference")
        if not any(
            isinstance(check, dict) and check.get("result") == "pass"
            for check in receipt.get("validation", [])
        ):
            errors.append("completed receipts require at least one passing validation record")

    if gate_result == "HALT" and completion_status == "completed":
        errors.append("HALT receipts cannot be marked completed")

    next_improvement = receipt.get("next_improvement")
    if next_improvement is not None:
        if not isinstance(next_improvement, dict):
            errors.append("next_improvement must be null or an object")
        else:
            expected = {"objective", "rationale", "evidence_refs", "expected_leverage", "requires_review"}
            missing = expected - set(next_improvement)
            extra = set(next_improvement) - expected
            if missing:
                errors.append(f"next_improvement missing field(s): {', '.join(sorted(missing))}")
            if extra:
                errors.append(f"next_improvement unexpected field(s): {', '.join(sorted(extra))}")
            for field in ("objective", "rationale"):
                if not _nonempty_string(next_improvement.get(field)):
                    errors.append(f"next_improvement.{field} must be non-empty")
            if not _string_list(next_improvement.get("evidence_refs")):
                errors.append("next_improvement.evidence_refs is invalid")
            if next_improvement.get("expected_leverage") not in {"low", "medium", "high", "unknown"}:
                errors.append("next_improvement.expected_leverage is invalid")
            if not isinstance(next_improvement.get("requires_review"), bool):
                errors.append("next_improvement.requires_review must be boolean")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Leverage Engine execution receipt")
    parser.add_argument("receipt", type=Path)
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schemas" / "execution-receipt.schema.json",
    )
    parser.add_argument(
        "--expect-invalid",
        action="store_true",
        help="succeed only when the supplied receipt is invalid",
    )
    args = parser.parse_args()

    try:
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors = validate_receipt(receipt, schema)

    if args.expect_invalid:
        if errors:
            print("EXPECTED_INVALID")
            for error in errors:
                print(f"- {error}")
            return 0
        print("ERROR: receipt unexpectedly validated", file=sys.stderr)
        return 1

    if errors:
        print("INVALID", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
