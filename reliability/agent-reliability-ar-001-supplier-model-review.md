# AR-001 — Supplier & Model Review

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Review version:** 0.2  
**Status:** OWNER APPROVED — FROZEN FOR HARNESS IMPLEMENTATION  
**Provider:** OpenAI API Platform  
**Model:** `gpt-5.6-terra`  
**Reasoning effort:** `high`  
**Endpoint:** `/v1/responses`

## Purpose

Freeze the approved supplier/model selection for AR-001 and provide evidence for `SUP-001` and `AI-001`. This review supersedes v0.1, which proposed `gpt-5.6-sol` at medium reasoning before the operator selected and approved the Terra/high configuration.

## Approved technical selection

| Field | Frozen value |
|---|---|
| provider | OpenAI API Platform |
| API | Responses API |
| model ID | `gpt-5.6-terra` |
| reasoning effort | `high` |
| reasoning mode | standard |
| tools | none |
| web search | disabled |
| file search | disabled |
| code interpreter | disabled |
| MCP | disabled |
| external retrieval | disabled |
| request storage | `store: false` |
| input class | synthetic experiment evidence only |
| client/production data | prohibited |

OpenAI's current GPT-5.6 model documentation identifies `gpt-5.6-terra` as the Terra model ID, describes Terra as the balance-of-intelligence-and-cost tier, supports the Responses API and structured outputs, and supports reasoning effort values including `high`.

## Selection rationale

AR-001 measures governed reproducibility rather than maximum frontier capability. Terra/high is selected as the commercially representative baseline because it preserves substantial reasoning capacity while reducing inference cost relative to Sol. The experimental question is whether equivalent governed inputs produce materially equivalent governed outcomes under a fixed configuration.

The selection is not a claim that Terra/high is universally more capable than Sol/medium. It is a workload-specific experimental design choice. Cross-model and cross-effort comparisons remain out of scope for AR-001 and belong in AR-006 or a separately frozen perturbation study.

## Model identity and drift limitation

The reviewed model catalog exposes `gpt-5.6-terra` as the model identifier. AR-001 does not claim stronger provider-side pinning than the identifier and metadata actually returned by the API.

Compensating controls:

1. use exactly `gpt-5.6-terra`;
2. set `reasoning.effort` to exactly `high`;
3. record returned model identifier and provider request ID for every run;
4. record any provider-exposed fingerprint/version metadata when available;
5. do not change model ID or reasoning effort inside a pilot or cohort;
6. HALT the active stage on observable model-identity/fingerprint drift;
7. disclose unobservable provider-side drift as a residual limitation;
8. do not represent AR-001 as proof of cross-version or cross-model reproducibility.

## Data-use boundary

The admitted packet is synthetic and may not contain client, production, credential, secret, regulated, or personal data.

AR-001 requires `store: false`. Zero Data Retention is not asserted or required for this synthetic-only experiment. If a stronger account-level retention control is already active, it may be used without broadening scope.

## Supplier risk register

| Risk | Treatment | Residual |
|---|---|---|
| provider behavior changes behind model ID | identity/fingerprint capture; stage HALT on observable drift; report limitation | medium |
| provider outage/rate limit | mark run incomplete; no semantic retry; repeat only with governed new run ID | low |
| provider retention/monitoring | synthetic-only packet; `store:false`; prohibit secrets/client data | low |
| provider tool/network expansion | expose zero tools to evaluated agent | low |
| pricing/availability change | freeze model ID; HALT rather than silently substitute | low |
| unobservable provider-side change | disclose limitation; evaluate substitution separately | medium |

## Frozen execution budget

The AR-001 harness must enforce identical ceilings across equivalent runs:

- maximum assembled input: `32,000` tokens;
- maximum output: `8,000` tokens;
- evaluated-agent turns: `1`;
- tool calls: `0`;
- wall-clock request timeout: `180 seconds`;
- automatic semantic retries: `0`;
- automatic provider/inference retries after request acceptance: `0`;
- incomplete/timeout disposition: `REVIEW`; any repeat receives a new governed run ID;
- sampling controls: omit temperature/top-p unless the API requires a supported fixed value; any required value must be frozen before pilot authorization.

The assembled experiment context must be identical across equivalent runs. These maxima are safety ceilings, not permission to vary context.

## Provider dependency boundary

OpenAI receives only the frozen synthetic input packet and frozen instruction/context required for the assessment. API transport is a harness dependency, not an evaluated-agent tool.

No MCP, search, file service, code interpreter, hosted shell, computer use, or external data connector is permitted in AR-001 v1.

## Disable/replacement path

If `gpt-5.6-terra` becomes unavailable or materially changes before a governed stage completes:

- HALT the active stage;
- preserve completed run receipts;
- do not silently substitute another model or reasoning effort;
- supersede the configuration/experiment version or route substitution to AR-006;
- restart the affected cohort if equivalence can no longer be established.

## Evidence sources reviewed

Reviewed 2026-08-17 against current official OpenAI model documentation and model guidance. The documentation identifies Terra as `gpt-5.6-terra`, supports the Responses API and structured outputs, and lists `high` among supported GPT-5.6 reasoning-effort settings.

## Owner approval record

On 2026-08-17, the operator explicitly approved proceeding after selecting the revised `gpt-5.6-terra` / `high` configuration in place of the earlier Sol/medium proposal.

Approval scope:

- OpenAI API Platform as provider;
- `gpt-5.6-terra` at `high` reasoning;
- synthetic-only data transfer;
- `store:false`;
- zero evaluated-agent tools;
- documented bounded provider/model residual risks;
- harness implementation only, subject to the separate governed pre-code receipt.

This approval does not authorize the 2-run pilot or 30-run cohort.

## Decision

**ALLOW FOR HARNESS CONFIGURATION.**

The supplier/model technical and owner-approval fields required for the pre-code gate are now satisfied for the bounded AR-001 configuration. Pilot execution remains separately gated.
