# Recommendation Standard

Version: v0.1 governance foundation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Draft foundation for commercial v1.0

## 1. Purpose

This standard governs how Operator Intelligence converts evidence-backed findings into client-safe recommendations.

It defines recommendation admissibility, validation requirements, package routing, phase sequencing, scope controls, acceptance criteria, measurement boundaries, change control, and DecisionLedger traceability.

This standard does not create findings, redefine category scores, or replace the canonical package registry in `framework/recommendation-index.md`.

## 2. Governing principle

A recommendation is a controlled implementation decision, not a generic suggestion or sales device.

Every recommendation must answer:

1. What verified condition requires action?
2. What evidence supports that condition?
3. How confident is the assessment?
4. What business impact is reasonably supported?
5. What action directly addresses the root condition?
6. Which canonical package owns the work?
7. What prerequisites, dependencies, and blocked conditions apply?
8. How will completion be verified?
9. What remains unknown?
10. Where is the decision recorded?

## 3. Required source chain

A recommendation is admissible only when the following trace exists:

```text
Evidence Record
  → Scored Criterion or Governed Observation
  → Approved Finding
  → Impact and Risk Classification
  → Recommendation Object
  → Canonical Package Route
  → Roadmap Phase
  → Acceptance Criteria
  → DecisionLedger Record
```

A missing link blocks client-facing use.

## 4. Recommendation classes

| Class | Use |
|---|---|
| `implementation` | Evidence and prerequisites support defined corrective work. |
| `validation` | Material uncertainty must be resolved before implementation is justified. |
| `monitoring` | Current evidence does not justify change, but a controlled review condition exists. |
| `defer` | The recommendation is valid but sequencing, capacity, budget, or prerequisites require delay. |
| `halt` | Safety, privacy, legal, policy, accuracy, authorization, or control conditions prohibit action. |

Unknown evidence routes to `validation`, not automatically to `implementation`.

## 5. Minimum recommendation object

```yaml
recommendation_id: OI-REC-YYYY-NNN
recommendation_class: implementation|validation|monitoring|defer|halt
finding_refs: []
evidence_refs: []
ledger_refs: []
observation_summary: ""
root_condition: ""
confidence: high|medium|low|unknown
unknowns: []
impact_class: ""
risk_level: ""
priority: critical|high|medium|low
primary_package_id: ""
primary_package_name: ""
dependent_package_ids: []
prerequisites: []
blocked_conditions: []
included_scope: []
excluded_scope: []
roadmap_phase: ""
implementation_owner: ""
acceptance_criteria: []
measurement_plan: []
status: proposed|accepted|deferred|blocked|in_progress|complete|rejected
decision_reason: ""
review_state: ALLOW|REVIEW|HALT
```

Required fields may not be replaced by narrative implication.

## 6. Admission rules

A recommendation may enter a client report, roadmap, proposal, or implementation handoff only when:

- every source finding is governed and traceable
- evidence references are valid and current enough for the decision
- confidence is assigned separately from maturity
- unknowns and blocked conditions are explicit
- root condition is identified
- impact and risk are classified without unsupported claims
- one primary package is assigned
- dependencies and prerequisites are separated
- included and excluded scope are stated
- roadmap sequencing respects dependencies
- acceptance criteria are observable
- measurement limits are disclosed
- implementation ownership is assigned
- DecisionLedger references exist
- language is executive-safe

## 7. One-primary-package rule

Each recommendation has exactly one primary package.

The primary package is the package that directly resolves the root condition. Additional packages may be recorded only as prerequisites or dependencies.

Do not:

- assign several primary packages to one recommendation
- inflate scope by attaching unrelated packages
- select a package because it is commercially attractive
- force a finding into a package without defensible fit
- duplicate the same deliverable across packages

When no canonical package fits, create a methodology or validation gap record. Do not improvise a client package.

## 8. Scope proportionality

Recommendation scope must be proportional to the supported condition.

Included scope must identify only the work needed to resolve the source findings. Excluded scope must identify adjacent work that is not supported, not authorized, or deferred.

A recommendation must not expand from:

- one broken form into an unsupported full-site redesign
- one missing service page into unrestricted content production
- inconsistent follow-up into automation of an undefined workflow
- limited AI interest into customer-facing AI deployment
- weak reporting into a dashboard without defined decision use

## 9. Prerequisite and phase controls

Default roadmap sequence:

```text
Phase 1 — Quick Wins
Phase 2 — Growth Foundation
Phase 3 — Automation and Reporting
Phase 4 — Governed AI Enablement
```

Rules:

1. Foundational accuracy and visible critical failures precede growth expansion.
2. Offer, proof, service, and conversion dependencies must be recorded before scaling acquisition work.
3. Undefined workflows must be documented before automation.
4. Metric definitions and source systems must exist before dashboard implementation.
5. Workflow, data, privacy, review, escalation, logging, and QA prerequisites must pass before Phase 4 AI work.
6. Any unresolved `HALT` condition blocks dependent implementation.

## 10. Confidence handling

Confidence does not alter the maturity score or severity of the observed condition.

| Confidence | Recommendation treatment |
|---|---|
| High | Implementation may proceed when all other gates pass. |
| Medium | Implementation may proceed with stated limitations and validation controls. |
| Low | Prefer validation-first scope; material implementation requires governance review. |
| Unknown | Implementation is prohibited until evidence is obtained or the condition is formally blocked. |

A recommendation cannot carry stronger confidence than its weakest material evidence dependency.

## 11. Unknown and blocked handling

Unknown is not negative evidence.

When a material condition is unknown:

- record the missing evidence
- state why it matters
- define the minimum validation action
- assign an owner where possible
- do not create an implementation recommendation solely from the absence of access

Use `blocked` when authorization, privacy, safety, legal, policy, access, or control restrictions prevent defensible validation or implementation.

## 12. Acceptance criteria

Acceptance criteria must be observable, binary where practical, and tied to the source finding.

Valid criteria describe a verifiable operating state, such as:

- the specified inquiry path submits successfully on desktop and mobile
- every inquiry enters the approved system of record with owner and stage
- approved service pages are published and internally linked
- dashboard metrics reconcile to named source records
- review-request triggers and escalation paths are documented and tested
- AI test cases pass boundary, escalation, logging, and human-review controls

Invalid criteria include:

- improve performance
- increase leads
- strengthen the brand
- optimize operations
- achieve better ROI

Completion requires acceptance evidence, not deliverable existence alone.

## 13. Measurement boundaries

Separate implementation completion from outcome validation.

Do not promise or infer traffic, rankings, lead volume, close rate, savings, revenue, market share, or ROI without validated baseline and post-implementation evidence.

Every measurement plan must identify:

- metric definition
- source system
- baseline status
- review window
- responsible owner
- known limitations
- decision triggered by the result

Use leading indicators when outcome data is immature.

## 14. Executive-safe language

Client-facing recommendations must distinguish:

- observed fact
- interpretation
- unknown condition
- recommended action
- expected operational effect
- unverified business outcome

Preferred language:

> Evidence supports correcting the documented inquiry-routing gap and assigning an accountable owner. The expected operational effect is improved handling consistency. Lead and revenue impact require post-implementation measurement.

Prohibited language includes unsupported claims that the business is losing a specific number of leads, revenue, rankings, customers, or market share.

## 15. Change control

Reopen governance review when any of the following changes:

- source evidence
- finding interpretation
- confidence
- risk or impact
- package route
- included or excluded scope
- roadmap phase
- owner
- acceptance criteria
- measurement plan
- blocked condition

Every material change requires an updated DecisionLedger entry and reason.

## 16. Validation messages

### Blocking errors

- `REC-TRACE-001`: recommendation lacks a complete source chain
- `REC-EVID-001`: recommendation exceeds supporting evidence
- `REC-CONF-001`: implementation is routed from unknown confidence
- `REC-PKG-001`: no valid primary package is assigned
- `REC-DUP-001`: duplicate primary scope exists across packages
- `REC-PHASE-001`: roadmap sequencing violates prerequisites
- `REC-SCOPE-001`: scope is disproportionate or undefined
- `REC-ACCEPT-001`: acceptance criteria are not observable
- `REC-LEDGER-001`: DecisionLedger traceability is incomplete
- `REC-HALT-001`: implementation proceeds despite an unresolved HALT condition

### Warnings

- `REC-VALID-001`: low-confidence material work lacks validation-first scope
- `REC-OWNER-001`: implementation owner is weakly defined
- `REC-MEASURE-001`: measurement plan lacks baseline or source clarity
- `REC-LANGUAGE-001`: client language implies unsupported outcomes
- `REC-CHANGE-001`: material scope change lacks recorded review

## 17. DecisionLedger minimum record

```yaml
ledger_ref: OI-DL-YYYY-NNN
decision_type: recommendation
recommendation_id: OI-REC-YYYY-NNN
finding_refs: []
evidence_refs: []
decision: ALLOW|REVIEW|HALT
confidence: high|medium|low|unknown
primary_package_id: ""
dependent_package_ids: []
roadmap_phase: ""
unknowns: []
blocked_conditions: []
decision_reason: ""
reviewed_by: ""
reviewed_at: ""
```

## 18. Completion checklist

Before release, confirm:

- the evidence-to-recommendation chain is complete
- the root condition is explicit
- confidence and unknowns are visible
- one primary package is assigned
- prerequisites and dependencies are separated
- scope is proportional and bounded
- phase order is valid
- acceptance criteria are testable
- measurement claims are bounded
- blocked conditions are resolved or disclosed
- implementation authorization is separate from report publication
- DecisionLedger traceability is complete

## 19. Canonical references

Use this standard with:

- `framework/finding-index.md`
- `framework/recommendation-index.md`
- `framework/risk-impact-model.md`
- `framework/lifecycle-roadmap-map.md`
- `scoring/recommendation-map.md`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/publication-standard.md`

## 20. v1.0 connection

This standard makes recommendations repeatable, evidence-bound, package-controlled, phase-aware, measurable, and safe for commercial reporting and implementation handoff.