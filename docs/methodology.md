# Operator Intelligence Assessment Methodology

Version: commercial v1.0  
Folder alignment: `docs/`  
Status: Canonical operating-method summary

## 1. Purpose

Operator Intelligence evaluates how a contractor or local-service business turns market attention into qualified inquiries, estimates, booked work, customer proof, and operational learning.

The methodology treats website, messaging, conversion, local search, Google Business Profile, trust, social, lead handling, follow-up, automation, AI readiness, analytics, and competitive context as one connected growth system.

## 2. Governing objective

Produce repeatable, evidence-backed decisions that another qualified evaluator can review and materially reproduce.

The methodology does not guarantee rankings, leads, conversion, revenue, savings, ROI, market share, competitor performance, or timelines.

## 3. Canonical architecture

```text
Scope and authority
→ Surface mapping
→ Evidence admission
→ Criterion evaluation
→ Category and Operator Score
→ Finding resolution
→ Risk / impact / opportunity synthesis
→ Recommendation priority
→ Package eligibility and routing
→ Phase 0 or phases 1–5 roadmap
→ Report and QC
→ Publication decision
→ Client decision
→ Proposal and onboarding
→ Separate implementation authorization
→ Completion evidence
→ Monitoring / realized-value evidence
→ Renewal or closure
→ DecisionLedger
```

## 4. Assessment domains and weights

| Category | Weight |
|---|---:|
| Website structure and UX | 10% |
| Messaging and offer clarity | 10% |
| Conversion infrastructure | 15% |
| Local SEO | 15% |
| Google Business Profile | 10% |
| Reputation and trust | 10% |
| Social presence | 5% |
| Automation maturity | 10% |
| AI readiness | 5% |
| Analytics and reporting | 5% |
| Competitive position | 5% |

The criteria corpus contains 140 unique signals. Messaging and offer criteria share one weighted category while retaining distinct finding domains.

## 5. Lifecycle

| ID | Stage | Required exit evidence |
|---|---|---|
| `OI-LC-01` | Qualification | Fit, decision question, authority, next action |
| `OI-LC-02` | Intake | Scope, exclusions, access, data, testing authority |
| `OI-LC-03` | Surface Mapping | Applicable public/internal surface inventory |
| `OI-LC-04` | Evidence Collection | Admitted evidence snapshot, unknowns, blockers |
| `OI-LC-05` | Scoring | Reproducible criteria, categories, coverage, confidence, bounds, state |
| `OI-LC-06` | Finding Resolution | Validated/suppressed/blocked/closed finding register |
| `OI-LC-07` | Risk and Opportunity Synthesis | Canonical impact, effort, evidence, strategic-fit decisions |
| `OI-LC-08` | Recommendation Routing | Class, priority, eligibility, package, phase, acceptance evidence |
| `OI-LC-09` | Report and Roadmap Build | Versioned artifacts ready for QC |
| `OI-LC-10` | Delivery and Decision | Publication and client decisions recorded |
| `OI-LC-11` | Proposal and Onboarding | Accepted scope and start prerequisites |
| `OI-LC-12` | Implementation | Separately authorized work and completion evidence |
| `OI-LC-13` | Monitoring and Realized Value | Measured evidence and next decision |
| `OI-LC-14` | Renewal or Closure | Renewed scope, maintenance, deferment, or closure |

No stage advances without its required evidence, owner, authority, and gate.

## 6. Scope and authority

Before evidence collection:

- identify the client decision
- define systems, channels, services, locations, periods, and exclusions
- identify owners and decision authority
- define access and test boundaries
- classify data sensitivity and handling
- record conflicts, dependencies, and prohibited actions
- issue `ALLOW`, `REVIEW`, or `HALT`

Unauthorized or materially ambiguous scope requires HALT.

## 7. Evidence methodology

### Evidence classes

| Class | Meaning |
|---|---|
| A | Directly observable or testable |
| B | Comparative evidence against a defined set |
| C | Approved pattern applied to visible evidence |
| D | Inferred or plausible; validation-only by default |
| E | Client-provided record, export, screenshot, or statement |

Class, evidence strength, confidence support, and admission state remain separate.

### Evidence rules

- Every material source has a stable Evidence ID.
- Source, date, method, scope, owner, authorization, integrity, and limitations are recorded.
- Client statements remain reported until admitted/corroborated.
- Public absence does not prove internal nonexistence.
- Missing access is unknown or blocked, not negative evidence.
- Contradictions remain visible.
- One condition has one weighted owner.
- Rejected and superseded records remain auditable.

## 8. Criterion states

- `scored`
- `unknown`
- `blocked`
- `not_applicable`

Unknown and blocked criteria remain inside applicable coverage. Only approved not-applicable weight is removed before normalization.

## 9. Scoring

### Category observed score

```text
Observed Category Score =
sum(criterion score × criterion weight)
÷ Known Criterion Weight
```

### Category coverage

```text
Category Coverage =
Known Criterion Weight
÷ Applicable Criterion Weight
```

### Observed normalized Operator Score

```text
Observed Normalized Operator Score =
sum(observed category score × included category weight)
÷ sum(included category weight)
```

### Weighted evidence coverage

```text
Weighted Evidence Coverage =
sum(category coverage × category weight)
```

### Operator confidence index

```text
Operator Confidence Index =
sum(category confidence factor × category weight × category coverage)
÷ sum(category weight × category coverage)
```

### Confidence factors and bounds

| Confidence | Factor | Normal score bound |
|---|---:|---|
| High | 1.00 | Exact observed score |
| Medium | 0.75 | Observed score ±12.5 |
| Low | 0.50 | Observed score ±25 |
| Unknown | 0.00 | 0–100 uncertainty; not scoreable |

Confidence affects uncertainty, validation, publication, assertion strength, and report language. It never multiplies maturity or priority.

## 10. Operator Score publication

Publication states:

- `official`
- `provisional`
- `range_only`
- `blocked`
- `internal_only`

Official publication requires, at minimum:

- active category weights total 100%
- weighted evidence coverage at least 80%
- Operator confidence index at least 0.65
- no major category below its required coverage
- no high-materiality unknown invalidating the point estimate
- no unresolved G4 boundary
- duplicate controls pass
- mapping and validation checks pass
- required independent review and publication approval

Coverage alone never authorizes official publication.

## 11. Finding methodology

A governed finding contains:

1. observation
2. evidence refs
3. interpretation
4. business impact
5. confidence and basis
6. limitations, unknowns, and contradictions
7. weighted owner and reference-only uses
8. severity and score effect
9. report-use state
10. DecisionLedger refs

Candidate findings may be validated, split, merged, suppressed, blocked, published, closed, or superseded.

Unknown conditions do not automatically create negative findings.

## 12. Risk, opportunity, and priority

Recommendation priority uses canonical framework authorities:

- impact score
- evidence-strength score
- effort inverse
- strategic-fit score

```text
Priority Score =
((Impact × 0.40)
+ (Evidence Strength × 0.20)
+ (Effort Inverse × 0.15)
+ (Strategic Fit × 0.25)) × 20
```

Confidence remains a separate gate. Priority cannot bypass evidence, authority, dependencies, or Phase 0.

## 13. Recommendation classes

- `implementation`
- `validation`
- `monitoring`
- `defer`
- `halt`

A valid recommendation includes observation, evidence, interpretation, business impact, confidence, priority, package eligibility, roadmap phase, acceptance evidence, owner, and ledger refs.

## 14. Package eligibility and routing

Eligibility states:

- `eligible`
- `validation_required`
- `blocked`
- `not_applicable`

Rules:

- Eligibility precedes assignment.
- Exactly one primary package is required only when eligible.
- Validation, monitoring, and blocked actions may have no package.
- Dependent packages cannot duplicate ownership, deliverables, or billing.
- No package is selected because it is commercially attractive.
- A missing fit creates a methodology or validation gap, not an invented package.

## 15. Roadmap phases

| Phase | Purpose |
|---:|---|
| 0 | Validation and Access |
| 1 | Quick Wins |
| 2 | Growth Foundation |
| 3 | Automation and Reporting |
| 4 | Governed AI Enablement |
| 5 | Optimization and Renewal |

Phase 0 cannot contain implementation authorization. Phase 4 requires workflow, data, privacy, human review, escalation, logging, QA, and failure controls.

## 16. Quality control and publication

Quality control reviews, in order:

1. scope and version
2. evidence
3. scoring and unknowns
4. findings
5. recommendations and routing
6. roadmap and authorization
7. DecisionLedger
8. executive language
9. distribution and publication state

QC outcomes are `ALLOW`, `REVIEW`, or `HALT`. QC ALLOW permits a separate publication decision only.

## 17. Client delivery and commercial scope

- Reports disclose score state, coverage, confidence, bounds, limitations, unknowns, findings, eligibility, phase, and authorization.
- Proposals include only eligible bounded scope.
- Commercial terms do not imply outcomes.
- Proposal acceptance does not start work.
- Onboarding verifies owner, access, data, prerequisites, testing, recovery, escalation, and acceptance.
- Implementation begins only with a separate authorization record.

## 18. Completion, monitoring, and value

Implementation completion requires observable acceptance evidence against authorized scope.

Realized value requires separate:

- baseline
- metric definition
- source
- comparison period
- confounders
- confidence and limitations
- decision review

Completion does not prove rankings, leads, conversion, savings, revenue, ROI, or causation.

## 19. DecisionLedger

Every material state change records:

- subject and decision
- evidence and rationale
- fact, interpretation, assumptions, limitations, unknowns, blockers
- confidence and canonical priority inputs where applicable
- package eligibility, route, phase, publication, and authorization
- owner, authority, reviewer, approver, and timestamps
- acceptance/completion/value evidence
- supersession and integrity refs

Approved or published history is never silently overwritten.

## 20. Executive-safe language

Use bounded patterns such as:

- “verified across the reviewed scope”
- “supported by the available evidence”
- “not visible on the tested public surfaces”
- “requires internal validation”
- “this creates a risk because [mechanism]”

Do not use unsupported certainty, blame, guaranteed outcomes, or public-absence claims about internal operations.

## 21. Canonical records

Use `templates/index.md` and `playbooks/index.md`. Do not create alternate record structures that change controlled states, packages, phases, or authorization boundaries without reopening the relevant folder gate.

## 22. Commercial v1.0 connection

This document summarizes the completed methodology. Detailed authority remains in the framework, scoring, standards, templates, playbooks, and folder completion gates.