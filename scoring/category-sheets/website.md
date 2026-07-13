# Website Structure and UX Category Scoring Sheet

Version: v0.2 scoring execution contract  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `website`  
Default Operator Score weight: 10%  
Status: Reconciled for commercial v1.0

## 1. Purpose and category boundary

This sheet governs scoring for website structure and user experience. It measures whether buyers have a usable, accessible, and logically organized path to understand the business, discover services, navigate key pages, and reach contact options.

Included:

- page and navigation structure
- service-page organization
- mobile usability
- phone and contact-path accessibility
- page hierarchy and scanning support
- footer utility
- functional links and buyer paths

Excluded from independent scoring:

- message or offer strength
- CTA persuasion and lead-capture workflow
- search visibility or technical SEO
- trust-asset quality
- follow-up automation
- analytics instrumentation
- competitive performance

Cross-domain effects must be recorded as dependencies, not duplicate scores.

## 2. Criterion inventory

| Criterion ID | Observable condition | Primary evidence |
|---|---|---|
| `OI-WEB-001` | Homepage communicates the business type immediately | Desktop and mobile above-fold screenshots |
| `OI-WEB-002` | Homepage communicates the service area | Hero, footer, contact page, service-area copy |
| `OI-WEB-003` | Navigation is simple and buyer-oriented | Desktop and mobile menu tests |
| `OI-WEB-004` | Services are organized into clear pages | URL inventory, menu, service-page inventory |
| `OI-WEB-005` | Website works cleanly on mobile | Mobile screenshots and interaction tests |
| `OI-WEB-006` | Phone number is visible and usable | Header, footer, contact page, tap-to-call test |
| `OI-WEB-007` | Contact or estimate page is easy to reach | Navigation and path testing |
| `OI-WEB-008` | Website has a logical page hierarchy | Sitemap, URL inventory, internal links |
| `OI-WEB-009` | Visual hierarchy supports scanning | Key-page screenshots and heading review |
| `OI-WEB-010` | Page content supports buyer decision-making | Homepage and service-page review |
| `OI-WEB-011` | Website avoids template-generic presentation | Homepage and representative competitor comparison |
| `OI-WEB-012` | Footer supports trust and navigation | Footer screenshot and link test |

Each criterion has one weighted owner: `website`.

## 3. Required evidence and scope

Primary evidence:

- homepage desktop and mobile screenshots
- desktop and mobile navigation tests
- URL and core service-page inventory
- contact or estimate path test
- phone-link test
- footer review
- broken-link or dead-path observations

Supporting evidence may include sitemap, CMS inventory, browser notes, competitor screenshots, client-confirmed service priorities, and hosting or domain-access records.

A category result is admissible only when the evaluator reviews, where present:

1. homepage on desktop and mobile
2. desktop and mobile navigation
3. contact or estimate page
4. at least two core service pages, or all when fewer than two exist
5. footer
6. phone and primary contact paths
7. service-page and URL inventory
8. one complete homepage-to-inquiry path

A single-page review cannot be generalized to the category. Scope exceptions require a documented limitation and may force `provisional`, `range_only`, or `blocked` publication.

## 4. Applicability and weighting

All `OI-WEB-*` criteria are normally applicable when a public website exists.

Use `not_applicable` only when structural irrelevance is documented and approved. Missing access, incomplete tests, uncertain functionality, or an unfavorable result do not justify `not_applicable`.

All applicable criteria use equal weighting:

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before recalculation. Unequal weighting requires a versioned methodology change under `scoring/weight-rules.md`.

## 5. Maturity anchors

Use only `0`, `25`, `50`, `75`, and `100`. Interpolation is prohibited.

| Anchor | Website interpretation |
|---:|---|
| 0 | Required structure or buyer path is absent, broken, inaccessible, or materially misleading within tested scope. |
| 25 | A limited baseline exists, but material friction, omission, or inconsistency is directly observed. |
| 50 | Core tasks are possible, but recurring structural, usability, or decision-support gaps remain. |
| 75 | Major buyer tasks work consistently across tested pages and devices. |
| 100 | Structure is complete, tested, maintained, governed, and aligned to documented buyer paths and service priorities. |

Criterion evidence must support the selected anchor directly. Evaluator preference, unverified client claims, automated results without manual confirmation, or desktop-only evidence used to infer mobile behavior cannot support a point score alone.

## 6. Confidence and uncertainty

Approved confidence factors:

```text
high    = 1.00
medium  = 0.75
low     = 0.50
unknown = 0.00
```

Confidence remains separate from maturity.

```text
Confidence Index = Sum(confidence factors for scored criteria) ÷ Scored Criterion Count
```

Use criterion-level defensible bounds:

- high confidence: observed anchor retained
- medium confidence: observed anchor ±12.5, bounded to 0–100
- low confidence: observed anchor ±25, bounded to 0–100
- unknown or blocked: 0–100 unless a narrower approved bound is evidenced

```text
Category Lower Bound = Sum(criterion lower bounds) ÷ Applicable Criterion Count
Category Upper Bound = Sum(criterion upper bounds) ÷ Applicable Criterion Count
```

These bounds express evidence uncertainty and unresolved scope. They are not statistical confidence intervals.

## 7. Unknown, blocked, and not-applicable treatment

Common unknowns include untested mobile behavior, unverified contact destinations, incomplete service-page inventory, unconfirmed priority services, unavailable competitor comparison, and unavailable CMS ownership evidence.

Common blocks include denied site access, unsafe form or phone testing, malware or privacy risk, and conflicting site versions.

Every material unknown or block must record:

- reason code
- affected criterion
- evidence or test required
- validation owner
- materiality
- next action
- publication effect

Unknown is not score `0`. Confirmed public absence may support `0` only after the required search or test is completed.

## 8. Duplicate-signal boundaries

| Overlap | Website owns | Adjacent category owns |
|---|---|---|
| Messaging | Placement, structure, accessibility | Strength, specificity, differentiation, offer quality |
| Conversion | Ability to reach inquiry paths | CTA effectiveness, form design, confirmation, routing |
| SEO | Page and navigation architecture | Intent, indexability, metadata, local relevance, visibility |
| Trust | Placement and accessibility of proof | Quality and credibility of proof assets |
| Automation | Public path to contact | Lead handling, assignment, acknowledgement, follow-up |
| Analytics | Presence of usable buyer paths | Instrumentation, attribution, reporting, decision use |
| Competitive | Site-specific structure and usability | Relative market position and benchmark interpretation |

Duplicate scoring is prohibited.

## 9. Finding and recommendation routing

A weak category result does not automatically create a finding or package recommendation.

Eligible website finding domain:

```text
OI-FIND-WEB-*
```

Common governed routing:

| Evidence-backed condition | Primary route | Package |
|---|---|---|
| Navigation, mobile usability, phone visibility, or contact access is weak | Website finding | `OI-PKG-WEB-001` |
| Core service-page architecture is absent | SEO finding primary; website dependency | `OI-PKG-SEO-001` |
| Proof is unavailable or poorly integrated | Trust finding primary | `OI-PKG-TRUST-001` |
| Form exists but lead handling is weak | Automation or conversion finding primary | `OI-PKG-CRM-001` |
| Outcomes cannot be measured | Analytics finding primary | `OI-PKG-DASH-001` |
| Website ownership or functionality is unverified | Validation record | No package until validation passes |

Routing requires observation, evidence, interpretation, buyer impact, confidence, priority, governed finding ID, one primary package, roadmap phase, and DecisionLedger traceability.

Do not recommend a full redesign when a narrower evidence-backed correction is sufficient. Package routing does not authorize implementation.

## 10. Publication controls

Allowed publication states:

- `official`
- `provisional`
- `range_only`
- `blocked`

Controls:

- no `official` result without desktop, mobile, navigation, and contact-path testing
- no untested functionality may be represented as confirmed failure
- unknown and blocked criteria retain applicable weight
- unresolved material unknowns force `range_only` when they can materially change interpretation
- duplicate-domain mapping failures block publication
- `observed_indicator` cannot be represented as an official score when `publication_state: range_only`
- publication does not imply implementation authorization

Client reporting must include coverage, numeric confidence, defensible range, publication state, and material limitations.

## 11. DecisionLedger contract

```yaml
category_key: website
category_sheet_version: "0.2"
criterion_inventory_version: "criteria-library-v0.2"
score_run_id: OI-SCORE-YYYY-NNN
required_scope_completed: false
desktop_tested: false
mobile_tested: false
navigation_tested: false
contact_path_tested: false
applicable_criteria: []
scored_criteria: []
unknown_criteria: []
blocked_criteria: []
not_applicable_criteria: []
observed_indicator: null
coverage_percent: null
confidence_index: null
confidence_band: null
score_range: [null, null]
publication_state: range_only
material_unknowns: []
duplicate_check_passed: false
finding_ids: []
validation_required: false
validation_criteria: []
primary_package: null
dependent_packages: []
roadmap_phase: null
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 12. Validation messages

Blocking:

- `CAT-WEB-SCOPE-001`: minimum page and device scope is incomplete
- `CAT-WEB-EVID-001`: selected maturity anchor lacks sufficient evidence
- `CAT-WEB-MAP-001`: criterion is missing, duplicated, or assigned to another weighted owner
- `CAT-WEB-DUP-001`: condition is duplicated in an adjacent category
- `CAT-WEB-WEIGHT-001`: applicable criterion weights do not total 100%
- `CAT-WEB-CONF-001`: confidence factor or index is missing or invalid
- `CAT-WEB-BOUND-001`: defensible bounds are missing, invalid, or nonreproducible
- `CAT-WEB-PUB-001`: publication state conflicts with coverage, bounds, or material unknowns
- `CAT-WEB-ROUTE-001`: finding or package routing is unsupported, duplicated, or lacks one primary package
- `CAT-WEB-AUTH-001`: implementation is represented as authorized without approval evidence
- `CAT-WEB-GATE-001`: access, safety, privacy, or buyer-path failure blocks scoring or publication
- `CAT-WEB-LEDGER-001`: required evidence or scoring trace is missing

Warnings:

- `CAT-WEB-UNKNOWN-001`: unresolved material website unknown affects reliability
- `CAT-WEB-MOBILE-001`: mobile scope is incomplete
- `CAT-WEB-FUNCTION-001`: visible functionality was not tested
- `CAT-WEB-COMP-001`: differentiation lacks sufficient comparison evidence

## 13. Canonical regression fixture

Controlled fixture: `scoring/examples/website-worked-example.md`

Verified result:

```yaml
observed_indicator: 50
coverage_percent: 91.67
confidence_index: 0.9091
confidence_band: high
score_range: [41.67, 58.33]
publication_state: range_only
material_unknowns:
  - OI-WEB-011
validation_required: true
validation_criteria:
  - OI-WEB-011
finding_ids:
  - OI-FIND-WEB-004
primary_package: OI-PKG-SEO-001
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
implementation_authorized: false
review_state: REVIEW
ledger_ref: OI-DL-2026-012
```

The unresolved competitor-comparison criterion routes to validation and does not create a negative finding. The verified service-page architecture weakness supports `OI-FIND-WEB-004` and exactly one primary package. The observed indicator must not be published as an official score.

## 14. Executive-safe statement

> The reviewed website provides functional navigation, contact access, and a usable baseline across desktop and mobile. Core service-page architecture remains limited, and representative competitor comparison was not completed. The current evidence therefore supports a range of 41.67–58.33 rather than a single official Website Structure and UX score. Validation and reviewed scope approval are required before implementation is authorized.

## 15. Completion checklist

Before approval, confirm:

- all criteria use approved states and anchors
- required page, device, navigation, and contact-path scope is complete or limited explicitly
- confidence and bounds are reproducible from criterion-level evidence
- unknown and blocked criteria retain applicable weight
- website and adjacent-domain conditions are not double counted
- findings use governed IDs
- exactly one primary package is assigned per validated recommendation
- roadmap phase and dependencies are recorded
- `implementation_authorized` is explicit and defaults to `false`
- DecisionLedger fields are complete
- publication state matches evidence, coverage, confidence, bounds, and material unknowns
- client language avoids unsupported redesign, traffic, ranking, lead, conversion, revenue, ROI, safety, compliance, or competitor-performance claims
