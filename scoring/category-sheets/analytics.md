# Analytics Category Scoring Sheet

Version: v0.2 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `analytics`  
Default Operator Score weight: 5%  
Status: Draft foundation for commercial v1.0

## 1. Purpose and category boundary

This sheet governs scoring for measurement installation, conversion tracking, source attribution, outcome reporting, reputation monitoring, reporting cadence, and decision use.

It measures whether operating data is defined, sourced, tested, reviewed, and used to support accountable decisions.

It does not independently score:

- website conversion quality or buyer-facing form friction
- lead ownership, workflow execution, or CRM process maturity
- SEO implementation quality
- review generation quality or public response behavior
- offer strength, sales effectiveness, or commercial performance
- whether a dashboard looks polished
- inferred revenue, ROI, close rate, or traffic without validated data

Analytics scores measurement maturity, not business success. Strong performance cannot be inferred from missing data, and poor performance cannot be inferred from inaccessible systems.

## 2. Included criteria

Included prefix:

```text
OI-AN-*
```

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-AN-001` | Website analytics are installed and verifiable | Tag review, analytics access, page test | Equal |
| `OI-AN-002` | Search Console is configured and accessible | Property access, ownership evidence | Equal |
| `OI-AN-003` | Form submissions are tracked as defined conversion events | Event test, form logs, analytics records | Equal |
| `OI-AN-004` | Phone clicks or calls are measured where relevant | Event test, call logs, tracking records | Equal |
| `OI-AN-005` | Lead source is captured through a governed rule | CRM fields, UTM handling, intake records | Equal |
| `OI-AN-006` | Estimate outcomes are reported using defined statuses | CRM, estimate log, outcome records | Equal |
| `OI-AN-007` | Review growth and response completion are monitored | GBP history, review tracker, report | Equal |
| `OI-AN-008` | Priority service-page performance is visible | Page reports, landing-page analysis | Equal |
| `OI-AN-009` | A recurring reporting cadence exists | Reports, calendar, meeting notes | Equal |
| `OI-AN-010` | Reports produce decisions, owners, and actions | Decision log, action register, meeting record | Equal |

Each criterion has one weighted owner: `analytics`.

## 3. Evidence requirements

### Primary evidence

- analytics property access or direct implementation evidence
- Search Console property access or ownership confirmation
- tag and event configuration
- at least one safe form-event test
- mobile phone-click or call-tracking test where relevant
- lead-source fields and attribution rule
- at least ten recent lead or estimate records, or all when fewer exist
- estimate outcome and lost-reason definitions
- review-count and response-completion history
- reports for priority landing and service pages
- at least two recurring reporting periods where available
- meeting notes, action logs, or DecisionLedger records showing metric use

### Supporting evidence

- client interview
- analytics screenshots or exports
- tag-manager records
- CRM exports
- call logs
- accounting reconciliation
- metric dictionary
- dashboard documentation
- reporting SOP
- tracking-change history

### Evidence that cannot support a point score alone

- an analytics account screenshot without implementation verification
- a dashboard screenshot without source and metric definitions
- software subscription or vendor presence
- isolated traffic totals without date range, source, and context
- owner recollection used as a substitute for records
- estimated conversion, revenue, lead volume, close rate, or ROI
- third-party grades without underlying measurement evidence

## 4. Minimum evaluation scope

An Analytics category score is admissible only when the evaluator reviews:

1. analytics installation status
2. Search Console status
3. all primary inquiry event types
4. source-attribution fields and rules
5. at least ten recent lead or estimate records, or all when fewer exist
6. estimate status and outcome definitions
7. review-growth reporting
8. priority service-page reporting
9. recurring report cadence
10. evidence that reports produce named decisions or actions

If access is unavailable, affected criteria become `unknown` or `blocked`. Inaccessibility does not establish failure.

## 5. Applicability rules

All criteria are normally applicable to contractor and local-service businesses.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples:

- `OI-AN-004` when phone is not an offered inquiry path
- `OI-AN-006` when the business does not use estimates or proposals and an equivalent governed outcome measure exists
- `OI-AN-008` when no distinct priority service pages exist, provided the related website or SEO deficiency is scored in its owning category

The following do not justify `not_applicable`:

- tracking was never configured
- data access was not granted
- the system cannot produce the metric
- the metric would expose weak performance
- the evaluator considers the criterion optional

## 6. Weighting rule

All applicable criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before recalculation. Unequal weighting requires a versioned methodology change under `scoring/weight-rules.md`.

## 7. Category-specific anchors

Use only `0`, `25`, `50`, `75`, and `100`. Interpolation is prohibited.

### Installation and access — `OI-AN-001`, `OI-AN-002`

| Score | Observable condition |
|---:|---|
| 0 | Required measurement is absent, materially broken, or configured in a way that produces misleading data. |
| 25 | Tools appear present, but ownership, access, scope, or accuracy is incomplete or unverified. |
| 50 | Core tools are installed and accessible, but implementation coverage, validation, or maintenance remains partial. |
| 75 | Analytics and Search Console are correctly configured, accessible, tested, and aligned to active website surfaces. |
| 100 | Installation, access, validation, ownership, change control, and routine QA are governed and auditable. |

### Conversion and attribution — `OI-AN-003` through `OI-AN-005`

| Score | Observable condition |
|---:|---|
| 0 | Meaningful inquiry events or sources cannot be identified, or tracking materially misstates activity. |
| 25 | Some events or source fields exist, but coverage, naming, reconciliation, or consistency is weak. |
| 50 | Primary forms, calls, and source data are tracked at a functional baseline, but gaps or reconciliation issues remain. |
| 75 | Conversion events and source attribution are defined, tested, consistently captured, and reconciled to operating records. |
| 100 | Event and attribution logic is governed through definitions, source controls, test history, monitoring, and accountable correction. |

### Outcome, reputation, and page reporting — `OI-AN-006` through `OI-AN-008`

| Score | Observable condition |
|---:|---|
| 0 | Estimate outcomes, reputation trends, or priority-page activity cannot be measured or are materially unreliable. |
| 25 | Partial reporting exists, but statuses, formulas, sources, or coverage are inconsistent. |
| 50 | Core outcomes and trends are visible, but definitions, completeness, segmentation, or reconciliation remains incomplete. |
| 75 | Estimate outcomes, review activity, and priority-page performance are consistently defined, sourced, and usable. |
| 100 | These measures are governed through approved definitions, source reconciliation, thresholds, change history, and routine QA. |

### Reporting cadence and decision use — `OI-AN-009`, `OI-AN-010`

| Score | Observable condition |
|---:|---|
| 0 | Reporting is absent, materially misleading, or does not support any accountable operating decision. |
| 25 | Reports are produced irregularly or consumed passively without clear ownership or action. |
| 50 | A recurring reporting baseline exists, but decisions, owners, triggers, or follow-through are inconsistent. |
| 75 | Reports are reviewed on schedule and produce documented decisions, owners, due dates, and follow-up. |
| 100 | Reporting operates as an auditable decision system with governed metrics, thresholds, actions, review, and corrective learning. |

## 8. Metric governance requirements

A metric may support a score above `50` only when the following are defined:

```yaml
metric_name: ""
business_question: ""
definition: ""
source_system: ""
calculation: ""
owner: ""
review_cadence: ""
action_trigger: ""
validation_status: tested|partially_tested|unverified
data_limitations: []
```

Installed tracking without tested accuracy cannot support a `75` or `100` anchor.

## 9. Confidence guidance

| Confidence | Factor | Analytics-specific use |
|---|---:|---|
| High | 1.00 | Direct access, tested events, reconciled records, governed definitions, and repeated reporting evidence support the selected anchor. |
| Medium | 0.75 | Exports, screenshots, or partial tests support the result, but one material source, period, or reconciliation step remains incomplete. |
| Low | 0.50 | Result depends mainly on interviews, isolated screenshots, stale exports, or unverified installation. |
| Unknown | 0.00 | Evidence is insufficient to select an anchor. |

```text
Category Confidence Index = Sum of scored-criterion confidence factors ÷ Scored Criterion Count
```

Confidence remains separate from maturity. High confidence that data is unavailable does not establish poor operating performance.

For defensible bounds, apply the approved confidence adjustment from `scoring/confidence-adjusted-scoring.md` to each scored criterion. Unknown criteria contribute `0–100` while remaining inside applicable weight. The resulting range is an evidence-bound estimate, not a statistical confidence interval.

## 10. Unknown, blocked, and not-applicable treatment

Use `unknown` when evidence is unavailable or insufficient.

Use `blocked` when access, privacy, authorization, ownership, or testing restrictions prevent defensible evaluation.

Use `not_applicable` only under Section 5.

Do not:

- replace unknown with zero
- infer performance from missing measurement
- remove unknown or blocked weight
- claim tracking accuracy from installation alone
- reconstruct metrics without disclosing method and limitations
- test live contact paths without authorization

A material unknown affecting conversion events, source attribution, or estimate outcomes forces `range_only` or `blocked` publication until validation resolves the uncertainty.

## 11. Duplicate-signal boundaries

| Evidence condition | Primary scoring owner | Dependency treatment |
|---|---|---|
| Form UX, CTA placement, or confirmation copy | Conversion | Analytics scores event measurement only. |
| Lead routing, ownership, stages, and reminder execution | Automation | Analytics scores whether those states are measurable and reported. |
| SEO implementation or content quality | SEO | Analytics scores Search Console access and performance visibility only. |
| Review generation or public response quality | GBP or Trust | Analytics scores trend and completion measurement only. |
| Offer quality, pricing, or close effectiveness | Messaging/Offer | Analytics may report outcomes but does not score commercial strength. |
| AI-generated analysis or recommendations | AI readiness | Analytics owns source and metric integrity; AI readiness owns model controls and review gates. |

Cross-domain dependencies must be referenced without duplicating weighted points.

## 12. Finding and package routing

Weak criteria route only to approved `OI-FIND-AN-*` records in `framework/findings/analytics-findings.md`.

| Condition | Primary package | Roadmap phase |
|---|---|---|
| Missing or unverified analytics, Search Console, events, metrics, or reporting | Operator Dashboard Pack | Phase 3 — Automation and Reporting |
| Missing source fields, statuses, outcomes, or record discipline | CRM and Follow-Up System | Phase 3 — Automation and Reporting |
| Broken form or call path revealed during testing | Website Conversion Fix Pack | Phase 1 — Quick Wins |
| Weak review measurement tied to weak review workflow | Operator Dashboard Pack | Phase 3 — Automation and Reporting |
| AI-assisted reporting proposed before metric stability | No AI routing until definitions, sources, review gates, and auditability are established | Phase 4 only after prerequisites |

Each validated recommendation receives exactly one primary package. Related packages may be recorded only as dependencies. Unknown criteria route first to `Phase 0 — Validation and Access`, with `primary_package: null` and `implementation_authorized: false`.

A category score does not automatically create a finding or recommendation. Every routed action requires observation, evidence, interpretation, impact, confidence, priority, package, roadmap phase, and DecisionLedger traceability.

## 13. Publication controls

`official` publication requires:

- minimum scope completed
- category coverage at or above 80%
- tested status for primary conversion events
- documented metric definitions for reported KPIs
- no unresolved material unknown
- no unresolved duplicate-signal failure
- no unsupported traffic, lead, conversion, revenue, close-rate, or ROI claims
- valid DecisionLedger references for report findings

Use `provisional` when coverage is 60–79.99% or one non-material source remains partially verified.

Use `range_only` when unknown measurement conditions could materially change interpretation.

Use `blocked` when access, privacy, ownership, authorization, or data-integrity failures prevent a defensible result.

Publication does not authorize implementation.

## 14. DecisionLedger minimum record

```yaml
category_key: analytics
criterion_ids: []
evidence_refs: []
metric_definitions: []
observation: ""
interpretation: ""
measurement_impact: ""
observed_indicator: null
coverage_percent: null
confidence_index: null
confidence_band: high|medium|low|unknown
score_range: [null, null]
publication_state: official|provisional|range_only|blocked
review_state: ALLOW|REVIEW|HALT
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
reviewed_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 15. Validation messages

### Blocking errors

- `AN-EVID-001`: scored criterion lacks admissible evidence
- `AN-SCOPE-001`: minimum evaluation scope is incomplete
- `AN-STATE-001`: score conflicts with criterion state
- `AN-DUP-001`: measurement condition is double counted
- `AN-TEST-001`: tracking accuracy is claimed without testing
- `AN-METRIC-001`: reported KPI lacks a governed definition
- `AN-CONF-001`: confidence index is absent, nonnumeric, or unreproducible
- `AN-BOUND-001`: defensible bounds are absent, incomplete, or conflict with criterion states
- `AN-PUB-001`: publication state conflicts with coverage, material unknowns, or evidence gates
- `AN-ROUTE-001`: unknown evidence creates an implementation recommendation or package assignment
- `AN-AUTH-001`: implementation is represented as authorized without a separate approval record
- `AN-CLAIM-001`: unsupported performance or ROI claim is present
- `AN-LEDGER-001`: reported finding lacks DecisionLedger traceability

### Warnings

- `AN-COVER-001`: category coverage is below 80%
- `AN-ACCESS-001`: result depends materially on inaccessible systems or client statements
- `AN-RECON-001`: analytics and operating records have not been reconciled
- `AN-DECISION-001`: report cadence exists but decision use is unverified
- `AN-CHANGE-001`: tracking changes lack validation history

## 16. Worked example

Canonical regression fixture: `scoring/examples/analytics-worked-example.md`.

The fixture evaluates 10 applicable criteria: eight scored and two unknown. Five scored criteria have high confidence and three have medium confidence.

```text
Known maturity total = 450
Scored criterion count = 8
Observed Category Score = 450 ÷ 8 = 56.25
Displayed observed indicator = 56

Coverage = 8 ÷ 10 × 100 = 80.00%
Confidence Index = ((5 × 1.00) + (3 × 0.75)) ÷ 8 = 0.90625
Displayed confidence index = 0.9063

Known lower-bound total = 412.5
Known upper-bound total = 487.5
Unknown lower-bound total = 0
Unknown upper-bound total = 200
Category Lower Bound = 412.5 ÷ 10 = 41.25
Category Upper Bound = 687.5 ÷ 10 = 68.75
```

```yaml
score_value: null
score_type: range
observed_indicator: 56
score_range: [41.25, 68.75]
coverage_percent: 80.0
confidence_index: 0.9063
confidence_band: high
publication_state: range_only
material_unknowns:
  - OI-AN-005
  - OI-AN-006
review_state: REVIEW
validation_required: true
primary_package: null
roadmap_phase: "Phase 0 — Validation and Access"
implementation_authorized: false
ledger_ref: OI-DL-2026-011
```

The observed indicator is not an official category score. Lead-source attribution and estimate-outcome reporting are material unknowns, so publication remains `range_only` and implementation routing remains blocked pending validation.

Executive-safe statement:

> Analytics maturity is supported by verified installation, core event tracking, reporting, and documented decision use across the reviewed scope. Lead-source attribution and estimate-outcome reporting remain unverified, so the current evidence supports a range of 41.25–68.75 rather than a single official category score. Validation is required before implementation routing or performance conclusions.

## 17. Completion checklist

Before publishing, confirm:

- all 10 criteria have valid states
- minimum scope is complete
- the canonical 5% category weight reconciles
- observed indicator, coverage, confidence index, and bounds reproduce the registered fixture
- unknown and blocked criteria retain applicable weight
- confidence is separate from maturity
- tracking installation is not treated as proof of accuracy
- metric definitions, sources, owners, cadences, and action triggers exist where required
- duplicate ownership checks pass
- findings use approved `OI-FIND-AN-*` identifiers
- unknown criteria route to validation before implementation
- each validated recommendation has exactly one primary package
- publication and implementation authorization remain separate
- DecisionLedger references exist
- client language avoids unsupported traffic, conversion, revenue, close-rate, and ROI claims

## 18. v1.0 connection

This sheet makes analytics scoring reproducible, protects the Operator Score from unsupported measurement assumptions, and connects evidence quality to governed findings, package routing, roadmap sequencing, publication controls, and auditable client reporting required for commercial v1.0.
