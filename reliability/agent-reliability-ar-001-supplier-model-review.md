# AR-001 — Supplier & Model Review

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Review version:** 0.1  
**Status:** TECHNICAL REVIEW COMPLETE — OWNER APPROVAL REQUIRED  
**Provider candidate:** OpenAI API Platform  
**Model candidate:** `gpt-5.6-sol`  
**Endpoint:** `/v1/responses`

## Purpose

Resolve the technical supplier/model selection for AR-001 while preserving the owner-controlled approved-use gate. This review is evidence for `SUP-001` and `AI-001`; it is not itself the human/operator approval.

## Technical selection

Recommended frozen configuration:

| Field | Selected value |
|---|---|
| provider | OpenAI API Platform |
| API | Responses API |
| model ID | `gpt-5.6-sol` |
| alias intentionally avoided | `gpt-5.6` |
| reasoning effort | `medium` |
| tools | none |
| web search | disabled |
| file search | disabled |
| code interpreter | disabled |
| MCP | disabled |
| external retrieval | disabled |
| request storage | `store: false` |
| input class | synthetic experiment evidence only |
| client/production data | prohibited |

OpenAI's current model documentation identifies `gpt-5.6-sol` as the GPT-5.6 Sol model ID, states that the `gpt-5.6` alias routes to Sol, supports structured outputs and the Responses API, and supports configurable reasoning including `medium`.

## Why this model

AR-001 is intended to establish a commercially relevant baseline for current agent operation, not benchmark a legacy model. GPT-5.6 Sol is the current flagship tier for complex professional work, while `medium` reasoning is the provider default and gives a bounded baseline before later model/effort perturbation work.

AR-006 remains the correct place to compare alternate model families or providers.

## Snapshot limitation and compensating control

The current GPT-5.6 Sol model page exposes `gpt-5.6-sol` as the model identifier but does not expose a distinct dated snapshot identifier in the reviewed documentation. Therefore AR-001 cannot claim that provider-side model internals are pinned more narrowly than the documented model ID.

Compensating controls:

1. use `gpt-5.6-sol`, never the broader `gpt-5.6` alias;
2. record the returned model identifier and provider request ID for every run;
3. record any provider-exposed backend/system fingerprint when available;
4. execute pilot/cohort only after a single configuration freeze and without changing model ID;
5. HALT the active stage if returned model identity/fingerprint changes across equivalent runs;
6. treat provider-side unobservable drift as residual risk in the final reliability report;
7. do not represent AR-001 as proof of cross-version reproducibility.

## Data-use review

The admitted packet is synthetic and contains no permitted client, production, credential, secret, or personal data.

Current OpenAI API documentation states that API inputs/outputs are not used to train OpenAI models by default unless the customer explicitly opts in. It also states that abuse-monitoring logs may be retained for up to 30 days by default. The Responses API supports `store: false`; AR-001 requires it.

Zero Data Retention is not assumed. If the operator's project is ZDR-enabled, the harness may use that existing control without changing the experiment. AR-001 does not require ZDR because the admitted packet is intentionally synthetic, but it must not silently expand to sensitive data.

## Supplier risk register

| Risk | Treatment | Residual |
|---|---|---|
| provider model behavior changes behind model ID | identity/fingerprint capture; stage HALT on observable drift; report limitation | medium |
| provider outage/rate limit | mark run incomplete; no semantic retry; rerun only under governed new run ID | low |
| provider retention | synthetic-only packet; `store:false`; no secrets/client data | low |
| provider tool/network expansion | no tools supplied to evaluated agent | low |
| pricing/availability change | freeze model ID before cohort; HALT if unavailable rather than substitute | low |
| unobservable provider-side change | disclose as residual limitation; AR-006/model-change testing later | medium |

## Execution budget recommendation

Freeze the following for the initial AR-001 configuration:

- maximum assembled input: `32,000` tokens;
- maximum output: `8,000` tokens;
- evaluated-agent turns: `1`;
- tool calls: `0`;
- wall-clock request timeout: `180 seconds`;
- automatic semantic retries: `0`;
- automatic provider/inference retries after request acceptance: `0`;
- incomplete/timeout run disposition: `REVIEW` and new governed run ID if repeated;
- temperature/top-p: omit unless the selected model/API explicitly requires or supports a frozen value; do not introduce unsupported sampling controls.

The actual assembled input must be byte-identical across equivalent runs; the maximum is a safety ceiling, not permission to vary context.

## Provider dependency boundary

OpenAI receives only the frozen instruction/context necessary to perform the synthetic assessment. The evaluated agent receives no general network capability. API transport belongs to the harness/provider boundary and is not an agent tool.

No third-party MCP, search, file service, code interpreter, hosted shell, or external data connector is permitted in AR-001 v1.

## Disable/replacement path

If `gpt-5.6-sol` becomes unavailable or materially changes before the cohort is complete:

- HALT the active AR-001 stage;
- preserve completed run receipts;
- do not silently substitute another model;
- supersede the configuration/experiment version or route model substitution to AR-006;
- restart the affected reliability cohort if equivalence can no longer be established.

## Evidence sources reviewed

Reviewed on 2026-08-17:

- OpenAI GPT-5.6 Sol model documentation;
- OpenAI GPT-5.6 model guidance/model catalog;
- OpenAI API data-controls documentation;
- OpenAI enterprise-privacy documentation.

## Recommendation

**RECOMMEND ALLOW — SYNTHETIC AR-001 ONLY**, subject to explicit owner/operator approval of:

- OpenAI as the provider;
- `gpt-5.6-sol` with `medium` reasoning;
- the documented provider-drift residual risk;
- the bounded synthetic-data transfer described above.

No provider approval is inferred or self-issued by this review.

## Next gate

After owner approval, bind this review, the instruction digest, input digest, execution budget, retention rule, risk treatment, and repository commit into the superseding `ALLOW_TO_WRITE_HARNESS` decision receipt.
