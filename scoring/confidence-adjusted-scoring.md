# Operator Intelligence Confidence-Adjusted Scoring

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file defines how confidence affects score interpretation, uncertainty ranges, publication status, and validation without converting weak evidence into an automatic performance penalty.

The primary maturity score describes the observed condition. Confidence describes how strongly the evidence supports that score.

## v1.0 connection

Commercial v1.0 requires scores that are both useful and honest about evidence limitations.

This file strengthens v1.0 readiness by providing:

- confidence factors
- criterion uncertainty bounds
- category and Operator Score confidence indexes
- publication-state controls
- score-range behavior
- high-impact and low-confidence escalation
- report wording
- recalculation and audit rules

## Core principles

1. Confidence is not performance.
2. Low confidence must not push a maturity score toward zero.
3. Unknown data must not receive a confidence-discounted numeric score.
4. Confidence affects uncertainty, admissibility, and language.
5. Strong evidence may narrow a range but cannot increase the underlying maturity score.
6. High-impact, low-confidence conditions route to validation, REVIEW, or HALT rather than false certainty.
7. Confidence must derive from evidence quality, coverage, recency, comparability, and test completeness.
8. Confidence adjustments must be reproducible from stored score objects.

## Confidence levels and factors

| Confidence | Factor | Use when |
|---|---:|---|
| `high` | 1.00 | Direct, current, relevant evidence or tested operation supports the score |
| `medium` | 0.75 | Evidence supports the pattern, but material context or test coverage is incomplete |
| `low` | 0.50 | Evidence is limited, indirect, client-recalled, narrow, or materially incomplete |
| `unknown` | 0.00 | Evidence cannot support a score |

The factor is used to calculate confidence indexes. It is not multiplied by the maturity score.

## Criterion uncertainty bounds

For a scored criterion, assign bounds according to confidence:

| Confidence | Lower bound | Upper bound |
|---|---|---|
| High | `score` | `score` |
| Medium | `score - 12.5` | `score + 12.5` |
| Low | `score - 25` | `score + 25` |
| Unknown | Not scoreable | Not scoreable |

Clamp bounds to `0–100`.

Examples:

| Score | Confidence | Defensible bound |
|---:|---|---|
| 75 | High | 75–75 |
| 75 | Medium | 62.5–87.5 |
| 75 | Low | 50–100 |
| 25 | Medium | 12.5–37.5 |
| 0 | Low | 0–25 |

These bounds represent scoring uncertainty, not statistical confidence intervals.

## Unknown and blocked criteria

Unknown and blocked criteria do not use confidence bounds around a point score.

They contribute:

```text
minimum = 0
maximum = 100
confidence factor = 0
```

This preserves uncertainty without pretending the midpoint is known.

## Criterion confidence assignment

Evaluate the following dimensions:

- evidence directness
- source integrity
- source recency
- scope coverage
- test completeness
- source agreement
- applicability certainty
- internal-record reliability
- competitor comparability when relevant

### High confidence requires

- direct or verified evidence
- applicable scope confirmed
- no material evidence conflict
- required test coverage completed
- source is current enough for the criterion

### Medium confidence may apply when

- condition is directly visible but impact context is incomplete
- several consistent sources exist but one material gap remains
- client records are available but not fully reconciled
- competitor or search evidence is useful but variable

### Low confidence may apply when

- evidence depends on recollection
- sample size is narrow
- system access is incomplete
- internal process is inferred
- source recency is weak
- applicability or causality remains uncertain

### Unknown applies when

- no defensible score anchor can be selected
- evidence is absent or materially conflicting
- the evaluator cannot distinguish absence from inaccessibility

## Category confidence index

Calculate category confidence using scored criterion weight only:

```text
Category Confidence Index =
sum(criterion confidence factor × scored criterion weight)
÷ sum(scored criterion weight)
```

If no criterion is scored, category confidence is unknown.

### Confidence index bands

| Index | Category confidence |
|---:|---|
| 0.85–1.00 | High |
| 0.65–0.8499 | Medium |
| 0.01–0.6499 | Low |
| 0 | Unknown |

Category confidence must be reported alongside category coverage. A high confidence index on a small scored sample does not make the category complete.

Example:

```text
Coverage: 35%
Confidence index on known evidence: 95%
```

This means the known evidence is strong, but the category remains under-evaluated.

## Confidence-adjusted category bounds

Calculate category bounds in two parts.

### Known scored criteria

Use each criterion's confidence lower and upper bounds.

### Unknown or blocked criteria

Use `0–100`.

```text
Category Lower Bound =
sum(criterion lower bound × criterion weight)
÷ applicable criterion weight

Category Upper Bound =
sum(criterion upper bound × criterion weight)
÷ applicable criterion weight
```

This confidence-adjusted range replaces the simpler unknown-only range when confidence data is available.

The observed category score remains the weighted average of scored maturity anchors.

## Operator Score confidence index

```text
Operator Confidence Index =
sum(category confidence index × category weight × category coverage)
÷ sum(category weight × category coverage)
```

This gives more influence to categories with stronger evidence coverage.

If weighted evidence coverage is zero, Operator Score confidence is unknown.

### Operator confidence bands

| Index | Confidence |
|---:|---|
| 0.85–1.00 | High |
| 0.65–0.8499 | Medium |
| 0.01–0.6499 | Low |
| 0 | Unknown |

## Confidence-adjusted Operator Score range

```text
Operator Lower Bound =
sum(category lower bound × category weight)

Operator Upper Bound =
sum(category upper bound × category weight)
```

Use all active categories.

Do not replace this range with the midpoint for client reporting.

## Publication controls

### Official point score

An official score requires:

- weighted evidence coverage at least 80%
- Operator confidence index at least 0.65
- no major category below required coverage
- no unresolved high-materiality unknown
- no blocking scoring or control-boundary error

### Provisional point score

A provisional point score may be shown when:

- calculator coverage permits a provisional result
- confidence index is at least 0.50
- range and material unknowns are disclosed
- point estimate is labeled provisional

### Range only

Use range only when:

- confidence index is below 0.50
- weighted coverage is below calculator threshold
- unresolved evidence conflict is material
- range crosses several maturity tiers
- major internal systems are unavailable

### Blocked

Block publication when:

- confidence is fabricated or unsupported
- evidence integrity is in question
- G4 control-boundary conditions affect score validity
- methodology or weight version is unresolved
- required approval is missing

## Maturity tier confidence

A maturity tier is:

- `resolved` when the permitted point estimate and confidence-adjusted range remain inside one tier
- `borderline` when the range crosses one adjacent tier boundary
- `unresolved` when the range crosses more than one tier or no point estimate is permitted

Client language must reflect the tier state.

## High-impact, low-confidence rule

When a condition could create severe business, privacy, safety, legal, customer, financial-commitment, or AI-execution exposure but confidence is low:

1. do not reduce the severity because confidence is low
2. do not present the condition as confirmed
3. create a high-priority validation task
4. route to REVIEW or HALT when the potential consequence requires it
5. disclose the evidence limitation

Confidence governs assertion strength. It does not erase potential consequence.

## Confidence and recommendation priority

Recommendation priority must not use confidence as a direct value booster.

Use confidence to decide:

- recommend
- validate
- defer
- monitor
- block

Examples:

| Impact | Confidence | Routing |
|---|---|---|
| High | High | Recommend and prioritize |
| High | Medium | Recommend with validation or conditions |
| High | Low | Validate urgently; REVIEW or HALT if consequence is severe |
| Low | High | Low-priority improvement or exclude |
| Low | Low | Monitor or exclude |

## Confidence decay

Evidence confidence may decrease when:

- public content changes
- data becomes stale
- workflow ownership changes
- tools or configurations change
- competitor evidence is no longer current
- client statements conflict with newer records
- implementation invalidates the original baseline

A score-run policy should define review dates for volatile evidence. Until that policy exists, evaluators must record capture dates and flag materially stale sources.

## Cross-source confidence rules

### Client-provided evidence

Client-provided evidence may be high confidence when it is complete, directly relevant, internally consistent, and verifiable.

It is not automatically high or low solely because the client supplied it.

### Comparative evidence

Confidence depends on:

- named comparable competitors
- matched services and geography
- observation date
- equivalent surfaces
- sufficient sample

### Analytics and CRM evidence

Confidence depends on:

- metric definitions
- tracking completeness
- reconciliation
- date range
- attribution limits
- data quality

### Screenshots

Screenshots may confirm visible state at a moment in time but may not prove workflow behavior, ownership, historical performance, or recurring consistency.

## Report language

### High confidence

> The reviewed evidence confirms this condition within the tested scope.

### Medium confidence

> The available evidence supports this conclusion, although additional validation would improve certainty.

### Low confidence

> The available evidence suggests this condition may be present, but internal validation is required before treating it as confirmed.

### Unknown

> This area could not be scored because the required evidence was unavailable or inconclusive.

### Score range

> The score range reflects both unresolved criteria and the strength of evidence supporting the current observations.

## Confidence-adjustment object

```yaml
criterion_score_ref: OI-CS-YYYY-NNNN
confidence: medium
confidence_factor: 0.75
observed_score: 75
lower_bound: 62.5
upper_bound: 87.5
basis:
  directness: direct
  recency: current
  coverage: partial
  agreement: consistent
limitations:
  - mobile workflow not tested
review_required: false
ledger_ref: OI-DL-YYYY-NNN
```

## Validation errors

### Blocking

- scored criterion has unknown confidence
- confidence factor does not match controlled vocabulary
- numeric score is assigned to unknown evidence
- official score confidence is below threshold
- score bounds are missing
- evidence conflict is hidden
- confidence is manually increased without evidence change

### Warnings

- low-confidence criterion has high category weight
- category confidence is high but coverage is low
- evidence is stale
- score range crosses tier boundary
- client-provided data is unreconciled
- comparative evidence sample is narrow

## Recalculation rules

Recalculate confidence outputs when:

- evidence is added, removed, corrected, or invalidated
- confidence level changes
- criterion applicability changes
- category weight changes
- evidence becomes stale
- system access resolves an unknown
- duplicate-control logic changes

Published score objects must be superseded rather than silently overwritten.

## DecisionLedger requirements

```yaml
score_run_id: OI-SCORE-YYYY-NNN
operator_score_ref: OI-OS-YYYY-NNN
weighted_evidence_coverage: 0
operator_confidence_index: 0
operator_confidence: unknown
confidence_adjusted_range: [0, 100]
publication_state: range_only
material_low_confidence_items: []
high_impact_validation_tasks: []
review_decision: validate
approver: ""
rationale: ""
ledger_ref: OI-DL-YYYY-NNN
```

## Usage instructions

1. Assign criterion maturity anchor from evidence.
2. Assign confidence independently.
3. Convert confidence to controlled factor and bounds.
4. Calculate category confidence and bounds.
5. Calculate weighted Operator confidence and range.
6. Apply coverage and publication gates.
7. Route high-impact, low-confidence conditions to validation or escalation.
8. Use confidence-safe report language.
9. Preserve all confidence bases and limitations.
10. Recalculate when evidence changes.

## Completion check

Before publishing confidence-adjusted results, confirm:

- maturity and confidence are separate
- factors match controlled levels
- unknown criteria have no point score
- criterion bounds are calculated
- category confidence and coverage are both disclosed
- Operator confidence index is calculated
- full score range uses all active categories
- publication state passes thresholds
- high-impact, low-confidence items have validation routes
- tier state is resolved, borderline, or unresolved
- report wording matches confidence
- DecisionLedger traceability exists
