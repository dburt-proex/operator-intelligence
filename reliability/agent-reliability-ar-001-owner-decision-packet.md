# AR-001 — Owner Decision Packet

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Packet version:** 0.1  
**Status:** READY FOR OWNER DECISION  
**Decision gate:** `ALLOW_TO_WRITE_HARNESS`

## Purpose

Consolidate the remaining human/operator-controlled decisions required after technical AR-001 configuration was frozen. Approval of this packet may authorize only the smallest executable harness. It does not authorize pilot or cohort execution.

## Evidence already closed

The following pre-code technical requirements are complete:

- oracle-safe synthetic input packet exists;
- packet SHA-256 and byte length are verified;
- source-evidence/oracle separation is explicit;
- evaluated-agent authority and tool boundary are frozen;
- evaluated-agent tool count is zero;
- PromptBP-style AR-001 instruction artifact is frozen and hashed;
- execution budget is frozen;
- model/provider technical review is complete;
- risk, threat, incident, data, supplier, recovery, logging, and review requirements are defined;
- permission/security/recovery execution tests are correctly deferred to `ALLOW_TO_RUN_PILOT`, after harness creation.

## Decision 1 — Provider/model approved use

**Recommendation: APPROVE WITH CONDITIONS**

Approve OpenAI API Platform for AR-001 synthetic-only inference using:

- endpoint: `/v1/responses`;
- model: `gpt-5.6-sol`;
- reasoning effort: `medium`;
- `store: false`;
- no model tools;
- no web/file search;
- no MCP, code interpreter, shell, computer use, or external retrieval;
- no client, production, personal, credential, secret, or regulated data.

Condition: a model-identity/fingerprint change during an active stage is fail-closed. No silent model substitution is allowed.

## Decision 2 — Residual-risk treatment

**Recommendation: ACCEPT FOR HARNESS IMPLEMENTATION ONLY**

Accept the following bounded residual risks at the pre-code gate:

| Residual risk | Level | Treatment |
|---|---|---|
| unobservable provider-side model drift behind `gpt-5.6-sol` | medium | disclose limitation; capture observable identity; HALT on observable drift; AR-006 handles model substitution |
| provider availability/rate limiting | low | no semantic retry; failed request remains incomplete; new run ID required |
| provider abuse-monitoring retention | low | synthetic-only input; `store:false`; no sensitive data |
| prompt/evidence injection | medium until tested | instruction hierarchy frozen; mandatory adversarial boundary test before pilot |
| receipt/integrity failure | low until tested | packet/instruction hashes; mandatory recovery/integrity test before pilot |

This acceptance does not waive any `HALT` condition and does not authorize pilot execution before security/permission/recovery tests pass.

## Decision 3 — Data retention/deletion

**Recommendation: APPROVE**

Apply the following experiment retention policy:

- specifications, manifests, integrity receipts, gate decisions, aggregate metrics, incident records, and supersession history: retain as durable repository/program evidence;
- raw individual model response bodies and request metadata: retain for `180 days after AR-001 cohort closeout` unless needed longer for an unresolved incident, dispute, or validation investigation;
- disposable local temporary files: delete after their hashes/required evidence are captured and verified;
- API request storage: `store:false`;
- client/production data: prohibited;
- any future sensitive-data scope requires a superseding specification and new approval.

## Decision 4 — Incident and recovery ownership

**Recommendation: APPROVE**

Assign the Operator Intelligence operator/repository owner as the accountable owner for:

- incident classification and escalation;
- experiment HALT/resume authority;
- residual-risk acceptance;
- recovery-test review;
- supplier/model approved use;
- retention exceptions;
- final pilot/cohort gate decisions.

Automated agents may detect, record, validate, and recommend; they may not close incidents, accept residual risk, or self-authorize resumption.

## Decision 5 — Harness implementation scope

**Recommendation: ALLOW WHEN THIS PACKET IS APPROVED AND BASELINE SHA IS RECORDED**

The implementation authorization is limited to the smallest harness that can:

1. verify packet/instruction hashes before inference;
2. assemble identical clean context;
3. call the frozen model/configuration;
4. expose zero evaluated-agent tools;
5. capture structured output and provider metadata;
6. validate output schema/provenance/authority rules;
7. canonicalize results for comparison;
8. calculate AR-001 predeclared metrics;
9. emit immutable run receipts;
10. fail closed on integrity, authority, oracle, model-identity, or governance violations.

It must not run the two-clone pilot until a separate `ALLOW_TO_RUN_PILOT` receipt exists.

## Rejected alternatives

- **Use the full representative `run.json` as evaluated input:** rejected because it contains downstream expected-answer/oracle material.
- **Use the broad `gpt-5.6` alias:** rejected because `gpt-5.6-sol` is the more specific documented model ID.
- **Enable tools for convenience:** rejected because AR-001 does not require them and they increase the authority surface.
- **Make ZDR a hard prerequisite:** rejected for this synthetic-only study; `store:false` and synthetic-data restriction are sufficient at this bounded stage. ZDR may be used if already available.
- **Auto-retry weak or failed model runs:** rejected because retries can obscure reliability failures and compromise independent-run accounting.

## Approval effect

An explicit owner approval of this packet authorizes creation of a superseding `ALLOW_TO_WRITE_HARNESS` receipt bound to the reviewed repository baseline SHA and then the smallest executable harness.

Approval does **not** authorize:

- pilot inference runs;
- 30-run cohort;
- production/client data;
- publication of reliability claims;
- external assurance claims;
- changing frozen thresholds after results.

## Owner decision fields

```json
{
  "experiment_id": "AR-001",
  "gate": "ALLOW_TO_WRITE_HARNESS",
  "provider_model_approved": null,
  "bounded_residual_risk_accepted": null,
  "retention_policy_approved": null,
  "incident_recovery_ownership_approved": null,
  "harness_scope_approved": null,
  "decision": "PENDING_OWNER",
  "owner": null,
  "decision_timestamp": null,
  "notes": null
}
```

No agent may replace the null owner-decision fields without explicit operator authority.
