# AR-001 — Frozen Input Manifest

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Manifest version:** 0.1  
**State:** FROZEN FOR HARNESS DESIGN — NOT AUTHORIZED FOR EXECUTION  
**Parent specification:** `reliability/agent-reliability-ar-001-implementation-readiness.md` v0.2  
**Control packet:** `reliability/agent-reliability-ar-001-control-evidence-packet.md` v0.1

## Purpose

Define the exact evidence/input boundary for AR-001 before executable harness work or experiment execution. This manifest freezes identity, scope, evidence semantics, oracle separation, provenance expectations, and integrity procedure. It does not claim a SHA-256 value that has not been independently computed from canonical bytes.

## Frozen fixture identity

- repository: `dburt-proex/operator-intelligence`
- fixture path: `assessment-evidence-graph/fixtures/representative-assessment/run.json`
- fixture Git blob SHA at freeze: `e680047f0e49ecdb7ba4ae11d05fef2e4af4e60f`
- fixture version declared in fixture: `1.0.0`
- fixture run ID: `OI-RUN-2026-001`
- assessment ID: `OI-ASSESS-2026-001`
- tenant: `OI-TENANT-SYNTHETIC-001`
- data classification: `SYNTHETIC_EXPERIMENT_EVIDENCE`
- production/client data: prohibited

The Git blob SHA identifies the repository object but is not represented as the required SHA-256 evidence-packet digest. Before `ALLOW_TO_WRITE_HARNESS`, canonical fixture bytes must be exported and SHA-256 computed and recorded in a superseding integrity receipt or approved update to this manifest.

## Frozen assessment scope

Assess configured and observed follow-up notification behavior in the synthetic fixture only.

Included evidence classes:

- synthetic configuration export;
- authorized synthetic safe test.

Excluded:

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
- content SHA-256 recorded by fixture: `e923f77f7548f0e26c21cf2710a94ebcf8804b83ab41936341de098e9de158de`
- limitation: configuration state does not prove delivery behavior

### OI-EV-2026-002

- source: `synthetic://northstar/safe-test/follow-up`
- source type: safe test
- observation: authorized synthetic safe test observed no follow-up notification within the 30-minute test window
- content SHA-256 recorded by fixture: `1515433f82709812e08edfb6b9e1cef4e305cfdb309616d64c375ea4e042e615`
- limitation: one bounded test cannot establish persistent system behavior

Both evidence items are mandatory. A run that omits either cannot satisfy evidence-set agreement.

## Frozen contradiction

The configuration evidence supports an enabled notification state while observed safe-test evidence does not observe delivery within the bounded window. The evaluated agent must preserve this contradiction rather than average it away, invent reconciliation evidence, or infer persistent failure.

## Hidden-oracle boundary

The evaluated agent must not receive the completed expected graph, canonical answer, expected publication decision, peer outputs, or previous run outputs.

Oracle custody belongs outside evaluated-agent context. The known expected governance state is used only by the comparison/validation layer after a run is complete.

Any oracle leakage invalidates the affected stage and is `HALT`.

## Input assembly contract

Each evaluated run receives the same frozen:

1. source evidence packet represented by this manifest;
2. assessment scope;
3. Operator Intelligence methodology/criteria versions selected by the final configuration manifest;
4. PromptBP/instruction artifact selected by the final configuration manifest;
5. tool/permission manifest;
6. execution budget;
7. clean starting context.

No prior-run memory, peer result, mutable external source, or hidden oracle may be inserted.

## Integrity procedure

Before harness implementation ALLOW:

1. resolve the fixture path at the recorded repository commit;
2. export canonical raw bytes without transformation;
3. calculate SHA-256 over those bytes;
4. record digest, byte length, repository commit SHA, fixture Git blob SHA, timestamp, and responsible operator in an immutable integrity receipt;
5. verify the same digest before every pilot/cohort run;
6. HALT on mismatch.

The required packet SHA-256 remains `validation_required` until that procedure is executed. It is not guessed from Git metadata.

## Change rule

This manifest is frozen at v0.1. Any material change to evidence, scope, contradiction semantics, oracle rule, or input assembly requires a superseding manifest version and re-evaluation of the implementation gate. Existing approved/run records must not be overwritten.

## Current gate

`REVIEW` — input semantics and repository object identity are frozen; canonical packet SHA-256 and final repository commit receipt remain required before `ALLOW_TO_WRITE_HARNESS`.

## v1.0 connection

This manifest makes AR-001 evidence reproducible and auditable while preserving unknown/validation-required states instead of manufacturing integrity evidence.