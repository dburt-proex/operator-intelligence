# Roadmap Standard

Version: v0.1 governance foundation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Draft foundation for commercial v1.0

## 1. Purpose

This standard governs how Operator Intelligence converts approved recommendations into a sequenced, client-safe implementation roadmap.

It defines phase assignment, dependency handling, entry and exit gates, ownership, acceptance evidence, change control, blocked work, and DecisionLedger traceability.

This standard does not create findings, redefine scores, or replace package eligibility rules in `framework/recommendation-index.md`.

## 2. Governing principle

A roadmap is a controlled sequence of authorized work, not a prioritized wish list.

No item advances because it appears valuable, urgent, or commercially attractive. It advances only when its evidence, prerequisites, owner, authority, scope, and acceptance conditions satisfy the applicable gate.

## 3. Required source chain

Every roadmap item must preserve this trace:

```text
Evidence Record
  → Governed Finding
  → Risk and Impact Classification
  → Approved Recommendation
  → Canonical Package Route
  → Roadmap Phase
  → Entry Gate
  → Acceptance Criteria
  → Completion Evidence
  → DecisionLedger Record
```

A broken source chain blocks client-facing roadmap use.

## 4. Canonical roadmap phases

| Phase | Name | Primary purpose |
|---|---|---|
| `1` | Quick Wins | Correct verified critical friction, accuracy, access, or buyer-path failures with bounded scope. |
| `2` | Growth Foundation | Establish service, proof, local presence, content, and conversion foundations required for durable growth work. |
| `3` | Automation and Reporting | Standardize workflows, ownership, system-of-record use, follow-up, measurement, and reporting. |
| `4` | Governed AI Enablement | Introduce bounded AI assistance only after workflow, data, privacy, review, escalation, logging, and QA controls pass. |

These phases are dependency defaults, not promises of duration or financial outcome.

## 5. Minimum roadmap item

```yaml
roadmap_item_id: OI-RM-YYYY-NNN
recommendation_id: OI-REC-YYYY-NNN
finding_refs: []
evidence_refs: []
ledger_refs: []
primary_package_id: ""
roadmap_phase: 1|2|3|4
sequence_rank: 0
status: proposed|validation_required|approved|blocked|in_progress|complete|deferred|rejected
review_state: ALLOW|REVIEW|HALT
owner: ""
decision_authority: ""
prerequisites: []
dependencies: []
blocked_conditions: []
included_scope: []
excluded_scope: []
entry_criteria: []
acceptance_criteria: []
completion_evidence_refs: []
measurement_plan: []
unknowns: []
confidence: high|medium|low|unknown
target_window: ""
decision_reason: ""
```

Required fields may not be replaced by narrative implication.

## 6. Admission rules

A recommendation may enter a roadmap only when:

- its source finding and evidence are traceable
- confidence is assigned separately from maturity
- unknowns and blocked conditions are explicit
- one primary package is assigned
- included and excluded scope are defined
- prerequisites and dependencies are identified
- phase assignment follows the root condition and dependency state
- ownership and decision authority are identified
- entry and acceptance criteria are observable
- implementation authorization is recorded separately from publication approval
- a DecisionLedger reference exists

Unknown or low-confidence conditions normally enter as `validation_required`, not implementation work.

## 7. Phase assignment rules

Assign the earliest phase that is both appropriate and eligible.

### Phase 1 — Quick Wins

Use when evidence supports a bounded correction that:

- resolves a visible critical failure or accuracy issue
- does not depend on undefined strategy or workflow
- has limited implementation risk
- can be verified with direct acceptance evidence

Do not use Phase 1 to bypass discovery, package scope, or governance review.

### Phase 2 — Growth Foundation

Use when work establishes or strengthens:

- service and location coverage
- offer clarity
- buyer-facing proof
- local profile accuracy and authority
- content usefulness
- conversion foundations

Phase 2 work must not scale unsupported services, claims, locations, or capacity.

### Phase 3 — Automation and Reporting

Use only when:

- the workflow is documented
- owners, stages, triggers, exceptions, and handoffs are defined
- the system of record is known
- metric definitions and sources are identified where reporting is involved
- access and implementation authority exist

Do not automate an undefined workflow or build dashboards without named decision use.

### Phase 4 — Governed AI Enablement

Use only when all material AI-readiness prerequisites pass:

- bounded use case
- documented workflow
- structured inputs
- approved knowledge sources
- privacy and permission controls
- allowed and blocked topics
- human review rules
- escalation path
- audit logging
- QA owner and cadence
- explicit `ALLOW`, `REVIEW`, or `HALT` state

Any unresolved `HALT` condition blocks dependent AI implementation.

## 8. Dependency rules

Dependencies must be recorded as relationships, not hidden inside phase labels.

Rules:

1. A dependent item cannot begin before required prerequisite evidence exists.
2. A higher phase cannot override an unresolved lower-phase dependency.
3. Parallel work is allowed only when workstreams do not share a blocking prerequisite.
4. A package may be a prerequisite without becoming a second primary package.
5. Circular dependencies require governance review and decomposition.
6. Missing access, ownership, or authority must be represented as blocked conditions.

## 9. Sequence ranking

Sequence rank must reflect:

- safety, legal, privacy, policy, or authorization exposure
- critical buyer or operational failure
- dependency order
- evidence strength
- impact and reach
- implementation effort
- client capacity
- reversibility
- measurement readiness

Priority score alone cannot determine sequence.

Do not place a high-opportunity item ahead of a control, access, data, or workflow prerequisite solely because its commercial upside appears larger.

## 10. Entry gates

Before an item moves to `approved` or `in_progress`, confirm:

- source evidence remains current enough for the decision
- scope is approved
- owner accepts responsibility
- decision authority is documented
- required access is available
- prerequisites are complete or formally waived by authorized review
- blocked conditions are resolved
- acceptance criteria are testable
- rollback or escalation needs are defined where material
- implementation does not exceed the approved package boundary

Failure of a material gate routes the item to `validation_required`, `blocked`, `deferred`, or `HALT`.

## 11. Completion rules

An item is `complete` only when:

- included scope is delivered
- every material acceptance criterion passes
- completion evidence is recorded
- known exceptions are documented
- unresolved defects or limitations are assigned an owner and state
- relevant operating documentation is updated
- the DecisionLedger contains the completion decision

Deliverable existence alone does not prove completion.

Implementation completion remains separate from outcome validation.

## 12. Unknown and blocked handling

Unknown is not failure and must not be converted to zero, urgency, or implementation scope.

For each material unknown, record:

- missing evidence
- why it matters
- minimum validation action
- owner where known
- effect on sequencing

Use `blocked` when access, authority, privacy, safety, legal, policy, data, technical, or control conditions prevent defensible progress.

Blocked items retain their source evidence, package route, and dependency relationships.

## 13. Capacity and scheduling controls

Target windows are planning fields, not guarantees.

A roadmap must disclose material capacity constraints involving:

- client approvals
- content or asset production
- technical access
- internal ownership
- vendor dependencies
- data availability
- testing windows
- operational change load

Do not assign dates that assume unresolved dependencies will clear without evidence.

## 14. Measurement boundaries

Every roadmap item must distinguish:

- implementation evidence
- operational adoption
- leading indicators
- business outcomes
- unverified expected effects

Do not promise or infer traffic, rankings, leads, close rate, savings, revenue, market share, or ROI without validated baseline and post-implementation evidence.

Measurement plans must identify the metric definition, source, baseline state, review window, owner, limitation, and decision triggered by the result.

## 15. Change control

Reopen roadmap review when any of the following changes materially:

- evidence or finding interpretation
- confidence
- risk or impact
- package route
- included or excluded scope
- prerequisite or dependency
- phase assignment
- ownership or authority
- implementation conditions
- acceptance criteria
- measurement plan

Material changes require a new or amended DecisionLedger record. Silent resequencing is prohibited.

## 16. Executive-safe language

Client-facing roadmaps must distinguish verified work, validation work, blocked work, and expected operational effects.

Preferred language:

> Phase 3 begins after the inquiry workflow, ownership rules, and source-system fields are approved. The sequence is designed to prevent automation from formalizing an undefined process. Business outcome effects will be evaluated after implementation and adoption evidence are available.

Prohibited language includes unsupported certainty about revenue, lead volume, rankings, savings, completion dates, or ROI.

## 17. DecisionLedger requirements

Each roadmap decision must record:

- roadmap item ID
- recommendation and finding references
- evidence references
- assigned phase and sequence rank
- primary package
- prerequisites and blocked conditions
- owner and decision authority
- decision state and reason
- approval or escalation record
- acceptance criteria
- change history
- completion evidence where applicable

## 18. Validation codes

| Code | Condition |
|---|---|
| `ROAD-SOURCE-001` | Required evidence, finding, recommendation, or ledger trace is missing. |
| `ROAD-PHASE-001` | Phase assignment conflicts with prerequisites or root condition. |
| `ROAD-DEP-001` | A dependency is missing, circular, or bypassed. |
| `ROAD-AUTH-001` | Ownership, access, or decision authority is missing. |
| `ROAD-SCOPE-001` | Scope exceeds the approved recommendation or package boundary. |
| `ROAD-ACCEPT-001` | Acceptance criteria or completion evidence are insufficient. |
| `ROAD-UNKNOWN-001` | A material unknown is hidden or treated as failure. |
| `ROAD-AI-001` | Phase 4 work lacks required readiness controls or has an unresolved `HALT`. |
| `ROAD-LANG-001` | Client language contains unsupported outcome certainty. |
| `ROAD-LEDGER-001` | Roadmap creation, change, or completion lacks DecisionLedger traceability. |

Any unresolved validation code blocks official roadmap release or the affected item's advancement.

## 19. Governance checklist

Before release, confirm:

- every item has a valid source chain
- exactly one primary package is assigned per recommendation
- phase and sequence respect prerequisites
- unknowns and blocked conditions remain visible
- ownership and authority are named
- entry and acceptance criteria are observable
- Phase 4 controls are complete
- implementation and outcome validation are separate
- client language is evidence-bound
- all decisions and changes are ledgered

## 20. Cross references

- `framework/lifecycle-roadmap-map.md`
- `framework/recommendation-index.md`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/publication-standard.md`
- `standards/recommendation-standard.md`
- `scoring/recommendation-map.md`
- `templates/roadmap.md`
- `templates/decision-ledger.md`
