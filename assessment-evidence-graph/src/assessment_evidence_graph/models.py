"""Strict, versioned graph and receipt contracts."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated, Literal, TypeAlias

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


ID_PATTERN = r"^OI-[A-Z][A-Z0-9-]+$"
ASSESSMENT_ID_PATTERN = r"^OI-ASSESS-[A-Z0-9-]+$"
TENANT_ID_PATTERN = r"^OI-TENANT-[A-Z0-9-]+$"
SHA256_PATTERN = r"^[0-9a-f]{64}$"
SEMVER_PATTERN = r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$"


class Gate(StrEnum):
    ALLOW = "ALLOW"
    REVIEW = "REVIEW"
    HALT = "HALT"


class PublicationState(StrEnum):
    OFFICIAL = "official"
    PROVISIONAL = "provisional"
    RANGE_ONLY = "range_only"
    BLOCKED = "blocked"
    INTERNAL_ONLY = "internal_only"


class EdgeType(StrEnum):
    HAS_SCOPE = "HAS_SCOPE"
    REQUIRES_EVIDENCE = "REQUIRES_EVIDENCE"
    SATISFIES = "SATISFIES"
    SUPPORTS = "SUPPORTS"
    CONTRADICTS = "CONTRADICTS"
    SUPPORTS_FINDING = "SUPPORTS_FINDING"
    SUPPORTED_BY = "SUPPORTED_BY"
    IDENTIFIES = "IDENTIFIES"
    ADDRESSED_BY = "ADDRESSED_BY"
    VERIFIED_BY = "VERIFIED_BY"
    INFORMS = "INFORMS"
    EMITS = "EMITS"


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)


def _validate_timestamp(value: str) -> str:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return value


class NodeBase(StrictModel):
    node_id: str = Field(pattern=ID_PATTERN)
    tenant_id: str = Field(pattern=TENANT_ID_PATTERN)
    assessment_id: str = Field(pattern=ASSESSMENT_ID_PATTERN)
    schema_version: str = Field(pattern=SEMVER_PATTERN)
    record_version: str = Field(pattern=SEMVER_PATTERN)
    recorded_at: str

    _recorded_at = field_validator("recorded_at")(_validate_timestamp)


class Engagement(NodeBase):
    node_type: Literal["Engagement"]
    engagement_name: str = Field(min_length=1)
    synthetic: bool


class Scope(NodeBase):
    node_type: Literal["Scope"]
    statement: str = Field(min_length=1)
    inclusions: tuple[str, ...] = Field(min_length=1)
    exclusions: tuple[str, ...] = Field(min_length=1)
    authorization_refs: tuple[str, ...] = Field(min_length=1)


class EvidenceRequirement(NodeBase):
    node_type: Literal["EvidenceRequirement"]
    criterion_ids: tuple[str, ...] = Field(min_length=1)
    requirement: str = Field(min_length=1)
    minimum_strength: Literal["high", "medium", "low"]


class EvidenceArtifact(NodeBase):
    node_type: Literal["EvidenceArtifact"]
    source_type: Literal[
        "screenshot",
        "url",
        "document",
        "export",
        "system_record",
        "safe_test",
        "interview",
        "observation",
        "third_party",
    ]
    source_locator: str = Field(min_length=1)
    source_version: str = Field(min_length=1)
    observation: str = Field(min_length=1)
    content_sha256: str = Field(pattern=SHA256_PATTERN)
    evidence_class: Literal["A", "B", "C", "D", "E"]
    evidence_strength: Literal["high", "medium", "low", "insufficient"]
    review_state: Literal["accepted", "limited", "rejected", "superseded"]
    limitations: tuple[str, ...]
    authorization_ref: str | None


class Claim(NodeBase):
    node_type: Literal["Claim"]
    subject_key: str = Field(min_length=1)
    statement: str = Field(min_length=1)
    stance: Literal["supports", "refutes", "unknown"]
    evidence_refs: tuple[str, ...] = Field(min_length=1)


class Finding(NodeBase):
    node_type: Literal["Finding"]
    observation: str = Field(min_length=1)
    interpretation: str = Field(min_length=1)
    business_impact: str = Field(min_length=1)
    confidence: Literal["high", "medium", "low", "unknown"]
    priority: Literal["critical", "high", "medium", "low", "validation"]
    material: bool
    evidence_refs: tuple[str, ...]
    claim_refs: tuple[str, ...] = Field(min_length=1)
    limitations: tuple[str, ...]


class ControlGap(NodeBase):
    node_type: Literal["ControlGap"]
    description: str = Field(min_length=1)
    finding_refs: tuple[str, ...] = Field(min_length=1)


class Remediation(NodeBase):
    node_type: Literal["Remediation"]
    action: str = Field(min_length=1)
    control_gap_refs: tuple[str, ...] = Field(min_length=1)
    roadmap_phase: Literal[0, 1, 2, 3, 4, 5]
    advisory_only: bool
    implementation_authorized: bool


class Verification(NodeBase):
    node_type: Literal["Verification"]
    remediation_ref: str = Field(pattern=ID_PATTERN)
    status: Literal["verified", "failed", "partial", "not_run"]
    expected_state: str = Field(min_length=1)
    observed_state: str = Field(min_length=1)
    evidence_refs: tuple[str, ...]


DomainNode: TypeAlias = Annotated[
    Engagement
    | Scope
    | EvidenceRequirement
    | EvidenceArtifact
    | Claim
    | Finding
    | ControlGap
    | Remediation
    | Verification,
    Field(discriminator="node_type"),
]


class GraphEdge(StrictModel):
    edge_id: str = Field(pattern=r"^OI-EDGE-[0-9A-F]{16}$")
    tenant_id: str = Field(pattern=TENANT_ID_PATTERN)
    assessment_id: str = Field(pattern=ASSESSMENT_ID_PATTERN)
    edge_type: EdgeType
    from_id: str = Field(pattern=ID_PATTERN)
    to_id: str = Field(pattern=ID_PATTERN)
    provenance_refs: tuple[str, ...] = Field(min_length=1)
    schema_version: str = Field(pattern=SEMVER_PATTERN)
    recorded_at: str

    _recorded_at = field_validator("recorded_at")(_validate_timestamp)


class PublicationRequest(StrictModel):
    publication_decision_id: str = Field(pattern=r"^OI-PUB-[A-Z0-9-]+$")
    ledger_id: str = Field(pattern=r"^OI-DL-[A-Z0-9-]+$")
    requested_state: PublicationState
    result_level: Literal["finding_set", "report"]
    quality_control_ref: str | None
    publication_approver: str | None
    client_safe_summary: str = Field(min_length=1)
    claims_certification: bool = False
    implementation_authorized: bool = False


class VersionSet(StrictModel):
    fixture: str = Field(pattern=SEMVER_PATTERN)
    graph_schema: str = Field(pattern=SEMVER_PATTERN)
    methodology: str = Field(min_length=1)
    policy: str = Field(pattern=SEMVER_PATTERN)
    producer: str = Field(pattern=SEMVER_PATTERN)
    envelope: str = Field(pattern=SEMVER_PATTERN)
    repository_baseline_sha: str = Field(pattern=r"^[0-9a-f]{40}$")


class AssessmentFixture(StrictModel):
    run_id: str = Field(pattern=r"^OI-RUN-[A-Z0-9-]+$")
    trace_id: str = Field(pattern=r"^OI-TRACE-[A-Z0-9-]+$")
    idempotency_key: str = Field(min_length=1)
    tenant_id: str = Field(pattern=TENANT_ID_PATTERN)
    assessment_id: str = Field(pattern=ASSESSMENT_ID_PATTERN)
    recorded_at: str
    expected_canonical_version: int = Field(ge=0)
    versions: VersionSet
    nodes: tuple[DomainNode, ...] = Field(min_length=1)
    edges: tuple[GraphEdge, ...] = Field(min_length=1)
    publication_request: PublicationRequest

    _recorded_at = field_validator("recorded_at")(_validate_timestamp)

    @model_validator(mode="after")
    def validate_boundaries(self) -> "AssessmentFixture":
        node_ids: set[str] = set()
        node_types: set[str] = set()
        for node in self.nodes:
            if node.tenant_id != self.tenant_id or node.assessment_id != self.assessment_id:
                raise ValueError("all nodes must remain inside the fixture tenant and assessment boundary")
            if node.node_id in node_ids:
                raise ValueError(f"duplicate node_id: {node.node_id}")
            node_ids.add(node.node_id)
            node_types.add(node.node_type)
        required = {
            "Engagement",
            "Scope",
            "EvidenceRequirement",
            "EvidenceArtifact",
            "Claim",
            "Finding",
            "ControlGap",
            "Remediation",
            "Verification",
        }
        missing = sorted(required - node_types)
        if missing:
            raise ValueError(f"missing required node types: {missing}")
        edge_ids: set[str] = set()
        for edge in self.edges:
            if edge.tenant_id != self.tenant_id or edge.assessment_id != self.assessment_id:
                raise ValueError("all edges must remain inside the fixture tenant and assessment boundary")
            if edge.edge_id in edge_ids:
                raise ValueError(f"duplicate edge_id: {edge.edge_id}")
            edge_ids.add(edge.edge_id)
            if edge.from_id not in node_ids or edge.to_id not in node_ids:
                raise ValueError(f"dangling graph edge: {edge.edge_id}")
        return self


class GateEvaluation(StrictModel):
    evidence_gate: Gate
    publication_authority_gate: Gate
    final_publication_gate: Gate
    publication_state: PublicationState
    reason_codes: tuple[str, ...]
    evidence_refs: tuple[str, ...]
    evidence_snapshot_sha256: str = Field(pattern=SHA256_PATTERN)


class PublicationDecision(NodeBase):
    node_type: Literal["PublicationDecision"] = "PublicationDecision"
    gate: Gate
    publication_state: PublicationState
    result_level: Literal["finding_set", "report"]
    reason_codes: tuple[str, ...]
    evidence_refs: tuple[str, ...]
    evidence_snapshot_sha256: str = Field(pattern=SHA256_PATTERN)
    quality_control_ref: str | None
    publication_approver: str | None
    client_safe_summary: str
    implementation_authorized: Literal[False] = False


class EvidenceReference(StrictModel):
    evidence_id: str = Field(pattern=r"^OI-EV-[A-Z0-9-]+$")
    content_sha256: str = Field(pattern=SHA256_PATTERN)
    source_version: str = Field(min_length=1)


class LedgerEventEnvelope(StrictModel):
    envelope_schema_version: str = Field(pattern=SEMVER_PATTERN)
    event_id: str = Field(pattern=r"^OI-EVT-[0-9A-F]{16}$")
    event_type: Literal["operator_intelligence.publication_decision"]
    producer: Literal["operator-intelligence.assessment-evidence-graph"]
    producer_version: str = Field(pattern=SEMVER_PATTERN)
    producer_repository: Literal["dburt-proex/operator-intelligence"]
    repository_baseline_sha: str = Field(pattern=r"^[0-9a-f]{40}$")
    recorded_at: str
    trace_id: str
    idempotency_key: str
    tenant_id: str
    assessment_id: str
    publication_decision_ref: str
    ledger_ref: str
    evidence_refs: tuple[EvidenceReference, ...]
    evaluated_versions: dict[str, str]
    evidence_gate: Gate
    publication_authority_gate: Gate
    final_publication_gate: Gate
    reason_codes: tuple[str, ...]
    before_canonical_version: int
    after_canonical_version: int
    canonical_state_sha256: str = Field(pattern=SHA256_PATTERN)
    domain_state_owner: Literal["operator-intelligence"]
    receipt_owner: Literal["shared-decision-ledger"]
    implementation_authorized: Literal[False] = False
    payload_sha256: str = Field(pattern=SHA256_PATTERN)

    _recorded_at = field_validator("recorded_at")(_validate_timestamp)


class LedgerReceipt(StrictModel):
    node_id: str = Field(pattern=r"^OI-DL-[A-Z0-9-]+$")
    node_type: Literal["LedgerReceipt"] = "LedgerReceipt"
    tenant_id: str
    assessment_id: str
    publication_decision_ref: str
    event_id: str
    event_sha256: str = Field(pattern=SHA256_PATTERN)
    evidence_refs: tuple[EvidenceReference, ...]
    evaluated_versions: dict[str, str]
    before_canonical_version: int
    after_canonical_version: int
    canonical_state_sha256: str = Field(pattern=SHA256_PATTERN)
    final_publication_gate: Gate
    reason_codes: tuple[str, ...]
    idempotency_key: str
    domain_state_owner: Literal["operator-intelligence"]
    receipt_owner: Literal["shared-decision-ledger"]
    implementation_authorized: Literal[False] = False


class ReplayResult(StrictModel):
    run_id: str
    decision: PublicationDecision
    receipt: LedgerReceipt
    envelope: LedgerEventEnvelope
    ledger_appended: bool
    idempotent_replay: bool
    final_state_verified: bool
    canonical_state: dict[str, object]
    graph_edges: tuple[GraphEdge, ...]
