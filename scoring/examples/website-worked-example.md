# Website Structure and UX Worked Scoring Example

Version: v0.1 regression fixture  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Category key: `website`  
Default Operator Score weight: 10%  
Status: Commercial v1.0 validation fixture

## 1. Purpose

Provide a reproducible Website Structure and UX category calculation that verifies maturity scoring, evidence coverage, numeric confidence, uncertainty bounds, material-unknown treatment, governed finding routing, package ownership, roadmap phase, publication state, implementation authorization, and DecisionLedger traceability.

This fixture supplements `scoring/category-sheets/website.md`. It does not replace the category contract.

## 2. Scenario

A local-service business has a public website with directly reviewed desktop and mobile pages, navigation, contact paths, phone links, service-page inventory, and footer behavior.

Competitor comparison required to evaluate differentiation remains unavailable. Four scored criteria have medium confidence because device coverage, page sampling, or repeated path testing is incomplete.

All 12 criteria are applicable and equally weighted.

## 3. Criterion results

| Criterion | State | Score | Confidence | Factor | Defensible bound | Evidence reference |
|---|---|---:|---|---:|---|---|
| `OI-WEB-001` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-WEB-001` desktop and mobile above-fold screenshots |
| `OI-WEB-002` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-WEB-002` hero, footer, and contact-page service-area review |
| `OI-WEB-003` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-WEB-003` desktop and mobile navigation tests |
| `OI-WEB-004` | scored | 25 | high | 1.00 | 25–25 | `OI-EVID-WEB-004` service list and URL inventory comparison |
| `OI-WEB-005` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-WEB-005` representative mobile interaction test; secondary browser not tested |
| `OI-WEB-006` | scored | 75 | high | 1.00 | 75–75 | `OI-EVID-WEB-006` header, footer, and tap-to-call verification |
| `OI-WEB-007` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-WEB-007` homepage-to-contact path test |
| `OI-WEB-008` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-WEB-008` sitemap and internal-link sample; full crawl incomplete |
| `OI-WEB-009` | scored | 50 | medium | 0.75 | 37.5–62.5 | `OI-EVID-WEB-009` key-page hierarchy review; secondary service pages sampled |
| `OI-WEB-010` | scored | 25 | medium | 0.75 | 12.5–37.5 | `OI-EVID-WEB-010` service-page review; objection and process coverage incomplete |
| `OI-WEB-011` | unknown | — | unknown | 0.00 | 0–100 | `OI-EVID-WEB-011` representative competitor comparison not completed |
| `OI-WEB-012` | scored | 50 | high | 1.00 | 50–50 | `OI-EVID-WEB-012` footer screenshot and link test |

## 4. Observed maturity calculation

```text
Known maturity total = 550
Scored criterion count = 11
Observed Category Score = 550 ÷ 11 = 50.0000
Displayed observed indicator = 50
```

The unknown criterion is excluded from the observed point-score denominator because no maturity anchor is defensible. It remains inside applicable weight for coverage and range calculations.

## 5. Evidence coverage

```text
Scored applicable criteria = 11
Total applicable criteria = 12
Coverage = 11 ÷ 12 × 100 = 91.6667%
Displayed coverage = 91.67%
```

Coverage above 90% does not independently authorize `official` publication when a material criterion remains unresolved.

## 6. Confidence index

Seven scored criteria have high confidence and four have medium confidence.

```text
Confidence factor total = (7 × 1.00) + (4 × 0.75) = 10.00
Category Confidence Index = 10.00 ÷ 11 = 0.909090...
Displayed confidence index = 0.9091
Confidence band = high
```

The high confidence index applies only to known evidence. It does not resolve `OI-WEB-011`.

## 7. Confidence-adjusted bounds

For the four medium-confidence criteria, apply ±12.5. High-confidence criteria retain their observed anchors. The unknown criterion contributes 0–100.

```text
Known lower-bound total = 550 - (4 × 12.5) = 500
Known upper-bound total = 550 + (4 × 12.5) = 600
Unknown lower-bound total = 0
Unknown upper-bound total = 100

Category Lower Bound = (500 + 0) ÷ 12 = 41.6667
Category Upper Bound = (600 + 100) ÷ 12 = 58.3333
Displayed defensible range = 41.67–58.33
```

This range reflects evidence uncertainty and unresolved scope. It is not a statistical confidence interval.

## 8. Publication decision

```yaml
score_value: null
score_type: range
observed_indicator: 50
score_range: [41.67, 58.33]
coverage_percent: 91.67
confidence_index: 0.9091
confidence_band: high
publication_state: range_only
material_unknowns:
  - OI-WEB-011 differentiation relative to representative competitors
review_state: REVIEW
```

The category remains `range_only` because the unresolved differentiation criterion could materially affect the category interpretation. The observed indicator must not be represented as an official score.

## 9. Finding and recommendation routing

The directly observed service-page architecture supports one governed finding:

```yaml
finding_id: OI-FIND-WEB-004
criterion_owner: OI-WEB-004
observation: "Multiple core services are represented within an overly broad page rather than distinct, buyer-oriented service pages."
interpretation: "The verified page inventory does not provide sufficient structural depth for several core services."
buyer_impact: "Buyers may receive limited service-specific context, while high-intent service discovery remains constrained."
confidence: high
priority: high
limitations:
  - "No traffic, lead, conversion, ranking, revenue, or competitor-performance effect is inferred."
ledger_ref: OI-DL-2026-012
```

The unresolved differentiation criterion creates a separate validation requirement and does not create a negative finding by itself.

```yaml
validation_required: true
validation_criteria:
  - OI-WEB-011
primary_package: OI-PKG-SEO-001
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
implementation_authorized: false
```

Exactly one primary package is assigned because the verified weakness is service-page architecture. Implementation remains unauthorized until review, dependency validation, scope approval, and a superseding DecisionLedger event are complete.

## 10. DecisionLedger record

```yaml
category_key: website
category_sheet_version: "0.1"
criterion_ids:
  - OI-WEB-001
  - OI-WEB-002
  - OI-WEB-003
  - OI-WEB-004
  - OI-WEB-005
  - OI-WEB-006
  - OI-WEB-007
  - OI-WEB-008
  - OI-WEB-009
  - OI-WEB-010
  - OI-WEB-011
  - OI-WEB-012
evidence_refs:
  - OI-EVID-WEB-001
  - OI-EVID-WEB-002
  - OI-EVID-WEB-003
  - OI-EVID-WEB-004
  - OI-EVID-WEB-005
  - OI-EVID-WEB-006
  - OI-EVID-WEB-007
  - OI-EVID-WEB-008
  - OI-EVID-WEB-009
  - OI-EVID-WEB-010
  - OI-EVID-WEB-011
  - OI-EVID-WEB-012
required_scope_completed: false
desktop_tested: true
mobile_tested: true
navigation_tested: true
contact_path_tested: true
observed_indicator: 50
coverage_percent: 91.67
confidence_index: 0.9091
score_range: [41.67, 58.33]
publication_state: range_only
finding_ids:
  - OI-FIND-WEB-004
primary_package: OI-PKG-SEO-001
dependent_packages: []
roadmap_phase: "Phase 2 — Growth Foundation"
unknowns:
  - OI-WEB-011
blocked_conditions: []
duplicate_check_passed: true
implementation_authorized: false
review_state: REVIEW
reviewed_by: ""
ledger_ref: OI-DL-2026-012
```

## 11. Executive-safe statement

> The reviewed website provides functional navigation, contact access, and a usable baseline across desktop and mobile. Core service-page architecture remains limited, and representative competitor comparison was not completed. The current evidence therefore supports a range of 41.67–58.33 rather than a single official Website Structure and UX score. Validation and reviewed scope approval are required before implementation is authorized.

## 12. Regression assertions

This fixture passes only when:

- observed score equals `50.0000`
- coverage equals `91.6667%` before display rounding
- confidence index equals `0.909090...` before display rounding
- defensible bounds equal `41.6667–58.3333` before display rounding
- the Website category retains its canonical 10% Operator Score weight
- unknown criteria remain inside applicable weight
- unknown criteria are not scored as zero
- confidence does not alter maturity anchors
- unresolved competitor-comparison evidence forces `range_only`
- `OI-WEB-011` routes to validation rather than an unsupported negative finding
- the verified service-page architecture finding routes to exactly one primary package
- package routing does not authorize implementation
- publication and implementation authorization remain separate
- all material outputs retain DecisionLedger traceability
- client language avoids unsupported redesign, traffic, lead, ranking, conversion, revenue, ROI, or competitor-performance claims
