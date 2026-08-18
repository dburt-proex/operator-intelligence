from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from .io import load_json
from .paths import RECEIPT_DIR, SCHEMA_DIR
from .schema_validation import load_and_validate


def _timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_validated_receipts(receipt_dir: Path = RECEIPT_DIR) -> list[dict[str, Any]]:
    """Load retained execution receipts in stable order and validate every record."""
    if not receipt_dir.exists():
        return []
    schema_path = SCHEMA_DIR / "execution-receipt.schema.json"
    receipts: list[dict[str, Any]] = []
    for path in sorted(receipt_dir.glob("LE-EXEC-*.json")):
        receipt = load_json(path)
        load_and_validate(receipt, schema_path)
        receipts.append(receipt)
    return receipts


def compile_experience_context(
    receipts: list[dict[str, Any]],
    *,
    run_timestamp: str,
    project_id: str,
    reuse_scope: list[str],
) -> list[dict[str, Any]]:
    """Project only relevant, evidence-backed prior experience into a later run.

    The projection is deliberately authority-neutral: gate results, permissions,
    policy state, and approval state are not propagated from prior receipts.
    """
    scopes = set(reuse_scope)
    if not scopes:
        return []

    cutoff = _timestamp(run_timestamp)
    projected: list[dict[str, Any]] = []

    for receipt in receipts:
        if _timestamp(receipt["recorded_at"]) > cutoff:
            continue

        for learning in receipt.get("reusable_learnings", []):
            matched_scope = sorted(scopes.intersection(learning["reuse_scope"]))
            if not matched_scope:
                continue
            projected.append(
                {
                    "source_execution_id": receipt["execution_id"],
                    "source_directive_id": receipt["directive_id"],
                    "kind": "learning",
                    "statement": learning["learning"],
                    "evidence_refs": sorted(set(learning["evidence_refs"])),
                    "matched_scope": matched_scope,
                }
            )

        next_improvement = receipt.get("next_improvement")
        if next_improvement and receipt["project_id"] == project_id:
            projected.append(
                {
                    "source_execution_id": receipt["execution_id"],
                    "source_directive_id": receipt["directive_id"],
                    "kind": "next_improvement",
                    "statement": next_improvement["objective"],
                    "evidence_refs": sorted(set(next_improvement["evidence_refs"])),
                    "matched_scope": sorted(scopes),
                }
            )

    projected.sort(
        key=lambda item: (
            item["source_execution_id"],
            item["kind"],
            item["statement"],
        )
    )
    return projected
