# Finding Register Template

## Purpose

Use this register to control every material assessment finding from evidence review through recommendation, package routing, roadmap sequencing, publication, and DecisionLedger traceability.

A finding is not publishable merely because an issue appears plausible. It must be supported by admissible evidence, assigned confidence, checked for duplicate ownership, and written in executive-safe language.

## Register metadata

| Field | Required value |
|---|---|
| Assessment ID | Stable assessment identifier |
| Client | Legal or approved client name |
| Assessment version | Current governed version |
| Evidence snapshot date | Date of the evidence set used |
| Publication state | `internal_only`, `provisional`, `range_only`, `official`, or `blocked` |
| Register owner | Accountable analyst |
| Reviewer | Required reviewer for material findings |
| DecisionLedger reference | Ledger record governing this register version |

## Controlled finding states

- `candidate`: observed condition awaiting evidence validation
- `validated`: evidence supports the finding and confidence is assigned
- `suppressed`: duplicate, immaterial, out of scope, or unsupported
- `blocked`: evidence or access is insufficient to determine the condition
- `published`: approved for client-facing release
- `superseded`: replaced by a later governed finding

## Finding record

Create one record per distinct root condition.

| Field | Requirement |
|---|---|
| Finding ID | Stable unique identifier |
| Title | Clear condition statement, not a recommendation |
| Category | Canonical assessment category |
| Criterion IDs | Criteria directly affected |
| Evidence IDs | Admissible supporting evidence |
| Contradictory evidence IDs | Any evidence that materially challenges the finding |
| Evidence state | `verified`, `reported`, `inferred`, `unknown`, or `blocked` |
| Finding state | Controlled finding state |
| Condition | What is demonstrably present, absent, inconsistent, or unresolved |
| Operational effect | Evidence-bounded effect on the operating system |
| Confidence | `high`, `medium`, `low`, or `unknown` |
| Confidence basis | Why the evidence supports that confidence level |
| Material unknowns | Missing facts that could change interpretation |
| Duplicate-owner check | Primary criterion or finding that owns the signal |
| Severity | Governed severity from the scoring framework |
| Score effect | Score relationship or `unscored` |
| Recommendation IDs | Approved recommendations derived from this finding |
| Primary package | Exactly one package when implementation is authorized |
| Roadmap phase | Governed phase or `validation_required` |
| Publication effect | `allow`, `review`, or `halt` |
| DecisionLedger IDs | Records supporting validation, suppression, publication, or supersession |
| Reviewer decision | `ALLOW`, `REVIEW`, or `HALT` |
| Approval date | Date approved or left blank |

## Finding statement structure

Use this sequence:

```text
Condition
→ Evidence
→ Operational effect
→ Confidence and limitations
→ Required decision
```

### Condition

State only the evidenced condition. Do not embed a solution, sales claim, or assumed cause.

### Evidence

Reference the specific Evidence IDs and represented date range. Client statements remain `reported` until corroborated.

### Operational effect

Describe the bounded operational consequence supported by the evidence. Do not claim revenue loss, conversion impact, market-share effect, ranking impact, or ROI unless independently supported by admissible evidence.

### Confidence and limitations

Explain what is known, what remains unknown, and what would materially change the finding.

### Required decision

State whether the finding permits recommendation development, requires validation, or blocks dependent work.

## Evidence and unknown-data rules

- Missing access is not negative evidence.
- Public absence does not prove internal absence.
- Unknown or blocked conditions remain unscored unless the scoring standard explicitly permits another treatment.
- Confidence cannot exceed the supporting evidence chain.
- Contradictory evidence must remain visible and routes the finding to `REVIEW` unless resolved.
- A finding with no resolvable Evidence ID cannot advance beyond `candidate`.

## Duplicate ownership

Each material signal must have one primary finding owner.

A second record may reference the signal only when it represents a distinct root condition. It must not duplicate weighted score impact, recommendation ownership, or implementation scope.

Duplicate ownership that changes score, priority, package routing, or publication state requires `HALT` until resolved.

## Recommendation and package routing

- A finding may support multiple recommendations only when each recommendation addresses a distinct controlled action.
- Every implementation recommendation must route to exactly one primary package.
- Unknown or blocked findings route to validation, not implementation.
- `HALT` findings block dependent roadmap items.
- Priority cannot bypass roadmap prerequisites.
- Phase 4 AI work cannot proceed without required workflow, data, privacy, review, escalation, logging, and QA controls.

## Suppression rules

A finding may be suppressed only when the DecisionLedger records one of these reasons:

- duplicate ownership
- immaterial to the approved scope
- unsupported by admissible evidence
- superseded by a more precise finding
- resolved before publication with verification evidence

Suppression must not conceal an unknown, blocked condition, material contradiction, or release blocker.

## Executive-safe language

Use precise, bounded language:

- “Evidence indicates…”
- “The assessed sample shows…”
- “This condition may constrain…”
- “Validation is required before implementation…”

Do not use guaranteed, universal, or unsupported financial claims.

## Pre-publication validation

A finding can move to `published` only when all applicable checks pass:

- [ ] Finding ID is unique and stable.
- [ ] Scope and criterion references are valid.
- [ ] Evidence IDs are admissible and traceable.
- [ ] Contradictory evidence is disclosed.
- [ ] Confidence matches the evidence chain.
- [ ] Unknown and blocked states are preserved.
- [ ] Duplicate weighted ownership is absent.
- [ ] Score effect is reproducible or explicitly unscored.
- [ ] Recommendation routing is proportional and traceable.
- [ ] Exactly one primary package is assigned when required.
- [ ] Roadmap prerequisites are preserved.
- [ ] Executive language contains no unsupported outcome claim.
- [ ] DecisionLedger approval is complete.
- [ ] Publication state permits release.

Any failed evidence-integrity, duplicate-ownership, unknown-state, score-reproducibility, package-routing, or authorization check requires `HALT`.

## Cross-references

- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`
- `standards/quality-control-standard.md`
- `templates/evidence-register.md`
- `templates/decision-ledger.md`
- `framework/findings/`
