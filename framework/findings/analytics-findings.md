# Analytics Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable analytics and reporting findings for Operator Intelligence assessments.

Analytics findings identify where contractor and local-service businesses cannot reliably observe website activity, inquiry sources, lead quality, estimate outcomes, reputation growth, or operating trends because tracking is missing, fragmented, inconsistent, inaccessible, or not used for decisions.

This library converts measurement weaknesses into governed findings that can be scored, routed, reported, and implemented without inventing performance claims from incomplete data.

## v1.0 connection

Operator Intelligence v1.0 requires a measurement layer that improves Operator Score confidence and allows recommendations to be validated after implementation.

This file strengthens v1.0 readiness by supporting:

- evidence quality and confidence adjustment
- baseline creation
- lead-source attribution
- estimate and sales reporting
- reputation reporting
- executive dashboard routing
- post-implementation verification
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- Analytics category score is weak, partial, unknown, or inconsistent.
- Website analytics or Search Console status is unknown.
- Forms, calls, bookings, or other conversion events are not verified.
- Leads cannot be counted by source, service, location, urgency, or status.
- Estimate outcomes, close rate, lost reasons, job value, or sales-cycle length are not tracked.
- Review velocity, response completion, or testimonial capture is not monitored.
- Reports exist but do not produce clear decisions or assigned actions.
- The owner cannot quickly see the operating metrics needed to manage growth.

## Outputs and deliverables

A valid use of this file should produce:

- one or more analytics findings
- evidence record for each finding
- confidence level for each finding
- measurement impact statement
- recommended implementation package
- roadmap phase
- validation requirements
- DecisionLedger entry

## Governance rules

1. Absence of accessible data is not proof of poor performance.
2. Unknown metrics must be marked `unknown` or `validation_required`, not scored as confirmed failure.
3. Do not estimate traffic, conversion rate, lead volume, close rate, job value, or revenue without evidence.
4. Distinguish tracking installation, tracking accuracy, reporting availability, and decision use as separate conditions.
5. A dashboard is not considered effective merely because it exists.
6. Metrics must have a definition, source, owner, review cadence, and decision use before being treated as governed reporting.
7. Recommendations must prioritize decision-critical measures over vanity metrics.
8. Every analytics recommendation must identify what future decision or validation the metric will support.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Evidence Gate | Finding references analytics access, screenshots, tag review, Search Console, CRM records, reports, interviews, or a documented validation gap. | Finding assumes missing data means poor results. | Mark `validation_required` or remove. |
| Metric Definition Gate | Metric has an unambiguous definition. | Different users could calculate it differently. | Define numerator, denominator, status, or event. |
| Source Gate | System of record is identified. | Metric is manually reconstructed without disclosure. | Assign source or lower confidence. |
| Accuracy Gate | Tracking behavior is tested or limitations are stated. | Installed tools are assumed accurate. | Test or mark unverified. |
| Decision Gate | Metric supports a named decision or review action. | Metric is informational only. | Remove from priority dashboard. |
| Ownership Gate | Person or role responsible for review and correction is identified. | Data has no accountable owner. | Assign owner before implementation. |
| Confidence Gate | Confidence reflects evidence quality and data completeness. | Conclusions overstate certainty. | Downgrade confidence. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct system access, tested tracking, reconciled CRM records, or consistent reports confirm the condition. |
| Medium | Screenshots, exports, or interviews indicate the condition, but accuracy or completeness is not fully tested. |
| Low | Finding depends on owner recollection, partial records, inaccessible systems, or unverified installation. |
| Unknown | No sufficient evidence exists. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-AN-001 | Website analytics installation is missing or unverified | OI-AN-001 | Analytics access, tag review, page-source check, CMS review | Website performance cannot be reliably baselined or compared over time. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Low until tested |
| OI-FIND-AN-002 | Search Console is missing, inaccessible, or unverified | OI-AN-002 | Search Console access, ownership screenshot, client interview | Organic search visibility, indexing, and query performance cannot be validated. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Low to Medium |
| OI-FIND-AN-003 | Conversion events are not defined | OI-AN-003, OI-CONV-014 | Event inventory, analytics configuration, business-goal review | The business cannot consistently distinguish meaningful buyer actions from general traffic. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AN-004 | Form submissions are not tracked or reconciled | OI-AN-003, OI-AN-004, OI-AUTO related signals | Form test, analytics events, CRM entries, inbox records | Inquiry counts may be incomplete, duplicated, or disconnected from actual lead handling. | Operator Dashboard Pack plus CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium to High when tested |
| OI-FIND-AN-005 | Phone clicks or call outcomes are not measured | OI-AN-003, OI-AN-004 | Mobile event test, call log, call-tracking review, CRM record | A major inquiry path may be invisible in channel and conversion reporting. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AN-006 | Lead source attribution is missing or unreliable | OI-AN-004, OI-AUTO-014, OI-CONV-014 | CRM fields, hidden form fields, UTM handling, intake records | The owner cannot confidently compare which channels produce qualified inquiries. | Operator Dashboard Pack plus CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AN-007 | Lead qualification fields are incomplete | OI-AN-004, OI-AN-005 | CRM/form field inventory, intake records | Reporting cannot separate leads by service, location, urgency, or fit. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-AN-008 | Lead status is not consistently tracked | OI-AN-005, OI-AUTO related signals | Pipeline review, sample records, status definitions | Lead flow and follow-up completion cannot be measured reliably. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AN-009 | Estimate sent and outcome status are not tracked | OI-AN-005, OI-AN-006 | Estimate records, CRM pipeline, spreadsheet, client interview | The business cannot calculate a dependable estimate-to-win pattern or identify stalled opportunities. | CRM and Follow-Up System plus Operator Dashboard Pack | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AN-010 | Lost reasons are missing or inconsistent | OI-AN-006 | Lost-record sample, CRM fields, interview | Pricing, timing, fit, competition, and follow-up problems cannot be separated for corrective action. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AN-011 | Close rate is unavailable or calculated inconsistently | OI-AN-006 | Defined formula, estimate counts, won/lost records | Sales performance may be discussed without a repeatable denominator or reliable baseline. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Low to Medium |
| OI-FIND-AN-012 | Average job value or revenue by service is unavailable | OI-AN-006 | Accounting export, CRM records, service categories, client confirmation | Service priorities and ROI assumptions cannot be validated with operating data. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Low until reconciled |
| OI-FIND-AN-013 | Sales-cycle length is not observed | OI-AN-006 | Inquiry, estimate, decision, and job timestamps | The business cannot identify delays between inquiry, estimate, acceptance, and completion. | Operator Dashboard Pack plus CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AN-014 | Review growth and response completion are not monitored | OI-AN-007, OI-TRUST related signals | GBP review history, review tracker, response audit | Reputation activity may decline without an owner noticing or correcting the trend. | Review Generation System plus Operator Dashboard Pack | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-AN-015 | Dashboard exists but metrics lack definitions or sources | OI-AN-008, OI-AN-009 | Dashboard review, metric dictionary, source inventory | Reporting may create false confidence because figures are not governed or reproducible. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | High when observable |
| OI-FIND-AN-016 | Reporting does not generate decisions or action owners | OI-AN-009, OI-AN-010 | Meeting notes, dashboard review, action log, client interview | Data collection may consume effort without changing priorities, ownership, or execution. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AN-017 | Monthly performance review cadence is absent | OI-AN-009, OI-AN-010 | Calendar, meeting notes, reporting SOP, client interview | Trends and operating problems may remain unnoticed until they become larger constraints. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AN-018 | Tracking changes lack validation or change history | OI-AN-001, OI-AN-003, OI-AN-010 | Tag-change records, test log, DecisionLedger, release notes | Measurement can silently break, reducing confidence in future comparisons. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Low to Medium |

## Metric definition requirements

Every recommended KPI must include:

```text
metric_name:
business_question:
definition:
source_system:
calculation:
review_cadence:
owner:
acceptable_data_gap:
action_trigger:
validation_status:
```

Minimum governed metrics for the Operator Dashboard Pack:

| Metric | Required definition |
|---|---|
| Qualified leads | Count of inquiries meeting documented service, location, and fit requirements. |
| Lead source | First-touch or governed attribution rule used consistently across records. |
| Response time | Time from captured inquiry to first documented human response. |
| Estimates sent | Count of estimates formally delivered during the period. |
| Estimate outcome | Won, lost, pending, expired, or disqualified using defined statuses. |
| Close rate | Won estimates divided by decided estimates; pending estimates excluded. |
| Lost reason | Controlled reason selected when an estimate is marked lost. |
| Review velocity | New public reviews received during the defined period. |
| Review response completion | Reviews responded to divided by reviews requiring response. |

## Cross-domain routing rules

| Analytics issue | Cross-domain dependency | Routing rule |
|---|---|---|
| Form events do not match received inquiries | Conversion and Automation | Pair with conversion and automation findings; verify the lead path before dashboard work. |
| Lead source is unavailable | Automation | Pair with CRM finding when capture fields or routing must change. |
| Search performance is unknown | SEO | Keep SEO performance conclusions low confidence until Search Console or equivalent evidence is available. |
| Review trends are unknown | Trust and GBP | Pair with trust or GBP finding when reputation process is also weak. |
| Dashboard shows metrics but no action follows | Governance | Treat as decision-use failure, not a visualization problem. |
| ROI cannot be validated | ROI framework | Mark assumptions explicitly and require baseline plus post-implementation measures. |

## Evidence requirements

Acceptable evidence includes:

- analytics access or screenshots
- Search Console access or screenshots
- tag or event test results
- form submission tests
- call logs or call-tracking records
- CRM exports or sample records
- estimate records
- accounting records
- GBP review history
- dashboards and report exports
- metric dictionaries
- meeting notes and action logs
- client interviews

If system access is unavailable, record the access gap and lower confidence. Do not substitute screenshots of installed tools for proof that tracking is accurate.

## Business impact language

| Weak wording | Use instead |
|---|---|
| The business has no idea what works. | Current reporting does not yet provide a reliable view of which channels produce qualified inquiries. |
| Analytics is broken. | Tracking installation may be present, but conversion accuracy has not been verified. |
| Leads are being lost. | Lead status and follow-up completion are not consistently measurable, creating an operational visibility gap. |
| The dashboard is useless. | The current dashboard presents information, but metric definitions and decision actions are not yet governed. |
| ROI is impossible. | ROI cannot yet be validated because baseline, outcome, or attribution data is incomplete. |

## Recommended package routing

| Condition | Recommended package | Notes |
|---|---|---|
| Analytics, Search Console, conversion events, or KPI reporting is missing or unverified. | Operator Dashboard Pack | Default Phase 3. |
| Lead fields, statuses, outcomes, or ownership are missing. | CRM and Follow-Up System | Implement system-of-record controls before advanced reporting. |
| Review tracking or response reporting is weak. | Review Generation System plus Operator Dashboard Pack | Coordinate reputation workflow and measurement. |
| Form or call tracking exposes a broken inquiry path. | Website Conversion Fix Pack plus CRM and Follow-Up System | Repair path before optimizing reporting. |
| Search performance cannot be validated. | Operator Dashboard Pack | Add Search Console and governed organic reporting. |
| AI is proposed for analysis or reporting. | Governed AI Enablement only after data and metric definitions are stable | Require review gates and source traceability. |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Only when a measurement test reveals a broken live contact or form path that must be repaired immediately. |
| Phase 2 — Growth Foundation | Use only for measurement dependencies embedded in website, SEO, trust, or GBP foundation work. |
| Phase 3 — Automation and Reporting | Default for analytics verification, CRM reporting, attribution, dashboards, metric governance, and review cadence. |
| Phase 4 — Governed AI Enablement | Use for AI-assisted analysis only after stable sources, definitions, review gates, and audit logs exist. |

## Report-use rules

An analytics finding can enter a client report only when:

1. The measurement or decision gap is clearly defined.
2. Evidence is listed or access is marked `validation_required`.
3. Confidence reflects data completeness and accuracy.
4. No unsupported performance or ROI claim is included.
5. The future decision supported by the recommendation is named.
6. Package and roadmap phase are justified.
7. DecisionLedger entry can be completed.

## DecisionLedger requirements

```text
finding_id:
observation:
evidence:
data_source:
metric_definition_status:
tracking_validation_status:
interpretation:
business_impact:
confidence:
priority:
recommended_package:
roadmap_phase:
owner_validation_needed:
decision_supported:
report_section:
status:
```

## Example ledger record

```text
finding_id: OI-FIND-AN-006
observation: Website inquiries are recorded, but source values are not consistently captured in the lead tracker.
evidence: Lead tracker field review and sample inquiry records.
data_source: Existing lead tracker
metric_definition_status: Lead-source categories require standardization
tracking_validation_status: Partial
interpretation: Lead volume can be counted, but channel performance cannot be compared reliably.
business_impact: The owner cannot confidently determine which marketing sources produce qualified inquiries.
confidence: High
priority: High
recommended_package: Operator Dashboard Pack plus CRM and Follow-Up System
roadmap_phase: Phase 3 — Automation and Reporting
owner_validation_needed: Yes
decision_supported: Channel investment and follow-up prioritization
report_section: Analytics and Reporting Findings
status: report_ready
```

## Usage instructions

1. Inventory all analytics, search, CRM, estimate, accounting, review, and reporting systems.
2. Separate installation from tested accuracy.
3. Identify the system of record for each decision-critical metric.
4. Match observed gaps to the closest finding ID.
5. Assign confidence based on access, completeness, and validation.
6. Route workflow gaps to CRM and measurement gaps to the Operator Dashboard Pack.
7. Define the decision each recommended metric must support.
8. Add the DecisionLedger record.
9. Mark missing access or incomplete evidence `validation_required`.

## Completion check

Before final report use, confirm:

- Finding is evidence-backed or explicitly marked for validation.
- Unknown data is not treated as poor performance.
- Metric definition and source are clear.
- Tracking accuracy is tested or disclosed as unverified.
- Business impact does not overstate results.
- Package and roadmap routing are justified.
- Decision supported by the metric is named.
- Ledger record is complete.
