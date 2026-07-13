# Category Sheet Reconciliation Status

Version: v0.1 commercial v1.0 scoring control  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/`  
Status: Active reconciliation register

## Purpose

Provide one controlled view of category-sheet readiness without treating file presence as methodology approval.

This register supplements:

- `scoring/category-sheets/index.md`
- `scoring/category-sheet-reconciliation.md`
- `scoring/examples/index.md`
- `scoring/calculator-spec.md`
- `standards/publication-standard.md`

A category is not eligible for commercial scoring use until its sheet, regression fixture, calculations, publication controls, routing, and DecisionLedger record reconcile to an `ALLOW` result.

## Canonical category inventory

| Category key | Sheet | Operator Score weight | Registered regression fixture | Reconciliation state |
|---|---|---:|---|---|
| `website` | `scoring/category-sheets/website.md` | 10% | none registered | `REVIEW` |
| `messaging_offer` | `scoring/category-sheets/messaging-offer.md` | 10% | none registered | `REVIEW` |
| `conversion` | `scoring/category-sheets/conversion.md` | 15% | none registered | `REVIEW` |
| `seo` | `scoring/category-sheets/seo.md` | 15% | none registered | `REVIEW` |
| `gbp` | `scoring/category-sheets/gbp.md` | 10% | none registered | `REVIEW` |
| `trust` | `scoring/category-sheets/trust.md` | 10% | `scoring/examples/trust-worked-example.md` | `REVIEW` |
| `social` | `scoring/category-sheets/social.md` | 5% | `scoring/examples/social-worked-example.md` | `REVIEW` |
| `automation` | `scoring/category-sheets/automation.md` | 10% | `scoring/examples/automation-worked-example.md` | `REVIEW` |
| `ai_readiness` | `scoring/category-sheets/ai-readiness.md` | 5% | `scoring/examples/ai-readiness-worked-example.md` | `REVIEW` |
| `analytics` | `scoring/category-sheets/analytics.md` | 5% | `scoring/examples/analytics-worked-example.md` | `REVIEW` |
| `competitive` | `scoring/category-sheets/competitive.md` | 5% | none registered | `REVIEW` |

Canonical weight total: **100%**.

`REVIEW` means the artifact is present or referenced but has not yet received a complete, current reconciliation record proving all commercial v1.0 gates pass. It must not be interpreted as failure or approval.

## Required reconciliation record

Create one record per category using this schema:

```yaml
category_key: ""
category_sheet_path: ""
category_sheet_version: ""
canonical_weight_percent: null
declared_weight_percent: null
criterion_inventory_complete: false
criterion_count: null
registered_fixture_path: null
fixture_values_match: false
observed_score: null
coverage_percent: null
confidence_index: null
score_range: []
publication_state: ""
material_unknowns: []
finding_refs: []
recommendation_refs: []
primary_package: null
roadmap_phase: null
implementation_authorized: false
decision_ledger_ref: ""
validation_codes: []
reconciliation_state: ALLOW|REVIEW|HALT
reviewed_by: ""
approved_by: ""
```

## ALLOW gate

A category may move to `ALLOW` only when all conditions pass:

1. The declared weight equals the canonical weight.
2. Every governed criterion is mapped exactly once.
3. The sheet contains all required contract sections.
4. Evidence scope, anchors, confidence rules, unknown treatment, and duplicate boundaries are testable.
5. A registered regression fixture exists and recalculates exactly.
6. Coverage, confidence index, bounds, and publication state are reproducible.
7. Material unknowns remain inside applicable weight and are not scored as zero.
8. Findings use governed IDs or route to a documented methodology gap.
9. Every validated recommendation has exactly one primary package and a roadmap phase.
10. Publication is separate from implementation authorization.
11. DecisionLedger traceability is complete.
12. Client language avoids unsupported revenue, ROI, conversion, ranking, lead-loss, safety, compliance, and competitor-performance claims.

## State rules

### `ALLOW`

All reconciliation requirements pass. The approved sheet version may support governed scoring use.

### `REVIEW`

The sheet is usable only as controlled draft guidance because one or more reconciliation checks remain incomplete, unverified, or awaiting approval.

### `HALT`

A blocking conflict exists, including:

- weight mismatch
- missing or duplicate criterion ownership
- unreproducible fixture values
- unknown criteria converted to zero
- confidence altering maturity
- unsupported point-score publication
- recommendation without a governed finding
- multiple primary packages
- missing DecisionLedger traceability
- implementation treated as automatically authorized
- unsupported executive claim

`HALT` blocks category publication until corrected and re-reviewed.

## Completion rule

The `scoring/` folder cannot be marked commercially complete until:

- all 11 categories have registered regression fixtures
- all 11 reconciliation records resolve to `ALLOW`
- canonical weights total 100%
- calculator-level regression runs pass
- no unresolved blocking validation code remains

Status changes require a versioned repository edit and a DecisionLedger reference. File presence alone never changes a reconciliation state.