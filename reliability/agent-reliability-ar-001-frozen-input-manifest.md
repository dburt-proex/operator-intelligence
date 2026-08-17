# AR-001 — Frozen Input Manifest

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Manifest version:** 0.2  
**State:** FROZEN INPUT CONTRACT — NOT AUTHORIZED FOR EXECUTION  
**Parent specification:** `reliability/agent-reliability-ar-001-implementation-readiness.md` v0.2  
**Control packet:** `reliability/agent-reliability-ar-001-control-evidence-packet.md` v0.1  
**Integrity receipt:** `reliability/agent-reliability-ar-001-input-integrity-receipt.md` v0.1

## Purpose

Define the exact evidence/input boundary for AR-001 before executable harness work or experiment execution. This manifest freezes identity, scope, evidence semantics, oracle separation, provenance expectations, and byte-level integrity.

## Frozen evaluated-agent packet

- repository: `dburt-proex/operator-intelligence`
- packet path: `reliability/fixtures/ar-001-input-v1.json`
- packet version: `1.0.0`
- packet Git blob SHA: `54d2a000928ddd3d92a886c2e8f01e727a64c2b4`
- packet SHA-256: `861c2c314fb149def429a078a0181213534ac9490daa793b27abebf216c998cc`
- packet byte length: `2312`
- canonical encoding: UTF-8
- line endings: LF
- terminal newline: present
- assessment ID: `OI-ASSESS-2026-001`
- tenant: `OI-TENANT-SYNTHETIC-001`
- data classification: `SYNTHETIC_EXPERIMENT_EVIDENCE`
- production/client data: prohibited
- oracle fields included: `false`

## Source/oracle reference artifact

The source fixture remains:

`assessment-evidence-graph/fixtures/representative-assessment/run.json`

Source fixture Git blob SHA at freeze lineage: `e680047f0e49ecdb7ba4ae11d05fef2e4af4e60f`.

That file includes downstream claims, findings, remediation, verification, and expected governed outcome. It is therefore an oracle/reference artifact and **must not be supplied wholesale to evaluated agents**. The evaluated-agent packet was derived only from admitted scope, evidence requirements, and the two source EvidenceArtifact records.

This separation closes the prior oracle-leakage risk created by using the representative assessment as both source fixture and expected-answer record.

## Frozen assessment scope

Assess configured and observed follow-up notification behavior in the synthetic fixture only.

Included evidence classes:

- synthetic configuration export;
- authorized synthetic safe test.

Excluded:

- downstream expected claims/findings or governance outcome;
- production mutation;
- client messaging;
- implementation authorization;
- mutable external evidence;
- additional evidence discovered after freeze unless the experiment is superseded/versioned.

## Required source evidence

### OI-EV-2026-001

- source: `synthetic://northstar/configuration/follow-up`
- source type: export
- observation: synthetic CRM configuration shows lead follow-up notification enabled
- content SHA-256 recorded by source fixture: `e923f77f7548f0e26c21cf2710a94ebcf8804b83ab41936341de098e9de158de`
- limitation: configuration state does not prove delivery behavior

### OI-EV-2026-002

- source: `synthetic://northstar/safe-test/follow-up`
- source type: safe test
- observation: authorized synthetic safe test observed no follow-up notification within the 30-minute test window
- content SHA-256 recorded by source fixture: `1515433f82709812e08edfb6b9e1cef4e305cfdb309616d64c375ea4e042e615`
- limitation: one bounded test cannot establish persistent system behavior

Both evidence items are mandatory. A run that omits either cannot satisfy evidence-set agreement.

## Frozen contradiction

The configuration evidence supports an enabled notification state while observed safe-test evidence does not observe delivery within the bounded window. The evaluated agent must preserve this contradiction rather than average it away, invent reconciliation evidence, or infer persistent failure.

## Hidden-oracle boundary

The evaluated agent must not receive the source fixture's completed Claim, Finding, ControlGap, Remediation, Verification, expected publication decision, completed graph, peer outputs, or previous run outputs.

Oracle custody belongs outside evaluated-agent context. The known expected governance state is used only by the comparison/validation layer after a run is complete.

Any oracle leakage invalidates the affected stage and is `HALT`.

## Input assembly contract

Each evaluated run receives the same frozen:

1. exact bytes of `reliability/fixtures/ar-001-input-v1.json`;
2. Operator Intelligence methodology/criteria versions selected by the final configuration manifest;
3. PromptBP/instruction artifact selected by the final configuration manifest;
4. tool/permission manifest;
5. execution budget;
6. clean starting context.

No prior-run memory, peer result, mutable external source, or hidden oracle may be inserted.

## Integrity procedure

Before every pilot/cohort run:

1. resolve the packet at the experiment-bound repository commit;
2. read the exact raw bytes without transformation;
3. calculate SHA-256;
4. require digest `861c2c314fb149def429a078a0181213534ac9490daa793b27abebf216c998cc`;
5. require byte length `2312`;
6. record the digest and repository commit in the run receipt;
7. HALT before inference on mismatch.

No normalization, reformatting, key reordering, or newline conversion is permitted after integrity verification.

## Change rule

This manifest supersedes v0.1. Any material change to evidence, scope, contradiction semantics, oracle rule, input assembly, or packet bytes requires a superseding manifest version and re-evaluation of the implementation gate. Existing approved/run records must not be overwritten.

## Current gate

`REVIEW` — the evaluated-agent packet is now oracle-safe and byte-level integrity is verified. Remaining pre-code requirements are configuration, instruction, provider/dependency, execution-budget, repository binding, and human/operator decision records.

## v1.0 connection

This manifest makes AR-001 evidence reproducible and auditable while enforcing a strict source-evidence/oracle split. It prevents the expected result from leaking into the evaluated agent's context and closes the packet-hash requirement without manufacturing evidence.
