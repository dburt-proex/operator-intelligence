# Evidence Validation Playbook

Version: v1.0 commercial operating playbook  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Governed evidence-admission workflow

## 1. Purpose

Use this playbook to decide whether collected material is admissible for scoring, findings, recommendations, publication, package eligibility, roadmap decisions, or implementation planning.

It operationalizes the evidence and confidence standards. It does not replace the Evidence Register, scoring rules, DecisionLedger, QC, or publication approval.

## 2. Inputs

- approved intake scope and exclusions
- access/testing authorization
- evidence register and source artifacts
- criteria library and category sheets
- current finding/recommendation records
- publication target
- DecisionLedger

## 3. Outputs

- accepted, limited, rejected, superseded, unknown, and blocked evidence states
- evidence class, strength, confidence support, limitations, and traceability
- duplicate-ownership decisions
- contradiction and validation register
- evidence coverage inputs
- ALLOW/REVIEW/HALT decision
- ledger events for material decisions

## 4. Validation sequence

### 4.1 Scope and authorization

For every item verify:

- it is inside approved systems, channels, locations, date range, and test boundary
- collection and storage were authorized
- privacy, confidentiality, retention, and sharing rules are satisfied
- the item represents the stated source and period

Missing authority or material scope integrity requires HALT.

### 4.2 Canonical identity and provenance

Required:

- stable Evidence ID
- capture date and collector
- source type, owner, location, and source date
- scope, sample scope, capture method, and observation
- authorization, storage, and integrity reference
- reviewer and review state

A client statement remains reported/Class E context until its use and reliability are admitted. Public absence does not prove internal absence.

### 4.3 Evidence class and strength

| Class | Use |
|---|---|
| A | Direct observation/test; may support scoring/findings after admission |
| B | Defined comparative evidence; comparability must be recorded |
| C | Approved pattern applied to visible evidence; requires criterion permission |
| D | Inference; validation only, not independent negative scoring or routing |
| E | Client-provided material; use depends on completeness, reliability, corroboration, and scope |

Class, evidence strength, confidence support, and review state remain separate.

### 4.4 Relevance and sufficiency

Evidence must support or contradict a specific criterion, finding, claim, limitation, or validation requirement.

Limit when evidence is:

- stale for the decision
- incomplete or narrow
- ambiguous
- nonrepresentative
- disconnected from the governed subject
- unable to support the proposed assertion strength

Multiple copies of one underlying signal do not increase evidence strength.

### 4.5 Duplicate ownership

For repeated signals:

1. identify the source condition
2. identify transformed or syndicated copies
3. assign one weighted owner
4. mark other uses reference-only
5. ledger material ownership decisions

Duplicate weighted ownership requires HALT.

### 4.6 Contradictions

Retain conflicting evidence. Record:

- evidence IDs
- disputed condition
- resolution action
- effect on score, confidence, finding, route, roadmap, and publication
- owner and deadline/condition

Use REVIEW for bounded conflicts. Use HALT when unresolved conflict can materially alter the client decision.

### 4.7 Unknown and blocked states

- `unknown`: available evidence cannot determine the condition.
- `blocked`: evidence may exist but access, authority, timing, or system constraints prevent validation.

Both states remain visible, are not score zero, reduce coverage where applicable, cannot independently create negative findings, and normally route to Phase 0 before implementation.

### 4.8 Confidence support

Assign confidence based on the weakest material evidence dependency, considering:

- directness
- provenance and integrity
- recency
- scope/sample coverage
- corroboration
- contradiction
- authorization and reproducibility

Confidence cannot exceed evidence quality and never modifies maturity or priority.

### 4.9 Coverage inputs

Record applicable, known, unknown, blocked, and not-applicable weight under the scoring specification. Do not independently publish a score from the evidence register.

### 4.10 Downstream-use decision

Evidence may support a governed finding only when:

- identity and provenance resolve
- scope and authorization pass
- review state permits use
- weighted ownership is unique
- contradictions and limitations are resolved or disclosed
- confidence support is appropriate
- unknown/blocked handling is correct

Evidence does not directly authorize a package, roadmap item, report, or implementation action.

## 5. Decision gates

### ALLOW

The evidence is admissible for its stated bounded use.

### REVIEW

A limitation, contradiction, recency, sample, or authority question requires qualified judgment or validation.

### HALT

Use for unauthorized collection, broken provenance/integrity, duplicate weighted ownership, material unresolved contradiction, unknown-as-failure treatment, unsupported assertion strength, or missing traceability.

## 6. Decision record

```yaml
evidence_validation_id: OI-EVVAL-YYYY-NNN
evidence_refs: []
intended_uses: []
accepted_uses: []
limited_uses: []
rejected_uses: []
unknowns: []
blocked_conditions: []
contradictions: []
duplicate_owner_decisions: []
confidence_support: high|medium|low|unknown
review_state: ALLOW|REVIEW|HALT
reviewer: ""
ledger_refs: []
```

## 7. Recovery and supersession

When evidence changes:

1. preserve the prior record
2. create a new source/version
3. link supersession
4. reassess dependent scores, findings, recommendations, routes, roadmaps, reports, and authorizations
5. rerun QC

## 8. Completion checklist

- [ ] Scope and authorization pass.
- [ ] Canonical fields resolve.
- [ ] Class, strength, confidence support, and review state are separate.
- [ ] Reported/inferred material is not presented as verified fact.
- [ ] Duplicate and contradiction controls pass.
- [ ] Unknown and blocked states remain visible.
- [ ] Coverage inputs reproduce.
- [ ] Material decisions are ledgered.
- [ ] Downstream use is bounded.

## 9. Commercial v1.0 connection

This playbook makes evidence admission repeatable and defensible across assessors, protecting every downstream score, finding, recommendation, and report.

## 10. References

- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `templates/evidence-register.md`
- `templates/quality-control-checklist.md`