from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from typing import Any

from .experience_items import build_receipt_items
from .paths import SCHEMA_DIR
from .schema_validation import load_and_validate

_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_-]+")
_STOPWORDS = {
    "the", "and", "for", "with", "from", "that", "this", "into", "only",
    "then", "than", "have", "has", "had", "was", "were", "are", "but",
    "not", "can", "may", "must", "should", "would", "could", "our", "its",
    "use", "using", "used", "add", "make", "without", "before", "after",
}


def _timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def tokenize(value: str) -> list[str]:
    return sorted(
        {
            token
            for token in _TOKEN_RE.findall(value.lower())
            if len(token) >= 3 and token not in _STOPWORDS
        }
    )


def _search_tokens(item: dict[str, Any]) -> set[str]:
    values = [
        item["statement"],
        item["kind"],
        item["source_project_id"],
        *item["evidence_refs"],
    ]
    tokens: set[str] = set()
    for value in values:
        tokens.update(tokenize(value))
    return tokens


def retrieve_candidates(
    receipts: list[dict[str, Any]],
    *,
    run_timestamp: str,
    project_id: str,
    query: str,
    relations: list[dict[str, Any]] | None = None,
    max_candidates: int = 24,
) -> dict[str, Any]:
    """Propose bounded receipt items; never admit context or authorize execution.

    v0.1 is deliberately deterministic: lexical token overlap seeds candidates,
    then active context relations may add one-hop graph neighbors. The Context
    Compiler remains the only admission boundary.
    """
    if max_candidates < 0:
        raise ValueError("max_candidates must be non-negative")
    query_tokens = tokenize(query)
    if not query_tokens:
        raise ValueError("retrieval query must contain at least one meaningful token")

    cutoff = _timestamp(run_timestamp)
    items = [
        item
        for item in build_receipt_items(receipts)
        if item["source_project_id"] == project_id
        and _timestamp(item["source_recorded_at"]) <= cutoff
    ]
    by_id = {item["item_id"]: item for item in items}

    proposed: dict[str, dict[str, Any]] = {}
    for item in items:
        matched = sorted(set(query_tokens).intersection(_search_tokens(item)))
        if not matched:
            continue
        proposed[item["item_id"]] = {
            "item_id": item["item_id"],
            "source_execution_id": item["source_execution_id"],
            "source_recorded_at": item["source_recorded_at"],
            "kind": item["kind"],
            "statement": item["statement"],
            "evidence_refs": item["evidence_refs"],
            "match_type": "lexical",
            "matched_tokens": matched,
            "match_score": len(matched),
        }

    seed_ids = set(proposed)
    active_relations = sorted(
        [
            relation
            for relation in (relations or [])
            if _timestamp(relation["recorded_at"]) <= cutoff
        ],
        key=lambda relation: (relation["recorded_at"], relation["relation_id"]),
    )
    for relation in active_relations:
        source_id = relation["source_item_id"]
        target_id = relation["target_item_id"]
        if source_id in seed_ids and target_id in by_id and target_id not in proposed:
            neighbor_id, seed_id = target_id, source_id
        elif target_id in seed_ids and source_id in by_id and source_id not in proposed:
            neighbor_id, seed_id = source_id, target_id
        else:
            continue
        item = by_id[neighbor_id]
        proposed[neighbor_id] = {
            "item_id": item["item_id"],
            "source_execution_id": item["source_execution_id"],
            "source_recorded_at": item["source_recorded_at"],
            "kind": item["kind"],
            "statement": item["statement"],
            "evidence_refs": item["evidence_refs"],
            "match_type": "graph_neighbor",
            "matched_tokens": [],
            "match_score": 0,
            "neighbor_of": seed_id,
        }

    ordered = sorted(
        proposed.values(),
        key=lambda item: (
            -item["match_score"],
            0 if item["match_type"] == "lexical" else 1,
            -_timestamp(item["source_recorded_at"]).timestamp(),
            item["item_id"],
        ),
    )[:max_candidates]

    basis = {
        "run_timestamp": run_timestamp,
        "project_id": project_id,
        "query": query,
        "query_tokens": query_tokens,
        "max_candidates": max_candidates,
        "candidates": ordered,
    }
    digest = hashlib.sha256(
        json.dumps(basis, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:16]
    result = {
        "retrieval_id": f"LE-RETR-{digest}",
        **basis,
        "authority_neutral": True,
        "execution_authorized": False,
    }
    load_and_validate(result, SCHEMA_DIR / "candidate-retrieval.schema.json")
    return result
