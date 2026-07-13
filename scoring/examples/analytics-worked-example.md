# Analytics Worked Scoring Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `analytics`  
Default Operator Score weight: 5%  
Status: Commercial v1.0 validation fixture

## 1. Purpose

Provide a reproducible Analytics category calculation that verifies maturity scoring, evidence coverage, confidence indexing, uncertainty bounds, material-unknown treatment, finding routing, package ownership, roadmap phase, publication state, implementation authorization, and DecisionLedger traceability.

This fixture supplements `scoring/category-sheets/analytics.md`. It does not replace the category contract.

## 2. Scenario

A local-service business has verifiable website analytics, Search Console access, form-event tracking, phone-click measurement, review monitoring, priority-page reporting, a recurring reporting cadence, and documented decision use.

Lead-source attribution and estimate-outcome reporting remain unverified. Three scored criteria have medium confidence because reconciliation, event coverage, or repeated-period evidence is incomplete.

All 10 criteria are applicable and equally weighted.

## 3. Criterion results

| Criterion | State | Score | Confidence | Factor | Defensible bound | Evidence reference |
|---|---|---:|---|---:|---|---|
| `OI-AN-001` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-AN-001` direct property access, tag review, and page test |
| `OI-AN-002` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-AN-002` Search Console ownership and property access |
| `OI-AN-003` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-AN-003` safe form-event test; secondary form coverage incomplete |
| `OI-AN-004` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-AN-004` phone-click event test; call-log reconciliation incomplete |
| `OI-AN-005` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-AN-005` governed lead-source rule and field history not supplied |
| `OI-AN-006` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-AN-006` estimate outcomes and status definitions not supplied |
| `OI-AN-007` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-AN-007` review tracker and response-completion report |
| `OI-AN-008` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-AN-008` priority-page report with source and date range |
| `OI-AN-009` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-AN-009` recurring reports; only one complete prior period supplied |
| `OI-AN-010` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-AN-010` meeting notes with decisions, owners, and due dates |

## 4. Observed maturity calculation

```text
Known maturity total = 450
Scored criterion count = 8
Observed Category Score = 450 ÷ 8 = 56.25
Displayed observed score = 56
```

Unknown criteria are excluded from the observed point-score denominator because no maturity anchor is defensible. They remain inside applicable weight for coverage and range calculations.

## 5. Evidence coverage

```text
Scored applicable criteria = 8
Total applicable criteria = 10
Coverage = 8 ÷ 10 × 100 = 80.00%
Displayed coverage = 80.0%
```

Coverage at 80% does not independently authorize `official` publication.

## 6. Confidence index

Five scored criteria have high confidence and three have medium confidence.

```text
Confidence factor total = (5 × 1.00) + (3 × 0.75) = 7.25
Category Confidence Index = 7.25 ÷ 8 = 0.90625
Displayed confidence index = 0.9063
Confidence band = high
```

The high confidence index applies only to known evidence. It does not resolve the two unknown criteria.

## 7. Confidence-adjusted bounds

For the three medium-confidence criteria, apply ±12.5. High-confidence criteria retain their observed anchors. Unknown criteria contribute 0–100.

```text
Known lower-bound total = 450 - (3 × 12.5) = 412.5
Known upper-bound total = 450 + (3 × 12.5) = 487.5
Unknown lower-bound total = 0
Unknown upper-bound total = 200

Category Lower Bound = (412.5 + 0) ÷ 10 = 41.25
Category Upper Bound = (487.5 + 200) ÷ 10 = 68.75
Displayed defensible range = 41.25–68.75
```

This range reflects evidence uncertainty and unresolved scope. It is not a statistical confidence interval.

## 8. Publication decision

```yaml
score_value: null
score_type: range
observed_indicator: 56
score_range: [41.25, 68.75]
coverage_percent: 80.0
confidence_index: 0.9063
confidence_band: high
publication_state: range_only
material_unknowns:
  - OI-AN-005 lead-source attribution
  - OI-AN-006 estimate-outcome reporting
review_state: REVIEW
```

`OI-AN-005` and `OI-AN-006` are material because unresolved attribution and outcome definitions could materially change the interpretation of reporting maturity. The category therefore remains `range_only` despite 80% coverage and high confidence on known evidence.

## 9. Finding and recommendation routing

The evidence supports one governed validation finding:

```yaml
finding_id: OI-FIND-AN-006
criterion_owner: OI-AN-005
observation: "A governed lead-source attribution rule and complete field history were not available across the reviewed records."
interpretation: "The available evidence does not establish consistent source attribution across inquiry records."
measurement_impact: "Channel comparison remains provisional because source capture and attribution consistency are not verified."
confidence: unknown
priority: high
limitations:
  - "CRM field definitions, attribution rules, and reconciled record history were unavailable."
ledger_ref: OI-DL-2026-011
```

Because the criterion is unknown, the finding routes first to validation rather than directly authorizing implementation.

```yaml
validation_required: true
primary_package: null
dependent_packages: []
roadmap_phase: "Phase 0 — Validation and Access"
implementation_authorized: false
```

After direct evidence validates a material weakness, a superseding DecisionLedger event may route remediation to exactly one approved primary package, normally the Operator Dashboard Pack or CRM and Follow-Up System according to the confirmed ownership boundary.

## 10. DecisionLedger record

```yaml
category_key: analytics
criterion_ids:
  - OI-AN-001
  - OI-AN-002
  - OI-AN-003
  - OI-AN-004
  - OI-AN-005
  - OI-AN-006
  - OI-AN-007
  - OI-AN-008
  - OI-AN-009
  - OI-AN-010
evidence_refs:
  - OI-EVID-AN-001
  - OI-EVID-AN-002
  - OI-EVID-AN-003
  - OI-EVID-AN-004
  - OI-EVID-AN-005
  - OI-EVID-AN-006
  - OI-EVID-AN-007
  - OI-EVID-AN-008
  - OI-EVID-AN-009
  - OI-EVID-AN-010
observed_indicator: 56
coverage_percent: 80.0
confidence_index: 0.9063
score_range: [41.25, 68.75]
publication_state: range_only
finding_ids:
  - OI-FIND-AN-006
primary_package: null
dependent_packages: []
roadmap_phase: "Phase 0 — Validation and Access"
unknowns:
  - OI-AN-005
  - OI-AN-006
blocked_conditions: []
duplicate_check_passed: true
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
ledger_ref: OI-DL-2026-011
```

## 11. Executive-safe statement

> Analytics maturity is supported by verified installation, core event tracking, reporting, and documented decision use across the reviewed scope. Lead-source attribution and estimate-outcome reporting remain unverified, so the current evidence supports a range of 41.25–68.75 rather than a single official category score. Validation is required before implementation routing or performance conclusions.

## 12. Regression assertions

This fixture passes only when:

- observed score equals `56.25` before display rounding
- coverage equals `80.00%`
- confidence index equals `0.90625` before display rounding
- defensible bounds equal `41.25–68.75`
- the Analytics category retains its canonical 5% Operator Score weight
- unknown criteria remain inside applicable weight
- unknown criteria are not scored as zero
- confidence does not alter maturity anchors
- unresolved attribution and outcome evidence force `range_only`
- the unknown finding routes to validation, not implementation
- no primary package is assigned before validation
- publication and implementation authorization remain separate
- all material outputs retain DecisionLedger traceability
- client language avoids unsupported traffic, lead, conversion, close-rate, revenue, or ROI claims
