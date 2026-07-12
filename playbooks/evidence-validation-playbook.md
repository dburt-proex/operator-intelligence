# Evidence Validation Playbook

## Purpose

Use this playbook to determine whether collected evidence is admissible for scoring, findings, recommendations, publication, or implementation planning.

It operationalizes the repository evidence gates without replacing the Evidence Register, scoring rules, finding standards, recommendation standards, or DecisionLedger.

## Required inputs

- Approved assessment scope
- Completed client intake
- Evidence Register
- Applicable criteria and scoring sheets
- Finding Register
- DecisionLedger
- Current publication state

## Required outputs

- Validated Evidence Register
- Evidence coverage result
- Material unknown and blocked-condition register
- Confidence decisions
- Finding authorization state
- DecisionLedger references for material decisions

## Validation sequence

### 1. Confirm scope and authorization

For each evidence item, confirm:

- the source is inside the approved assessment scope;
- access and collection were authorized;
- collection did not exceed privacy, confidentiality, or testing limits;
- the evidence represents the stated system, workflow, owner, and date range.

Use `HALT` when authorization, scope, or handling integrity cannot be established.

### 2. Verify provenance

Record or confirm:

- stable Evidence ID;
- source type and source owner;
- collection method and collection date;
- represented date range;
- original artifact or resolvable reference;
- analyst responsible for collection;
- verification state.

A client statement remains `reported` until corroborated. Missing access is not negative evidence. Public absence does not prove internal absence.

### 3. Test relevance and sufficiency

An item is admissible only when it directly supports or contradicts a defined criterion, finding, limitation, or validation requirement.

Mark evidence as insufficient when it is outdated, incomplete, non-representative, materially ambiguous, or disconnected from the decision being made.

Do not increase confidence by accumulating multiple copies of the same underlying signal.

### 4. Resolve duplicates and ownership

For each repeated signal:

1. identify the original source;
2. identify transformed, quoted, summarized, or syndicated copies;
3. assign one weighted criterion owner;
4. retain secondary references as non-weighted context;
5. record the ownership decision when it materially affects scoring.

Duplicate weighted ownership requires `HALT` until corrected.

### 5. Preserve contradictions

Do not remove evidence because it conflicts with the leading interpretation.

For each contradiction, record:

- conflicting Evidence IDs;
- the exact disputed condition;
- whether the conflict is resolvable;
- the validation action required;
- the effect on confidence, scoring, findings, and publication.

Use `REVIEW` for resolvable contradictions. Use `HALT` when the contradiction can materially change a score, package route, roadmap phase, or executive conclusion and remains unresolved.

### 6. Classify unknown and blocked conditions

Use:

- `unknown` when the condition cannot be determined from available evidence;
- `blocked` when required evidence exists in principle but access, authorization, timing, or system constraints prevent validation.

Unknown and blocked conditions:

- remain visible;
- are not scored as zero;
- do not support negative findings;
- reduce evidence coverage where applicable;
- route to validation before implementation.

### 7. Assign confidence

Confidence must reflect the weakest material link in the evidence chain.

Use the repository-controlled confidence vocabulary. Document:

- confidence level;
- evidence basis;
- contradictory evidence;
- material limitations;
- conditions that would change the decision.

Confidence cannot exceed evidence quality, provenance integrity, scope coverage, or contradiction status.

### 8. Calculate evidence coverage

Calculate coverage using only criteria eligible for the approved assessment scope.

Exclude unknown and blocked criteria from achieved points, but keep their eligible weight visible. Report:

- verified weighted coverage;
- reported-only weighted coverage;
- unknown weighted coverage;
- blocked weighted coverage;
- total eligible weight.

Do not publish an Operator Score without the coverage disclosure required by the scoring and publication standards.

### 9. Authorize downstream use

Evidence may support a finding only when:

- provenance is resolvable;
- scope and authorization pass;
- weighted ownership is unique;
- material contradictions are resolved or disclosed;
- confidence is evidence-bounded;
- unknown and blocked states are correctly preserved.

Evidence may support implementation routing only after the related finding and recommendation pass their own approval gates.

### 10. Record material decisions

Create or reference DecisionLedger records for material:

- admissibility exceptions;
- duplicate ownership decisions;
- confidence overrides;
- contradiction resolutions;
- unknown or blocked treatment;
- score-impact decisions;
- publication restrictions;
- supersession events.

Approved evidence records are corrected through supersession or controlled update history, never silent replacement.

## Decision gates

### ALLOW

Use when all material evidence is authorized, traceable, admissible, uniquely owned, and sufficient for the intended downstream decision.

### REVIEW

Use when uncertainty is bounded and resolvable without invalidating the assessment, score, package route, or executive conclusion.

### HALT

Use when any of the following exists:

- unauthorized collection or access;
- broken provenance or artifact integrity;
- duplicate weighted ownership;
- material unresolved contradiction;
- unknown treated as a failure;
- confidence exceeding the evidence chain;
- unsupported downstream claim;
- missing required DecisionLedger traceability.

## Completion checklist

- [ ] Scope and authorization verified
- [ ] Every material item has a stable Evidence ID
- [ ] Provenance and represented date range recorded
- [ ] Reported claims are distinguished from verified evidence
- [ ] Duplicate signals have one weighted owner
- [ ] Contradictions remain visible and governed
- [ ] Unknown and blocked conditions remain unscored
- [ ] Confidence is evidence-bounded
- [ ] Evidence coverage is reproducible
- [ ] Finding authorization is explicit
- [ ] Material decisions are traceable in the DecisionLedger
- [ ] Publication restrictions are recorded

## Cross-references

- `templates/client-intake.md`
- `templates/evidence-register.md`
- `templates/finding-register.md`
- `templates/recommendation-register.md`
- `standards/decision-ledger-standard.md`
- `standards/quality-control-standard.md`
- `standards/recommendation-standard.md`
- `standards/roadmap-standard.md`
