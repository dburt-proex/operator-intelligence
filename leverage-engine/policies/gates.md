# Governance Gates

**Version:** 0.1.0  
**Stage:** Advisory MVP  
**Folder alignment:** `leverage-engine/policies/`

`ALLOW` means eligible for presentation. `REVIEW` means evidence, judgment, or authorization is required. `HALT` means the candidate cannot advance.

Gate precedence is `HALT` then `REVIEW` then `ALLOW`. G4 always overrides score. Unknown confidence, stale snapshots, unvalidated evidence, material contradictions, and missing completion evidence cannot advance to directive selection. Every result records stable rule IDs.

The executable policy is `config/policy-profile.yaml`; this document explains it and does not replace the versioned machine-readable profile.
