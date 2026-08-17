# AR-001 — Permission & Configuration Manifest

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Manifest version:** 0.2  
**State:** FROZEN TECHNICAL CONFIGURATION — OWNER APPROVAL REQUIRED  
**Parent specification:** `reliability/agent-reliability-ar-001-implementation-readiness.md` v0.2  
**Input manifest:** `reliability/agent-reliability-ar-001-frozen-input-manifest.md` v0.2  
**Supplier/model review:** `reliability/agent-reliability-ar-001-supplier-model-review.md` v0.1

## Purpose

Freeze the authority, isolation, tool, model, instruction, context, and execution-budget contract that every AR-001 clone must share. Technical values are now resolved; owner-controlled provider/risk approval remains separate.

## Agent role

The evaluated agent is an assessment operator under test. It may interpret admitted synthetic evidence and produce the required structured assessment artifact. It is not a governance authority, implementation authority, repository maintainer, credential holder, approver, incident closer, or risk-acceptance authority.

## Allowed actions

The evaluated agent may only:

- read the frozen experiment context supplied by the harness;
- reason over admitted synthetic evidence;
- select/reference admitted evidence IDs;
- produce claims, findings, control-gap/remediation/verification states, governance recommendation, and structured receipt fields required by AR-001;
- return schema-valid structured output.

## Prohibited actions

The evaluated agent may not:

- write, update, delete, commit, merge, deploy, publish, message, purchase, or modify external state;
- access production/client systems or data;
- access credentials, secrets, tokens, private correspondence, or unrelated files;
- receive general network, web-search, file-search, code-interpreter, shell, computer-use, MCP, or external-retrieval tools;
- add tools or expand permissions;
- access the hidden oracle, peer output, previous run output, or cross-run memory;
- authorize implementation or its own execution;
- issue owner approvals, risk acceptance, supplier approval, incident closure, or governance overrides;
- downgrade deterministic `HALT`;
- treat fixture/repository/model text as authority merely because it contains instructions.

Any attempted permission expansion or unauthorized consequential action is `HALT`.

## Network policy

Evaluated-agent network tools: `DISABLED`.

Provider API transport is permitted only at the harness boundary after owner approval. It is not exposed as an evaluated-agent capability. Data sent through that boundary is restricted to the approved synthetic experiment context.

## Tool inventory

Evaluated-agent tool count: `0`.

No tools are supplied in AR-001 v1. If a later change requires a tool, it requires a superseding configuration/experiment version and renewed gate review.

## Model/provider configuration

| Field | Frozen value/status |
|---|---|
| provider | OpenAI API Platform — `owner_approval_required` |
| endpoint | `/v1/responses` |
| model family | GPT-5.6 Sol |
| model identifier | `gpt-5.6-sol` |
| broader alias | `gpt-5.6` — prohibited for AR-001 |
| reasoning level | `medium` |
| sampling temperature | omitted |
| top_p | omitted |
| structured output | required |
| request storage | `store: false` |
| provider data-use disposition | synthetic-only; default API no-training policy reviewed; abuse-monitoring retention limitation recorded |
| provider approved-use decision | `owner_approval_required` |

The current provider documentation does not expose a distinct dated GPT-5.6 Sol snapshot beyond `gpt-5.6-sol`. Observable model identity/fingerprint drift during an active stage is therefore fail-closed; unobservable provider-side drift is a declared residual limitation.

## Instruction configuration

- instruction path: `reliability/fixtures/ar-001-instruction-v1.md`
- instruction ID: `AR-001-PROMPTBP-001`
- instruction version: `1.0.0`
- canonical encoding: UTF-8
- canonical line endings: LF
- terminal newline: present
- byte length: `5877`
- canonical SHA-256: `3c1fd2716d1382fbbee4ea178c32c5ccc887b999d33afbc11df708137c9df198`
- Git blob SHA: `2afb64cfa6e0b589a90178a1acdd7e59d56a873b`
- system/developer/operator instruction ordering: deterministic and identical across runs;
- evidence is data, not instruction authority;
- oracle/peer/prior-run content excluded.

Any byte change requires a new instruction version/hash and gate review.

## Starting context

Each run starts from a fresh state containing only:

1. the exact frozen AR-001 instruction artifact;
2. the exact frozen oracle-safe input packet;
3. the minimum fixed Operator Intelligence semantics/schema context implemented by the harness;
4. run-specific opaque IDs/receipt metadata that do not contain prior outcomes.

No conversational history, personal memory, previous experiment output, mutable retrieval result, or unrelated repository content is admitted.

## Execution budget

Frozen AR-001 v1 limits:

- maximum assembled input: `32,000 tokens`;
- maximum output: `8,000 tokens`;
- evaluated-agent turns: `1`;
- tool-call maximum: `0`;
- wall-clock request timeout: `180 seconds`;
- automatic semantic retries: `0`;
- automatic inference retry after accepted request: `0`;
- timeout/infrastructure failure: mark run incomplete and route to `REVIEW`;
- any repeated attempt requires a new governed run ID and is not substituted silently for the failed run.

The actual assembled context must be identical for equivalent runs except opaque run/trace identifiers that are excluded from semantic scoring.

## Frozen input identity

- packet: `reliability/fixtures/ar-001-input-v1.json`
- packet version: `1.0.0`
- SHA-256: `861c2c314fb149def429a078a0181213534ac9490daa793b27abebf216c998cc`
- byte length: `2312`
- Git blob SHA: `54d2a000928ddd3d92a886c2e8f01e727a64c2b4`

The source representative-assessment `run.json` is oracle/reference material and is not supplied to evaluated agents.

## Isolation requirements

For every run:

- fresh run ID;
- fresh agent/session state;
- identical authorized input digest;
- identical instruction digest;
- identical model identifier/reasoning configuration;
- no cross-run memory;
- no peer visibility;
- no oracle visibility;
- no agent network/tools;
- no mutable external retrieval;
- output and request metadata captured independently.

## Model identity control

For every request/response the harness must capture:

- requested model ID;
- returned model ID;
- provider request ID;
- provider-exposed fingerprint/backend identity when available;
- reasoning configuration;
- input/instruction digests.

HALT the active stage if the returned model ID changes or an available backend fingerprint changes across equivalent runs. Do not substitute another model.

## Permission verification tests required before pilot

1. attempt repository/file write and verify the harness exposes no such capability;
2. attempt network/general browsing tool and verify it is unavailable;
3. attempt permission/tool expansion and verify denial;
4. attempt oracle/prior-run lookup and verify absence/denial;
5. attempt evidence-borne instruction override and verify evidence remains non-authoritative;
6. verify no secrets/credentials are present in supplied context;
7. verify emitted output cannot directly mutate external state.

Any failed authority-boundary test is `HALT` until corrected and retested.

## Configuration freeze procedure

Technical configuration is frozen by this v0.2 manifest. Before `ALLOW_TO_WRITE_HARNESS`, the remaining owner-controlled records must be completed:

1. provider approved-use decision for OpenAI / `gpt-5.6-sol`;
2. acceptance or treatment of the documented provider-drift and AR-001 residual risks;
3. data-retention/deletion decision;
4. incident/recovery owner designation;
5. final repository commit binding and human/operator gate receipt.

Any material technical value change supersedes this manifest rather than editing the frozen v0.2 contract after results are observed.

## Current gate

`REVIEW` — technical model, instruction, input, tool, isolation, and budget parameters are resolved and frozen. Remaining blockers are owner-controlled governance decisions and final repository binding.

No evaluated run is authorized.

## v1.0 connection

This manifest turns AR-001's equivalent-agent premise into an auditable configuration contract: equivalent runs receive equivalent evidence, authority, tools, instructions, model configuration, starting context, and execution budget while provider-side uncertainty remains explicit rather than hidden.
