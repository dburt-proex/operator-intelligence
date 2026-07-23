# Agentic Control Platform Readiness Gap Register

Version: 0.1.0
Purpose: Source-of-truth register for control findings and decision effects

## Register control

```yaml
assessment_id: ""
register_version: "0.1.0"
evidence_snapshot_date: YYYY-MM-DD
owner: ""
independent_reviewer: ""
publication_state: internal_only|official|provisional|range_only|blocked
ledger_refs: []
implementation_authorized: false
```

## Finding record

```yaml
finding_id: ACPR-F-DOMAIN-NNN
finding_version: "1.0"
supersedes: null
assessment_id: ""
domain_id: AIGR-D1|AIGR-D2|AIGR-D3|AIGR-D4|AIGR-D5|AIGR-D6|AIGR-D7
control_refs: []
control_plane: governance|change_time|runtime|assurance
state: VERIFIED_GAP|PARTIAL_CONTROL|CONTROLLED|UNKNOWN|NOT_APPLICABLE
severity: critical|high|medium|low|informational
observation: ""
interpretation: ""
platform_decision_effect: ""
evidence_refs: []
contradictory_evidence_refs: []
evidence_strength: high|medium|low|insufficient
confidence: high|medium|low|unknown
confidence_basis: ""
assumptions: []
limitations: []
unknowns: []
validation_required: []
remediation_condition: ""
owner: ""
decision_authority: ""
target_gate: pre_procurement|pre_configuration|pre_pilot|pre_expansion|monitoring
dependencies: []
acceptance_criteria: []
acceptance_evidence: []
control_gate: ALLOW|REVIEW|HALT
review_state: candidate|validation_required|validated|blocked|published|closed|superseded
recommendation_refs: []
roadmap_refs: []
ledger_refs: []
```

## Deterministic state rules

| State | Rule | Required route |
|---|---|---|
| `NOT_APPLICABLE` | Decision authority approves a documented scope test showing the control does not apply | Retain rationale; remove from denominator |
| `UNKNOWN` | Evidence is absent, rejected, unauthorized, conflicting, or insufficient | Validation plus `REVIEW`; `HALT` if safe continuation requires inference |
| `VERIFIED_GAP` | Admitted evidence directly shows a required control is absent or ineffective | Route by severity and decision effect |
| `PARTIAL_CONTROL` | Admitted evidence shows a control exists but material scope, consistency, enforcement, ownership, or evidence limits remain | Owner, remediation condition, and gate required |
| `CONTROLLED` | Admitted evidence shows the control is defined, authorized, operating, and effective for the reviewed scope and sample | Bounded conclusion only |

## Materiality and evidence rules

- `VERIFIED_GAP`, `PARTIAL_CONTROL`, and `CONTROLLED` require at least one admitted `evidence_ref`.
- Critical or high findings require a named owner, decision authority, target gate, acceptance criteria, and DecisionLedger reference.
- `UNKNOWN` cannot be converted to a negative score or implementation recommendation.
- A designed control without operating evidence cannot be marked `CONTROLLED`.
- Contradictory evidence routes to `REVIEW` unless a governed resolution is recorded.
- Approved or published findings are superseded; they are never silently overwritten.

## Register view

| Finding ID | Domain | Plane | State | Severity | Confidence | Decision effect | Owner | Target gate | Gate | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

## Quality gate

- [ ] Each finding has one primary domain and one control plane.
- [ ] Material finding evidence resolves and passed admission.
- [ ] Observation, interpretation, and decision effect are separated.
- [ ] Unknowns and contradictions remain visible.
- [ ] Severity does not override confidence.
- [ ] Change-time and runtime gaps are distinguishable.
- [ ] Material remediation has an owner, authority, dependency, gate, and acceptance evidence.
- [ ] DecisionLedger and supersession references resolve.
- [ ] Implementation authorization remains false unless separately granted.
