# AI Readiness Standard

Version: v0.2 standards reconciliation  
Stage alignment: Stage 4 — standards/  
Folder alignment: standards/  
Status: Reconciled commercial v1.0 control standard; pending folder approval

## 1. Purpose

This standard governs whether a proposed or active AI use case is sufficiently defined, bounded, evidenced, reviewed, and controlled to enter an Operator Intelligence roadmap or implementation decision.

It converts AI readiness from a general maturity concept into a use-case-specific control decision. It governs workflow definition, data fitness, approved knowledge, privacy and access, human review, customer-facing boundaries, escalation, prompt control, auditability, testing, quality review, change control, and DecisionLedger traceability.

This standard does not certify legal compliance, cybersecurity, model safety, vendor suitability, or business outcomes. Conditions requiring privacy, security, legal, regulatory, contractual, employment, safety, or professional-domain judgment must be escalated to an authorized specialist.

## 2. Governing principle

AI must not be used to hide an undefined process, compensate for unreliable data, bypass accountability, or create unreviewed customer commitments.

AI interest, tool ownership, subscription level, a successful demonstration, or an isolated output is not readiness.

Every decision applies to one bounded use case and one reviewed version. A category score cannot authorize a use case, and approval of one use case cannot authorize another.

## 3. Core rules

1. Define the operational problem before selecting an AI tool.
2. Name the workflow owner, decision authority, users, affected customers, and escalation owner.
3. Identify all inputs, source systems, outputs, actions, handoffs, exceptions, and completion states.
4. Use only approved knowledge and authorized data.
5. Apply least-privilege access and record material retention and sharing rules.
6. Require human review for sensitive, uncertain, exceptional, customer-facing, or binding outputs unless a separately approved control policy permits otherwise.
7. Define allowed topics, blocked topics, prohibited actions, uncertainty behavior, and escalation triggers.
8. Retain enough input, output, approval, correction, and action evidence to reconstruct material behavior.
9. Test the exact use-case version against representative, boundary, failure, and misuse cases before release.
10. Assign ALLOW, REVIEW, or HALT to the use case; never infer a control state from readiness score alone.
11. Keep evidence confidence, maturity score, publication state, and implementation authorization separate.
12. Record material decisions, exceptions, changes, incidents, approvals, and supersessions in the DecisionLedger.
13. Unknown or blocked conditions create validation work, not negative scores or implementation scope.
14. Outcome, savings, labor-replacement, revenue, conversion, lead-volume, or ROI claims require validated baseline and post-implementation evidence.

## 4. Scope and category boundary

This standard applies when AI is active, proposed, piloted, purchased for operational use, or materially included in a recommendation.

It governs:

- internal drafting, summarization, classification, retrieval, and decision support
- customer-response drafting and intake assistance
- customer-facing assistants
- AI-supported routing, recommendations, or workflow actions
- prompts, system instructions, knowledge sources, evaluations, and logs
- human approvals, escalations, exceptions, corrections, and incidents

It does not independently score:

- general automation maturity
- CRM implementation quality
- analytics installation
- website chatbot placement or interface design
- vendor benchmark performance
- general information-security maturity
- speculative financial value

Cross-domain conditions remain dependencies owned by their primary category. They must not be counted again as AI-readiness weaknesses under a different label.

## 5. Approved criterion contract

The authoritative scoring contract remains scoring/category-sheets/ai-readiness.md. This standard governs the operating control represented by each criterion.

| Criterion | Governed control |
|---|---|
| OI-AI-001 | Core workflow, owner, handoffs, exceptions, and completion state are documented. |
| OI-AI-002 | Required customer and operational data is structured, attributable, and fit for the use case. |
| OI-AI-003 | The use case is defined by task, outcome, owner, boundary, and success criteria. |
| OI-AI-004 | Human review gates cover sensitive, uncertain, exceptional, and binding outputs. |
| OI-AI-005 | Customer-facing topics, actions, claims, and commitments are explicitly bounded. |
| OI-AI-006 | Approved knowledge sources have owners, versions, and review dates. |
| OI-AI-007 | Material inputs, outputs, approvals, corrections, and actions can be audited. |
| OI-AI-008 | Data privacy, access, sharing, and retention expectations are defined. |
| OI-AI-009 | Low-risk, reversible assistance is prioritized before higher-risk use. |
| OI-AI-010 | Named escalation routes and trigger conditions exist and are testable. |
| OI-AI-011 | Prompts and system instructions are structured, versioned, and controlled. |
| OI-AI-012 | Representative samples, failure categories, review cadence, and corrections are recorded. |

Scoring uses the approved 0, 25, 50, 75, and 100 anchors. This standard does not create alternate anchors or change category math.

## 6. Minimum use-case record

Every assessed use case must have a unique record before it can receive a control-state decision.

~~~yaml
use_case_id: OI-AI-UC-YYYY-NNN
assessment_id: ""
name: ""
business_problem: ""
task_boundary: ""
workflow_owner: ""
decision_authority: ""
users: []
affected_parties: []
trigger: ""
inputs: []
source_systems: []
approved_knowledge_refs: []
outputs: []
permitted_actions: []
prohibited_actions: []
human_review_rules: []
escalation_triggers: []
escalation_owner: ""
data_classes: []
access_roles: []
retention_rule: ""
logging_ref: ""
success_criteria: []
acceptance_tests: []
known_limitations: []
dependencies: []
criterion_ids: []
evidence_refs: []
control_state: ALLOW|REVIEW|HALT
publication_state: internal_only|official|provisional|range_only|blocked
implementation_authorized: false
reviewed_by: ""
reviewed_at: YYYY-MM-DD
ledger_ref: OI-DL-YYYY-NNN
version: ""
~~~

Required fields may not be silently omitted. Use null only where structural inapplicability is documented and approved.

## 7. Operational risk bands

Risk bands support review depth; they do not replace the canonical gates.

| Band | Typical condition | Default treatment |
|---|---|---|
| R1 — bounded internal assistance | Reversible internal drafting, summarization, classification, or retrieval from approved sources | May reach ALLOW when all applicable gates pass |
| R2 — human-approved external support | AI prepares customer-facing content or recommendations, but a named person approves before use | REVIEW until approval, logging, and escalation controls pass |
| R3 — customer-facing or system-affecting use | AI interacts with customers, routes records, changes workflow state, or influences material decisions | REVIEW or HALT pending full control evidence and authorization |
| R4 — sensitive, binding, irreversible, or specialist use | Pricing, guarantees, legal terms, safety advice, regulated or sensitive data, financial action, irreversible system action | HALT unless separately authorized under documented specialist and governance review |

Risk may be raised by data sensitivity, action consequence, customer exposure, reversibility, scale, uncertainty, exception frequency, or inability to audit.

## 8. Canonical governance gates

Apply the gates in framework/governance-gate-index.md and retain each material result.

| Gate ID | Gate | Pass requirement | Failure outcome |
|---|---|---|---|
| OI-GATE-AI-001 | Use-Case Fit | Task, owner, outcome, boundary, and success criteria are defined. | HALT |
| OI-GATE-AI-002 | Knowledge Source | Approved source material has an owner, version, and review date. | HALT customer-facing use |
| OI-GATE-AI-003 | Human Review | Sensitive, uncertain, exceptional, or binding output requires appropriate approval. | HALT |
| OI-GATE-AI-004 | Boundary | Allowed and blocked topics, actions, claims, and commitments are explicit. | HALT |
| OI-GATE-AI-005 | Escalation | Named route and trigger conditions exist and can be tested. | HALT customer-facing launch |
| OI-GATE-AI-006 | Privacy | Allowed, restricted, and prohibited data plus retention and sharing rules are defined. | HALT affected workflow |
| OI-GATE-AI-007 | Permission | Tool, user, integration, and source access follow least privilege. | HALT affected access |
| OI-GATE-AI-008 | Auditability | Material inputs, outputs, approvals, corrections, and actions can be reconstructed. | HALT higher-risk use |
| OI-GATE-AI-009 | Prompt Standard | Role, objective, inputs, constraints, outputs, rules, and checks are controlled. | REVIEW |
| OI-GATE-AI-010 | Quality Assurance | Samples, failure categories, owner, cadence, and correction process exist. | Defer scale |
| OI-GATE-AI-011 | Control State | The reviewed version is explicitly ALLOW, REVIEW, or HALT. | HALT roadmap admission |

Also apply OI-GATE-DATA-001 through OI-GATE-DATA-003 and applicable automation gates when the use case depends on operational data, integrations, or workflow actions.

A downstream pass cannot override an upstream HALT.

## 9. Control-state decisions

| State | Meaning | Permitted treatment |
|---|---|---|
| ALLOW | The bounded, reviewed version has approved inputs, sources, instructions, ownership, logging, exception handling, tests, and authority appropriate to its risk. | May proceed only within recorded scope and separate implementation authorization. |
| REVIEW | AI may prepare, retrieve, classify, or recommend, but a named human must approve, correct, or handle exceptions before consequential use. | May proceed only with the recorded review gate and conditions. |
| HALT | A material workflow, data, privacy, permission, boundary, review, escalation, audit, test, authority, or specialist condition is unresolved. | Do not implement, launch, expand, or continue the affected behavior. |

A strong readiness score does not require ALLOW. A low score does not automatically require HALT. Control state depends on the risk and gate evidence for the specific use case.

Each HALT record must name the blocking condition, containment action, owner, validation required, and restart condition.

## 10. Workflow and data prerequisites

Before AI implementation, verify:

- task trigger and completion state
- accountable owner and handoff owners
- normal, exceptional, delayed, failed, and duplicate paths
- required input fields and source-of-truth systems
- data definitions, completeness, known quality limitations, and correction owner
- output destination and downstream consumer
- action permissions and rollback or recovery path
- measurement source and review cadence

Undefined workflow or unstructured data normally routes to OI-PKG-CRM-001 or a process prerequisite in Phase 3 before Phase 4 AI work.

Missing operational measurement may route to OI-PKG-DASH-001 before or alongside AI readiness work.

## 11. Knowledge-source controls

Every source used to ground AI behavior must record:

~~~yaml
knowledge_ref: OI-KNOW-YYYY-NNN
title: ""
owner: ""
source_location: ""
approved_use: []
prohibited_use: []
version: ""
effective_date: YYYY-MM-DD
review_due: YYYY-MM-DD
supersedes: null
limitations: []
approval_ref: ""
~~~

Uncontrolled web content, model memory, stale documents, draft policies, vendor marketing, or unattributed files cannot serve as authoritative sources for customer-facing claims or binding actions.

Conflicting sources must be retained, resolved by an authorized owner, and ledgered when material.

## 12. Privacy, access, and specialist escalation

The assessment must identify organization-approved data classes and the permitted treatment for each. Do not assume that vendor settings or contracts alone establish safe use.

At minimum, record:

- data owner and system of record
- allowed, restricted, and prohibited data
- user, tool, model, connector, and integration access
- least-privilege rationale
- storage, retention, deletion, and sharing expectations
- training or secondary-use settings where relevant and observable
- credential and secret handling
- incident and revocation path
- specialist approval where required

Default to HALT for the affected workflow when authorization is absent or when sensitive customer, employee, payment, authentication, health, legal, location, confidential business, or other controlled data could be exposed without an approved rule.

This standard does not declare a vendor or workflow compliant. Record the evidence and escalate decisions beyond assessment authority.

## 13. Human review and escalation

Human review rules must define:

- outputs requiring approval
- authorized reviewer role
- information the reviewer must inspect
- approval, correction, rejection, and escalation actions
- maximum response or hold time where operationally relevant
- treatment when no reviewer is available
- evidence retained for the decision

Customer-facing pricing, guarantees, availability, legal terms, safety guidance, complaint resolution, policy exceptions, unusual requests, or binding commitments require review unless separately authorized under a documented control policy.

Escalation triggers must include uncertainty, missing information, conflicting instructions, blocked topics, suspected sensitive data, customer distress, safety concerns, policy conflict, failed integrations, repeated errors, and attempts to bypass controls where applicable.

## 14. Prompt and instruction standard

Prompts and system instructions must use a controlled PromptBP-style structure:

1. Role — the bounded operating role.
2. Objective — the task and success condition.
3. Inputs — approved fields, sources, and context.
4. Constraints — prohibited topics, actions, claims, and data.
5. Output — required format and destination.
6. Rules — review, escalation, citation, logging, and uncertainty behavior.
7. Checks — pre-release validation and failure handling.
8. Version — owner, effective date, change reason, and supersession link.

Informal user prompts may not override system boundaries, data restrictions, human review, or escalation rules.

Material instruction changes require regression testing and a superseding DecisionLedger event before release.

## 15. Testing and quality assurance

Before release, test the exact configured version across the minimum scope in scoring/category-sheets/ai-readiness.md: at least ten representative tests, or every available case when fewer exist.

The test set must cover applicable conditions:

- normal and expected requests
- missing or ambiguous information
- out-of-scope and prohibited requests
- sensitive-data handling
- pricing, promises, complaints, and exception cases
- escalation triggers
- conflicting or stale knowledge
- instruction-override attempts
- tool or integration failure
- logging, approval, correction, and recovery behavior

Use synthetic or approved test data. Do not expose real sensitive information or trigger customer-facing, production, financial, public, or irreversible actions without explicit authorization.

Define use-case-specific acceptance thresholds before testing. Useful measures may include grounded-response rate, escalation precision, prohibited-action rate, human-correction rate, routing accuracy, logging completeness, and recovery success. No universal threshold may be invented after results are known.

Retain the test set, version, expected result, actual result, reviewer, defects, correction, and retest evidence.

## 16. Unknown, blocked, and not-applicable handling

Use unknown when required evidence was not supplied or cannot support a defensible conclusion.

Use blocked when authorization, privacy, safety, legal, policy, access, technical, or specialist conditions prevent review or testing.

Use not_applicable only for approved structural irrelevance. Missing controls, missing tools, limited access, low readiness, or score impact do not justify not_applicable.

Do not:

- convert unknown to zero
- infer safety from absence of incidents
- infer readiness from tool presence
- infer compliance from vendor claims
- remove unknown or blocked weight
- create a negative finding or package route from an unknown criterion
- conduct live tests to eliminate an unknown without authorization

Material unknowns involving privacy, permission, customer behavior, binding actions, review, escalation, knowledge, or auditability require range_only or blocked publication and may require HALT routing.

## 17. Findings, package routing, and roadmap

Findings must use approved OI-FIND-AI identifiers from framework/findings/ai-readiness-findings.md and must trace to admissible evidence and scored criteria.

Unknown controls create validation requirements before findings or packages.

Exactly one primary package may own a recommendation:

| Condition | Primary route | Phase |
|---|---|---|
| Undefined process, ownership, workflow state, or structured data | OI-PKG-CRM-001 or approved process prerequisite | Phase 3 before AI |
| Missing operational measurement | OI-PKG-DASH-001 | Phase 3 before or alongside AI |
| Bounded AI use case with prerequisites and gates satisfied | OI-PKG-AI-001 | Phase 4 — Governed AI Enablement |
| Unresolved privacy, review, boundary, escalation, audit, or specialist condition | Validation and control remediation | Phase 0 or governed prerequisite |

A sellable package is not evidence that the route is appropriate. Implementation scope must remain proportional to the finding and control state.

## 18. Publication and implementation separation

An assessment may publish a readiness result only under standards/publication-standard.md.

Official publication additionally requires:

- the minimum evaluation scope is complete
- scoring coverage is at least 80 percent
- every assessed use case has a recorded control state
- no unresolved material privacy, boundary, review, escalation, audit, or authorization unknown remains
- duplicate-signal checks pass
- reported findings resolve to DecisionLedger records

Use provisional for a bounded non-material limitation, range_only when unknowns could materially change interpretation, and blocked when evidence or control failures prevent defensible publication.

Publication approval does not authorize implementation. Quality-control ALLOW does not authorize implementation. Package selection does not authorize implementation.

Implementation requires a separate named owner, scope, authority, date, conditions, and ledger record. The default remains implementation_authorized: false.

## 19. DecisionLedger record

Every material use-case decision must record:

~~~yaml
decision_id: OI-DL-YYYY-NNN
decision_type: ai_use_case_control
use_case_id: OI-AI-UC-YYYY-NNN
use_case_version: ""
criterion_ids: []
evidence_refs: []
gate_results: []
risk_band: R1|R2|R3|R4
unknowns: []
blocked_conditions: []
confidence: high|medium|low|unknown
control_state: ALLOW|REVIEW|HALT
conditions: []
validation_required: []
primary_package: null
dependent_packages: []
roadmap_phase: null
publication_state: internal_only|official|provisional|range_only|blocked
implementation_authorized: false
decision_owner: ""
decision_date: YYYY-MM-DD
supersedes: null
restart_conditions: []
~~~

Material changes to model, vendor, prompt, knowledge, data, access, integrations, actions, review, escalation, tests, scope, or owner reopen the control decision.

Published and approved records are superseded, not silently overwritten.

## 20. Validation codes

### Blocking errors

- AISTD-USE-001: use-case record is missing or materially incomplete
- AISTD-GATE-001: required canonical gate lacks a result
- AISTD-DATA-001: data source, owner, class, or authorization is unresolved
- AISTD-KNOW-001: customer-facing behavior relies on an unapproved knowledge source
- AISTD-REVIEW-001: sensitive, uncertain, exceptional, or binding output lacks human review
- AISTD-BOUND-001: allowed and prohibited topics or actions are undefined
- AISTD-ESC-001: escalation trigger or owner is missing
- AISTD-AUDIT-001: material behavior cannot be reconstructed
- AISTD-TEST-001: required representative testing is incomplete or unauthorized
- AISTD-STATE-001: use case lacks ALLOW, REVIEW, or HALT
- AISTD-ROUTE-001: unknown evidence created a finding or implementation route
- AISTD-AUTH-001: publication, quality review, or package routing is treated as implementation authorization
- AISTD-LEDGER-001: material decision lacks DecisionLedger traceability
- AISTD-DUP-001: an operational condition is scored or routed more than once

### Warnings

- AISTD-TOOL-001: tool ownership or a demonstration is being treated as readiness
- AISTD-SAMPLE-001: test or QA sample is narrow but disclosed
- AISTD-RECENCY-001: knowledge, prompt, policy, or test evidence may be stale
- AISTD-OWNER-001: operational owner exists but approval authority is pending
- AISTD-MEASURE-001: implementation acceptance is defined but outcome evidence is not yet available

Warnings require disposition and may still force REVIEW depending on materiality.

## 21. Executive-safe language

Use:

- the reviewed evidence supports bounded internal assistance
- customer-facing use remains subject to human review
- privacy and escalation controls require validation
- the use case is not authorized for implementation
- the current result is range-only because material evidence remains unknown
- no outcome claim is made until baseline and post-implementation evidence are available

Avoid without direct evidence and authority:

- the business is AI-ready
- the system is safe, secure, private, compliant, unbiased, or accurate
- AI will replace staff or save a stated number of hours
- AI will increase leads, conversion, revenue, or ROI
- the vendor guarantees data protection
- autonomous use is approved because the readiness score is high

## 22. Canonical regression decision

The canonical fixture is scoring/examples/ai-readiness-worked-example.md.

Its verified result is:

~~~yaml
observed_indicator: 57.50
coverage_percent: 83.33
confidence_index: 1.0000
score_range: [47.92, 64.58]
publication_state: range_only
unknowns:
  - OI-AI-008
  - OI-AI-010
control_state:
  internal_assistance: REVIEW
  customer_facing_execution: HALT
primary_package: null
roadmap_phase: Phase 0 — Validation and Access
implementation_authorized: false
~~~

This fixture demonstrates the required separation: strong confidence in scored evidence does not resolve unknown privacy and escalation controls, and the observed indicator does not authorize customer-facing use or package implementation.

## 23. Completion checklist

Before a use case advances, confirm:

- unique use-case ID and reviewed version exist
- workflow, owner, task, inputs, outputs, handoffs, exceptions, and completion state are defined
- all 12 scoring criteria have valid states when a category result is published
- applicable data, automation, and all 11 AI gates are evaluated
- approved knowledge and data sources resolve
- privacy, access, retention, sharing, and specialist boundaries are recorded
- human review, customer boundaries, and escalation routes are testable
- prompt instructions are structured, versioned, and controlled
- representative tests and QA evidence are retained
- logging can reconstruct material activity
- unknown and blocked conditions remain visible
- control state, publication state, and implementation authorization are separate
- findings use approved OI-FIND-AI identifiers
- exactly one primary package owns each recommendation
- Phase 3 prerequisites precede Phase 4 implementation
- client language does not exceed the evidence
- DecisionLedger record and supersession state are complete

## 24. Cross references

- scoring/category-sheets/ai-readiness.md
- scoring/examples/ai-readiness-worked-example.md
- scoring/criteria-library.md
- scoring/unknown-data-handling.md
- scoring/confidence-adjusted-scoring.md
- framework/findings/ai-readiness-findings.md
- framework/governance-gate-index.md
- framework/lifecycle-roadmap-map.md
- standards/evidence-standard.md
- standards/confidence-standard.md
- standards/publication-standard.md
- standards/decision-ledger-standard.md
- standards/recommendation-standard.md
- standards/package-routing-standard.md
- standards/roadmap-standard.md
- standards/quality-control-standard.md

## 25. Commercial v1.0 connection

This standard makes AI-readiness decisions reproducible and auditable across evidence collection, scoring, findings, prerequisite routing, Phase 4 roadmap admission, publication, implementation approval, testing, monitoring, change control, and executive reporting.

It authorizes no AI use by itself. Each use case requires evidence, gate results, a control-state decision, and separate implementation authority.
