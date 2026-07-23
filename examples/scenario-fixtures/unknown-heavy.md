# OI-FIX-001 — Unknown-Heavy Engagement

## Scenario brief
A contractor assessment has complete public website evidence but no analytics, CRM, call tracking, or internal follow-up records. The buyer requests an official Operator Score and implementation roadmap.

## Input records
- Website and GBP criteria: directly observed.
- Analytics, automation, conversion attribution, and CRM criteria: `unknown`.
- Weighted evidence coverage: below the official publication threshold.
- No G4 condition.

## Expected decision
- Gate: `REVIEW`.
- Publication: `range_only` or `provisional`, never `official`.
- Unknown criteria carry no score.
- Roadmap routes missing internal evidence to Phase 0 validation.
- No implementation package is justified solely by missing access.

## Validation record
Pass when the observed score remains separate from coverage, the uncertainty range expands, unknown is not converted to zero, and the report states that internal performance could not be verified.
