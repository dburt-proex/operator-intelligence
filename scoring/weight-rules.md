# Operator Intelligence Weight Rules

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file governs category and criterion weights used by the Operator Intelligence scoring system.

It prevents evaluators from changing weights to fit a preferred conclusion, hiding weak categories through normalization, or producing scores that cannot be compared or reproduced.

This file supplements `scoring/weights.md`. The approved numeric profiles remain defined there. These rules govern selection, modification, calculation, approval, and disclosure.

## Core rules

1. Every score run must use one named weight profile.
2. Active category weights must total exactly 100% before publication.
3. Weight changes must reflect assessment scope or business-model relevance, not observed performance.
4. A weak category must not receive a lower weight because it would reduce the Operator Score.
5. An unknown category must not be removed merely because evidence is unavailable.
6. `not_applicable` exclusions require documented structural irrelevance and approval.
7. Category and criterion weights must be fixed before scoring begins.
8. Any weight change after evidence review requires a new score run.
9. Original and adjusted profiles must remain traceable.
10. Client-facing reports must disclose non-default profiles and their rationale.

## Approved weight profiles

### Default profile

Use the default profile when the assessment covers a general local-service or contractor business and no material operating-model difference requires adjustment.

Profile key:

```text
OI-WEIGHT-DEFAULT-01
```

### Contractor-heavy profile

Use the contractor-heavy profile only when the business materially depends on local high-intent discovery, estimate requests, rapid lead response, reputation, and service-area conversion.

Profile key:

```text
OI-WEIGHT-CONTRACTOR-01
```

The numeric values for both profiles are defined in `scoring/weights.md`.

## Profile selection gate

Select a profile before criterion scoring.

The score run must record:

```yaml
weight_profile: OI-WEIGHT-DEFAULT-01
profile_version: "0.1"
selection_reason: ""
selected_by: ""
approved_by: ""
selected_at: ""
```

Use the default profile unless another approved profile is demonstrably better aligned to the business model.

A profile-selection rationale must reference observable characteristics such as:

- primary buyer path
- service urgency
- transaction structure
- geographic market dependence
- sales-cycle length
- lead-response requirements
- repeat or subscription model
- regulated operating constraints

Do not select a profile based on:

- which profile produces the highest score
- which profile makes a package easier to sell
- a client’s preferred result
- incomplete evidence
- evaluator intuition without documented business-model support

## Custom weight profiles

A custom profile is permitted only when approved profiles materially misrepresent the business model.

Custom profile key format:

```text
OI-WEIGHT-CUSTOM-YYYY-NNN
```

A custom profile requires:

- business-model rationale
- proposed category weights
- confirmation that weights total 100%
- comparison with the closest approved profile
- documented effect on interpretation
- named evaluator
- independent reviewer approval
- DecisionLedger reference
- methodology version

A custom profile must not be created solely for one weak or unknown category.

## Category-weight integrity

Before scoring, validate:

```text
Sum of Active Category Weights = 100%
```

Blocking conditions:

- total is below or above 100%
- a required category has no state
- duplicate category keys exist
- a category weight is negative
- a category weight exceeds 30% without methodology approval
- profile version is missing
- profile selection lacks rationale when non-default

A failed integrity check sets the score-run publication state to `blocked`.

## Category exclusion rules

A category may be excluded only when every underlying criterion is approved as `not_applicable` or the assessment scope explicitly excludes the category for a valid structural reason.

Evidence unavailable, access denied, or testing incomplete does not make a category not applicable.

When a category is excluded:

1. Record the category key.
2. Record the structural reason.
3. Record the affected criteria.
4. Record evaluator and reviewer approval.
5. Preserve the original profile.
6. Create a derived active profile whose remaining weights total 100%.
7. Disclose the exclusion in score methodology notes.

Derived active weights are calculated as:

```text
Normalized Active Category Weight =
Original Category Weight ÷ Sum of Remaining Original Weights
```

Normalization is allowed only after an approved `not_applicable` exclusion. It must not be used to hide unknown, blocked, or low-coverage categories.

## Unknown and blocked categories

Unknown and blocked categories retain their original category weight.

They contribute to:

- weighted evidence coverage
- Operator Score minimum and maximum
- publication-state determination
- validation and escalation

They must not be silently dropped from the score model.

## Criterion weights inside categories

Unless an approved category sheet states otherwise, applicable criteria within a category use equal weight.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

`not_applicable` criteria are removed only after approval.

Unknown and blocked criteria remain in applicable criterion weight.

A category sheet may define unequal criterion weights only when:

- the weights total 100% within the category
- the rationale is tied to materiality, not observed performance
- the weighting version is recorded
- duplicate-signal controls pass
- evaluator guidance is explicit
- regression examples exist

## Weight freezing

Weights freeze when the score run enters evidence interpretation.

After freezing, changes to any of the following require a new score run or version:

- selected category profile
- category exclusions
- category weights
- criterion applicability
- criterion weights
- category mapping

Narrative edits do not require a rerun unless they change evidence, applicability, score, confidence, or calculation inputs.

## Duplicate-signal control

Weights must not amplify one operational condition through overlapping criteria or categories.

Before publication, confirm:

- each criterion has one weighted category owner
- cross-domain impacts are represented as dependencies, not duplicate scores
- one evidence item may support several criteria only when each criterion measures a distinct condition
- combined messaging and offer criteria remain inside the single `messaging_offer` category
- social signals do not create invented social finding IDs

A material duplicate-signal failure blocks the Operator Score.

## Sensitivity check

Run a sensitivity check when:

- a custom profile is used
- any category weight changes by 5 percentage points or more from the closest approved profile
- one category receives 20% or more
- the score result is within 3 points of a maturity-tier boundary

The sensitivity check compares the active result with the closest approved profile using the same category scores.

Record:

```yaml
comparison_profile: ""
active_operator_score: null
comparison_operator_score: null
absolute_difference: null
tier_changed: false
interpretation_changed: false
review_required: false
```

A weight-driven tier change requires explicit review and disclosure.

## Publication rules

An Operator Score is not eligible for `official` publication unless:

- the weight profile is approved
- active weights total 100%
- exclusions are valid and approved
- weights were frozen before scoring
- no performance-driven reweighting occurred
- duplicate-signal checks pass
- required sensitivity review is complete
- profile and version are stored in score objects

If the calculation is otherwise valid but a non-default profile materially changes interpretation, publication may be limited to `provisional` pending review.

## DecisionLedger minimum record

```yaml
ledger_ref: OI-DL-YYYY-NNN
score_run_id: OI-SCORE-YYYY-NNN
weight_profile: OI-WEIGHT-DEFAULT-01
profile_version: "0.1"
original_weights: {}
active_weights: {}
excluded_categories: []
selection_reason: ""
custom_profile_reason: null
weights_frozen_at: ""
sensitivity_check_ref: null
duplicate_check_passed: false
selected_by: ""
reviewed_by: ""
approved_by: ""
publication_effect: none
```

## Validation messages

### Blocking errors

- `WEIGHT-TOTAL-001`: active category weights do not total 100%
- `WEIGHT-PROFILE-001`: weight profile is missing or unsupported
- `WEIGHT-RATIONALE-001`: non-default profile lacks rationale
- `WEIGHT-EXCLUDE-001`: category exclusion lacks valid approval
- `WEIGHT-FREEZE-001`: weights changed after scoring began without rerun
- `WEIGHT-DUPLICATE-001`: duplicate weighting materially inflates a score
- `WEIGHT-PERFORMANCE-001`: weights were adjusted in response to observed performance
- `WEIGHT-VERSION-001`: profile or criterion-weight version is missing

### Warnings

- `WEIGHT-SENSITIVITY-001`: sensitivity review is required
- `WEIGHT-CONCENTRATION-001`: one category carries at least 20%
- `WEIGHT-TIER-001`: profile choice changes the maturity tier
- `WEIGHT-CUSTOM-001`: custom profile limits comparability

## Client-facing language

Preferred:

> The assessment used the contractor-heavy weight profile because the business depends primarily on local high-intent search, estimate conversion, rapid response, and reputation. The profile was selected before scoring and is disclosed for comparability.

Preferred exclusion language:

> One category was excluded because the approved assessment scope established that it was structurally not applicable. The remaining weights were normalized, and the exclusion is documented in the methodology notes.

Do not say:

- weights were changed to better reflect the final score
- weak areas were deprioritized
- unknown categories were removed
- the profile guarantees a more accurate business outcome

## Completion check

Before publishing, confirm:

- one named profile is recorded
- profile selection occurred before scoring
- weights total 100%
- non-default rationale is documented
- exclusions are structurally valid
- unknowns retained their weight
- criterion weighting follows the category sheet or equal-weight default
- weights were frozen
- duplicate-signal checks pass
- sensitivity review is complete when required
- DecisionLedger traceability exists
- client methodology notes disclose material deviations
