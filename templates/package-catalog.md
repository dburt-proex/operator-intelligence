# Operator Intelligence Implementation Package Catalog

Version: v0.1 commercial v1.0 catalog  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed canonical delivery catalog

## 1. Purpose

This catalog defines the client-delivery representation of the eight canonical Operator Intelligence implementation packages.

It standardizes package identity, eligibility, default phase, evidence triggers, prerequisites, included and excluded scope, acceptance criteria, completion evidence, dependencies, commercial boundaries, and report/proposal use.

This catalog does not authorize package-first selling. A package may be proposed only when a governed recommendation is package-eligible and the package directly resolves the verified root condition.

## 2. Package control rules

1. Package IDs and names are immutable canonical identifiers.
2. Package eligibility precedes package assignment.
3. Exactly one primary package is required only for eligible implementation or deferred recommendations.
4. Validation, monitoring, blocked, and halt recommendations may remain unrouted in Phase 0.
5. Dependent packages may not duplicate ownership, deliverables, or billing.
6. Included scope is selected proportionally from the catalog; the package name does not silently authorize every possible deliverable.
7. Completion requires acceptance evidence, not deliverable existence alone.
8. Package approval, proposal acceptance, and implementation authorization are separate decisions.
9. Unsupported ROI, revenue, lead, ranking, conversion, savings, market-share, or timeline claims are prohibited.
10. Material changes require a new package scope version and DecisionLedger event.

## 3. Canonical package registry

| Package ID | Canonical name | Primary trigger | Default phase | Controlled outcome |
|---|---|---|---|---|
| `OI-PKG-WEB-001` | Website Conversion Fix Pack | Buyer path, CTA, phone, form, mobile, contact, or action-path weakness | Phase 1 | Reduce verified inquiry friction |
| `OI-PKG-SEO-001` | Local SEO Expansion Pack | Service coverage, local relevance, buyer-intent content, metadata, internal linking, or indexing gap | Phase 2 | Improve governed local discoverability foundations |
| `OI-PKG-GBP-001` | Google Business Authority Pack | Incomplete, inaccurate, underused, or misaligned Google Business Profile | Phase 2 | Improve profile accuracy, relevance, proof, and action readiness |
| `OI-PKG-TRUST-001` | Trust Proof System | Weak review, project, human, local, process, credential, or risk-reduction proof | Phase 2 | Reduce buyer uncertainty with verified proof |
| `OI-PKG-CRM-001` | CRM and Follow-Up System | Scattered inquiries, unclear ownership, inconsistent stages, handoffs, follow-up, or customer history | Phase 3 | Establish a controlled lead and sales workflow |
| `OI-PKG-REV-001` | Review Generation System | Weak review velocity, inconsistent requests, limited testimonial capture, or unmanaged response workflow | Phase 3 | Systematize ethical review and testimonial operations |
| `OI-PKG-DASH-001` | Operator Dashboard Pack | Missing attribution, outcome tracking, metric definitions, dashboards, or decision cadence | Phase 3 | Make operating performance observable and decision-ready |
| `OI-PKG-AI-001` | Governed AI Intake Assistant | Bounded AI use case with passed workflow, data, privacy, review, escalation, logging, and QA gates | Phase 4 | Add controlled AI assistance without weakening accountability |

## 4. Package scope object

Use one record for each proposed or authorized package scope.

```yaml
package_scope_id: OI-PKGSCOPE-YYYY-NNN
package_id: OI-PKG-XXX-001
package_name: ""
package_catalog_version: "v0.1"
assessment_id: ""
recommendation_refs: []
finding_refs: []
evidence_refs: []
routing_refs: []
roadmap_refs: []
package_eligibility: eligible|validation_required|blocked|not_applicable
scope_version: "1.0"
supersedes: null
default_phase: 1|2|3|4
approved_phase: 1|2|3|4|5|null
included_scope: []
excluded_scope: []
prerequisites: []
dependencies: []
blocked_conditions: []
owner: ""
decision_authority: ""
acceptance_criteria: []
acceptance_evidence_refs: []
measurement_plan: []
implementation_authorized: false
implementation_authorization_ref: null
status: proposed|approved|blocked|authorized|in_progress|complete|monitoring|cancelled|superseded
qc_ref: null
ledger_refs: []
```

## 5. `OI-PKG-WEB-001` — Website Conversion Fix Pack

### Purpose

Correct verified buyer-facing friction in the path from interest to contact, estimate request, booking, or other approved action.

### Eligible when

- affected page or path is identified
- expected buyer action is known
- evidence shows the path is unclear, inaccessible, passive, broken, inconsistent, or difficult to use
- desktop and mobile evidence exists where relevant
- messaging, trust, offer, and technical dependencies are recorded

### Typical included scope

- primary and secondary CTA hierarchy
- click-to-call and contact-path correction
- form field, error, confirmation, and routing improvements
- mobile action-path correction
- contact-page and estimate-request structure
- service-page conversion blocks
- trust-proof placement required to support the action
- bounded analytics event requirements for the corrected path

### Excluded by default

- aesthetic redesign without structural evidence
- full rebrand
- service or location content expansion as the root issue
- internal lead handling after submission
- unsupported conversion-rate promises
- paid media or unrelated custom software

### Prerequisites

- verified business contact details
- approved offer and CTA language
- required access and rollback path
- routing destination and owner
- privacy or consent requirements for forms

### Acceptance criteria examples

- approved primary CTA is visible and functional on desktop and mobile
- test inquiry completes without blocking error
- confirmation and routing behavior match the approved workflow
- contact information is accurate across reviewed surfaces
- acceptance evidence includes screenshots and safe test records

## 6. `OI-PKG-SEO-001` — Local SEO Expansion Pack

### Purpose

Correct verified structural gaps that limit discoverability for real, high-intent local services and locations.

### Eligible when

- service is real and currently offered
- service area and business identity are accurate
- page intent and evidence gap are defined
- service, location, metadata, linking, indexing, or competitor evidence supports the route
- capacity and delivery constraints are disclosed where material

### Typical included scope

- service-page architecture and priority map
- verified service-page briefs or implementation
- local relevance and service-area alignment
- titles, descriptions, headings, and internal links
- indexability and canonicalization corrections within scope
- NAP/citation reconciliation dependencies
- local buyer-intent content requirements
- Search Console validation plan when access exists

### Excluded by default

- ranking guarantees
- location pages for unsupported service areas
- keyword-volume work without buyer relevance
- content production before offer and delivery fit are understood
- link schemes, fabricated citations, or deceptive local signals
- unrelated site redesign

### Prerequisites

- approved service and location inventory
- canonical business identity record
- website access and ownership
- content approval owner
- evidence-supported priority order

### Acceptance criteria examples

- approved service pages are published and internally linked
- metadata and headings match verified page intent
- indexability checks pass for approved pages
- unsupported service or location claims are absent
- completion evidence records URLs, screenshots, and validation results

## 7. `OI-PKG-GBP-001` — Google Business Authority Pack

### Purpose

Improve the accuracy, relevance, proof, and action readiness of the verified Google Business Profile.

### Eligible when

- profile identity and ownership/access state are known
- services, service area, hours, categories, and links can be verified
- evidence shows incomplete, inaccurate, underused, or misaligned profile elements
- policy-safe implementation is possible

### Typical included scope

- primary and secondary category review
- services, description, hours, service area, and link alignment
- photo and project-proof plan
- Q&A and update-content operating plan
- website/GBP identity alignment
- review-response and escalation dependencies
- profile action-path verification

### Excluded by default

- false locations or service areas
- inaccurate categories
- unsupported service claims
- review gating, artificial reviews, or policy evasion
- administrative status presented as verified fact
- ranking guarantees

### Prerequisites

- verified canonical identity
- authorized profile access
- approved business facts and service inventory
- policy and ownership review
- review-response owner where included

### Acceptance criteria examples

- approved categories, services, hours, links, and service area match verified business scope
- prohibited or unsupported claims are absent
- selected profile actions function
- completion evidence includes before/after screenshots and approval records

## 8. `OI-PKG-TRUST-001` — Trust Proof System

### Purpose

Reduce buyer uncertainty by placing authentic, relevant, and verified proof at the decisions where it matters.

### Eligible when

- the proof type and placement gap are identified
- work, review, credential, warranty, process, policy, team, or local proof can be authenticated
- evidence shows buyers lack visible proof for a material decision

### Typical included scope

- proof inventory and verification
- project/case-study structure
- testimonial and review placement
- process, warranty, credential, team, and local legitimacy blocks
- risk-reduction and expectation-setting copy
- proof-to-service and proof-to-CTA mapping
- proof maintenance owner and cadence

### Excluded by default

- fabricated testimonials, credentials, awards, warranties, or case results
- unsupported performance claims
- generic brand redesign
- review acquisition workflow owned by `OI-PKG-REV-001`
- legal interpretation of credentials or warranties

### Prerequisites

- authentic source assets
- publication permission
- verified credential and policy claims
- named approval owner
- service relevance mapping

### Acceptance criteria examples

- approved proof is visible on specified service and action pages
- each published claim resolves to source evidence
- expired or unsupported claims are removed
- completion evidence records source, placement, and approval

## 9. `OI-PKG-CRM-001` — CRM and Follow-Up System

### Purpose

Create a controlled system for inquiry capture, ownership, stage, handoff, follow-up, estimate outcome, customer history, and reactivation.

### Eligible when

- current intake sources are inventoried
- workflow owner is named
- stages, outcomes, exceptions, and handoffs are understood or included in bounded validation scope
- a system of record is identified or selected during authorized scope

### Typical included scope

- intake-source and field map
- lead/contact/job object requirements
- stage and status model
- ownership, handoff, escalation, and SLA rules
- estimate follow-up workflow
- lost-reason and next-action fields
- task/notification requirements
- migration or import plan within approved scope
- safe workflow tests and operating SOP

### Excluded by default

- automating an undefined workflow
- unrestricted customer-data migration
- replacing unrelated operational systems
- custom software beyond approved scope
- AI intake before readiness gates pass
- guaranteed close-rate or revenue outcomes

### Prerequisites

- workflow owner and decision authority
- system and data access authorization
- privacy, retention, and permission rules
- approved stages and required fields
- exception and failure handling

### Acceptance criteria examples

- every approved test inquiry enters the system of record with owner, source, stage, and next action
- handoff and escalation tests pass
- required fields and status transitions validate
- completion evidence includes test records, screenshots, and SOP approval

## 10. `OI-PKG-REV-001` — Review Generation System

### Purpose

Create an ethical, consistent workflow for requesting reviews, capturing testimonials, monitoring feedback, responding, and escalating service-recovery issues.

### Eligible when

- completion or success trigger is defined
- owner, timing, and channel are defined
- negative feedback follows a separate escalation path
- requests are not conditional on sentiment
- tracking exists or is included in scope

### Typical included scope

- request trigger and eligibility rules
- message templates and channel selection
- neutral review-request process
- negative-feedback escalation workflow
- testimonial permission/capture process
- response ownership and cadence
- tracking fields and reporting dependencies
- safe process tests

### Excluded by default

- review gating
- incentives prohibited by platform policy
- fabricated, purchased, employee, or conflicted reviews
- reputation guarantees
- profile optimization outside dependent GBP scope

### Prerequisites

- verified completion trigger
- customer-contact permission basis
- assigned escalation owner
- platform policy review
- system-of-record or tracking destination

### Acceptance criteria examples

- approved trigger creates a neutral request for eligible test cases
- negative feedback routes to the approved escalation path
- request and response ownership are observable
- completion evidence includes workflow tests and template approvals

## 11. `OI-PKG-DASH-001` — Operator Dashboard Pack

### Purpose

Make growth-system performance observable through governed metrics, source reconciliation, assigned review cadence, and defined decisions.

### Eligible when

- leadership lacks reliable visibility into a material operating question
- each metric has a definition and source
- owner, cadence, and decision use are named
- limitations and access are explicit

### Typical included scope

- KPI and metric dictionary
- source-system and field mapping
- baseline and coverage status
- dashboard or scorecard configuration
- exception and data-quality flags
- review cadence, owner, and decision rules
- reconciliation and QA checks
- DecisionLedger or action-log requirements

### Excluded by default

- vanity metrics without decision use
- unsupported attribution or ROI claims
- data warehouse engineering outside approved scope
- source-data cleanup not explicitly included
- dashboards that conceal unknown or blocked data

### Prerequisites

- source access and data-use authority
- metric definitions
- named business owner
- review cadence and decision thresholds
- data-quality limitations

### Acceptance criteria examples

- metrics reconcile to approved source records within stated tolerance
- definitions, owners, and review cadence are documented
- unknown or blocked data remains visible
- dashboard tests produce assigned actions or review decisions

## 12. `OI-PKG-AI-001` — Governed AI Intake Assistant

### Purpose

Add bounded AI assistance to an approved intake workflow while preserving human accountability, privacy, escalation, auditability, and failure containment.

### Eligible only when

- use case and prohibited actions are bounded
- workflow and structured inputs exist
- knowledge sources are approved
- privacy, permission, retention, and data boundaries pass
- human review and escalation rules exist
- logging, QA owner, test cases, and failure behavior exist
- control state permits implementation

### Typical included scope

- agent role, objective, inputs, outputs, and boundaries
- allowed/prohibited action policy
- knowledge-source registry
- prompt/capability contract
- human-review and escalation routing
- audit log and decision record requirements
- evaluation set and boundary tests
- limited integration with approved systems
- rollback, kill switch, and incident response

### Excluded by default

- autonomous financial, legal, safety, eligibility, or high-impact decisions
- unrestricted system or customer-data access
- silent scope expansion
- unsupervised outbound commitments
- unsupported replacement of accountable staff
- deployment before workflow and data readiness

### Prerequisites

- passed AI-readiness assessment
- approved workflow and system of record
- access/permission model
- privacy and retention decision
- human decision owner
- evaluation, monitoring, and incident owner

### Acceptance criteria examples

- approved test cases pass output, boundary, escalation, logging, and human-review checks
- prohibited actions are blocked or escalated
- audit records resolve to inputs, outputs, decisions, and reviewer actions
- rollback and halt procedures pass a controlled test

## 13. Package combination and dependency rules

- Website may depend on Trust when proof placement is required, but CTA/path ownership remains Website.
- SEO may depend on Website when new pages require conversion paths, but discoverability ownership remains SEO.
- GBP may depend on Trust or Review Generation, but profile accuracy ownership remains GBP.
- CRM may be prerequisite to Dashboard and Governed AI when workflow/data state is undefined.
- Review Generation may depend on CRM for triggers and Dashboard for monitoring.
- Dashboard does not own source-workflow correction.
- Governed AI cannot precede CRM/workflow, data, privacy, review, escalation, logging, and QA readiness.
- Phase 5 may renew or extend an existing package through new approved scope; it does not create a ninth default package.

## 14. Commercial representation rules

Every report or proposal package summary must state:

- package ID and canonical name
- verified routing basis
- package eligibility
- included and excluded scope
- prerequisites and dependencies
- roadmap phase
- owner and decision authority
- acceptance criteria and evidence
- fee and third-party-cost treatment when proposed
- authorization state
- material unknowns and blocked conditions
- outcome and timeline claim boundaries

## 15. Quality-control checklist

- [ ] Package ID and name match the canonical registry.
- [ ] Eligibility is supported by governed findings and evidence.
- [ ] Exactly one primary package exists only when eligible.
- [ ] Scope resolves the verified root condition.
- [ ] Dependencies do not duplicate ownership or billing.
- [ ] Phase and prerequisites are valid.
- [ ] Included and excluded scope are explicit.
- [ ] Acceptance criteria and evidence are observable.
- [ ] Implementation authorization remains separate.
- [ ] Completion and realized value remain separate.
- [ ] Unsupported claims are absent.
- [ ] Routing, QC, and DecisionLedger refs resolve.

## 16. Usage instructions

1. Resolve package eligibility through the recommendation and routing standards.
2. Select the canonical package that owns the root implementation path.
3. Create a versioned package-scope object.
4. Include only justified deliverables.
5. Record exclusions, dependencies, owner, acceptance criteria, and authorization state.
6. Use the same scope object in the report, roadmap, proposal, delivery plan, and completion review.

## 17. Commercial v1.0 connection

This catalog turns recommendation routing into consistent sellable scope while preventing package-first selling, duplicate ownership, uncontrolled expansion, and unsupported outcome claims.

## 18. References

- `framework/recommendation-index.md`
- `scoring/recommendation-map.md`
- `standards/package-routing-standard.md`
- `standards/recommendation-standard.md`
- `standards/roadmap-standard.md`
- `standards/ai-readiness-standard.md`
- `standards/quality-control-standard.md`
- `templates/recommendation-register.md`
- `templates/roadmap.md`
- `templates/proposal.md`