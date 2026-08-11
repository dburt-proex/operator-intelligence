"""SQLite canonical store for Operator Intelligence assessment graph state."""

from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Iterator

from .canonical import canonical_json, sha256_json
from .models import EvidenceArtifact, Finding, GraphEdge, PublicationDecision


class StoreError(RuntimeError):
    pass


class CanonicalCollision(StoreError):
    pass


SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS canonical_versions (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    version INTEGER NOT NULL,
    PRIMARY KEY (tenant_id, assessment_id)
);

CREATE TABLE IF NOT EXISTS entities (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    node_id TEXT NOT NULL,
    node_type TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    content_sha256 TEXT NOT NULL,
    PRIMARY KEY (tenant_id, assessment_id, node_id)
);

CREATE TABLE IF NOT EXISTS evidence_artifacts (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    evidence_id TEXT NOT NULL,
    source_version TEXT NOT NULL,
    content_sha256 TEXT NOT NULL,
    review_state TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    PRIMARY KEY (tenant_id, assessment_id, evidence_id)
);

CREATE TABLE IF NOT EXISTS claims (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    claim_id TEXT NOT NULL,
    subject_key TEXT NOT NULL,
    stance TEXT NOT NULL,
    evidence_refs_json TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    PRIMARY KEY (tenant_id, assessment_id, claim_id)
);

CREATE TABLE IF NOT EXISTS findings (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    finding_id TEXT NOT NULL,
    material INTEGER NOT NULL,
    evidence_refs_json TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    PRIMARY KEY (tenant_id, assessment_id, finding_id)
);

CREATE TABLE IF NOT EXISTS decisions (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    decision_id TEXT NOT NULL,
    gate TEXT NOT NULL,
    publication_state TEXT NOT NULL,
    reason_codes_json TEXT NOT NULL,
    implementation_authorized INTEGER NOT NULL CHECK (implementation_authorized = 0),
    payload_json TEXT NOT NULL,
    PRIMARY KEY (tenant_id, assessment_id, decision_id)
);

CREATE TABLE IF NOT EXISTS graph_edges (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    edge_id TEXT NOT NULL,
    edge_type TEXT NOT NULL,
    from_id TEXT NOT NULL,
    to_id TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    content_sha256 TEXT NOT NULL,
    PRIMARY KEY (tenant_id, assessment_id, edge_id)
);

CREATE TABLE IF NOT EXISTS provenance_events (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    run_id TEXT NOT NULL,
    trace_id TEXT NOT NULL,
    idempotency_key TEXT NOT NULL,
    policy_version TEXT NOT NULL,
    before_version INTEGER NOT NULL,
    after_version INTEGER NOT NULL,
    final_gate TEXT NOT NULL,
    reason_codes_json TEXT NOT NULL,
    recorded_at TEXT NOT NULL,
    PRIMARY KEY (tenant_id, assessment_id, run_id)
);

CREATE TABLE IF NOT EXISTS ledger_outbox (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    event_id TEXT NOT NULL,
    envelope_json TEXT NOT NULL,
    payload_sha256 TEXT NOT NULL,
    dispatched INTEGER NOT NULL DEFAULT 0 CHECK (dispatched IN (0, 1)),
    PRIMARY KEY (tenant_id, assessment_id, event_id)
);

CREATE TABLE IF NOT EXISTS idempotency_keys (
    tenant_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    idempotency_key TEXT NOT NULL,
    request_sha256 TEXT NOT NULL,
    response_json TEXT NOT NULL,
    PRIMARY KEY (tenant_id, assessment_id, idempotency_key)
);
"""


class SQLiteGraphStore:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(SCHEMA)
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    @contextmanager
    def transaction(self) -> Iterator[sqlite3.Connection]:
        self.connection.execute("BEGIN IMMEDIATE")
        try:
            yield self.connection
        except Exception:
            self.connection.rollback()
            raise
        else:
            self.connection.commit()

    def current_version(self, tenant_id: str, assessment_id: str) -> int:
        row = self.connection.execute(
            "SELECT version FROM canonical_versions WHERE tenant_id = ? AND assessment_id = ?",
            (tenant_id, assessment_id),
        ).fetchone()
        return int(row["version"]) if row else 0

    def set_version(self, tenant_id: str, assessment_id: str, version: int) -> None:
        self.connection.execute(
            """
            INSERT INTO canonical_versions (tenant_id, assessment_id, version)
            VALUES (?, ?, ?)
            ON CONFLICT (tenant_id, assessment_id) DO UPDATE SET version = excluded.version
            """,
            (tenant_id, assessment_id, version),
        )

    def get_idempotent_response(
        self, tenant_id: str, assessment_id: str, idempotency_key: str
    ) -> tuple[str, dict[str, Any]] | None:
        row = self.connection.execute(
            """
            SELECT request_sha256, response_json FROM idempotency_keys
            WHERE tenant_id = ? AND assessment_id = ? AND idempotency_key = ?
            """,
            (tenant_id, assessment_id, idempotency_key),
        ).fetchone()
        if row is None:
            return None
        return str(row["request_sha256"]), json.loads(row["response_json"])

    def put_idempotent_response(
        self,
        tenant_id: str,
        assessment_id: str,
        idempotency_key: str,
        request_sha256: str,
        response: dict[str, Any],
    ) -> None:
        self.connection.execute(
            """
            INSERT INTO idempotency_keys
                (tenant_id, assessment_id, idempotency_key, request_sha256, response_json)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                tenant_id,
                assessment_id,
                idempotency_key,
                request_sha256,
                canonical_json(response),
            ),
        )

    def _insert_immutable(
        self,
        *,
        table: str,
        id_column: str,
        tenant_id: str,
        assessment_id: str,
        record_id: str,
        payload_json: str,
        insert: Callable[[], None],
    ) -> None:
        row = self.connection.execute(
            f"SELECT payload_json FROM {table} WHERE tenant_id = ? AND assessment_id = ? AND {id_column} = ?",
            (tenant_id, assessment_id, record_id),
        ).fetchone()
        if row is not None:
            if str(row["payload_json"]) != payload_json:
                raise CanonicalCollision(
                    f"{table} ID collision with different content: {record_id}"
                )
            return
        insert()

    def insert_node(self, node: Any) -> None:
        payload = node.model_dump(mode="json")
        payload_json = canonical_json(payload)
        content_hash = sha256_json(payload)

        def insert_entity() -> None:
            self.connection.execute(
                """
                INSERT INTO entities
                    (tenant_id, assessment_id, node_id, node_type, payload_json, content_sha256)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    node.tenant_id,
                    node.assessment_id,
                    node.node_id,
                    node.node_type,
                    payload_json,
                    content_hash,
                ),
            )

        self._insert_immutable(
            table="entities",
            id_column="node_id",
            tenant_id=node.tenant_id,
            assessment_id=node.assessment_id,
            record_id=node.node_id,
            payload_json=payload_json,
            insert=insert_entity,
        )

        if isinstance(node, EvidenceArtifact):
            self.connection.execute(
                """
                INSERT OR IGNORE INTO evidence_artifacts
                    (tenant_id, assessment_id, evidence_id, source_version, content_sha256, review_state, payload_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    node.tenant_id,
                    node.assessment_id,
                    node.node_id,
                    node.source_version,
                    node.content_sha256,
                    node.review_state,
                    payload_json,
                ),
            )
        elif node.node_type == "Claim":
            self.connection.execute(
                """
                INSERT OR IGNORE INTO claims
                    (tenant_id, assessment_id, claim_id, subject_key, stance, evidence_refs_json, payload_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    node.tenant_id,
                    node.assessment_id,
                    node.node_id,
                    node.subject_key,
                    node.stance,
                    canonical_json(list(node.evidence_refs)),
                    payload_json,
                ),
            )
        elif isinstance(node, Finding):
            self.connection.execute(
                """
                INSERT OR IGNORE INTO findings
                    (tenant_id, assessment_id, finding_id, material, evidence_refs_json, payload_json)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    node.tenant_id,
                    node.assessment_id,
                    node.node_id,
                    int(node.material),
                    canonical_json(list(node.evidence_refs)),
                    payload_json,
                ),
            )
        elif isinstance(node, PublicationDecision):
            self.connection.execute(
                """
                INSERT OR IGNORE INTO decisions
                    (tenant_id, assessment_id, decision_id, gate, publication_state,
                     reason_codes_json, implementation_authorized, payload_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    node.tenant_id,
                    node.assessment_id,
                    node.node_id,
                    node.gate,
                    node.publication_state,
                    canonical_json(list(node.reason_codes)),
                    int(node.implementation_authorized),
                    payload_json,
                ),
            )

    def insert_edge(self, edge: GraphEdge) -> None:
        payload = edge.model_dump(mode="json")
        payload_json = canonical_json(payload)
        content_hash = sha256_json(payload)

        def insert() -> None:
            self.connection.execute(
                """
                INSERT INTO graph_edges
                    (tenant_id, assessment_id, edge_id, edge_type, from_id, to_id,
                     payload_json, content_sha256)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    edge.tenant_id,
                    edge.assessment_id,
                    edge.edge_id,
                    edge.edge_type,
                    edge.from_id,
                    edge.to_id,
                    payload_json,
                    content_hash,
                ),
            )

        self._insert_immutable(
            table="graph_edges",
            id_column="edge_id",
            tenant_id=edge.tenant_id,
            assessment_id=edge.assessment_id,
            record_id=edge.edge_id,
            payload_json=payload_json,
            insert=insert,
        )

    def insert_provenance(
        self,
        *,
        tenant_id: str,
        assessment_id: str,
        run_id: str,
        trace_id: str,
        idempotency_key: str,
        policy_version: str,
        before_version: int,
        after_version: int,
        final_gate: str,
        reason_codes: tuple[str, ...],
        recorded_at: str,
    ) -> None:
        self.connection.execute(
            """
            INSERT INTO provenance_events
                (tenant_id, assessment_id, run_id, trace_id, idempotency_key,
                 policy_version, before_version, after_version, final_gate,
                 reason_codes_json, recorded_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                tenant_id,
                assessment_id,
                run_id,
                trace_id,
                idempotency_key,
                policy_version,
                before_version,
                after_version,
                final_gate,
                canonical_json(list(reason_codes)),
                recorded_at,
            ),
        )

    def insert_outbox(
        self,
        tenant_id: str,
        assessment_id: str,
        event_id: str,
        envelope: dict[str, Any],
        payload_sha256: str,
    ) -> None:
        self.connection.execute(
            """
            INSERT INTO ledger_outbox
                (tenant_id, assessment_id, event_id, envelope_json, payload_sha256)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                tenant_id,
                assessment_id,
                event_id,
                canonical_json(envelope),
                payload_sha256,
            ),
        )

    def canonical_state(self, tenant_id: str, assessment_id: str) -> dict[str, Any]:
        entities = [
            {
                "node_id": row["node_id"],
                "node_type": row["node_type"],
                "payload": json.loads(row["payload_json"]),
                "content_sha256": row["content_sha256"],
            }
            for row in self.connection.execute(
                """
                SELECT node_id, node_type, payload_json, content_sha256
                FROM entities WHERE tenant_id = ? AND assessment_id = ?
                ORDER BY node_id
                """,
                (tenant_id, assessment_id),
            )
        ]
        edges = [
            {
                "edge_id": row["edge_id"],
                "edge_type": row["edge_type"],
                "from_id": row["from_id"],
                "to_id": row["to_id"],
                "payload": json.loads(row["payload_json"]),
                "content_sha256": row["content_sha256"],
            }
            for row in self.connection.execute(
                """
                SELECT edge_id, edge_type, from_id, to_id, payload_json, content_sha256
                FROM graph_edges WHERE tenant_id = ? AND assessment_id = ?
                ORDER BY edge_id
                """,
                (tenant_id, assessment_id),
            )
        ]
        return {
            "tenant_id": tenant_id,
            "assessment_id": assessment_id,
            "canonical_version": self.current_version(tenant_id, assessment_id),
            "entities": entities,
            "edges": edges,
        }

    def row_counts(self, tenant_id: str, assessment_id: str) -> dict[str, int]:
        tables = (
            "entities",
            "evidence_artifacts",
            "claims",
            "findings",
            "decisions",
            "graph_edges",
            "provenance_events",
            "ledger_outbox",
            "idempotency_keys",
        )
        return {
            table: int(
                self.connection.execute(
                    f"SELECT COUNT(*) FROM {table} WHERE tenant_id = ? AND assessment_id = ?",
                    (tenant_id, assessment_id),
                ).fetchone()[0]
            )
            for table in tables
        }
