import hashlib
from datetime import datetime, timedelta
from typing import Any


def ledger_record_id(run_id: str, opportunity_id: str | None) -> str:
    basis = f"{run_id}|{opportunity_id or 'NO_ACTION'}"
    return f"LE-LED-{hashlib.sha256(basis.encode()).hexdigest()[:16]}"


def build_directive(run: dict[str, Any], opportunity: dict[str, Any]) -> dict[str, Any]:
    timestamp = datetime.fromisoformat(run["run_timestamp"].replace("Z", "+00:00"))
    suffix = int(opportunity["opportunity_id"].rsplit("-", 1)[1]) % 1000
    evidence = sorted(set(opportunity["supporting_signals"] + run.get("evidence_refs", [])))
    return {
        "directive_id": f"LD-{timestamp.date().isoformat()}-{suffix:03d}",
        "run_id": run["run_id"],
        "selected_opportunity_id": opportunity["opportunity_id"],
        "objective": opportunity["objective"],
        "target_system": run["target_system"],
        "proposed_action": run["proposed_actions"][opportunity["opportunity_id"]],
        "evidence_refs": evidence,
        "score_summary": {
            "raw_value_score": opportunity["raw_value_score"],
            "friction_score": opportunity["friction_score"],
            "risk_score": opportunity["risk_score"],
            "confidence": opportunity["confidence"],
            "leverage_index": opportunity["leverage_index"],
            "gate_result": opportunity["gate_result"],
        },
        "assumptions": opportunity["assumptions"],
        "dependencies": opportunity["dependencies"],
        "allowed_actions": ["prepare_draft_artifact", "request_human_review"],
        "prohibited_actions": ["repository_mutation", "external_action", "agent_dispatch", "financial_action", "policy_change"],
        "review_owner": run["review_owner"],
        "approval_state": "draft",
        "expires_at": (timestamp + timedelta(hours=24)).isoformat().replace("+00:00", "Z"),
        "expected_outcome": opportunity["expected_outcome"],
        "completion_evidence": opportunity["success_evidence"],
        "rollback_or_recovery": "Reject or allow the draft to expire; no external state has changed.",
        "ledger_record_id": ledger_record_id(run["run_id"], opportunity["opportunity_id"]),
    }
