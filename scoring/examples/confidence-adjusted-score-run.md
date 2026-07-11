# Confidence-Adjusted Operator Score Run Example

Version: v0.1 scoring execution example  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Example key: `OI-EX-SCORE-CONFIDENCE-001`  
Status: Synthetic methodology example for commercial v1.0 validation

## 1. Purpose

This file demonstrates how Operator Intelligence keeps maturity, evidence coverage, and confidence separate while using confidence adjustment as an internal review and prioritization aid.

The confidence-adjusted indicator in this example is not an official Operator Score, client grade, probability of success, or forecast. It must not replace the observed maturity score or conceal evidence limitations.

The company, evidence, and results below are synthetic.

## 2. Governing rule

```text
Maturity answers: How strong is the observed operating condition?
Confidence answers: How strongly does the evidence support that judgment?
Coverage answers: How much of the applicable assessment was evaluated?
```

A low-confidence score is not automatically a low maturity score. A high-confidence score is not automatically a strong maturity score.

Confidence must never be used to:

- raise a weak maturity score
- convert unknown into zero
- create false precision
- authorize publication that fails coverage or evidence gates
- imply financial, conversion, lead, or ROI certainty
- suppress the need for validation

## 3. Assessment header

```yaml
assessment_id: OI-ASSESS-EXAMPLE-003
client_name: Northline Exterior Services
client_status: synthetic_example
assessment_type: full_operator_assessment
methodology_version: "0.1"
weight_profile: OI-WEIGHT-DEFAULT-01
weights_frozen_before_scoring: true
publication_state: provisional
confidence_adjustment_use: internal_review_only
```

## 4. Confidence factors

The factors below are used only to create an internal evidence-support view.

| Confidence | Factor | Use |
|---|---:|---|
| High | 1.00 | Direct, current, sufficiently scoped evidence supports the selected anchor. |
| Medium | 0.75 | Evidence supports the direction, but one material validation surface remains incomplete. |
| Low | 0.50 | The result depends materially on limited samples, interview evidence, stale records, or indirect observation. |
| Unknown | 0.00 | Evidence is insufficient to support a maturity judgment. The criterion remains unknown, not zero. |

These factors are diagnostic controls, not changes to the approved category or Operator Score formula.

## 5. Category score register

| Category | Weight | Category score | Confidence | Weighted maturity contribution | Confidence factor | Confidence-adjusted indicator contribution |
|---|---:|---:|---|---:|---:|---:|
| Website structure and UX | 10% | 62 | High | 6.20 | 1.00 | 6.20 |
| Messaging and offer clarity | 10% | 58 | Medium | 5.80 | 0.75 | 4.35 |
| Conversion infrastructure | 15% | 54 | High | 8.10 | 1.00 | 8.10 |
| Local SEO | 15% | 47 | Medium | 7.05 | 0.75 | 5.2875 |
| Google Business Profile | 10% | 68 | High | 6.80 | 1.00 | 6.80 |
| Reputation and trust | 10% | 64 | High | 6.40 | 1.00 | 6.40 |
| Social presence | 5% | 42 | Low | 2.10 | 0.50 | 1.05 |
| Automation maturity | 10% | 50 | Medium | 5.00 | 0.75 | 3.75 |
| AI readiness | 5% | 38 | Low | 1.90 | 0.50 | 0.95 |
| Analytics and reporting | 5% | 45 | Medium | 2.25 | 0.75 | 1.6875 |
| Competitive position | 5% | 55 | Medium | 2.75 | 0.75 | 2.0625 |
| **Total** | **100%** |  |  | **54.35** |  | **46.6375** |

## 6. Official maturity calculation

```text
Operator Score = Σ(Category Score × Category Weight)
Operator Score = 54.35
Displayed maturity score = 54
```

The official maturity result remains `54`. Confidence factors do not alter it.

## 7. Internal confidence diagnostics

### 7.1 Confidence-adjusted indicator

```text
Confidence-Adjusted Indicator
= Σ(Weighted Maturity Contribution × Confidence Factor)
= 46.6375
= 46.64 internal display
```

Interpretation:

> The observed maturity result is 54.35, but the evidence-supported portion of that result is weaker in several categories. The 46.64 indicator flags review exposure; it is not a replacement score.

### 7.2 Weighted evidence-support index

```text
Weighted Evidence-Support Index
= Σ(Category Weight × Confidence Factor) × 100

= (45% × 1.00)
+ (45% × 0.75)
+ (10% × 0.50)

= 83.75%
```

This index shows the weighted strength of evidence supporting the category judgments. It does not measure maturity.

### 7.3 Confidence exposure

```text
Confidence Exposure = 100% - 83.75% = 16.25%
```

The exposure indicates how much weighted confidence support is missing relative to an all-high-confidence assessment.

## 8. Why publication is provisional

The assessment has complete criterion coverage, but material categories rely on medium- or low-confidence evidence.

```yaml
criterion_coverage: 100%
weighted_evidence_support: 83.75%
material_low_confidence_categories:
  - social
  - ai_readiness
material_medium_confidence_categories:
  - messaging_offer
  - local_seo
  - automation
  - analytics
  - competitive
publication_state: provisional
```

Publication is provisional because the score is calculable and broadly supported, but assertion strength must remain limited until the highest-impact confidence gaps are validated.

## 9. Validation priority register

Validation priority is based on category weight, decision materiality, confidence gap, and roadmap dependency. It is not based solely on the lowest score.

| Priority | Category | Current confidence | Missing validation | Decision affected |
|---:|---|---|---|---|
| 1 | Local SEO | Medium | Current indexation, Search Console, and controlled local-query evidence | Phase 2 visibility roadmap |
| 2 | Automation | Medium | Broader lead-record sample, follow-up task history, and failure monitoring | Phase 3 CRM and follow-up package |
| 3 | AI readiness | Low | Approved use-case inventory, data rules, review gates, escalation, and logs | Phase 4 authorization boundary |
| 4 | Analytics | Medium | Event validation, source-field accuracy, and reporting decision cadence | Phase 3 dashboard package |
| 5 | Competitive | Medium | Dated comparison across consistent competitors and buyer intents | Roadmap prioritization |
| 6 | Social | Low | Complete channel inventory and representative response sample | Lower-weight supporting work |

## 10. Finding treatment

Confidence affects assertion strength and validation routing, not whether an observed maturity gap is automatically severe.

| Finding condition | Allowed treatment |
|---|---|
| High-confidence observable weakness | May become a governed finding when all required fields pass. |
| Medium-confidence weakness | May become a finding using qualified language and a validation action where material. |
| Low-confidence weakness | Normally remains a validation-required candidate unless direct evidence supports a limited claim. |
| Unknown condition | Cannot become a negative finding solely because evidence is unavailable. |

Example:

```yaml
finding_id: OI-FIND-AI-004
criterion_id: OI-AI-004
maturity_score: 25
confidence: low
state: validation_required
observation: "General review expectations were described, but no approved use-case-specific review matrix was provided."
interpretation: "Available evidence is insufficient to confirm controlled customer-facing AI readiness."
business_impact: "Production authorization should remain withheld until review and escalation controls are documented and tested."
priority: high
package_route: null
roadmap_phase: "Phase 4 — Governed AI Enablement"
ledger_ref: OI-DL-EX-021
```

No implementation package is authorized from this record until the evidence and control prerequisites pass.

## 11. Executive-safe reporting

### Approved language

> The assessment produced an observed Operator Score of 54. Evidence coverage was complete, but several category judgments rely on medium- or low-confidence support. The score is therefore provisional. Validation should focus first on Local SEO, lead-management workflows, analytics, and AI governance controls before those areas drive final implementation decisions.

### Prohibited language

Do not state:

- the true score is 46.64
- the business is 83.75% reliable
- confidence adjustment predicts future performance
- the confidence gap represents lost revenue
- low confidence proves the underlying process is weak
- validation will produce a specific score increase

## 12. DecisionLedger records

```yaml
- ledger_ref: OI-DL-EX-020
  decision: "Publish observed Operator Score as provisional."
  evidence_refs: [OI-EV-EX-001, OI-EV-EX-012]
  rationale: "Coverage is complete, but material category judgments do not yet have uniformly high-confidence support."
  operator_score: 54.35
  confidence_adjusted_indicator: 46.6375
  weighted_evidence_support: 83.75
  publication_state: provisional
  review_state: REVIEW

- ledger_ref: OI-DL-EX-021
  decision: "Withhold customer-facing AI implementation routing."
  evidence_refs: [OI-EV-EX-011, OI-EV-EX-012]
  rationale: "AI readiness evidence is low confidence and required review, escalation, data, and audit controls are not fully verified."
  roadmap_phase: "Phase 4 — Governed AI Enablement"
  review_state: HALT
```

## 13. Validation checks

```yaml
maturity_confidence_separation: pass
unknown_to_zero_conversion: 0
confidence_factor_changes_official_score: false
confidence_indicator_client_grade: false
coverage_gate_passed: true
duplicate_signal_check: pass
unsupported_financial_claims: 0
decisionledger_traceability: pass
publication_state: provisional
```

## 14. Completion rule

This example is valid only when:

- the official Operator Score remains calculated from maturity and frozen category weights
- confidence is assigned from evidence quality
- coverage is calculated independently
- the confidence-adjusted indicator is labeled internal and non-official
- low confidence routes to validation rather than automatic failure
- unknown remains unknown
- findings retain qualified, evidence-safe language
- package routing remains blocked when prerequisites are not established
- publication state reflects material confidence limitations
- DecisionLedger records preserve the maturity result, confidence diagnostics, and authorization decision separately
