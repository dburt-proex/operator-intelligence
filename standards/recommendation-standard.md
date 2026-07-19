# Recommendation Standard

Version: v0.2 standards reconciliation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Reconciled commercial v1.0 control standard; pending folder approval

## 1. Purpose

This standard governs how Operator Intelligence converts evidence-backed findings into client-safe recommendations.

It defines recommendation admissibility, validation requirements, package routing, phase sequencing, scope controls, acceptance criteria, measurement boundaries, change control, and DecisionLedger traceability.

This standard does not create findings, redefine category scores, or replace the canonical package registry in `framework/recommendation-index.md`.

## 2. Governing principle

A recommendation is a governed action proposal and routing record, not a generic suggestion or sales device. It does not authorize implementation.

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
  → Risk-Impact Classification
  → Opportunity or Validation Decision
  → Effort Record when implementation scope is considered
  → Recommendation Object
  → Canonical Package Eligibility and Route
  → Roadmap Phase or Phase 0 Validation State
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

~~~yaml
recommendation_id: OI-REC-YYYY-NNN
recommendation_version: ""
supersedes: null
recommendation_class: implementation|validation|monitoring|defer|halt
finding_refs: []
evidence_refs: []
ledger_refs: []
risk_impact_refs: []
opportunity_ref: null
effort_ref: null
observation_summary: ""
root_condition: ""
validation_state: verified|validation_required|blocked
confidence: high|medium|low|unknown
unknowns: []
impact_class: ""
impact_score: 1-5|null
evidence_strength_score: 1-5|null
effort_inverse: 1-5|null
strategic_fit_score: 1-5|null
priority_score: 4-20|null
priority: critical|high|medium|low|null
risk_level: ""
package_registry_version: ""
package_eligibility: eligible|validation_required|blocked|not_applicable
primary_package_id: null
primary_package_name: null
dependent_package_ids: []
prerequisites: []
blocked_conditions: []
included_scope: []
excluded_scope: []
roadmap_phase: "Phase 0|Phase 1|Phase 2|Phase 3|Phase 4|Phase 5"
lifecycle_entry_state: OI-LC-08
implementation_owner: ""
implementation_authorized: false
implementation_authorization_ref: null
acceptance_criteria: []
measurement_plan: []
publication_state: internal_only|official|provisional|range_only|blocked
status: proposed|accepted|deferred|blocked|in_progress|complete|rejected
decision_owner: ""
decision_date: YYYY-MM-DD|null
decision_reason: ""
review_state: ALLOW|REVIEW|HALT
~~~

Required fields may not be replaced by narrative implication. Null package and priority fields are permitted only for validation, monitoring, halt, or blocked work when the reason and next gate are explicit.

## 6. Admission rules

A recommendation may enter a client report, roadmap, proposal, or implementation handoff only when:

- every source finding is governed and traceable
- evidence references are valid and current enough for the decision
- confidence is assigned separately from maturity
- unknowns and blocked conditions are explicit
- root condition is identified
- impact and risk are classified without unsupported claims
- implementation-class priority inputs and score can be reproduced
- package eligibility is explicit
- exactly one primary package is assigned when package eligibility is eligible
- dependencies and prerequisites are separated
- included and excluded scope are stated
- roadmap sequencing respects dependencies
- acceptance criteria are observable
- measurement limits are disclosed
- implementation ownership is identified without implying authorization
- implementation authorization is recorded separately and defaults to false
- DecisionLedger references exist
- language is executive-safe

## 7. Priority calculation and decision state

Implementation-class recommendation priority uses the approved four-input formula:

~~~text
Priority Score =
Impact
+ Evidence Strength
+ Effort Inverse
+ Strategic Fit
~~~

| Priority score | Priority |
|---:|---|
| 17–20 | critical |
| 13–16 | high |
| 9–12 | medium |
| 4–8 | low |

Rules:

1. Import impact from framework/risk-impact-model.md.
2. Assign evidence strength from admissible evidence under standards/evidence-standard.md.
3. Import effort inverse from framework/effort-model.md.
4. Assign strategic fit against current goals, capacity, dependencies, and roadmap eligibility.
5. Store every input and the calculated result.
6. Confidence remains a separate gate and does not change the priority score.
7. High impact with low or unknown confidence routes to validation, REVIEW, or HALT.
8. Priority cannot override privacy, safety, legal, policy, authorization, package, dependency, or control-boundary gates.
9. Validation, monitoring, and halt recommendations may leave priority null when scoring would imply unsupported implementation certainty.

## 8. Package eligibility and one-primary-package rule

Each package-eligible implementation or deferred recommendation must have exactly one canonical primary package.

The primary package is the smallest registered package that directly resolves the verified root condition. Additional packages may be recorded only as prerequisites or dependencies.

Validation, monitoring, halt, and blocked recommendations may have primary_package_id: null until eligibility is established. A null route must retain the validation action, blocked condition, next gate, and DecisionLedger trace.

Do not:

- assign several primary packages to one recommendation
- force validation work into a sellable package
- inflate scope by attaching unrelated packages
- select a package because it is commercially attractive
- force a finding into a package without defensible fit
- duplicate the same deliverable across packages

When no canonical package fits, create a methodology or validation gap record. Do not improvise a client package.

Canonical regression controls:

- OI-FIND-SEO-002 routes to OI-PKG-SEO-001 in Phase 2 with implementation_authorized: false.
- The AI readiness fixture remains in Phase 0 with primary_package_id: null while OI-AI-008 and OI-AI-010 are unknown.
- Package routing, roadmap placement, report publication, and client acceptance do not authorize implementation.

## 9. Scope proportionality

Recommendation scope must be proportional to the supported condition.

Included scope must identify only the work needed to resolve the source findings. Excluded scope must identify adjacent work that is not supported, not authorized, or deferred.

A recommendation must not expand from:

- one broken form into an unsupported full-site redesign
- one missing service page into unrestricted content production
- inconsistent follow-up into automation of an undefined workflow
- limited AI interest into customer-facing AI deployment
- weak reporting into a dashboard without defined decision use

## 10. Prerequisite and phase controls

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

## 11. Confidence handling

Confidence does not alter the maturity score or severity of the observed condition.

| Confidence | Recommendation treatment |
|---|---|
| High | Implementation may proceed when all other gates pass. |
| Medium | Implementation may proceed with stated limitations and validation controls. |
| Low | Prefer validation-first scope; material implementation requires governance review. |
| Unknown | Implementation is prohibited until evidence is obtained or the condition is formally blocked. |

A recommendation cannot carry stronger confidence than its weakest material evidence dependency.

## 12. Unknown and blocked handling

Unknown is not negative evidence.

When a material condition is unknown:

- record the missing evidence
- state why it matters
- define the minimum validation action
- assign an owner where possible
- do not create an implementation recommendation solely from the absence of access

Use `blocked` when authorization, privacy, safety, legal, policy, access, or control restrictions prevent defensible validation or implementation.

## 13. Acceptance criteria

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

## 14. Measurement boundaries

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

## 15. Executive-safe language

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

## 16. Change control

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

## 17. Validation messages

### Blocking errors

- `REC-TRACE-001`: recommendation lacks a complete source chain
- `REC-EVID-001`: recommendation exceeds supporting evidence
- `REC-CONF-001`: implementation is routed from unknown confidence
- `REC-PKG-001`: a package-eligible recommendation lacks exactly one canonical primary package
- `REC-PRIORITY-001`: required priority inputs or calculation cannot be reproduced
- `REC-AUTH-001`: recommendation, publication, or package routing is treated as implementation authorization
- `REC-VERSION-001`: material recommendation change lacks version or supersession trace
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

## 18. DecisionLedger minimum record

~~~yaml
ledger_ref: OI-DL-YYYY-NNN
decision_type: recommendation
recommendation_id: OI-REC-YYYY-NNN
recommendation_version: ""
supersedes: null
finding_refs: []
evidence_refs: []
risk_impact_refs: []
opportunity_ref: null
effort_ref: null
decision: ALLOW|REVIEW|HALT
confidence: high|medium|low|unknown
priority_inputs: {}
priority_score: null
package_eligibility: eligible|validation_required|blocked|not_applicable
primary_package_id: null
dependent_package_ids: []
roadmap_phase: ""
unknowns: []
blocked_conditions: []
publication_state: internal_only|official|provisional|range_only|blocked
implementation_authorized: false
implementation_authorization_ref: null
decision_reason: ""
decision_owner: ""
reviewed_by: ""
reviewed_at: YYYY-MM-DD
~~~

## 19. Completion checklist

Before release, confirm:

- the evidence-to-recommendation chain is complete
- the root condition is explicit
- confidence and unknowns are visible
- package eligibility is explicit
- exactly one primary package is assigned only when package eligible
- validation work may remain unrouted without implying implementation
- priority inputs and score reproduce when required
- prerequisites and dependencies are separated
- scope is proportional and bounded
- phase order is valid
- acceptance criteria are testable
- measurement claims are bounded
- blocked conditions are resolved or disclosed
- publication, client acceptance, roadmap approval, and implementation authorization remain separate
- implementation_authorized defaults to false
- DecisionLedger traceability is complete

## 20. Canonical references

Use this standard with:

- `framework/finding-index.md`
- `framework/recommendation-index.md`
- `framework/risk-impact-model.md`
- `framework/opportunity-model.md`
- `framework/effort-model.md`
- `framework/lifecycle-roadmap-map.md`
- `scoring/recommendation-map.md`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/publication-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/decision-ledger-standard.md`
- `standards/quality-control-standard.md`

## 21. v1.0 connection

This standard makes recommendations repeatable, evidence-bound, package-controlled, phase-aware, measurable, and safe for commercial reporting and implementation handoff.