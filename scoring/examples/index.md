# Scoring Regression Fixture Index

Version: v0.8 scoring validation registry  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Status: Commercial v1.0 control artifact

## 1. Purpose

Register canonical worked scoring fixtures and define the minimum contract each fixture must satisfy before it can be used to validate a category sheet, calculator implementation, quality-control review, or client-report example.

A fixture is a deterministic regression test, not a substitute for the governing category sheet.

## 2. Registered fixtures

| Category | Fixture | Validates |
|---|---|---|
| Trust | `scoring/examples/trust-worked-example.md` | criterion evidence, coverage, confidence index, uncertainty bounds, unknown handling, finding and package routing |
| Social | `scoring/examples/social-worked-example.md` | numeric confidence, provisional publication, material unknown treatment, DecisionLedger completeness |
| Automation | `scoring/examples/automation-worked-example.md` | 14-criterion calculation, confidence-adjusted range, validation-first routing, implementation authorization separation |
| AI Readiness | `scoring/examples/ai-readiness-worked-example.md` | use-case control states, prerequisite gates, range-only publication, validation routing, DecisionLedger traceability |
| Analytics | `scoring/examples/analytics-worked-example.md` | canonical 5% weight, 10-criterion calculation, confidence-adjusted range, attribution and outcome unknowns, validation-first routing |
| Website Structure and UX | `scoring/examples/website-worked-example.md` | canonical 10% weight, 12-criterion calculation, confidence-adjusted range, competitor-evidence unknown handling, governed finding and package routing |
| Messaging and Offer Clarity | `scoring/examples/messaging-offer-worked-example.md` | canonical 10% weight, 18-criterion calculation, numeric confidence, confidence-adjusted range, material reactivation unknown handling, one-primary-package routing, implementation authorization separation |
| Conversion Infrastructure | `scoring/examples/conversion-worked-example.md` | canonical 15% weight, 14-criterion calculation, numeric confidence, confidence-adjusted range, material attribution unknown handling, one-primary-package routing, implementation authorization separation |
| Local SEO | `scoring/examples/seo-worked-example.md` | canonical 15% weight, 16-criterion calculation, numeric confidence, provisional publication, citation unknown handling, one-primary-package routing, implementation authorization separation |
| Google Business Profile | `scoring/examples/gbp-worked-example.md` | canonical 10% weight, 12-criterion calculation, numeric confidence, provisional publication, governed peer-set unknown handling, one-primary-package routing, implementation authorization separation |
| Competitive Position | `scoring/examples/competitive-worked-example.md` | canonical 5% weight, 10-criterion calculation, numeric confidence, range-only publication, controlled search and content unknowns, one-primary-package routing, implementation authorization separation |

Unlisted category examples remain illustrative until they satisfy this contract and are added through a versioned repository change.

## 3. Required fixture contract

Every registered fixture must include:

- category key and applicable criterion inventory
- criterion-level state, anchor, confidence, factor, and evidence reference
- applicable and scored weight totals
- observed score calculation
- evidence coverage calculation
- numeric confidence index and band
- defensible lower and upper bounds
- publication state and score type
- visible unknown, blocked, and not-applicable treatment
- finding and recommendation outcome
- exactly one primary package when a validated recommendation is routed
- roadmap phase and prerequisites
- implementation authorization recorded separately
- complete DecisionLedger fixture
- executive-safe client statement
- regression assertions with expected values

## 4. Validation gates

A fixture must not be registered when:

- unknown or blocked criteria are scored as zero
- unresolved applicable weight is removed
- confidence changes the maturity score
- bounds cannot be reproduced
- publication state conflicts with coverage or material unknowns
- a recommendation is created directly from an unknown criterion
- package routing lacks a valid finding or assigns multiple primary packages
- publication is treated as implementation authorization
- evidence references or DecisionLedger traceability are missing
- client language contains unsupported revenue, ROI, conversion, lead-loss, safety, compliance, or competitor-performance claims

Any blocking failure requires `HALT` until the fixture or governing methodology is corrected.

## 5. Category-sheet integration

A category sheet using a registered fixture should:

1. link the fixture in its worked-example or cross-reference section
2. reproduce the same score, coverage, confidence, bounds, and publication state
3. preserve category-specific evidence and routing requirements
4. treat the fixture as a regression baseline when methodology changes

A fixture mismatch is a scoring-control failure and must be resolved before publication.

## 6. DecisionLedger minimum registration record

```yaml
fixture_path: ""
category_key: ""
methodology_version: ""
expected_observed_score: null
expected_coverage_percent: null
expected_confidence_index: null
expected_score_range: []
expected_publication_state: ""
unknown_criteria: []
expected_primary_package: null
expected_roadmap_phase: null
implementation_authorized: false
validation_state: ALLOW|REVIEW|HALT
reviewed_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 7. Cross references

- `scoring/calculator-spec.md`
- `scoring/confidence-adjusted-scoring.md`
- `scoring/unknown-data-handling.md`
- `scoring/category-sheets/index.md`
- `standards/quality-control-standard.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`
