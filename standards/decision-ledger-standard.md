# Operator Intelligence DecisionLedger Standard

Version: v0.1 commercial-readiness standard  
Stage alignment: `standards/`  
Status: Canonical governance standard

## Purpose

This standard defines the minimum record, control, and traceability requirements for every material Operator Intelligence decision. The DecisionLedger preserves how evidence became a score, finding, recommendation, package route, roadmap action, publication decision, or controlled halt.

The ledger is an audit record, not a substitute for evidence, scoring logic, approval, or client authorization.

## Scope

A DecisionLedger record is required for any material decision that affects:

- criterion or category scoring
- confidence assignment
- unknown, blocked, or not-applicable treatment
- finding creation, revision, suppression, or closure
- recommendation class or priority
- primary package routing
- roadmap phase or dependency sequence
- publication state
- approval, exception, escalation, or halt
- supersession of a prior decision

Routine notes that do not alter assessment state may remain outside the ledger.

## Identifier and immutability

Decision records use the identifier pattern:

```text
OI-DL-YYYY-NNN
```

Identifiers are immutable. Published or approved records must not be silently overwritten. Corrections create a superseding record linked to the prior record.

## Canonical record

```yaml
ledger_id: OI-DL-YYYY-NNN
assessment_id: ""
score_run_id: ""
decision_type: scoring
subject_type: criterion_score
subject_id: ""
prior_ledger_ref: null
supersedes: null
status: draft
decision: ""
rationale: ""
evidence_refs: []
criterion_refs: []
finding_refs: []
recommendation_refs: []
primary_package: null
secondary_packages: []
roadmap_phase: null
dependency_refs: []
confidence: unknown
unknown_state: none
publication_effect: none
control_gate: REVIEW
limitations: []
assumptions: []
validation_required: []
decided_by: ""
reviewed_by: ""
approved_by: ""
decided_at: ""
reviewed_at: null
approved_at: null
methodology_version: ""
change_reason: null
client_safe_summary: ""
```

## Controlled vocabularies

### Decision type

- `scoring`
- `confidence`
- `unknown_handling`
- `finding`
- `recommendation`
- `package_routing`
- `roadmap`
- `publication`
- `exception`
- `approval`
- `halt`
- `supersession`

### Status

- `draft`
- `review_required`
- `approved`
- `rejected`
- `superseded`
- `closed`

### Control gate

- `ALLOW`
- `REVIEW`
- `HALT`

The gate records decision authority. It does not replace publication state or implementation authorization.

### Unknown state

- `none`
- `unknown`
- `blocked`
- `not_applicable`

### Publication effect

- `none`
- `official`
- `provisional`
- `range_only`
- `blocked`
- `internal_only`

## Required fields

Every material record requires:

- immutable `ledger_id`
- assessment or score-run reference
- decision type and governed subject
- explicit decision and rationale
- supporting evidence references, or a documented reason evidence is unavailable
- confidence
- control gate
- limitations and assumptions
- decision owner and timestamp
- methodology version
- client-safe summary when the decision may appear in a report

Records that authorize publication, package routing, roadmap work, exceptions, or `HALT` also require review and approval fields.

## Decision chain

The standard traceability chain is:

```text
Evidence
→ Criterion evaluation
→ Category interpretation
→ Finding
→ Recommendation
→ Primary package
→ Roadmap phase
→ Publication or implementation decision
→ DecisionLedger record
```

A ledger record may reference only the portion of the chain relevant to its decision, but all upstream material references must remain resolvable.

## Evidence and confidence rules

1. The ledger records evidence references; it does not restate or replace evidence objects.
2. Confidence must follow `standards/confidence-standard.md`.
3. Missing access is not negative evidence.
4. `unknown` and `blocked` must not be converted into numeric failure states.
5. Public absence cannot establish that an internal capability does not exist.
6. Conflicting evidence requires `REVIEW` until resolved or explicitly accepted with limitations.
7. A decision cannot carry stronger confidence than its supporting evidence chain.

## Gate rules

### ALLOW

Use only when evidence, authority, dependencies, and applicable standards support the decision without a material unresolved control issue.

### REVIEW

Use when a qualified reviewer must resolve evidence limitations, conflicting interpretations, material unknowns, package dependencies, publication effects, or exceptions.

### HALT

Use when proceeding would violate an evidence gate, publication rule, authorization boundary, required dependency, methodology constraint, or client-safe reporting requirement.

`HALT` blocks dependent decisions until a superseding record resolves the condition.

## Score and finding controls

- Score changes require the prior score reference, reason, evidence, and methodology version.
- Confidence changes must not alter maturity directly.
- Findings require evidence, business relevance, confidence, and a governed subject.
- Suppressed findings remain traceable with the suppression reason.
- Duplicate signals must identify the single weighted owner and any reference-only uses.

## Recommendation and package controls

- Every implementation recommendation must have exactly one primary package.
- Secondary packages are dependency, downstream, or reference relationships only.
- Validation recommendations may precede package selection when evidence is insufficient.
- Package-first selling, unsupported scope expansion, and duplicate ownership are prohibited.
- Material route changes require a superseding ledger record.

## Roadmap controls

- Roadmap phase must follow `standards/roadmap-standard.md`.
- Dependencies cannot be bypassed by priority alone.
- Undefined workflows cannot advance into automation.
- AI work cannot advance without required workflow, data, privacy, review, escalation, logging, and QA controls.
- Completion requires acceptance evidence, not deliverable existence alone.

## Publication controls

- Publication decisions must follow `standards/publication-standard.md`.
- Published scores must disclose evidence coverage and limitations.
- `range_only` and `provisional` states must remain explicit.
- Publication approval does not authorize implementation.
- Unsupported ROI, revenue, lead-loss, conversion, ranking, market-share, or competitor-performance claims are prohibited.

## Supersession and change control

A superseding record must:

1. reference the prior ledger record
2. state what changed
3. identify new or corrected evidence
4. preserve the prior record status as `superseded`
5. record the new review and approval state
6. update dependent finding, recommendation, package, roadmap, or publication references

Deletion of approved ledger history is prohibited except where legally required. Any such removal must retain a controlled removal record.

## Executive-safe language

The `client_safe_summary` must:

- distinguish observation from interpretation
- disclose material limitations
- avoid certainty beyond the evidence
- avoid implying implementation authorization
- avoid unsupported financial or competitive claims
- use plain language suitable for executive review

## Validation codes

| Code | Condition | Severity |
|---|---|---|
| `DL-TRACE-001` | Material decision lacks upstream references | error |
| `DL-EVID-001` | Decision lacks evidence or documented evidence limitation | error |
| `DL-CONF-001` | Confidence exceeds supporting evidence | error |
| `DL-UNKNOWN-001` | Unknown or blocked state converted to failure | error |
| `DL-OWNER-001` | Decision owner or timestamp missing | error |
| `DL-APPROVAL-001` | Controlled decision lacks required review or approval | error |
| `DL-ROUTE-001` | Recommendation lacks exactly one primary package | error |
| `DL-DEPEND-001` | Roadmap or implementation dependency bypassed | error |
| `DL-PUB-001` | Publication effect conflicts with publication standard | error |
| `DL-SUPER-001` | Material change overwrote history without supersession | error |
| `DL-LANG-001` | Client summary contains unsupported certainty or outcome claims | error |
| `DL-DUP-001` | Duplicate signal ownership is unresolved | warning |

## Release checklist

Before a ledger-controlled decision is approved:

- [ ] governed subject and decision type are valid
- [ ] evidence references resolve
- [ ] rationale separates fact, assumption, and interpretation
- [ ] confidence is evidence-derived
- [ ] unknown and blocked states are preserved
- [ ] control gate is justified
- [ ] primary package ownership is valid when applicable
- [ ] roadmap dependencies are enforced
- [ ] publication effect is valid
- [ ] reviewer and approver are recorded where required
- [ ] methodology version is recorded
- [ ] client-safe summary is bounded and supportable
- [ ] prior decisions are superseded rather than overwritten

## Cross references

- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/publication-standard.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `scoring/score-objects.md`
- `framework/findings/`
