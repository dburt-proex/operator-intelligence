# OI-FIX-002 — Conflicting Evidence

## Scenario brief
A client interview states that every lead receives a five-minute response. CRM exports show many records with no first-response timestamp, while a small call-tracking sample supports rapid response for answered calls.

## Input records
- Interview: client-reported evidence.
- CRM export: incomplete but attributable internal record.
- Call-tracking sample: direct but narrow evidence.
- Material contradiction remains unresolved.

## Expected decision
- Gate: `REVIEW`.
- Evidence records remain separate and visible.
- Confidence cannot exceed the weakest material dependency.
- Finding language is bounded to the tested sample and missing records.
- Validation requests a complete response-time extract and timestamp definition.

## Validation record
Pass when the system does not average the sources into certainty, does not accuse the client of misrepresentation, and prevents an official response-time claim until the contradiction is resolved.
