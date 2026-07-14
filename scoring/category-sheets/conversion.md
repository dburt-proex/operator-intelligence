# Conversion Infrastructure Category Scoring Sheet

Version: v0.2 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `conversion`  
Default Operator Score weight: 15%  
Status: Reconciled commercial v1.0 scoring contract

## 1. Purpose and category boundary

This sheet governs scoring for conversion infrastructure.

The category measures whether buyer interest can become a captured, acknowledged, attributable, and actionable inquiry through clear calls to action, usable intake paths, appropriate qualification, confirmation, and channel choice.

It includes:

- CTA visibility and intent alignment
- CTA placement across service pages
- form qualification and friction
- post-submit confirmation
- mobile tap-to-call
- service-specific inquiry prompts
- project-detail capture
- response-time expectations
- proof placement near decision points
- multiple conversion paths
- urgent-buyer handling where relevant
- lead-source capture readiness

It does not independently score:

- website navigation or page architecture
- message quality or offer strength
- internal lead assignment, CRM automation, or follow-up execution
- analytics reporting quality
- organic visibility or traffic generation
- trust-asset credibility outside conversion placement

Cross-domain effects must be recorded as dependencies rather than duplicate scores.

## 2. Criterion inventory

Included prefix:

```text
OI-CONV-*
```

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-CONV-001` | Primary CTA is visible above the fold | Desktop and mobile homepage screenshots | Equal |
| `OI-CONV-002` | CTA language matches buyer intent | CTA text inventory | Equal |
| `OI-CONV-003` | CTAs appear throughout service pages | Service-page screenshots | Equal |
| `OI-CONV-004` | Contact form captures useful qualification data | Form field inventory | Equal |
| `OI-CONV-005` | Form friction matches service complexity and buyer stage | Field count and completion test | Equal |
| `OI-CONV-006` | Confirmation sets expectations after submission | Safe test submission or verified workflow record | Equal |
| `OI-CONV-007` | Mobile tap-to-call exists and functions | Mobile interaction test | Equal |
| `OI-CONV-008` | Service pages contain service-specific inquiry prompts | Service-page CTA review | Equal |
| `OI-CONV-009` | Buyer can provide project details easily | Form, intake, upload, or structured prompt review | Equal |
| `OI-CONV-010` | Response-time expectation is visible | Contact page, CTA area, and confirmation review | Equal |
| `OI-CONV-011` | Social proof appears near CTAs | CTA-section screenshots | Equal |
| `OI-CONV-012` | Multiple usable conversion paths exist | Phone, form, booking, email, or alternate channel tests | Equal |
| `OI-CONV-013` | Urgent buyers have a clear path where relevant | Urgent-service pages, phone prominence, availability language | Equal |
| `OI-CONV-014` | Lead source can be tracked | Form payload, hidden fields, CRM, UTM, or analytics evidence | Equal |

Each criterion has one weighted owner: `conversion`.

## 3. Required evidence surfaces

### Primary evidence

- homepage desktop and mobile above-fold screenshots
- CTA inventory across homepage and core service pages
- at least one complete inquiry-path test
- form field and validation review
- safe post-submit confirmation test
- mobile tap-to-call test
- contact or estimate page review
- proof placement near primary CTAs
- urgent-service path review when structurally relevant
- source-capture evidence for `OI-CONV-014`

### Supporting evidence

- form-builder configuration
- CRM intake records
- booking-system settings
- email or SMS acknowledgement examples
- UTM and hidden-field configuration
- analytics conversion-event configuration
- client-approved response standard

### Evidence that cannot support a point score alone

- visible CTA without interaction testing
- client claim that forms work without test or record evidence
- form-builder screenshot without published-page verification
- analytics tag presence without confirmed event or destination behavior
- one service page used to infer full-site CTA coverage
- evaluator preference about ideal form length

## 4. Minimum evaluation scope

A conversion result is admissible only when the evaluator reviews, where present:

1. homepage desktop and mobile primary CTA
2. contact or estimate page
3. at least two core service pages, or all when fewer than two exist
4. all public inquiry paths used in the assessed buyer journey
5. one safe end-to-end form or booking test
6. post-submit confirmation behavior
7. mobile phone path
8. proof placement near at least two primary decision points
9. urgent-buyer path when time-sensitive service is an approved offer
10. source-capture configuration or a documented access limitation

A visible form is not sufficient evidence of successful capture, acknowledgement, routing, or attribution.

Scope exceptions require a documented limitation and may reduce publication to `provisional`, `range_only`, or `blocked`.

## 5. Applicability rules

All `OI-CONV-*` criteria are normally applicable when the business accepts public inquiries through a website or linked digital property.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples:

- `OI-CONV-007` when phone contact is intentionally unavailable by approved operating design
- `OI-CONV-013` when no assessed service has urgent or time-sensitive buyer intent
- `OI-CONV-014` only when source attribution is structurally impossible under the approved channel model, not merely unconfigured

The following do not justify `not_applicable`:

- a form was not tested
- CRM access was not provided
- the confirmation state could not be observed
- attribution settings were unavailable
- the criterion would reduce the score

Confirmed absence after the required test may support score `0`. Missing internal access normally produces `unknown` or `blocked`.

## 6. Weighting and maturity rules

All applicable conversion criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before weights are recalculated.

Use only approved maturity anchors: `0`, `25`, `50`, `75`, `100`. Interpolation is not permitted.

## 7. Category-specific anchor guidance

### CTA visibility, language, and placement — `OI-CONV-001`, `OI-CONV-002`, `OI-CONV-003`, `OI-CONV-008`

| Score | Observable condition |
|---:|---|
| 0 | Primary actions are absent, broken, misleading, or inaccessible within tested buyer journeys. |
| 25 | CTAs exist but are vague, buried, inconsistent, generic, or sparsely placed. |
| 50 | A functional primary action exists, but intent alignment, service specificity, or page coverage is materially incomplete. |
| 75 | Clear, specific CTAs appear consistently at relevant decision points across tested pages and devices. |
| 100 | CTA structure is consistently implemented, tested, measured, governed, and maintained across defined buyer journeys. |

### Form qualification and friction — `OI-CONV-004`, `OI-CONV-005`, `OI-CONV-009`

| Score | Observable condition |
|---:|---|
| 0 | Intake is absent, broken, unsafe, or unable to capture information required for action. |
| 25 | Intake exists but is materially underqualified, overlong, confusing, inaccessible, or poorly matched to the service. |
| 50 | The form captures a workable baseline but leaves material qualification, usability, or project-context gaps. |
| 75 | Intake captures appropriate project and contact detail with friction matched to service complexity and buyer stage. |
| 100 | Intake is tested, intentionally segmented, measured for completion quality, governed, and integrated with operational requirements. |

### Confirmation and response expectations — `OI-CONV-006`, `OI-CONV-010`

| Score | Observable condition |
|---:|---|
| 0 | Submission produces no reliable confirmation, misleading next steps, or a broken destination. |
| 25 | A generic confirmation appears but gives no meaningful response expectation, next step, or fallback path. |
| 50 | Submission is acknowledged and a basic next step is stated, but timing or channel expectations remain incomplete. |
| 75 | Confirmation clearly states receipt, expected response timing, next step, and alternate contact path where appropriate. |
| 100 | Confirmation is channel-aware, tested, monitored, owned, and aligned to a documented service standard. |

### Channel access and urgent intent — `OI-CONV-007`, `OI-CONV-012`, `OI-CONV-013`

| Score | Observable condition |
|---:|---|
| 0 | Relevant buyers lack a usable contact path, or tested channels are broken or misleading. |
| 25 | Only one weak path exists, mobile calling is difficult, or urgent intent receives no usable direction. |
| 50 | Buyers can contact the business through at least one working route, but channel choice or urgent handling is limited. |
| 75 | Multiple appropriate paths work across devices, and urgent buyers receive a clear route when relevant. |
| 100 | Channel options are tested, monitored, intentionally routed by buyer need, and governed through documented ownership and fallback rules. |

### Proof proximity — `OI-CONV-011`

| Score | Observable condition |
|---:|---|
| 0 | CTA-adjacent content is misleading or contains invalid proof. |
| 25 | Proof exists elsewhere but is absent, weak, or disconnected from primary decision points. |
| 50 | Some relevant proof appears near CTAs, but coverage or relevance is inconsistent. |
| 75 | Relevant reviews, project proof, guarantees, or credentials consistently support major CTAs. |
| 100 | Proof placement is journey-specific, current, verified, tested, governed, and measured for decision support. |

### Attribution readiness — `OI-CONV-014`

| Score | Observable condition |
|---:|---|
| 0 | Confirmed inquiries cannot retain any source or page context despite completed inspection. |
| 25 | Partial source data exists but is unreliable, overwritten, unstructured, or unavailable to operators. |
| 50 | Basic channel or page attribution is captured for some conversion paths, with material gaps. |
| 75 | Major inquiry paths consistently retain usable source, campaign, or page context through intake. |
| 100 | Attribution is validated end to end, normalized, governed, monitored, and usable in reporting and operational decisions. |

## 8. Confidence index and defensible bounds

Confidence remains separate from maturity.

| Confidence | Factor | Criterion bound |
|---|---:|---|
| High | 1.00 | exact selected anchor |
| Medium | 0.75 | selected anchor ±12.5 |
| Low | 0.50 | selected anchor ±25 |
| Unknown | 0.00 | 0–100 |

```text
Category Confidence Index =
Sum(Confidence Factor for Scored Criteria)
÷ Scored Criterion Count

Category Lower Bound =
Sum(Criterion Lower Bounds)
÷ Applicable Criterion Count

Category Upper Bound =
Sum(Criterion Upper Bounds)
÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside the applicable denominator and contribute `0–100` until resolved. Confidence factors never multiply maturity scores.

## 9. Unknown, blocked, and not-applicable treatment

Common `unknown` conditions:

- form destination or receipt cannot be verified
- confirmation behavior is not safely testable
- CRM or intake records are unavailable
- source fields, UTM retention, or conversion events cannot be inspected
- response standard is claimed but undocumented
- urgent-service applicability is unresolved

Common `blocked` conditions:

- test submission may create client harm, billing, dispatch, or legal commitment
- authentication or permissions prevent required inspection
- privacy-sensitive records cannot be reviewed under current authorization
- the form or booking tool is unavailable during the evaluation window
- conflicting production and staging versions prevent reliable evaluation

Every material unknown or block must record its reason, affected criterion, required evidence, validation owner, materiality, next action, and publication effect.

Unknown is not score `0`. Confirmed absence may support score `0` only after the required search or safe test is completed.

## 10. Duplicate-signal boundaries

| Overlap | Conversion owns | Adjacent category owns |
|---|---|---|
| Website | CTA and inquiry effectiveness within buyer paths | Navigation, page hierarchy, and general access to contact pages |
| Messaging and offer | Action language and service-specific prompt alignment | Positioning, differentiation, offer content, and objection handling |
| Trust | Placement of proof near conversion decisions | Validity, depth, recency, and credibility of proof assets |
| Automation | Public capture, acknowledgement state, and conversion-path readiness | Internal assignment, workflow execution, follow-up, SLA enforcement, and exception handling |
| Analytics | Source-context capture readiness at inquiry | Event instrumentation, reporting, dashboards, interpretation, and decision use |
| SEO and GBP | Conversion behavior after entry | Visibility, ranking, profile completeness, and traffic acquisition |

One form may support several criteria only when each criterion measures a distinct condition. Duplicate scoring is prohibited.

## 11. Finding and recommendation routing

A weak conversion score does not automatically create a finding or package recommendation.

Eligible primary finding domain:

```text
OI-FIND-CONV-*
```

| Evidence-backed condition | Primary route | Common package dependency |
|---|---|---|
| CTA visibility, specificity, or service-page placement is weak | Conversion finding | `OI-PKG-WEB-001` Website Conversion Fix Pack |
| Intake cannot capture actionable project context | Conversion finding | `OI-PKG-WEB-001` Website Conversion Fix Pack |
| Submission is captured but not acknowledged, assigned, or followed up | Automation finding primary; conversion dependency | `OI-PKG-CRM-001` CRM and Follow-Up System |
| Source data is not retained or usable | Analytics finding primary; conversion dependency | `OI-PKG-DASH-001` Operator Dashboard Pack |
| Proof is invalid or insufficient | Trust finding primary | `OI-PKG-TRUST-001` Trust Proof System |
| Conversion behavior cannot be safely verified | Validation record | No package commitment until validation passes |

Routing requires observation, evidence, interpretation, business impact, confidence, priority, one primary package, roadmap phase, and DecisionLedger traceability.

Do not recommend a full rebuild when a narrower correction resolves the evidence-backed constraint.

## 12. Publication controls

Conversion results use the shared publication states:

- `official`
- `provisional`
- `range_only`
- `blocked`

Additional controls:

- no `official` score without desktop and mobile CTA review
- no `official` score without one safe end-to-end inquiry-path test
- no `official` score when confirmation behavior is materially unknown
- no `official` score while a material `OI-CONV-014` attribution unknown could change interpretation
- an unresolved material attribution unknown requires `range_only` or `blocked`
- a broken primary inquiry path requires `REVIEW` and may require `HALT`
- privacy, billing, dispatch, or client-harm risk blocks unsafe testing
- unresolved duplicate-domain ownership blocks publication
- publication never authorizes implementation

Client reporting must include coverage, numeric confidence, defensible range, tested paths, material limitations, review state, and implementation authorization state.

## 13. DecisionLedger requirements

Each conversion result must retain:

```yaml
category_key: conversion
category_sheet_version: "0.2"
criterion_inventory_version: "criteria-library-v0.2"
regression_fixture: scoring/examples/conversion-worked-example.md
score_run_id: OI-SCORE-YYYY-NNN
applicable_criteria: []
scored_criteria: []
unknown_criteria: []
blocked_criteria: []
not_applicable_criteria: []
score_type: official|observed_indicator|range|null
observed_indicator: null
score_range: [null, null]
coverage_percent: null
confidence_index: null
confidence_band: high|medium|low|unknown
publication_state: official|provisional|range_only|blocked
material_unknowns: []
tested_conversion_paths: []
form_receipt_verified: false
confirmation_verified: false
source_capture_verified: false
validation_required: false
duplicate_check_passed: false
finding_refs: []
recommendation_refs: []
primary_package: null
dependent_packages: []
roadmap_phase: null
implementation_authorized: false
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

Evidence records must distinguish public observation, safe test result, internal record, client assertion, and evaluator interpretation.

## 14. Validation messages

| Code | Blocking condition | Required correction |
|---|---|---|
| `CAT-CONVERSION-SCOPE-001` | Minimum page or path coverage not met | Complete required desktop, mobile, service-page, and inquiry-path review |
| `CAT-CONVERSION-EVID-001` | Selected anchor exceeds evidence | Add direct test or record evidence, or reduce the anchor |
| `CAT-CONVERSION-MAP-001` | Criterion is missing, duplicated, or mapped outside `conversion` | Repair criterion inventory and ownership |
| `CAT-CONVERSION-DUP-001` | Capture, routing, attribution, or reporting signal is scored twice | Assign one primary owner and record dependencies |
| `CAT-CONVERSION-UNKNOWN-001` | High-materiality form, confirmation, or source-capture unknown remains unresolved | Obtain evidence or publish `range_only`/`blocked` |
| `CAT-CONVERSION-WEIGHT-001` | Applicable weights do not reconcile to 100% | Recalculate after approved applicability decisions |
| `CAT-CONVERSION-CONF-001` | Confidence index is missing, nonnumeric, or inconsistent with criterion factors | Recalculate from scored criterion confidence factors |
| `CAT-CONVERSION-BOUNDS-001` | Published bounds omit confidence uncertainty or unresolved applicable weight | Recalculate all criterion bounds and retain unknown weight |
| `CAT-CONVERSION-PUB-001` | Publication state conflicts with material unknowns or defensible range | Downgrade to `range_only` or `blocked` |
| `CAT-CONVERSION-ROUTE-001` | Recommendation lacks a valid finding, one primary package, or roadmap phase | Repair evidence-first routing |
| `CAT-CONVERSION-AUTH-001` | Publication or package routing is treated as implementation authorization | Set authorization to false until separately approved |
| `CAT-CONVERSION-GATE-001` | Safe testing boundary is violated or a primary path is broken | Stop testing, document risk, and route to `REVIEW` or `HALT` |
| `CAT-CONVERSION-LEDGER-001` | Required traceability is missing | Complete evidence, decision, routing, and approval records |

## 15. Canonical worked scoring example

The controlled regression fixture is:

```text
scoring/examples/conversion-worked-example.md
```

The fixture evaluates all 14 applicable criteria and produces:

```text
Observed indicator = 67.31
Coverage = 92.86%
Confidence index = 0.9231
Defensible range = 58.93–73.21
Publication state = range_only
Review state = REVIEW
Implementation authorized = false
```

`OI-CONV-014` remains unknown because form configuration, CRM source fields, and UTM retention evidence are unavailable. The unresolved applicable weight contributes `0–100` to the category range and cannot be removed or scored as zero.

The verified intake-context weakness routes through `OI-FIND-CONV-005` to exactly one primary package, `OI-PKG-WEB-001`, in `Phase 1 — Quick Wins`. The attribution unknown routes to validation and does not independently create an Analytics, Automation, CRM, or Dashboard package commitment.

Example executive-safe statement:

> The reviewed conversion paths provide a functional baseline through visible estimate actions, working phone and form routes, and a verified confirmation state. The estimate form captures basic contact information but leaves material project-context gaps, while lead-source retention could not be verified. The current evidence therefore supports a range of 58.93–73.21 rather than a single official Conversion Infrastructure score. Validation and reviewed scope approval are required before implementation is authorized.

## 16. Completion checklist

- [ ] All 14 `OI-CONV-*` criteria are mapped exactly once
- [ ] Category boundary is explicit
- [ ] Required evidence and safe test actions are documented
- [ ] Minimum desktop, mobile, service-page, and inquiry-path scope is complete or limitation is recorded
- [ ] Applicability decisions are recorded
- [ ] Equal weights reconcile to 100%
- [ ] Anchor decisions use observable conditions
- [ ] Confidence index is numeric and separate from maturity
- [ ] Defensible bounds include confidence uncertainty and unresolved applicable weight
- [ ] Unknown and blocked records include reason, owner, next action, and publication effect
- [ ] Duplicate checks pass across website, messaging, trust, automation, and analytics
- [ ] Findings route through approved identifiers
- [ ] Every recommendation has exactly one primary package and a roadmap phase
- [ ] Publication state matches evidence, material unknowns, and range
- [ ] Implementation authorization is recorded separately and defaults to false
- [ ] Regression fixture recalculates exactly
- [ ] DecisionLedger record is complete
- [ ] Reviewer approval is recorded
