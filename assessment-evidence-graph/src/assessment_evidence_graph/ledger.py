"""Shared Decision Ledger-compatible envelope and local outbox helpers."""

from __future__ import annotations

import json
from pathlib import Path

from .canonical import canonical_json, sha256_json, stable_identifier
from .models import (
    AssessmentFixture,
    EvidenceArtifact,
    EvidenceReference,
    GateEvaluation,
    LedgerEventEnvelope,
    LedgerReceipt,
    PublicationDecision,
)
from .policy import PublicationPolicy


class LedgerError(RuntimeError):
    pass


def evaluated_versions(
    fixture: AssessmentFixture, policy: PublicationPolicy
) -> dict[str, str]:
    versions = {
        "fixture": fixture.versions.fixture,
        "graph_schema": fixture.versions.graph_schema,
        "methodology": fixture.versions.methodology,
        "policy": fixture.versions.policy,
        "producer": fixture.versions.producer,
        "envelope": fixture.versions.envelope,
        "repository_baseline_sha": fixture.versions.repository_baseline_sha,
    }
    for standard in policy.standards:
        versions[f"standard:{standard.path}"] = (
            f"{standard.version}@{standard.git_blob_sha}"
        )
    return dict(sorted(versions.items()))


def evidence_references(fixture: AssessmentFixture) -> tuple[EvidenceReference, ...]:
    artifacts = sorted(
        (
            node
            for node in fixture.nodes
            if isinstance(node, EvidenceArtifact)
        ),
        key=lambda node: node.node_id,
    )
    return tuple(
        EvidenceReference(
            evidence_id=node.node_id,
            content_sha256=node.content_sha256,
            source_version=node.source_version,
        )
        for node in artifacts
    )


def build_envelope(
    fixture: AssessmentFixture,
    policy: PublicationPolicy,
    evaluation: GateEvaluation,
    decision: PublicationDecision,
    *,
    before_version: int,
    after_version: int,
    canonical_state_sha256: str,
) -> LedgerEventEnvelope:
    event_id = stable_identifier(
        "EVT",
        fixture.tenant_id,
        fixture.assessment_id,
        decision.node_id,
        fixture.versions.envelope,
    )
    payload = {
        "envelope_schema_version": fixture.versions.envelope,
        "event_id": event_id,
        "event_type": "operator_intelligence.publication_decision",
        "producer": "operator-intelligence.assessment-evidence-graph",
        "producer_version": fixture.versions.producer,
        "producer_repository": "dburt-proex/operator-intelligence",
        "repository_baseline_sha": fixture.versions.repository_baseline_sha,
        "recorded_at": fixture.recorded_at,
        "trace_id": fixture.trace_id,
        "idempotency_key": fixture.idempotency_key,
        "tenant_id": fixture.tenant_id,
        "assessment_id": fixture.assessment_id,
        "publication_decision_ref": decision.node_id,
        "ledger_ref": fixture.publication_request.ledger_id,
        "evidence_refs": [
            item.model_dump(mode="json") for item in evidence_references(fixture)
        ],
        "evaluated_versions": evaluated_versions(fixture, policy),
        "evidence_gate": evaluation.evidence_gate,
        "publication_authority_gate": evaluation.publication_authority_gate,
        "final_publication_gate": evaluation.final_publication_gate,
        "reason_codes": list(evaluation.reason_codes),
        "before_canonical_version": before_version,
        "after_canonical_version": after_version,
        "canonical_state_sha256": canonical_state_sha256,
        "domain_state_owner": "operator-intelligence",
        "receipt_owner": "shared-decision-ledger",
        "implementation_authorized": False,
    }
    payload["payload_sha256"] = sha256_json(payload)
    return LedgerEventEnvelope.model_validate(payload)


def build_receipt(envelope: LedgerEventEnvelope) -> LedgerReceipt:
    return LedgerReceipt(
        node_id=envelope.ledger_ref,
        tenant_id=envelope.tenant_id,
        assessment_id=envelope.assessment_id,
        publication_decision_ref=envelope.publication_decision_ref,
        event_id=envelope.event_id,
        event_sha256=envelope.payload_sha256,
        evidence_refs=envelope.evidence_refs,
        evaluated_versions=envelope.evaluated_versions,
        before_canonical_version=envelope.before_canonical_version,
        after_canonical_version=envelope.after_canonical_version,
        canonical_state_sha256=envelope.canonical_state_sha256,
        final_publication_gate=envelope.final_publication_gate,
        reason_codes=envelope.reason_codes,
        idempotency_key=envelope.idempotency_key,
        domain_state_owner=envelope.domain_state_owner,
        receipt_owner=envelope.receipt_owner,
        implementation_authorized=False,
    )


def append_envelope(path: Path | None, envelope: LedgerEventEnvelope) -> bool:
    if path is None:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = canonical_json(envelope.model_dump(mode="json"))
    if path.exists():
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            if not raw_line.strip():
                continue
            existing = json.loads(raw_line)
            if existing.get("event_id") != envelope.event_id:
                continue
            if canonical_json(existing) != serialized:
                raise LedgerError("event ID collision with different envelope content")
            return False
    with path.open("a", encoding="utf-8") as handle:
        handle.write(serialized + "\n")
    return True
