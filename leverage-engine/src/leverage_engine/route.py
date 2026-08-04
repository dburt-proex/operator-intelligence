from datetime import datetime
from typing import Any


def _age_hours(older: str, newer: str) -> float:
    old_dt = datetime.fromisoformat(older.replace("Z", "+00:00"))
    new_dt = datetime.fromisoformat(newer.replace("Z", "+00:00"))
    return (new_dt - old_dt).total_seconds() / 3600


def route_opportunity(
    opportunity: dict[str, Any],
    signals_by_id: dict[str, dict[str, Any]],
    repositories: list[dict[str, Any]],
    policy: dict[str, Any],
    run_timestamp: str,
) -> tuple[str, list[str]]:
    reasons: list[str] = []
    if opportunity["state"] == "duplicate":
        return "REVIEW", ["LE-GATE-DUPLICATE-SUPPRESSED"]

    g4 = sorted(set(opportunity["boundary_flags"]) & set(policy["g4_rules"]))
    if g4:
        return "HALT", g4

    supporting = [signals_by_id[item] for item in opportunity["supporting_signals"]]
    if any(item["validation_state"] in {"contradicted", "blocked"} for item in supporting):
        reasons.append("LE-GATE-EVIDENCE-CONFLICT")
    if any(item["validation_state"] != "validated" for item in supporting):
        reasons.append("LE-GATE-EVIDENCE-VALIDATION-REQUIRED")
    if any(item["freshness_state"] in {"stale", "unknown"} for item in supporting):
        reasons.append("LE-GATE-SIGNAL-FRESHNESS")
    if opportunity["confidence"] in {"low", "unknown"}:
        reasons.append("LE-GATE-CONFIDENCE-INSUFFICIENT")
    if opportunity["risk_score"] >= policy["risk_review_threshold"]:
        reasons.append("LE-GATE-MATERIAL-RISK")

    targets = set(opportunity["target_assets"])
    for repository in repositories:
        if targets & set(repository["commercial_assets"]):
            if _age_hours(repository["captured_at"], run_timestamp) > policy["maximum_repository_snapshot_age_hours"]:
                reasons.append("LE-GATE-REPOSITORY-SNAPSHOT-STALE")

    return ("REVIEW", sorted(set(reasons))) if reasons else ("ALLOW", ["LE-GATE-ELIGIBLE-FOR-HUMAN-REVIEW"])
