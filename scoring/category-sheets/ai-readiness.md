# AI Readiness Category Scoring Sheet

Version: v0.2 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `ai-readiness`  
Default Operator Score weight: 5%  
Status: Reconciled commercial v1.0 scoring contract

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

Included prefix: `OI-AI-*`

| Criterion ID | Observable condition | Primary evidence | Weighting |
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

## 3. Evidence requirements

Primary evidence includes:

- target workflow, owner, inputs, outputs, handoffs, exceptions, and completion state
- source-system or data-schema evidence
- bounded use-case definition and success condition
- human approval and exception rules
- customer-facing boundaries and prohibited actions
- approved knowledge sources with ownership and review dates
- output, approval, correction, and action logs
- privacy, access, retention, sharing, and prohibited-data rules
- risk-ranked pilot sequence
- escalation triggers, route, owner, and test evidence
- controlled prompt or system-instruction inventory
- QA sample, failure taxonomy, cadence, and correction record

Supporting evidence may include interviews, configuration screenshots, access-role reviews, sample transcripts, boundary tests, change logs, and incident records.

The following cannot support a point score alone:

- an AI subscription or login screen
- a successful demo without repeatable workflow evidence
- vendor claims about safety, privacy, or accuracy
- generic prompts not used in the workflow
- owner enthusiasm or stated intent
- estimated savings, revenue, or replacement capacity without validated operating data

## 4. Minimum evaluation scope

A category result is admissible only when the evaluator reviews:

1. at least one proposed or active use case
2. the complete target workflow and owner
3. required inputs and source systems
4. human review requirements
5. customer-facing boundaries when applicable
6. approved knowledge sources
7. privacy, access, retention, and sharing rules
8. output and approval logging
9. escalation triggers and route
10. prompt instructions
11. at least ten representative tests, or all available when fewer exist
12. QA ownership, cadence, and corrective-action process

When no use case is proposed or active, baseline readiness may be assessed, but client-facing conclusions must not imply implementation need.

Unavailable internal evidence becomes `unknown` or `blocked`. Missing access is not score `0`.

## 5. Applicability and weighting

All criteria are normally applicable when AI use is active, proposed, or materially under consideration.

Use `not_applicable` only when structural irrelevance is documented and approved. Missing policy, missing tooling, incomplete implementation, or score impact do not justify `not_applicable`.

All applicable criteria use equal weighting:

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before recalculation. Unequal weighting requires a versioned methodology change under `scoring/weight-rules.md`.

## 6. Maturity anchors

Use only `0`, `25`, `50`, `75`, and `100`. Interpolation is prohibited.

| Anchor | General interpretation |
|---:|---|
| 0 | Required control is absent, materially unsafe, unusable, or uncontrolled. |
| 25 | Partial practice exists, but scope, ownership, enforcement, or evidence is materially weak. |
| 50 | A functional baseline exists, but governance, testing, exception handling, or consistency remains incomplete. |
| 75 | The control is clear, implemented, owned, tested, and suitable for the reviewed use case. |
| 100 | The control is versioned, monitored, auditable, stress-tested, and governed through continuous improvement. |

Apply these anchors to four criterion groups:

- workflow, data, and use-case definition: `OI-AI-001` through `OI-AI-003`
- human control, boundaries, and escalation: `OI-AI-004`, `OI-AI-005`, `OI-AI-010`
- knowledge, privacy, and auditability: `OI-AI-006` through `OI-AI-008`
- risk sequencing, prompt standards, and QA: `OI-AI-009`, `OI-AI-011`, `OI-AI-012`

## 7. Control-state overlay

Maturity, evidence confidence, and execution control state are separate.

| State | Use when |
|---|---|
| `ALLOW` | Low-risk, bounded assistance has approved inputs, instructions, sources, ownership, logging, and exception handling. |
| `REVIEW` | AI may prepare or recommend, but a human must approve, correct, or handle exceptions before consequential use. |
| `HALT` | Workflow, data, privacy, knowledge, boundary, review, audit, or escalation failures make implementation or continued use indefensible. |

A strong category result does not authorize every use case. Each use case requires its own control-state decision.

## 8. Confidence and uncertainty

Use the approved confidence factors:

| Confidence | Factor |
|---|---:|
| high | 1.00 |
| medium | 0.75 |
| low | 0.50 |
| unknown | not scored |

```text
Confidence Index = Σ confidence factors ÷ scored criterion count
```

Confidence remains separate from maturity and from `ALLOW`, `REVIEW`, or `HALT`.

For unresolved applicable criteria, publish a defensible range:

```text
Lower Bound = known score total ÷ applicable criterion count
Upper Bound = (known score total + maximum unresolved score total) ÷ applicable criterion count
```

Using zero in the lower-bound calculation does not convert an unknown criterion into a scored zero. It represents the minimum defensible category result while the state remains unresolved.

## 9. Unknown, blocked, and not-applicable treatment

Use `unknown` when required evidence was not supplied or cannot be verified.

Use `blocked` when review or testing cannot proceed because of authorization, privacy, safety, legal, access, or technical restrictions.

Do not:

- replace unknown with zero
- infer safety from absence of incidents
- infer readiness from tool ownership
- remove unknown or blocked weight
- run live customer or production tests without authorization
- expose sensitive data to test a control

A material unknown involving sensitive data, binding commitments, customer-facing behavior, review, escalation, or auditability forces `range_only` or `blocked` publication and may require `HALT` routing.

## 10. Duplicate-signal boundaries

| Evidence condition | Primary scoring owner | AI Readiness treatment |
|---|---|---|
| Workflow stages, reminders, handoffs, or CRM operations | Automation | Score only whether the workflow is sufficiently defined for AI use. |
| Data capture or reporting instrumentation | Analytics | Score structure, access, fitness, and governance for the use case. |
| Customer-facing CTA or chatbot placement | Conversion | Score behavior boundaries and controls, not placement. |
| Published service facts, FAQs, or policies | Messaging, Offer, Trust, or Website | Score source approval, ownership, freshness, and retrieval control. |
| Public review outcomes | GBP or Trust | Score only AI-assisted workflow controls when applicable. |
| General software security or legal compliance | External specialist domain | Record the limitation and require validation; do not imply certification. |

## 11. Finding and package routing

Weak criteria route only to approved `OI-FIND-AI-*` records in `framework/findings/ai-readiness-findings.md`.

| Condition | Primary route | Roadmap phase |
|---|---|---|
| Undefined workflow, ownership, stages, or structured data | `OI-PKG-CRM-001` or process prerequisite | Phase 3 before AI |
| Missing operational measurement | `OI-PKG-DASH-001` | Phase 3 before or alongside AI |
| Controlled bounded intake with prerequisites satisfied | `OI-PKG-AI-001` | Phase 4 — Governed AI Enablement |
| Missing privacy, review, boundary, escalation, or audit controls | Validation and control remediation | Phase 0 or governed prerequisite |

A category result does not automatically create a finding, authorize AI, or select a package. Unknown criteria create validation requirements, not implementation findings.

Every recommendation requires a valid finding, evidence, interpretation, bounded business impact, confidence, priority, control state, prerequisites, exactly one primary package, roadmap phase, and DecisionLedger record.

## 12. Publication controls

`official` requires:

- minimum scope completed
- coverage at or above 80%
- each assessed use case assigned `ALLOW`, `REVIEW`, or `HALT`
- no unresolved material privacy, boundary, audit, review, or escalation unknown
- duplicate-signal checks passed
- valid DecisionLedger references for reported findings

Use:

- `provisional` when a bounded, non-material limitation remains
- `range_only` when a material unknown could change readiness interpretation
- `blocked` when authorization, privacy, access, safety, or unresolved control failures prevent a defensible result

## 13. DecisionLedger minimum record

```yaml
category_key: ai-readiness
criterion_ids: []
use_case_id: ""
evidence_refs: []
observed_indicator: null
coverage_percent: null
confidence_index: null
score_range: null
publication_state: internal_only|official|provisional|range_only|blocked
observation: ""
interpretation: ""
business_impact: ""
confidence: high|medium|low|unknown
priority: critical|high|medium|low
control_state: ALLOW|REVIEW|HALT
finding_ids: []
validation_required: []
prerequisites: []
primary_package: null
dependent_packages: []
roadmap_phase: null
unknowns: []
blocked_conditions: []
duplicate_check_passed: false
implementation_authorized: false
reviewed_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 14. Validation messages

### Blocking errors

- `AI-EVID-001`: scored criterion lacks required evidence
- `AI-SCOPE-001`: minimum evaluation scope is incomplete
- `AI-STATE-001`: score conflicts with criterion state
- `AI-CONF-001`: confidence index is missing or cannot be reproduced
- `AI-RANGE-001`: unresolved applicable weight lacks defensible bounds
- `AI-PUB-001`: publication state conflicts with coverage or material unknowns
- `AI-CTRL-001`: assessed use case lacks `ALLOW`, `REVIEW`, or `HALT`
- `AI-PRIV-001`: material privacy or access boundary is unresolved
- `AI-ROUTE-001`: unknown criterion creates a finding or package without validation
- `AI-AUTH-001`: publication or review state is treated as implementation authorization
- `AI-DUP-001`: readiness signal is double counted
- `AI-TEST-001`: live workflow was tested without authorization
- `AI-LEDGER-001`: material output lacks DecisionLedger traceability

### Warnings

- `AI-COVER-001`: category coverage is below 80%
- `AI-ACCESS-001`: result depends materially on client-supplied statements
- `AI-KNOW-001`: knowledge ownership or freshness is unverified
- `AI-QA-001`: QA sample or correction process is incomplete
- `AI-TOOL-001`: tool ownership is being mistaken for readiness

## 15. Canonical worked example

The canonical regression fixture is:

`scoring/examples/ai-readiness-worked-example.md`

Its verified outputs are:

```yaml
observed_indicator: 57.50
coverage_percent: 83.33
confidence_index: 1.0000
confidence_band: high
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
```

The two unknown controls remain inside applicable weight and prevent an official single-value score. They create validation requirements before finding creation or package routing.

Executive-safe statement:

> The reviewed evidence supports a workable foundation for bounded internal AI assistance. Privacy, access, and escalation controls require validation before customer-facing or autonomous use can be considered.

Do not state that the business is AI-ready without the range, coverage, unknowns, control state, and use-case boundary.

## 16. Completion checklist

Before publication, confirm:

- all 12 criteria have valid states
- minimum scope is complete
- weights reconcile
- unknown and blocked criteria retain applicable weight
- score, coverage, confidence index, and bounds reproduce exactly
- confidence, maturity, and control state remain separate
- each use case has bounded scope, ownership, inputs, outputs, exceptions, and success conditions
- privacy, access, knowledge, review, boundary, escalation, audit, prompt, and QA controls are assessed
- duplicate ownership checks pass
- findings use approved `OI-FIND-AI-*` identifiers
- unknowns route to validation before findings or packages
- prerequisites precede Phase 4 implementation
- implementation authorization is recorded separately
- DecisionLedger references exist
- client language avoids unsupported safety, compliance, accuracy, labor-replacement, revenue, or ROI claims

## 17. Cross references

- `scoring/examples/ai-readiness-worked-example.md`
- `scoring/examples/index.md`
- `scoring/confidence-adjusted-scoring.md`
- `scoring/unknown-data-handling.md`
- `scoring/calculator-spec.md`
- `framework/findings/ai-readiness-findings.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`

## 18. v1.0 connection

This sheet makes AI-readiness scoring reproducible across evaluators and connects evidence to use-case control states, governed findings, prerequisite routing, Phase 4 implementation decisions, publication gates, and auditable client reporting required for commercial v1.0.
