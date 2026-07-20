# Operator Intelligence Evidence Register Template

Version: v0.2 template reconciliation  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed evidence source-of-truth template

## 1. Purpose

Use this register as the source-of-truth index for evidence accepted, limited, rejected, superseded, pending validation, or blocked during an Operator Intelligence engagement.

Evidence records support decisions; they do not replace interpretation, scoring, approval, or authorization.

## 2. Register control

```yaml
assessment_id: ""
register_version: ""
methodology_version: ""
evidence_snapshot_date: YYYY-MM-DD
register_owner: ""
reviewer: ""
publication_state: internal_only|official|provisional|range_only|blocked
qc_ref: null
ledger_ref: OI-DL-YYYY-NNN
supersedes: null
```

## 3. Canonical evidence record

Create one record per distinct source, export, test, interview, or observation.

```yaml
evidence_id: OI-EV-YYYY-NNN
assessment_id: ""
captured_at: "YYYY-MM-DDThh:mm:ssZ"
captured_by: ""
source_type: screenshot|url|document|export|system_record|safe_test|interview|observation|third_party
source_location: ""
source_owner: public|client|evaluator|third_party
evidence_class: A|B|C|D|E
source_date: null
scope: ""
sample_scope: ""
capture_method: ""
observation: ""
claim_scope: ""
criterion_ids: []
finding_ids: []
evidence_strength: high|medium|low|insufficient
confidence_support: high|medium|low|unknown
limitations: []
authorization_ref: null
storage_ref: ""
integrity_ref: null
review_state: accepted|limited|rejected|superseded
reviewed_by: ""
reviewed_at: "YYYY-MM-DD"
sensitivity: public|internal|confidential|restricted
retention_requirement: ""
ledger_refs: []
```

## 4. Evidence class and use

| Class | Meaning | Normal decision use |
|---|---|---|
| A | Directly observable or testable | May support scoring/findings when scope and admission pass |
| B | Comparative evidence against a defined set | May support scoring when comparability is documented |
| C | Approved pattern applied to visible evidence | Requires explicit rationale and criterion permission |
| D | Inferred or plausible, not directly verified | Validation only; cannot independently create a negative score or package route |
| E | Client-provided records, exports, screenshots, or statements | Use according to completeness, reliability, corroboration, and scope |

Evidence class does not automatically set confidence.

## 5. Admissibility review

| Gate | Result | Evidence / notes | Failure treatment |
|---|---|---|---|
| Identity | pass / review / fail | | assign ID |
| Attribution | pass / review / fail | | limit or reject |
| Recency | pass / review / fail | | stale / limited |
| Relevance | pass / review / fail | | reject unrelated use |
| Scope | pass / review / fail | | limit assertion |
| Integrity | pass / review / fail | | reject / recapture |
| Authorization | pass / review / fail | | blocked; do not test |
| Traceability | pass / review / fail | | block publication use |
| Limitation | pass / review / fail | | change confidence/publication |

### Admission decision

```yaml
review_state: accepted|limited|rejected|superseded
control_gate: ALLOW|REVIEW|HALT
decision_reason: ""
reviewer: ""
decision_date: YYYY-MM-DD
ledger_ref: OI-DL-YYYY-NNN
```

## 6. Traceability and duplicate control

| Evidence ID | Criterion ID | Category | Finding ID | Use | Weighted owner | Confidence / publication effect |
|---|---|---|---|---|---|---|
| | | | | primary / corroborating / contextual / contradiction | primary / reference-only | |

Rules:

- One record may support several decisions only when every use is explicit.
- One operational condition has one weighted owner.
- Contradictory evidence remains visible and routes to REVIEW.
- Rejected or superseded evidence stays auditable but cannot support new outputs.
- Confidence cannot exceed the supporting evidence chain.

## 7. Unknown and blocked register

| Item ID | Evidence ref | Condition | State | Decision effect | Resolution requirement | Owner | Gate | Status |
|---|---|---|---|---|---|---|---|---|
| | | | unknown / blocked | scoring / finding / routing / publication / authorization | | | REVIEW / HALT | open / resolved / accepted limitation |

Missing access is not negative evidence. Public absence does not prove internal absence.

## 8. Coverage summary

| Category | Applicable weight | Known weight | Unknown weight | Blocked weight | Coverage | Confidence | Publication effect |
|---|---:|---:|---:|---:|---:|---|---|
| | | | | | | | |

This summary does not independently authorize an Operator Score or report publication.

## 9. Supersession and change control

When evidence changes materially:

1. preserve the prior record
2. create a new ID or versioned source reference
3. link prior and superseding records
4. reassess affected scores, findings, recommendations, routes, roadmaps, and publication decisions
5. create a DecisionLedger event

## 10. Pre-release validation

- [ ] Every cited evidence ID resolves.
- [ ] Required canonical fields are complete.
- [ ] Class, strength, confidence support, and review state remain separate.
- [ ] Reported statements are not presented as verified facts.
- [ ] Unknowns, blockers, contradictions, and limitations remain visible.
- [ ] Duplicate weighted ownership is absent.
- [ ] Sensitive evidence has approved handling and retention controls.
- [ ] Admission, rejection, exception, and supersession decisions are ledgered.
- [ ] Publication uses the exact evidence snapshot reviewed.

Any failed authorization, integrity, provenance, traceability, or duplicate-ownership control requires HALT.

## 11. Commercial v1.0 connection

This register makes evidence capture and admission repeatable across assessors and provides the audit foundation for scoring, findings, reports, and implementation decisions.

## 12. References

- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/decision-ledger-standard.md`
- `templates/decision-ledger.md`