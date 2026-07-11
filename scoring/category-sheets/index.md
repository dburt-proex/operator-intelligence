# Operator Intelligence Category Scoring Sheets

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Status: Draft foundation for commercial v1.0

## Purpose

This index defines the mandatory contract for every Operator Intelligence category scoring sheet.

Category sheets translate general scoring anchors into domain-specific evaluator guidance so two qualified evaluators using the same evidence can reach materially similar criterion scores, confidence assignments, category interpretations, and publication decisions.

They supplement, but do not replace:

- `scoring/criteria-library.md`
- `scoring/calculator-spec.md`
- `scoring/weight-rules.md`
- `scoring/evidence-thresholds.md`
- `scoring/unknown-data-handling.md`
- `scoring/confidence-adjusted-scoring.md`
- `framework/finding-index.md`
- `framework/recommendation-index.md`

## Canonical category sheets

| Category key | Required file | Criteria prefixes | Default Operator Score weight |
|---|---|---|---:|
| `website` | `website.md` | `OI-WEB-*` | 10% |
| `messaging_offer` | `messaging-offer.md` | `OI-MSG-*`, `OI-OFFER-*` | 10% |
| `conversion` | `conversion.md` | `OI-CONV-*` | 15% |
| `seo` | `seo.md` | `OI-SEO-*` | 15% |
| `gbp` | `gbp.md` | `OI-GBP-*` | 10% |
| `trust` | `trust.md` | `OI-TRUST-*` | 10% |
| `social` | `social.md` | `OI-SOC-*` | 5% |
| `automation` | `automation.md` | `OI-AUTO-*` | 10% |
| `ai_readiness` | `ai-readiness.md` | `OI-AI-*` | 5% |
| `analytics` | `analytics.md` | `OI-AN-*` | 5% |
| `competitive` | `competitive.md` | `OI-COMP-*` | 5% |

The category list and weights must remain aligned with `scoring/calculator-spec.md` and `scoring/weights.md`.

## Required sheet structure

Every category sheet must contain these sections in this order:

1. Purpose and category boundary
2. Included criterion prefixes and criterion inventory
3. Required evidence surfaces
4. Minimum evaluation scope
5. Applicability rules
6. Criterion weighting rule
7. Category-specific anchor guidance
8. Confidence assignment guidance
9. Unknown, blocked, and not-applicable treatment
10. Duplicate-signal boundaries
11. Finding and recommendation routing
12. Publication controls
13. DecisionLedger requirements
14. Validation messages
15. Worked scoring example
16. Completion checklist

A category sheet is incomplete if any required section is absent.

## Category boundary requirement

Each sheet must state what the category measures and what it does not measure.

The boundary must prevent the same operating condition from being scored in multiple categories without distinct measurement logic.

Examples:

- Website structure measures navigation, usability, page architecture, and buyer-path accessibility. It does not independently score message quality or form follow-up.
- Messaging and offer clarity measures positioning, service clarity, differentiation, buyer relevance, and offer structure. It does not score technical page performance.
- Conversion infrastructure measures the ability to turn interest into a captured, acknowledged, routed, and actionable lead. It does not score lead-source visibility.
- Analytics measures instrumentation, reporting, and decision usability. It does not score the performance outcome merely because data is unavailable.

Cross-domain impact must be recorded as a dependency, not a duplicate score.

## Criterion inventory requirement

Each sheet must list every governed criterion assigned to the category.

For every criterion, record:

```yaml
criterion_id: OI-WEB-001
criterion_name: ""
category_key: website
applicability_rule: ""
minimum_evidence: []
anchor_guidance_ref: ""
default_weighting: equal
finding_domains: []
```

A criterion may have only one weighted category owner.

Missing, duplicated, deprecated, or unmapped criterion IDs block category publication.

## Evidence requirements

Each sheet must define:

- primary evidence sources
- acceptable supporting evidence
- required test actions
- minimum sample or surface coverage
- evidence recency expectations
- evidence classes that cannot support a point score alone
- conditions requiring client records or system access

Evidence must separate:

```text
Observation
→ Source
→ Scope
→ Test result
→ Interpretation
→ Confidence
```

Public absence may confirm a missing public feature only after the required search or test is completed.

Missing access to internal systems normally produces `unknown` or `blocked`, not score `0`.

## Minimum evaluation scope

Each category sheet must define the minimum scope required before a category score is admissible.

Scope may include:

- number and type of pages reviewed
- desktop and mobile testing
- locations or profiles reviewed
- forms or contact paths tested
- review sample size
- date range examined
- records or workflows sampled
- competitors compared
- analytics period inspected

A completed test on one narrow surface must not be generalized to the full category unless the sheet explicitly permits it.

## Applicability rules

Every criterion must resolve to one of:

- `scored`
- `unknown`
- `not_applicable`
- `blocked`

`not_applicable` requires structural irrelevance, documented rationale, and approval.

The following are not valid reasons for `not_applicable`:

- evidence was not provided
- access was unavailable
- the condition was difficult to inspect
- the score would decrease
- the evaluator considers the criterion unimportant without methodology support

## Weighting rule

Equal weighting is the category default:

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

A sheet may define unequal criterion weights only when all requirements in `scoring/weight-rules.md` pass.

Unknown and blocked criteria remain inside applicable criterion weight.

Approved `not_applicable` criteria are removed before internal weights are recalculated.

## Category-specific anchor guidance

Every criterion or criterion family must define observable conditions for these anchors:

| Score | Required interpretation |
|---:|---|
| 0 | Confirmed absent, broken, misleading, or actively harmful within tested scope |
| 25 | Present but materially weak, incomplete, inconsistent, or unreliable |
| 50 | Functional baseline with material improvement opportunity |
| 75 | Strong, commercially useful, and consistently implemented |
| 100 | Mature, differentiated, measured, integrated, and governed |

Anchor guidance must use observable conditions, not adjectives alone.

A score of `100` must require more than presence. It normally requires consistency, integration, measurement, ownership, and evidence of operational control.

Interpolation is prohibited unless the sheet defines an approved rule and the score object records the rule version.

## Confidence guidance

Category sheets must explain what supports high, medium, low, or unknown confidence in that domain.

Confidence must consider:

- evidence directness
- source integrity
- recency
- scope coverage
- test completeness
- source agreement
- internal-record reliability
- comparability where relevant

Confidence must not be multiplied into the maturity score.

High confidence on a narrow sample does not replace category coverage.

## Unknown and blocked treatment

Each sheet must identify common unknown and blocked conditions and assign approved reason codes from `scoring/unknown-data-handling.md`.

Every material unknown must include:

- reason code
- evidence requested or test required
- validation owner
- materiality
- next action
- publication effect

A high-materiality unknown may force `range_only`, `REVIEW`, or `HALT` even when numeric coverage exceeds the normal publication threshold.

## Duplicate-signal boundaries

Each sheet must identify likely overlaps with adjacent categories and define ownership.

At minimum, document:

```yaml
overlap_with: conversion
condition: ""
primary_owner: website
secondary_effect: ""
duplicate_scoring_prohibited: true
```

One evidence item may support multiple criteria only when each criterion measures a distinct condition.

The `messaging_offer` sheet must preserve separate messaging and offer criterion records while aggregating them into one weighted category.

The `social` sheet must not create `OI-FIND-SOC-*` finding IDs unless a governed social finding library is later approved.

## Finding and recommendation routing

A category score does not automatically create a finding or recommendation.

Routing requires:

1. evidence-backed observation
2. governed finding ID or documented methodology gap
3. business impact
4. confidence
5. priority
6. package fit
7. roadmap phase
8. DecisionLedger record

Category sheets must identify eligible finding domains and common package dependencies without making package selection automatic.

Package-first selling is prohibited.

## Publication controls

Each sheet must apply the common publication states:

| State | Minimum treatment |
|---|---|
| `official` | Publish score, confidence, coverage, range, and material unknowns |
| `provisional` | Publish qualified point score with range and validation note |
| `range_only` | Publish range or insufficient-data state without false precision |
| `blocked` | Do not publish a category score |

Category-specific controls may be stricter than the common thresholds but may not weaken them without methodology approval.

## DecisionLedger minimum record

Each category result must retain:

```yaml
category_key: website
category_sheet_version: "0.1"
criterion_inventory_version: ""
score_run_id: OI-SCORE-YYYY-NNN
applicable_criteria: []
scored_criteria: []
unknown_criteria: []
blocked_criteria: []
not_applicable_criteria: []
observed_score: null
lower_bound: null
upper_bound: null
coverage: null
confidence_index: null
publication_state: range_only
material_unknowns: []
duplicate_check_passed: false
finding_refs: []
recommendation_refs: []
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## Validation messages

Every sheet must define category-specific validation messages using this format:

```text
CAT-{CATEGORY}-{TYPE}-{NNN}
```

Required shared validation types:

- `SCOPE`: minimum evaluation scope not met
- `EVID`: evidence does not support the selected anchor
- `MAP`: criterion or category mapping failure
- `DUP`: duplicate-signal conflict
- `UNKNOWN`: unresolved material unknown
- `WEIGHT`: internal weighting failure
- `GATE`: governance boundary blocks scoring or publication
- `LEDGER`: required traceability missing

Blocking messages must identify the failed rule and required correction.

## Worked example requirement

Every category sheet must include one complete worked example showing:

- applicable criteria
- evidence references
- criterion states
- anchor decisions
- confidence decisions
- internal weights
- category observed score
- category bounds
- coverage
- confidence index
- publication state
- finding-routing outcome
- DecisionLedger reference

The example must include at least one unknown or blocked criterion so uncertainty handling is demonstrated.

## Sheet approval gate

A category sheet is eligible for scoring use only when:

- all required sections are complete
- every assigned criterion is mapped once
- category boundaries are explicit
- minimum evidence and scope are testable
- anchors use observable conditions
- confidence guidance is domain-specific
- unknown and blocked rules are explicit
- duplicate-signal boundaries pass review
- finding and package routing preserve governance
- validation messages are defined
- the worked example recalculates correctly
- a reviewer approves the sheet version

Until approved, the calculator must use the general rubric and equal weighting while marking category-sheet guidance as unavailable.

## Change control

Changes to category boundaries, criterion ownership, evidence thresholds, anchor definitions, internal weights, duplicate rules, or publication controls require:

1. category-sheet version increment
2. rationale
3. regression example
4. impact review across scoring and findings
5. DecisionLedger entry
6. methodology approval

Historical score runs retain the category-sheet version used at calculation time.