# AI Readiness Category Scoring Sheet

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `ai-readiness`  
Default Operator Score weight: 5%  
Status: Draft foundation for commercial v1.0

## 1. Purpose and category boundary

This sheet governs scoring for the operational, data, knowledge, control, privacy, review, escalation, audit, prompt, and QA prerequisites required for safe and commercially useful AI use.

It measures whether a business can place AI into a defined workflow without creating uncontrolled commitments, data exposure, unowned exceptions, unverifiable outputs, or tool-first experimentation.

It does not independently score:

- general automation maturity
- CRM implementation quality
- analytics installation
- website chatbot design
- model capability or benchmark performance
- vendor brand, subscription tier, or feature count
- speculative AI ROI

AI interest, tool ownership, or prior experimentation is not readiness. Cross-domain prerequisites must be recorded as dependencies, not duplicate scores.

## 2. Criterion inventory

Included prefix:

```text
OI-AI-*
```

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-AI-001` | Core workflows are documented | SOPs, workflow maps, checklists | Equal |
| `OI-AI-002` | Customer and operational data is structured | CRM schema, forms, sample records | Equal |
| `OI-AI-003` | AI use cases are defined by task and outcome | Use-case brief, owner, success criteria | Equal |
| `OI-AI-004` | Human review gates exist | Approval workflow, policy, configuration | Equal |
| `OI-AI-005` | Customer-facing AI boundaries are explicit | Allowed and blocked topics, action limits | Equal |
| `OI-AI-006` | An approved knowledge base exists | Source inventory, owner, review dates | Equal |
| `OI-AI-007` | AI outputs and approvals can be audited | Logs, transcripts, CRM notes, revisions | Equal |
| `OI-AI-008` | Data privacy and access expectations are defined | Policy, permissions, retention rules | Equal |
| `OI-AI-009` | Low-risk use cases are prioritized first | Risk-ranked roadmap, pilot brief | Equal |
| `OI-AI-010` | Escalation paths and triggers exist | Escalation SOP, named owner, tests | Equal |
| `OI-AI-011` | Prompt standards are documented and controlled | Prompt templates, instructions, version history | Equal |
| `OI-AI-012` | AI performance is reviewed and corrected | QA samples, failure categories, action log | Equal |

Each criterion has one weighted owner: `ai-readiness`.

## 3. Required evidence surfaces

### Primary evidence

- documented target workflow, trigger, owner, inputs, outputs, handoffs, exceptions, and completion state
- CRM, form, spreadsheet, or system schema used by the proposed workflow
- written AI use-case definition with scope and success condition
- human approval and exception-handling rules
- customer-facing allowed topics, blocked topics, commitments, disclaimers, and action limits
- approved knowledge-source inventory with owner and review date
- output, approval, correction, and action logs where required
- privacy, access, retention, sharing, and prohibited-data rules
- use-case risk ranking and pilot sequence
- escalation triggers, route, owner, and test evidence
- prompt or system-instruction inventory with version control
- QA sample, failure taxonomy, review cadence, and correction record

### Supporting evidence

- client interview
- tool configuration screenshots
- access-role review
- sample transcripts
- red-team or boundary tests
- policy documents
- change logs
- vendor data-handling settings
- incident or exception records

### Evidence that cannot support a point score alone

- AI tool subscription or login screen
- a successful demo without repeatable workflow evidence
- vendor claims about safety, privacy, or accuracy
- generic prompt examples not used in the workflow
- owner enthusiasm or stated intent
- estimated time savings, revenue, or replacement capacity without validated operating data

## 4. Minimum evaluation scope

An AI Readiness category score is admissible only when the evaluator reviews:

1. at least one proposed or active AI use case
2. the complete target workflow and named owner
3. the required input data and source systems
4. human review requirements
5. customer-facing boundaries when applicable
6. approved knowledge sources
7. privacy, access, retention, and sharing rules
8. output and approval logging
9. escalation triggers and route
10. prompt instructions
11. at least ten representative test cases, or all available when fewer exist
12. QA ownership, cadence, and corrective-action process

When no AI use case is proposed or active, the category may still be assessed for baseline readiness, but client-facing conclusions must not imply implementation need.

If internal access is unavailable, affected criteria become `unknown` or `blocked`. Missing access is not score `0`.

## 5. Applicability rules

All criteria are normally applicable when AI use is active, proposed, or materially under consideration.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples:

- `OI-AI-005` when the use case is strictly internal, cannot communicate externally, and cannot make operational commitments
- `OI-AI-007` when the bounded internal task has no material decision, customer, compliance, or execution consequence and logging is explicitly deemed unnecessary
- `OI-AI-010` when the tool cannot encounter exceptions or route outputs beyond a fully deterministic, low-risk internal transform

The following do not justify `not_applicable`:

- no policy exists
- the tool does not support the control
- the business has not documented the workflow
- implementation has not started
- the criterion would reduce the score

## 6. Weighting rule

All applicable criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before recalculation. Unequal weighting is prohibited without a versioned methodology change under `scoring/weight-rules.md`.

## 7. Category-specific anchors

Use only `0`, `25`, `50`, `75`, and `100`. Interpolation is not permitted.

### Workflow, data, and use-case definition — `OI-AI-001` through `OI-AI-003`

| Score | Observable condition |
|---:|---|
| 0 | AI is active or proposed in an undefined workflow, required data is materially unusable, or the use case has no bounded task, owner, output, or success condition. |
| 25 | Some process and data context exists, but scope, ownership, inputs, outputs, exceptions, or success measures remain materially incomplete. |
| 50 | A functional workflow and use case are defined, but data quality, exception handling, ownership, or measurement remains partial. |
| 75 | Workflow, owner, data, scope, outputs, exceptions, and success criteria are clear and implementation-ready. |
| 100 | Definitions are version-controlled, tested, monitored, and governed through accountable change and review processes. |

### Human control, boundaries, and escalation — `OI-AI-004`, `OI-AI-005`, `OI-AI-010`

| Score | Observable condition |
|---:|---|
| 0 | AI can issue sensitive, unsafe, binding, or out-of-scope outputs without required review or escalation. |
| 25 | Some review or boundary language exists, but coverage is vague, incomplete, untested, or dependent on operator memory. |
| 50 | Baseline approval, boundary, and escalation controls exist, but exception coverage, enforcement, testing, or ownership remains incomplete. |
| 75 | Sensitive outputs, uncertainty, blocked topics, commitments, and exceptions are consistently routed through defined human controls. |
| 100 | Control behavior is policy-driven, tested, logged, auditable, versioned, and routinely stress-tested against boundary cases. |

### Knowledge, privacy, and auditability — `OI-AI-006` through `OI-AI-008`

| Score | Observable condition |
|---:|---|
| 0 | AI relies on uncontrolled sources, sensitive data lacks rules, access is materially excessive, or consequential outputs cannot be reconstructed. |
| 25 | Some sources, privacy expectations, or logs exist, but ownership, freshness, permissions, retention, or coverage remains weak. |
| 50 | Approved sources, baseline data rules, and logging exist, but governance, review dates, approval history, or least-privilege enforcement remains incomplete. |
| 75 | Knowledge, access, privacy, retention, outputs, approvals, and corrections are controlled and auditable across the use case. |
| 100 | These controls are continuously governed through source ownership, access review, retention enforcement, integrity checks, and exception investigation. |

### Risk sequencing, prompt standards, and QA — `OI-AI-009`, `OI-AI-011`, `OI-AI-012`

| Score | Observable condition |
|---:|---|
| 0 | The first use case is materially high risk, behavior depends on uncontrolled prompts, or outputs are not reviewed despite consequential use. |
| 25 | A pilot, prompt, or review practice exists, but risk selection, instruction quality, sampling, failure categorization, or correction is inconsistent. |
| 50 | Low-risk sequencing, reusable instructions, and baseline QA exist, but versioning, test depth, cadence, metrics, or corrective action remains partial. |
| 75 | Bounded pilots use controlled prompts, representative tests, recurring QA, named owners, and documented corrections. |
| 100 | Risk sequencing, prompt controls, evaluation sets, failure analysis, corrective actions, and deployment decisions operate as a governed improvement loop. |

## 8. Control-state overlay

Maturity score and execution control state are separate.

| State | Use when |
|---|---|
| `ALLOW` | Low-risk, bounded assistance has approved inputs, instructions, sources, ownership, logging, and exception handling. |
| `REVIEW` | AI may prepare or recommend, but a human must approve, correct, or handle exceptions before consequential use. |
| `HALT` | Workflow, data, privacy, knowledge, boundary, review, audit, or escalation failures make implementation or continued use indefensible. |

A strong category score does not authorize every use case. Each use case requires its own control-state decision.

## 9. Confidence guidance

| Confidence | AI-readiness-specific use |
|---|---|
| High | Direct workflow, configuration, policy, access, source, prompt, log, test, and QA evidence supports the selected anchor across required scope. |
| Medium | Multiple artifacts support the result, but one important control, system surface, exception path, or test set remains incomplete. |
| Low | Result depends mainly on interviews, narrow screenshots, self-reported practice, or untested controls. |
| Unknown | Evidence is insufficient to select an anchor. |

Confidence remains separate from maturity and from ALLOW, REVIEW, or HALT routing.

## 10. Unknown, blocked, and not-applicable treatment

Use `unknown` when required evidence was not supplied or cannot be verified.

Use `blocked` when review or testing cannot proceed because of access, privacy, safety, legal, authorization, or technical restrictions.

Use `not_applicable` only under Section 5.

Do not:

- replace unknown with zero
- infer safety from absence of incidents
- infer readiness from tool ownership
- drop unknown or blocked weight
- run live customer or production tests without authorization
- expose sensitive data to test a control

A material unknown involving sensitive data, binding commitments, customer-facing behavior, review, escalation, or auditability normally forces `range_only` or `blocked` publication and may require `HALT` routing.

## 11. Duplicate-signal boundaries

| Evidence condition | Primary scoring owner | Dependency treatment |
|---|---|---|
| Workflow stages, reminders, handoffs, or CRM operations | Automation | AI Readiness scores whether the workflow is sufficiently defined for AI use. |
| Data capture or reporting instrumentation | Analytics | AI Readiness scores structure, access, fitness, and governance for the use case. |
| Customer-facing CTA or chatbot placement | Conversion | AI Readiness scores behavior boundaries and controls, not placement. |
| Published service facts, FAQs, or policies | Messaging, Offer, Trust, or Website | AI Readiness scores source approval, ownership, freshness, and retrieval control. |
| Public review outcomes | GBP or Trust | AI Readiness scores only AI-assisted review workflow controls when applicable. |
| General software security or legal compliance | External specialist domain | Record limitation and require validation; do not imply certification. |

## 12. Finding and package routing

Weak criteria route only to approved `OI-FIND-AI-*` records in `framework/findings/ai-readiness-findings.md`.

| Condition | Primary route | Roadmap phase |
|---|---|---|
| Undefined workflow, ownership, stages, or structured data | `OI-PKG-CRM-001` CRM and Follow-Up System or process prerequisite | Phase 3 before AI |
| Missing operational measurement | `OI-PKG-DASH-001` Operator Dashboard Pack | Phase 3 before or alongside AI |
| Controlled, bounded intake use case with prerequisites satisfied | `OI-PKG-AI-001` Governed AI Intake Assistant | Phase 4 — Governed AI Enablement |
| Missing privacy, review, boundary, escalation, or audit controls | Validation and control remediation before AI package | Phase 1 correction or Phase 4 prerequisite |

A category score does not automatically create a finding, authorize AI, or select a package. Every recommendation requires observation, evidence, interpretation, business impact, confidence, priority, control state, prerequisite route, package, roadmap phase, and DecisionLedger record.

## 13. Publication controls

`official` publication requires:

- minimum scope completed
- category coverage at or above 80%
- each assessed use case assigned ALLOW, REVIEW, or HALT
- no unresolved material privacy, boundary, audit, review, or escalation unknown
- duplicate-signal checks passed
- valid DecisionLedger references for reported findings

Use `provisional` when coverage is 60–79.99% or one non-critical internal control remains incompletely verified.

Use `range_only` when a material unknown could change readiness interpretation.

Use `blocked` when authorization, privacy, access, safety, or unresolved control failures prevent a defensible result.

## 14. DecisionLedger minimum record

```yaml
category_key: ai-readiness
criterion_ids: []
use_case_id: ""
evidence_refs: []
observation: ""
interpretation: ""
business_impact: ""
confidence: high|medium|low|unknown
priority: critical|high|medium|low
control_state: ALLOW|REVIEW|HALT
finding_ids: []
prerequisites: []
primary_package: null
dependent_packages: []
roadmap_phase: null
unknowns: []
blocked_conditions: []
duplicate_check_passed: false
reviewed_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 15. Validation messages

### Blocking errors

- `AI-EVID-001`: scored criterion lacks required evidence
- `AI-SCOPE-001`: minimum evaluation scope is incomplete
- `AI-STATE-001`: score conflicts with criterion state
- `AI-CTRL-001`: assessed use case lacks ALLOW, REVIEW, or HALT decision
- `AI-PRIV-001`: material privacy or access boundary is unresolved
- `AI-DUP-001`: readiness signal is double counted
- `AI-TEST-001`: live workflow was tested without authorization
- `AI-LEDGER-001`: reported finding lacks DecisionLedger traceability

### Warnings

- `AI-COVER-001`: category coverage is below 80%
- `AI-ACCESS-001`: result depends materially on client-supplied statements
- `AI-KNOW-001`: knowledge ownership or freshness is unverified
- `AI-QA-001`: QA sample or correction process is incomplete
- `AI-TOOL-001`: tool ownership is being mistaken for readiness

## 16. Worked example

Assume 12 applicable criteria:

- 9 scored criteria total 525 points
- 1 additional scored criterion scores 50
- 2 criteria are `unknown`

```text
Known Criterion Count = 10
Applicable Criterion Count = 12
Observed Category Score = 575 ÷ 10 = 57.5
Category Coverage = 10 ÷ 12 × 100 = 83.3%
```

The published category score is `58`, with `83.3%` coverage. The two unknown criteria remain visible and may still force `range_only` or `HALT` when they concern privacy, review, escalation, or customer-facing boundaries.

Example executive-safe statement:

> The business has a workable foundation for bounded internal AI assistance, but customer-facing use should remain under human review until privacy, escalation, and audit controls are fully verified.

## 17. Completion checklist

Before publishing, confirm:

- all 12 criteria have valid states
- minimum scope is complete
- weights reconcile
- unknown and blocked criteria retain applicable weight
- confidence, maturity, and control state remain separate
- each use case has a bounded task, owner, inputs, outputs, exceptions, and success condition
- privacy, access, knowledge, review, boundary, escalation, audit, prompt, and QA controls are assessed
- duplicate ownership checks pass
- findings use approved `OI-FIND-AI-*` identifiers
- prerequisites precede Phase 4 implementation
- DecisionLedger references exist
- client language avoids unsupported safety, compliance, accuracy, labor-replacement, revenue, or ROI claims

## 18. v1.0 connection

This sheet makes AI-readiness scoring reproducible across evaluators and connects evidence to use-case control states, governed findings, prerequisite routing, Phase 4 implementation decisions, publication gates, and auditable client reporting required for commercial v1.0.