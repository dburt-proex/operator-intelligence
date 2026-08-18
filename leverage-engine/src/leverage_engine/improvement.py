from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from .io import load_json
from .paths import CONFIG_DIR, SCHEMA_DIR
from .schema_validation import load_and_validate


SIGNAL_FIELDS = ("friction", "failures", "residual_risks")
LEVERAGE_ORDER = {"high": 0, "medium": 1, "low": 2, "unknown": 3}


def _timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_improvement_patterns(path: Path | None = None) -> dict[str, Any]:
    registry_path = path or (CONFIG_DIR / "improvement-patterns.json")
    document = load_json(registry_path)
    load_and_validate(document, SCHEMA_DIR / "improvement-patterns.schema.json")
    return document


def _explicit_signals(
    receipts: list[dict[str, Any]],
    *,
    generated_at: str,
    project_id: str,
) -> list[dict[str, Any]]:
    cutoff = _timestamp(generated_at)
    signals: list[dict[str, Any]] = []
    for receipt in receipts:
        if receipt.get("project_id") != project_id:
            continue
        if _timestamp(receipt["recorded_at"]) > cutoff:
            continue
        execution_id = receipt["execution_id"]
        for field in SIGNAL_FIELDS:
            for index, statement in enumerate(receipt.get(field, []), 1):
                signals.append(
                    {
                        "source_execution_id": execution_id,
                        "source_field": field,
                        "source_index": index,
                        "statement": statement,
                        "evidence_ref": f"receipt:{execution_id}:{field}:{index}",
                    }
                )
    signals.sort(
        key=lambda item: (
            item["source_execution_id"],
            item["source_field"],
            item["source_index"],
        )
    )
    return signals


def _matches(statement: str, match_any: list[str]) -> bool:
    normalized = statement.casefold()
    return any(token.casefold() in normalized for token in match_any)


def _proposal_id(candidate: dict[str, Any], generated_at: str, project_id: str) -> str:
    basis = {
        "generated_at": generated_at,
        "project_id": project_id,
        "pattern_id": candidate["pattern_id"],
        "source_execution_ids": candidate["source_execution_ids"],
        "evidence_refs": candidate["evidence_refs"],
    }
    digest = hashlib.sha256(
        json.dumps(basis, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:16]
    return f"LE-IMPROVE-{digest}"


def generate_improvement_analysis(
    receipts: list[dict[str, Any]],
    *,
    generated_at: str,
    project_id: str,
    pattern_document: dict[str, Any] | None = None,
    min_distinct_executions: int = 2,
) -> dict[str, Any]:
    """Mine explicit retained friction into a governed improvement proposal.

    v0.1 performs lexical matching against a versioned pattern registry only.
    It does not semantically infer latent problems. A selected proposal always
    requires REVIEW and never carries execution authority.
    """
    if min_distinct_executions < 1:
        raise ValueError("min_distinct_executions must be at least 1")

    registry = pattern_document or load_improvement_patterns()
    load_and_validate(registry, SCHEMA_DIR / "improvement-patterns.schema.json")
    signals = _explicit_signals(
        receipts,
        generated_at=generated_at,
        project_id=project_id,
    )

    candidates: list[dict[str, Any]] = []
    for pattern in registry["patterns"]:
        matched = [item for item in signals if _matches(item["statement"], pattern["match_any"])]
        if not matched:
            continue
        source_execution_ids = sorted({item["source_execution_id"] for item in matched})
        evidence_refs = sorted({item["evidence_ref"] for item in matched})
        candidates.append(
            {
                "pattern_id": pattern["pattern_id"],
                "category": pattern["category"],
                "objective": pattern["objective"],
                "proposed_action": pattern["proposed_action"],
                "expected_leverage": pattern["expected_leverage"],
                "occurrence_count": len(matched),
                "distinct_execution_count": len(source_execution_ids),
                "source_execution_ids": source_execution_ids,
                "evidence_refs": evidence_refs,
                "scope": sorted(set(pattern["scope"])),
                "not_in_scope": sorted(set(pattern["not_in_scope"])),
                "eligible": len(source_execution_ids) >= min_distinct_executions,
            }
        )

    candidates.sort(
        key=lambda item: (
            -item["distinct_execution_count"],
            -item["occurrence_count"],
            LEVERAGE_ORDER[item["expected_leverage"]],
            item["pattern_id"],
        )
    )
    eligible = [item for item in candidates if item["eligible"]]

    if eligible:
        top = eligible[0]
        selected_proposal: dict[str, Any] | None = {
            "proposal_id": _proposal_id(top, generated_at, project_id),
            "pattern_id": top["pattern_id"],
            "category": top["category"],
            "objective": top["objective"],
            "proposed_action": top["proposed_action"],
            "rationale": (
                f"Pattern {top['pattern_id']} matched {top['occurrence_count']} explicit retained signal(s) "
                f"across {top['distinct_execution_count']} distinct execution(s) and ranked first under "
                "recurrence-first deterministic ordering."
            ),
            "expected_leverage": top["expected_leverage"],
            "occurrence_count": top["occurrence_count"],
            "distinct_execution_count": top["distinct_execution_count"],
            "source_execution_ids": top["source_execution_ids"],
            "evidence_refs": top["evidence_refs"],
            "scope": top["scope"],
            "not_in_scope": top["not_in_scope"],
            "required_gate": "REVIEW",
            "execution_authorized": False,
        }
        decision = "PROPOSE"
    else:
        selected_proposal = None
        decision = "NO_ACTION"

    analysis_basis = {
        "generated_at": generated_at,
        "project_id": project_id,
        "registry_version": registry["version"],
        "min_distinct_executions": min_distinct_executions,
        "decision": decision,
        "candidates": candidates,
        "selected_proposal": selected_proposal,
    }
    digest = hashlib.sha256(
        json.dumps(analysis_basis, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:16]
    analysis = {
        "analysis_id": f"LE-IMPA-{digest}",
        "generated_at": generated_at,
        "project_id": project_id,
        "registry_version": registry["version"],
        "min_distinct_executions": min_distinct_executions,
        "decision": decision,
        "candidates": candidates,
        "selected_proposal": selected_proposal,
        "execution_authorized": False,
    }
    load_and_validate(analysis, SCHEMA_DIR / "improvement-analysis.schema.json")
    return analysis
