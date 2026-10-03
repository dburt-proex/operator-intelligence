# AR-001 Guardian integration candidate

Staged locally in `integrations/operator-intelligence`, based on upstream
`dburt-proex/operator-intelligence` commit
`47c48d459111846f384712c8d05063491a95bea5` (inspected 2026-10-02).
No branch was pushed, PR published, workflow dispatched, credential changed,
or provider call made.

The two `Execute pilot run` steps invoke
`python3 -m reliability.guardian_ar_001`. The wrapper creates an exact action,
checks trusted evidence, persists admission through `govern_and_execute`, then
invokes the existing harness argv with `shell=False` only on ALLOW. This
prevents a check/execution split. The generic Guardian runtime still sends
external model execution to REVIEW. The explicit inference profile retains
all baseline restrictions, exact action matching, VIL, and required host
verification.

The wrapper checks the named repository, main branch, manual dispatch, first
run attempt, credential presence, frozen source/authorization hashes, two
fixed run/trace pairs, zero tools/retries, and closeout authority. Duplicate
IDs in the current ledger HALT. Secrets, subprocess stdout/stderr and provider
content are not copied into the Guardian ledger. The staged harness rejects
all redirects, ignores implicit environment proxies, and bounds provider
response reads to 1 MiB. Its new LF source hash is pinned in the wrapper.
These source changes do not reopen historical authorization. Existing harness receipts
and stderr remain separate; Guardian receipts and ledger join the 180-day
artifact upload. Network egress is a property of the pinned harness, not an
OS firewall enforced by Guardian.

## Current authority: HALT

The committed authorization is historical and consumed. The canonical
`reliability/receipts/ar-001-stage-a-v2-closeout.json` says `decision: REVIEW`,
`stage_closed: true`, and `next_inference_authorized: false`. The original
closeout also preserves the original two real executions. Existing provider
runs must not be repeated under that v1 artifact.

The staged wrapper therefore HALTs with current evidence. This implementation
does not supply a new authorization or reopen the experiment. A future ALLOW
requires a separately reviewed authority/budget contract binding new runs,
input configuration, stop conditions, and durable consumption across workflow
invocations. Current-ledger duplicate protection alone is not a durable global
spend or replay control. Changing a closeout flag alone is insufficient.

## Validation and adoption

The ALLOW path uses no-network mocks. The integration suite covers admission,
duplicate IDs, consumed authority, and nonzero subprocess outcomes; provider
tests exercise redirect rejection and bounded reads with dummy credentials.

The target deterministic workflow runs integration tests and the vendored
Guardian regression suite without inference. ALLOW tests inject trusted mock
verification and a fake subprocess; they establish execution gating, not live
authorization. Windows checkouts must preserve frozen fixture LF bytes;
autocrlf conversion fails the upstream hash checks as intended.

Publish only after owner approval, then review exact-head workflow results
and governance checks before merging. Run no live pilot until a fresh bounded
authorization is independently approved. No Linux/GitHub CI execution or
live-provider behavior is asserted from local Windows tests.

Owner directive `DAXXER-GUARDIAN-AR001-CI-INTEGRATION-001` authorizes branch/PR
publication and deterministic CI only. The pilot workflow is now manual-only;
PR creation cannot trigger it. The deterministic workflow checks out the exact
PR head, receives no provider credential, runs both baseline suites, and probes
both denied run paths with forbidden executors and network sentinels. Its
`guardian-ci-evidence/integration-validation.json` records the tested SHA,
counts, Guardian decision hashes, consumed authority, and invocation counters.
CI evidence artifacts request 90-day retention; original pilot evidence remains
on its separately configured historical retention. This neither approves nor
executes a new pilot. Integration ALLOW means validation succeeded; each
consumed-authority action must separately remain HALT.

Rollback before execution: restore the original two workflow commands and
remove the wrapper/vendor additions through a reviewed revert. Preserve all
existing and newly produced receipts and ledgers. After uncertain invocation
or outcome-audit failure, reconcile provider and harness receipts before any
retry; do not delete history to reset duplicate protection.
