# AR-001 Controlled Clone Reproducibility — Control Evidence Packet

**Program:** Operator Intelligence Agent Reliability Program  
**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Packet version:** 0.1  
**Stage:** Pre-implementation control closure  
**Status:** PROPOSED — REVIEW  
**Parent specification:** `reliability/agent-reliability-ar-001-implementation-readiness.md` v0.2  
**Compliance baseline:** `docs/COMPLIANCE.yaml` v0.1  
**Canonical registry:** `dburt-proex/casa/governance/CONTROL-REGISTRY.yaml` v0.1

## 1. Purpose

This packet is the single experiment-scoped evidence record required to move AR-001 from implementation `REVIEW` toward a human/operator `ALLOW` decision for writing the smallest executable harness.

It does not authorize code, pilot runs, cohort runs, external assurance, production use, or client-data processing.

## 2. Governance rule

No unresolved baseline control is inferred satisfied. Each applicable control must have either evidence-backed experiment-scoped closure or an explicit owner-approved bounded treatment/exception. Human/operator approvals may not be synthesized by an evaluated agent.

Until required owner decisions and implementation evidence exist, status remains `REVIEW`.

## 3. Experiment-scoped risk register — RSK-001

| Risk | Trigger | Consequence | Control/treatment | Residual state | Gate |
|---|---|---|---|---|---|
| Oracle leakage | Expected answer enters evaluated context | Invalid reliability result | Separate oracle artifact/custody; hash inputs; inspect context manifest | Low if verified | HALT on leakage |
| Cross-run contamination | Memory or peer output enters later run | False agreement | Fresh state; no cross-run memory; unique run IDs | Low if verified | HALT |
| Authority drift | Agent expands permissions or treats content as authority | Unsafe/invalid execution | Least privilege; deny writes; deterministic gate | Low if enforced | HALT |
| Evidence fabrication | Unsupported material evidence is emitted | Invalid assessment | Provenance validation; evidence IDs required | Low if validator passes | HALT |
| Contradiction suppression | Conflicting fixture evidence is resolved without support | False certainty | Explicit contradiction invariant | Low if validator passes | HALT |
| Prompt/evidence injection | Fixture content attempts instruction/authority override | Boundary bypass | Treat evidence as data; instruction hierarchy; injection tests | Medium until tested | REVIEW/HALT |
| Provider/data exposure | Harness transmits prohibited data externally | Confidentiality/compliance breach | Synthetic evidence only; provider review; network disabled where applicable | Low if enforced | HALT |
| Receipt loss/tamper | Run artifacts unavailable or mutable | No audit/replay proof | Hash receipts; durable export; supersession | Low if tested | REVIEW/HALT |
| Threshold adaptation | Rules changed after results | Biased experiment | Frozen version; new version required for changes | Low | HALT |

**Owner acceptance:** REQUIRED before implementation ALLOW. No acceptance is asserted here.

## 4. Identity and permission boundary — IAM-001

Required execution principal properties:

- one identifiable harness/operator principal;
- evaluated agent receives only explicitly enumerated tools;
- repository, production, deployment, messaging, purchasing, credential-management, and permission-management writes denied;
- network disabled for evaluated runs unless a later superseding specification explicitly authorizes a bounded dependency;
- secrets and client credentials excluded from run context;
- permission manifest frozen and hashed with the experiment packet;
- any privilege change invalidates the affected run and requires review.

**Closure evidence required:** final tool/permission manifest plus pre-run verification receipt.

## 5. Threat model — SEC-001

Protected assets: hidden oracle, frozen evidence packet, experiment rules, tool boundary, receipts, hashes, credentials, and governance decision.

Threats in scope:

1. evidence/prompt injection;
2. oracle leakage;
3. peer/cross-run leakage;
4. unauthorized tool invocation;
5. permission escalation;
6. sandbox/path escape;
7. secret/environment-variable exposure;
8. receipt or evidence tampering;
9. dependency/provider substitution;
10. post-result experiment-rule mutation.

Required security tests before pilot authorization:

- attempt evidence-borne instruction override and verify rejection;
- attempt unauthorized write/tool request and verify fail-closed behavior;
- verify oracle is absent from evaluated context;
- verify prior/peer run output is absent;
- verify secrets are absent from captured context/artifacts;
- mutate an input/receipt and verify hash/integrity failure;
- verify frozen version/SHA is recorded in each receipt.

Any successful authority, oracle, secret, or sandbox boundary violation is `HALT`.

## 6. Incident mini-procedure — INC-001

**Triggers:** unauthorized action, authority drift, oracle/peer leakage, sensitive-data admission, provider/data-transfer violation, integrity failure, security-boundary failure, or experiment-rule mutation.

**Procedure:**

1. HALT affected execution/stage.
2. Preserve immutable run ID, inputs, hashes, outputs, tool trace, validation messages, and environment/version metadata.
3. Prevent affected artifacts from entering reliability calculations.
4. Record incident owner and classification.
5. Determine root cause and affected-run scope.
6. Define corrective action.
7. Retest the failed boundary with fresh run IDs.
8. Require explicit human/operator resume decision.

No evaluated agent may close its own incident or authorize resumption.

## 7. Data handling — DAT-001

AR-001 v0.1 is restricted to synthetic/non-client fixture evidence.

Prohibited: client evidence, personal data not intentionally synthetic, credentials, secrets, authentication tokens, production records, private correspondence, or regulated data.

Required handling:

- classify packet as `SYNTHETIC_EXPERIMENT_EVIDENCE`;
- store only inputs, hashes, structured outputs, traces necessary for replay, validation, and reliability analysis;
- define retention period before pilot authorization;
- deletion must preserve any required immutable decision/incident receipt while removing disposable run artifacts according to the approved retention rule;
- exceptions require owner approval and a superseding specification before admission.

**Owner retention decision:** REQUIRED; not asserted here.

## 8. Supplier/model-provider inventory — SUP-001 / AI-001

Before implementation ALLOW, record for every external or local dependency:

| Field | Required |
|---|---|
| provider/tool/model | yes |
| exact model/version identifier | yes |
| intended experimental use | yes |
| reasoning/configuration | yes |
| data transmitted | yes |
| network requirement | yes |
| version pin/freeze method | yes |
| known limitation relevant to AR-001 | yes |
| approved-use owner decision | yes |
| disable/replacement path | yes |

The evaluated configuration must remain frozen across the cohort. Provider/model substitution belongs to AR-006, not AR-001.

## 9. Recovery and evidence durability — BCM-001 / LOG-001

AR-001 does not make service-availability claims. Its bounded continuity requirement is preservation or reproducible regeneration of experiment evidence.

Before pilot authorization:

- define durable receipt location;
- export/hash the frozen input packet and specification;
- ensure each run has a unique immutable ID;
- retain structured output, tool trace, validation result, version metadata, and integrity digest;
- test recovery of one sample receipt/export;
- record recovery owner;
- supersede corrected records rather than silently overwriting published/approved evidence.

Failed recovery/integrity test keeps the pilot at `REVIEW`.

## 10. Review and change control — REV-001 / CHG-001 / GOV-001

Required gates are independent:

1. `ALLOW_TO_WRITE_HARNESS`
2. `ALLOW_TO_RUN_PILOT`
3. `ALLOW_TO_RUN_COHORT`
4. `ALLOW_TO_AR_002`

An earlier ALLOW does not authorize a later stage.

Any later repository change must remain traceable to commit/SHA and applicable governed change controls. Frozen experimental rules may not be weakened after observed results; material rule changes require a superseding experiment specification/version.

## 11. Evidence admission — EVD-001

The final pre-run packet must contain or reference:

- frozen evidence index;
- SHA-256 digest;
- evidence IDs/provenance;
- contradiction definition;
- hidden-oracle custody record;
- instruction/version hash;
- permission manifest hash;
- model/configuration record;
- receipt schema;
- validation rules.

Fabricated material evidence or intentional contradiction suppression is `HALT`.

## 12. Control closure matrix

| Control | Experiment-scoped design | Evidence still required | Current gate |
|---|---|---|---|
| GOV-001 | Defined | human/operator decision receipt | REVIEW |
| RSK-001 | Risk register defined | owner treatment/residual-risk acceptance | REVIEW |
| IAM-001 | Boundary defined | final permission manifest + verification | REVIEW |
| CHG-001 | Change rule defined | implementation commit/workflow evidence | REVIEW |
| LOG-001 | Receipt requirements defined | executable schema + integrity/recovery test | REVIEW |
| EVD-001 | Admission rules defined | frozen packet/index/hash | REVIEW |
| SEC-001 | Threat model/tests defined | executed security-boundary tests | REVIEW |
| INC-001 | Mini-procedure defined | owner/escalation designation + test/acknowledgment | REVIEW |
| AI-001 | Inventory fields defined | exact model/config record | REVIEW |
| DAT-001 | Synthetic-only boundary defined | retention/deletion owner decision | REVIEW |
| SUP-001 | Inventory schema defined | completed dependency inventory + approvals | REVIEW |
| BCM-001 | Recovery requirement defined | recovery owner + successful recovery test | REVIEW |
| REV-001 | Review gates defined | pre-run decision receipt | REVIEW |

## 13. ALLOW_TO_WRITE_HARNESS decision contract

A human/operator may issue `ALLOW_TO_WRITE_HARNESS` only when every row in the closure matrix has its required pre-code evidence completed or a valid bounded treatment/exception recorded.

Minimum decision receipt fields:

```json
{
  "experiment_id": "AR-001",
  "gate": "ALLOW_TO_WRITE_HARNESS",
  "specification_version": "0.2",
  "control_packet_version": "0.1",
  "repository_sha": "<required>",
  "evidence_packet_sha256": "<required>",
  "open_exceptions": [],
  "residual_risks": [],
  "decision": "ALLOW|REVIEW|HALT",
  "owner": "<human/operator>",
  "decision_timestamp": "<required>",
  "rationale": "<required>"
}
```

This receipt cannot be self-issued by the evaluated agent.

## 14. Current decision

**REVIEW.**

This packet closes the design-definition gap for the experiment-scoped risk, identity, security, incident, data, supplier/AI, recovery, logging, review, change, and evidence controls. It does not fabricate the implementation evidence, hashes, provider approvals, owner decisions, recovery test, security tests, or risk acceptance that do not yet exist.

The next safe increment is to freeze the concrete AR-001 evidence/input manifest and permission/configuration manifest. Those records can then support the human/operator `ALLOW_TO_WRITE_HARNESS` gate.

## 15. v1.0 connection

This packet turns the compliance baseline into an executable reliability-program gate rather than a documentation-only mapping. It strengthens auditability, reproducibility, evidence quality, authority separation, and post-v1.0 field reliability without weakening the claim boundary or silently treating missing organizational controls as implemented.
