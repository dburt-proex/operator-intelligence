# Agentic Control Platform Readiness Control Map

Version: 0.1.0
Model: Vendor-neutral control requirements mapped to seven canonical domains

## Mapping contract

Each control record must include:

```yaml
control_id: ACPR-C-DOMAIN-NNN
domain_id: AIGR-D1|AIGR-D2|AIGR-D3|AIGR-D4|AIGR-D5|AIGR-D6|AIGR-D7
control_plane: governance|change_time|runtime|assurance
control_objective: ""
mechanism: automated|human_approved|human_executed|advisory
system_of_record: ""
owner: ""
evidence_refs: []
state: CONTROLLED|PARTIAL_CONTROL|VERIFIED_GAP|UNKNOWN|NOT_APPLICABLE
confidence: high|medium|low|unknown
control_gate: ALLOW|REVIEW|HALT
dependencies: []
```

Policy or documentation alone cannot satisfy an enforcement objective. A control described as automated must have operating evidence from the relevant enforcement point.

## Canonical control matrix

| Control ID | Domain | Plane | Objective | Minimum operating evidence |
|---|---|---|---|---|
| `ACPR-C-D1-001` | `AIGR-D1` | governance | Maintain an authoritative inventory of AI assets, agents, versions, environments, owners, and lifecycle state | Current inventory export plus lifecycle history |
| `ACPR-C-D1-002` | `AIGR-D1` | governance | Bind each asset to an allowed purpose, prohibited purpose, accountable owner, and decision authority | Approved purpose/ownership records |
| `ACPR-C-D1-003` | `AIGR-D1` | assurance | Detect unregistered, duplicated, stale, third-party, and retired assets | Discovery result and disposition history |
| `ACPR-C-D2-001` | `AIGR-D2` | runtime | Resolve effective human, machine, service, and agent permissions across connected systems | Entitlement export and effective-access trace |
| `ACPR-C-D2-002` | `AIGR-D2` | runtime | Enforce least privilege, separation of duties, environment scope, and time-bounded access | Denied-access test and reviewed grants |
| `ACPR-C-D2-003` | `AIGR-D2` | governance | Bind data sources to classification, purpose, owner, retention, deletion, and residency rules | Data registry and approved use decisions |
| `ACPR-C-D2-004` | `AIGR-D2` | assurance | Review, revoke, and evidence stale, excessive, or orphaned access | Review and deprovisioning records |
| `ACPR-C-D3-001` | `AIGR-D3` | runtime | Enforce allowed tools, operations, parameters, resource targets, and action limits | Policy decision and blocked-action trace |
| `ACPR-C-D3-002` | `AIGR-D3` | runtime | Require approval for consequential actions before execution | Approval-bound tool-call trace |
| `ACPR-C-D3-003` | `AIGR-D3` | runtime | Verify post-mutation state and route partial execution before memory or downstream use | Pre/post state, expected delta, and exception record |
| `ACPR-C-D3-004` | `AIGR-D3` | runtime | Contain, reverse, compensate, or isolate failed and unauthorized actions | Controlled recovery test |
| `ACPR-C-D4-001` | `AIGR-D4` | governance | Define reviewers, authority, thresholds, exceptions, overrides, escalation, and risk acceptance | Approved decision matrix |
| `ACPR-C-D4-002` | `AIGR-D4` | runtime | Enforce approval identity, freshness, target, scope, version, and non-bypass conditions | Accepted and rejected approval traces |
| `ACPR-C-D4-003` | `AIGR-D4` | assurance | Preserve review, exception, override, appeal, and supersession history | Reconstructable decision records |
| `ACPR-C-D5-001` | `AIGR-D5` | change_time | Block changes that fail required evaluation, regression, security, or governance thresholds | Failed-change result and block evidence |
| `ACPR-C-D5-002` | `AIGR-D5` | runtime | Detect behavior, policy, performance, permission, or context drift against defined thresholds | Signal, threshold, and routed event |
| `ACPR-C-D5-003` | `AIGR-D5` | assurance | Version evaluation sets, results, thresholds, limitations, and defect decisions | Evaluation registry and defect disposition |
| `ACPR-C-D6-001` | `AIGR-D6` | runtime | Correlate material inputs, outputs, policies, identities, approvals, tool calls, results, and verification | End-to-end trace with stable IDs |
| `ACPR-C-D6-002` | `AIGR-D6` | assurance | Protect log integrity, access, retention, exportability, and evidence lineage | Integrity verification and governed export |
| `ACPR-C-D6-003` | `AIGR-D6` | governance | Preserve immutable material decisions, supersession, and risk acceptance | DecisionLedger chain |
| `ACPR-C-D7-001` | `AIGR-D7` | change_time | Evaluate code, configuration, prompt, model, policy, permission, data, and workflow changes before acceptance | Change result linked to reviewed diff/version |
| `ACPR-C-D7-002` | `AIGR-D7` | runtime | Monitor material events and route alerts to owned response paths | Alert, owner acknowledgement, and disposition |
| `ACPR-C-D7-003` | `AIGR-D7` | runtime | Isolate, disable, revoke, roll back, or fail closed when critical boundaries fail | Recovery exercise evidence |
| `ACPR-C-D7-004` | `AIGR-D7` | assurance | Preserve incident, recovery, post-incident learning, and control-change evidence | Incident and improvement records |

## Change-time versus runtime test

| Question | Change-time | Runtime |
|---|---|---|
| When does the control act? | Before a proposed change is accepted or released | While an agent, workflow, identity, or platform operates |
| Typical subject | Code, configuration, model, prompt, policy, permission, workflow, dependency | Request, identity, permission, tool call, resource, approval, event, incident |
| Required proof | Reviewed version/diff, evaluated rule, result, gate, and prevented acceptance | Correlated event, effective policy, action/result, verification, and response |
| Failure route | Block merge/release; require review; record exception | Deny, isolate, stop, roll back, alert, escalate, preserve evidence |

Every engagement must assess at least one applicable control from both planes or explicitly record why a plane is `NOT_APPLICABLE`.

## Platform requirement mapping

Buyer requirements should be expressed as capabilities, not vendor feature names:

- authoritative AI asset inventory and discovery;
- lifecycle, ownership, and exception workflows;
- identity graph and effective-permission resolution;
- policy decision and enforcement points;
- change-time evaluation and release gates;
- runtime monitoring, evaluation, containment, and recovery;
- trace correlation, evidence export, and immutable decisions;
- interoperability, portability, data handling, and exit controls.

A product demonstration is supporting evidence about product capability, not proof that the buyer has implemented or operates the control.
