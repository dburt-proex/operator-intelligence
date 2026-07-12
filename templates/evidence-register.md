# Evidence Register Template

Use this register as the source-of-truth index for all evidence admitted, rejected, pending validation, or blocked during an Operator Intelligence assessment.

---

## 1. Register Control

| Field | Value |
|---|---|
| Assessment ID |  |
| Client / system |  |
| Report version |  |
| Evidence snapshot date |  |
| Register owner |  |
| Reviewer |  |
| DecisionLedger reference |  |
| Status | draft / review / approved / superseded |

## 2. Evidence Record

Create one record per distinct source or observation.

| Field | Required entry |
|---|---|
| Evidence ID | Stable unique identifier |
| Title | Plain-language source label |
| Source type | document / system record / interview / observation / test result / public source / client statement |
| Source location | Resolvable path, URL, repository reference, or controlled storage location |
| Source owner | Person or system responsible for the source |
| Collection date | Date obtained or observed |
| Evidence date range | Period represented by the evidence |
| Collector | Person or process that obtained it |
| Verification state | verified / corroborated / reported / pending / rejected / blocked |
| Admissibility | admitted / limited / excluded |
| Confidence | high / medium / low / unknown |
| Scope relevance | Criterion, category, finding, or decision supported |
| Material limitation | Known constraint, ambiguity, age, access gap, or sampling limitation |
| Unknowns introduced | Questions the evidence does not resolve |
| Sensitivity | public / internal / confidential / restricted |
| Retention requirement | Required retention period or controlling policy |
| Integrity check | Hash, version, screenshot date, export ID, or other integrity reference |
| DecisionLedger ID | Ledger record governing admission, rejection, exception, or supersession |
| Supersedes / superseded by | Related Evidence ID, when applicable |
| Notes | Factual handling notes only |

## 3. Verification Rules

- `verified`: directly inspected and attributable to a controlled source.
- `corroborated`: supported by at least one independent admissible source.
- `reported`: supplied through interview, intake, or stakeholder statement without independent verification.
- `pending`: potentially relevant but not yet validated.
- `rejected`: unusable because integrity, relevance, provenance, or reliability requirements failed.
- `blocked`: validation could not be completed because required access, authorization, or source material was unavailable.

A client statement remains `reported` until corroborated. Missing access is not negative evidence. Public absence does not establish internal absence.

## 4. Admissibility Decision

Record the basis for the evidence decision.

| Check | Result | Notes |
|---|---|---|
| Source is attributable | pass / fail / unknown |  |
| Collection method is documented | pass / fail / unknown |  |
| Date range is known | pass / fail / unknown |  |
| Scope relevance is explicit | pass / fail / unknown |  |
| Integrity is sufficient | pass / fail / unknown |  |
| Material limitations are disclosed | pass / fail / unknown |  |
| Handling authorization is valid | pass / fail / unknown |  |
| Duplicate ownership has been checked | pass / fail / unknown |  |

### Decision

- Admissibility: admitted / limited / excluded
- Decision gate: ALLOW / REVIEW / HALT
- Decision reason:
- Reviewer:
- Approval date:
- DecisionLedger ID:

## 5. Criterion and Finding Traceability

| Evidence ID | Criterion ID | Category | Finding ID | Use | Weight ownership | Confidence effect |
|---|---|---|---|---|---|---|
|  |  |  |  | primary / corroborating / contextual / contradiction | primary / reference-only |  |

Rules:

- A source may support multiple decisions, but duplicate weighted ownership is prohibited.
- Contradictory evidence must remain visible and route to review.
- Confidence cannot exceed the supporting evidence chain.
- Unknown or blocked evidence cannot be converted into a numeric failure.
- Findings must cite the exact Evidence IDs used.

## 6. Unknown and Blocked Register

| Item ID | Related Evidence ID | Unknown or blocker | Material effect | Resolution requirement | Owner | Gate | Status |
|---|---|---|---|---|---|---|---|
|  |  |  | scoring / finding / routing / publication / implementation |  |  | REVIEW / HALT | open / resolved / accepted limitation |

Accepted limitations require an explicit DecisionLedger record and must remain visible in client-facing reporting when material.

## 7. Evidence Coverage Summary

| Category | Applicable weight | Admitted evidence weight | Blocked weight | Unknown weight | Coverage % | Confidence |
|---|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |

Do not publish an official Operator Score from this table alone. Publication state must be determined under the publication standard and recorded in the DecisionLedger.

## 8. Supersession and Change Control

When evidence changes materially:

1. Preserve the prior record.
2. Create a new Evidence ID or versioned source reference.
3. Link the superseded and superseding records.
4. Reassess affected criteria, findings, confidence, recommendations, package routes, roadmap items, and publication state.
5. Record the change in the DecisionLedger.

Approved evidence records must not be silently overwritten.

## 9. Pre-Release Validation

- [ ] Every cited Evidence ID resolves to an accessible controlled source.
- [ ] Verification state and admissibility are recorded separately.
- [ ] Reported statements are not presented as verified facts.
- [ ] Unknown and blocked conditions remain visible.
- [ ] Contradictory evidence has been routed to review.
- [ ] Duplicate weighted ownership has been checked.
- [ ] Confidence does not exceed source quality.
- [ ] Sensitive evidence has authorized handling and retention controls.
- [ ] Material admission, rejection, exception, and supersession decisions have DecisionLedger records.
- [ ] Published findings and scores cite the exact supporting Evidence IDs.

Any failed integrity, authorization, provenance, duplicate-ownership, or material traceability check requires `HALT` until resolved or formally superseded.