# Operator Intelligence Implementation Onboarding Checklist

Version: v0.1 commercial v1.0 checklist  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed implementation-onboarding template

## 1. Purpose

Use this checklist after proposal acceptance and before implementation begins. It verifies authority, scope, ownership, access, prerequisites, data handling, testing, communication, acceptance, recovery, and DecisionLedger controls.

Onboarding completion does not start work unless a separate implementation authorization is recorded.

## 2. Onboarding identity

```yaml
onboarding_id: OI-ONB-YYYY-NNN
engagement_id: ""
client: ""
proposal_id: ""
package_scope_id: ""
roadmap_item_refs: []
package_id: OI-PKG-XXX-001
package_name: ""
onboarding_owner: ""
decision_authority: ""
implementation_authorized: false
authorization_ref: null
review_state: ALLOW|REVIEW|HALT
ledger_ref: OI-DL-YYYY-NNN
```

## 3. Commercial and scope controls

- [ ] Accepted proposal version resolves.
- [ ] Package eligibility and primary package route resolve.
- [ ] Included, excluded, deferred, and blocked scope are explicit.
- [ ] Fees, third-party costs, payment terms, and change control are accepted.
- [ ] Dependencies and phase sequence are approved.
- [ ] Material assumptions and limitations are visible.

## 4. Authority and ownership

| Role | Name | Authority | Responsibility | Acceptance recorded |
|---|---|---|---|---|
| Client decision owner | | | | |
| Delivery owner | | | | |
| System owner | | | | |
| Data / privacy owner | | | | |
| Reviewer / approver | | | | |
| Escalation owner | | | | |

- [ ] Implementation authorization is separate and resolvable.
- [ ] Owner acceptance is documented.
- [ ] No unresolved authority conflict exists.

## 5. Access and data handling

| System / account | Owner | Access level | Allowed actions | Prohibited actions | Expiration / revocation | Verification evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

- [ ] Least privilege is used.
- [ ] Credential handling method is approved.
- [ ] Personal, confidential, or regulated data is classified.
- [ ] Storage, retention, redaction, deletion, and sharing rules are documented.
- [ ] Test data and production data boundaries are explicit.
- [ ] Access revocation owner is named.

## 6. Requirements and prerequisites

- [ ] Root finding and recommendation refs resolve.
- [ ] Current-state workflow, assets, content, data, and system dependencies are available.
- [ ] Required client approvals are complete.
- [ ] Phase-specific entry gates pass.
- [ ] AI readiness gates pass for Phase 4.
- [ ] No unresolved HALT blocks the work.

## 7. Delivery plan

| Work item | Owner | Input | Output | Dependency | Acceptance criterion | Evidence | Target window |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Planning windows are assumptions unless expressly contracted.

## 8. Testing, recovery, and escalation

- [ ] Test environment or safe test method is defined.
- [ ] Expected and prohibited outcomes are documented.
- [ ] Rollback or recovery path exists where material.
- [ ] Failure, privacy, customer-impact, security, and quality escalation routes are defined.
- [ ] Stop/HALT authority is named.
- [ ] Incident and decision logging requirements are defined.

## 9. Communication and review cadence

| Review | Cadence / trigger | Participants | Required evidence | Decision authority | Record location |
|---|---|---|---|---|---|
| | | | | | |

## 10. Acceptance and measurement

- [ ] Acceptance criteria are observable.
- [ ] Required completion evidence is defined.
- [ ] Client acceptance process and owner are defined.
- [ ] Defect and exception handling is defined.
- [ ] Business-outcome measures, baselines, sources, and review windows are separate from completion.

## 11. Onboarding gate

```yaml
scope_control: pass|review|fail
authority_control: pass|review|fail
access_control: pass|review|fail
data_control: pass|review|fail
prerequisite_control: pass|review|fail
testing_control: pass|review|fail
acceptance_control: pass|review|fail
review_state: ALLOW|REVIEW|HALT
implementation_authorized: false
start_condition: ""
blocked_conditions: []
```

- `ALLOW` permits start only when implementation authorization is true.
- `REVIEW` requires bounded correction or accepted exception.
- `HALT` blocks start.

## 12. Commercial v1.0 connection

This checklist turns accepted commercial scope into a controlled implementation start state with explicit authority and recovery boundaries.

## 13. References

- `templates/proposal.md`
- `templates/package-catalog.md`
- `templates/roadmap.md`
- `standards/roadmap-standard.md`
- `standards/decision-ledger-standard.md`