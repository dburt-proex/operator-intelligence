# OI-FIX-007 — Completion Without Realized Value

## Scenario brief
A new estimate form and CRM handoff are implemented and pass acceptance tests. No post-launch measurement window has elapsed and lead-volume data is unavailable.

## Input records
- Implementation completion: verified.
- Acceptance criteria: passed.
- Outcome baseline: partial.
- Measurement window: not complete.
- Revenue, conversion, and lead effects: unknown.

## Expected decision
- Delivery completion: `ALLOW`.
- Realized-value state: `not_measured` or `measurement_planned`.
- No ROI, conversion-lift, revenue, or lead-volume claim may be published.
- Monitoring owner and review date are recorded.

## Validation record
Pass when completion evidence is retained separately from outcome evidence and the Realized Value Register does not infer success from delivery acceptance.
