# Agentic AI Control Readiness Weight Rules

**Status:** Stage 3B canonical scoring control — proposed for review  
**Version:** 0.1.0  
**Authority:** Operator Intelligence assessment methodology  
**Active model:** Agentic AI Control Readiness Assessment v0.1  
**Implementation authorization created by this artifact:** `false`

## Purpose

Define the canonical weighting rules, category relationships, confidence treatment, and unknown-data behavior for the active Agentic AI Control Readiness Assessment.

This file is the single Stage 3B source for domain weights. Domain sheets may reference these weights but must not redefine, override, or duplicate them.

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
5. `NOT_APPLICABLE` may remove a criterion from a domain denominator only when the exclusion is evidence-backed and buyer-side rationale is recorded.
6. A whole domain may be excluded only when the assessment contract explicitly places it outside scope and the exclusion does not make the assessment incapable of answering its stated executive decision. Such exclusion requires a DecisionLedger record and publication review.

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

For a domain:

```text
domain_score =
  sum(known_criterion_score × criterion_weight)
  / sum(known_criterion_weight)
```

For the overall observed readiness score:

```text
readiness_score =
  sum(domain_score × active_domain_weight)
  / sum(active_domain_weight)
```

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

- remove the criterion from applicable criterion weight;
- do not treat it as evidence of strength or weakness;
- do not use `NOT_APPLICABLE` to hide missing evidence or weak controls.

## Evidence coverage

Evidence coverage remains separate from readiness:

```text
coverage =
  sum(known_criterion_weight × domain_weight)
  / sum(applicable_criterion_weight × domain_weight)
```

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

### Example 2 — Not applicable is excluded

A domain has four equal criteria. One is legitimately `NOT_APPLICABLE`; the other three score `75`, `75`, and `100`.

```text
observed domain score = (75 + 75 + 100) / 3 = 83.33
applicable criteria = 3
known criteria = 3
coverage = 100%
```

The excluded criterion neither helps nor harms the score.

### Example 3 — Contradictory evidence

Configuration evidence indicates a tool action requires approval, while an authorized test demonstrates the action completing without the expected approval event.

Do not average the two observations into a numeric compromise. Preserve the contradiction, constrain confidence, determine whether the criterion is `PARTIAL_CONTROL`, `VERIFIED_GAP`, or `UNKNOWN` under the domain sheet, and apply the applicable governance gate.

### Example 4 — High aggregate score with critical failure

Six domains score highly, but admissible evidence shows an in-scope agent has unbounded consequential action authority with no enforceable approval boundary.

The aggregate weighted score may still exceed 75. The decision does **not** become `ALLOW`; the critical gate takes precedence and routes `HALT` / `NOT_READY` according to the scoring profile.

### Example 5 — Cross-domain evidence without duplicate credit

An IAM export shows an agent service identity has write access to a CRM. The same evidence may support:

- D2: whether identity/access is least-privilege and understood;
- D3: contextual proof that a tool can perform a consequential write action.

The access-control criterion receives weighted credit only in D2. D3 must score its own action-authority criterion using its own control expectation, even if it references the same evidence record.

## Legacy-model authority conflict

The existing `scoring/weights.md`, `scoring/category-sheets/website.md`, and related SEO/GBP/messaging/conversion category artifacts belong to the earlier Business Growth Systems Assessment / contractor-local-service model.

They are not canonical inputs for the active Agentic AI Control Readiness Assessment.

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
- a domain exclusion may materially weaken the assessment decision;
- a new scoring profile is proposed but not yet approved.

**HALT**

- domain weights conflict with the canonical profile;
- unknown is scored as zero;
- confidence modifies maturity;
- a critical gate is diluted by aggregation;
- the same control earns weighted credit in multiple domains;
- legacy contractor weights are presented as active AICR weights;
- a domain sheet silently overrides this file.

## Validation method

Validation for this file requires:

1. Recalculate the seven domain weights to confirm a 100% total.
2. Compare every weight against `playbooks/agentic-control-platform-readiness/scoring-profile.md`.
3. Confirm the domain names and ownership model match the AICR seven-domain contract.
4. Run worked examples for complete evidence, unknown-heavy evidence, contradictory evidence, critical-gate precedence, and not-applicable exclusions.
5. Confirm downstream domain sheets contain references only and no competing domain-level weights.

## Known limitations

- Internal criterion weights are not yet defined for the seven domains; equal applicable weighting is the controlled default.
- Existing root `scoring/weights.md` and contractor category-sheet infrastructure remain in the repository and may confuse consumers until a separate legacy namespace/reconciliation decision is authorized.
- No seven-domain Stage 3B domain sheets or regression fixtures are approved by this file alone.
- This artifact does not validate field reliability, customer outcomes, compliance, security, ROI, or implementation effectiveness.

## v1.0 connection

This file does not rewrite the earlier Business Growth Systems Assessment v1.0 scoring model. It establishes the Stage 3B canonical weight control for the post-v1 Agentic AI Control Readiness commercial profile authorized in Issue #69 and merged through AICR v0.1.

## Next action

Create the first active AICR domain sheet for `AIGR-D1 — Purpose and ownership`, not `website.md`, after reviewing the canonical criteria/control mapping for D1 and defining a deterministic worked fixture.

Do not modify legacy category sheets until a separate authority decision defines their archival or namespace treatment.
