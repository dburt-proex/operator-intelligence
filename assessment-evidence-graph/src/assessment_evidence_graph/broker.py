"""Deterministic, transactional write broker for canonical graph mutations."""

from __future__ import annotations

from pathlib import Path
from typing import Callable

from .canonical import sha256_json, stable_identifier
from .ledger import append_envelope, build_envelope, build_receipt
from .models import (
    AssessmentFixture,
    EdgeType,
    GateEvaluation,
    GraphEdge,
    LedgerEventEnvelope,
    LedgerReceipt,
    PublicationDecision,
    StrictModel,
    Verification,
)
from .policy import PublicationPolicy
from .store import SQLiteGraphStore


class BrokerError(RuntimeError):
    pass


class IdempotencyCollision(BrokerError):
    pass


class StaleCanonicalVersion(BrokerError):
    pass


class FinalStateVerificationError(BrokerError):
    pass


class BrokerCommit(StrictModel):
    decision: PublicationDecision
    receipt: LedgerReceipt
    envelope: LedgerEventEnvelope
    ledger_appended: bool
    idempotent_replay: bool
    final_state_verified: bool
    canonical_state: dict[str, object]
    graph_edges: tuple[GraphEdge, ...]


class AssessmentWriteBroker:
    """The only canonical write path for this bounded graph increment."""

    def __init__(self, database_path: Path):
        self.store = SQLiteGraphStore(database_path)

    def close(self) -> None:
        self.store.close()

    def commit(
        self,
        fixture: AssessmentFixture,
        policy: PublicationPolicy,
        evaluation: GateEvaluation,
        decision: PublicationDecision,
        *,
        ledger_path: Path | None = None,
        before_commit_hook: Callable[[], None] | None = None,
    ) -> BrokerCommit:
        request_sha256 = sha256_json(
            {
                "fixture": fixture.model_dump(mode="json"),
                "policy": policy.model_dump(mode="json"),
            }
        )
        tenant_id = fixture.tenant_id
        assessment_id = fixture.assessment_id

        existing = self.store.get_idempotent_response(
            tenant_id, assessment_id, fixture.idempotency_key
        )
        if existing is not None:
            existing_request_sha, response = existing
            if existing_request_sha != request_sha256:
                raise IdempotencyCollision(
                    "idempotency key was already committed with different content"
                )
            envelope = LedgerEventEnvelope.model_validate(response["envelope"])
            receipt = LedgerReceipt.model_validate(response["receipt"])
            stored_decision = PublicationDecision.model_validate(response["decision"])
            graph_edges = tuple(GraphEdge.model_validate(item) for item in response["graph_edges"])
            state = self.store.canonical_state(tenant_id, assessment_id)
            verified = sha256_json(state) == receipt.canonical_state_sha256
            if not verified:
                raise FinalStateVerificationError(
                    "idempotent replay no longer resolves to the recorded canonical state"
                )
            appended = append_envelope(ledger_path, envelope)
            return BrokerCommit(
                decision=stored_decision,
                receipt=receipt,
                envelope=envelope,
                ledger_appended=appended,
                idempotent_replay=True,
                final_state_verified=True,
                canonical_state=state,
                graph_edges=graph_edges,
            )

        with self.store.transaction():
            before_version = self.store.current_version(tenant_id, assessment_id)
            if before_version != fixture.expected_canonical_version:
                raise StaleCanonicalVersion(
                    f"expected canonical version {fixture.expected_canonical_version}, found {before_version}"
                )
            after_version = before_version + 1

            for node in fixture.nodes:
                self.store.insert_node(node)
            self.store.insert_node(decision)

            stored_edges = list(fixture.edges)
            for node in fixture.nodes:
                if isinstance(node, Verification):
                    edge = GraphEdge(
                        edge_id=stable_identifier(
                            "EDGE", node.node_id, EdgeType.INFORMS, decision.node_id
                        ),
                        tenant_id=tenant_id,
                        assessment_id=assessment_id,
                        edge_type=EdgeType.INFORMS,
                        from_id=node.node_id,
                        to_id=decision.node_id,
                        provenance_refs=tuple(node.evidence_refs) or (node.node_id,),
                        schema_version=fixture.versions.graph_schema,
                        recorded_at=fixture.recorded_at,
                    )
                    stored_edges.append(edge)
            for edge in stored_edges:
                self.store.insert_edge(edge)

            self.store.set_version(tenant_id, assessment_id, after_version)
            self.store.insert_provenance(
                tenant_id=tenant_id,
                assessment_id=assessment_id,
                run_id=fixture.run_id,
                trace_id=fixture.trace_id,
                idempotency_key=fixture.idempotency_key,
                policy_version=policy.policy_version,
                before_version=before_version,
                after_version=after_version,
                final_gate=evaluation.final_publication_gate,
                reason_codes=evaluation.reason_codes,
                recorded_at=fixture.recorded_at,
            )

            state = self.store.canonical_state(tenant_id, assessment_id)
            state_sha256 = sha256_json(state)
            envelope = build_envelope(
                fixture,
                policy,
                evaluation,
                decision,
                before_version=before_version,
                after_version=after_version,
                canonical_state_sha256=state_sha256,
            )
            receipt = build_receipt(envelope)
            emit_edge = GraphEdge(
                edge_id=stable_identifier(
                    "EDGE", decision.node_id, EdgeType.EMITS, receipt.node_id
                ),
                tenant_id=tenant_id,
                assessment_id=assessment_id,
                edge_type=EdgeType.EMITS,
                from_id=decision.node_id,
                to_id=receipt.node_id,
                provenance_refs=(envelope.event_id,),
                schema_version=fixture.versions.graph_schema,
                recorded_at=fixture.recorded_at,
            )
            all_edges = tuple(stored_edges + [emit_edge])
            self.store.insert_outbox(
                tenant_id,
                assessment_id,
                envelope.event_id,
                envelope.model_dump(mode="json"),
                envelope.payload_sha256,
            )
            response = {
                "decision": decision.model_dump(mode="json"),
                "receipt": receipt.model_dump(mode="json"),
                "envelope": envelope.model_dump(mode="json"),
                "graph_edges": [edge.model_dump(mode="json") for edge in all_edges],
            }
            self.store.put_idempotent_response(
                tenant_id,
                assessment_id,
                fixture.idempotency_key,
                request_sha256,
                response,
            )
            if before_commit_hook is not None:
                before_commit_hook()

        final_state = self.store.canonical_state(tenant_id, assessment_id)
        final_verified = sha256_json(final_state) == receipt.canonical_state_sha256
        if not final_verified:
            raise FinalStateVerificationError(
                "post-commit canonical state differs from the receipt"
            )
        appended = append_envelope(ledger_path, envelope)
        return BrokerCommit(
            decision=decision,
            receipt=receipt,
            envelope=envelope,
            ledger_appended=appended,
            idempotent_replay=False,
            final_state_verified=True,
            canonical_state=final_state,
            graph_edges=all_edges,
        )
