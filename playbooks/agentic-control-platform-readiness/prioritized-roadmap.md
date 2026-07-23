# Agentic Control Platform Readiness Roadmap

Version: 0.1.0
Purpose: Sequence validation and remediation without authorizing implementation

## Roadmap control

```yaml
roadmap_id: ACPR-RM-YYYY-NNN
assessment_id: ""
version: "1.0"
evidence_snapshot_date: YYYY-MM-DD
owner: ""
decision_authority: ""
publication_state: internal_only|official|provisional|range_only|blocked
decision: READY|CONDITIONAL|NOT_READY|BLOCKED
control_gate: ALLOW|REVIEW|HALT
ledger_refs: []
implementation_authorized: false
```

## Sequencing model

| Gate | Objective | Exit evidence |
|---|---|---|
| `pre_procurement` | Resolve scope, ownership, inventory, requirements, authority, conflicts, and critical unknowns before a platform commitment | Approved requirement baseline and decision record |
| `pre_configuration` | Define target architecture, systems of record, identity/data boundaries, integrations, control ownership, and operating model | Approved design and implementation boundary |
| `pre_pilot` | Configure and test change-time, runtime, approval, logging, evaluation, containment, and recovery controls in a safe environment | Passed acceptance fixtures and reviewed exceptions |
| `pre_expansion` | Validate operating evidence, coverage, reliability, incident readiness, adoption, and unresolved gaps before adding authority or scope | Independent readiness review and expansion decision |
| `monitoring` | Review drift, access, incidents, exceptions, control effectiveness, realized value, and retirement decisions | Periodic DecisionLedger event |

## Roadmap item

```yaml
item_id: ACPR-RM-ITEM-NNN
finding_refs: []
recommendation_ref: ""
action: ""
target_gate: pre_procurement|pre_configuration|pre_pilot|pre_expansion|monitoring
priority_score: 0
priority_band: critical|high|medium|low
criticality: 1
platform_decision_effect: 1
evidence_strength: 1
dependency_leverage: 1
confidence: high|medium|low|unknown
owner: ""
decision_authority: ""
dependencies: []
blocked_by: []
included_scope: []
excluded_scope: []
acceptance_criteria: []
acceptance_evidence: []
target_window: ""
status: proposed|validation_required|approved|blocked|authorized|in_progress|complete|monitoring|deferred|rejected|cancelled
control_gate: ALLOW|REVIEW|HALT
implementation_authorized: false
ledger_refs: []
```

## Required ordering rules

1. Authority, evidence integrity, data handling, and critical unknowns precede procurement recommendations.
2. Inventory, ownership, systems of record, identity/data boundaries, and integration decisions precede configuration.
3. Change-time and runtime controls must each pass safe acceptance tests before pilot.
4. Critical permissions, approval, logging, evaluation, containment, and recovery gaps block pilot.
5. Operating evidence and independent review precede authority or scope expansion.
6. Implementation authorization is separate for each approved scope; roadmap approval is insufficient.

## Working register

| Rank | Item | Gate | Priority | Confidence | Owner | Dependencies | Acceptance evidence | Control gate | Status |
|---:|---|---|---:|---|---|---|---|---|---|
| | | | | | | | | | |

## Acceptance review

- [ ] Every item traces to a governed finding or validation requirement.
- [ ] Priority inputs reproduce.
- [ ] Confidence remains a gate rather than a multiplier.
- [ ] Critical unknowns are not scheduled as implementation work.
- [ ] Each item has an owner and decision authority.
- [ ] Dependencies and blockers are explicit.
- [ ] Acceptance criteria are observable and bounded.
- [ ] Required evidence distinguishes design, implementation completion, operating effectiveness, and realized value.
- [ ] No target window is represented as guaranteed.
- [ ] Start requires separate implementation authorization.
