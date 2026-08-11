"""End-to-end deterministic replay for the GE-001 vertical slice."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

from .broker import AssessmentWriteBroker
from .models import (
    AssessmentFixture,
    Gate,
    GateEvaluation,
    PublicationDecision,
    ReplayResult,
)
from .policy import (
    PublicationPolicy,
    evaluate_publication,
    load_policy,
    verify_policy_sources,
)


SUBSYSTEM_ROOT = Path(__file__).resolve().parents[2]
REPOSITORY_ROOT = SUBSYSTEM_ROOT.parent
DEFAULT_POLICY = SUBSYSTEM_ROOT / "config" / "publication-policy.json"


class GovernanceHalt(RuntimeError):
    def __init__(self, evaluation: GateEvaluation):
        self.evaluation = evaluation
        super().__init__(
            "publication proposal halted: " + ", ".join(evaluation.reason_codes)
        )


def load_fixture(path: Path) -> AssessmentFixture:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"fixture cannot be loaded: {exc}") from exc
    return AssessmentFixture.model_validate(raw)


def _decision_from_evaluation(
    fixture: AssessmentFixture, evaluation: GateEvaluation
) -> PublicationDecision:
    request = fixture.publication_request
    return PublicationDecision(
        node_id=request.publication_decision_id,
        tenant_id=fixture.tenant_id,
        assessment_id=fixture.assessment_id,
        schema_version=fixture.versions.graph_schema,
        record_version="1.0.0",
        recorded_at=fixture.recorded_at,
        gate=evaluation.final_publication_gate,
        publication_state=evaluation.publication_state,
        result_level=request.result_level,
        reason_codes=evaluation.reason_codes,
        evidence_refs=evaluation.evidence_refs,
        evidence_snapshot_sha256=evaluation.evidence_snapshot_sha256,
        quality_control_ref=request.quality_control_ref,
        publication_approver=request.publication_approver,
        client_safe_summary=request.client_safe_summary,
        implementation_authorized=False,
    )


def replay_fixture(
    fixture_path: Path,
    database_path: Path,
    *,
    ledger_path: Path | None = None,
    policy_path: Path = DEFAULT_POLICY,
    before_commit_hook: Callable[[], None] | None = None,
) -> ReplayResult:
    fixture = load_fixture(fixture_path)
    policy: PublicationPolicy = load_policy(policy_path)
    verify_policy_sources(policy, REPOSITORY_ROOT)
    evaluation = evaluate_publication(fixture, policy)
    if evaluation.final_publication_gate == Gate.HALT:
        raise GovernanceHalt(evaluation)
    decision = _decision_from_evaluation(fixture, evaluation)
    broker = AssessmentWriteBroker(database_path)
    try:
        commit = broker.commit(
            fixture,
            policy,
            evaluation,
            decision,
            ledger_path=ledger_path,
            before_commit_hook=before_commit_hook,
        )
    finally:
        broker.close()
    return ReplayResult(
        run_id=fixture.run_id,
        decision=commit.decision,
        receipt=commit.receipt,
        envelope=commit.envelope,
        ledger_appended=commit.ledger_appended,
        idempotent_replay=commit.idempotent_replay,
        final_state_verified=commit.final_state_verified,
        canonical_state=commit.canonical_state,
        graph_edges=commit.graph_edges,
    )
