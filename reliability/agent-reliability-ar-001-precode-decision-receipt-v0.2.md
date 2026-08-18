# AR-001 — Pre-Code Gate Decision Receipt v0.2

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Gate:** `ALLOW_TO_WRITE_HARNESS`  
**Decision:** `ALLOW`  
**Recorded:** 2026-08-17  
**Supersedes:** `agent-reliability-ar-001-precode-decision-receipt.md` v0.1 (`REVIEW`)  
**Reviewed repository baseline:** `8c828dfa910605658894d53831bebce222e15a00`

## Decision

**ALLOW — bounded harness implementation only.**

The pre-code gate is satisfied because the technical experiment parameters are frozen and the remaining owner-controlled decisions have been explicitly approved. This receipt authorizes implementation of the smallest AR-001 harness within the scope below. It does not authorize inference execution, the two-clone pilot, or the 30-run cohort.

## Bound evidence

| Evidence | Bound state |
|---|---|
| implementation-readiness specification | v0.2 / frozen |
| control evidence packet | v0.1 |
| frozen input manifest | v0.2 |
| input integrity receipt | v0.1 / PASS |
| oracle-safe input packet | `reliability/fixtures/ar-001-input-v1.json` |
| input packet SHA-256 | `861c2c314fb149def429a078a0181213534ac9490daa793b27abebf216c998cc` |
| input byte length | `2312` |
| evaluated-agent instruction | `reliability/fixtures/ar-001-instruction-v1.md` v1.0.0 |
| instruction SHA-256 | `3c1fd2716d1382fbbee4ea178c32c5ccc887b999d33afbc11df708137c9df198` |
| instruction byte length | `5877` |
| permission/configuration manifest | v0.3 |
| supplier/model review | v0.2 |
| owner decision packet | v0.2 / APPROVED |
| provider | OpenAI API Platform |
| model | `gpt-5.6-terra` |
| reasoning effort | `high` |
| request storage | `store:false` |
| evaluated-agent tools | `0` |

## Frozen execution budget

- maximum assembled input: `32,000 tokens`;
- maximum output: `8,000 tokens`;
- evaluated-agent turns: `1`;
- tool calls: `0`;
- wall-clock timeout: `180 seconds`;
- automatic semantic retries: `0`;
- automatic inference retries after request acceptance: `0`.

Timeout/infrastructure failure produces an incomplete run routed to `REVIEW`. A repeat requires a new governed run ID.

## Owner-controlled decisions satisfied

- OpenAI / `gpt-5.6-terra` / high reasoning: approved;
- bounded residual-risk treatment: accepted for harness implementation;
- synthetic-only provider data boundary: approved;
- retention/deletion policy: approved;
- incident/recovery/risk/resume owner: Operator Intelligence operator/repository owner;
- bounded harness implementation scope: approved.

## Authorized implementation scope

The harness may only:

1. verify frozen packet and instruction digests/byte lengths;
2. validate fixed configuration before request construction;
3. assemble the deterministic evaluation context;
4. construct one Responses API request for `gpt-5.6-terra`, high reasoning, `store:false`, no tools;
5. send the request only when a later execution gate explicitly authorizes execution;
6. parse and validate structured output;
7. enforce evidence provenance, contradiction, authority and certification boundaries;
8. capture observable request/model metadata;
9. canonicalize comparable fields;
10. calculate predeclared AR-001 agreement/safety metrics;
11. emit integrity-bound run receipts;
12. fail closed on digest, schema, authority, oracle, model-identity or governance violations.

## Explicitly not authorized

This receipt does not authorize:

- any OpenAI inference request for AR-001;
- two-clone pilot execution;
- 30-run cohort execution;
- production/client data;
- nonzero evaluated-agent tools;
- web/file search, MCP, shell, code interpreter or computer use;
- model or reasoning-effort substitution;
- threshold changes after observed results;
- reliability/compliance/certification claims.

## Next gate

After the harness and deterministic tests are implemented and verified, produce an `ALLOW_TO_RUN_PILOT` readiness decision. Required evidence includes:

- permission/authority denial tests;
- evidence-borne instruction override test;
- oracle/prior-run isolation verification;
- secret/context exclusion check;
- packet/instruction integrity failure tests;
- output schema/provenance validation tests;
- receipt integrity/recovery test;
- model/config request-construction verification;
- fail-closed behavior evidence.

No pilot request may be sent before that separate gate is `ALLOW`.

## Machine-readable decision

```json
{
  "experiment_id": "AR-001",
  "gate": "ALLOW_TO_WRITE_HARNESS",
  "receipt_version": "0.2",
  "decision": "ALLOW",
  "recorded_date": "2026-08-17",
  "reviewed_repository_baseline_sha": "8c828dfa910605658894d53831bebce222e15a00",
  "model": "gpt-5.6-terra",
  "reasoning_effort": "high",
  "input_packet_sha256": "861c2c314fb149def429a078a0181213534ac9490daa793b27abebf216c998cc",
  "instruction_sha256": "3c1fd2716d1382fbbee4ea178c32c5ccc887b999d33afbc11df708137c9df198",
  "harness_implementation_authorized": true,
  "pilot_execution_authorized": false,
  "cohort_execution_authorized": false,
  "next_gate": "ALLOW_TO_RUN_PILOT"
}
```

## Governance disposition

Pre-code technical and owner-control requirements: **PASS**.  
Harness implementation: **ALLOW**.  
Experiment execution: **REVIEW pending pilot-readiness evidence**.
