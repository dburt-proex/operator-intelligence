# Competitive Position Worked Scoring Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `competitive`  
Default Operator Score weight: 5%  
Fixture key: `OI-EX-SCORE-COMP-001`  
Status: Candidate regression fixture for commercial v1.0

## 1. Purpose

Provide a reproducible Competitive Position category calculation that validates comparable-set governance, maturity scoring, evidence coverage, numeric confidence, uncertainty bounds, controlled search and content unknowns, finding admission, package ownership, roadmap phase, publication state, implementation authorization, and DecisionLedger traceability.

This fixture is synthetic and must not be represented as a real market assessment.

## 2. Commercial v1.0 connection and intended use

Use this fixture to validate the 10-criterion Competitive category sheet, calculator behavior, evaluator consistency, report outputs, recommendation routing, and future methodology changes.

The expected deliverables are:

- one governed comparable set
- criterion state, anchor, confidence, factor, bound, and evidence
- applicable, scored, unknown, blocked, and excluded weight
- observed score, coverage, confidence index, and defensible range
- range-only publication for material comparison unknowns
- evidence-backed finding and one-primary-package routing
- separate implementation authorization
- complete DecisionLedger and regression assertions

## 3. Synthetic scenario and evidence scope

Cedar Ridge Exterior Services is compared with three named synthetic competitors that match verified service area, buyer type, and core-service model.

The controlled review includes:

- dated comparable-set matrix
- review profiles
- homepage and two priority-service pages per business
- project, gallery, testimonial, and case-study proof
- homepage and priority-service messaging
- five target local-search attempts
- primary mobile inquiry path for each business
- six months of visible content activity
- cross-surface professional consistency
- finding, package, roadmap, and DecisionLedger routing

The competitor set is valid. However, a governed local-search context could not be established for the target-search observations, and visible content volume could not be converted into buyer usefulness or strategic value without a confirmed content-priority model. Those two criteria remain unknown.

## 4. Governance rules

1. Competitors must match service, geography, buyer type, and operating model.
2. Unknown is not score `0`; unresolved weight remains applicable.
3. Search observations are dated snapshots and require query, location context, device or context, result type, and limitations.
4. Content volume does not establish usefulness, demand, engagement, or business impact.
5. Confidence affects bounds and publication, not maturity anchors.
6. Competitive evidence records relative context; primary operational weaknesses remain owned by their domain categories.
7. One condition cannot receive duplicate weighted penalties across Competitive, Trust, SEO, GBP, Website, Messaging, or Conversion.
8. No competitor revenue, market share, lead volume, conversion rate, software, or internal performance may be inferred.
9. Findings and packages require verified evidence, business fit, priority, and DecisionLedger traceability.
10. Publication does not authorize implementation.

## 5. Criterion results

All 10 criteria are applicable and equally weighted at `10%` each.

| Criterion | State | Score | Confidence | Factor | Defensible bound | Evidence reference |
|---|---|---:|---|---:|---|---|
| `OI-COMP-001` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-COMP-001` approved three-competitor matrix with service, geography, buyer type, URL, and date |
| `OI-COMP-002` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-COMP-002` dated review count, rating, recency, and response comparison |
| `OI-COMP-003` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-COMP-003` homepage and two priority-service page inventories per business |
| `OI-COMP-004` | scored | 25 | medium | 0.75 | 12.5–37.5 | `OI-EVID-COMP-004` project, gallery, testimonial, and case-study comparison; asset context incomplete |
| `OI-COMP-005` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-COMP-005` homepage and priority-service messaging comparison with proof review |
| `OI-COMP-006` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-COMP-006` five target-search attempts; governed local context could not be established |
| `OI-COMP-007` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-COMP-007` mobile CTA, phone, form, confirmation, and next-step comparison |
| `OI-COMP-008` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-COMP-008` six-month content inventories; buyer usefulness and strategic fit unresolved |
| `OI-COMP-009` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-COMP-009` cross-surface consistency, hierarchy, business-detail, and proof comparison |
| `OI-COMP-010` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-COMP-010` governed finding, package, roadmap, and DecisionLedger review |

```yaml
applicable_criteria: 10
scored_criteria: 8
unknown_criteria:
  - OI-COMP-006
  - OI-COMP-008
blocked_criteria: []
not_applicable_criteria: []
applicable_weight_percent: 100.00
scored_weight_percent: 80.00
unknown_weight_percent: 20.00
blocked_weight_percent: 0.00
excluded_weight_percent: 0.00
```

No criterion is blocked or structurally not applicable. Both unknown criteria remain in the category range and cannot create negative findings.

## 6. Observed maturity calculation

```text
Known maturity total = 450
Scored criterion count = 8
Observed Category Score = 450 ÷ 8 = 56.25
Displayed observed indicator = 56.25
```

## 7. Evidence coverage

```text
Scored applicable criteria = 8
Total applicable criteria = 10
Coverage = 8 ÷ 10 × 100 = 80.00%
```

Coverage reaches the numeric threshold, but it does not resolve the high-materiality search-context unknown.

## 8. Confidence index

Five scored criteria have high confidence and three have medium confidence.

```text
Confidence factor total = (5 × 1.00) + (3 × 0.75) = 7.25
Category Confidence Index = 7.25 ÷ 8 = 0.90625
Displayed confidence index = 0.9063
Confidence band = high
```

The confidence index applies only to scored evidence.

## 9. Confidence-adjusted bounds

The three medium-confidence criteria use `score ± 12.5`. High-confidence criteria retain their anchors. The two unknown criteria each contribute `0–100`.

```text
Known lower-bound total = 450 - (3 × 12.5) = 412.5
Known upper-bound total = 450 + (3 × 12.5) = 487.5
Unknown lower-bound total = 0
Unknown upper-bound total = 200

Category Lower Bound = (412.5 + 0) ÷ 10 = 41.25
Category Upper Bound = (487.5 + 200) ÷ 10 = 68.75
Displayed defensible range = 41.25–68.75
```

The range is an evidence boundary, not a probability interval or prediction.

## 10. Unknown validation and publication decision

```yaml
- criterion_id: OI-COMP-006
  state: unknown
  reason_code: not_tested
  materiality: high
  requested_evidence:
    - approved target-query set
    - governed local observation context
    - dated device and result-type record
    - Search Console or controlled tracking when available
  validation_owner: assessment_reviewer
  next_action: repeat_controlled_local_search_review
  finding_effect: no_visibility_finding_until_validated
  recommendation_effect: no_SEO_or_GBP_route_from_this_criterion
  validation_ref: OI-VAL-2026-0903

- criterion_id: OI-COMP-008
  state: unknown
  reason_code: not_provided
  materiality: medium
  requested_evidence:
    - approved service and buyer priorities
    - content-to-service relevance map
    - decision-usefulness review
  validation_owner: client_growth_owner
  next_action: validate_content_priority_and_usefulness
  finding_effect: no_content_gap_finding_until_validated
  recommendation_effect: no_content_or_dashboard_route_from_this_criterion
  validation_ref: OI-VAL-2026-0904
```

```yaml
score_value: null
score_type: range
observed_indicator: 56.25
score_range: [41.25, 68.75]
coverage_percent: 80.00
confidence_index: 0.9063
confidence_band: high
publication_state: range_only
material_unknowns:
  - OI-COMP-006 governed local-search context
  - OI-COMP-008 content usefulness and strategic fit
review_state: REVIEW
```

The high-materiality search-context unknown prevents responsible point-score publication despite 80% coverage. The observed indicator remains internal; the client-facing result is the governed range.

## 11. Finding and recommendation routing

The directly observed proof comparison supports one governed finding:

```yaml
finding_id: OI-FIND-COMP-009
criterion_owner: OI-COMP-004
observation: "The assessed business presents a basic image gallery, while each comparable competitor provides service-specific project pages or before-and-after proof with materially greater project context."
interpretation: "Buyers comparing providers receive less visible evidence to evaluate project fit, process, and completed-work relevance from the assessed business."
business_impact: "Comparable providers may give buyers more decision-useful evidence about relevant work and experience."
confidence: medium
priority: medium
limitations:
  - "No competitor revenue, market share, lead, conversion, ranking, or ROI effect is inferred."
ledger_ref: OI-DL-2026-016
```

The two unknown criteria route to validation only.

```yaml
primary_package: OI-PKG-TRUST-001
primary_package_name: Trust Proof System
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
routing_prerequisites:
  proof_type_and_placement_gap_identified: true
  claims_verified_before_publication: true
  work_and_review_assets_authentic: true
  local_and_service_relevance_documented: true
implementation_authorized: false
```

Routing eligibility passes. Implementation remains unauthorized until project selection, customer-data permissions, content ownership, acceptance criteria, and client approval are recorded.

## 12. DecisionLedger record

```yaml
fixture_path: scoring/examples/competitive-worked-example.md
fixture_version: "0.1"
category_key: competitive
category_sheet_version: "0.2"
criterion_inventory_version: criteria-library-v0.2
score_run_id: OI-SCORE-2026-006
criterion_ids:
  - OI-COMP-001
  - OI-COMP-002
  - OI-COMP-003
  - OI-COMP-004
  - OI-COMP-005
  - OI-COMP-006
  - OI-COMP-007
  - OI-COMP-008
  - OI-COMP-009
  - OI-COMP-010
evidence_refs:
  - OI-EVID-COMP-001
  - OI-EVID-COMP-002
  - OI-EVID-COMP-003
  - OI-EVID-COMP-004
  - OI-EVID-COMP-005
  - OI-EVID-COMP-006
  - OI-EVID-COMP-007
  - OI-EVID-COMP-008
  - OI-EVID-COMP-009
  - OI-EVID-COMP-010
applicable_criteria: 10
scored_criteria:
  - OI-COMP-001
  - OI-COMP-002
  - OI-COMP-003
  - OI-COMP-004
  - OI-COMP-005
  - OI-COMP-007
  - OI-COMP-009
  - OI-COMP-010
unknown_criteria:
  - OI-COMP-006
  - OI-COMP-008
blocked_criteria: []
not_applicable_criteria: []
applicable_weight_percent: 100.00
scored_weight_percent: 80.00
observed_indicator: 56.25
coverage_percent: 80.00
confidence_index: 0.9063
score_range: [41.25, 68.75]
publication_state: range_only
validation_refs:
  - OI-VAL-2026-0903
  - OI-VAL-2026-0904
finding_ids:
  - OI-FIND-COMP-009
primary_package: OI-PKG-TRUST-001
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
routing_prerequisites_complete: true
duplicate_check_passed: true
unsupported_claim_check_passed: true
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
ledger_ref: OI-DL-2026-016
```

## 13. Executive-safe statement

> The reviewed evidence supports a functional competitive baseline across the approved peer set, including comparable review context, service-page coverage, mobile inquiry paths, and professional presentation. The assessed business provides less service-specific project proof than the compared providers. Governed local-search context and the strategic usefulness of visible content remain unresolved, so the current evidence supports a Competitive Position range of 41.25–68.75 rather than a single official score. Validation and reviewed scope approval are required before implementation.

## 14. Usage instructions

1. Recalculate every value before changing the Competitive category sheet.
2. Preserve the approved comparable set and all 10 applicable criteria.
3. Keep `OI-COMP-006` and `OI-COMP-008` unknown until their validation evidence is available.
4. Do not create visibility, content, SEO, GBP, or Dashboard recommendations from those unknowns.
5. Preserve `OI-FIND-COMP-009` as the fixture recommendation root.
6. Keep `OI-PKG-TRUST-001` as the single primary package.
7. Preserve the separation between publication and implementation authorization.
8. Do not reuse synthetic scores or findings in a real engagement.

## 15. Regression assertions

This fixture passes only when:

- observed score equals `56.25`
- coverage equals `80.00%`
- confidence index equals `0.90625`
- known lower-bound total equals `412.5`
- known upper-bound total equals `487.5`
- defensible bounds equal `41.25–68.75`
- the Competitive category retains its canonical 5% Operator Score weight
- all 10 criterion records remain distinct
- applicable weight equals `100%`
- scored weight equals `80%`
- unknown weight equals `20%`
- unknown, blocked, and not-applicable states remain explicit
- both unknown criteria remain unscored and each contributes `0–100` to the range
- confidence does not modify maturity anchors
- publication remains `range_only`
- unknowns route to validation rather than findings
- `OI-FIND-COMP-009` routes to exactly one primary package
- package routing does not authorize implementation
- duplicate checks preserve Trust, SEO, GBP, Website, Messaging, and Conversion ownership
- client language avoids unsupported competitor performance claims

## 16. Completion check

- [x] Purpose, stage, folder alignment, usage, governance, and v1.0 connection are explicit
- [x] All 10 criteria are mapped exactly once
- [x] Comparable-set requirements are explicit
- [x] Applicable and scored weights reconcile
- [x] Unknown, blocked, and not-applicable treatment is visible
- [x] Score, coverage, confidence, and bounds recalculate
- [x] Publication matches coverage and unknown materiality
- [x] Finding and package routes match governed authorities
- [x] Implementation authorization is separate and false
- [x] DecisionLedger traceability is complete
- [x] Executive language is evidence-safe
- [ ] Category-sheet reconciliation completed
- [ ] Fixture registry admission completed
- [ ] Reviewer approval recorded
