# Assessment Evidence Graph

Status: `REVIEW`
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
python -m pip install -e ./assessment-evidence-graph
oi-assessment-evidence-graph \
  assessment-evidence-graph/fixtures/representative-assessment/run.json \
  --database /tmp/oi-assessment-graph.sqlite3 \
  --ledger-outbox /tmp/oi-assessment-ledger.jsonl
```

## Verify

```bash
PYTHONPATH=assessment-evidence-graph/src \
  python -m unittest discover -s assessment-evidence-graph/tests -v

python registry/validate_registry.py
python tools/generate_repository_map.py --check
```

The release gate remains `REVIEW` even when deterministic tests pass. GE-002 must not begin until the representative fixture and receipt replay pass and the reviewable branch state is verified.
