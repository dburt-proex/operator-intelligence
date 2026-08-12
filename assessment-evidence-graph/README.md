# Assessment Evidence Graph

Status: `MERGED CLOSEOUT — bounded GE-001 package scope`
Directive: `GE-2026-08-08-001`
Owner: Operator Intelligence domain state

This subsystem implements one bounded assessment evidence vertical slice. It is intentionally separate from the Leverage Engine and is not a universal ecosystem graph.

The replay path is:

```text
Engagement
→ Scope
→ EvidenceRequirement
→ EvidenceArtifact
→ Claim
→ Finding
→ ControlGap
→ Remediation
→ Verification
→ PublicationDecision
→ LedgerReceipt
```

The representative fixture preserves contradictory evidence. A configuration export says follow-up is enabled while an authorized synthetic safe test observes no notification within its bounded test window. Neither record is deleted or averaged away. The conflict deterministically routes publication to `REVIEW` and leaves `implementation_authorized: false`.

## Control boundary

- Pydantic v2 provides strict typed and versioned contracts.
- SQLite stores tenant- and assessment-scoped Operator Intelligence canonical state.
- `AssessmentWriteBroker` is the only supported canonical mutation path.
- Idempotency collisions, stale writes, policy-source drift, integrity failures, cross-tenant records, certification claims, and attempted implementation authorization fail closed.
- The Shared Decision Ledger boundary receives a versioned envelope containing references, versions, hashes, gates, and reason codes. It does not receive ownership of evidence, claims, findings, or remediation state.
- Runtime code has no network, subprocess, GitHub, or cross-repository execution path.

The local JSONL ledger option is an outbox/replay surface only. It is not a claim that an external Shared Decision Ledger consumer accepted the event.

## Run the slice

```bash
python -m pip install ./assessment-evidence-graph
oi-assessment-evidence-graph \
  assessment-evidence-graph/fixtures/representative-assessment/run.json \
  --database /tmp/oi-assessment-graph.sqlite3 \
  --ledger-outbox /tmp/oi-assessment-ledger.jsonl \
  --standards-root "$PWD"
```

The package bundles its publication policy. Standards remain an explicit external
input: `--standards-root` must point to the exact Operator Intelligence repository
baseline named by the policy. Missing or drifted policy sources fail closed before
canonical-state mutation.

## Verify

```bash
PYTHONPATH=assessment-evidence-graph/src \
  python -m unittest discover -s assessment-evidence-graph/tests -v

python registry/validate_registry.py
python tools/generate_repository_map.py --check
```

## GE-001 merged closeout

The bounded GE-001 package closeout merged through PR #24 at
`ed5b430e1d86d4264ed877bfa6292cc90059ae15`. Post-merge conformance workflow
run `31618320770` completed successfully, including the non-editable wheel
smoke test and the assessment-evidence-graph replay and adversarial tests.

This records only the local synthetic-fixture, SQLite, and JSONL-outbox scope
described above. It does not establish a Shared Decision Ledger consumer, live
client ingestion, remediation authority, production enforcement, or authority
for any later graph increment.
