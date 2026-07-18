# Local SEO Worked Scoring Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `seo`  
Default Operator Score weight: 15%  
Fixture key: `OI-EX-SCORE-SEO-001`  
Status: Commercial v1.0 validation fixture

## 1. Purpose

Provide a deterministic Local SEO category calculation that validates criterion maturity, evidence coverage, numeric confidence, confidence-adjusted bounds, controlled unknown handling, publication state, finding admission, package ownership, roadmap routing, implementation authorization, and DecisionLedger traceability.

This is a synthetic methodology fixture. It must not be presented as a real client assessment or reused as evidence for another score run.

## 2. Commercial v1.0 connection and intended use

Commercial v1.0 requires qualified evaluators using the same evidence to produce materially similar results. This fixture supplies expected values for:

- all 16 `OI-SEO-*` criterion records
- equal internal criterion weighting
- observed category score
- applicable, scored, and unresolved weight
- evidence coverage
- confidence index and band
- confidence-adjusted lower and upper bounds
- provisional publication with a material citation unknown
- evidence-backed finding and package routing
- separate implementation authorization
- regression and quality-control review

Use this fixture to test `scoring/category-sheets/seo.md`, calculator implementations, report generation, reviewer consistency, and future scoring-method changes.

## 3. Synthetic scenario and evidence scope

Cedar Ridge Exterior Services is a synthetic local contractor with four core services, one owner-confirmed priority service, a public service-area website, a project gallery, and a functioning sitemap.

The controlled review includes:

- the approved core-service and priority-service inventory, including current delivery-fit confirmation
- the complete public URL inventory
- homepage, four core service pages, contact page, and service-area page
- title, meta-description, H1, URL, and internal-link inventories
- robots, response, canonical, noindex, sitemap, and search checks
- twelve representative images across priority pages
- project and gallery content
- rendered structured data on homepage and representative page types
- five public citation sources
- a three-competitor service-page comparison

The approved business identity record required to validate citation consistency was requested but not provided. Citation maturity therefore remains unknown. Search rankings, traffic, lead volume, revenue, and ROI are outside this fixture.

## 4. Governance rules

1. Unknown is not score `0`.
2. All 16 criteria remain applicable; unresolved citation weight is retained.
3. Confidence affects bounds and publication treatment, not maturity anchors.
4. Sitemap presence alone does not establish indexability.
5. Search, traffic, lead, ranking, and revenue claims require dated attributable evidence and are not inferred here.
6. One operational condition may have only one weighted category owner.
7. A weak score does not automatically create a finding or recommendation.
8. Every routed recommendation requires evidence, interpretation, business impact, confidence, priority, one primary package, roadmap phase, and DecisionLedger traceability.
9. Publication does not authorize implementation.
10. The fixture must recalculate exactly before registry admission.

## 5. Criterion results

All 16 SEO criteria are applicable and equally weighted at `6.25%` each.

| Criterion | State | Score | Confidence | Factor | Defensible bound | Evidence reference |
|---|---|---:|---|---:|---|---|
| `OI-SEO-001` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-SEO-001` approved core-service inventory matched to the complete public URL inventory |
| `OI-SEO-002` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-SEO-002` owner-confirmed priority service, URL comparison, and three-competitor page sample |
| `OI-SEO-003` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-SEO-003` title inventory for homepage, service, service-area, and contact pages |
| `OI-SEO-004` | scored | 25 | high | 1.00 | 25–25 | `OI-EVID-SEO-004` crawl showing missing or duplicated descriptions on multiple sampled pages |
| `OI-SEO-005` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-SEO-005` rendered H1 inventory aligned to sampled page intent |
| `OI-SEO-006` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-SEO-006` internal-link crawl; priority pages linked but project support remains incomplete |
| `OI-SEO-007` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-SEO-007` approved service-area record compared with public location copy |
| `OI-SEO-008` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-SEO-008` buyer-question review across four core service pages |
| `OI-SEO-009` | scored | 25 | medium | 0.75 | 12.5–37.5 | `OI-EVID-SEO-009` rendered sample of twelve priority-page images and alt attributes |
| `OI-SEO-010` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-SEO-010` complete public URL inventory with clean descriptive paths |
| `OI-SEO-011` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-SEO-011` robots, response, noindex, canonical, and search checks on priority pages |
| `OI-SEO-012` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-SEO-012` XML sitemap reconciled to intended indexable URL inventory |
| `OI-SEO-013` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-SEO-013` content inventory and owner-confirmed service-priority map |
| `OI-SEO-014` | scored | 25 | high | 1.00 | 25–25 | `OI-EVID-SEO-014` gallery review confirming completed-work images lack descriptive indexable project pages |
| `OI-SEO-015` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-SEO-015` five-source citation capture; approved business identity record requested but not provided |
| `OI-SEO-016` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-SEO-016` rendered LocalBusiness and breadcrumb validation; service markup coverage incomplete |

Control-state summary:

```yaml
applicable_criteria: 16
scored_criteria: 15
unknown_criteria:
  - OI-SEO-015
blocked_criteria: []
not_applicable_criteria: []
applicable_weight_percent: 100.00
scored_weight_percent: 93.75
unknown_weight_percent: 6.25
blocked_weight_percent: 0.00
excluded_weight_percent: 0.00
```

No criterion is blocked or structurally not applicable in this scenario. `OI-SEO-015` is unknown because the citation sample cannot be reconciled without an approved business identity record.

## 6. Observed maturity calculation

```text
Known maturity total = 800
Scored criterion count = 15
Observed Category Score = 800 ÷ 15 = 53.333333...
Displayed provisional score = 53.33
```

The unknown criterion is excluded from the observed point-score denominator because no maturity anchor is defensible. It remains inside applicable weight for coverage and range calculations.

## 7. Evidence coverage

```text
Scored applicable criteria = 15
Total applicable criteria = 16
Coverage = 15 ÷ 16 × 100 = 93.75%
Displayed coverage = 93.75%
```

Coverage supports provisional reporting. It does not resolve citation consistency or authorize an official category score.

## 8. Confidence index

Ten scored criteria have high confidence and five have medium confidence.

```text
Confidence factor total = (10 × 1.00) + (5 × 0.75) = 13.75
Category Confidence Index = 13.75 ÷ 15 = 0.916666...
Displayed confidence index = 0.9167
Confidence band = high
```

The confidence index applies only to scored evidence. It does not assign maturity to `OI-SEO-015`.

## 9. Confidence-adjusted bounds

Medium-confidence criteria use `score ± 12.5`. High-confidence criteria retain their observed anchors. The unknown criterion contributes `0–100`.

```text
Known lower-bound total = 800 - (5 × 12.5) = 737.5
Known upper-bound total = 800 + (5 × 12.5) = 862.5
Unknown lower-bound total = 0
Unknown upper-bound total = 100

Category Lower Bound = (737.5 + 0) ÷ 16 = 46.09375
Category Upper Bound = (862.5 + 100) ÷ 16 = 60.15625
Displayed defensible range = 46.09–60.16
```

This is an evidence boundary, not a statistical confidence interval or outcome prediction.

## 10. Unknown validation and publication decision

```yaml
criterion_id: OI-SEO-015
state: unknown
reason_code: not_provided
materiality: medium
requested_evidence:
  - approved legal business name, address, phone, and website record
  - confirmation that the record is current and authorized for citation comparison
validation_owner: client_business_owner
due_state: before_official_category_publication
next_action: provide_approved_business_identity_record
score_effect: expands_category_range
finding_effect: no_citation_finding_until_validated
recommendation_effect: citation_remediation_scope_not_authorized
validation_ref: OI-VAL-2026-0901
```

Governed publication output:

```yaml
score_value: 53.33
score_type: provisional_point_with_range
observed_indicator: 53.33
score_range: [46.09, 60.16]
coverage_percent: 93.75
confidence_index: 0.9167
confidence_band: high
publication_state: provisional
material_unknowns:
  - OI-SEO-015 citation consistency
review_state: REVIEW
```

A qualified point score is supportable because required public and technical surfaces were inspected, evidence coverage exceeds 80%, and the unresolved condition is confined to a material citation subset. Official publication requires the approved business identity record and recalculation.

## 11. Finding and recommendation routing

The directly observed priority-service architecture condition supports one governed finding:

```yaml
finding_id: OI-FIND-SEO-002
criterion_owner: OI-SEO-002
observation: "One owner-confirmed priority service is described only inside a broad services page and has no dedicated public URL."
interpretation: "The current architecture provides less search and buyer context for that priority service than a dedicated page would."
business_impact: "The priority service may receive weaker visibility and buyer relevance than dedicated service coverage would provide."
confidence: medium
priority: medium
limitations:
  - "No ranking, traffic, lead-volume, conversion, revenue, market-share, or ROI effect is inferred."
ledger_ref: OI-DL-2026-014
```

The citation unknown creates a validation requirement and does not create a negative finding or package route.

```yaml
primary_package: OI-PKG-SEO-001
primary_package_name: Local SEO Expansion Pack
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
prerequisites:
  service_currently_offered: true
  priority_relevance_confirmed: true
  service_area_validated: true
  page_intent_and_evidence_gap_defined: true
  capacity_constraints_recorded: true
implementation_authorized: false
```

Exactly one primary package is assigned to the verified root condition. Routing eligibility passes. Implementation remains unauthorized until package scope, content ownership, acceptance criteria, and client authorization are recorded.

## 12. DecisionLedger record

```yaml
fixture_path: scoring/examples/seo-worked-example.md
fixture_version: "0.1"
category_key: seo
category_sheet_version: "0.1"
criterion_inventory_version: criteria-library-v0.2
score_run_id: OI-SCORE-2026-004
criterion_ids:
  - OI-SEO-001
  - OI-SEO-002
  - OI-SEO-003
  - OI-SEO-004
  - OI-SEO-005
  - OI-SEO-006
  - OI-SEO-007
  - OI-SEO-008
  - OI-SEO-009
  - OI-SEO-010
  - OI-SEO-011
  - OI-SEO-012
  - OI-SEO-013
  - OI-SEO-014
  - OI-SEO-015
  - OI-SEO-016
evidence_refs:
  - OI-EVID-SEO-001
  - OI-EVID-SEO-002
  - OI-EVID-SEO-003
  - OI-EVID-SEO-004
  - OI-EVID-SEO-005
  - OI-EVID-SEO-006
  - OI-EVID-SEO-007
  - OI-EVID-SEO-008
  - OI-EVID-SEO-009
  - OI-EVID-SEO-010
  - OI-EVID-SEO-011
  - OI-EVID-SEO-012
  - OI-EVID-SEO-013
  - OI-EVID-SEO-014
  - OI-EVID-SEO-015
  - OI-EVID-SEO-016
applicable_criteria: 16
scored_criteria:
  - OI-SEO-001
  - OI-SEO-002
  - OI-SEO-003
  - OI-SEO-004
  - OI-SEO-005
  - OI-SEO-006
  - OI-SEO-007
  - OI-SEO-008
  - OI-SEO-009
  - OI-SEO-010
  - OI-SEO-011
  - OI-SEO-012
  - OI-SEO-013
  - OI-SEO-014
  - OI-SEO-016
unknown_criteria:
  - OI-SEO-015
blocked_criteria: []
not_applicable_criteria: []
applicable_weight_percent: 100.00
scored_weight_percent: 93.75
observed_indicator: 53.33
coverage_percent: 93.75
confidence_index: 0.9167
score_range: [46.09, 60.16]
publication_state: provisional
validation_refs:
  - OI-VAL-2026-0901
finding_ids:
  - OI-FIND-SEO-002
primary_package: OI-PKG-SEO-001
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
routing_prerequisites_complete: true
duplicate_check_passed: true
unsupported_claim_check_passed: true
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
ledger_ref: OI-DL-2026-014
```

## 13. Executive-safe statement

> The reviewed site provides a functional local-search baseline, including dedicated core-service pages, clean URLs, indexable priority pages, and a sitemap aligned to the public inventory. One confirmed priority service remains consolidated inside a broad page, while metadata, internal linking, image context, project-page depth, and structured-data coverage remain uneven. Citation consistency could not be validated without an approved business identity record. The current evidence supports a provisional Local SEO score of 53.33 with a defensible range of 46.09–60.16. Validation and reviewed scope approval are required before official publication or implementation.

## 14. Usage instructions

1. Recalculate every criterion, total, factor, bound, and publication output before changing the governing SEO sheet.
2. Preserve all 16 criteria and equal weighting unless an approved methodology change supersedes this fixture.
3. Treat `OI-SEO-015` as unknown until the approved identity record is available.
4. Route the unknown to validation, not to a negative finding or automatic package.
5. Preserve `OI-FIND-SEO-002` as the only fixture recommendation root.
6. Keep `OI-PKG-SEO-001` as the single primary package.
7. Record any changed evidence, applicability, confidence, score, package, or publication state as a new score-run version.
8. Do not copy synthetic findings, scores, or conclusions into a real assessment.

## 15. Regression assertions

This fixture passes only when:

- observed score equals `53.333333...` before display rounding
- coverage equals `93.75%`
- confidence index equals `0.916666...` before display rounding
- known lower-bound total equals `737.5`
- known upper-bound total equals `862.5`
- defensible bounds equal `46.09375–60.15625` before display rounding
- the SEO category retains its canonical 15% Operator Score weight
- all 16 criterion records remain distinct
- applicable weight equals `100%`
- scored weight equals `93.75%`
- unknown weight equals `6.25%`
- unknown, blocked, and not-applicable states remain explicit
- `OI-SEO-015` remains unscored and contributes `0–100` to the range
- confidence does not alter maturity anchors
- publication remains `provisional` until citation identity is validated
- `OI-SEO-015` routes to validation rather than an unsupported negative finding
- `OI-FIND-SEO-002` routes to exactly one primary package
- package routing does not authorize implementation
- publication and implementation authorization remain separate
- duplicate checks preserve website, messaging, GBP, trust, analytics, and competitive ownership boundaries
- all material outputs retain DecisionLedger traceability
- client language avoids unsupported ranking, traffic, lead, conversion, revenue, market-share, and ROI claims

## 16. Completion check

- [x] Purpose, stage, folder alignment, intended use, and v1.0 connection are explicit
- [x] All 16 criteria are mapped exactly once
- [x] Evidence scope meets the synthetic fixture design
- [x] Unknown, blocked, and not-applicable treatment is visible
- [x] Applicable and scored weights reconcile
- [x] Observed score recalculates
- [x] Confidence index is numeric and separate from maturity
- [x] Confidence-adjusted bounds recalculate
- [x] Publication state matches coverage and unknown materiality
- [x] Finding identity and package route match governed authorities
- [x] One primary package and roadmap phase are recorded
- [x] Implementation authorization is separate and false
- [x] DecisionLedger fixture is complete
- [x] Executive language is evidence-safe
- [x] Regression assertions are explicit
- [x] Category-sheet reconciliation completed
- [x] Fixture registry admission completed
- [ ] Reviewer approval recorded
