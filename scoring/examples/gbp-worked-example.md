# Google Business Profile Worked Scoring Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `gbp`  
Default Operator Score weight: 10%  
Fixture key: `OI-EX-SCORE-GBP-001`  
Status: Candidate regression fixture for commercial v1.0

## 1. Purpose

Provide a reproducible Google Business Profile category calculation that validates maturity scoring, evidence coverage, numeric confidence, uncertainty bounds, competitor-context unknown handling, governed finding routing, package ownership, roadmap phase, publication state, implementation authorization, and DecisionLedger traceability.

This synthetic fixture must not be represented as a real client assessment.

## 2. Commercial v1.0 connection and intended use

Use this fixture to validate the 12-criterion GBP category sheet, calculator behavior, reviewer consistency, report outputs, and future methodology changes. It defines expected values for:

- criterion state, anchor, confidence, factor, bound, and evidence
- applicable, scored, unknown, blocked, and excluded weight
- observed score, coverage, confidence index, and defensible range
- provisional publication with an unresolved peer-comparison criterion
- evidence-backed finding admission and package routing
- separate implementation authorization
- DecisionLedger and regression controls

## 3. Synthetic scenario and evidence scope

Cedar Ridge Exterior Services has one verified, findable Google Business Profile with accurate core identity, a suitable primary category, a current service list, active recent reviews, consistent owner responses, and a website link aligned to the business.

The controlled review includes:

- branded and category-location searches
- canonical profile and duplicate-profile checks
- primary and all visible secondary categories
- complete services and description
- twelve recent profile photos
- current review count and rating
- the most recent twelve reviews across a six-month lookback
- the most recent twelve owner-response opportunities
- all visible Q&A
- six months of posts
- major GBP services mapped to website pages
- three candidate local peer profiles

The three peer profiles cannot yet be treated as a governed comparison set because service mix, operating model, and market comparability remain unresolved. No conclusion about competitive review strength is authorized.

## 4. Governance rules

1. Unknown is not score `0`.
2. All 12 criteria remain applicable; unresolved peer-comparison weight is retained.
3. Confidence affects bounds and publication treatment, not maturity anchors.
4. Profile identity, categories, services, service area, hours, and links must be verified before package routing.
5. Review gating, artificial reviews, false locations, inaccurate categories, and unsupported service claims are prohibited.
6. Competitor counts require a named, controlled, comparable peer set.
7. GBP evidence does not duplicate Trust, SEO, Website, Conversion, or Competitive scoring.
8. Findings require direct evidence and cannot be created from an unknown criterion.
9. Every recommendation requires one primary package, roadmap phase, prerequisites, and DecisionLedger record.
10. Publication does not authorize implementation.

## 5. Criterion results

All 12 GBP criteria are applicable and equally weighted at `8.333333%` each.

| Criterion | State | Score | Confidence | Factor | Defensible bound | Evidence reference |
|---|---|---:|---|---:|---|---|
| `OI-GBP-001` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-GBP-001` branded and category-location searches, canonical profile URL, and duplicate check |
| `OI-GBP-002` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-GBP-002` primary category matched to the approved core-service inventory |
| `OI-GBP-003` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-GBP-003` secondary-category inventory; one service relationship requires owner confirmation |
| `OI-GBP-004` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-GBP-004` full GBP service list compared with approved current services |
| `OI-GBP-005` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-GBP-005` current description compared with approved business facts and service area |
| `OI-GBP-006` | scored | 25 | medium | 0.75 | 12.5–37.5 | `OI-EVID-GBP-006` twelve-photo sample; recent owner-controlled project proof is limited |
| `OI-GBP-007` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-GBP-007` three candidate peer profiles captured; operating-model comparability unresolved |
| `OI-GBP-008` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-GBP-008` most recent twelve reviews and six-month date history |
| `OI-GBP-009` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-GBP-009` response review across the most recent twelve reviews |
| `OI-GBP-010` | scored | 25 | medium | 0.75 | 12.5–37.5 | `OI-EVID-GBP-010` complete visible Q&A review; ownership cadence not documented |
| `OI-GBP-011` | scored | 25 | high | 1.00 | 25–25 | `OI-EVID-GBP-011` six-month post history confirming extended inactivity |
| `OI-GBP-012` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-GBP-012` full GBP-to-website major-service alignment map |

```yaml
applicable_criteria: 12
scored_criteria: 11
unknown_criteria:
  - OI-GBP-007
blocked_criteria: []
not_applicable_criteria: []
applicable_weight_percent: 100.00
scored_weight_percent: 91.6667
unknown_weight_percent: 8.3333
blocked_weight_percent: 0.00
excluded_weight_percent: 0.00
```

No criterion is blocked or structurally not applicable. `OI-GBP-007` is unknown because comparability has not been governed, not because the review count is confirmed weak.

## 6. Observed maturity calculation

```text
Known maturity total = 550
Scored criterion count = 11
Observed Category Score = 550 ÷ 11 = 50.0000
Displayed provisional score = 50.00
```

The unknown criterion remains inside applicable weight for coverage and range calculations.

## 7. Evidence coverage

```text
Scored applicable criteria = 11
Total applicable criteria = 12
Coverage = 11 ÷ 12 × 100 = 91.666666...
Displayed coverage = 91.67%
```

## 8. Confidence index

Eight scored criteria have high confidence and three have medium confidence.

```text
Confidence factor total = (8 × 1.00) + (3 × 0.75) = 10.25
Category Confidence Index = 10.25 ÷ 11 = 0.931818...
Displayed confidence index = 0.9318
Confidence band = high
```

High confidence applies only to the scored evidence and does not resolve `OI-GBP-007`.

## 9. Confidence-adjusted bounds

The three medium-confidence criteria use `score ± 12.5`. High-confidence criteria retain their anchors. The unknown criterion contributes `0–100`.

```text
Known lower-bound total = 550 - (3 × 12.5) = 512.5
Known upper-bound total = 550 + (3 × 12.5) = 587.5
Unknown lower-bound total = 0
Unknown upper-bound total = 100

Category Lower Bound = (512.5 + 0) ÷ 12 = 42.708333...
Category Upper Bound = (587.5 + 100) ÷ 12 = 57.291666...
Displayed defensible range = 42.71–57.29
```

The range is an evidence boundary, not a statistical confidence interval or outcome prediction.

## 10. Unknown validation and publication decision

```yaml
criterion_id: OI-GBP-007
state: unknown
reason_code: insufficient_sample
materiality: medium
requested_evidence:
  - named local peer set
  - service-mix and operating-model comparison
  - common geographic market
  - dated review-count captures
validation_owner: assessment_reviewer
due_state: before_official_category_publication
next_action: approve_or_replace_peer_set
score_effect: expands_category_range
finding_effect: no_review_count_finding_until_validated
recommendation_effect: no_review_generation_route_from_this_criterion
validation_ref: OI-VAL-2026-0902
```

```yaml
score_value: 50.00
score_type: provisional_point_with_range
observed_indicator: 50.00
score_range: [42.71, 57.29]
coverage_percent: 91.67
confidence_index: 0.9318
confidence_band: high
publication_state: provisional
material_unknowns:
  - OI-GBP-007 controlled peer comparison
review_state: REVIEW
```

A qualified point score is supportable because the live profile, identity, services, review history, response sample, Q&A, activity, and website alignment were inspected. Official publication requires a governed comparable peer set and recalculation.

## 11. Finding and recommendation routing

Six months of directly observed post history supports one governed finding:

```yaml
finding_id: OI-FIND-GBP-018
criterion_owner: OI-GBP-011
observation: "The reviewed profile contains no published posts or updates within the six-month review window."
interpretation: "The profile provides limited visible evidence of current activity or timely service relevance through its update surface."
business_impact: "Buyers may receive less current profile context about recent work, seasonal priorities, or service availability."
confidence: high
priority: medium
limitations:
  - "No ranking, visibility, traffic, lead, conversion, revenue, or ROI effect is inferred."
ledger_ref: OI-DL-2026-015
```

`OI-GBP-007` routes to validation only and does not justify `OI-FIND-GBP-012` or a Review Generation System recommendation.

```yaml
primary_package: OI-PKG-GBP-001
primary_package_name: Google Business Authority Pack
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
routing_prerequisites:
  profile_and_business_identity_verified: true
  ownership_or_access_limitations_explicit: true
  services_service_area_hours_and_links_accurate: true
  policy_safe_implementation_possible: true
implementation_authorized: false
```

Routing eligibility passes. Implementation remains unauthorized until scope, content ownership, cadence, acceptance criteria, and client approval are recorded.

## 12. DecisionLedger record

```yaml
fixture_path: scoring/examples/gbp-worked-example.md
fixture_version: "0.1"
category_key: gbp
category_sheet_version: "0.1"
criterion_inventory_version: criteria-library-v0.2
score_run_id: OI-SCORE-2026-005
criterion_ids:
  - OI-GBP-001
  - OI-GBP-002
  - OI-GBP-003
  - OI-GBP-004
  - OI-GBP-005
  - OI-GBP-006
  - OI-GBP-007
  - OI-GBP-008
  - OI-GBP-009
  - OI-GBP-010
  - OI-GBP-011
  - OI-GBP-012
evidence_refs:
  - OI-EVID-GBP-001
  - OI-EVID-GBP-002
  - OI-EVID-GBP-003
  - OI-EVID-GBP-004
  - OI-EVID-GBP-005
  - OI-EVID-GBP-006
  - OI-EVID-GBP-007
  - OI-EVID-GBP-008
  - OI-EVID-GBP-009
  - OI-EVID-GBP-010
  - OI-EVID-GBP-011
  - OI-EVID-GBP-012
applicable_criteria: 12
scored_criteria:
  - OI-GBP-001
  - OI-GBP-002
  - OI-GBP-003
  - OI-GBP-004
  - OI-GBP-005
  - OI-GBP-006
  - OI-GBP-008
  - OI-GBP-009
  - OI-GBP-010
  - OI-GBP-011
  - OI-GBP-012
unknown_criteria:
  - OI-GBP-007
blocked_criteria: []
not_applicable_criteria: []
applicable_weight_percent: 100.00
scored_weight_percent: 91.6667
observed_indicator: 50.00
coverage_percent: 91.67
confidence_index: 0.9318
score_range: [42.71, 57.29]
publication_state: provisional
validation_refs:
  - OI-VAL-2026-0902
finding_ids:
  - OI-FIND-GBP-018
primary_package: OI-PKG-GBP-001
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
routing_prerequisites_complete: true
duplicate_check_passed: true
unsupported_claim_check_passed: true
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
ledger_ref: OI-DL-2026-015
```

## 13. Executive-safe statement

> The reviewed Google Business Profile provides a functional local-discovery baseline with verified identity, suitable core categorization, current services, recent review activity, consistent owner responses, and an aligned website destination. Photo recency, Q&A ownership, and profile updates remain uneven. Review-count competitiveness could not be determined because a governed comparable peer set has not yet been approved. The current evidence supports a provisional GBP score of 50.00 with a defensible range of 42.71–57.29. Peer-set validation and reviewed scope approval are required before official publication or implementation.

## 14. Usage instructions

1. Recalculate all maturity, coverage, confidence, and range values before changing the governing GBP sheet.
2. Retain all 12 applicable criteria and unresolved peer-comparison weight.
3. Do not assign a score or finding to `OI-GBP-007` without an approved comparable peer set.
4. Preserve `OI-FIND-GBP-018` as the fixture recommendation root.
5. Keep `OI-PKG-GBP-001` as the single primary package.
6. Keep publication and implementation authorization separate.
7. Version any evidence, applicability, confidence, score, package, or publication change.
8. Do not reuse synthetic findings or scores in a real engagement.

## 15. Regression assertions

This fixture passes only when:

- observed score equals `50.0000`
- coverage equals `91.666666...%` before display rounding
- confidence index equals `0.931818...` before display rounding
- known lower-bound total equals `512.5`
- known upper-bound total equals `587.5`
- defensible bounds equal `42.708333...–57.291666...`
- the GBP category retains its canonical 10% Operator Score weight
- all 12 criterion records remain distinct
- applicable weight equals `100%`
- scored weight equals `91.6667%`
- unknown weight equals `8.3333%`
- unknown, blocked, and not-applicable states remain explicit
- `OI-GBP-007` remains unscored and contributes `0–100` to the range
- confidence does not modify maturity anchors
- publication remains `provisional` until the peer set is governed
- the peer-set unknown routes to validation rather than a negative finding
- `OI-FIND-GBP-018` routes to exactly one primary package
- package routing does not authorize implementation
- duplicate checks preserve Trust, SEO, Website, Conversion, and Competitive ownership
- client language avoids unsupported ranking, traffic, lead, conversion, revenue, and ROI claims

## 16. Completion check

- [x] Purpose, stage, folder alignment, usage, governance, and v1.0 connection are explicit
- [x] All 12 criteria are mapped exactly once
- [x] Applicable and scored weights reconcile
- [x] Unknown, blocked, and not-applicable treatment is visible
- [x] Observed score, coverage, confidence, and bounds recalculate
- [x] Publication matches coverage and unknown materiality
- [x] Finding and package routes match governed authorities
- [x] Implementation authorization is separate and false
- [x] DecisionLedger traceability is complete
- [x] Executive language is evidence-safe
- [ ] Category-sheet reconciliation completed
- [ ] Fixture registry admission completed
- [ ] Reviewer approval recorded
