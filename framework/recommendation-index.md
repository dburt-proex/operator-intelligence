# Operator Intelligence Recommendation Index

Version: v0.1 control-layer foundation  
Stage alignment: Stage 2 — `framework/`  
Folder alignment: `framework/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file is the canonical routing index for Operator Intelligence implementation recommendations.

It connects governed findings to approved implementation packages, prerequisites, roadmap phases, ownership, acceptance criteria, and DecisionLedger records. It does not replace `scoring/recommendation-map.md`; that file remains the source for criteria-to-package mappings and baseline deliverables. This index governs how those packages are selected, combined, deferred, blocked, and represented in reports.

## v1.0 connection

Commercial v1.0 requires a recommendation system that is repeatable, evidence-bound, commercially usable, and resistant to package-first selling.

This index strengthens v1.0 readiness by providing:

- stable package identifiers
- one routing process across all finding domains
- prerequisite and blocked-condition controls
- package-combination rules
- recommendation object requirements
- implementation acceptance criteria
- report and proposal admission gates
- DecisionLedger traceability

## Inputs and triggers

Use this index after:

- a finding has been resolved through `framework/finding-index.md`
- evidence and confidence have been assigned
- business impact has been classified
- the root domain and dependencies are known
- risk and impact have been evaluated

Use it again when preparing:

- executive reports
- contractor reports
- proposals
- package scopes
- 90-day roadmaps
- implementation handoffs
- completion reviews

## Outputs and deliverables

A valid use of this index produces:

- one primary package route per recommendation
- prerequisite and dependent package routes where justified
- explicit included and excluded scope
- roadmap phase
- implementation owner
- acceptance criteria
- measurement or validation plan
- recommendation status
- DecisionLedger reference

## Canonical package registry

| Package ID | Canonical package | Primary trigger | Default phase | Primary outcome |
|---|---|---|---|---|
| `OI-PKG-WEB-001` | Website Conversion Fix Pack | Buyer journey, CTA, phone, form, mobile, contact, or action-path weakness | Phase 1 — Quick Wins | Reduce visible inquiry friction |
| `OI-PKG-SEO-001` | Local SEO Expansion Pack | Missing service coverage, weak local relevance, thin buyer-intent content, or structural search gaps | Phase 2 — Growth Foundation | Improve high-intent local discoverability |
| `OI-PKG-GBP-001` | Google Business Authority Pack | Incomplete, inaccurate, underused, or misaligned Google Business Profile | Phase 2 — Growth Foundation | Improve local profile relevance, proof, and action readiness |
| `OI-PKG-TRUST-001` | Trust Proof System | Weak review, work, human, local, process, credential, or risk-reduction proof | Phase 2 — Growth Foundation | Reduce buyer uncertainty with verified proof |
| `OI-PKG-CRM-001` | CRM and Follow-Up System | Scattered inquiries, unclear ownership, inconsistent stages, handoffs, follow-up, or customer history | Phase 3 — Automation and Reporting | Create controlled lead and sales workflow |
| `OI-PKG-REV-001` | Review Generation System | Weak review velocity, inconsistent requests, limited testimonial capture, or unmanaged response process | Phase 3 — Automation and Reporting | Systematize ethical review and testimonial growth |
| `OI-PKG-DASH-001` | Operator Dashboard Pack | Missing attribution, outcome tracking, metric definitions, dashboards, or decision cadence | Phase 3 — Automation and Reporting | Make growth-system performance observable and actionable |
| `OI-PKG-AI-001` | Governed AI Intake Assistant | Defined, bounded AI use case with sufficient workflow, data, knowledge, review, privacy, escalation, logging, and QA controls | Phase 4 — Governed AI Enablement | Add controlled AI assistance without weakening accountability |

Package names above are canonical. Reports, proposals, ledgers, and roadmaps should use the package ID and canonical name together.

## Package eligibility controls

### `OI-PKG-WEB-001` — Website Conversion Fix Pack

Eligible when evidence shows a buyer-facing path is unclear, inaccessible, passive, broken, or difficult to use.

Required before routing:

- affected page or path is identified
- desktop or mobile evidence is captured where relevant
- the action expected from the buyer is known
- messaging, trust, or offer dependencies are recorded

Do not use for:

- aesthetic preference alone
- full redesign without structural need
- search-page expansion as the primary issue
- internal lead-management problems after submission

### `OI-PKG-SEO-001` — Local SEO Expansion Pack

Eligible when verified service, location, content, metadata, internal-linking, indexing, or competitor evidence shows a discoverability gap.

Required before routing:

- service is real and currently offered
- priority or strategic relevance is confirmed when material
- service area is accurate
- page intent and evidence gap are defined
- capacity or delivery constraints are recorded when applicable

Do not use for:

- unsupported ranking promises
- location pages for areas the business does not serve
- keyword volume without buyer relevance
- content production before offer and delivery fit are understood

### `OI-PKG-GBP-001` — Google Business Authority Pack

Eligible when profile accuracy, categories, services, description, photos, reviews, Q&A, activity, or website alignment is weak.

Required before routing:

- profile and business identity are verified
- ownership or access limitations are explicit
- services, service area, hours, and links are accurate
- policy-safe implementation is possible

Blocked conditions:

- false locations
- inaccurate categories
- unsupported service claims
- review gating or artificial reviews
- administrative state presented as fact without evidence

### `OI-PKG-TRUST-001` — Trust Proof System

Eligible when buyers lack visible, relevant, and verified evidence needed to reduce uncertainty.

Required before routing:

- proof type and placement gap are identified
- credentials, warranties, process, or policy claims are verified before publication
- work and review assets are authentic
- local or service relevance is documented

Do not use to manufacture credibility claims that the business cannot support.

### `OI-PKG-CRM-001` — CRM and Follow-Up System

Eligible when inquiry capture, ownership, status, handoffs, estimate follow-up, lost reasons, service history, referral, or reactivation processes are inconsistent or unobservable.

Required before routing:

- workflow owner is named
- current intake sources are inventoried
- required stages and outcomes are defined
- exceptions and handoffs are understood
- system of record is identified or selected during scope

Do not automate an undefined workflow. Route unclear process conditions to validation or process documentation first.

### `OI-PKG-REV-001` — Review Generation System

Eligible when review requests, responses, testimonial capture, or review monitoring are inconsistent or weak relative to verified need.

Required before routing:

- completion or success trigger is defined
- request owner and timing are defined
- negative feedback has a separate escalation path
- review requests are not conditional on sentiment
- tracking method exists or is included in scope

### `OI-PKG-DASH-001` — Operator Dashboard Pack

Eligible when leadership cannot reliably observe lead flow, source performance, estimate outcomes, review growth, page performance, or implementation results.

Required before routing:

- each metric has a definition
- source system is identified
- responsible owner is assigned
- review cadence and decision use are named
- known data limitations are disclosed

Do not build a dashboard whose metrics do not produce decisions.

### `OI-PKG-AI-001` — Governed AI Intake Assistant

Eligible only when the use case is bounded and AI-readiness gates pass.

Required before routing:

- documented workflow
- structured input data
- approved knowledge sources
- allowed and blocked topics
- human review rules
- escalation path
- privacy and permission controls
- audit logging
- QA owner and cadence
- `ALLOW`, `REVIEW`, or `HALT` control state

Any unresolved HALT condition blocks implementation scope.

## Canonical recommendation object

```yaml
recommendation_id: OI-REC-YYYY-NNN
finding_refs:
  - OI-FIND-DOMAIN-NNN
ledger_refs:
  - OI-DL-YYYY-NNN
observation_summary: ""
evidence_refs: []
confidence: unknown
validation_state: validation_required
impact_class: ""
impact_score: 0
risk_level: ""
priority_score: 0
priority: ""
primary_package_id: OI-PKG-XXX-001
primary_package_name: ""
dependent_package_ids: []
prerequisites: []
included_scope: []
excluded_scope: []
roadmap_phase: ""
implementation_owner: ""
acceptance_criteria: []
measurement_plan: []
status: proposed
decision_reason: ""
```

A recommendation cannot enter a client report, proposal, or roadmap with required fields blank.

## Routing sequence

1. Confirm that every source finding exists in a governed finding library.
2. Confirm evidence, confidence, validation state, impact, and risk.
3. Identify the root condition and the package that directly resolves it.
4. Assign one primary package.
5. Record prerequisite or dependent packages separately.
6. Apply package eligibility and blocked-condition checks.
7. Select only the deliverables needed to resolve the supported findings.
8. State excluded scope to prevent silent expansion.
9. Assign roadmap phase and implementation owner.
10. Define acceptance criteria and measurement plan.
11. Record the recommendation in the DecisionLedger.
12. Admit the recommendation to reports or proposals only after governance review.

## One-primary-package rule

Each recommendation object has one primary package.

A finding may depend on several packages, but the package that resolves the root condition remains primary. For example:

- unclear CTA wording: Website Conversion Fix Pack primary; Trust Proof System dependent only when proof placement is also required
- missing service page: Local SEO Expansion Pack primary; Website Conversion Fix Pack dependent only when inquiry paths also require work
- no estimate follow-up: CRM and Follow-Up System primary; Operator Dashboard Pack dependent when outcome reporting is also absent
- AI intake use case with weak CRM data: CRM and Follow-Up System prerequisite; Governed AI Intake Assistant deferred until readiness passes

## Package-combination rules

1. Several findings may be consolidated into one package scope when they share the same root implementation path.
2. Every consolidated finding retains its own evidence, confidence, impact, and ledger record.
3. Package combinations must preserve phase order.
4. Phase 1 corrections may be bundled with Phase 2 work only when dependencies and ownership remain clear.
5. Phase 3 workflow or measurement prerequisites must precede any dependent Phase 4 AI implementation.
6. A package must not absorb unrelated work merely to increase scope.
7. Repeated deliverables across packages should be assigned to one owner and one acceptance criterion to avoid duplication.

## Recommendation states

| State | Meaning |
|---|---|
| `proposed` | Governance checks pass and the recommendation is ready for client review |
| `accepted` | Client or authorized owner approved the recommendation |
| `deferred` | Valid recommendation is intentionally delayed because of sequencing, capacity, budget, or prerequisite constraints |
| `blocked` | Evidence, safety, privacy, accuracy, package, or dependency conditions prevent implementation |
| `in_progress` | Implementation has started under approved scope |
| `complete` | Acceptance criteria are met and evidence is recorded |
| `rejected` | Authorized owner declined the recommendation and the reason is recorded |

## Acceptance-criteria standard

Acceptance criteria must be observable and tied to the finding. Examples:

- primary CTA is visible and functional on desktop and mobile
- verified core-service pages are published and internally linked
- GBP categories and services match the actual business scope
- project proof is visible on specified service and CTA pages
- every inquiry enters the approved system of record with owner and status
- review request triggers and escalation paths are documented and tested
- dashboard metrics reconcile to source records and produce assigned actions
- AI test cases pass boundary, escalation, logging, and human-review checks

Completion is not based on deliverable existence alone. The implemented change must satisfy the approved acceptance criteria.

## Measurement and validation rules

- Do not promise traffic, rankings, lead volume, close rate, savings, or revenue without baseline and post-implementation evidence.
- Use leading indicators when outcome data is not yet mature.
- Separate implementation completion from performance validation.
- Record measurement windows and source limitations.
- Low-confidence, high-impact recommendations should begin with validation tasks rather than unsupported implementation claims.

## Report and proposal admission gate

A recommendation may enter a client-facing artifact only when:

- source findings are governed and traceable
- evidence and unknowns are explicit
- confidence is appropriate
- impact and risk are classified
- package eligibility passes
- blocked conditions are absent or resolved
- primary and dependent packages are separated
- included and excluded scope are stated
- roadmap phase respects dependencies
- acceptance criteria are observable
- implementation owner is identified
- DecisionLedger references exist
- client language is executive-safe

## Governance rules

1. Never recommend a package only because it is sellable.
2. Never force a finding into an existing package when no defensible fit exists.
3. When no package fits, create a methodology or validation gap record rather than an improvised client package.
4. Package scope must be proportional to the evidence-backed condition.
5. Unknown is not negative and does not automatically justify implementation.
6. Safety, privacy, legal, policy, accuracy, and binding-commitment concerns override commercial urgency.
7. Package names, IDs, default phases, and routing rules may change only through methodology review.

## Usage instructions

1. Resolve findings through `framework/finding-index.md`.
2. Apply `framework/risk-impact-model.md`.
3. Select the canonical package from this registry.
4. Apply prerequisites, exclusions, blocked conditions, and phase rules.
5. Build the recommendation object.
6. Create or update its DecisionLedger record.
7. Use the approved object in reports, proposals, roadmaps, and implementation handoffs.
8. Reopen the record when scope, evidence, risk, or acceptance criteria change.

## Completion check

Before use, confirm:

- package ID and name are canonical
- one primary package is assigned
- dependencies are explicit
- scope is evidence-proportional
- phase sequencing is valid
- acceptance criteria are testable
- measurement claims are bounded
- DecisionLedger traceability is complete

This file is the framework-level source of truth for recommendation routing. `scoring/recommendation-map.md` remains the criteria-to-package source, and future package-catalog templates should derive from both files.