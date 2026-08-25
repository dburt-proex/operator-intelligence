from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from .experience_items import build_receipt_items
from .io import load_json
from .paths import CONFIG_DIR, SCHEMA_DIR
from .schema_validation import load_and_validate


def _timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_context_relations(path: Path | None = None) -> list[dict[str, Any]]:
    relation_path = path or (CONFIG_DIR / "context-relations.json")
    document = load_json(relation_path)
    load_and_validate(document, SCHEMA_DIR / "context-relations.schema.json")
    return document["relations"]


def _candidate_items(
    receipts: list[dict[str, Any]],
    *,
    project_id: str,
    reuse_scope: list[str],
    retrieved_item_ids: set[str],
) -> list[dict[str, Any]]:
    scopes = set(reuse_scope)
    candidates: list[dict[str, Any]] = []
    for base in build_receipt_items(receipts):
        matched_scope: list[str] = []
        if base["kind"] == "learning":
            matched_scope = sorted(scopes.intersection(base["reuse_scope"]))
        elif base["kind"] == "next_improvement" and base["source_project_id"] == project_id:
            matched_scope = sorted(scopes)

        relevance_basis: list[str] = []
        if matched_scope:
            relevance_basis.append("exact_scope")
        if base["item_id"] in retrieved_item_ids:
            relevance_basis.append("retrieval")

        candidates.append(
            {
                "item_id": base["item_id"],
                "source_execution_id": base["source_execution_id"],
                "source_directive_id": base["source_directive_id"],
                "source_recorded_at": base["source_recorded_at"],
                "source_project_id": base["source_project_id"],
                "kind": base["kind"],
                "statement": base["statement"],
                "evidence_refs": base["evidence_refs"],
                "matched_scope": matched_scope,
                "relevance_basis": sorted(relevance_basis),
            }
        )
    return candidates


def _item_cost(item: dict[str, Any]) -> int:
    return max(
        1,
        len(item["statement"])
        + sum(len(value) for value in item["evidence_refs"])
        + sum(len(value) for value in item["matched_scope"])
        + sum(len(value) for value in item["relevance_basis"]),
    )


def _exclusion(item: dict[str, Any], reason: str, related_item_id: str | None = None) -> dict[str, Any]:
    record = {
        "item_id": item["item_id"],
        "source_execution_id": item["source_execution_id"],
        "reason": reason,
    }
    if related_item_id:
        record["related_item_id"] = related_item_id
    return record


def compile_context_package(
    receipts: list[dict[str, Any]],
    *,
    run_timestamp: str,
    project_id: str,
    reuse_scope: list[str],
    relations: list[dict[str, Any]] | None = None,
    retrieved_item_ids: set[str] | None = None,
    max_items: int = 12,
    max_chars: int = 6000,
    max_age_days: int = 90,
) -> dict[str, Any]:
    """Compile deterministic, bounded, authority-neutral execution context.

    Retrieval is only an additional relevance basis. Every retrieved item still
    passes the compiler's future, freshness, relation, provenance, and budget
    controls. Historical approvals, permissions, policies, and gates are never
    projected into the package.
    """
    if max_items < 0 or max_chars < 0 or max_age_days < 0:
        raise ValueError("context budgets must be non-negative")

    cutoff = _timestamp(run_timestamp)
    stale_before = cutoff - timedelta(days=max_age_days)
    relation_records = relations if relations is not None else load_context_relations()
    retrieval_ids = set(retrieved_item_ids or set())
    candidates = _candidate_items(
        receipts,
        project_id=project_id,
        reuse_scope=reuse_scope,
        retrieved_item_ids=retrieval_ids,
    )

    eligible: dict[str, dict[str, Any]] = {}
    excluded: dict[str, dict[str, Any]] = {}

    for item in candidates:
        recorded_at = _timestamp(item["source_recorded_at"])
        if recorded_at > cutoff:
            excluded[item["item_id"]] = _exclusion(item, "future")
        elif recorded_at < stale_before:
            excluded[item["item_id"]] = _exclusion(item, "stale")
        elif not item["relevance_basis"]:
            excluded[item["item_id"]] = _exclusion(item, "unrelated")
        else:
            eligible[item["item_id"]] = item

    active_relations = [
        relation
        for relation in relation_records
        if _timestamp(relation["recorded_at"]) <= cutoff
    ]
    active_relations.sort(key=lambda item: (item["recorded_at"], item["relation_id"]))

    for relation in active_relations:
        source_id = relation["source_item_id"]
        target_id = relation["target_item_id"]
        if relation["relation_type"] == "invalidates" and target_id in eligible:
            excluded[target_id] = _exclusion(eligible[target_id], "invalidated", source_id)
            eligible.pop(target_id, None)
        elif relation["relation_type"] == "supersedes" and source_id in eligible and target_id in eligible:
            excluded[target_id] = _exclusion(eligible[target_id], "superseded", source_id)
            eligible.pop(target_id, None)

    for relation in active_relations:
        if relation["relation_type"] != "contradicts":
            continue
        source_id = relation["source_item_id"]
        target_id = relation["target_item_id"]
        if source_id in eligible and target_id in eligible:
            source = eligible.pop(source_id)
            target = eligible.pop(target_id)
            excluded[source_id] = _exclusion(source, "unresolved_contradiction", target_id)
            excluded[target_id] = _exclusion(target, "unresolved_contradiction", source_id)

    kind_priority = {
        "next_improvement": 0,
        "learning": 1,
        "failure": 2,
        "residual_risk": 3,
        "friction": 4,
        "decision_ref": 5,
        "evidence_ref": 6,
    }
    ordered = sorted(
        eligible.values(),
        key=lambda item: (
            kind_priority[item["kind"]],
            -_timestamp(item["source_recorded_at"]).timestamp(),
            item["item_id"],
        ),
    )

    included: list[dict[str, Any]] = []
    used_chars = 0
    for item in ordered:
        cost = _item_cost(item)
        if len(included) >= max_items:
            excluded[item["item_id"]] = _exclusion(item, "item_budget")
            continue
        if used_chars + cost > max_chars:
            excluded[item["item_id"]] = _exclusion(item, "character_budget")
            continue
        admitted = dict(item)
        admitted["cost_chars"] = cost
        included.append(admitted)
        used_chars += cost

    excluded_records = sorted(
        excluded.values(),
        key=lambda item: (item["source_execution_id"], item["item_id"], item["reason"]),
    )
    source_receipts = sorted({item["source_execution_id"] for item in included})
    normalized_scope = sorted(set(reuse_scope))
    basis = {
        "run_timestamp": run_timestamp,
        "project_id": project_id,
        "reuse_scope": normalized_scope,
        "budget": {
            "max_items": max_items,
            "max_chars": max_chars,
            "max_age_days": max_age_days,
        },
        "included": included,
        "excluded": excluded_records,
    }
    digest = hashlib.sha256(
        json.dumps(basis, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:16]
    package = {
        "context_id": f"LE-CTX-{digest}",
        "run_timestamp": run_timestamp,
        "project_id": project_id,
        "reuse_scope": normalized_scope,
        "budget": {
            "max_items": max_items,
            "max_chars": max_chars,
            "max_age_days": max_age_days,
            "used_items": len(included),
            "used_chars": used_chars,
        },
        "included": included,
        "excluded": excluded_records,
        "source_receipts": source_receipts,
        "authority_neutral": True,
    }
    load_and_validate(package, SCHEMA_DIR / "context-package.schema.json")
    return package
