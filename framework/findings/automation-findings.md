# Automation Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable automation and operations findings for Operator Intelligence assessments.

Automation findings identify where contractor and local-service businesses rely on manual memory, scattered inboxes, informal handoffs, or disconnected tools for lead capture, response, estimate follow-up, review generation, customer reactivation, and reporting.

This library converts observable workflow weaknesses into governed findings that can be scored, routed, reported, and implemented without recommending automation for its own sake.

## v1.0 connection

Operator Intelligence v1.0 requires operational findings that connect visible growth-system weaknesses to controlled implementation paths.

This file strengthens v1.0 readiness by giving evaluators a controlled automation finding set that supports:

- lead-system diagnosis
- CRM readiness assessment
- response and follow-up consistency
- estimate workflow evaluation
- review-system evaluation
- operational reporting readiness
- implementation package routing
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- Automation category score is weak, partial, unknown, or inconsistent.
- Inquiries arrive through multiple channels without one tracked destination.
- Website, Google, social, email, or phone inquiries can be missed.
- Confirmation, internal notification, owner assignment, or response standards are absent or unverified.
- Lead, estimate, won/lost, follow-up, or re-engagement status is not tracked.
- Review requests rely on memory or inconsistent manual effort.
- Customer history, seasonal outreach, or referral opportunities are not systematized.
- The owner lacks a usable view of pipeline, source, estimate, review, or follow-up performance.

## Outputs and deliverables

A valid use of this file should produce:

- one or more automation findings
- evidence record for each finding
- confidence level for each finding
- business impact statement
- recommended implementation package
- roadmap phase
- DecisionLedger entry
- report-safe language for client-facing output

## Governance rules

1. Do not recommend automation before the underlying workflow is understood.
2. Do not treat manual work as failure when volume, risk, or complexity does not justify automation.
3. A tool is not a system. Findings must evaluate routing, ownership, state, controls, and reporting.
4. Unknown internal workflow data must be marked `unknown` or `validation_required`, not scored as failure by default.
5. Do not claim missed revenue, lost leads, or response failure without CRM, message, call, analytics, or client evidence.
6. A recommendation is valid only when observation, evidence, interpretation, impact, confidence, priority, package, and roadmap phase are present.
7. High-risk customer-facing automation must include human review, escalation, auditability, and data-handling controls.
8. Broken capture or notification paths outrank convenience automation.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Evidence Gate | Finding has CRM, form, inbox, notification, workflow, dashboard, template, interview, or documented validation evidence. | Finding is based on assumed internal operations. | Mark `validation_required` or remove. |
| Workflow Definition Gate | Current process, trigger, owner, state, and outcome are understood. | Automation is proposed for an undefined workflow. | Document the workflow first. |
| Business Need Gate | Finding affects reliability, response, ownership, follow-up, measurement, or capacity. | Automation is only a novelty or convenience. | Do not recommend. |
| Control Gate | Failure handling, ownership, review, and escalation are considered. | Proposed automation can fail silently or act without accountability. | Add controls or block routing. |
| Confidence Gate | Confidence is assigned using evidence quality. | Certainty is overstated. | Downgrade confidence or request validation. |
| Impact Gate | Impact is tied to lead handling, response consistency, estimate progression, retention, or visibility. | Impact is vague. | Rewrite impact. |
| Package Gate | Package matches the actual workflow weakness. | Package is selected because it is sellable. | Block recommendation. |
| Roadmap Gate | Phase reflects prerequisites and implementation sequence. | Tool implementation precedes process clarity. | Re-sequence. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct evidence confirms the workflow state, such as CRM access, form routing test, notification test, dashboard review, template review, or documented SOP. |
| Medium | Multiple observations or client statements indicate a pattern, but system access or broader sampling would improve certainty. |
| Low | Finding depends mainly on client interview, partial screenshots, or incomplete internal records. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-AUTO-001 | Inquiries do not enter one tracked system | OI-AUTO-001, OI-CONV-014, OI-AN-005 | CRM or spreadsheet review, channel inventory, client interview, form destination review | Leads may be harder to assign, follow, report, and recover consistently. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-AUTO-002 | Website form notifications are missing or unreliable | OI-AUTO-002, OI-CONV-006 | Safe form test, form settings, inbox review, client confirmation | Submitted inquiries may not receive timely internal attention. | CRM and Follow-Up System | Phase 1 if broken; Phase 3 for systemization | High when tested |
| OI-FIND-AUTO-003 | Inquiry confirmation is missing or unclear | OI-AUTO-003, OI-CONV-006, OI-CONV-010 | Form test, confirmation screen, email/SMS review | Buyers may not know whether the inquiry was received or what happens next. | Website Conversion Fix Pack or CRM and Follow-Up System | Phase 1 for visible confirmation; Phase 3 for automated messaging | High when tested |
| OI-FIND-AUTO-004 | Lead ownership is undefined | OI-AUTO-004, OI-AUTO-012 | CRM fields, workflow review, SOP, client interview | Follow-up may be delayed or duplicated when no person is accountable for the lead. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AUTO-005 | Lead status is not tracked consistently | OI-AUTO-005, OI-AN-006 | CRM stage review, spreadsheet review, sample records | The business may lack a reliable view of which leads are new, contacted, estimated, won, lost, or stale. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | High when records are available |
| OI-FIND-AUTO-006 | Follow-up depends on memory | OI-AUTO-006, OI-OFFER-005 | CRM task review, reminder review, templates, client interview | Open inquiries or estimates may receive inconsistent follow-up. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-AUTO-007 | Estimate outcomes and lost reasons are not tracked | OI-AUTO-007, OI-AN-006, OI-OFFER-006 | CRM report, estimate log, lost-reason fields, client interview | The owner may not know where estimates stall or why prospects decline. | CRM and Follow-Up System plus Operator Dashboard Pack | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-AUTO-008 | Review requests are inconsistent or manual-only | OI-AUTO-008, OI-AN-007, OI-GBP-008 | Review workflow, message template, CRM automation, client interview | Review growth may depend on staff memory rather than a repeatable post-job process. | Review Generation System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-AUTO-009 | Negative feedback has no controlled routing path | OI-AUTO-008, OI-TRUST related signals | Review workflow, escalation SOP, client interview | Sensitive feedback may not reach the right owner before becoming a public reputation issue. | Review Generation System | Phase 3 — Automation and Reporting | Low to Medium |
| OI-FIND-AUTO-010 | Missed calls or messages lack a recovery workflow | OI-AUTO-009, OI-CONV-012 | Phone process review, call logs, voicemail/SMS workflow, social inbox review | High-intent inquiries may not receive a prompt second path after the first contact attempt is missed. | CRM and Follow-Up System | Phase 1 if path is broken; Phase 3 for full workflow | Medium |
| OI-FIND-AUTO-011 | Customer records do not preserve useful service history | OI-AUTO-010, OI-OFFER-008 | CRM fields, customer database, sample records | The business may be unable to segment past customers for maintenance, seasonal, referral, or repeat-service opportunities. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AUTO-012 | Repeat, seasonal, or reactivation outreach is absent | OI-AUTO-011, OI-OFFER-008 | CRM lists, campaign history, client interview | Past-customer demand may remain underused because no structured reactivation path exists. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Low to Medium |
| OI-FIND-AUTO-013 | Internal handoffs are informal or undocumented | OI-AUTO-012, OI-AI-001 | SOP review, workflow map, client interview | Work may depend on tribal knowledge, creating inconsistency as volume or staffing changes. | CRM and Follow-Up System or workflow documentation package | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AUTO-014 | Standard response templates are missing | OI-AUTO-013, OI-OFFER-005 | Email/SMS template review, CRM snippets, client interview | Customer communication may vary in speed, clarity, and completeness across staff or channels. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-AUTO-015 | Source attribution is absent or unreliable | OI-AUTO-001, OI-AN-005, OI-CONV-014 | CRM source fields, UTM capture, form fields, call tracking, sample records | The owner may not know which channels produce qualified inquiries. | Operator Dashboard Pack plus CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-AUTO-016 | Operational dashboard is missing or passive | OI-AUTO-014, OI-AN-001 through OI-AN-010 | Dashboard review, report review, meeting cadence, decision log | The owner may lack a usable view of pipeline health, response, estimates, reviews, and follow-up actions. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | High when observable |
| OI-FIND-AUTO-017 | Automation failures are not monitored | OI-AUTO-002, OI-AUTO-003, OI-AUTO-006, OI-AUTO-008 | Error logs, failed-run alerts, workflow settings, owner review process | Silent failures may interrupt lead, follow-up, review, or reporting workflows without detection. | CRM and Follow-Up System with monitoring controls | Phase 3 — Automation and Reporting | Low to Medium |
| OI-FIND-AUTO-018 | Customer-facing automation lacks escalation or review controls | OI-AUTO related signals, OI-AI-004, OI-AI-005, OI-AI-007, OI-AI-010 | Workflow design, assistant configuration, logs, escalation rules | Automated communication may create risk if uncertain, sensitive, pricing, complaint, or exception cases are not routed to a person. | Governed AI Intake Assistant | Phase 4 — Governed AI Enablement | Medium to High when system exists |

## Criteria mapping rules

Use automation findings as the primary finding type when the weakness concerns system reliability, routing, ownership, state tracking, follow-up, handoffs, repeatability, or operational visibility.

Use cross-domain routing when evidence shows dependency on another domain:

| Automation issue | Cross-domain dependency | Routing rule |
|---|---|---|
| Form submits but visible confirmation is weak | Conversion | Pair with conversion finding for buyer-facing friction. |
| Review requests are not systematized | Trust or GBP | Pair with trust/GBP finding when reputation impact is central. |
| Lead source or estimate performance is unknown | Analytics | Pair with analytics finding when measurement is the main constraint. |
| Estimate follow-up is inconsistent | Offer | Pair with offer finding when sales-process weakness drives the issue. |
| Workflow is undocumented | AI readiness | Pair with AI-readiness finding before proposing AI. |
| Customer-facing automation lacks controls | AI readiness | Route to governed AI findings and Phase 4. |
| Competitors respond or follow up more effectively | Competitive | Pair only when competitor evidence is direct and material. |

## Evidence requirements

Acceptable evidence includes:

- screenshot
- URL inventory
- page copy review
- CTA review
- form test
- mobile test
- GBP screenshot
- review comparison
- competitor comparison
- analytics
- Search Console
- CRM record
- client interview
- social review
- citation audit
- workflow configuration
- automation run history
- notification test
- SOP or process map
- message template
- dashboard or report

Minimum evidence by finding type:

| Finding group | Minimum evidence |
|---|---|
| Lead capture and routing | Channel inventory plus CRM/form destination evidence or client confirmation. |
| Notifications and confirmation | Safe test or workflow/settings evidence. |
| Ownership and pipeline state | CRM fields, sample records, SOP, or client interview. |
| Follow-up and estimates | Task rules, templates, pipeline records, or client interview. |
| Review system | Review request timing, workflow, templates, or client interview. |
| Customer history/reactivation | CRM field review, list review, campaign history, or client interview. |
| Reporting | Dashboard/report review plus evidence of decision cadence. |
| Failure monitoring | Error alerts, run logs, exception handling, or marked `validation_required`. |
| AI/customer-facing automation | Configuration, logs, human review, escalation, and data-handling evidence. |

If internal systems are inaccessible, use client interview evidence and mark confidence `low` or `medium`. Do not convert absence of access into a negative score.

## Business impact language

Use report-safe language that describes reliability and execution risk without blame.

| Weak wording | Use instead |
|---|---|
| Your leads are falling through the cracks. | Lead handling appears distributed across multiple channels, which may reduce consistency in assignment, follow-up, and reporting. |
| You need a CRM. | A shared lead-tracking system would create a clearer source of truth for ownership, status, and follow-up. |
| Your team is disorganized. | Internal handoffs appear to rely on informal knowledge rather than a documented workflow. |
| You are losing money by not automating. | This creates revenue leakage risk because open inquiries or estimates may not receive consistent follow-up. |
| Automate everything. | Prioritize automation only where the workflow is repeatable, evidence-backed, and operationally controlled. |

## Recommended package routing

| Condition | Recommended package | Notes |
|---|---|---|
| Leads are scattered, ownership is unclear, stages are missing, or follow-up depends on memory. | CRM and Follow-Up System | Default Phase 3. |
| Visible inquiry confirmation or notification is broken. | Website Conversion Fix Pack and/or CRM and Follow-Up System | Use Phase 1 for immediate repair, then Phase 3 for durable workflow. |
| Review requests are inconsistent or untracked. | Review Generation System | Phase 3. |
| Pipeline, source, estimate, review, or follow-up performance is not visible. | Operator Dashboard Pack | Phase 3. |
| Workflow and data are mature enough for controlled AI assistance. | Governed AI Intake Assistant | Phase 4 only after readiness gates pass. |
| Workflow is undefined or undocumented. | Process documentation before automation | Do not deploy tool-first automation. |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | A live lead path is broken, such as failed form notification, missing confirmation, or unusable missed-inquiry recovery. |
| Phase 2 — Growth Foundation | Use rarely, when website, proof, messaging, or service architecture must be stabilized before operational automation. |
| Phase 3 — Automation and Reporting | Default for CRM, ownership, pipeline, follow-up, review requests, reactivation, templates, dashboards, and monitoring. |
| Phase 4 — Governed AI Enablement | Use only when process clarity, structured data, audit logging, review gates, boundaries, and escalation are sufficient. |

## Report-use rules

An automation finding can enter a client report only when:

1. The current workflow or evidence gap is clearly documented.
2. The finding affects reliability, ownership, response, follow-up, retention, or visibility.
3. Evidence is listed or the gap is marked `validation_required`.
4. Confidence is assigned.
5. Business impact is stated without unsupported loss claims.
6. Package routing is justified by the workflow need.
7. Roadmap phase respects prerequisites.
8. DecisionLedger entry can be completed.

Do not recommend AI, CRM, messaging, or workflow tools solely because they are available. Recommend only when evidence, score weakness, impact, readiness, and phase alignment justify implementation.

## DecisionLedger requirements

Each automation recommendation must include this ledger record:

```text
finding_id:
observation:
evidence:
interpretation:
business_impact:
confidence:
priority:
recommended_package:
roadmap_phase:
workflow_prerequisite:
control_requirement:
owner_validation_needed:
report_section:
status:
```

## Example ledger record

```text
finding_id: OI-FIND-AUTO-006
observation: Open estimates are tracked informally, and no reminder rule or scheduled follow-up task was verified.
evidence: Client interview, pipeline review, and absence of task automation in the reviewed system.
interpretation: Estimate follow-up currently depends on individual memory rather than a repeatable workflow.
business_impact: This creates revenue leakage risk because open estimates may receive inconsistent follow-up.
confidence: Medium
priority: High
recommended_package: CRM and Follow-Up System
roadmap_phase: Phase 3 — Automation and Reporting
workflow_prerequisite: Define estimate stages, follow-up timing, and owner.
control_requirement: Overdue-task alert and manual exception handling.
owner_validation_needed: Yes
report_section: Automation and Operations Findings
status: validation_required
```

## Usage instructions

1. Review the automation score and relevant criteria IDs.
2. Map each workflow from trigger to owner, state, action, exception, and outcome.
3. Inspect channel routing, CRM or tracking system, notifications, templates, and reports.
4. Match the observed weakness to the closest finding ID.
5. Assign confidence based on evidence quality.
6. Identify workflow prerequisites and control requirements.
7. Route to package and roadmap phase.
8. Write the finding using client-safe language.
9. Add the DecisionLedger record.
10. If evidence is missing, mark `validation_required` instead of forcing a recommendation.

## Completion check

Before final report use, confirm:

- Finding is evidence-backed.
- Current workflow is understood or explicitly marked unknown.
- Recommendation solves a reliability or execution problem, not a novelty preference.
- Confidence is not overstated.
- Business impact is clear.
- Package selection is justified.
- Roadmap phase respects prerequisites.
- Failure handling and ownership are considered.
- Ledger record is complete.
