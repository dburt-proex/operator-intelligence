# AI Readiness Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable AI readiness and governance findings for Operator Intelligence assessments.

AI readiness findings identify where a contractor or local-service business may be unable to use AI safely, reliably, or commercially because process clarity, structured data, approved use cases, knowledge sources, human review, customer-facing boundaries, escalation, privacy controls, auditability, prompt standards, or quality review are weak, missing, inconsistent, or unverified.

This library converts AI interest into governed readiness findings that can be scored, routed, reported, and implemented without adding AI to undefined workflows or recommending tool adoption for its own sake.

## v1.0 connection

Operator Intelligence v1.0 requires an AI-readiness layer that protects client operations while identifying controlled, commercially useful assistance opportunities.

This file strengthens v1.0 readiness by supporting:

- workflow prerequisite enforcement
- structured-data readiness evaluation
- approved use-case selection
- CASA-style ALLOW, REVIEW, and HALT controls
- PromptBP instruction standards
- human review and escalation routing
- privacy and data-boundary controls
- output logging and quality review
- Governed AI Intake Assistant package routing
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- AI readiness category score is weak, partial, unknown, or inconsistent.
- The client wants AI but cannot define the workflow, owner, input, output, or success condition.
- Lead, estimate, communication, or handoff processes are undocumented.
- Customer data is inconsistent, scattered, or unstructured.
- AI tools are already used without approved use cases or usage boundaries.
- Customer-facing AI can make promises, pricing statements, scheduling commitments, or policy interpretations without review.
- Approved knowledge sources are missing or outdated.
- AI outputs are not logged, sampled, corrected, or reviewed.
- Sensitive customer, employee, project, payment, health, legal, or authentication data may be entered into tools without rules.
- No escalation path exists for uncertainty, complaints, exceptions, or high-risk requests.

## Outputs and deliverables

A valid use of this file should produce:

- one or more AI readiness findings
- evidence record for each finding
- readiness tier or validation state
- confidence level
- risk and business impact statement
- ALLOW, REVIEW, or HALT routing state
- prerequisite package when required
- AI implementation package when justified
- roadmap phase
- DecisionLedger entry
- executive-safe client language

## Governance rules

1. Do not recommend AI implementation before the target workflow, owner, inputs, outputs, exceptions, and success criteria are sufficiently defined.
2. AI interest, tool ownership, or prior experimentation is not proof of readiness.
3. Unknown process, data, access, privacy, or control conditions must be marked `unknown` or `validation_required`.
4. Use `HALT` when a proposed use case could create binding promises, unreviewed pricing, unsafe advice, uncontrolled data exposure, or customer harm.
5. Use `REVIEW` when AI can assist but human approval, escalation, sampling, or exception handling is required.
6. Use `ALLOW` only for low-risk, bounded work with approved inputs, instructions, sources, logging, and ownership.
7. Do not treat AI as a replacement for missing process design, CRM structure, source documentation, or accountability.
8. Customer-facing AI must have approved topics, blocked topics, uncertainty behavior, escalation rules, and identity disclosure when appropriate.
9. Sensitive data use requires explicit tool, access, storage, retention, and sharing rules.
10. AI-generated pricing, guarantees, availability, legal terms, safety guidance, complaint resolutions, or binding commitments require human review unless separately approved under a documented control policy.
11. AI output quality must be reviewed against examples, failure patterns, corrections, and updated rules.
12. A recommendation is valid only when observation, evidence, interpretation, impact, confidence, priority, control state, package, roadmap phase, and ledger record are present.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Workflow Definition Gate | Task, trigger, owner, inputs, outputs, handoffs, exceptions, and completion state are documented. | AI is placed into an undefined workflow. | HALT AI implementation and document process first. |
| Use-Case Fit Gate | Use case solves a defined operational problem with bounded scope. | Use case is tool-first, vague, or broad. | Mark `validation_required`. |
| Data Readiness Gate | Required data is structured, accessible, accurate enough, and governed. | Inputs are inconsistent, incomplete, or scattered. | Route prerequisite to CRM and Follow-Up System. |
| Knowledge Source Gate | Approved source material exists and has an owner and review date. | AI relies on memory, uncontrolled web content, or outdated documents. | HALT customer-facing use. |
| Permission Gate | Tool access matches role and least-privilege need. | AI or user can access unnecessary sensitive systems or data. | Restrict access before use. |
| Privacy Gate | Allowed, restricted, and prohibited data are defined with retention and sharing rules. | Sensitive data may be copied into tools without control. | HALT affected workflow. |
| Human Review Gate | Review is required for sensitive, uncertain, exceptional, or binding outputs. | AI can act without appropriate approval. | Set REVIEW or HALT. |
| Boundary Gate | Allowed topics, blocked topics, disclaimers, and action limits are explicit. | Customer-facing scope is open-ended. | HALT launch. |
| Escalation Gate | Named human route and trigger conditions exist. | AI has no path for uncertainty or exceptions. | Set REVIEW and add escalation. |
| Prompt Standard Gate | Instructions define role, objective, inputs, constraints, outputs, rules, and checks. | Behavior depends on informal prompts. | Apply PromptBP standard. |
| Auditability Gate | Inputs, outputs, approvals, corrections, and actions can be logged where required. | AI activity leaves no trace. | Block higher-risk use. |
| Quality Review Gate | Samples, error categories, owner, cadence, and correction process exist. | Performance is assumed from anecdotal success. | Add QA review before scaling. |
| Control State Gate | Each use case is classified ALLOW, REVIEW, or HALT. | Risk is discussed without an execution decision. | Block roadmap entry. |
| Package Gate | Prerequisite and AI packages match actual readiness. | AI package is selected because it is sellable. | Re-route or block. |
| Roadmap Gate | Workflow and data prerequisites precede AI implementation. | Phase 4 is scheduled before Phase 3 dependencies. | Re-sequence. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Control states

| State | Meaning | Typical use |
|---|---|---|
| ALLOW | Low-risk, bounded assistance may proceed under approved instructions and logging. | Internal drafting, summarization, categorization, FAQ retrieval from approved sources. |
| REVIEW | AI may prepare or recommend, but a human must approve or handle exceptions. | Customer replies, estimate preparation, complaint drafting, qualification, scheduling suggestions. |
| HALT | Do not implement or continue until required controls or prerequisites exist. | Binding pricing, uncontrolled promises, sensitive-data exposure, unsafe advice, undefined workflows. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct workflow documentation, tool configuration, access review, logs, policies, prompts, or observed operation confirms the condition. |
| Medium | Interviews, screenshots, or partial artifacts support the pattern, but behavior, data handling, or exceptions are not fully tested. |
| Low | Finding depends on owner recollection, inaccessible tools, undocumented use, unclear data flows, or unverified controls. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Control state | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|---|
| OI-FIND-AI-001 | Core workflow is undocumented | OI-AI-001 | SOP, checklist, workflow map, owner interview | AI may automate inconsistency or create new failure paths because the operating process is not stable. | HALT | CRM and Follow-Up System or process-documentation prerequisite | Phase 3 before Phase 4 | Medium |
| OI-FIND-AI-002 | Workflow ownership and handoffs are unclear | OI-AI-001, OI-AI-010 | Role map, handoff notes, escalation path | AI-assisted work may remain unowned or fail during exceptions. | HALT or REVIEW | CRM and Follow-Up System | Phase 3 before Phase 4 | Medium |
| OI-FIND-AI-003 | Customer data is unstructured or inconsistent | OI-AI-002 | CRM fields, spreadsheet, form inputs, data sample | AI outputs may be incomplete, misrouted, or unreliable because inputs lack consistent structure. | HALT for automation; REVIEW for limited assistance | CRM and Follow-Up System | Phase 3 — Automation and Reporting | High when records are reviewed |
| OI-FIND-AI-004 | Required status or outcome fields are missing | OI-AI-002, OI-AN related signals | CRM schema, pipeline, outcome records | AI cannot reliably classify state, recommend next action, or support measurement. | HALT for autonomous routing | CRM and Follow-Up System plus Operator Dashboard Pack | Phase 3 | High when observable |
| OI-FIND-AI-005 | AI use case is undefined or tool-first | OI-AI-003 | Strategy notes, owner interview, proposed workflow | Investment may produce experimentation without a governed business outcome. | HALT | Validation task before Governed AI Intake Assistant | Phase 1 validation, then Phase 4 if justified | High when observable |
| OI-FIND-AI-006 | AI use case lacks owner, inputs, outputs, or success criteria | OI-AI-003 | Use-case brief, workflow map, KPI definition | The business cannot determine whether the AI workflow is operating correctly or creating value. | HALT | Operator Dashboard Pack for measurement plus use-case definition | Phase 3 prerequisite | Medium to High |
| OI-FIND-AI-007 | Human review gates are missing | OI-AI-004 | Tool configuration, SOP, approval workflow, sample interactions | Sensitive or inaccurate outputs may reach customers without correction. | HALT | Governed AI Intake Assistant after review controls | Phase 4 — Governed AI Enablement | High when observable |
| OI-FIND-AI-008 | Review gates do not cover pricing, promises, complaints, or exceptions | OI-AI-004, OI-AI-005 | Prompt rules, policies, test cases, sample transcripts | AI may create expectation, financial, trust, or service-delivery risk. | HALT | Governed AI Intake Assistant | Phase 4 | High when observable |
| OI-FIND-AI-009 | Customer-facing AI boundaries are unclear | OI-AI-005 | Assistant instructions, allowed-topic list, blocked-topic list | The system may answer outside approved service, policy, or decision boundaries. | HALT | Governed AI Intake Assistant | Phase 4 | High when observable |
| OI-FIND-AI-010 | AI can make binding commitments without approval | OI-AI-004, OI-AI-005 | Test interactions, tool actions, policies | The business may create unauthorized pricing, scheduling, guarantee, or scope commitments. | HALT | Governed AI Intake Assistant with mandatory review | Phase 4 | High when tested |
| OI-FIND-AI-011 | Approved knowledge base is missing | OI-AI-006 | FAQ, service documents, policies, source inventory | AI may produce inconsistent answers because it lacks controlled source material. | HALT for customer-facing use | Governed AI Intake Assistant prerequisite | Phase 4 | High when observable |
| OI-FIND-AI-012 | Knowledge base is outdated or has no owner | OI-AI-006 | Document dates, owner, change log, source review | Correct information may degrade over time without a governed update process. | REVIEW | Governed AI Intake Assistant | Phase 4 | Medium to High |
| OI-FIND-AI-013 | AI outputs are not logged | OI-AI-007 | Transcript storage, CRM notes, audit log, tool settings | Errors, promises, corrections, and customer interactions may be difficult to investigate. | HALT for higher-risk use; REVIEW for low-risk use | Governed AI Intake Assistant plus Operator Dashboard Pack if reporting is needed | Phase 4 | High when observable |
| OI-FIND-AI-014 | Human approvals and corrections are not recorded | OI-AI-007 | Approval history, CRM notes, revision logs | The business cannot reliably audit who accepted, changed, or acted on AI output. | REVIEW or HALT | Governed AI Intake Assistant | Phase 4 | Medium to High |
| OI-FIND-AI-015 | Sensitive-data rules are undefined | OI-AI-008 | Policy, tool settings, data-flow review, access review | Customer or business information may be exposed, retained, or shared without approved boundaries. | HALT | Privacy and workflow prerequisite before Governed AI Intake Assistant | Phase 1 correction, then Phase 4 | Medium to High |
| OI-FIND-AI-016 | Tool access exceeds operational need | OI-AI-008 | Permission review, integrations, user roles | Excess access increases exposure and unauthorized-action risk. | HALT affected access | Governed AI Intake Assistant prerequisite with least-privilege controls | Phase 4 | High when access is reviewed |
| OI-FIND-AI-017 | First AI use case is too high risk | OI-AI-009 | Use-case list, risk assessment, owner interview | Early implementation may place pricing, commitments, complaints, or sensitive decisions into an immature control system. | HALT | Start with bounded low-risk assistance before Governed AI Intake Assistant expansion | Phase 4 | High when observable |
| OI-FIND-AI-018 | Low-risk pilot opportunity is defined but not controlled | OI-AI-003, OI-AI-009 | Pilot brief, sample inputs, review plan, logging plan | A commercially useful pilot exists, but missing controls may prevent reliable learning. | REVIEW | Governed AI Intake Assistant | Phase 4 | Medium |
| OI-FIND-AI-019 | Escalation path is missing | OI-AI-010 | Escalation SOP, owner assignment, test cases | Uncertain, unusual, or high-risk requests may receive incomplete or inappropriate handling. | HALT customer-facing launch | Governed AI Intake Assistant | Phase 4 | High when observable |
| OI-FIND-AI-020 | Escalation triggers are vague or untested | OI-AI-010 | Trigger list, test transcripts, exception review | AI may fail to hand off cases that exceed its approved boundary. | REVIEW | Governed AI Intake Assistant | Phase 4 | Medium to High |
| OI-FIND-AI-021 | Prompt instructions are informal or inconsistent | OI-AI-011 | Prompt inventory, system instructions, templates | Behavior may vary because role, objective, inputs, constraints, outputs, and checks are not standardized. | REVIEW | Governed AI Intake Assistant using PromptBP | Phase 4 | High when observable |
| OI-FIND-AI-022 | Prompt rules do not include recursive checks or failure behavior | OI-AI-011 | Prompt review, test cases, output samples | AI may answer confidently despite missing evidence, uncertainty, or policy conflicts. | REVIEW or HALT based on use case | Governed AI Intake Assistant | Phase 4 | Medium to High |
| OI-FIND-AI-023 | AI performance is not reviewed | OI-AI-012 | QA records, sample reviews, owner interview | Failure patterns may persist because no one samples outputs or updates rules. | REVIEW | Governed AI Intake Assistant plus Operator Dashboard Pack when metrics are needed | Phase 4 | High when observable |
| OI-FIND-AI-024 | QA review lacks categories, owner, cadence, or corrective action | OI-AI-012 | QA checklist, issue log, change log, meeting notes | Quality review may exist but fail to produce controlled improvement. | REVIEW | Governed AI Intake Assistant | Phase 4 | Medium to High |
| OI-FIND-AI-025 | AI-generated customer communication is published without provenance or approval record | OI-AI-004, OI-AI-007 | Message logs, CRM records, approval workflow | The business may be unable to distinguish human-approved communication from uncontrolled AI output. | HALT | Governed AI Intake Assistant | Phase 4 | Medium to High |
| OI-FIND-AI-026 | AI roadmap precedes automation and analytics prerequisites | OI-AI-001, OI-AI-002, OI-AI-012 | Roadmap, CRM status, workflow documentation, reporting readiness | AI implementation may amplify fragmented operations and remain difficult to measure. | HALT sequencing | CRM and Follow-Up System plus Operator Dashboard Pack before Governed AI Intake Assistant | Phase 3 before Phase 4 | High when observable |

## Criteria mapping rules

Use AI readiness findings when the issue concerns controlled AI adoption, not general automation or software selection.

| Observed issue | Primary domain | Routing rule |
|---|---|---|
| Workflow is undefined or manually inconsistent | Automation or offer | Complete process and CRM prerequisites before AI. |
| Customer records are inconsistent | Automation | Route to CRM and Follow-Up System. |
| AI outcome cannot be measured | Analytics | Route to Operator Dashboard Pack. |
| Approved source material is missing | Messaging, offer, trust, or operations | Build source content before AI knowledge use. |
| Customer-facing boundaries or review are missing | AI readiness | HALT until governed controls exist. |
| Tool is used only for private low-risk drafting | AI readiness | May be ALLOW or REVIEW depending on data and publication controls. |
| Competitive AI activity is observed | Competitive | Do not increase readiness score or priority without internal fit evidence. |

## Evidence requirements

Acceptable evidence includes:

- SOPs and workflow maps
- CRM schema and data samples
- tool configuration and permissions
- approved use-case brief
- prompts and system instructions
- knowledge-base inventory
- policies and data-handling rules
- test conversations and output samples
- approval records and audit logs
- escalation rules
- QA records and correction logs
- client interview
- roadmap and package dependencies

Minimum evidence:

| Finding group | Minimum evidence |
|---|---|
| Process clarity | SOP, workflow map, checklist, or structured owner interview. |
| Data readiness | CRM fields, forms, spreadsheet, or representative data sample. |
| Use-case fit | Defined task, owner, inputs, outputs, risk, and success condition. |
| Human review and boundaries | Tool rules, approval workflow, policies, or tested interactions. |
| Privacy and permissions | Access review, data-flow review, policy, or marked `validation_required`. |
| Knowledge base | Source inventory, owner, approval state, and review date. |
| Auditability | Logs, transcripts, CRM notes, approvals, or tool history. |
| Quality review | QA samples, issue categories, owner, cadence, and corrective actions. |

## Business impact language

| Weak wording | Use instead |
|---|---|
| The business is not ready for AI. | The current workflow and data controls do not yet support this AI use case reliably. |
| AI will save a lot of money. | A bounded AI workflow may reduce repetitive effort, but impact requires baseline and post-implementation measurement. |
| The chatbot is dangerous. | The customer-facing assistant lacks sufficient boundaries, review, or escalation controls for its current scope. |
| Your data is a mess. | Customer and workflow data are not yet structured consistently enough for reliable AI routing or output. |
| AI can replace this role. | AI may assist selected tasks, while ownership, review, exceptions, and accountability remain human-controlled. |

## Recommended package routing

| Condition | Recommended package | Default phase |
|---|---|---|
| Workflow, CRM, handoff, or data structure is weak | CRM and Follow-Up System | Phase 3 prerequisite |
| Measurement, logging, or QA visibility is weak | Operator Dashboard Pack | Phase 3 or Phase 4 dependency |
| Use case is defined and readiness gates pass | Governed AI Intake Assistant | Phase 4 |
| Customer-facing boundaries or review are missing | Governed AI Intake Assistant only after HALT conditions are resolved | Phase 4 |
| Knowledge source, privacy, or access controls are missing | Validation and governance prerequisite | Before Phase 4 |
| AI use case remains vague or tool-first | No AI package; complete use-case definition | Validation stage |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Stop misleading or uncontrolled AI behavior, remove unsafe access, or define immediate usage restrictions. |
| Phase 2 — Growth Foundation | Build approved source content, service information, policies, and buyer-facing knowledge required by the use case. |
| Phase 3 — Automation and Reporting | Document workflows, structure data, assign ownership, implement CRM stages, logging, and measurement. |
| Phase 4 — Governed AI Enablement | Implement bounded AI assistance with PromptBP instructions, review gates, escalation, audit logs, and QA cadence. |

## Report-use rules

An AI readiness finding can enter a client report only when:

1. The specific use case or readiness dependency is identified.
2. Evidence is listed or the condition is marked `validation_required`.
3. Control state is assigned as ALLOW, REVIEW, or HALT.
4. Confidence reflects access and test limitations.
5. Risk and business impact are stated without AI hype or unsupported ROI.
6. Prerequisites and package routing are explicit.
7. Roadmap phase preserves Phase 3 before Phase 4 dependencies.
8. DecisionLedger entry is complete.

## DecisionLedger requirements

Each AI readiness recommendation must include:

```text
finding_id:
use_case:
observation:
evidence:
interpretation:
business_impact:
risk:
confidence:
priority:
control_state: ALLOW | REVIEW | HALT
prerequisite_package:
recommended_package:
roadmap_phase:
data_classification:
human_review_required:
escalation_owner:
audit_requirement:
qa_requirement:
owner_validation_needed:
report_section:
status:
```

## Example ledger record

```text
finding_id: OI-FIND-AI-007
use_case: Customer-facing intake assistant
observation: The assistant can generate customer responses, but no documented approval step exists for pricing, promises, complaints, or unusual requests.
evidence: Assistant configuration review and sample interaction test.
interpretation: The system can communicate beyond low-risk intake collection without a controlled human review boundary.
business_impact: This creates expectation and service-delivery risk because inaccurate or unauthorized statements could reach buyers.
risk: High
confidence: High
priority: Critical
control_state: HALT
prerequisite_package: CRM and Follow-Up System if inquiry routing is not yet structured
recommended_package: Governed AI Intake Assistant
roadmap_phase: Phase 4 — Governed AI Enablement
human_review_required: Yes
escalation_owner: Designated sales or operations owner
audit_requirement: Store input, output, approval, correction, and final message
qa_requirement: Monthly sample review plus immediate review of escalations
owner_validation_needed: Yes
report_section: AI Readiness Findings
status: blocked_pending_controls
```

## Usage instructions

1. Define the proposed or existing AI use case.
2. Inspect workflow, data, knowledge, access, privacy, boundaries, review, escalation, logging, prompts, and QA.
3. Assign confidence and ALLOW, REVIEW, or HALT.
4. Route workflow and data prerequisites to Phase 3 packages.
5. Route controlled AI implementation to Phase 4 only when readiness gates pass.
6. Record evidence limitations and owner validations.
7. Complete the DecisionLedger record.
8. Reassess control state after implementation changes.

## Completion check

Before final report use, confirm:

- Use case is specific and bounded.
- Workflow and data prerequisites are evaluated.
- Privacy, permissions, review, boundaries, and escalation are controlled.
- Control state is assigned.
- Confidence is not overstated.
- AI impact claims are evidence-safe.
- Phase 3 dependencies precede Phase 4.
- Ledger record is complete.
