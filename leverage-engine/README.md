# Leverage Engine

**Version:** 0.1.0  
**Stage:** Advisory MVP  
**Folder alignment:** Isolated Operator Intelligence subsystem

## Purpose

The Leverage Engine selects the single highest-leverage, evidence-backed action available across an approved project ecosystem. It converts authorized signals, repository snapshots, objectives, and constraints into a deterministic ranking, one draft directive candidate or `NO_ACTION`, a governance result, and an auditable ledger receipt.

## Authority boundary

The MVP is advisory only. It may read static approved inputs and write local run outputs and append-only ledger records. It cannot modify repositories, publish content, message people, submit applications, spend money, dispatch agents, collect secrets, or change its own weights, policies, permissions, or prompts.

`ALLOW` means eligible to present for human review. It never authorizes execution. Drew Burt remains the approval owner. AEOS, PromptBP, DiffWall, CASA, Mirdexx, VIL, DecisionLedger, Operator Score, and the Leverage Engine retain the separate ownership described in `architecture/system-boundaries.md`.

## Inputs and outputs

Inputs are a versioned run fixture, the source and repository registries, the scoring profile, and the policy profile. A valid run produces:

- normalized signals with provenance;
- duplicate groups without deleting source records;
- scored and deterministically ranked opportunities;
- one draft directive or `NO_ACTION`;
- ALLOW, REVIEW, or HALT reasons;
- an idempotent DecisionLedger receipt.

## Run the proof

From this folder:

```bash
PYTHONPATH=src python -m leverage_engine.cli --fixture fixtures/daily-run-valid --ledger /tmp/leverage-ledger.jsonl
PYTHONPATH=src python -m unittest discover -s tests -v
```

The runtime uses only the Python standard library and performs no network access.

## Governance rules

- Unknown is uncertainty, never zero performance.
- G4 boundaries override every score.
- Low or unknown confidence cannot produce an executable directive.
- Stale repository evidence invalidates selection.
- Urgency requires a verified deadline.
- Ranking overrides require a separate attributable record.
- Historical evidence is superseded, never silently rewritten.
- No realized-value claim is valid without completion and outcome evidence.

## Commercial v1.0 connection

Operator Intelligence assesses what should be addressed. The Leverage Engine ranks what should be addressed next across approved assets. It does not alter Operator Score, client assessment findings, package eligibility, or commercial assessment semantics.

## Completion evidence

Advisory MVP completion requires five passing fixtures, deterministic replay, valid canonical schemas and profiles, a complete directive or `NO_ACTION` result, a ledger receipt, explicit recovery behavior, and the absence of mutation or external-action capabilities.
