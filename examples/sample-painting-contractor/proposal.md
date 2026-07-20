# Northstar Painting Co. — Synthetic Phase 1 Proposal

Version: v1.0 sample proposal  
Stage alignment: Stage 7 — `examples/`  
Status: Fictional commercial example; not accepted and not authorized

## 1. Proposal control

| Field | Value |
|---|---|
| Proposal ID | `OI-PROP-2026-EX001` |
| Assessment | `OI-ASSESS-2026-EX001` |
| Source report | `OI-REPORT-2026-EX001` v1.0 |
| Proposal version | 1.0 |
| Methodology version | commercial-v1.0 |
| Evidence snapshot | 2026-07-20 |
| Source publication state | provisional |
| QC reference | `OI-QC-2026-EX001` |
| Proposal acceptance | pending |
| Implementation authorized | false |
| Ledger reference | `OI-DL-2026-EX021` |

## 2. Objective

Address the verified estimate-path qualification gap through a bounded Website Conversion Fix Pack. The scope is designed to create a clearer and testable painting-project intake path. It does not promise lead, conversion, revenue, or scheduling outcomes.

## 3. Assessment basis

| Finding | Evidence | Confidence | Recommendation | Priority | Gate |
|---|---|---|---|---:|---|
| `OI-FIND-CONV-EX001` | EX003, EX004 | high | `OI-REC-2026-EX001` | 89 | REVIEW prerequisite |

### Prerequisite blocker

The form-routing destination and accountable owner are not yet verified. Phase 0 validation must resolve this condition before implementation authorization.

## 4. Package route

```yaml
package_eligibility: eligible
primary_package_id: OI-PKG-WEB-001
primary_package_name: Website Conversion Fix Pack
roadmap_phase: 1
prerequisite_refs:
  - OI-RM-2026-EX003
routing_ref: OI-DL-2026-EX011
implementation_authorized: false
```

## 5. Proposed scope

| Work item | Deliverable | Acceptance criterion | Acceptance evidence |
|---|---|---|---|
| `OI-WI-2026-EX001` | Approved painting-project field map | Every field has a defined decision use and owner approval | Field map and approval record |
| `OI-WI-2026-EX002` | Updated desktop/mobile estimate form | Approved fields render and validate without blocking the tested path | Screenshots and validation test |
| `OI-WI-2026-EX003` | Confirmation and bounded route | Test submission receives confirmation and reaches the approved destination | Test record and routing receipt |
| `OI-WI-2026-EX004` | Submission event requirement | Approved successful-submission event is observable in the test environment | Event test evidence |
| `OI-WI-2026-EX005` | Handoff note | Owner, form fields, routing, failure escalation, and maintenance responsibility are documented | Approved handoff record |

## 6. Included scope

- service type
- property type
- approximate project scope
- desired timing
- surface or repair context when approved
- optional photo upload when storage, permission, and use pass review
- form labels, validation, confirmation, and safe routing test
- success-event requirement
- bounded handoff documentation

## 7. Excluded scope

- CRM implementation or data migration
- automated estimate or price generation
- AI analysis of photos or project risk
- cabinet service page or project-proof work
- paid media, rebrand, full site redesign, or unrelated custom software
- guaranteed response time, conversion, lead, revenue, ranking, savings, or ROI

## 8. Client responsibilities

| Requirement | Owner | Effect if unavailable |
|---|---|---|
| Approve form owner and routing destination | Fictional operations owner | HALT start |
| Approve fields and decision uses | Fictional estimator/owner | REVIEW scope |
| Provide authorized website access | Fictional website owner | HALT implementation |
| Approve privacy/storage behavior for photos | Fictional data owner | Exclude photo upload or HALT that item |
| Review test evidence | Fictional decision owner | Completion remains pending |

## 9. Planning and commercial terms

This is a structural example only. It intentionally does not invent a real fee, payment schedule, delivery date, tax treatment, or contractual term.

```yaml
pricing_model: to_be_defined_in_real_engagement
package_fee: null
third_party_costs: excluded_unless_listed
planning_window: to_be_defined_after_access_and_prerequisite_validation
change_control: written_approval_and_ledger_update
```

A real proposal must state actual commercial terms before acceptance.

## 10. Change control

Material changes to the package, findings relied upon, fields, data handling, route, acceptance criteria, access, timeline, or commercial scope require written approval and a new or superseding ledger/proposal record.

## 11. Acceptance and authorization

### Proposal acceptance

```yaml
proposal_acceptance: pending
accepted_by: null
accepted_at: null
```

### Separate implementation authorization

```yaml
implementation_authorized: false
authorization_ref: null
authorized_by: null
authorized_at: null
authorized_scope: []
```

Work cannot begin until the prerequisite passes, the proposal is accepted, access is verified, the owner accepts responsibility, and separate implementation authorization is granted.

## 12. Completion and outcome boundary

Completion requires the five work-item acceptance records. It does not establish a change in lead volume, conversion, response time, estimate quality, revenue, or ROI.

## 13. Commercial v1.0 connection

This proposal demonstrates how Operator Intelligence converts one eligible recommendation into bounded sellable scope without inventing price, timing, results, or authorization.