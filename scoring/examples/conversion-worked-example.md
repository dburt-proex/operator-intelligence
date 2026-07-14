# Conversion Infrastructure Worked Scoring Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `conversion`  
Default Operator Score weight: 15%  
Status: Commercial v1.0 validation fixture

## 1. Purpose

Provide a reproducible Conversion Infrastructure category calculation that verifies maturity scoring, evidence coverage, numeric confidence, uncertainty bounds, material-unknown treatment, governed finding routing, package ownership, roadmap phase, publication state, implementation authorization, and DecisionLedger traceability.

This fixture supplements `scoring/category-sheets/conversion.md`. It does not replace the category contract.

## 2. Scenario

A local contractor has visible estimate CTAs, a functional estimate form, working tap-to-call links, multiple inquiry paths, and a verified confirmation state. Service-page CTA coverage and intake context are incomplete. Lead-source capture cannot be inspected because form configuration and CRM access were not provided.

All 14 criteria are applicable and equally weighted. Thirteen criteria are scored. `OI-CONV-014` remains unknown and material because attribution readiness cannot be verified.

## 3. Criterion results

| Criterion | State | Score | Confidence | Factor | Defensible bound | Evidence reference |
|---|---|---:|---|---:|---|---|
| `OI-CONV-001` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-CONV-001` desktop and mobile hero CTA screenshots |
| `OI-CONV-002` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-CONV-002` CTA language inventory and buyer-intent review |
| `OI-CONV-003` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-CONV-003` service-page CTA inventory showing inconsistent coverage |
| `OI-CONV-004` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-CONV-004` form field inventory; location and urgency fields absent |
| `OI-CONV-005` | scored | 75 | medium | 0.75 | 62.5–87.5 | `OI-EVID-CONV-005` one representative completion test; secondary path not tested |
| `OI-CONV-006` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-CONV-006` safe submission and confirmation screenshot |
| `OI-CONV-007` | scored | 100 | high | 1.00 | 100–100 | `OI-EVID-CONV-007` mobile tap-to-call tests across required pages |
| `OI-CONV-008` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-CONV-008` sampled service-specific prompts; several generic CTAs remain |
| `OI-CONV-009` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-CONV-009` project-detail field review; structured context and upload absent |
| `OI-CONV-010` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-CONV-010` contact-page and confirmation response expectation |
| `OI-CONV-011` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-CONV-011` review proof near primary CTAs |
| `OI-CONV-012` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-CONV-012` working phone and form paths |
| `OI-CONV-013` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-CONV-013` urgent phone path present; availability language incomplete |
| `OI-CONV-014` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-CONV-014` form configuration, CRM source fields, and UTM retention unavailable |

## 4. Observed maturity calculation

```text
Known maturity total = 875
Scored criterion count = 13
Observed Category Score = 875 ÷ 13 = 67.3077
Displayed observed indicator = 67.31
```

The unknown criterion is excluded from the observed point-score denominator because no maturity anchor is defensible. It remains inside applicable weight for coverage and range calculations.

## 5. Evidence coverage

```text
Scored applicable criteria = 13
Total applicable criteria = 14
Coverage = 13 ÷ 14 × 100 = 92.8571%
Displayed coverage = 92.86%
```

Coverage above 90% does not independently authorize `official` publication when material source-capture evidence remains unresolved.

## 6. Confidence index

Nine scored criteria have high confidence and four have medium confidence.

```text
Confidence factor total = (9 × 1.00) + (4 × 0.75) = 12.00
Category Confidence Index = 12.00 ÷ 13 = 0.923076...
Displayed confidence index = 0.9231
Confidence band = high
```

The high confidence index applies only to known evidence. It does not resolve `OI-CONV-014`.

## 7. Confidence-adjusted bounds

For the four medium-confidence criteria, apply ±12.5. High-confidence criteria retain their observed anchors. The unknown criterion contributes 0–100.

```text
Known lower-bound total = 875 - (4 × 12.5) = 825
Known upper-bound total = 875 + (4 × 12.5) = 925
Unknown lower-bound total = 0
Unknown upper-bound total = 100

Category Lower Bound = (825 + 0) ÷ 14 = 58.9286
Category Upper Bound = (925 + 100) ÷ 14 = 73.2143
Displayed defensible range = 58.93–73.21
```

This range represents evidence uncertainty and unresolved attribution scope. It is not a statistical confidence interval.

## 8. Publication decision

```yaml
score_value: null
score_type: range
observed_indicator: 67.31
score_range: [58.93, 73.21]
coverage_percent: 92.86
confidence_index: 0.9231
confidence_band: high
publication_state: range_only
material_unknowns:
  - OI-CONV-014 lead-source capture and attribution readiness
review_state: REVIEW
```

The category remains `range_only` because source capture could materially affect the interpretation of conversion infrastructure. The observed indicator must not be presented as an official point score.

## 9. Finding and recommendation routing

The directly observed intake limitation supports one governed finding:

```yaml
finding_id: OI-FIND-CONV-005
criterion_owner:
  - OI-CONV-004
  - OI-CONV-009
observation: "The estimate form captures baseline contact information but does not capture location, urgency, structured service context, or supporting project details."
interpretation: "The verified intake path may require additional manual clarification before the inquiry is ready for action."
business_impact: "Staff may need extra qualification steps, which can reduce response consistency and slow estimate preparation."
confidence: high
priority: medium
limitations:
  - "No lead-volume, conversion-rate, close-rate, revenue, or ROI effect is inferred."
ledger_ref: OI-DL-2026-014
```

The unresolved attribution criterion creates a validation requirement and does not create a negative analytics or automation finding by itself.

```yaml
validation_required: true
validation_criteria:
  - OI-CONV-014
primary_package: OI-PKG-WEB-001
dependent_packages: []
roadmap_phase: "Phase 1 — Quick Wins"
implementation_authorized: false
```

Exactly one primary package is assigned because the verified weakness is the public estimate form. CRM or dashboard packages remain uncommitted until internal evidence validates an operational or measurement dependency.

## 10. DecisionLedger record

```yaml
category_key: conversion
category_sheet_version: "0.1"
criterion_inventory_version: "criteria-library-v0.2"
criterion_ids:
  - OI-CONV-001
  - OI-CONV-002
  - OI-CONV-003
  - OI-CONV-004
  - OI-CONV-005
  - OI-CONV-006
  - OI-CONV-007
  - OI-CONV-008
  - OI-CONV-009
  - OI-CONV-010
  - OI-CONV-011
  - OI-CONV-012
  - OI-CONV-013
  - OI-CONV-014
evidence_refs:
  - OI-EVID-CONV-001
  - OI-EVID-CONV-002
  - OI-EVID-CONV-003
  - OI-EVID-CONV-004
  - OI-EVID-CONV-005
  - OI-EVID-CONV-006
  - OI-EVID-CONV-007
  - OI-EVID-CONV-008
  - OI-EVID-CONV-009
  - OI-EVID-CONV-010
  - OI-EVID-CONV-011
  - OI-EVID-CONV-012
  - OI-EVID-CONV-013
  - OI-EVID-CONV-014
required_scope_completed: false
desktop_cta_tested: true
mobile_cta_tested: true
form_submission_tested: true
form_receipt_verified: true
confirmation_verified: true
source_capture_verified: false
observed_indicator: 67.31
coverage_percent: 92.86
confidence_index: 0.9231
score_range: [58.93, 73.21]
publication_state: range_only
finding_ids:
  - OI-FIND-CONV-005
primary_package: OI-PKG-WEB-001
dependent_packages: []
roadmap_phase: "Phase 1 — Quick Wins"
unknowns:
  - OI-CONV-014
blocked_conditions: []
duplicate_check_passed: true
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-2026-014
```

## 11. Executive-safe statement

> The reviewed conversion paths provide a functional baseline through visible estimate actions, working phone and form routes, and a verified confirmation state. The estimate form captures basic contact information but leaves material project-context gaps, while lead-source retention could not be verified. The current evidence therefore supports a range of 58.93–73.21 rather than a single official Conversion Infrastructure score. Validation and reviewed scope approval are required before implementation is authorized.

## 12. Regression assertions

This fixture passes only when:

- observed score equals `67.3077` before display rounding
- coverage equals `92.8571%` before display rounding
- confidence index equals `0.923076...` before display rounding
- defensible bounds equal `58.9286–73.2143` before display rounding
- the Conversion Infrastructure category retains its canonical 15% Operator Score weight
- all 14 criteria remain applicable and equally weighted
- unknown criteria remain inside applicable weight
- unknown criteria are not scored as zero
- confidence does not alter maturity anchors
- unresolved source-capture evidence forces `range_only`
- `OI-CONV-014` routes to validation rather than an unsupported negative finding
- the verified intake-context finding routes to exactly one primary package
- package routing does not authorize implementation
- publication and implementation authorization remain separate
- duplicate checks preserve conversion, automation, and analytics ownership boundaries
- all material outputs retain DecisionLedger traceability
- client language avoids unsupported lead, conversion, close-rate, revenue, ROI, or attribution-performance claims
