# Leverage Engine Advisory MVP Completion Record

**Version:** 0.1.0  
**Stage:** Advisory MVP complete / review gate  
**Folder alignment:** `leverage-engine/`  
**Decision owner:** Drew Burt

## Purpose

Record the implementation scope, validation evidence, authority boundary, and next gate for the first deterministic Leverage Engine proof.

## Delivered

- Subsystem charter, authority model, system boundaries, data flow, permissions, gates, and retention rules
- Versioned source/repository registries and scoring/policy profiles
- Five canonical JSON schemas
- Standard-library Python CLI and static-fixture runner
- Normalization and prompt-injection containment
- Signal/opportunity duplicate detection with source preservation
- Weighted Leverage Index scoring and deterministic ordering
- ALLOW/REVIEW/HALT routing, G4 override, stale-state invalidation, and material-tie review
- Draft directive generation with expiry, owner, prohibited actions, completion evidence, and recovery
- Auditable graph edges with provenance, creator, creation time, and confidence
- Idempotent append-only JSONL DecisionLedger adapter
- Five governed fixtures and sixteen acceptance tests

## Validation evidence

The following command completed with zero failures under Python 3.12.13:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Result: `16 tests passed`.

The CLI determinism check completed for all five fixture families:

| Fixture | Expected selection | Expected top gate |
|---|---|---|
| `daily-run-valid` | `DIRECTIVE` | `ALLOW` |
| `unknown-heavy` | `NO_ACTION` | `REVIEW` |
| `duplicate-signals` | One canonical `DIRECTIVE` | `ALLOW` |
| `stale-repository` | `NO_ACTION` | `REVIEW` |
| `g4-halt` | `NO_ACTION` | `HALT` |

Python bytecode compilation also completed successfully. All published implementation files were compared with the validated local files before closure.

## Governance decision

**ALLOW:** Present the advisory MVP for repository review and merge consideration.

This decision does not authorize directive approval, agent dispatch, live repository inspection, network source ingestion, repository mutation, external actions, spending, policy self-modification, Phase 5 handoff, or Phase 6 automation. In this MVP, `ALLOW` means eligible for human review only.

## Acceptance result

The advisory MVP definition of done is satisfied:

- canonical schemas and profiles validate;
- five governed fixtures pass;
- one CLI completes the static end-to-end cycle;
- outputs contain ranking, selection, rationale, assumptions, evidence, gates, and ledger receipt;
- repeated execution is deterministic;
- no autonomous mutation or external-action path exists;
- ownership and recovery boundaries are documented;
- selection evidence is inspectable by a second evaluator.

## Remaining gates

1. Human review and merge decision for the feature PR.
2. Calibration against reviewed real runs before treating the formula as predictive.
3. Separate Phase 2 approval before adding any live read-only repository adapter.
4. Separate source-rights and retention review before Phase 3 external discovery.
5. Separate contracts for Mirdexx, shared DecisionLedger, VIL, and AEOS integrations.

No remaining item blocks the advisory MVP. Each is a separately governed post-MVP expansion.
