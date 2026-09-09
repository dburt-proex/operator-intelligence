# Agentic AI Control Readiness Weight Rules

**Status:** Stage 3B canonical scoring control — proposed for review  
**Version:** 0.1.0  
**Authority:** Operator Intelligence assessment methodology  
**Active model:** Agentic AI Control Readiness Assessment v0.1  
**Implementation authorization created by this artifact:** `false`

## Purpose

Define the canonical weighting rules, category relationships, confidence treatment, and unknown-data behavior for the active Agentic AI Control Readiness Assessment.

At `scoring/aicr/weight-rules.md`, this file is the single Stage 3B source for AICR v0.1 domain weights. AICR domain sheets may reference these weights but must not redefine, override, or duplicate them.

## Scoring-authority boundary

| Assessment profile | Canonical rule path | Permitted consumers |
|---|---|---|
| Business Growth Systems Assessment / contractor-local-service | `scoring/weight-rules.md` | Existing legacy category sheets, examples, calculator artifacts, and score runs |
| Agentic AI Control Readiness Assessment v0.1 | `scoring/aicr/weight-rules.md` | `playbooks/agentic-control-platform-readiness/scoring-profile.md`, AICR outputs, and future `AIGR-D1..D7` sheets |

Profile selection is explicit. A consumer must never infer scoring authority from whichever file was edited most recently. Legacy consumers remain bound to `scoring/weight-rules.md`; AICR consumers must resolve only to this AICR-specific path.

## Inputs

Canonical inputs:

- `playbooks/agentic-ai-governance-readiness-assessment.md`
- `playbooks/agentic-control-platform-readiness/scoring-profile.md`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`

Legacy contractor/local-service scoring artifacts are not inputs to the active Agentic AI Control Readiness model.

## Outputs and consumers

This file governs:

- domain-sheet weight references;
- overall readiness-score calculation;
- evidence-coverage calculation;
- active-domain treatment;
- weighted ownership boundaries;
- publication and validation checks;
- future worked scoring fixtures;
- client-facing score explanations;
- DecisionLedger scoring receipts.

Primary consumers are the AICR scoring profile, future AIGR domain sheets, scoring fixtures, executive decision brief, remediation roadmap, and evidence receipt.

## Canonical seven-domain weights

| Domain | Canonical weight |
|---|---:|
| `AIGR-D1` — Purpose and ownership | 10% |
| `AIGR-D2` — Data and system access | 15% |
| `AIGR-D3` — Tool and action authority | 15% |
| `AIGR-D4` — Workflow approvals and human intervention | 15% |
| `AIGR-D5` — Evaluation and failure testing | 15% |
| `AIGR-D6` — Logging, evidence, and auditability | 15% |
| `AIGR-D7` — Deployment, monitoring, rollback, and incident response | 15% |
| **Total** | **100%** |

### Weight integrity rules

1. The seven canonical domain weights must total exactly 100%.
2. Domain sheets must not contain competing or alternate domain weights.
3. Engagement-specific reweighting is not permitted in v0.1 unless a separately versioned scoring profile is approved before evidence review.
4. A high aggregate score never overrides a deterministic critical gate or `HALT` condition.
5. `NOT_APPLICABLE` may remove an individual criterion from its domain denominator only when structural irrelevance is evidence-backed and the buyer-side rationale is recorded.
6. Whole-domain exclusion is prohibited in AICR v0.1. All seven canonical domain weights remain in the profile and in the evidence-coverage denominator.
7. If a bounded subject makes an entire canonical domain structurally inapplicable, the run is invalid under AICR v0.1 and routes `HALT` pending an explicitly approved, separately versioned scoring profile. Do not normalize the remaining six domains.

## Domain ownership and relationships

Each commercial surface has one primary weighted owner. Other domains may reference the same evidence without receiving duplicate weighted credit.

| Surface | Primary weighted owner | Reference-only relationship |
|---|---|---|
| AI/agent inventory, purpose, owner, lifecycle | `AIGR-D1` | D6 may preserve discovery evidence |
| Identity, access, entitlements, data exposure | `AIGR-D2` | D3 may reference access when it becomes action authority |
| Tools, integrations, execution scopes and limits | `AIGR-D3` | D4 may reference approval boundaries; D7 may reference containment |
| Human review, approval, override, escalation | `AIGR-D4` | D3 may reference gated actions |
| Instructions, evaluations, failure/adversarial tests | `AIGR-D5` | D7 may reference release thresholds |
| Logs, provenance, replay, auditability | `AIGR-D6` | all domains may supply reconstructable evidence |
| Release, monitoring, rollback, incident response | `AIGR-D7` | D5 may reference failure thresholds and regression evidence |

### No-double-counting rule

The same control outcome must not earn weighted maturity credit in more than one domain.

Evidence may support multiple domain interpretations, but each scored criterion must have exactly one weighted owner. Cross-domain references are contextual or dependency evidence only.

## Criterion weighting inside domains

Until a domain sheet explicitly defines approved internal criterion weights, criteria inside that domain are **equally weighted among applicable criteria**.

A future domain sheet may introduce unequal internal criterion weights only when:

- the weighting rationale is tied to control materiality rather than commercial preference;
- all criterion weights in the domain sum to 100%;
- examples demonstrate changed calculations;
- duplicate ownership has been checked;
- the change is versioned and approved before use in an assessment evidence snapshot.

No domain sheet may alter the seven domain-level weights in this file.

## Readiness calculation

For a domain with at least one known weighted criterion:

```text
domain_score =
  sum(known_criterion_score × criterion_weight)
  / sum(known_criterion_weight)
```

A domain whose `sum(known_criterion_weight) = 0` has:

```text
domain_score = null
domain_status = UNSCORED
domain_coverage = 0
```

This is a defined non-numeric result, not zero. The domain retains its canonical weight and blocks `official` publication until known evidence exists.

For an otherwise valid AICR v0.1 run, the observed-readiness denominator contains exactly the canonical weights of domains with non-null domain scores:

```text
observed_domain_weight = canonical domain weight when domain_score is non-null; otherwise 0

readiness_score =
  sum(domain_score × observed_domain_weight)
  / sum(observed_domain_weight)
```

If `sum(observed_domain_weight) = 0`, then `readiness_score = null`, the result is non-publishable, and the decision routes `BLOCKED` / `HALT`.

Omitting an unscored domain from the observed-readiness denominator is not domain exclusion or reweighting. All seven canonical weights remain fixed, all seven domains remain required, and evidence coverage continues to measure the full seven-domain surface.

The observed score represents control performance only for known evidence. It must be accompanied by evidence coverage, confidence, unknowns, contradictions, critical gates, and publication state.

## Unknown-data behavior

`UNKNOWN`, `blocked`, and `NOT_APPLICABLE` are states, not numeric scores.

### `UNKNOWN`

Use when admissible evidence is insufficient to determine the control state.

Rules:

- never convert unknown to `0`;
- retain the criterion inside applicable weight;
- exclude it from known-weight maturity calculation;
- reduce evidence coverage;
- widen uncertainty or force validation/publication constraints as required;
- route material unknowns to validation before remediation authority is inferred.

### `blocked`

Use when a result cannot be determined because authority, safe access, evidence integrity, scope, handling, or another governed prerequisite prevents evaluation.

Rules:

- do not assign a numeric maturity score;
- retain the applicable weight unless the assessment contract legitimately excludes the criterion;
- record the blocking reason and owner/gate;
- apply `HALT` when the block prevents a defensible assessment decision or violates a critical boundary.

### `NOT_APPLICABLE`

Use only when the control genuinely does not apply to the bounded subject and the rationale is documented.

Rules:

- remove the individual criterion from applicable criterion weight;
- do not treat it as evidence of strength or weakness;
- do not use `NOT_APPLICABLE` to hide missing evidence or weak controls;
- do not apply it to every criterion in a domain to remove that domain from AICR v0.1.

## Evidence coverage

Evidence coverage remains separate from readiness:

```text
domain_coverage =
  sum(known_criterion_weight)
  / sum(applicable_criterion_weight)

coverage =
  sum(domain_coverage × canonical_domain_weight)
  / 100
```

Every one of the seven canonical domain weights participates in the coverage denominator. An unscored all-`UNKNOWN` or all-`blocked` domain contributes zero known coverage while retaining its full canonical weight. An attempted whole-domain exclusion invalidates the v0.1 run; it does not reduce the denominator.

Coverage answers how much of the applicable weighted control surface is supported by admissible evidence. It does not answer how mature the controls are.

## Confidence treatment

Confidence is not a score multiplier and does not change the domain or readiness score.

Confidence remains a separate signal derived from evidence quality, scope, recency, integrity, corroboration, and contradiction.

Confidence affects:

- assertion strength;
- validation requirements;
- uncertainty/range treatment;
- publication eligibility;
- recommendation language;
- DecisionLedger rationale.

Confidence must not:

- increase a weak control's maturity score;
- decrease a strong control's maturity score;
- convert missing evidence into failure;
- resolve contradictory evidence by averaging;
- authorize implementation.

## Publication relationship

Weight completion alone never authorizes publication.

The active scoring profile requires, at minimum, for an `official` result:

- at least 80% evidence coverage;
- known evidence in all seven domains;
- no unresolved material contradiction;
- independent review complete.

A high readiness score with inadequate coverage or unresolved critical evidence remains provisional, range-only, blocked, or internal-only according to the publication standard.

## Critical-gate precedence

Critical controls are not diluted by weights.

A verified condition such as unbounded consequential action authority, absent accountable ownership, inability to enforce least privilege for material access, missing required human decision boundaries, absent defensible evaluation/release gates, unreconstructable material actions, or absent critical containment/rollback/incident routes can route `HALT` regardless of aggregate score.

## Examples and edge cases

### Example 1 — Unknown is not zero

A domain has four equally weighted applicable criteria. Three are scored `100`, `75`, and `50`; one is `UNKNOWN`.

```text
observed domain score = (100 + 75 + 50) / 3 = 75
coverage = 3 / 4 = 75%
```

The unknown criterion is not scored as `0`. The domain reports observed performance `75` with 75% coverage and the unknown remains explicit.

### Example 2 — All criteria unknown in one domain

`AIGR-D2` has three equally weighted applicable criteria. All three are `UNKNOWN`.

```text
known criterion weight = 0
domain_score = null
domain_status = UNSCORED
domain_coverage = 0%
```

`AIGR-D2` contributes no value and no weight to the observed-readiness numerator or denominator. Its canonical 15% remains in the full-profile evidence-coverage calculation, and the missing known evidence prevents `official` publication.

### Example 3 — Partial-known domains

`AIGR-D1` has two equal applicable criteria: one scores `80`, one is `UNKNOWN`. `AIGR-D2` has three equal applicable criteria: two score `50` and `100`, one is `UNKNOWN`. `AIGR-D3..D7` are entirely `UNKNOWN`.

```text
D1 domain score = 80; D1 coverage = 1/2 = 50%
D2 domain score = (50 + 100) / 2 = 75; D2 coverage = 2/3 = 66.67%

observed readiness = ((80 × 10) + (75 × 15)) / (10 + 15) = 77
evidence coverage = ((50% × 10) + (66.67% × 15) + (0% × 75)) / 100 = 15%
```

Readiness `77` describes only observed controls. Coverage `15%` separately exposes the evidence gap, so the result is not official and cannot route `ALLOW`.

### Example 4 — Attempted whole-domain exclusion

An evaluator marks every `AIGR-D7` criterion `NOT_APPLICABLE` and attempts to normalize D1–D6 to 100%.

```text
profile_valid = false
readiness_score = null
publication_state = blocked
control_gate = HALT
```

The six-domain normalization is rejected. AICR v0.1 remains seven-domain; a structurally different scope requires a separately versioned and explicitly approved profile.

### Example 5 — Individual criterion not applicable

A domain has four equal criteria. One is legitimately `NOT_APPLICABLE`; the other three score `75`, `75`, and `100`.

```text
observed domain score = (75 + 75 + 100) / 3 = 83.33
applicable criteria = 3
known criteria = 3
coverage = 100%
```

The excluded criterion neither helps nor harms the score.

### Example 6 — Contradictory evidence

Configuration evidence indicates a tool action requires approval, while an authorized test demonstrates the action completing without the expected approval event.

Do not average the two observations into a numeric compromise. Preserve the contradiction, constrain confidence, determine whether the criterion is `PARTIAL_CONTROL`, `VERIFIED_GAP`, or `UNKNOWN` under the domain sheet, and apply the applicable governance gate.

### Example 7 — High aggregate score with critical failure

Six domains score highly, but admissible evidence shows an in-scope agent has unbounded consequential action authority with no enforceable approval boundary.

The aggregate weighted score may still exceed 75. The decision does **not** become `ALLOW`; the critical gate takes precedence and routes `HALT` / `NOT_READY` according to the scoring profile.

### Example 8 — Cross-domain evidence without duplicate credit

An IAM export shows an agent service identity has write access to a CRM. The same evidence may support:

- D2: whether identity/access is least-privilege and understood;
- D3: contextual proof that a tool can perform a consequential write action.

The access-control criterion receives weighted credit only in D2. D3 must score its own action-authority criterion using its own control expectation, even if it references the same evidence record.

## Legacy-model authority conflict

`scoring/weight-rules.md`, `scoring/weights.md`, `scoring/category-sheets/website.md`, and related SEO/GBP/messaging/conversion artifacts belong to the earlier Business Growth Systems Assessment / contractor-local-service model.

The complete legacy contract remains authoritative at `scoring/weight-rules.md`. Those artifacts are not canonical inputs for AICR. The AICR v0.1 authority is this file at `scoring/aicr/weight-rules.md`, with the profile boundary declared by `playbooks/agentic-control-platform-readiness/scoring-profile.md`.

Therefore:

- do not copy those weights into AICR domain sheets;
- do not build `website.md` as the first active AICR category sheet;
- do not delete or rewrite the legacy artifacts in this increment;
- preserve them as legacy until a separately authorized archival, namespace, or migration decision is made;
- the next active scoring-sheet work must use the seven `AIGR-D1..D7` domains.

This resolves the Stage 3B website authority check as **HALT for active-model use**, not as a defect in the legacy product.

## Governance states for this artifact

**ALLOW**

- seven domain weights match the canonical AICR scoring profile;
- total equals 100%;
- confidence remains separate from maturity;
- unknown remains non-numeric;
- critical gates override aggregate scores;
- no duplicate weighted ownership exists.

**REVIEW**

- an internal criterion-weight proposal lacks validation examples;
- a separately versioned profile is proposed because one canonical domain is structurally inapplicable;
- a new scoring profile is proposed but not yet approved.

**HALT**

- domain weights conflict with the canonical profile;
- unknown is scored as zero;
- confidence modifies maturity;
- a critical gate is diluted by aggregation;
- the same control earns weighted credit in multiple domains;
- legacy contractor weights are presented as active AICR weights;
- a domain sheet silently overrides this file;
- any consumer points legacy assessment work at the AICR path or AICR work at the legacy path;
- a whole domain is excluded or the remaining six domains are normalized under AICR v0.1;
- no domain has known weighted evidence and readiness is reported as numeric.

## Validation method

Validation for this file requires:

1. Confirm legacy consumers continue to resolve to `scoring/weight-rules.md` and AICR consumers resolve only to `scoring/aicr/weight-rules.md`.
2. Recalculate the seven domain weights to confirm a 100% total.
3. Compare every weight against `playbooks/agentic-control-platform-readiness/scoring-profile.md`.
4. Confirm the domain names and ownership model match the AICR seven-domain contract.
5. Reproduce the all-unknown-domain, partial-known-domain, attempted-domain-exclusion, contradictory-evidence, and critical-gate cases.
6. Confirm zero known domain weight returns `null` without division by zero or zero coercion.
7. Confirm all seven weights remain in evidence coverage and publication eligibility.
8. Confirm downstream AICR domain sheets contain references only and no competing domain-level weights.

## Known limitations

- Internal criterion weights are not yet defined for the seven domains; equal applicable weighting is the controlled default.
- The supported legacy model remains at its stable paths. Its coexistence is intentional and governed by the explicit profile-selection boundary; no migration or deletion is authorized here.
- No seven-domain Stage 3B domain sheets or regression fixtures are approved by this file alone.
- This artifact does not validate field reliability, customer outcomes, compliance, security, ROI, or implementation effectiveness.

## v1.0 connection

This file does not rewrite the earlier Business Growth Systems Assessment v1.0 scoring model. It establishes the Stage 3B canonical weight control for the post-v1 Agentic AI Control Readiness commercial profile authorized in Issue #69 and merged through AICR v0.1.

## Next action

Do not begin `AIGR-D1` solely because this scoring repair passes. The first active AICR domain sheet may proceed only after the commercial-readiness / first-paid-pilot gate independently justifies it, and must target `AIGR-D1 — Purpose and ownership`, not `website.md`.

Do not modify legacy category sheets until a separate authority decision defines their archival or namespace treatment.
