# AR-001 — Owner Decision Packet

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Packet version:** 0.2  
**Status:** OWNER APPROVED  
**Decision gate:** `ALLOW_TO_WRITE_HARNESS`  
**Decision date:** 2026-08-17

## Purpose

Record the operator's explicit approval of the remaining human-controlled decisions required for the AR-001 pre-code gate. This approval authorizes only the smallest executable harness. It does not authorize either pilot inference run or the 30-run cohort.

## Technical evidence closed before approval

- oracle-safe synthetic input packet exists and excludes downstream oracle material;
- packet SHA-256 and byte length are verified;
- source-evidence/oracle separation is explicit;
- evaluated-agent authority and tool boundary are frozen;
- evaluated-agent tool count is zero;
- PromptBP-style AR-001 instruction artifact is frozen and hashed;
- execution budget is frozen;
- supplier/model review is complete;
- risk, threat, incident, data, supplier, recovery, logging, and review requirements are defined;
- permission/security/recovery execution tests are correctly deferred to `ALLOW_TO_RUN_PILOT`, after harness creation.

## Approved decision 1 — Provider/model use

**APPROVED WITH BOUNDED CONDITIONS**

- provider: OpenAI API Platform;
- endpoint: `/v1/responses`;
- model: `gpt-5.6-terra`;
- reasoning effort: `high`;
- reasoning mode: standard;
- `store: false`;
- evaluated-agent tools: zero;
- web/file search, MCP, code interpreter, hosted shell, computer use and external retrieval: disabled;
- data class: synthetic AR-001 evidence only;
- client, production, personal, credential, secret and regulated data: prohibited.

Observable model identity/fingerprint change during an active stage is fail-closed. No silent model or effort substitution is permitted.

## Approved decision 2 — Residual-risk treatment

**ACCEPTED FOR HARNESS IMPLEMENTATION ONLY**

| Residual risk | Level | Treatment |
|---|---|---|
| unobservable provider-side drift behind `gpt-5.6-terra` | medium | disclose limitation; capture observable identity; HALT on observable drift; use AR-006 for model substitution |
| provider availability/rate limiting | low | no semantic retry; failed request remains incomplete; repeat only with a new governed run ID |
| provider retention/monitoring | low | synthetic-only input; `store:false`; no sensitive data |
| prompt/evidence injection | medium until tested | frozen instruction hierarchy; mandatory adversarial boundary test before pilot |
| receipt/integrity failure | low until tested | packet/instruction hashes; mandatory recovery/integrity test before pilot |

This acceptance does not waive any `HALT` condition and does not authorize pilot execution before required implementation tests pass.

## Approved decision 3 — Data retention/deletion

- specifications, manifests, integrity receipts, gate decisions, aggregate metrics, incident records and supersession history: retain as durable program evidence;
- raw individual model response bodies and request metadata: retain for `180 days after AR-001 cohort closeout`, unless needed longer for an unresolved incident, dispute or validation investigation;
- disposable local temporary artifacts: delete after required hashes/evidence are captured and verified;
- API request storage: `store:false`;
- client/production data: prohibited;
- future sensitive-data scope requires a superseding specification and new approval.

## Approved decision 4 — Incident and recovery ownership

The Operator Intelligence operator/repository owner is the accountable owner for:

- incident classification and escalation;
- experiment HALT/resume authority;
- bounded residual-risk acceptance;
- recovery-test review;
- supplier/model approved use;
- retention exceptions;
- final pilot/cohort gate decisions.

Automated agents may detect, record, validate and recommend. They may not close incidents, accept residual risk or self-authorize resumption.

## Approved decision 5 — Harness implementation scope

**ALLOW — BOUNDED HARNESS IMPLEMENTATION**

The implementation authorization is limited to the smallest harness that can:

1. verify packet/instruction hashes before inference;
2. assemble identical clean context;
3. call `gpt-5.6-terra` with `reasoning.effort=high` and `store=false`;
4. expose zero evaluated-agent tools;
5. capture structured output and observable provider metadata;
6. validate output schema, provenance and authority rules;
7. canonicalize results for comparison;
8. calculate AR-001 predeclared metrics;
9. emit integrity-bound run receipts;
10. fail closed on integrity, authority, oracle, model-identity or governance violations.

The harness must not run the two-clone pilot until a separate `ALLOW_TO_RUN_PILOT` receipt exists.

## Rejected alternatives

- full representative `run.json` as evaluated input: rejected because it contains downstream expected-answer/oracle material;
- `gpt-5.6` alias: rejected because the experiment requires a specific tier identifier;
- Sol/medium as baseline: superseded by explicit operator selection of Terra/high before experiment execution;
- convenience tools: rejected because AR-001 does not require them and they increase authority surface;
- silent retry of weak/failed model runs: rejected because it compromises independent-run accounting;
- automatic pilot execution after harness creation: rejected because pilot requires its own governance gate.

## Approval effect

The operator's explicit approval authorizes creation of a superseding `ALLOW_TO_WRITE_HARNESS` receipt bound to the reviewed repository baseline and then implementation of the bounded harness.

Approval does **not** authorize:

- pilot inference runs;
- 30-run cohort;
- production/client data;
- reliability publication claims;
- external assurance/certification claims;
- changes to frozen thresholds after results.

## Owner decision receipt

```json
{
  "experiment_id": "AR-001",
  "gate": "ALLOW_TO_WRITE_HARNESS",
  "provider_model_approved": true,
  "provider": "OpenAI API Platform",
  "model": "gpt-5.6-terra",
  "reasoning_effort": "high",
  "bounded_residual_risk_accepted": true,
  "retention_policy_approved": true,
  "incident_recovery_ownership_approved": true,
  "harness_scope_approved": true,
  "decision": "APPROVED",
  "owner": "Operator Intelligence operator/repository owner",
  "decision_date": "2026-08-17",
  "pilot_execution_authorized": false,
  "cohort_execution_authorized": false,
  "notes": "Explicit operator approval received after selecting Terra/high as the frozen AR-001 baseline."
}
```

## Governance boundary

This packet records real operator authority supplied in the project interaction. It does not transfer that authority to the evaluated agent or future repository automation. Later execution gates remain human/operator-controlled.
