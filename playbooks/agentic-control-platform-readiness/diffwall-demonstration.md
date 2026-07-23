# DiffWall Change-Time Control Demonstration

Version: 0.1.0
Purpose: Provide bounded evidence that change-time controls can evaluate and block unsafe AI-system changes before acceptance

## Demonstration boundary

This demonstration proves a change-time enforcement pattern in a controlled repository fixture. It does not prove the buyer's runtime controls, platform readiness, security posture, regulatory compliance, or production control effectiveness.

The demonstration must use:

- a synthetic or buyer-approved non-production repository;
- no secrets, personal data, restricted evidence, or customer records;
- an approved rule set and expected decisions;
- reversible branches or pull requests;
- no deployment, external communication, or production mutation; and
- a named evaluator and buyer observer.

## Control objective

Demonstrate that a proposed change is evaluated against deterministic policy and routed before acceptance:

```text
Proposed diff
→ Rule evaluation
→ Evidence-bearing finding
→ ALLOW / REVIEW / HALT
→ Merge or release consequence
→ Audit record
```

## Required fixtures

| Fixture | Proposed change | Expected result | Required proof |
|---|---|---|---|
| `DW-ACPR-001` | Approved documentation-only change outside protected paths | `ALLOW` | Rule results, commit/diff identity, decision record |
| `DW-ACPR-002` | Change to identity, permission, policy, or governance configuration | `REVIEW` | Sensitive-path/rule match and required reviewer |
| `DW-ACPR-003` | Secret-like material or prohibited credential path | `HALT` | Blocked acceptance without exposing secret value |
| `DW-ACPR-004` | Destructive operation, unrestricted execution, or unsafe network capability | `HALT` | Deterministic rule and blocked acceptance |
| `DW-ACPR-005` | Large generated or dependency change above threshold | `REVIEW` | Threshold result and reviewer route |
| `DW-ACPR-006` | Attempt to suppress, bypass, or disable required control | `HALT` | Tamper/bypass finding and audit event |

## Demonstration record

```yaml
demonstration_id: DW-ACPR-YYYY-NNN
assessment_id: ""
repository: ""
environment: non_production
diffwall_version: ""
policy_version: ""
fixture_version: ""
authorized_by: ""
authorization_ref: ""
executed_by: ""
executed_at: YYYY-MM-DDThh:mm:ssZ
fixtures:
  - fixture_id: DW-ACPR-001
    commit_or_diff_ref: ""
    expected_gate: ALLOW
    observed_gate: ""
    rule_refs: []
    evidence_refs: []
    passed: false
limitations: []
control_gate: ALLOW|REVIEW|HALT
ledger_refs: []
```

## Pass conditions

- Every fixture resolves to the expected decision.
- Results bind to exact diff/commit, policy version, rule IDs, timestamps, and evaluator.
- `HALT` fixtures cannot be accepted through the normal path.
- `REVIEW` fixtures require the named reviewer path.
- Audit evidence preserves the decision without storing prohibited values.
- A changed rule or fixture creates a new version and superseding result.
- The demonstration produces no production mutation.

## Failure handling

| Failure | Route |
|---|---|
| Expected and observed gate differ | `HALT`; do not use as readiness proof |
| Rule or policy version cannot be resolved | `HALT` |
| Reviewer bypass succeeds | `HALT`; record critical gap |
| Sensitive value appears in evidence | Stop, restrict evidence, follow incident route |
| Only advisory output exists with no acceptance consequence | Record as advisory evidence, not enforcement proof |
| Demonstration passes but buyer integration is untested | Record implementation evidence as `UNKNOWN` |

## Assessment handoff

Map accepted demonstration evidence to:

- `AIGR-D5` for deterministic evaluation and regression control;
- `AIGR-D6` for traceability and audit evidence; and
- `AIGR-D7` for change-time release governance.

The DiffWall demonstration must never be used to infer runtime identity, permission, monitoring, containment, or incident-response effectiveness.
