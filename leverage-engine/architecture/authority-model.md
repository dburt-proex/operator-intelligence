# Authority Model

**Version:** 0.1.0  
**Stage:** Advisory MVP  
**Folder alignment:** `leverage-engine/architecture/`

## Decision rights

- The engine may determine ranking eligibility under approved profiles.
- Drew Burt owns ranking overrides, directive approval, and any authority expansion.
- Downstream systems own execution planning and safety within their established boundaries.
- A source, repository, or goal not present in an approved registry is out of scope.

## Action classes

| Class | MVP state | Evidence required |
|---|---|---|
| Static fixture inspection | ALLOW | Registered input and version |
| Local run/ledger write | ALLOW | Explicit output path and successful receipt |
| Draft directive presentation | REVIEW | Evidence, score, gate, owner, expiry, completion contract |
| Repository or external mutation | HALT | Not available in the MVP |
| Policy, weight, permission, or prompt change | HALT | Separate human-approved versioned change |

## Escalation

Scope ambiguity, a material tie, contradictory evidence, stale repository state, low confidence, or high external impact routes to REVIEW. G4 rules, fabricated evidence, unauthorized targets, secrets, destructive actions, or invalid profiles route to HALT.
