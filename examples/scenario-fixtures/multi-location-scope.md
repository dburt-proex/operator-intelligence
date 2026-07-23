# OI-FIX-008 — Multi-Location Scope

## Scenario brief
A contractor operates three locations. One website serves all locations, each GBP is managed differently, and only one location supplies call and CRM records. The buyer requests a single company-wide conclusion.

## Input records
- Shared website evidence applies across the defined shared surface.
- GBP evidence is location-specific.
- Internal conversion evidence exists for one location only.
- Ownership and date ranges differ by source.

## Expected decision
- Gate: `REVIEW` until applicability is separated.
- Shared evidence may have one primary owner and referenced effects.
- Location-specific evidence cannot be generalized without support.
- Unknown locations remain unknown.
- Report may publish location-level findings and a bounded shared-surface conclusion.

## Validation record
Pass when duplicate scoring is prevented, evidence scope is explicit, and one location's internal performance is not represented as company-wide fact.
