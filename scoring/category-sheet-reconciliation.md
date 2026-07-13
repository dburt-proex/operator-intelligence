# Category Sheet Reconciliation Control

Version: v0.1  
Stage alignment: Stage 3 — `scoring/`  
Status: Commercial v1.0 control

## Purpose

Define the mandatory reconciliation check for every category sheet before the scoring folder can be declared complete.

This control prevents category-level examples, weights, confidence calculations, publication states, and routing fields from drifting away from the canonical scoring methodology.

## Required source comparison

Each category sheet must be reconciled against:

- `scoring/category-sheets/index.md`
- `scoring/weights.md`
- `scoring/calculator-spec.md`
- `scoring/confidence-adjusted-scoring.md`
- `scoring/unknown-data-handling.md`
- its canonical fixture in `scoring/examples/`, when one exists
- its approved finding library in `framework/findings/`
- `framework/recommendation-index.md`
- the applicable publication standard

## Reconciliation record

Record the following for each category:

```yaml
category_key: ""
category_sheet: ""
category_weight_percent: null
canonical_weight_percent: null
criterion_count: null
fixture_path: null
observed_indicator: null
coverage_percent: null
confidence_index: null
score_range: []
publication_state: official|provisional|range_only|blocked
material_unknowns: []
finding_ids: []
primary_package: null
roadmap_phase: null
implementation_authorized: false
decisionledger_ref: ""
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
reviewed_at: ""
```

## Mandatory checks

A category passes reconciliation only when all conditions below are true.

### Weight integrity

- The category weight matches the canonical index and `scoring/weights.md`.
- The complete category set reconciles to 100%.
- No category sheet defines an independent weight override.

### Criterion integrity

- Every criterion uses the approved category prefix.
- Every criterion has exactly one weighted owner.
- Applicable, unknown, blocked, and not-applicable states follow the canonical rules.
- Unknown and blocked criteria remain inside applicable weight.
- Unknown is never converted to zero.

### Confidence integrity

- Confidence remains separate from maturity.
- The confidence index is numeric and reproducible.
- Approved confidence factors are used consistently.
- Confidence uncertainty is included in lower and upper bounds.
- High confidence on known evidence does not resolve material unknowns.

### Publication integrity

- A single official score is published only when the publication gates are satisfied.
- Material unknowns force `range_only` or `blocked` when they could materially change interpretation.
- Coverage alone does not authorize official publication.
- The sheet and its canonical fixture report the same observed indicator, coverage, confidence index, bounds, and publication state.

### Routing integrity

- Recommendations originate only from approved findings.
- Unknown evidence routes to validation before implementation.
- Each validated recommendation has exactly one primary package.
- Roadmap phase follows dependencies and prerequisite gates.
- Publication does not authorize implementation.
- `implementation_authorized` defaults to `false` unless a separate authorization event exists.

### Traceability integrity

Every material output must preserve:

```text
Evidence
→ Criterion
→ Category Result
→ Coverage
→ Confidence
→ Bounds
→ Publication State
→ Finding
→ Recommendation
→ Primary Package
→ Roadmap Phase
→ DecisionLedger
```

## Review states

### ALLOW

All mandatory checks pass and the category sheet matches its canonical sources.

### REVIEW

The category remains usable, but one or more non-blocking inconsistencies require correction before scoring completion.

### HALT

Use HALT when any of the following is present:

- weight mismatch
- unknown scored as zero
- confidence used to alter maturity
- incomplete or unreproducible bounds
- material unknown published as a single official score
- unsupported finding or package routing
- more than one primary package
- implementation treated as authorized by publication
- missing DecisionLedger traceability
- unsupported revenue, ROI, conversion, lead-loss, ranking, safety, compliance, or competitor-performance claim

## Completion gate

The `scoring/` folder cannot be marked complete until every category has an `ALLOW` reconciliation record and all registered regression fixtures pass.

Any unresolved `REVIEW` or `HALT` state remains visible in the scoring completion report and blocks commercial v1.0 scoring sign-off.
