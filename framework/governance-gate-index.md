# Operator Intelligence Governance Gate Index

Version: v0.1 control-layer foundation  
Stage alignment: Stage 2 — `framework/`  
Folder alignment: `framework/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file is the canonical index of governance gates used across Operator Intelligence.

It provides one decision vocabulary for evidence collection, scoring, findings, risk, opportunities, recommendations, reports, proposals, implementation, AI use, measurement, and methodology maintenance.

## v1.0 connection

Commercial v1.0 requires predictable control boundaries so that two evaluators using the same evidence do not advance materially different recommendations merely because they apply different judgment standards.

This index strengthens v1.0 readiness by providing:

- stable gate identifiers
- common pass, review, halt, and validation outcomes
- stage-specific admission and exit controls
- escalation and approval rules
- report, proposal, and implementation boundaries
- control ownership and evidence requirements
- DecisionLedger traceability
- methodology-change governance

## Core gate outcomes

| Outcome | Meaning | Allowed next action |
|---|---|---|
| `PASS` | Gate requirements are satisfied | Advance within approved scope |
| `PASS_WITH_CONDITIONS` | Requirements mostly pass, with explicit conditions and owner | Advance only under recorded conditions |
| `VALIDATE` | Evidence or authority is insufficient | Collect evidence; do not assert conclusion |
| `REVIEW` | Human approval or expert judgment is required | Pause execution pending named review |
| `DEFER` | Work is valid but a prerequisite or higher-priority dependency must occur first | Sequence later |
| `MONITOR` | Condition is not currently actionable but requires observation | Track defined signals |
| `HALT` | Execution or publication would violate a critical boundary | Stop until controls are restored |
| `REJECT` | Proposed finding, recommendation, scope, or change is not valid | Remove or redesign |
| `CLOSE` | Acceptance, transfer, and monitoring requirements are satisfied | Complete workstream |

## Gate severity

| Severity | Meaning |
|---|---|
| `G1 Advisory` | Quality improvement; failure may reduce usefulness but does not block |
| `G2 Required` | Failure blocks stage admission or report/proposal use |
| `G3 Escalation` | Failure requires named human review and explicit approval |
| `G4 Control Boundary` | Failure requires HALT because customer, privacy, legal, policy, safety, financial, or irreversible exposure exists |

## Canonical gate record

```yaml
gate_id: OI-GATE-DOMAIN-NNN
gate_name: ""
severity: G2
lifecycle_states: []
applies_to: []
owner_role: ""
pass_requirements: []
required_evidence: []
fail_outcome: VALIDATE
conditions: []
approvals_required: []
escalation_route: ""
ledger_ref: OI-DL-YYYY-NNN
```

## Universal gates

| Gate ID | Gate | Severity | Pass requirement | Failure outcome |
|---|---|---|---|---|
| `OI-GATE-UNI-001` | Evidence Gate | G2 | Observation has sufficient direct evidence or an explicit validation gap | VALIDATE |
| `OI-GATE-UNI-002` | Confidence Gate | G2 | Confidence matches evidence quality and limitations | VALIDATE |
| `OI-GATE-UNI-003` | Unknown Data Gate | G2 | Unknowns are explicit and are not silently scored as failure | REJECT or VALIDATE |
| `OI-GATE-UNI-004` | Accuracy Gate | G3 | Claims, services, locations, policies, credentials, prices, and capabilities are verified | REVIEW or HALT |
| `OI-GATE-UNI-005` | Root Domain Gate | G2 | One primary domain owns the condition | VALIDATE |
| `OI-GATE-UNI-006` | Duplicate Control Gate | G2 | One root condition is not counted as several independent findings or benefits | REJECT |
| `OI-GATE-UNI-007` | Materiality Gate | G2 | Condition affects a defined buyer, operating, risk, or decision outcome | REJECT |
| `OI-GATE-UNI-008` | Client Language Gate | G2 | Wording is executive-safe and does not overstate certainty or blame | REVIEW |
| `OI-GATE-UNI-009` | Ledger Gate | G2 | Decision can be traced through required DecisionLedger fields | HALT admission |
| `OI-GATE-UNI-010` | Ownership Gate | G2 | Responsible owner and decision authority are named | DEFER |
| `OI-GATE-UNI-011` | Dependency Gate | G2 | Prerequisites and blockers are identified and sequenced | DEFER |
| `OI-GATE-UNI-012` | Acceptance Gate | G2 | Completion can be tested through explicit acceptance criteria | REJECT scope |
| `OI-GATE-UNI-013` | Measurement Gate | G2 | Baseline or validation metric is defined, or limitation is explicit | VALIDATE |
| `OI-GATE-UNI-014` | Scope Boundary Gate | G3 | Included and excluded scope are explicit | REVIEW |
| `OI-GATE-UNI-015` | Change Control Gate | G3 | Material changes are recorded and reapproved | HALT changed work |

## Lifecycle gates

| Gate ID | Gate | Lifecycle state | Pass requirement | Failure outcome |
|---|---|---|---|---|
| `OI-GATE-LC-001` | Qualification Fit | OI-LC-01 | Product, authority, need, capacity, and commercial fit are sufficient | DEFER or REJECT |
| `OI-GATE-LC-002` | Intake Completeness | OI-LC-02 | Required context exists or unknowns have owners and validation plans | VALIDATE |
| `OI-GATE-LC-003` | Surface Coverage | OI-LC-03 | In-scope surfaces and systems are inventoried | VALIDATE |
| `OI-GATE-LC-004` | Evidence Coverage | OI-LC-04 | Evidence thresholds or unknown handling pass | VALIDATE |
| `OI-GATE-LC-005` | Scoring Admission | OI-LC-05 | Criteria, weights, confidence, and unknown treatment reconcile | HALT scoring |
| `OI-GATE-LC-006` | Finding Admission | OI-LC-06 | Canonical finding and root domain resolve | VALIDATE |
| `OI-GATE-LC-007` | Synthesis Admission | OI-LC-07 | Risk, opportunity, effort, and value states are governed | VALIDATE |
| `OI-GATE-LC-008` | Recommendation Admission | OI-LC-08 | Package eligibility, prerequisites, scope, and acceptance pass | DEFER or REJECT |
| `OI-GATE-LC-009` | Report Admission | OI-LC-09 | Every client-facing claim passes evidence, confidence, impact, routing, and language controls | HALT publication |
| `OI-GATE-LC-010` | Client Decision | OI-LC-10 | Decision-maker and explicit decision are recorded | REVIEW |
| `OI-GATE-LC-011` | Implementation Readiness | OI-LC-11 | Scope, access, owners, approvals, schedule state, and change rules are complete | HALT start |
| `OI-GATE-LC-012` | Implementation Acceptance | OI-LC-12 | Deliverables, testing, evidence, and acceptance pass | REWORK or REVIEW |
| `OI-GATE-LC-013` | Measurement Readiness | OI-LC-13 | Baseline, metric, owner, period, and attribution limits exist | VALIDATE |
| `OI-GATE-LC-014` | Closure | OI-LC-14 | Acceptance, ownership transfer, unresolved risks, and archive are complete | REVIEW |

## Scoring gates

| Gate ID | Gate | Pass requirement | Failure outcome |
|---|---|---|---|
| `OI-GATE-SCORE-001` | Criterion Evidence | Score traces to evidence or approved unknown treatment | HALT criterion score |
| `OI-GATE-SCORE-002` | Anchor Consistency | Score uses approved 0, 25, 50, 75, or 100 anchors or documented interpolation rule | REVIEW |
| `OI-GATE-SCORE-003` | Weight Integrity | Active weights total 100% after approved normalization | HALT Operator Score |
| `OI-GATE-SCORE-004` | Category Coverage | Coverage and unknown proportion are disclosed | VALIDATE |
| `OI-GATE-SCORE-005` | Confidence Adjustment | Confidence treatment follows the scoring specification | HALT adjusted score |
| `OI-GATE-SCORE-006` | Double Count | One signal is not weighted through several overlapping criteria without boundary logic | REVIEW |
| `OI-GATE-SCORE-007` | Score Range | A range replaces false precision when material data is unknown | REVIEW |
| `OI-GATE-SCORE-008` | Operator Score Use | Score is explained with evidence and not used as a gimmick | REVIEW |

## Finding and synthesis gates

| Gate ID | Gate | Pass requirement | Failure outcome |
|---|---|---|---|
| `OI-GATE-FIND-001` | Canonical ID | Finding ID exists in an approved domain library | REJECT |
| `OI-GATE-FIND-002` | Observation Separation | Observation is recorded separately from interpretation | REVIEW |
| `OI-GATE-FIND-003` | Domain Boundary | Root condition and dependent domains are explicit | VALIDATE |
| `OI-GATE-FIND-004` | Impact | Impact language is material and evidence-safe | REVIEW |
| `OI-GATE-FIND-005` | Risk Severity | Severity, likelihood, reach, and evidence are not conflated | REVIEW |
| `OI-GATE-FIND-006` | Opportunity Eligibility | Opportunity has outcome, owner, capacity, effort, and package eligibility | VALIDATE |
| `OI-GATE-FIND-007` | Benefit Overlap | One benefit is not counted across several opportunities | REJECT |
| `OI-GATE-FIND-008` | Competitive Comparability | Competitors match service, geography, buyer, and date | VALIDATE |
| `OI-GATE-FIND-009` | Social Signal Boundary | Social evidence uses an existing governed domain until a social library is approved | REVIEW |

## Recommendation and commercial gates

| Gate ID | Gate | Severity | Pass requirement | Failure outcome |
|---|---|---|---|---|
| `OI-GATE-REC-001` | Package Eligibility | G2 | Evidence-backed condition matches the canonical package trigger | REJECT |
| `OI-GATE-REC-002` | Package-First Selling | G3 | Package is selected because it resolves the condition, not because it is sellable | REJECT |
| `OI-GATE-REC-003` | Primary Package | G2 | One primary package owns the recommendation | REVIEW |
| `OI-GATE-REC-004` | Prerequisite Routing | G2 | Required readiness work precedes growth or AI implementation | DEFER |
| `OI-GATE-REC-005` | Delivery Fit | G3 | Offer, capacity, geography, policy, and operational reality support the recommendation | REVIEW or HALT |
| `OI-GATE-REC-006` | Effort Completeness | G2 | Migration, governance, testing, client inputs, and access are included | REVIEW |
| `OI-GATE-REC-007` | Scope Clarity | G2 | Included and excluded work are explicit | REVIEW |
| `OI-GATE-REC-008` | Acceptance Criteria | G2 | Recommendation can be accepted through testable evidence | REJECT scope |
| `OI-GATE-REC-009` | Proposal Consistency | G3 | Proposal scope, phase, package, assumptions, and exclusions match the approved recommendation | HALT proposal |
| `OI-GATE-REC-010` | Price-Value Separation | G2 | Price is not represented as proof of value and value is not treated as guaranteed ROI | REVIEW |

## ROI and value gates

| Gate ID | Gate | Pass requirement | Failure outcome |
|---|---|---|---|
| `OI-GATE-ROI-001` | Value State | Qualitative, baseline, modeled, measured, or validated state is explicit | REVIEW |
| `OI-GATE-ROI-002` | Baseline | Metric definition, source, owner, and period exist | Use qualitative value |
| `OI-GATE-ROI-003` | Input Source | Every model input has a named source and confidence | REJECT input |
| `OI-GATE-ROI-004` | Cost Completeness | Implementation, recurring, client, migration, training, and governance cost are included when material | HALT ROI |
| `OI-GATE-ROI-005` | Attribution | Causality limits are disclosed | Reduce claim |
| `OI-GATE-ROI-006` | Capacity | Modeled demand or workload fits delivery capacity | Cap or HALT model |
| `OI-GATE-ROI-007` | Measurement Window | Window matches adoption, sales cycle, seasonality, and outcome lag | Extend window |
| `OI-GATE-ROI-008` | Double Counting | One benefit has one primary modeled owner | REJECT overlap |
| `OI-GATE-ROI-009` | Scenario Precision | Precision matches input confidence | Use range or qualitative value |
| `OI-GATE-ROI-010` | Guarantee Language | Modeled or observed value is not presented as guaranteed future performance | HALT publication |

## Data, automation, and AI gates

| Gate ID | Gate | Severity | Pass requirement | Failure outcome |
|---|---|---|---|---|
| `OI-GATE-DATA-001` | Data Source | G2 | System of record and owner are identified | VALIDATE |
| `OI-GATE-DATA-002` | Data Quality | G2 | Required fields, status, completeness, and limitations are known | REVIEW |
| `OI-GATE-DATA-003` | Access | G4 | Access is authorized and least privilege | HALT unauthorized work |
| `OI-GATE-AUTO-001` | Workflow Definition | G3 | Trigger, owner, states, handoffs, exceptions, and completion are defined | HALT automation |
| `OI-GATE-AUTO-002` | Failure Recovery | G3 | Missed, failed, duplicate, or delayed actions have recovery and alert paths | REVIEW or HALT |
| `OI-GATE-AUTO-003` | Customer Communication | G3 | Automated messages are accurate, approved, and recordable | REVIEW |
| `OI-GATE-AI-001` | Use-Case Fit | G3 | AI use case is bounded, owned, and outcome-defined | HALT |
| `OI-GATE-AI-002` | Knowledge Source | G3 | Approved source material has owner and review date | HALT customer-facing use |
| `OI-GATE-AI-003` | Human Review | G4 | Sensitive, uncertain, exceptional, or binding output requires approval | HALT |
| `OI-GATE-AI-004` | Boundary | G4 | Allowed and blocked topics and actions are explicit | HALT |
| `OI-GATE-AI-005` | Escalation | G4 | Named route and triggers exist | HALT customer-facing launch |
| `OI-GATE-AI-006` | Privacy | G4 | Allowed, restricted, and prohibited data and retention rules exist | HALT affected workflow |
| `OI-GATE-AI-007` | Permission | G4 | Tool and integration access follow least privilege | HALT affected access |
| `OI-GATE-AI-008` | Auditability | G3 | Inputs, outputs, approvals, corrections, and actions can be reconstructed | HALT higher-risk use |
| `OI-GATE-AI-009` | Prompt Standard | G2 | Role, objective, inputs, constraints, outputs, rules, and checks are defined | REVIEW |
| `OI-GATE-AI-010` | QA | G3 | Samples, failure categories, owner, cadence, and correction process exist | DEFER scale |
| `OI-GATE-AI-011` | Control State | G3 | Use case is explicitly ALLOW, REVIEW, or HALT | HALT roadmap admission |

## Privacy, safety, legal, and policy escalation

The following conditions require G4 treatment unless a documented specialist review authorizes a narrower response:

- uncontrolled sensitive-data exposure
- unauthorized credentials or system access
- false business identity, location, license, insurance, warranty, or pricing claims
- review gating, artificial reviews, or deceptive profile practices
- AI-generated binding commitments without review
- unsafe technical, legal, medical, financial, or emergency advice
- irreversible customer or system action without approval
- policy or contractual conflict
- unapproved use of customer, employee, payment, health, legal, authentication, or confidential data

Escalation records must include:

- observed condition
- affected system or customer
- immediate containment
- named reviewer
- required approval
- evidence and decision
- restart conditions

## Report and publication gates

A report, proposal, roadmap, public claim, or client deliverable may be released only when:

- evidence references are complete
- confidence and unknowns are visible
- scores reconcile
- findings use canonical IDs
- duplicate checks pass
- impact language is safe
- package scope and phase match the recommendation
- financial language follows ROI rules
- privacy, safety, legal, policy, and AI escalations are resolved
- DecisionLedger references exist
- required approvals are recorded

## Implementation and acceptance gates

Implementation may start only when:

- approved scope and package exist
- access is authorized
- dependencies are resolved or governed
- owners are named
- acceptance criteria exist
- testing and rollback are defined when needed
- change control is active
- commercial authorization exists
- specialist approvals exist where required

Implementation may close only when:

- acceptance criteria pass
- completion evidence is attached
- unresolved issues are disclosed
- ownership is transferred
- monitoring and maintenance are assigned
- access is removed or transferred appropriately
- DecisionLedger and lifecycle status are updated

## Methodology-change gates

A methodology change may be approved only when:

1. the gap is documented through delivery, scoring, evidence, or QC
2. existing files cannot represent the condition accurately
3. duplicate and downstream impacts are analyzed
4. IDs, mappings, gates, packages, templates, examples, and docs are identified
5. one source-of-truth file is updated first
6. a migration rule exists when active records are affected
7. version and changelog requirements are defined
8. approval is recorded

Do not introduce new terminology, categories, findings, packages, indexes, or formulas solely because they are interesting or marketable.

## Gate evaluation order

Apply gates in this order:

1. G4 control boundaries
2. authorization and access
3. evidence, accuracy, and unknowns
4. scoring and finding admission
5. risk and opportunity synthesis
6. package and delivery fit
7. effort, scope, and acceptance
8. roadmap and lifecycle sequencing
9. ROI and value language
10. report, proposal, or implementation release
11. completion and closure

A downstream PASS cannot override an upstream HALT.

## DecisionLedger requirements

```yaml
gate_evaluation_ref: OI-GE-YYYY-NNN
subject_ref: ""
lifecycle_state: ""
gate_results:
  - gate_id: OI-GATE-UNI-001
    outcome: VALIDATE
    evidence_refs: []
    conditions: []
    owner: ""
    reviewed_by: ""
    reviewed_at: ""
blocking_gates: []
approvals_required: []
restart_conditions: []
final_gate_state: VALIDATE
ledger_ref: OI-DL-YYYY-NNN
```

## Usage instructions

1. Identify the lifecycle stage and subject being evaluated.
2. Apply G4 controls first.
3. Apply all required universal gates.
4. Apply stage, domain, commercial, data, AI, ROI, or implementation gates.
5. Record each material gate result.
6. Resolve blocking gates before advancing.
7. Carry conditions into scope, roadmap, acceptance, and monitoring.
8. Reapply gates when evidence, scope, access, risk, or ownership changes.
9. Preserve the evaluation in the DecisionLedger.

## Completion check

Before declaring a stage, recommendation, deliverable, or implementation complete, confirm:

- applicable gates were identified
- G4 conditions were resolved
- PASS and conditional states have evidence
- VALIDATE and REVIEW states have owners
- HALT states have restart conditions
- dependencies and approvals are explicit
- report and value language are governed
- acceptance evidence exists
- DecisionLedger traceability is complete
