# Operator Intelligence Calculator Specification

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file defines the deterministic calculation order for criterion scores, category scores, score coverage, confidence outputs, and the Operator Score.

It converts the existing criteria, anchors, weights, evidence thresholds, and framework gates into one auditable scoring procedure. It does not replace domain criteria or category sheets.

## v1.0 connection

Commercial v1.0 requires two qualified evaluators using the same evidence to produce materially similar results.

This specification strengthens v1.0 readiness by providing:

- one criterion scoring scale
- one category aggregation method
- one weighted Operator Score formula
- explicit unknown and not-applicable handling
- confidence and coverage outputs
- score-range rules
- publication eligibility gates
- calculation validation errors
- deterministic calculation order
- DecisionLedger and score-run traceability

## Source alignment

The calculator consumes:

- `scoring/criteria-library.md`
- `scoring/grading-rubric.md`
- `scoring/evidence-thresholds.md`
- `scoring/confidence-model.md`
- `scoring/weights.md`
- `scoring/unknown-data-handling.md`
- `scoring/confidence-adjusted-scoring.md`
- future approved category sheets

It must also pass the scoring gates in `framework/governance-gate-index.md`.

## Core scoring principles

1. Unknown is not zero.
2. Not applicable is not unknown and requires documented justification.
3. Performance score and evidence confidence are separate outputs.
4. Evidence uncertainty must not be converted into an automatic performance penalty.
5. Category weights must reconcile to 100% before an official Operator Score is published.
6. One signal must not be counted through overlapping criteria without approved boundary logic.
7. Raw calculations retain decimal precision; client-facing scores round to the nearest whole number.
8. A precise score must not be published when evidence coverage does not support precision.
9. Weight changes require a named profile, rationale, approval, and calculation record.
10. Every published score must be reproducible from stored score objects.

## Canonical weighted categories

| Category key | Client-facing category | Criteria prefixes | Default weight |
|---|---|---|---:|
| `website` | Website structure and UX | `OI-WEB-*` | 10% |
| `messaging_offer` | Messaging and offer clarity | `OI-MSG-*`, `OI-OFFER-*` | 10% |
| `conversion` | Conversion infrastructure | `OI-CONV-*` | 15% |
| `seo` | Local SEO | `OI-SEO-*` | 15% |
| `gbp` | Google Business Profile | `OI-GBP-*` | 10% |
| `trust` | Reputation and trust | `OI-TRUST-*` | 10% |
| `social` | Social presence | `OI-SOC-*` | 5% |
| `automation` | Automation maturity | `OI-AUTO-*` | 10% |
| `ai_readiness` | AI readiness | `OI-AI-*` | 5% |
| `analytics` | Analytics and reporting | `OI-AN-*` | 5% |
| `competitive` | Competitive position | `OI-COMP-*` | 5% |

The `messaging_offer` category combines messaging and offer criteria because the approved Operator Score weight model treats them as one category. The criterion records remain separate for findings, recommendations, and implementation routing.

Social criteria remain scoreable because they exist in the criteria library. Until a governed social finding library is approved, social score weaknesses may support existing governed findings or a methodology-gap record but must not create `OI-FIND-SOC-*` IDs.

## Criterion score states

| State | Meaning | Numeric contribution |
|---|---|---|
| `scored` | Evidence supports an anchor score | Uses approved score |
| `unknown` | Evidence is insufficient | No point value; expands score range |
| `not_applicable` | Criterion is structurally irrelevant to this business | Excluded from applicable weight with approval |
| `blocked` | Evaluation cannot proceed because access, policy, conflict, or control boundary prevents scoring | Treated as unknown and flagged for review |

## Criterion anchors

Use the approved universal anchors unless a future category sheet defines stricter criterion-specific anchors.

| Score | Operational meaning |
|---:|---|
| 0 | Confirmed missing, broken, misleading, or actively harmful |
| 25 | Present but weak, incomplete, inconsistent, or unreliable |
| 50 | Functional baseline with material improvement opportunity |
| 75 | Strong, commercially useful, and consistently implemented |
| 100 | Mature, differentiated, measured, integrated, and governed |

### Anchor rule

Commercial v1.0 criterion scores use `0`, `25`, `50`, `75`, or `100` only.

Do not interpolate between anchors unless an approved category sheet defines the interpolation rule and the score object records that rule.

## Criterion admission

A criterion may be scored when:

- applicable scope is confirmed
- evidence meets the threshold in `scoring/evidence-thresholds.md`
- the observation is distinguishable from interpretation
- confidence is assigned
- the score anchor can be defended
- overlapping criteria have been checked

Class D inferred evidence should normally produce `unknown`, `blocked`, or a validation task rather than a score penalty.

## Criterion weighting

Default criterion weight inside a weighted category is equal:

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

A future category sheet may define non-equal criterion weights. When it does:

- weights must total 100% within the category
- rationale must be documented
- the version must be stored in the score run
- no weight may be changed during a client assessment without rerunning the full category

## Category calculation

For each category:

```text
Known Criterion Weight = sum(weights for scored criteria)
Unknown Criterion Weight = sum(weights for unknown or blocked criteria)
Applicable Criterion Weight = Known Criterion Weight + Unknown Criterion Weight

Observed Category Score =
sum(criterion score × criterion weight) ÷ Known Criterion Weight

Category Coverage =
Known Criterion Weight ÷ Applicable Criterion Weight
```

`not_applicable` criteria are excluded from applicable weight after the exclusion passes review.

### Category score range

Unknown criteria create a mathematically honest range:

```text
Category Minimum =
sum(known criterion score × weight) ÷ Applicable Criterion Weight

Category Maximum =
[sum(known criterion score × weight)
+ sum(100 × unknown criterion weight)]
÷ Applicable Criterion Weight
```

The observed category score describes the known evidence only. The minimum and maximum show how unresolved evidence could change the full category result.

## Category publication states

| Coverage | State | Client-facing treatment |
|---:|---|---|
| 80–100% | `reportable` | Publish category score, confidence, coverage, and material unknowns |
| 60–79.99% | `provisional` | Publish provisional score with range and validation note |
| Below 60% | `range_only` | Do not publish a precise category score; publish range or insufficient-data state |

A category may be forced to `range_only` or `blocked` regardless of coverage when:

- a material control-boundary question is unresolved
- evidence conflicts materially
- the criterion set does not represent the business model
- weight or duplicate-control integrity fails

## Operator Score calculation

The default formula is:

```text
Operator Score =
sum(category score × category weight)
```

The calculator produces three distinct outputs.

### 1. Observed normalized score

Uses only categories with an observed score:

```text
Observed Normalized Operator Score =
sum(observed category score × included category weight)
÷ sum(included category weight)
```

This value must always disclose how much category weight was included. It is not automatically eligible as the official Operator Score.

### 2. Full Operator Score range

Uses every active category and its minimum and maximum:

```text
Operator Minimum = sum(category minimum × category weight)
Operator Maximum = sum(category maximum × category weight)
```

### 3. Official Operator Score

An official point score is eligible only when all conditions pass:

- active category weights equal 100%
- weighted evidence coverage is at least 80%
- no category weighted at 10% or more has coverage below 60%
- no G4 control-boundary scoring issue is unresolved
- duplicate-control and category-mapping checks pass
- score-run validation produces no blocking errors

When these conditions do not pass, publish a provisional score and range, or range only.

## Weighted evidence coverage

```text
Weighted Evidence Coverage =
sum(category coverage × category weight)
```

Because active category weights total 100%, the result is a percentage from 0% to 100%.

Coverage describes how much of the weighted model was evaluated. It does not describe business maturity.

## Operator Score publication states

| Condition | Publication state |
|---|---|
| Official-score gates pass | `official` |
| Weighted coverage is 65–79.99%, or one major category is below 60% coverage | `provisional` |
| Weighted coverage is below 65% | `range_only` |
| Weight, duplicate, source, policy, or control-boundary validation fails | `blocked` |

## Maturity tier assignment

Assign a maturity tier from the official or provisional point estimate only when a point estimate is permitted.

| Score | Tier |
|---:|---|
| 0–39 | Foundational Risk |
| 40–59 | Developing |
| 60–74 | Growth Ready |
| 75–89 | High Performing |
| 90–100 | Market Leader |

When the score range crosses more than one tier, report the range and state that the maturity tier is not yet resolved.

## Confidence integration

Confidence does not reduce the raw maturity score.

The calculator uses confidence to produce:

- criterion uncertainty bounds
- category confidence index
- Operator Score confidence index
- publication state
- validation flags
- report wording

The detailed method is defined in `scoring/confidence-adjusted-scoring.md`.

## Calculation order

Run the calculator in this exact order:

1. Load scoring version, criteria version, weight profile, and category map.
2. Validate category weights.
3. Validate criterion IDs and category assignments.
4. Resolve criterion applicability.
5. Attach evidence and evidence class.
6. Assign criterion state.
7. Assign score anchor for scored criteria.
8. Assign confidence.
9. Run duplicate-control checks.
10. Calculate criterion weights.
11. Calculate category observed scores, coverage, bounds, confidence, and publication states.
12. Calculate weighted evidence coverage.
13. Calculate observed normalized Operator Score.
14. Calculate Operator Score minimum and maximum.
15. Apply official, provisional, range-only, or blocked publication gate.
16. Assign maturity tier only when permitted.
17. Create validation errors and warnings.
18. Persist score objects and score-run metadata.
19. Generate client-safe score language.
20. Link the result to findings and the DecisionLedger.

## Rounding rules

- Store raw criterion and category calculations to at least four decimal places.
- Display category and Operator Scores as whole numbers.
- Display coverage and confidence indexes as whole percentages.
- Do not round category scores before calculating the Operator Score.
- Do not convert a range into a point estimate by averaging its endpoints for client reporting.

## Validation errors

### Blocking errors

- active category weights do not total 100%
- criterion ID does not exist
- criterion appears in more than one weighted category without approved mapping
- scored criterion lacks admissible evidence
- scored criterion lacks confidence
- unknown criterion has a numeric score
- not-applicable exclusion lacks reason or approval
- published point score fails coverage gates
- duplicate signal materially inflates score
- score-run versions are missing

### Warnings

- category coverage below 80%
- low-confidence criterion affects a high-weight category
- score range crosses maturity tiers
- client-provided inputs are unreconciled
- social score weakness lacks a governed finding route
- category sheet is absent and equal criterion weights are being used

## Deterministic example

Assume a category has four equally weighted applicable criteria:

| Criterion | State | Score |
|---|---|---:|
| A | scored | 75 |
| B | scored | 50 |
| C | scored | 25 |
| D | unknown | — |

Each criterion weight is 25%.

```text
Observed Category Score = (75 + 50 + 25) ÷ 3 = 50
Category Coverage = 3 ÷ 4 = 75%
Category Minimum = (75×.25 + 50×.25 + 25×.25) = 37.5
Category Maximum = 37.5 + (100×.25) = 62.5
```

Client-facing result:

```text
Provisional category score: 50
Evidence coverage: 75%
Current defensible range: 38–63
```

The unknown criterion is not scored as zero.

## DecisionLedger minimum record

```yaml
score_run_id: OI-SCORE-YYYY-NNN
client_ref: ""
calculator_version: "0.1"
criteria_version: ""
weight_profile: default
category_map_version: "0.1"
criterion_score_refs: []
category_score_refs: []
weighted_evidence_coverage: 0
observed_normalized_score: null
operator_minimum: 0
operator_maximum: 100
publication_state: range_only
maturity_tier: unresolved
validation_errors: []
warnings: []
reviewer: ""
approver: ""
ledger_ref: OI-DL-YYYY-NNN
```

## Usage instructions

1. Build criterion score objects from evidence.
2. Resolve unknown and not-applicable states before aggregation.
3. Validate weights and category mapping.
4. Run category calculations without early rounding.
5. Calculate score coverage and bounds.
6. Apply confidence and publication rules.
7. Store all objects and validation messages.
8. Publish only the score form permitted by the admission gates.
9. Link weak scored criteria to governed findings without creating duplicates.
10. Recalculate when evidence, scope, applicability, or weights change.

## Completion check

Before publishing an Operator Score, confirm:

- source versions are recorded
- category weights total 100%
- criterion IDs are valid
- unknown is not scored as zero
- not-applicable exclusions are justified
- evidence coverage is disclosed
- confidence is separate from maturity
- score bounds are calculated
- publication state is correct
- tier assignment is permitted
- duplicate controls pass
- validation errors are resolved
- DecisionLedger traceability exists
