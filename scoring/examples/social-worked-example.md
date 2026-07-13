# Social Presence Worked Scoring Example

Version: v0.1  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `social`  
Status: Regression fixture for commercial v1.0

## Purpose

Provide a reproducible Social Presence category example that applies the approved maturity anchors, confidence factors, unknown-data rules, confidence-adjusted bounds, publication controls, routing requirements, and DecisionLedger traceability.

This example supplements `scoring/category-sheets/social.md`. It does not create a governed Social finding library.

## Scenario

Ten criteria are applicable and equally weighted at 10% each. Nine criteria are scored. Public-response evidence for `OI-SOC-009` is insufficient, so the criterion remains `unknown` inside applicable weight.

Confidence factors:

- High: `1.00`
- Medium: `0.75`
- Low: `0.50`
- Unknown: `0.00`

Confidence bounds:

- High: score to score
- Medium: score minus 12.5 to score plus 12.5
- Low: score minus 25 to score plus 25
- Unknown or blocked: 0 to 100

All bounds are clamped to 0–100.

## Criterion results

| Criterion | State | Anchor | Confidence | Factor | Lower | Upper | Evidence ref | Evidence summary |
|---|---|---:|---|---:|---:|---:|---|---|
| `OI-SOC-001` | scored | 75 | High | 1.00 | 75.0 | 75.0 | `OI-EVID-SOC-001` | Facebook page is current, branded, and identifiable. |
| `OI-SOC-002` | scored | 50 | High | 1.00 | 50.0 | 50.0 | `OI-EVID-SOC-002` | Core fields align, but one profile retains an outdated service-area statement. |
| `OI-SOC-003` | scored | 50 | High | 1.00 | 50.0 | 50.0 | `OI-EVID-SOC-003` | Nine posts were observed across six months with two material inactivity gaps. |
| `OI-SOC-004` | scored | 75 | High | 1.00 | 75.0 | 75.0 | `OI-EVID-SOC-004` | Most sampled posts show attributable local projects and process evidence. |
| `OI-SOC-005` | scored | 25 | Medium | 0.75 | 12.5 | 37.5 | `OI-EVID-SOC-005` | Two educational posts exist, but buyer-question coverage is narrow. |
| `OI-SOC-006` | scored | 50 | Medium | 0.75 | 37.5 | 62.5 | `OI-EVID-SOC-006` | Review and team proof exists, but source attribution is inconsistent. |
| `OI-SOC-007` | scored | 50 | High | 1.00 | 50.0 | 50.0 | `OI-EVID-SOC-007` | The profile CTA works; only half of sampled posts contain a clear next action. |
| `OI-SOC-008` | scored | 25 | High | 1.00 | 25.0 | 25.0 | `OI-EVID-SOC-008` | Links are sparse and mostly route to the homepage rather than relevant service pages. |
| `OI-SOC-009` | unknown | — | Unknown | 0.00 | 0.0 | 100.0 | `OI-EVID-SOC-009` | Public thread coverage is insufficient and private response records were not provided. |
| `OI-SOC-010` | scored | 50 | Medium | 0.75 | 37.5 | 62.5 | `OI-EVID-SOC-010` | Seasonal topics appear, but no approved campaign calendar was provided. |

## Recalculation

### Observed maturity score

```text
Observed points = 75 + 50 + 50 + 75 + 25 + 50 + 50 + 25 + 50
Observed points = 450
Scored criterion count = 9
Observed score = 450 ÷ 9
Observed score = 50.00
```

The observed score uses scored applicable weight only. `OI-SOC-009` is not converted to zero.

### Coverage

```text
Scored applicable weight = 90%
Total applicable weight = 100%
Coverage = 90 ÷ 100
Coverage = 0.9000, or 90.00%
```

### Confidence index

```text
High-confidence scored criteria = 6
Medium-confidence scored criteria = 3

Confidence numerator = (6 × 1.00 × 0.10) + (3 × 0.75 × 0.10)
Confidence numerator = 0.825
Scored criterion weight = 0.90
Confidence index = 0.825 ÷ 0.90
Confidence index = 0.9167
Confidence band = High
```

The high confidence index applies only to known evidence. It does not remove the material unknown or increase the maturity score.

### Confidence-adjusted bounds

```text
Lower-bound points = 75 + 50 + 50 + 75 + 12.5 + 37.5 + 50 + 25 + 0 + 37.5
Lower-bound points = 412.5
Category lower bound = 412.5 ÷ 10
Category lower bound = 41.25

Upper-bound points = 75 + 50 + 50 + 75 + 37.5 + 62.5 + 50 + 25 + 100 + 62.5
Upper-bound points = 587.5
Category upper bound = 587.5 ÷ 10
Category upper bound = 58.75
```

The confidence-adjusted range is `41.25–58.75`. This replaces the simpler unknown-only range because criterion confidence data is available.

## Publication decision

```yaml
category_key: social
observed_score: 50.00
score_type: official
coverage_percent: 90.00
confidence_index: 0.9167
confidence_band: high
lower_bound: 41.25
upper_bound: 58.75
publication_state: provisional
material_unknowns:
  - criterion_id: OI-SOC-009
    reason: "Public response sample is insufficient and private response records were not provided."
    validation_required: "Inspect an adequate public thread sample or approved internal response records."
    publication_effect: "Prevents official category publication until resolved or accepted as a bounded limitation."
duplicate_check_passed: true
language_review_passed: true
```

`provisional` is required because a bounded material validation limitation remains despite 90% coverage and a high confidence index on known evidence.

## Finding and recommendation routing

No `OI-FIND-SOC-*` identifier is created because a governed Social finding library has not been approved.

```yaml
finding_refs: []
methodology_gaps:
  - social_finding_library_required
recommendation_refs: []
primary_package: null
dependent_packages: []
roadmap_phase: ""
implementation_authorized: false
```

Evidence may route to an existing adjacent governed finding only when that finding's evidence contract, ownership boundary, and materiality requirements are satisfied. Package-first routing is prohibited.

## DecisionLedger fixture

```yaml
category_key: social
category_sheet_version: "0.1"
criterion_inventory_version: "criteria-library-v0.2-draft"
score_run_id: OI-SCORE-2026-EXAMPLE-SOC
platforms_reviewed:
  - facebook
sample_period: "six months ending on evidence snapshot date"
applicable_criteria:
  - OI-SOC-001
  - OI-SOC-002
  - OI-SOC-003
  - OI-SOC-004
  - OI-SOC-005
  - OI-SOC-006
  - OI-SOC-007
  - OI-SOC-008
  - OI-SOC-009
  - OI-SOC-010
scored_criteria:
  - OI-SOC-001
  - OI-SOC-002
  - OI-SOC-003
  - OI-SOC-004
  - OI-SOC-005
  - OI-SOC-006
  - OI-SOC-007
  - OI-SOC-008
  - OI-SOC-010
unknown_criteria:
  - OI-SOC-009
blocked_criteria: []
not_applicable_criteria: []
observed_score: 50.00
lower_bound: 41.25
upper_bound: 58.75
coverage: 0.9000
confidence_index: 0.9167
confidence_band: high
publication_state: provisional
material_unknowns:
  - OI-SOC-009
finding_refs: []
methodology_gaps:
  - social_finding_library_required
recommendation_refs: []
primary_package: null
package_dependencies: []
roadmap_phase: ""
duplicate_check_passed: true
language_review_passed: true
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-2026-EXAMPLE-SOC
```

## Regression assertions

A conforming implementation must reproduce all of the following:

```yaml
observed_score: 50.00
coverage: 0.9000
confidence_index: 0.9167
confidence_band: high
lower_bound: 41.25
upper_bound: 58.75
publication_state: provisional
unknown_is_zero: false
social_finding_created: false
implementation_authorized: false
```

Fail the regression when:

- `OI-SOC-009` is scored as zero
- medium-confidence criteria are treated as point bounds
- the confidence index is stored only as a label
- the unknown-only range `45.0–55.0` replaces the confidence-adjusted range
- high confidence is used to justify `official` publication despite the material unknown
- an ungoverned `OI-FIND-SOC-*` identifier is created
- a package is selected without a valid governed finding
- publication approval is treated as implementation authorization
- unsupported reach, engagement, lead, revenue, ROI, response-time, or market-performance claims are introduced

## Cross references

- `scoring/category-sheets/social.md`
- `scoring/confidence-adjusted-scoring.md`
- `scoring/calculator-spec.md`
- `scoring/unknown-data-handling.md`
- `standards/publication-standard.md`
- `standards/quality-control-standard.md`
- `standards/decision-ledger-standard.md`
