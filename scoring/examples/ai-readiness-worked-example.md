# AI Readiness Worked Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `ai-readiness`  
Status: Commercial v1.0 scoring fixture

## 1. Purpose

Provide a reproducible AI Readiness score run that verifies criterion states, evidence coverage, confidence, uncertainty bounds, control-state routing, prerequisite handling, publication state, package routing, and DecisionLedger traceability.

This fixture is a scoring regression test. It does not authorize AI implementation.

## 2. Scenario

A service business is considering a bounded internal AI intake assistant. Ten readiness criteria are directly supported. Privacy and escalation controls cannot yet be verified.

All 12 criteria remain applicable. `OI-AI-008` and `OI-AI-010` are `unknown`; neither is scored as zero or removed from applicable weight.

## 3. Criterion-level inputs

| Criterion | State | Anchor | Confidence | Factor | Evidence reference |
|---|---|---:|---|---:|---|
| `OI-AI-001` | scored | 75 | high | 1.00 | `OI-EVID-AI-001` workflow map and owner |
| `OI-AI-002` | scored | 50 | high | 1.00 | `OI-EVID-AI-002` CRM schema sample |
| `OI-AI-003` | scored | 75 | high | 1.00 | `OI-EVID-AI-003` bounded use-case brief |
| `OI-AI-004` | scored | 50 | high | 1.00 | `OI-EVID-AI-004` human approval workflow |
| `OI-AI-005` | scored | 50 | high | 1.00 | `OI-EVID-AI-005` allowed and blocked topics |
| `OI-AI-006` | scored | 50 | high | 1.00 | `OI-EVID-AI-006` approved source inventory |
| `OI-AI-007` | scored | 50 | high | 1.00 | `OI-EVID-AI-007` output and approval log sample |
| `OI-AI-008` | unknown | — | unknown | — | `OI-EVID-AI-008` privacy and access rules unavailable |
| `OI-AI-009` | scored | 75 | high | 1.00 | `OI-EVID-AI-009` risk-ranked pilot plan |
| `OI-AI-010` | unknown | — | unknown | — | `OI-EVID-AI-010` escalation route not verified |
| `OI-AI-011` | scored | 50 | high | 1.00 | `OI-EVID-AI-011` versioned prompt standard |
| `OI-AI-012` | scored | 50 | high | 1.00 | `OI-EVID-AI-012` QA sample and correction log |

Known score total:

```text
75 + 50 + 75 + 50 + 50 + 50 + 50 + 75 + 50 + 50 = 575
```

## 4. Score calculation

```text
Applicable Criterion Count = 12
Scored Applicable Criterion Count = 10
Known Score Total = 575

Observed Category Score = 575 ÷ 10
Observed Category Score = 57.50

Coverage = 10 ÷ 12 × 100
Coverage = 83.33%
```

The observed category score describes only the ten scored criteria. It is not an official single-value category score because two material criteria remain unknown.

## 5. Confidence calculation

All scored criteria are supported by direct evidence and use confidence factor `1.00`.

```text
Confidence Index = Σ confidence factors ÷ scored criterion count
Confidence Index = 10.00 ÷ 10
Confidence Index = 1.0000
Confidence Band = high
```

Confidence remains separate from maturity. High confidence in the known evidence does not resolve the two unknown controls.

## 6. Defensible score range

Equal applicable weighting is used across all 12 criteria.

Lower bound assigns no maturity value to unresolved criteria without converting them to scored zeros:

```text
Lower Bound = 575 ÷ 12
Lower Bound = 47.92
```

Upper bound allows each unresolved criterion its maximum possible anchor:

```text
Upper Bound = (575 + 100 + 100) ÷ 12
Upper Bound = 64.58
```

Published score representation:

```yaml
score_value: null
observed_indicator: 57.50
score_type: range
score_range: [47.92, 64.58]
coverage_percent: 83.33
confidence_index: 1.0000
confidence_band: high
publication_state: range_only
```

## 7. Material unknown treatment

`OI-AI-008` affects privacy, permissions, retention, sharing, and prohibited-data handling.

`OI-AI-010` affects exception escalation, accountable ownership, and safe failure handling.

These unknowns can materially change both readiness interpretation and use-case authorization. Therefore:

- they remain inside applicable weight
- they are not scored as zero
- they prevent `official` publication
- they require validation before package authorization
- customer-facing deployment remains `HALT`
- bounded internal preparation remains `REVIEW` only

## 8. Finding and routing outcome

The unknown criteria do not directly create implementation findings. They create validation requirements.

```yaml
finding_ids: []
validation_required:
  - OI-AI-008 privacy and access control review
  - OI-AI-010 escalation-path verification
control_state:
  internal_assistance: REVIEW
  customer_facing_execution: HALT
primary_package: null
dependent_packages: []
roadmap_phase: Phase 0 — Validation and Access
implementation_authorized: false
```

After validation, supported findings may route through approved `OI-FIND-AI-*` records. Exactly one primary package may then be selected if prerequisites pass.

## 9. DecisionLedger fixture

```yaml
category_key: ai-readiness
criterion_ids:
  - OI-AI-001
  - OI-AI-002
  - OI-AI-003
  - OI-AI-004
  - OI-AI-005
  - OI-AI-006
  - OI-AI-007
  - OI-AI-008
  - OI-AI-009
  - OI-AI-010
  - OI-AI-011
  - OI-AI-012
use_case_id: OI-USE-AI-001
evidence_refs:
  - OI-EVID-AI-001
  - OI-EVID-AI-002
  - OI-EVID-AI-003
  - OI-EVID-AI-004
  - OI-EVID-AI-005
  - OI-EVID-AI-006
  - OI-EVID-AI-007
  - OI-EVID-AI-009
  - OI-EVID-AI-011
  - OI-EVID-AI-012
observed_indicator: 57.50
coverage_percent: 83.33
confidence_index: 1.0000
score_range: [47.92, 64.58]
publication_state: range_only
observation: "Ten readiness controls were verified; privacy/access and escalation controls remain unverified."
interpretation: "The evidence supports bounded internal assistance under review, not autonomous or customer-facing execution."
business_impact: "Unverified control boundaries increase the risk of inappropriate data handling or unowned exceptions; operational effect requires validation."
confidence: high
priority: high
control_state: REVIEW
finding_ids: []
prerequisites:
  - verify OI-AI-008
  - verify OI-AI-010
primary_package: null
dependent_packages: []
roadmap_phase: Phase 0 — Validation and Access
unknowns:
  - OI-AI-008
  - OI-AI-010
blocked_conditions: []
duplicate_check_passed: true
implementation_authorized: false
reviewed_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 10. Executive-safe statement

> The reviewed evidence supports a workable foundation for bounded internal AI assistance. Privacy, access, and escalation controls require validation before customer-facing or autonomous use can be considered.

Do not state that the business is AI-ready without the range, coverage, unknowns, control state, and use-case boundary.

## 11. Regression assertions

This fixture passes only when:

- observed score equals `57.50`
- coverage equals `83.33%`
- confidence index equals `1.0000`
- lower bound equals `47.92`
- upper bound equals `64.58`
- publication state equals `range_only`
- `OI-AI-008` and `OI-AI-010` remain unknown
- internal assistance remains `REVIEW`
- customer-facing execution remains `HALT`
- no finding or package is created directly from an unknown criterion
- implementation authorization remains `false`
- DecisionLedger traceability is present

## 12. Cross references

- `scoring/category-sheets/ai-readiness.md`
- `scoring/confidence-adjusted-scoring.md`
- `scoring/unknown-data-handling.md`
- `scoring/calculator-spec.md`
- `framework/findings/ai-readiness-findings.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`
