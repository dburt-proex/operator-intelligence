# Automation Worked Scoring Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `automation`  
Status: Commercial v1.0 validation fixture

## 1. Purpose

Provide a reproducible Automation category calculation that verifies maturity scoring, evidence coverage, confidence indexing, uncertainty bounds, material-unknown treatment, finding routing, package ownership, roadmap phase, publication state, and DecisionLedger traceability.

This fixture supplements `scoring/category-sheets/automation.md`. It does not replace the category contract.

## 2. Scenario

A local-service business uses one primary lead tracker and has functional form notifications, basic ownership, defined pipeline stages, follow-up reminders, estimate outcomes, customer records, handoff notes, and controlled response templates.

Evidence remains incomplete for missed-inquiry recovery and the recurring operating review. Four scored criteria have medium confidence because workflow monitoring, record reconciliation, or test coverage is incomplete.

All 14 criteria are applicable and equally weighted.

## 3. Criterion results

| Criterion | State | Score | Confidence | Factor | Defensible bound | Evidence reference |
|---|---|---:|---|---:|---|---|
| `OI-AUTO-001` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-AUTO-001` channel inventory and tracker records |
| `OI-AUTO-002` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-AUTO-002` safe form test; failure monitoring unverified |
| `OI-AUTO-003` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-AUTO-003` confirmation test and message record |
| `OI-AUTO-004` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-AUTO-004` ownership field and sample records |
| `OI-AUTO-005` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-AUTO-005` pipeline stages and recent records |
| `OI-AUTO-006` | scored | 75 | medium | 0.75 | 62.5–87.5 | `OI-EVID-AUTO-006` reminder rules; exception sample incomplete |
| `OI-AUTO-007` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-AUTO-007` estimate status and lost-reason fields |
| `OI-AUTO-008` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-AUTO-008` review-request workflow and run history |
| `OI-AUTO-009` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-AUTO-009` missed-call and social-message recovery not verified |
| `OI-AUTO-010` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-AUTO-010` customer records; history sample partially reconciled |
| `OI-AUTO-011` | scored | 25 | high | 1.00 | 25–25 | `OI-EVID-AUTO-011` seasonal list without controlled cadence |
| `OI-AUTO-012` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-AUTO-012` handoff SOP and role assignment |
| `OI-AUTO-013` | scored | 75 | medium | 0.75 | 62.5–87.5 | `OI-EVID-AUTO-013` approved templates; version review incomplete |
| `OI-AUTO-014` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-AUTO-014` recurring operating review not supplied |

## 4. Observed maturity calculation

```text
Known maturity total = 700
Scored criterion count = 12
Observed Category Score = 700 ÷ 12 = 58.3333
Displayed observed score = 58
```

Unknown criteria are excluded from the observed point-score denominator because no maturity anchor is defensible. They remain inside applicable weight for coverage and range calculations.

## 5. Evidence coverage

```text
Scored applicable criteria = 12
Total applicable criteria = 14
Coverage = 12 ÷ 14 × 100 = 85.7143%
Displayed coverage = 85.7%
```

Coverage above 80% does not independently authorize `official` publication.

## 6. Confidence index

Eight scored criteria have high confidence and four have medium confidence.

```text
Confidence factor total = (8 × 1.00) + (4 × 0.75) = 11.00
Category Confidence Index = 11.00 ÷ 12 = 0.9167
Confidence band = high
```

The high confidence index applies only to known evidence. It does not resolve the two unknown criteria.

## 7. Confidence-adjusted bounds

For the four medium-confidence criteria, apply ±12.5. High-confidence criteria retain their observed anchors. Unknown criteria contribute 0–100.

```text
Known lower-bound total = 700 - (4 × 12.5) = 650
Known upper-bound total = 700 + (4 × 12.5) = 750
Unknown lower-bound total = 0
Unknown upper-bound total = 200

Category Lower Bound = (650 + 0) ÷ 14 = 46.4286
Category Upper Bound = (750 + 200) ÷ 14 = 67.8571
Displayed defensible range = 46.43–67.86
```

This range reflects evidence uncertainty and unresolved scope. It is not a statistical confidence interval.

## 8. Publication decision

```yaml
score_value: null
score_type: range
observed_indicator: 58
score_range: [46.43, 67.86]
coverage_percent: 85.7
confidence_index: 0.9167
confidence_band: high
publication_state: range_only
material_unknowns:
  - OI-AUTO-009 missed-inquiry recovery
  - OI-AUTO-014 operating-review visibility
review_state: REVIEW
```

`OI-AUTO-009` is material because unverified recovery controls could materially change the interpretation of inquiry-handling reliability. The category therefore remains `range_only` despite coverage above 80% and high confidence on known evidence.

## 9. Finding and recommendation routing

The evidence supports one governed finding:

```yaml
finding_id: OI-FIND-AUTO-009
criterion_owner: OI-AUTO-009
observation: "Missed-call and social-message recovery could not be verified across the reviewed scope."
interpretation: "The available evidence does not establish a reliable recovery path for missed inquiries."
business_impact: "Unrecovered inquiries may remain unassigned or unresolved; the frequency and commercial effect are not established."
confidence: unknown
priority: high
limitations:
  - "Internal call-routing and inbox workflow evidence was unavailable."
ledger_ref: OI-DL-2026-010
```

Because the criterion is unknown, the finding routes first to validation rather than directly authorizing implementation.

```yaml
validation_required: true
primary_package: null
dependent_packages: []
roadmap_phase: "Phase 0 — Validation and Access"
implementation_authorized: false
```

After direct evidence validates a material weakness, a superseding DecisionLedger event may route remediation to exactly one approved primary package, normally `OI-PKG-CRM-001`.

## 10. DecisionLedger record

```yaml
category_key: automation
criterion_ids:
  - OI-AUTO-001
  - OI-AUTO-002
  - OI-AUTO-003
  - OI-AUTO-004
  - OI-AUTO-005
  - OI-AUTO-006
  - OI-AUTO-007
  - OI-AUTO-008
  - OI-AUTO-009
  - OI-AUTO-010
  - OI-AUTO-011
  - OI-AUTO-012
  - OI-AUTO-013
  - OI-AUTO-014
evidence_refs:
  - OI-EVID-AUTO-001
  - OI-EVID-AUTO-002
  - OI-EVID-AUTO-003
  - OI-EVID-AUTO-004
  - OI-EVID-AUTO-005
  - OI-EVID-AUTO-006
  - OI-EVID-AUTO-007
  - OI-EVID-AUTO-008
  - OI-EVID-AUTO-009
  - OI-EVID-AUTO-010
  - OI-EVID-AUTO-011
  - OI-EVID-AUTO-012
  - OI-EVID-AUTO-013
  - OI-EVID-AUTO-014
observed_indicator: 58
coverage_percent: 85.7
confidence_index: 0.9167
score_range: [46.43, 67.86]
publication_state: range_only
finding_ids:
  - OI-FIND-AUTO-009
primary_package: null
dependent_packages: []
roadmap_phase: "Phase 0 — Validation and Access"
unknowns:
  - OI-AUTO-009
  - OI-AUTO-014
blocked_conditions: []
duplicate_check_passed: true
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
ledger_ref: OI-DL-2026-010
```

## 11. Executive-safe statement

> Automation maturity is supported by a functional lead-management baseline across the reviewed records. Missed-inquiry recovery and recurring operating visibility remain unverified, so the current evidence supports a range of 46.43–67.86 rather than a single official category score. Validation is required before implementation routing.

## 12. Regression assertions

This fixture passes only when:

- observed score equals `58.3333` before display rounding
- coverage equals `85.7143%` before display rounding
- confidence index equals `0.9167`
- defensible bounds equal `46.4286–67.8571` before display rounding
- unknown criteria remain inside applicable weight
- unknown criteria are not scored as zero
- confidence does not alter maturity anchors
- `OI-AUTO-009` forces `range_only` while material and unresolved
- the unknown finding routes to validation, not implementation
- no primary package is assigned before validation
- publication and implementation authorization remain separate
- all material outputs retain DecisionLedger traceability
- client language avoids unsupported lead-loss, revenue, capacity, savings, or ROI claims
