# Trust Category Worked Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `trust`  
Status: Commercial v1.0 validation fixture

## Purpose

Provide a reproducible Trust category score run that demonstrates criterion states, evidence references, maturity anchors, confidence factors, confidence-adjusted bounds, coverage, publication state, finding routing, package routing, roadmap phase, and DecisionLedger traceability.

This fixture supplements `scoring/category-sheets/trust.md`. It does not change category ownership, criterion weights, scoring anchors, or publication thresholds.

## Inputs

All twelve `OI-TRUST-*` criteria are applicable and equally weighted.

```text
criterion_weight = 1 / 12 = 0.083333
```

Confidence factors follow `scoring/confidence-adjusted-scoring.md`:

```text
high = 1.00
medium = 0.75
low = 0.50
unknown = 0.00
```

## Criterion record

| Criterion | State | Score | Confidence | Evidence ref | Defensible bound |
|---|---|---:|---|---|---|
| `OI-TRUST-001` | scored | 50 | high | `OI-EVID-TRUST-001` | 50–50 |
| `OI-TRUST-002` | scored | 75 | high | `OI-EVID-TRUST-002` | 75–75 |
| `OI-TRUST-003` | scored | 50 | high | `OI-EVID-TRUST-003` | 50–50 |
| `OI-TRUST-004` | scored | 25 | medium | `OI-EVID-TRUST-004` | 12.5–37.5 |
| `OI-TRUST-005` | scored | 75 | high | `OI-EVID-TRUST-005` | 75–75 |
| `OI-TRUST-006` | unknown | — | unknown | `OI-EVID-TRUST-006-PENDING` | 0–100 |
| `OI-TRUST-007` | scored | 50 | medium | `OI-EVID-TRUST-007` | 37.5–62.5 |
| `OI-TRUST-008` | scored | 75 | high | `OI-EVID-TRUST-008` | 75–75 |
| `OI-TRUST-009` | scored | 50 | medium | `OI-EVID-TRUST-009` | 37.5–62.5 |
| `OI-TRUST-010` | scored | 75 | high | `OI-EVID-TRUST-010` | 75–75 |
| `OI-TRUST-011` | scored | 100 | high | `OI-EVID-TRUST-011` | 100–100 |
| `OI-TRUST-012` | scored | 50 | high | `OI-EVID-TRUST-012` | 50–50 |

## Calculation

### Observed score

Unknown criteria are excluded from the observed-score numerator and denominator.

```text
observed_score = 675 / 11 = 61.36
```

### Coverage

Unknown criteria remain inside applicable weight.

```text
coverage = 11 / 12 = 0.9167 = 91.67%
```

### Confidence index

Eight scored criteria are high confidence and three are medium confidence.

```text
confidence_index = ((8 × 1.00) + (3 × 0.75)) / 11
                 = 10.25 / 11
                 = 0.9318
confidence_band = high
```

The high confidence index applies only to scored evidence. It does not eliminate the material unknown.

### Confidence-adjusted bounds

Known criterion bounds use the confidence-specific ranges. The unknown criterion contributes `0–100`.

```text
lower_bound = 637.5 / 12 = 53.13
upper_bound = 812.5 / 12 = 67.71
```

These bounds replace the simpler unknown-only range for this regression fixture because medium-confidence criteria must also widen uncertainty.

## Publication and routing outcome

```yaml
category_key: trust
category_sheet_version: "0.2"
score_run_id: OI-SCORE-2026-TRUST-001
applicable_criteria: 12
scored_criteria: 11
unknown_criteria:
  - OI-TRUST-006
observed_score: 61.36
lower_bound: 53.13
upper_bound: 67.71
coverage: 0.9167
confidence_index: 0.9318
confidence_band: high
publication_state: provisional
material_unknowns:
  - criterion_id: OI-TRUST-006
    reason: credential and insurance evidence pending validation
    required_evidence: authoritative credential or insurance record
    validation_owner: client
    publication_effect: prevents official publication
finding_refs:
  - OI-FIND-TRUST-002
  - OI-FIND-TRUST-007
  - OI-FIND-TRUST-012
recommendation_refs:
  - OI-REC-TRUST-001
primary_package: OI-PKG-TRUST-001
primary_package_name: Trust Proof System
dependent_packages: []
roadmap_phase: Phase 2 — Growth Foundation
implementation_authorized: false
duplicate_check_passed: true
ledger_ref: OI-DL-2026-TRUST-001
```

## Governance assertions

- Unknown is not scored as zero.
- Confidence does not alter the maturity score.
- Medium-confidence criteria widen the defensible range.
- High confidence on known evidence does not convert incomplete coverage into official publication.
- Findings require criterion-level evidence and are not created from the category score alone.
- The recommendation has exactly one primary package.
- Publication does not authorize implementation.
- No revenue, ROI, conversion, legal-compliance, or competitor-performance claim is inferred.

## Regression acceptance checks

- [x] Observed score recalculates to `61.36`.
- [x] Coverage recalculates to `91.67%`.
- [x] Confidence index recalculates to `0.9318`.
- [x] Confidence-adjusted lower bound recalculates to `53.13`.
- [x] Confidence-adjusted upper bound recalculates to `67.71`.
- [x] `OI-TRUST-006` remains unknown and inside applicable weight.
- [x] Publication remains `provisional` until credential evidence is validated.
- [x] Finding, package, roadmap, and DecisionLedger references are present.
