"""Pure publication policy evaluation for an assessment graph proposal."""

from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path

from pydantic import Field

from .canonical import sha256_json
from .models import (
    AssessmentFixture,
    Claim,
    ControlGap,
    EdgeType,
    EvidenceArtifact,
    Finding,
    Gate,
    GateEvaluation,
    PublicationState,
    Remediation,
    Scope,
    StrictModel,
    Verification,
)


class PolicySource(StrictModel):
    name: str
    path: str
    version: str
    git_blob_sha: str = Field(pattern=r"^[0-9a-f]{40}$")


class PublicationPolicy(StrictModel):
    policy_version: str
    graph_schema_version: str
    release_gate: Gate
    standards: tuple[PolicySource, ...]


class PolicyError(RuntimeError):
    pass


GATE_ORDER = {Gate.ALLOW: 0, Gate.REVIEW: 1, Gate.HALT: 2}

ALLOWED_EDGE_ENDPOINTS = {
    EdgeType.HAS_SCOPE: ("Engagement", "Scope"),
    EdgeType.REQUIRES_EVIDENCE: ("Scope", "EvidenceRequirement"),
    EdgeType.SATISFIES: ("EvidenceArtifact", "EvidenceRequirement"),
    EdgeType.SUPPORTS: ("EvidenceArtifact", "Claim"),
    EdgeType.CONTRADICTS: ("Claim", "Claim"),
    EdgeType.SUPPORTS_FINDING: ("Claim", "Finding"),
    EdgeType.SUPPORTED_BY: ("Finding", "EvidenceArtifact"),
    EdgeType.IDENTIFIES: ("Finding", "ControlGap"),
    EdgeType.ADDRESSED_BY: ("ControlGap", "Remediation"),
    EdgeType.VERIFIED_BY: ("Remediation", "Verification"),
}

REQUIRED_BASE_EDGES = {
    EdgeType.HAS_SCOPE,
    EdgeType.REQUIRES_EVIDENCE,
    EdgeType.SATISFIES,
    EdgeType.SUPPORTS,
    EdgeType.SUPPORTS_FINDING,
    EdgeType.SUPPORTED_BY,
    EdgeType.IDENTIFIES,
    EdgeType.ADDRESSED_BY,
    EdgeType.VERIFIED_BY,
}

CERTIFICATION_PATTERN = re.compile(r"\b(certify|certified|certification|compliant)\b", re.IGNORECASE)
HOSTILE_INSTRUCTION_PATTERN = re.compile(
    r"\b(ignore (?:all |the )?(?:previous|prior) instructions|reveal (?:a |the )?secret|system prompt)\b",
    re.IGNORECASE,
)


def load_policy(path: Path) -> PublicationPolicy:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PolicyError(f"publication policy cannot be loaded: {exc}") from exc
    return PublicationPolicy.model_validate(data)


def verify_policy_sources(policy: PublicationPolicy, repository_root: Path) -> None:
    """Verify the exact Git blob content declared by the policy profile."""
    for standard in policy.standards:
        source_path = repository_root / standard.path
        try:
            content = source_path.read_bytes()
        except OSError as exc:
            raise PolicyError(f"policy source cannot be read: {standard.path}: {exc}") from exc
        git_blob = hashlib.sha1(
            f"blob {len(content)}\0".encode("utf-8") + content,
            usedforsecurity=False,
        ).hexdigest()
        if git_blob != standard.git_blob_sha:
            raise PolicyError(
                f"policy source drift: {standard.path} expected {standard.git_blob_sha}, found {git_blob}"
            )


def evidence_content_payload(evidence: EvidenceArtifact) -> dict[str, str]:
    return {
        "observation": evidence.observation,
        "source_locator": evidence.source_locator,
        "source_version": evidence.source_version,
    }


def _max_gate(*gates: Gate) -> Gate:
    return max(gates, key=GATE_ORDER.__getitem__)


def evaluate_publication(fixture: AssessmentFixture, policy: PublicationPolicy) -> GateEvaluation:
    if fixture.versions.policy != policy.policy_version:
        raise PolicyError("fixture and publication policy versions differ")
    if fixture.versions.graph_schema != policy.graph_schema_version:
        raise PolicyError("fixture and graph schema versions differ")

    nodes = {node.node_id: node for node in fixture.nodes}
    evidence = {
        node.node_id: node
        for node in fixture.nodes
        if isinstance(node, EvidenceArtifact)
    }
    claims = {node.node_id: node for node in fixture.nodes if isinstance(node, Claim)}
    findings = {node.node_id: node for node in fixture.nodes if isinstance(node, Finding)}
    scopes = {node.node_id: node for node in fixture.nodes if isinstance(node, Scope)}
    gaps = {node.node_id: node for node in fixture.nodes if isinstance(node, ControlGap)}
    remediations = {
        node.node_id: node for node in fixture.nodes if isinstance(node, Remediation)
    }
    verifications = {
        node.node_id: node for node in fixture.nodes if isinstance(node, Verification)
    }

    evidence_gate = Gate.ALLOW
    authority_gate = Gate.ALLOW
    evidence_reasons: set[str] = set()
    authority_reasons: set[str] = set()

    seen_edge_types = {edge.edge_type for edge in fixture.edges}
    if REQUIRED_BASE_EDGES - seen_edge_types:
        evidence_gate = Gate.HALT
        evidence_reasons.add("OI-GRAPH-PATH-001")
    for edge in fixture.edges:
        expected = ALLOWED_EDGE_ENDPOINTS.get(edge.edge_type)
        actual = (nodes[edge.from_id].node_type, nodes[edge.to_id].node_type)
        if expected is None or expected != actual:
            evidence_gate = Gate.HALT
            evidence_reasons.add("OI-GRAPH-EDGE-001")

    supporting_evidence_by_claim: dict[str, set[str]] = {}
    supporting_claims_by_finding: dict[str, set[str]] = {}
    supporting_evidence_by_finding: dict[str, set[str]] = {}
    scopes_by_requirement: dict[str, set[str]] = {}
    requirements_by_evidence: dict[str, set[str]] = {}
    for edge in fixture.edges:
        if edge.edge_type == EdgeType.SUPPORTS:
            supporting_evidence_by_claim.setdefault(edge.to_id, set()).add(edge.from_id)
        elif edge.edge_type == EdgeType.SUPPORTS_FINDING:
            supporting_claims_by_finding.setdefault(edge.to_id, set()).add(edge.from_id)
        elif edge.edge_type == EdgeType.SUPPORTED_BY:
            supporting_evidence_by_finding.setdefault(edge.from_id, set()).add(edge.to_id)
        elif edge.edge_type == EdgeType.REQUIRES_EVIDENCE:
            scopes_by_requirement.setdefault(edge.to_id, set()).add(edge.from_id)
        elif edge.edge_type == EdgeType.SATISFIES:
            requirements_by_evidence.setdefault(edge.from_id, set()).add(edge.to_id)

    for artifact in evidence.values():
        expected_hash = sha256_json(evidence_content_payload(artifact))
        if artifact.content_sha256 != expected_hash:
            evidence_gate = Gate.HALT
            evidence_reasons.update({"EVID-INTEG-001", "DL-INTEGRITY-001"})
        if artifact.source_type == "safe_test":
            applicable_scope_ids = {
                scope_id
                for requirement_id in requirements_by_evidence.get(artifact.node_id, set())
                for scope_id in scopes_by_requirement.get(requirement_id, set())
            }
            authorization_is_valid = bool(artifact.authorization_ref) and bool(
                applicable_scope_ids
            ) and all(
                artifact.authorization_ref in scopes[scope_id].authorization_refs
                for scope_id in applicable_scope_ids
            )
            if not authorization_is_valid:
                evidence_gate = Gate.HALT
                evidence_reasons.update({"EVID-AUTH-001", "EVID-TEST-001"})
        if artifact.review_state in {"rejected", "superseded"}:
            continue
        if artifact.review_state == "limited" or artifact.evidence_strength == "insufficient":
            evidence_gate = _max_gate(evidence_gate, Gate.REVIEW)
            evidence_reasons.add("PUB-EVID-LIMITED-001")
        if HOSTILE_INSTRUCTION_PATTERN.search(artifact.observation):
            evidence_gate = _max_gate(evidence_gate, Gate.REVIEW)
            evidence_reasons.add("OI-EVID-UNTRUSTED-INSTRUCTION")

    for claim in claims.values():
        missing = sorted(set(claim.evidence_refs) - set(evidence))
        if missing:
            evidence_gate = Gate.HALT
            evidence_reasons.update({"EVID-TRACE-001", "DL-TRACE-001"})
        if set(claim.evidence_refs) != supporting_evidence_by_claim.get(claim.node_id, set()):
            evidence_gate = Gate.HALT
            evidence_reasons.update({"EVID-TRACE-001", "DL-TRACE-001"})

    for finding in findings.values():
        missing_evidence = sorted(set(finding.evidence_refs) - set(evidence))
        missing_claims = sorted(set(finding.claim_refs) - set(claims))
        if finding.material and (not finding.evidence_refs or missing_evidence):
            evidence_gate = Gate.HALT
            evidence_reasons.update({"DL-EVID-001", "PUB-EVID-001"})
            if missing_evidence:
                evidence_reasons.update({"EVID-TRACE-001", "DL-TRACE-001"})
        if missing_claims:
            evidence_gate = Gate.HALT
            evidence_reasons.add("DL-TRACE-001")
        if set(finding.claim_refs) != supporting_claims_by_finding.get(finding.node_id, set()):
            evidence_gate = Gate.HALT
            evidence_reasons.add("DL-TRACE-001")
        if set(finding.evidence_refs) != supporting_evidence_by_finding.get(
            finding.node_id, set()
        ):
            evidence_gate = Gate.HALT
            evidence_reasons.update({"EVID-TRACE-001", "DL-TRACE-001"})
        admitted = [
            evidence[ref]
            for ref in finding.evidence_refs
            if ref in evidence and evidence[ref].review_state in {"accepted", "limited"}
        ]
        if finding.material and not admitted:
            evidence_gate = Gate.HALT
            evidence_reasons.update({"DL-EVID-001", "PUB-EVID-001"})
        language = " ".join(
            (finding.observation, finding.interpretation, finding.business_impact)
        )
        if CERTIFICATION_PATTERN.search(language):
            authority_gate = Gate.HALT
            authority_reasons.update({"PUB-LANGUAGE-001", "DL-LANG-001"})

    for gap in gaps.values():
        if set(gap.finding_refs) - set(findings):
            evidence_gate = Gate.HALT
            evidence_reasons.add("DL-TRACE-001")
    for remediation in remediations.values():
        if set(remediation.control_gap_refs) - set(gaps):
            evidence_gate = Gate.HALT
            evidence_reasons.add("DL-TRACE-001")
        if not remediation.advisory_only or remediation.implementation_authorized:
            authority_gate = Gate.HALT
            authority_reasons.update({"PUB-AUTH-001", "DL-IMPL-001"})
    for verification in verifications.values():
        if verification.remediation_ref not in remediations:
            evidence_gate = Gate.HALT
            evidence_reasons.add("DL-TRACE-001")
        if set(verification.evidence_refs) - set(evidence):
            evidence_gate = Gate.HALT
            evidence_reasons.update({"EVID-TRACE-001", "DL-TRACE-001"})
        if verification.status != "verified":
            evidence_gate = _max_gate(evidence_gate, Gate.REVIEW)
            evidence_reasons.add("OI-VERIFICATION-INCOMPLETE")

    contradiction_edges = [edge for edge in fixture.edges if edge.edge_type == EdgeType.CONTRADICTS]
    for edge in contradiction_edges:
        left = claims.get(edge.from_id)
        right = claims.get(edge.to_id)
        if left is None or right is None:
            evidence_gate = Gate.HALT
            evidence_reasons.add("OI-GRAPH-EDGE-001")
            continue
        if left.subject_key != right.subject_key or left.stance == right.stance:
            evidence_gate = Gate.HALT
            evidence_reasons.add("OI-GRAPH-CONFLICT-MALFORMED")
        else:
            evidence_gate = _max_gate(evidence_gate, Gate.REVIEW)
            evidence_reasons.add("OI-GRAPH-CONFLICT-001")

    claim_stances_by_subject: dict[str, set[str]] = {}
    for claim in claims.values():
        claim_stances_by_subject.setdefault(claim.subject_key, set()).add(claim.stance)
    if any(
        {"supports", "refutes"} <= stances
        for stances in claim_stances_by_subject.values()
    ):
        evidence_gate = _max_gate(evidence_gate, Gate.REVIEW)
        evidence_reasons.add("OI-GRAPH-CONFLICT-001")

    request = fixture.publication_request
    if request.implementation_authorized:
        authority_gate = Gate.HALT
        authority_reasons.update({"PUB-AUTH-001", "DL-IMPL-001"})
    if request.claims_certification or CERTIFICATION_PATTERN.search(request.client_safe_summary):
        authority_gate = Gate.HALT
        authority_reasons.update({"PUB-LANGUAGE-001", "DL-LANG-001"})
    if not request.quality_control_ref:
        authority_gate = _max_gate(authority_gate, Gate.REVIEW)
        authority_reasons.add("PUB-QC-001")
    if not request.publication_approver:
        authority_gate = _max_gate(authority_gate, Gate.REVIEW)
        authority_reasons.add("DL-APPROVAL-001")

    if policy.release_gate != Gate.ALLOW:
        authority_gate = _max_gate(authority_gate, policy.release_gate)
        authority_reasons.add("PUB-POLICY-GATE-001")

    final_gate = _max_gate(evidence_gate, authority_gate)
    if final_gate == Gate.HALT:
        publication_state = PublicationState.BLOCKED
    elif final_gate == Gate.REVIEW:
        publication_state = PublicationState.PROVISIONAL
    else:
        publication_state = request.requested_state

    evidence_snapshot = [
        {
            "evidence_id": item.node_id,
            "content_sha256": item.content_sha256,
            "source_version": item.source_version,
        }
        for item in sorted(evidence.values(), key=lambda value: value.node_id)
    ]
    return GateEvaluation(
        evidence_gate=evidence_gate,
        publication_authority_gate=authority_gate,
        final_publication_gate=final_gate,
        publication_state=publication_state,
        reason_codes=tuple(sorted(evidence_reasons | authority_reasons)),
        evidence_refs=tuple(item["evidence_id"] for item in evidence_snapshot),
        evidence_snapshot_sha256=sha256_json(evidence_snapshot),
    )
