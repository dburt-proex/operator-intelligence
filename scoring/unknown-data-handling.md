# Operator Intelligence Unknown-Data Handling

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file defines how Operator Intelligence handles missing, inaccessible, conflicting, untested, or structurally irrelevant data during scoring.

Its purpose is to prevent unknown information from being treated as failure, hidden through normalization, or converted into false precision.

## v1.0 connection

Commercial v1.0 requires reliable scoring even when clients cannot provide every internal record or system access.

This file strengthens v1.0 readiness by providing:

- controlled evaluation states
- unknown-reason codes
- absent-versus-unknown rules
- not-applicable controls
- coverage and range treatment
- validation ownership
- report language
- critical-unknown escalation
- recalculation requirements
- DecisionLedger traceability

## Core rules

1. Unknown is not a negative score.
2. Lack of visible evidence is not proof that an internal process does not exist.
3. Confirmed absence may be scored only when the criterion and evidence scope make absence observable.
4. `not_applicable` is not a convenience state and requires documented structural irrelevance.
5. Unknowns must remain visible in category coverage, score ranges, and client language.
6. Normalization must never conceal material evidence gaps.
7. A high-impact unknown may require validation or escalation even though it does not reduce the score.
8. New evidence requires recalculation rather than narrative correction alone.

## Canonical evaluation states

| State | Definition | Score treatment |
|---|---|---|
| `scored` | Evidence supports an approved anchor | Included in observed score |
| `unknown` | Evidence is insufficient to assign an anchor | No numeric score; included in possible range |
| `not_applicable` | Criterion is structurally irrelevant to the business or assessment scope | Excluded after approval |
| `blocked` | Access, policy, evidence conflict, system failure, or control boundary prevents evaluation | No numeric score; treated as unknown plus control flag |

## Unknown-reason codes

| Code | Use when |
|---|---|
| `not_provided` | Requested client information was not supplied |
| `access_unavailable` | System or account access was unavailable |
| `not_tested` | Required test was not performed or could not be completed |
| `insufficient_sample` | Available evidence is too limited to represent the condition |
| `conflicting_evidence` | Sources materially disagree |
| `internal_process_unverified` | Public evidence cannot confirm an internal workflow |
| `policy_restricted` | Access or evaluation is restricted by policy, privacy, or authority |
| `system_error` | Technical failure prevented evaluation |
| `methodology_gap` | Existing criteria or rules cannot represent the condition safely |
| `other_documented` | Another reason is recorded with sufficient detail |

Every unknown must include:

- reason code
- evidence requested or test required
- validation owner
- validation status
- materiality
- next action or documented decision not to validate

## Absent versus unknown

### Score as confirmed absence when:

- the criterion is publicly observable within the documented scope
- the evaluator completed the required search or test
- evidence directly confirms the feature, field, page, control, or process is missing or broken
- the criterion anchor defines confirmed absence as score `0`

Examples:

- no phone number appears on tested website pages
- the public Google Business Profile cannot be found after documented searches
- a form test confirms no submission acknowledgement
- a verified CRM schema contains no lead-owner field

### Mark unknown when:

- the condition is internal and client confirmation or system access is missing
- only one public surface was checked when the criterion covers several
- a test was not completed
- the evaluator cannot distinguish absence from access limitation
- evidence conflicts
- the criterion requires financial, operational, policy, or historical records not available

Examples:

- no CRM is visible publicly
- close rate was not disclosed
- follow-up may depend on memory but records were not reviewed
- AI logs may exist in an inaccessible tool
- capacity is unclear

## Not-applicable controls

A criterion may be `not_applicable` only when:

- the business model makes the criterion structurally irrelevant
- the assessment scope explicitly excludes the criterion for a valid reason
- the exclusion does not hide a weak or missing capability
- the reason is documented
- the evaluator and reviewer approve the exclusion

### Invalid not-applicable reasons

- evidence is unavailable
- the client does not want to answer
- the score would decrease
- the system is difficult to inspect
- the evaluator believes the criterion is unimportant without methodology support

### Examples of potentially valid exclusions

- a physical-address display criterion for a verified service-area business when public-address display is not required
- a seasonal reactivation criterion for a one-time regulated service where repeat outreach is prohibited or structurally irrelevant
- an appointment-booking criterion where the approved buyer path is emergency phone dispatch and online booking is not part of the operating model

Not-applicable decisions must record the criterion ID, reason, approver, and effect on category weighting.

## Blocked state

Use `blocked` when scoring cannot proceed because of a control condition rather than ordinary missing evidence.

Common blocked conditions:

- unauthorized account access
- privacy or policy restriction
- unresolved evidence tampering or integrity concern
- system failure that invalidates testing
- conflicting records with no authoritative source
- G4 AI, safety, legal, customer, or financial-commitment boundary
- methodology version conflict

Blocked criteria behave like unknown criteria in score mathematics but also create a blocking validation message or governance review.

## Unknown materiality

Classify each unknown:

| Materiality | Meaning | Required action |
|---|---|---|
| `low` | Unlikely to change category interpretation or recommendation routing | Disclose if useful; validation optional |
| `medium` | Could change category score, finding confidence, or package priority | Add validation action or provisional treatment |
| `high` | Could materially change Operator Score, risk, package eligibility, capacity, privacy, or delivery decision | Require validation, range-only output, review, or halt |

A high-materiality unknown must never be hidden inside a normalized score.

## Category coverage treatment

Unknown and blocked criteria remain part of applicable criterion weight.

```text
Category Coverage =
Known Scored Weight ÷ Applicable Weight
```

Not-applicable criteria are removed only after approval.

Category score bounds assume:

```text
Unknown Minimum = 0
Unknown Maximum = 100
```

This does not imply the actual unknown value is equally likely to be anywhere in the range. It defines the defensible mathematical boundary until evidence resolves the condition.

## Category publication thresholds

| Coverage | Treatment |
|---:|---|
| 80–100% | Score may be reportable if no material unknown blocks publication |
| 60–79.99% | Score is provisional and must include range and validation language |
| Below 60% | Publish range only or insufficient-data state |

A category with high-materiality unknowns may be forced into range-only or blocked status even when numeric coverage is above 80%.

## Operator Score treatment

Unknown categories must not be silently dropped and normalized into an apparently complete score.

The calculator must disclose:

- active weight represented by observed category scores
- weighted evidence coverage
- full Operator Score minimum and maximum
- normalized observed score, when calculated
- official, provisional, range-only, or blocked publication state

An official point score requires the coverage and governance gates in `scoring/calculator-spec.md`.

## Internal-data rule

For internal criteria involving CRM, sales, estimates, calls, finance, customer history, automation, analytics, AI, policy, or staff behavior:

- public absence is not sufficient evidence
- client interview may support low or medium confidence depending on specificity
- direct records or tested configuration support higher confidence
- missing internal access normally creates unknown, not zero

## Public-surface rule

For public criteria involving website pages, GBP, reviews, public social profiles, public directories, or visible contact paths:

- a documented search or test may confirm absence
- scope must include relevant devices, pages, locations, or profiles
- personalized search variability must be recorded
- one isolated result must not represent stable performance

## Conflicting evidence

When evidence conflicts:

1. mark evaluation state `unknown` or `blocked`
2. record each evidence source
3. identify the authoritative source if one exists
4. do not average contradictory claims
5. assign a validation owner
6. resolve before official publication when material

Example:

```text
Owner interview says every estimate receives follow-up.
CRM review shows no tasks or status history.
```

The criterion remains unresolved until workflow evidence, samples, or reconciled records establish the actual condition.

## Unknown-data validation object

```yaml
criterion_id: OI-AUTO-006
state: unknown
reason_code: access_unavailable
materiality: high
requested_evidence:
  - CRM task history
  - open-estimate follow-up sample
validation_owner: client_operations_owner
due_state: before_report_finalization
next_action: provide_export
score_effect: expands_category_range
finding_effect: validation_required
recommendation_effect: block_package_until_validated
ledger_ref: OI-DL-YYYY-NNN
```

## Report language

### Unknown internal process

> This area could not be fully evaluated because the required internal workflow or records were not available. It has not been scored as a failure.

### Provisional category

> The available evidence supports a provisional category score, but unresolved criteria create a wider defensible range. Validation is recommended before final prioritization.

### Range only

> Evidence coverage is not sufficient for a precise category score. The current range reflects confirmed evidence and unresolved criteria.

### Confirmed absence

> The reviewed evidence confirms that this capability is not currently present within the tested scope.

### Not applicable

> This criterion was excluded because it does not apply to the documented business model. The exclusion and resulting weight treatment were reviewed.

## Recommendation-routing rules

| Unknown condition | Routing |
|---|---|
| Low materiality and package eligibility otherwise passes | Recommendation may proceed with disclosure |
| Medium materiality affects scope or effort | Use provisional scope or validation task |
| High materiality affects package eligibility | Defer recommendation until validated |
| Privacy, safety, legal, binding commitment, or access boundary | REVIEW or HALT |
| No existing criterion represents the issue | Methodology-gap record; do not invent score |

## Recalculation rules

A score run must be recalculated when:

- unknown becomes scored
- scored becomes unknown due to evidence invalidation
- not-applicable decision changes
- evidence conflict is resolved
- scope expands or contracts
- system access changes a material criterion
- methodology mapping changes

The prior published score must remain preserved as a superseded object.

## Quality-control checks

Before closing unknown handling, confirm:

- every applicable criterion has an evaluation state
- unknowns contain no numeric score
- unknown reasons are controlled and documented
- absence is supported by evidence
- not-applicable exclusions are approved
- blocked states create governance flags
- materiality is assigned
- validation ownership exists
- category coverage includes unknown weight
- score ranges include unresolved criteria
- client language does not imply failure
- high-materiality unknowns affect publication state appropriately
- DecisionLedger traceability exists

## Usage instructions

1. Determine criterion applicability before reviewing performance.
2. Separate unavailable evidence from confirmed absence.
3. Assign evaluation state and reason code.
4. Record materiality and validation owner.
5. Apply score, range, and coverage treatment.
6. Run publication and package-eligibility gates.
7. Disclose material unknowns in client language.
8. Recalculate when evidence changes.
9. Preserve superseded score objects.
10. Route methodology gaps for formal review.
