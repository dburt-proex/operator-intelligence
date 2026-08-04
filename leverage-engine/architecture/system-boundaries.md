# System Boundaries

**Version:** 0.1.0  
**Stage:** Phase 0 contract  
**Folder alignment:** `leverage-engine/architecture/`

## Purpose

Prevent ownership collision while allowing an auditable handoff from assessment to prioritization and, after separate approval, execution planning.

| System | Owns | Leverage Engine interface | Prohibited transfer of authority |
|---|---|---|---|
| Operator Intelligence | Assessment evidence, findings, Operator Score, recommendations | Read approved evidence and asset context | Leverage Index cannot modify Operator Score or assessment records |
| VIL | Signal relevance, evidence strength, confidence features | Consume a versioned feature contract | Leverage Engine cannot redefine VIL semantics silently |
| Leverage Engine | Candidate generation, ranking, selection, directive draft, queue state | Produces one reviewable directive or `NO_ACTION` | Cannot execute, authorize, or claim realized value |
| AEOS | Execution planning, decomposition, scheduling, routing | Accept only approved, unexpired Phase 5 handoffs | Cannot choose strategic priority on behalf of this subsystem |
| PromptBP | Instruction contracts | Constrain approved handoff instructions | Cannot supply opportunity evidence |
| DiffWall | Change-time repository risk | Return a change-gate receipt | No repository mutation exists in the MVP |
| CASA | Runtime permission and action governance | Return runtime and partial-execution receipts | Cannot replace strategic selection |
| Mirdexx | Durable evidence, memory, outcomes, lessons | Future external storage adapter | Cannot approve action or overwrite history |
| DecisionLedger | Decisions, overrides, approvals, outcomes | Append an immutable run decision | Cannot discover or rank opportunities |

## Data flow and gates

1. Authorized registries define sources, repositories, objective scope, and versions.
2. Static inputs are normalized as untrusted data and validated.
3. Duplicate evidence is related without deletion.
4. Scoring uses the locked profile and explicit anchor values.
5. Policy routing overrides score where authority, evidence, freshness, or G4 rules require it.
6. The top eligible candidate becomes a draft directive.
7. The decision and rejected alternatives receive a ledger receipt.
8. Human approval and downstream execution remain outside the MVP.

## Failure and recovery

Malformed inputs HALT the run. Missing or stale evidence routes to REVIEW or `NO_ACTION`. A profile checksum or version mismatch HALTs scoring. Ledger failure prevents dispatch eligibility. Corrections create a superseding record; they do not mutate the prior decision.

## Acceptance criteria

- Each system has one explicit responsibility.
- Every run identifies the profile and input versions used.
- No code path grants execution authority.
- A second evaluator can trace selection from evidence through score, gate, directive, and ledger receipt.
