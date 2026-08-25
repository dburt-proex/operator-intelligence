from __future__ import annotations

from typing import Any


def _receipt_pointer(execution_id: str, field: str, index: int) -> str:
    return f"receipt:{execution_id}:{field}:{index}"


def build_receipt_items(receipts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Project validated receipts into authority-neutral candidate items.

    This function creates candidate representations only. It never carries gate,
    approval, permission, or policy state into a candidate item.
    """
    items: list[dict[str, Any]] = []
    for receipt in receipts:
        execution_id = receipt["execution_id"]
        common = {
            "source_execution_id": execution_id,
            "source_directive_id": receipt["directive_id"],
            "source_recorded_at": receipt["recorded_at"],
            "source_project_id": receipt["project_id"],
        }

        for index, learning in enumerate(receipt.get("reusable_learnings", []), 1):
            items.append(
                {
                    **common,
                    "item_id": f"{execution_id}:learning:{index}",
                    "kind": "learning",
                    "statement": learning["learning"],
                    "evidence_refs": sorted(set(learning["evidence_refs"])),
                    "reuse_scope": sorted(set(learning["reuse_scope"])),
                }
            )

        next_improvement = receipt.get("next_improvement")
        if next_improvement:
            items.append(
                {
                    **common,
                    "item_id": f"{execution_id}:next_improvement:1",
                    "kind": "next_improvement",
                    "statement": next_improvement["objective"],
                    "evidence_refs": sorted(set(next_improvement["evidence_refs"])),
                    "reuse_scope": [],
                }
            )

        for field, kind in (
            ("failures", "failure"),
            ("friction", "friction"),
            ("residual_risks", "residual_risk"),
        ):
            for index, statement in enumerate(receipt.get(field, []), 1):
                pointer = _receipt_pointer(execution_id, field, index)
                items.append(
                    {
                        **common,
                        "item_id": f"{execution_id}:{kind}:{index}",
                        "kind": kind,
                        "statement": statement,
                        "evidence_refs": [pointer],
                        "reuse_scope": [],
                    }
                )

        for field, kind in (
            ("evidence_refs", "evidence_ref"),
            ("decision_refs", "decision_ref"),
        ):
            for index, ref in enumerate(receipt.get(field, []), 1):
                items.append(
                    {
                        **common,
                        "item_id": f"{execution_id}:{kind}:{index}",
                        "kind": kind,
                        "statement": ref,
                        "evidence_refs": [ref],
                        "reuse_scope": [],
                    }
                )

    items.sort(key=lambda item: item["item_id"])
    return items
