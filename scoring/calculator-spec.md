# Operator Intelligence Calculator Specification

Version: v0.2 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file defines the deterministic calculation order for criterion scores, category scores, evidence coverage, confidence outputs, and the Operator Score.

It converts the existing criteria, anchors, weights, evidence thresholds, and framework gates into one auditable scoring procedure. It does not replace domain criteria or future category sheets.

## v1.0 connection

Commercial v1.0 requires two qualified evaluators using the same evidence to produce materially similar results.

This specification provides:

- one criterion scoring scale
- one category aggregation method
- one weighted Operator Score formula
- explicit unknown and not-applicable handling
- confidence and coverage outputs
- score-range rules
- publication eligibility gates
- deterministic validation errors
- score-run and DecisionLedger traceability

## Source alignment

The calculator consumes:

- `scoring/criteria-library.md`
- `scoring/grading-rubric.md`
- `scoring/evidence-thresholds.md`
- `scoring/confidence-model.md`
- `scoring/weights.md`
- `scoring/score-objects.md`
- `scoring/unknown-data-handling.md`
- `scoring/confidence-adjusted-scoring.md`
- future approved category sheets

It must pass the scoring gates in `framework/governance-gate-index.md`.

## Core scoring principles

1. Unknown is not zero.
2. Not applicable is not unknown and requires documented justification.
3. Maturity and evidence confidence are separate outputs.
4. Evidence uncertainty must not become an automatic performance penalty.
5. Active category weights must reconcile to 100% before an official Operator Score is published.
6. One signal must not be counted through overlapping criteria without approved boundary logic.
7. Raw calculations retain decimal precision; client-facing values round only at display time.
8. A precise score must not be published when evidence coverage does not support precision.
9. Weight changes require a named profile, rationale, approval, and rerun.
10. Every published result must be reproducible from stored score objects.

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

The `messaging_offer` category combines messaging and offer criteria because the approved Operator Score weight model treats them as one weighted category. Criterion records remain separate for findings and recommendation routing.

Social criteria remain scoreable because they exist in the criteria library. Until a governed social finding library is approved, social weaknesses may support existing findings or a methodology-gap record but must not create `OI-FIND-SOC-*` IDs.

## Criterion evaluation states

| State | Meaning | Numeric treatment |
|---|---|---|
| `scored` | Evidence supports an approved anchor | Included in observed score |
| `unknown` | Evidence is insufficient | No point value; expands range |
| `not_applicable` | Criterion is structurally irrelevant | Excluded after review |
| `blocked` | Access, policy, conflict, system, or control boundary prevents evaluation | Treated as unknown plus governance flag |

## Criterion anchors

| Score | Operational meaning |
|---:|---|
| 0 | Confirmed missing, broken, misleading, or actively harmful |
| 25 | Present but weak, incomplete, inconsistent, or unreliable |
| 50 | Functional baseline with material improvement opportunity |
| 75 | Strong, commercially useful, and consistently implemented |
| 100 | Mature, differentiated, measured, integrated, and governed |

Commercial v1.0 uses `0`, `25`, `50`, `75`, and `100` only unless an approved category sheet defines an interpolation rule and the score object records it.

## Criterion admission gate

A criterion may be scored only when:

- applicability is resolved
- evidence meets the approved threshold
- observation is separate from interpretation
- confidence is assigned
- the selected anchor is defensible
- overlapping criteria have been checked

Class D inferred evidence should normally produce `unknown`, `blocked`, or a validation task rather than a score penalty.

## Criterion weighting

Default weighting inside each category is equal:

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

A future category sheet may define non-equal weights only when:

- internal weights total 100%
- rationale and version are recorded
- the active run identifies that version
- any change triggers full category recalculation

## Category calculation

For each category:

```text
Known Weight = sum(weights for scored criteria)
Unknown Weight = sum(weights for unknown or blocked criteria)
Applicable Weight = Known Weight + Unknown Weight

Observed Category Score =
sum(criterion score × criterion weight) ÷ Known Weight

Category Coverage = Known Weight ÷ Applicable Weight
```

`not_applicable` criteria are excluded only after the exclusion is justified and approved.

## Category range

When confidence bounds are unavailable, use the unknown-only range:

```text
Category Minimum =
sum(known criterion score × weight) ÷ Applicable Weight

Category Maximum =
[sum(known criterion score × weight)
+ sum(100 × unknown weight)]
÷ Applicable Weight
```

When confidence bounds are available, use the method in `scoring/confidence-adjusted-scoring.md`.

The observed score describes known evidence. The range describes unresolved uncertainty.

## Category publication states

| Coverage and controls | State | Client-facing treatment |
|---|---|---|
| 80–100%, confidence gates pass, no material blocker | `official` | Publish score, confidence, coverage, and material unknowns |
| 60–79.99%, or confidence requires qualification | `provisional` | Publish provisional score with range and validation note |
| Below 60%, or confidence is insufficient | `range_only` | Publish range or insufficient-data state, not a precise score |
| Weight, duplicate, source, policy, or control-boundary integrity fails | `blocked` | Do not publish score |

A category may be forced to `range_only` or `blocked` regardless of numeric coverage when evidence conflicts, a material control boundary remains open, the criterion set does not represent the business, or mapping integrity fails.

## Operator Score outputs

The calculator produces three distinct outputs.

### Observed normalized score

```text
Observed Normalized Operator Score =
sum(observed category score × included category weight)
÷ sum(included category weight)
```

This output must disclose the included active weight. It is not automatically the official Operator Score.

### Full Operator Score range

```text
Operator Minimum = sum(category minimum × category weight)
Operator Maximum = sum(category maximum × category weight)
```

Use all active categories.

### Official Operator Score

An official point score is eligible only when:

- active category weights equal 100%
- weighted evidence coverage is at least 80%
- Operator confidence index is at least 0.65
- no category weighted at 10% or more has coverage below 60%
- no high-materiality unknown invalidates the point estimate
- no G4 scoring boundary is unresolved
- duplicate and category-mapping checks pass
- no blocking validation error remains

When these gates fail, publish a provisional score and range, range only, or blocked state.

## Weighted evidence coverage

```text
Weighted Evidence Coverage =
sum(category coverage × category weight)
```

Coverage measures how much of the weighted model was evaluated. It does not measure maturity.

## Operator Score publication states

| Condition | State |
|---|---|
| Official-score gates pass | `official` |
| Weighted coverage is 65–79.99%, or confidence is at least 0.50 but below official threshold | `provisional` |
| Weighted coverage is below 65%, confidence is below 0.50, or major categories remain unresolved | `range_only` |
| Weight, duplicate, evidence-integrity, policy, approval, or control-boundary validation fails | `blocked` |

## Maturity tiers

| Score | Tier |
|---:|---|
| 0–39 | Foundational Risk |
| 40–59 | Developing |
| 60–74 | Growth Ready |
| 75–89 | High Performing |
| 90–100 | Market Leader |

Assign a tier only when a point estimate is permitted. If the score range crosses more than one tier, the tier remains unresolved.

## Confidence integration

Confidence does not reduce the raw maturity score.

It determines:

- criterion uncertainty bounds
- category and Operator confidence indexes
- score range
- publication state
- validation flags
- report wording

Use `scoring/confidence-adjusted-scoring.md` as the authoritative method.

## Calculation order

1. Load calculator, criteria, rubric, evidence, confidence, category-map, and weight-profile versions.
2. Validate active category weights.
3. Validate criterion IDs and category assignments.
4. Resolve applicability.
5. Attach evidence and evidence class.
6. Assign evaluation state.
7. Assign anchor for scored criteria.
8. Assign confidence.
9. Run duplicate-control checks.
10. Calculate criterion weights.
11. Calculate category observed scores, coverage, bounds, confidence, and states.
12. Calculate weighted evidence coverage.
13. Calculate observed normalized Operator Score.
14. Calculate full Operator Score range.
15. Calculate Operator confidence index.
16. Apply publication gate.
17. Assign maturity tier only when permitted.
18. Create validation errors and warnings.
19. Persist score objects and run metadata.
20. Generate client-safe language and DecisionLedger references.

## Rounding

- Store calculations to at least four decimal places.
- Display score, coverage, and confidence values as whole numbers.
- Do not round category scores before calculating the Operator Score.
- Do not convert a range into a client-facing midpoint.

## Blocking validation errors

- active weights do not total 100%
- criterion ID does not exist
- criterion maps to overlapping weighted categories without approval
- scored criterion lacks admissible evidence or confidence
- unknown criterion contains a numeric score
- not-applicable exclusion lacks reason or approval
- point score fails coverage or confidence gates
- duplicate signal materially inflates score
- methodology versions are missing
- required review or approval is absent

## Warnings

- category coverage below 80%
- low-confidence criterion affects a high-weight category
- score range crosses maturity tiers
- client-provided inputs are unreconciled
- social weakness lacks a governed finding route
- equal criterion weights are used because no category sheet exists

## Deterministic example

Four equally weighted applicable criteria produce:

| Criterion | State | Score |
|---|---|---:|
| A | scored | 75 |
| B | scored | 50 |
| C | scored | 25 |
| D | unknown | — |

```text
Observed Score = (75 + 50 + 25) ÷ 3 = 50
Coverage = 3 ÷ 4 = 75%
Minimum = 37.5
Maximum = 62.5
```

Client-facing result:

```text
Provisional category score: 50
Evidence coverage: 75%
Defensible range: 38–63
```

The unknown criterion is not scored as zero.

## Canonical score-run summary

```yaml
score_run_id: OI-SCORE-YYYY-NNN
client_ref: ""
calculator_version: "0.2"
criteria_version: ""
category_map_version: "0.1"
weight_profile: default
criterion_score_refs: []
category_score_refs: []
weighted_evidence_coverage: 0
operator_confidence_index: 0
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

1. Build score objects from evidence.
2. Resolve unknown and not-applicable states before aggregation.
3. Validate weights and category mapping.
4. Calculate category outputs without early rounding.
5. Calculate coverage, confidence, and bounds.
6. Apply publication gates.
7. Store validation messages and approvals.
8. Publish only the permitted score form.
9. Link weak criteria to governed findings without duplication.
10. Recalculate when evidence, scope, applicability, confidence, or weights change.

## Completion check

Before publication, confirm:

- source versions are recorded
- category weights total 100%
- criterion IDs and mappings are valid
- unknown is not scored as zero
- exclusions are justified
- coverage and confidence are disclosed
- score bounds are calculated
- publication state is valid
- tier assignment is permitted
- duplicate controls pass
- validation errors are resolved
- review and approval are recorded
- DecisionLedger traceability exists
