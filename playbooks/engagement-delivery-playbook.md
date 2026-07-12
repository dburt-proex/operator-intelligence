# Engagement Delivery Playbook

Version: v0.1 execution foundation  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Draft foundation for commercial v1.0

## 1. Purpose

This playbook defines the governed operating sequence for delivering an Operator Intelligence engagement from approved intake through client handoff and implementation decision.

It converts the lifecycle, evidence, scoring, finding, recommendation, roadmap, quality-control, and publication controls into one repeatable engagement workflow.

This playbook does not replace domain finding libraries, scoring rules, publication approval, or implementation authorization.

## 2. Inputs

Required inputs:

- approved client scope and exclusions
- signed engagement or documented authorization
- client intake record
- evidence-access plan
- criteria library and category sheets
- evidence, finding, and recommendation registers
- package catalog and roadmap template
- DecisionLedger template
- publication and quality-control standards

Missing authorization, unresolved scope, or unavailable required records produce `HALT` before evidence collection begins.

## 3. Outputs

A completed engagement produces:

- approved scope record
- evidence register and evidence snapshot
- reproducible score run
- validated finding register
- governed recommendation register
- prioritized roadmap
- executive report
- quality-control record
- publication decision
- client decision record
- implementation authorization or closure state
- DecisionLedger history

## 4. Engagement states

| State | Meaning | Allowed next action |
|---|---|---|
| `qualified` | Client and problem fit are sufficient for controlled intake | Open intake |
| `intake_active` | Scope, access, objectives, and constraints are being resolved | Complete intake gate |
| `evidence_active` | Approved evidence is being collected and normalized | Advance to scoring when coverage gate passes |
| `scoring_active` | Criteria and categories are being evaluated | Resolve findings after validation |
| `finding_review` | Findings are being validated, merged, suppressed, or escalated | Route approved findings |
| `recommendation_review` | Recommendations, packages, prerequisites, and phases are being assigned | Build roadmap |
| `report_build` | Approved outputs are being assembled | Enter quality control |
| `quality_review` | Reproducibility, traceability, language, and publication state are checked | Publish, return, or halt |
| `client_delivery` | Approved deliverable is presented and decisions are recorded | Authorize implementation, defer, monitor, or close |
| `implementation_ready` | Separate implementation authorization exists | Begin approved package work |
| `monitoring` | Acceptance and realized-value evidence are being collected | Renew, revise, or close |
| `closed` | Engagement obligations and records are complete | No further action without new authorization |

State changes must be recorded. Material reversals require a DecisionLedger event.

## 5. Delivery sequence

```text
Qualification
→ Intake and scope control
→ Evidence planning
→ Evidence collection
→ Scoring
→ Finding resolution
→ Recommendation routing
→ Roadmap build
→ Report assembly
→ Quality control
→ Publication authorization
→ Client delivery
→ Implementation decision
→ Monitoring or closure
```

A downstream artifact cannot cure an upstream control failure. Correct the earliest failed stage and rerun affected downstream work.

## 6. Phase 1 — Qualification and intake

### Required checks

- business type and service area fit the approved assessment model
- decision-maker and accountable client owner are identified
- requested outcome is compatible with the assessment scope
- prohibited or unsupported promises are removed
- access requirements and evidence limits are disclosed
- conflicts, privacy constraints, and material dependencies are identified
- client understands that findings and recommendations depend on evidence

### Gate

- `ALLOW` when scope, authority, and delivery fit are clear
- `REVIEW` when bounded uncertainty can be resolved during intake
- `HALT` when authorization, fit, safety, or scope integrity is insufficient

### Required record

```yaml
engagement_id: OI-ENG-YYYY-NNN
client_id: ""
client_owner: ""
assessment_scope: []
excluded_scope: []
access_status: []
material_constraints: []
intended_deliverables: []
review_state: ALLOW|REVIEW|HALT
ledger_ref: OI-DL-YYYY-NNN
```

## 7. Phase 2 — Evidence planning and collection

### Evidence plan

For each applicable category, define:

- required criteria
- required evidence type
- source owner
- collection method
- authorization state
- freshness requirement
- blocked or unavailable conditions
- duplicate-signal owner

### Collection rules

- use approved evidence types only
- preserve URL, screenshot, date, source, and represented period where applicable
- distinguish observed, tested, reported, inferred, and unavailable evidence
- retain contradictory evidence
- do not convert missing access into failure
- stop testing when authorization or safety boundaries are reached
- mark unresolved material gaps `unknown`, `validation_required`, or `blocked`

### Exit gate

Evidence collection may advance when:

- required public surfaces are reviewed
- approved internal evidence has been collected or explicitly marked unavailable
- provenance is resolvable
- duplicate ownership is assigned
- material contradictions are resolved or routed to `REVIEW`
- the evidence register is complete enough for a defensible score state

Broken provenance, unauthorized collection, or duplicate weighted ownership requires `HALT`.

## 8. Phase 3 — Scoring

### Required controls

- use approved category sheets and anchors
- distinguish `scored`, `unknown`, `blocked`, and `not_applicable`
- retain unknown and blocked weight inside applicable weight
- remove only approved `not_applicable` weight before normalization
- keep confidence separate from maturity
- calculate coverage before choosing publication state
- perform duplicate-signal checks
- preserve score ranges when uncertainty is material

### Exit gate

Scoring advances only when:

- category calculations reproduce
- active category weights reconcile to 100%
- coverage is calculated correctly
- unknowns and blocked states remain visible
- confidence assignments are evidence-bounded
- Operator Score publication state is defensible
- no unresolved G4 boundary affects the result

Unreproducible calculations or unknown-as-zero treatment require `HALT`.

## 9. Phase 4 — Finding resolution

Each candidate finding must include:

- finding ID
- observation
- evidence references
- criterion or category owner
- interpretation
- bounded business impact
- confidence
- priority
- limitations and unknowns
- DecisionLedger reference

### Review actions

- approve supported findings
- merge duplicates without losing evidence
- suppress unsupported or immaterial candidates with rationale
- split findings when one record contains multiple owners or implementation paths
- escalate contradictory or high-materiality conditions
- supersede corrected findings rather than silently overwriting them

Unknown or blocked evidence cannot independently create an implementation finding.

## 10. Phase 5 — Recommendation and package routing

A valid recommendation requires:

- approved finding linkage
- evidence-bounded scope
- business impact
- confidence
- priority
- exactly one primary package
- explicit prerequisites
- dependent packages only when justified
- roadmap phase
- acceptance evidence
- separate implementation authorization state
- DecisionLedger record

### Routing rules

- never route from score weakness alone
- never select work because it is easier to sell
- never assign multiple primary packages
- never let priority bypass dependencies
- route unknown or blocked conditions to validation, not implementation
- keep Phase 4 AI work behind workflow, data, privacy, review, escalation, logging, and QA gates

Invalid package ownership or missing prerequisites require `HALT`.

## 11. Phase 6 — Roadmap build

The roadmap must sequence approved recommendations by dependency and readiness.

### Default phases

| Phase | Purpose |
|---|---|
| Phase 1 | Correct control, measurement, access, and critical buyer-path gaps |
| Phase 2 | Strengthen core visibility, trust, conversion, and operational foundations |
| Phase 3 | Expand systems, coverage, automation, and management visibility |
| Phase 4 | Add governed AI or advanced optimization after prerequisites pass |

### Required roadmap fields

```yaml
recommendation_id: ""
primary_package_id: ""
roadmap_phase: 1|2|3|4
prerequisite_ids: []
dependency_ids: []
owner: ""
acceptance_authority: ""
acceptance_evidence: []
planning_window: ""
implementation_authorized: false
ledger_ref: OI-DL-YYYY-NNN
```

Planning windows are assumptions, not guarantees.

## 12. Phase 7 — Report assembly

Build the client deliverable only from approved records.

Required report components:

- assessment scope and limitations
- publication state
- Operator Score or defensible range
- category results and coverage
- material unknowns
- prioritized findings
- governed recommendations
- package routing
- phased roadmap
- validation requirements
- implementation authorization state
- methodology and evidence snapshot metadata

Client language must remain executive-safe and evidence-bounded.

Prohibited:

- guaranteed ROI, revenue, lead, ranking, conversion, savings, or timeline claims
- internal-failure claims derived from public absence
- competitor-performance claims based on appearance alone
- hiding material unknowns
- presenting publication approval as implementation authorization

## 13. Phase 8 — Quality control and publication

Use `playbooks/publication-quality-review.md` before release.

The review must verify:

- scope accuracy
- evidence admissibility and recency
- scoring reproducibility
- confidence and unknown handling
- finding completeness
- duplicate ownership
- recommendation and package routing
- roadmap sequencing
- DecisionLedger completeness
- executive-safe language
- versioning and supersession
- defensible publication state

### Publication outcomes

- `official`
- `provisional`
- `range_only`
- `blocked`
- `internal_only`

Quality-control `ALLOW` does not itself authorize publication. Publication does not authorize implementation.

## 14. Phase 9 — Client delivery

The delivery session must:

1. restate scope, evidence window, and limitations
2. explain score type, coverage, and uncertainty
3. present material findings in priority order
4. connect each recommendation to its evidence and business impact
5. explain package routing and roadmap dependencies
6. distinguish validation work from implementation work
7. record client decisions, questions, objections, and accepted limitations
8. avoid changing material recommendations live without re-review
9. document next-state decisions

### Approved client decisions

- `accept_for_implementation_review`
- `request_validation`
- `defer`
- `monitor`
- `reject`
- `close`

Material client-requested changes require reassessment, supersession, and DecisionLedger recording before publication or implementation.

## 15. Phase 10 — Implementation authorization

Implementation starts only when all of the following exist:

- approved recommendation
- approved primary package
- validated prerequisites
- defined scope and exclusions
- owner and acceptance authority
- acceptance evidence
- privacy, access, and safety approval where applicable
- commercial authorization
- separate implementation authorization record

```yaml
implementation_authorized: true|false
recommendation_ids: []
package_ids: []
approved_scope: []
excluded_scope: []
prerequisites_passed: false
acceptance_evidence: []
authorized_by: ""
authorized_at: YYYY-MM-DD
ledger_ref: OI-DL-YYYY-NNN
```

No delivery, quality-control, publication, or client-interest state substitutes for this authorization.

## 16. Phase 11 — Acceptance, monitoring, and closure

### Implementation acceptance

Completion requires observable acceptance evidence, not deliverable existence alone.

Examples:

- tested form submission reaches the approved destination
- tracking event appears in the approved analytics property
- required service page is published and indexed for review
- follow-up workflow executes against a controlled test record
- dashboard reconciles to approved source data
- AI workflow passes human-review, escalation, logging, and QA checks

### Outcome monitoring

Realized value remains separate from implementation acceptance.

Record:

- baseline and comparison period
- metric definition and source
- confounding changes
- confidence and limitations
- observed direction
- whether further validation is required

Do not claim causation or ROI without validated data and approved methodology.

### Closure gate

Close only when:

- contracted deliverables are accepted, deferred, or formally rejected
- open risks and validation requirements are transferred to an owner
- publication and implementation records are retained
- superseded records remain accessible
- DecisionLedger history is complete
- renewal, monitoring, or closure state is recorded

## 17. Escalation and failure handling

### `REVIEW`

Use when a bounded issue requires judgment but does not invalidate the engagement.

Examples:

- narrow but disclosed evidence sample
- evidence near freshness limit
- provisional owner or acceptance authority
- resolvable client-requested scope change

### `HALT`

Use when:

- authorization is missing
- material evidence lacks provenance
- a score cannot be reproduced
- unknown is treated as zero
- confidence exceeds evidence
- duplicate weighted or package ownership exists
- a recommendation lacks a valid finding
- roadmap dependencies are bypassed
- unsupported outcome claims remain
- DecisionLedger traceability is broken
- publication is treated as implementation authorization
- a G4 boundary remains unresolved

Correct the earliest failed control, supersede affected records when material, and rerun all downstream checks.

## 18. DecisionLedger requirements

Record at minimum:

- engagement qualification
- scope approval and changes
- access and authorization decisions
- material evidence conflicts
- applicability and unknown-state decisions
- score publication state
- finding approval, suppression, merge, or supersession
- recommendation and package routing
- roadmap sequencing and exceptions
- quality-control outcome
- publication authorization
- client decisions
- implementation authorization
- acceptance, monitoring, renewal, or closure

Every material recommendation must preserve:

```text
evidence
→ interpretation
→ business impact
→ confidence
→ priority
→ package
→ roadmap phase
→ action
```

## 19. Engagement control record

```yaml
engagement_id: OI-ENG-YYYY-NNN
client_id: ""
current_state: ""
scope_version: ""
evidence_snapshot_date: YYYY-MM-DD
score_run_id: OI-SCORE-YYYY-NNN|null
report_id: OI-REPORT-YYYY-NNN|null
report_version: ""
publication_state: official|provisional|range_only|blocked|internal_only
qc_id: OI-QC-YYYY-NNN|null
open_blockers: []
open_warnings: []
validation_requirements: []
client_decisions: []
implementation_authorized: false
monitoring_state: not_started|active|complete|not_applicable
closure_state: open|deferred|closed
owner: ""
review_state: ALLOW|REVIEW|HALT
ledger_ref: OI-DL-YYYY-NNN
```

## 20. Delivery completion checklist

- [ ] engagement fit and authorization are documented
- [ ] scope and exclusions are approved
- [ ] evidence plan and access limits are recorded
- [ ] evidence register is complete and traceable
- [ ] score run reproduces under approved rules
- [ ] unknown, blocked, and not-applicable states are correct
- [ ] findings are supported, bounded, and uniquely owned
- [ ] recommendations have one primary package
- [ ] prerequisites and roadmap phases are valid
- [ ] report language is executive-safe
- [ ] quality-control review is complete
- [ ] publication authorization is recorded
- [ ] client decisions are recorded
- [ ] implementation authorization remains separate
- [ ] acceptance evidence is defined
- [ ] monitoring or closure owner is assigned
- [ ] DecisionLedger records are complete

## 21. Cross references

- `framework/lifecycle-roadmap-map.md`
- `framework/governance-gate-index.md`
- `playbooks/evidence-validation-playbook.md`
- `playbooks/finding-to-recommendation-review.md`
- `playbooks/publication-quality-review.md`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/quality-control-standard.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`
- `templates/client-intake.md`
- `templates/evidence-register.md`
- `templates/finding-register.md`
- `templates/recommendation-register.md`
- `templates/roadmap.md`
- `templates/executive-report.md`
- `templates/proposal.md`

## 22. Usage instructions

1. Open the engagement control record at qualification.
2. Advance one state only after the current exit gate passes.
3. Use the domain libraries and category sheets for evaluation, not this playbook.
4. Record material decisions and exceptions in the DecisionLedger.
5. Stop at `HALT`; do not bypass failed controls to preserve delivery speed.
6. Use the publication review before any client release.
7. Require separate authorization before implementation begins.
8. Close only after ownership, records, and unresolved validation needs are transferred.

## 23. v1.0 connection

This playbook establishes the repeatable delivery process required for commercial v1.0. It connects the completed methodology, scoring, findings, recommendations, packages, roadmap, reporting, quality control, client decision, implementation authorization, and monitoring layers into one auditable operating sequence.