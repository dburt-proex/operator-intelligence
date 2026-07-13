# Automation Category Scoring Sheet

Version: v0.2 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `automation`  
Default Operator Score weight: 10%  
Status: Commercial v1.0 candidate

## 1. Purpose and category boundary

This sheet governs scoring for lead routing, workflow ownership, pipeline state, follow-up reliability, customer-history use, internal handoffs, and operational visibility.

It measures whether repeatable work is captured, assigned, tracked, recovered, and reviewed through controlled systems rather than memory or scattered channels.

It does not independently score:

- website CTA quality or visible form friction
- analytics installation or metric accuracy
- review volume, rating, or public response quality
- offer positioning or sales-message quality
- AI controls, model behavior, or customer-facing AI safety
- whether a specific software product is used

Manual processes may score well when they are documented, reliable, owned, measurable, and appropriate to business volume. Cross-domain effects must be recorded as dependencies, not duplicate scores.

## 2. Criterion inventory

Included prefix: `OI-AUTO-*`

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-AUTO-001` | All inquiries enter one tracked system | Channel inventory, CRM, lead tracker | Equal |
| `OI-AUTO-002` | Website forms create reliable internal notifications | Safe form test, settings, inbox evidence | Equal |
| `OI-AUTO-003` | Inquiry confirmation is automated or otherwise reliably triggered | Confirmation screen, email/SMS, workflow | Equal |
| `OI-AUTO-004` | Every lead receives a defined owner | CRM field, assignment rule, SOP | Equal |
| `OI-AUTO-005` | Lead status is tracked through defined stages | Pipeline, sample records, stage definitions | Equal |
| `OI-AUTO-006` | Follow-up reminders exist for open leads and estimates | Tasks, reminders, workflow rules | Equal |
| `OI-AUTO-007` | Estimate outcomes and lost reasons are tracked | Estimate log, CRM fields, reports | Equal |
| `OI-AUTO-008` | Review requests follow a repeatable post-job process | Workflow, templates, run history | Equal |
| `OI-AUTO-009` | Missed inquiries have a recovery path | Call, inbox, voicemail, SMS workflow | Equal |
| `OI-AUTO-010` | Customer records preserve useful service history | CRM fields, sample records | Equal |
| `OI-AUTO-011` | Repeat or seasonal outreach is systematized where relevant | Lists, campaigns, cadence records | Equal |
| `OI-AUTO-012` | Internal handoffs are documented and owned | SOP, workflow map, role definitions | Equal |
| `OI-AUTO-013` | Standard response templates exist and are controlled | Approved email/SMS templates | Equal |
| `OI-AUTO-014` | An operational dashboard or equivalent review view exists | Dashboard, report, meeting record | Equal |

Each criterion has one weighted owner: `automation`.

## 3. Required evidence surfaces

### Primary evidence

- complete inquiry-channel inventory
- website form destination and safe notification test
- confirmation screen and customer acknowledgement evidence
- CRM, spreadsheet, or lead-tracker configuration
- at least ten recent lead records, or all when fewer exist
- assignment, stage, task, and reminder rules
- estimate outcome and lost-reason fields
- review-request workflow and message template
- missed-call, voicemail, email, and social-message recovery process
- customer-record field structure and sample service history
- repeat, seasonal, or reactivation campaign evidence where applicable
- handoff SOPs or workflow maps
- approved customer-response templates
- dashboard or recurring operator report

### Supporting evidence

- client interview
- automation run history
- error logs and failed-run alerts
- meeting notes and decision logs
- role descriptions
- vendor configuration screenshots
- call logs, inbox records, and task histories

### Evidence that cannot support a point score alone

- ownership claims without sample records or workflow evidence
- software subscription screenshots without configured use
- a tool list presented as proof of operational maturity
- one successful workflow run used to infer reliability
- vendor marketing claims
- estimated time savings or revenue impact without validated operating data

## 4. Minimum evaluation scope

An Automation category score is admissible only when the evaluator reviews:

1. every active inquiry channel
2. the primary tracking system or documented manual source of truth
3. at least ten recent lead records, or all when fewer exist
4. one safe website-form submission or equivalent configuration evidence
5. lead ownership, stage, follow-up, and estimate-outcome controls
6. review-request and missed-inquiry recovery processes
7. customer-history fields and repeat-outreach process where relevant
8. internal handoff documentation
9. response templates
10. dashboard or recurring operational review evidence

If internal access is unavailable, affected criteria become `unknown` or `blocked`; lack of access is not a score of zero.

## 5. Applicability rules

All criteria are normally applicable to contractor and local-service businesses.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples:

- `OI-AUTO-008` when the business cannot ethically or contractually request public reviews
- `OI-AUTO-011` when the service model has no reasonable repeat, maintenance, seasonal, or reactivation path
- `OI-AUTO-014` when a documented low-volume operating review provides equivalent decision visibility without a dashboard

The following do not justify `not_applicable`: the process has not been built, evidence was not provided, the current tool lacks the capability, the criterion would lower the score, or the evaluator prefers a different tool.

## 6. Weighting and calculation rules

All applicable criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
Observed Category Score = Sum of scored maturity anchors ÷ Scored Criterion Count
Coverage = Scored Applicable Weight ÷ Total Applicable Weight × 100
Confidence Index = Sum of confidence factors for scored criteria ÷ Scored Criterion Count
```

Confidence factors:

```text
high = 1.00
medium = 0.75
low = 0.50
unknown = 0.00
```

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before recalculation. Unknown is excluded from the observed maturity denominator because no anchor is defensible, but contributes `0–100` to defensible bounds. Unequal weighting is prohibited without a versioned methodology change under `scoring/weight-rules.md`.

## 7. Category-specific anchors

Use only `0`, `25`, `50`, `75`, and `100`. Interpolation is not permitted.

### Capture, notification, confirmation, and recovery — `OI-AUTO-001` through `OI-AUTO-003`, `OI-AUTO-009`

| Score | Observable condition |
|---:|---|
| 0 | Material inquiry paths are untracked, broken, or fail without a defined recovery or acknowledgement path. |
| 25 | Some capture and notification exists, but channels remain scattered, manual, inconsistently monitored, or failure-prone. |
| 50 | Primary channels are captured and acknowledged at a functional baseline, but backup routing, monitoring, or recovery remains incomplete. |
| 75 | Inquiry capture, internal notification, customer confirmation, and missed-inquiry recovery are consistent across active channels. |
| 100 | The system is monitored, tested, auditable, owner-assigned, and governed through documented failure and escalation controls. |

### Ownership, pipeline, follow-up, and estimates — `OI-AUTO-004` through `OI-AUTO-007`

| Score | Observable condition |
|---:|---|
| 0 | Leads lack accountable ownership or usable state, and open work cannot be reliably identified or progressed. |
| 25 | Ownership or stages exist informally, but records, reminders, estimate outcomes, or lost reasons are materially inconsistent. |
| 50 | A functional pipeline tracks core ownership and status, but follow-up discipline, outcome data, or exception handling remains incomplete. |
| 75 | Ownership, stages, reminders, estimate outcomes, and lost reasons are consistently recorded and used. |
| 100 | Pipeline controls are required, monitored, quality-checked, auditable, and tied to defined escalation and review cadences. |

### Customer lifecycle and communications — `OI-AUTO-008`, `OI-AUTO-010`, `OI-AUTO-011`, `OI-AUTO-013`

| Score | Observable condition |
|---:|---|
| 0 | Customer history is unusable and repeatable review, response, or reactivation processes are absent or materially unsafe. |
| 25 | Some records and templates exist, but use depends on memory, individual staff, or inconsistent lists. |
| 50 | Baseline customer history, templates, and post-job processes exist, but segmentation, approvals, cadence, or measurement remains partial. |
| 75 | Customer records support consistent review requests, approved communication, and relevant repeat or seasonal outreach. |
| 100 | Lifecycle communications are permission-aware, version-controlled, monitored, auditable, and routinely improved from observed results. |

### Handoffs and operational visibility — `OI-AUTO-012`, `OI-AUTO-014`

| Score | Observable condition |
|---:|---|
| 0 | Critical handoffs depend on tribal knowledge and the owner cannot reliably see active pipeline or follow-up state. |
| 25 | Some handoff notes or reports exist, but ownership, cadence, completeness, or decision use is inconsistent. |
| 50 | Core handoffs and operational views provide a usable baseline, but exceptions, accountability, or decision tracking remains incomplete. |
| 75 | Handoffs are documented and the operating view routinely supports accountable actions and follow-up. |
| 100 | Handoffs, controls, dashboards, decisions, exceptions, and corrective actions are governed through an auditable operating cadence. |

## 8. Confidence guidance

| Confidence | Factor | Automation-specific use |
|---|---:|---|
| High | 1.00 | Direct system access, safe tests, sample records, rules, logs, templates, and review evidence support the anchor across required scope. |
| Medium | 0.75 | Multiple records and workflow evidence support the result, but one important channel, rule, sample, or monitoring surface remains incomplete. |
| Low | 0.50 | Result depends mainly on interview statements, narrow screenshots, stale exports, or incomplete records. |
| Unknown | 0.00 | Evidence is insufficient to select an anchor. |

Confidence remains separate from maturity. A well-evidenced manual process may score higher than an unreliable automation.

For defensible bounds, apply the approved confidence uncertainty to each scored anchor and `0–100` to each unknown criterion. Bounds are evidence ranges, not statistical confidence intervals.

## 9. Unknown, blocked, and not-applicable treatment

Use `unknown` when required evidence was not supplied or cannot be verified. Use `blocked` when review cannot proceed because of access, privacy, safety, authorization, or control restrictions. Use `not_applicable` only under Section 5.

Do not replace unknown with zero, infer failure from missing access, drop unknown or blocked weight, award maturity because a tool is purchased, or test live customer workflows without authorization.

A high-materiality unknown affecting inquiry capture, ownership, notification, recovery, or follow-up forces `range_only` or `blocked` publication until resolved.

## 10. Duplicate-signal boundaries

| Evidence condition | Primary scoring owner | Dependency treatment |
|---|---|---|
| Visible form friction or CTA weakness | Conversion | Automation scores only routing, notification, acknowledgement, and internal handling. |
| Lead-source instrumentation or reporting accuracy | Analytics | Automation scores workflow use and ownership, not measurement installation. |
| Review volume or public response quality | GBP or Trust | Automation scores the request workflow only. |
| Sales messaging or offer follow-up content | Messaging/Offer | Automation scores repeatability, trigger, ownership, and state. |
| AI-generated customer communication | AI readiness | Automation may score workflow integration; AI controls remain owned by AI readiness. |
| Competitor workflow advantage | Competitive | Record as dependency only when directly evidenced. |

One operational condition may support several findings only when each measures a distinct governed condition.

## 11. Finding and recommendation routing

Weak scored criteria route only to approved `OI-FIND-AUTO-*` records in `framework/findings/automation-findings.md`.

An unknown criterion may create a validation finding, but it may not authorize implementation. Validation findings use `primary_package: null`, route to `Phase 0 — Validation and Access`, and require a superseding DecisionLedger event before remediation routing.

| Validated condition | Primary package | Roadmap phase |
|---|---|---|
| Scattered lead capture, unclear ownership, weak stages, or memory-based follow-up | `OI-PKG-CRM-001` CRM and Follow-Up System | Phase 3 — Automation and Reporting |
| Broken visible form confirmation | `OI-PKG-WEB-001` Website Conversion Fix Pack | Phase 1 — Foundations and Critical Fixes |
| Inconsistent review-request workflow | `OI-PKG-REV-001` Review Generation System | Phase 3 — Automation and Reporting |
| Missing operational visibility | `OI-PKG-DASH-001` Operator Dashboard Pack | Phase 3 — Automation and Reporting |
| Customer-facing AI workflow with adequate prerequisites | `OI-PKG-AI-001` Governed AI Intake Assistant | Phase 4 — Governed AI Enablement |

A category score does not automatically create a finding or select a package. Every implementation recommendation requires a validated finding and exactly one primary package.

## 12. Publication controls

`official` publication requires minimum scope completion, coverage at or above 80%, adequate material confidence, no unresolved material unknown, no unresolved G4 boundary, no duplicate-signal failure, verified critical capture evidence, and valid DecisionLedger references.

Use:

- `provisional` when a bounded non-material limitation remains
- `range_only` when a material unknown could change category interpretation
- `blocked` when privacy, authorization, safety, evidence conflict, or control failure prevents a defensible result

A displayed observed indicator is not an official category score when publication state is `range_only`.

## 13. DecisionLedger minimum record

```yaml
category_key: automation
criterion_ids: []
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
finding_ids: []
validation_required: false
primary_package: null
dependent_packages: []
roadmap_phase: null
unknowns: []
blocked_conditions: []
duplicate_check_passed: false
implementation_authorized: false
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 14. Validation messages

### Blocking errors

- `AUTO-EVID-001`: scored criterion lacks required evidence
- `AUTO-SCOPE-001`: minimum evaluation scope is incomplete
- `AUTO-STATE-001`: score conflicts with criterion state
- `AUTO-DUP-001`: operational condition is double counted
- `AUTO-TEST-001`: live workflow was tested without authorization
- `AUTO-GATE-001`: unresolved G4 control boundary exists
- `AUTO-LEDGER-001`: reported finding lacks DecisionLedger traceability
- `AUTO-CONF-001`: confidence index is missing, nonnumeric, or inconsistent with criterion factors
- `AUTO-BOUND-001`: required lower or upper bound is missing or cannot be reproduced
- `AUTO-PUB-001`: a single official score is published while a material unknown remains unresolved
- `AUTO-ROUTE-001`: an unknown criterion is routed directly to implementation
- `AUTO-AUTH-001`: publication or review approval is treated as implementation authorization

### Warnings

- `AUTO-COVER-001`: category coverage is below 80%
- `AUTO-ACCESS-001`: result depends materially on client-supplied statements
- `AUTO-MONITOR-001`: workflow exists but failure monitoring is unverified
- `AUTO-TOOL-001`: software presence is being mistaken for process maturity

## 15. Worked example

The canonical regression fixture is `scoring/examples/automation-worked-example.md`.

Its verified result is:

```yaml
observed_indicator: 58
coverage_percent: 85.7
confidence_index: 0.9167
confidence_band: high
score_range: [46.43, 67.86]
publication_state: range_only
material_unknowns:
  - OI-AUTO-009
  - OI-AUTO-014
review_state: REVIEW
validation_required: true
primary_package: null
roadmap_phase: "Phase 0 — Validation and Access"
implementation_authorized: false
ledger_ref: OI-DL-2026-010
```

The high confidence index applies only to known evidence. `OI-AUTO-009` remains material, so coverage above 80% and high confidence on scored criteria do not permit a single official score.

Executive-safe statement:

> Automation maturity is supported by a functional lead-management baseline across the reviewed records. Missed-inquiry recovery and recurring operating visibility remain unverified, so the current evidence supports a range of 46.43–67.86 rather than a single official category score. Validation is required before implementation routing.

## 16. Completion checklist

Before publishing, confirm:

- all 14 criteria have valid states
- minimum scope is complete
- weights and observed maturity reproduce
- numeric confidence index reproduces from criterion factors
- lower and upper bounds reproduce
- unknown and blocked criteria retain applicable weight
- confidence remains separate from maturity
- duplicate ownership checks pass
- findings use approved `OI-FIND-AUTO-*` identifiers
- unknown findings route to validation before implementation
- each implementation recommendation has exactly one primary package
- publication state matches material unknowns and bounds
- implementation authorization is recorded separately
- DecisionLedger references exist
- client language avoids unsupported lead-loss, revenue, capacity, savings, or ROI claims

## 17. Cross references

- `scoring/examples/automation-worked-example.md`
- `scoring/calculator-spec.md`
- `scoring/confidence-adjusted-scoring.md`
- `scoring/unknown-data-handling.md`
- `framework/findings/automation-findings.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`

## 18. v1.0 connection

This sheet makes Automation scoring reproducible across evaluators and connects operational evidence to governed findings, validation-first unknown handling, controlled package routing, roadmap sequencing, publication gates, and auditable client reporting required for commercial v1.0.