from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from datetime import datetime
from typing import Any

from .paths import SCHEMA_DIR
from .schema_validation import load_and_validate


def _timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _candidate_identity(receipt: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    executor = receipt["executor"]
    identity = {
        "agent": executor["agent"],
        "model": executor["model"],
        "tools": sorted(set(receipt.get("tools", []))),
    }
    digest = hashlib.sha256(
        json.dumps(identity, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:16]
    return f"LE-EXECUTOR-{digest}", identity


def _round(value: float) -> float:
    return round(value, 6)


def build_executor_profiles(
    receipts: list[dict[str, Any]],
    *,
    as_of: str,
    project_id: str,
    min_samples: int = 3,
) -> list[dict[str, Any]]:
    """Build deterministic observed-performance profiles from retained receipts.

    Future receipts and HALT executions are excluded from positive routing evidence.
    Operator interventions remain an observation and are not penalized automatically.
    """
    if min_samples < 1:
        raise ValueError("min_samples must be at least 1")
    cutoff = _timestamp(as_of)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    identities: dict[str, dict[str, Any]] = {}

    for receipt in receipts:
        if receipt.get("project_id") != project_id:
            continue
        if _timestamp(receipt["recorded_at"]) > cutoff:
            continue
        if receipt.get("gate_result") == "HALT":
            continue
        candidate_id, identity = _candidate_identity(receipt)
        identities[candidate_id] = identity
        grouped[candidate_id].append(receipt)

    profiles: list[dict[str, Any]] = []
    for candidate_id in sorted(grouped):
        samples = sorted(grouped[candidate_id], key=lambda item: item["execution_id"])
        sample_count = len(samples)
        completed_count = sum(item.get("completion_status") == "completed" for item in samples)
        partial_count = sum(item.get("completion_status") == "partial" for item in samples)
        failed_count = sum(item.get("completion_status") == "failed" for item in samples)
        validation_records = [
            check
            for item in samples
            for check in item.get("validation", [])
            if check.get("result") != "not_run"
        ]
        validation_passes = sum(check.get("result") == "pass" for check in validation_records)
        failure_events = sum(len(item.get("failures", [])) for item in samples)
        friction_events = sum(len(item.get("friction", [])) for item in samples)
        interventions = sum(len(item.get("operator_interventions", [])) for item in samples)
        identity = identities[candidate_id]
        profiles.append(
            {
                "candidate_id": candidate_id,
                "agent": identity["agent"],
                "model": identity["model"],
                "tools": identity["tools"],
                "sample_count": sample_count,
                "completed_count": completed_count,
                "partial_count": partial_count,
                "failed_count": failed_count,
                "completion_rate": _round(completed_count / sample_count),
                "validation_pass_rate": _round(
                    validation_passes / len(validation_records) if validation_records else 0.0
                ),
                "failure_event_rate": _round(failure_events / sample_count),
                "friction_events_per_execution": _round(friction_events / sample_count),
                "operator_intervention_count": interventions,
                "source_execution_ids": [item["execution_id"] for item in samples],
                "eligible": sample_count >= min_samples,
            }
        )
    return profiles


def _rank_key(profile: dict[str, Any]) -> tuple[Any, ...]:
    return (
        -profile["completion_rate"],
        -profile["validation_pass_rate"],
        profile["failure_event_rate"],
        profile["friction_events_per_execution"],
        -profile["sample_count"],
        profile["candidate_id"],
    )


def _materially_tied(first: dict[str, Any], second: dict[str, Any], tolerance: float) -> bool:
    return (
        abs(first["completion_rate"] - second["completion_rate"]) <= tolerance
        and abs(first["validation_pass_rate"] - second["validation_pass_rate"]) <= tolerance
        and abs(first["failure_event_rate"] - second["failure_event_rate"]) <= tolerance
        and abs(first["friction_events_per_execution"] - second["friction_events_per_execution"]) <= tolerance
    )


def route_executor(
    receipts: list[dict[str, Any]],
    *,
    as_of: str,
    project_id: str,
    min_samples: int = 3,
    tie_tolerance: float = 0.02,
) -> dict[str, Any]:
    """Recommend an observed executor or abstain when evidence is insufficient.

    ROUTE is only a recommendation. `execution_authorized` is always false.
    """
    if not 0 <= tie_tolerance <= 1:
        raise ValueError("tie_tolerance must be between 0 and 1")
    profiles = build_executor_profiles(
        receipts,
        as_of=as_of,
        project_id=project_id,
        min_samples=min_samples,
    )
    eligible = sorted((item for item in profiles if item["eligible"]), key=_rank_key)

    if not profiles:
        decision = "NO_EVIDENCE"
        selected = None
        reason = "No non-HALT historical execution evidence exists for this project at or before the routing timestamp."
    elif not eligible:
        decision = "REVIEW"
        selected = None
        reason = f"No executor has the required minimum of {min_samples} observed execution samples."
    elif len(eligible) > 1 and _materially_tied(eligible[0], eligible[1], tie_tolerance):
        decision = "REVIEW"
        selected = None
        reason = "Top executor profiles are materially tied under the configured tolerance."
    else:
        decision = "ROUTE"
        selected = eligible[0]["candidate_id"]
        reason = "Selected the strongest eligible observed profile using completion, validation, failure, friction, and sample evidence in deterministic order."

    evidence_refs = sorted(
        {
            f"execution:{execution_id}"
            for profile in profiles
            for execution_id in profile["source_execution_ids"]
        }
    )
    basis = {
        "as_of": as_of,
        "project_id": project_id,
        "min_samples": min_samples,
        "tie_tolerance": tie_tolerance,
        "decision": decision,
        "selected_candidate_id": selected,
        "profiles": profiles,
    }
    digest = hashlib.sha256(
        json.dumps(basis, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:16]
    result = {
        "routing_id": f"LE-ROUTE-{digest}",
        "as_of": as_of,
        "project_id": project_id,
        "min_samples": min_samples,
        "tie_tolerance": tie_tolerance,
        "decision": decision,
        "selected_candidate_id": selected,
        "reason": reason,
        "profiles": profiles,
        "evidence_refs": evidence_refs,
        "execution_authorized": False,
    }
    load_and_validate(result, SCHEMA_DIR / "routing-decision.schema.json")
    return result
