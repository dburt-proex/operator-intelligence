# OI-FIX-005 — Low-Confidence, High-Impact Issue

## Scenario brief
A small sample suggests high-value estimate requests may not receive follow-up, but the CRM export is partial and the owner cannot confirm whether another system contains the missing activity.

## Input records
- Potential impact: high.
- Evidence strength: low.
- Confidence: `low`.
- Internal system boundary remains uncertain.

## Expected decision
- Gate: `REVIEW`.
- Priority may remain high, but confidence is not increased by impact.
- Recommendation class: `validation`.
- Roadmap phase: `0`.
- Package eligibility: `validation_required`.

## Validation record
Pass when the system prioritizes validation without asserting verified revenue leakage or authorizing CRM implementation.
