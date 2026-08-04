# Retention and Supersession

**Version:** 0.1.0  
**Stage:** Advisory MVP  
**Folder alignment:** `leverage-engine/policies/`

Retain run IDs, version identifiers, evidence references, repository SHAs, normalized records, scores, gate reasons, directive drafts, concise decision rationale, overrides, errors, and ledger receipts. Do not retain hidden reasoning or unnecessary source bodies.

The file-backed ledger is append-only and idempotent by record ID. A correction appends a record that identifies the superseded record. Deletion of historical evidence or edges is prohibited. Production retention duration remains a REVIEW decision until data classes and storage ownership are approved.
