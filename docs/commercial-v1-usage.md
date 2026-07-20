# Operator Intelligence Commercial v1.0 Usage Guide

Version: commercial v1.0  
Folder alignment: `docs/`  
Status: Canonical operating guide

## 1. Purpose

Provide the practical sequence for qualifying, delivering, reviewing, proposing, implementing, monitoring, and closing an Operator Intelligence engagement using the governed repository artifacts.

## 2. Roles

| Role | Primary responsibility |
|---|---|
| Engagement owner | Scope, client communication, lifecycle state, commercial coordination |
| Evidence collector | Authorized capture, provenance, source records, limitations |
| Evaluator | Criteria scoring, finding construction, recommendation development |
| QC reviewer | Independent reproduction, routing, language, publication review |
| Client decision owner | Accept, defer, reject, authorize, renew, or close |
| Implementation owner | Authorized package delivery and acceptance evidence |
| Governance owner | REVIEW/HALT, privacy, AI, exception, and escalation decisions |

One person may hold several roles in a small engagement, but authority and review decisions must remain explicit.

## 3. Canonical file sequence

```text
sales-notes.md
→ discovery-form.md
→ client-intake.md
→ evidence-register.md
→ scoring objects
→ finding-register.md
→ recommendation-register.md
→ decision-ledger.md
→ executive-report.md / contractor-report.md
→ roadmap.md
→ package-catalog.md scope
→ proposal.md
→ onboarding-checklist.md
→ delivery-checklist.md
→ completion / monitoring / renewal records
```

Run `quality-control-checklist.md` before every material release or advancement.

## 4. Step 1 — Qualify the engagement

Use:

- `templates/sales-notes.md`
- `templates/discovery-form.md`

Confirm:

- contractor/local-service fit
- material decision question
- bounded scope potential
- identifiable decision authority
- plausible evidence/access
- expectations compatible with evidence-bound delivery
- no deceptive, unauthorized, unsafe, or unsupported objective

Output: qualified, conditional, deferred, declined, or more-information-required state.

## 5. Step 2 — Govern intake

Use `templates/client-intake.md`.

Define:

- services, locations, systems, channels, periods, and exclusions
- public versus internal scope
- access levels and allowed/prohibited tests
- data sensitivity, storage, retention, deletion, and sharing
- owners, reviewers, and authority
- intended publication and implementation use
- unknowns, blockers, and conflicts

Do not collect or test outside the approved boundary.

## 6. Step 3 — Apply the playbooks

Use:

1. `playbooks/engagement-delivery-playbook.md`
2. `playbooks/contractor-base.md`
3. the applicable industry playbook
4. `playbooks/evidence-validation-playbook.md`

Current commercial v1 industry variants:

- painting
- tree service

The contractor base applies where no narrower approved vertical exists. Record a methodology gap when a material industry condition cannot be represented safely.

## 7. Step 4 — Map surfaces and collect evidence

Create the public/internal surface inventory. Use `templates/evidence-register.md`.

For every evidence item record:

- stable ID
- source, owner, date, scope, and represented period
- capture method
- observation
- evidence class, strength, and confidence support
- authorization, storage, integrity, and sensitivity
- admission state and limitations
- criterion/finding uses
- DecisionLedger refs

Preserve unknown, blocked, rejected, contradictory, and superseded states.

## 8. Step 5 — Score the assessment

Use:

- `scoring/criteria-library.md`
- `scoring/category-sheets/`
- `scoring/calculator-spec.md`
- `scoring/score-objects.md`
- `scoring/unknown-data-handling.md`
- `scoring/confidence-adjusted-scoring.md`

Sequence:

1. determine applicability
2. evaluate known criteria using approved anchors
3. preserve unknown/blocked states
4. assign evidence-derived confidence
5. calculate category score/coverage/bounds
6. calculate observed Operator Score, coverage, confidence index, and range
7. apply validation and publication gates
8. freeze the score run and ledger material decisions

Never multiply maturity by confidence.

## 9. Step 6 — Resolve findings

Use:

- `framework/finding-index.md`
- `framework/findings/`
- `templates/finding-register.md`

For each candidate:

- verify observation and evidence
- separate interpretation
- state bounded business impact
- assign confidence and limitations
- resolve duplicate ownership
- determine score/report effect
- validate, suppress, block, close, or supersede

Unknown is not a negative finding.

## 10. Step 7 — Build recommendations

Use:

- `playbooks/finding-to-recommendation-review.md`
- `standards/recommendation-standard.md`
- `templates/recommendation-register.md`

Calculate canonical priority inputs, then determine:

- recommendation class
- package eligibility
- primary package only when eligible
- dependencies and exclusions
- Phase 0 or phases 1–5
- owner and authority
- acceptance criteria/evidence
- publication and authorization state

## 11. Step 8 — Build the roadmap and reports

Use:

- `templates/roadmap.md`
- `templates/executive-report.md`
- `templates/contractor-report.md`
- `assets/` specifications

Reports must display:

- release identity
- score type/state, coverage, confidence, bounds, and limitations
- verified strengths
- governed findings
- recommendations and package eligibility
- Phase 0 and phases 1–5
- requested decision
- implementation authorization state
- completion/outcome boundary

## 12. Step 9 — Quality control and publication

Use:

- `templates/quality-control-checklist.md`
- `playbooks/publication-quality-review.md`

Freeze the artifact version and evidence snapshot. Review in order. Issue QC `ALLOW`, `REVIEW`, or `HALT`. Then issue a separate publication decision.

A client artifact may be official, provisional, range-only, blocked, or internal-only.

## 13. Step 10 — Deliver and record client decisions

Use `templates/delivery-checklist.md`.

Record:

- artifact versions delivered
- scope and limitations explained
- client questions and corrections
- accepted, deferred, rejected, validation, monitoring, or closure decisions
- next gate, owner, and condition
- DecisionLedger event

Do not revise a material recommendation live without re-review.

## 14. Step 11 — Propose only eligible scope

Use:

- `templates/package-catalog.md`
- `templates/proposal.md`

A proposal states:

- evidence/finding/recommendation basis
- eligibility and one primary package
- included and excluded scope
- prerequisites/dependencies
- work items and acceptance evidence
- client responsibilities
- commercial terms and change control
- proposal acceptance state
- separate implementation authorization state

Validation work may be offered as separately bounded validation scope, not disguised as implementation.

## 15. Step 12 — Onboard and authorize

Use `templates/onboarding-checklist.md`.

Before start:

- accepted proposal/version resolves
- owner and authority are explicit
- least-privilege access passes
- data controls pass
- prerequisites and dependencies pass
- testing, rollback, recovery, and escalation are defined
- acceptance evidence is fixed
- AI gates pass where applicable
- separate implementation authorization exists

No unresolved HALT may affect the work.

## 16. Step 13 — Complete and monitor

Completion requires acceptance evidence against authorized scope.

For realized value, separately define:

- metric and baseline
- source and owner
- comparison window
- confounders
- observed direction
- confidence and limitations
- decision triggered

Do not infer causation or ROI from deliverable completion.

## 17. Step 14 — Renew or close

Record:

- accepted deliverables and residual defects
- open risks, unknowns, and owners
- monitoring state
- renewed/expanded scope or maintenance decision
- access revocation
- record retention/return/deletion
- final ledger/closure state

Renewal is a governed decision, not an automatic upsell.

## 18. Required engagement records

Minimum commercial engagement set:

- opportunity/discovery record
- approved intake
- surface inventory
- evidence register
- score run and category objects
- finding and recommendation registers
- DecisionLedger
- QC record
- released report and roadmap
- client decision record
- proposal/onboarding/authorization if implementation proceeds
- completion and monitoring/closure record

## 19. Quality escalation

Use `REVIEW` for bounded ambiguity, sample, recency, ownership, scope, or exception questions.

Use `HALT` for:

- missing authority
- broken evidence provenance/integrity
- unknown treated as zero/failure
- unreproducible score
- confidence exceeding evidence
- duplicate weighted or package ownership
- unsupported recommendation or claim
- invalid package/phase route
- AI bypassing controls
- publication treated as authorization
- missing DecisionLedger traceability

## 20. Commercial v1.0 connection

This guide is the operating bridge between the repository architecture and a real paid assessment. It identifies the artifacts, gates, owners, and completion evidence required to deliver the product consistently.