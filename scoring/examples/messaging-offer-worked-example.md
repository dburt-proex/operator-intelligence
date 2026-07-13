# Messaging and Offer Clarity Worked Scoring Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `messaging_offer`  
Default Operator Score weight: 10%  
Status: Commercial v1.0 validation fixture

## 1. Purpose

Provide a reproducible Messaging and Offer Clarity category calculation that verifies separate criterion records, maturity scoring, evidence coverage, numeric confidence, uncertainty bounds, material-unknown treatment, governed finding routing, package ownership, roadmap phase, publication state, implementation authorization, and DecisionLedger traceability.

This fixture supplements `scoring/category-sheets/messaging-offer.md`. It does not replace the category contract.

## 2. Scenario

A local-service business has a directly reviewed homepage, three service pages, contact path, process copy, FAQ content, CRM stages, estimate follow-up records, lost-reason fields, and a documented referral process.

The entry offer is consistently presented as a free estimate. Core services and the next step are understandable, but outcome language is generic, differentiation is weak, local relevance is limited, and pricing factors are incomplete. Reactivation records were not provided, so `OI-OFFER-008` remains unknown.

All 18 criteria are applicable and equally weighted.

## 3. Criterion results

| Criterion | State | Score | Confidence | Factor | Defensible bound | Evidence reference |
|---|---|---:|---|---:|---|---|
| `OI-MSG-001` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-MSGO-001` homepage hero capture |
| `OI-MSG-002` | scored | 25 | medium | 0.75 | 12.5–37.5 | `OI-EVID-MSGO-002` claims inventory; differentiators not operationally verified |
| `OI-MSG-003` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-MSGO-003` three service-page copy review |
| `OI-MSG-004` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-MSGO-004` service description inventory |
| `OI-MSG-005` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-MSGO-005` homepage, CTA, and contact-path review |
| `OI-MSG-006` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-MSGO-006` visible process-section review |
| `OI-MSG-007` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-MSGO-007` FAQ sample; objection coverage incomplete |
| `OI-MSG-008` | scored | 25 | medium | 0.75 | 12.5–37.5 | `OI-EVID-MSGO-008` local-reference inventory; project proof incomplete |
| `OI-MSG-009` | scored | 25 | medium | 0.75 | 12.5–37.5 | `OI-EVID-MSGO-009` full-site claims sample; proof alignment incomplete |
| `OI-MSG-010` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-MSGO-010` service priorities confirmed by owner; financial corroboration unavailable |
| `OI-OFFER-001` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-MSGO-011` free-estimate offer across public and sales surfaces |
| `OI-OFFER-002` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-MSGO-012` service-page and proposal sample |
| `OI-OFFER-003` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-MSGO-013` FAQ and estimate-language review |
| `OI-OFFER-004` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-MSGO-014` CRM stages and process-owner interview |
| `OI-OFFER-005` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-MSGO-015` estimate follow-up templates and CRM records |
| `OI-OFFER-006` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-MSGO-016` lost-reason field and report review |
| `OI-OFFER-007` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-MSGO-017` documented referral request process |
| `OI-OFFER-008` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-MSGO-018` reactivation records requested but not provided |

## 4. Observed maturity calculation

```text
Known maturity total = 875
Scored criterion count = 17
Observed Category Score = 875 ÷ 17 = 51.470588...
Displayed observed indicator = 51.47
```

The unknown criterion is excluded from the observed point-score denominator because no maturity anchor is defensible. It remains inside applicable weight for coverage and range calculations.

## 5. Evidence coverage

```text
Scored applicable criteria = 17
Total applicable criteria = 18
Coverage = 17 ÷ 18 × 100 = 94.4444%
Displayed coverage = 94.44%
```

Coverage above 90% does not independently authorize `official` publication when a material offer-system criterion remains unresolved.

## 6. Confidence index

Ten scored criteria have high confidence and seven have medium confidence.

```text
Confidence factor total = (10 × 1.00) + (7 × 0.75) = 15.25
Category Confidence Index = 15.25 ÷ 17 = 0.897058...
Displayed confidence index = 0.8971
Confidence band = high
```

The high confidence index applies only to known evidence. It does not resolve `OI-OFFER-008`.

## 7. Confidence-adjusted bounds

For the seven medium-confidence criteria, apply ±12.5. High-confidence criteria retain their observed anchors. The unknown criterion contributes 0–100.

```text
Known lower-bound total = 875 - (7 × 12.5) = 787.5
Known upper-bound total = 875 + (7 × 12.5) = 962.5
Unknown lower-bound total = 0
Unknown upper-bound total = 100

Category Lower Bound = (787.5 + 0) ÷ 18 = 43.7500
Category Upper Bound = (962.5 + 100) ÷ 18 = 59.027777...
Displayed defensible range = 43.75–59.03
```

This range reflects evidence uncertainty and unresolved scope. It is not a statistical confidence interval.

## 8. Publication decision

```yaml
score_value: null
score_type: range
observed_indicator: 51.47
score_range: [43.75, 59.03]
coverage_percent: 94.44
confidence_index: 0.8971
confidence_band: high
publication_state: range_only
material_unknowns:
  - OI-OFFER-008 retention or reactivation path
review_state: REVIEW
```

The category remains `range_only` because the unresolved reactivation criterion is part of the applicable offer-system scope. The observed indicator must not be represented as an official score.

## 9. Finding and recommendation routing

The directly observed generic differentiation condition supports one governed finding:

```yaml
finding_id: OI-FIND-MSG-003
criterion_owner: OI-MSG-002
observation: "The reviewed homepage and service pages rely on broad quality and reliability language without a verified operational differentiator."
interpretation: "The current message does not give buyers a well-supported basis for distinguishing the business from comparable providers."
buyer_impact: "Buyers may need additional evidence to understand why this provider is a suitable choice."
confidence: medium
priority: medium
limitations:
  - "No traffic, lead, conversion, close-rate, revenue, market-demand, or ROI effect is inferred."
ledger_ref: OI-DL-2026-013
```

The unresolved reactivation criterion creates a validation requirement and does not create a negative finding by itself.

```yaml
validation_required: true
validation_criteria:
  - OI-OFFER-008
primary_package: OI-PKG-TRUST-001
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
implementation_authorized: false
```

Exactly one primary package is assigned because the verified weakness is unsupported differentiation. Implementation remains unauthorized until proof requirements, scope approval, and a superseding DecisionLedger event are complete.

## 10. DecisionLedger record

```yaml
category_key: messaging_offer
category_sheet_version: "0.1"
criterion_ids:
  - OI-MSG-001
  - OI-MSG-002
  - OI-MSG-003
  - OI-MSG-004
  - OI-MSG-005
  - OI-MSG-006
  - OI-MSG-007
  - OI-MSG-008
  - OI-MSG-009
  - OI-MSG-010
  - OI-OFFER-001
  - OI-OFFER-002
  - OI-OFFER-003
  - OI-OFFER-004
  - OI-OFFER-005
  - OI-OFFER-006
  - OI-OFFER-007
  - OI-OFFER-008
evidence_refs:
  - OI-EVID-MSGO-001
  - OI-EVID-MSGO-002
  - OI-EVID-MSGO-003
  - OI-EVID-MSGO-004
  - OI-EVID-MSGO-005
  - OI-EVID-MSGO-006
  - OI-EVID-MSGO-007
  - OI-EVID-MSGO-008
  - OI-EVID-MSGO-009
  - OI-EVID-MSGO-010
  - OI-EVID-MSGO-011
  - OI-EVID-MSGO-012
  - OI-EVID-MSGO-013
  - OI-EVID-MSGO-014
  - OI-EVID-MSGO-015
  - OI-EVID-MSGO-016
  - OI-EVID-MSGO-017
  - OI-EVID-MSGO-018
required_public_scope_completed: true
required_internal_scope_completed: false
service_priority_verified: true
observed_indicator: 51.47
coverage_percent: 94.44
confidence_index: 0.8971
score_range: [43.75, 59.03]
publication_state: range_only
finding_ids:
  - OI-FIND-MSG-003
primary_package: OI-PKG-TRUST-001
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
unknowns:
  - OI-OFFER-008
blocked_conditions: []
duplicate_check_passed: true
unsupported_claim_check_passed: true
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
ledger_ref: OI-DL-2026-013
```

## 11. Executive-safe statement

> The reviewed messaging clearly identifies the core services and free-estimate next step, while estimate follow-up and lost-reason controls are directly supported by records. Differentiation and local relevance remain only partially supported, and reactivation evidence was not provided. The current evidence therefore supports a range of 43.75–59.03 rather than a single official Messaging and Offer Clarity score. Validation and reviewed scope approval are required before implementation is authorized.

## 12. Regression assertions

This fixture passes only when:

- observed score equals `51.470588...` before display rounding
- coverage equals `94.4444%` before display rounding
- confidence index equals `0.897058...` before display rounding
- defensible bounds equal `43.7500–59.027777...` before display rounding
- the Messaging and Offer category retains its canonical 10% Operator Score weight
- all 18 criterion records remain distinct
- unknown criteria remain inside applicable weight
- unknown criteria are not scored as zero
- confidence does not alter maturity anchors
- unresolved reactivation evidence forces `range_only`
- `OI-OFFER-008` routes to validation rather than an unsupported negative finding
- `OI-FIND-MSG-003` routes to exactly one primary package
- package routing does not authorize implementation
- publication and implementation authorization remain separate
- all material outputs retain DecisionLedger traceability
- client language avoids unsupported traffic, lead, conversion, close-rate, revenue, market-demand, ROI, or competitor-performance claims
