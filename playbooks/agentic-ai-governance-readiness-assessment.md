# Agentic AI Governance Readiness Assessment

Version: v0.1 proposed protocol  
Status: Draft for governed review; internal-only  
Directive: `LD-2026-07-22-001`  
Target project: Operator Intelligence Agentic AI Governance Readiness Assessment  
Control gate for this increment: `ALLOW`  
Implementation authorization: `false`

## 1. Protocol decision and purpose

This document defines a bounded, evidence-backed buyer engagement for organizations evaluating or deploying AI agents. It converts the existing Operator Intelligence assess-to-prioritize architecture into a readiness assessment without creating a runtime, changing scoring formulas, or authorizing implementation.

The protocol answers one decision question:

> Given the stated agent scope, evidence, authority, and operating context, which governance controls are verified, partial, missing, unknown, or not applicable, and what should be validated or prioritized before the buyer expands the agent's authority?

The protocol produces a defensible current-state assessment. “Readiness” means readiness for the stated decision and reviewed scope. It does not mean certification, regulatory compliance, security clearance, or production readiness.

The protocol preserves the existing Operator Intelligence chain:

```text
Scope and authority
→ Evidence admission
→ Control mapping
→ Governed findings
→ Risk / impact / opportunity synthesis
→ Recommendation priority
→ Recommendation handoff
→ DecisionLedger
```

This is a proposed assessment behavior layered over existing repository controls. It is not a replacement for the canonical lifecycle, evidence standard, confidence standard, recommendation standard, publication standard, or DecisionLedger standard.

## 2. Claim status and evidence boundary

The protocol separates what is already present in the repository from what this increment proposes.

| Classification | Treatment in this protocol |
|---|---|
| **Verified repository capability** | Operator Intelligence already contains an assess-to-prioritize lifecycle, evidence admission rules, finding controls, confidence separation, priority inputs, risk gates, publication boundaries, and DecisionLedger traceability. These authorities are linked in [References](#22-references). |
| **Proposed assessment behavior** | The seven-domain agentic assessment, deterministic finding states, domain evidence map, buyer engagement boundary, and handoff sequence are defined here for review. They are not represented as externally validated or production-operated behavior. |
| **Assumption** | The buyer can name an accountable sponsor, provide or authorize the evidence needed for the stated scope, identify the agent and connected systems, and distinguish assessment access from implementation access. |
| **Explicit exclusion** | No statement in this protocol claims certification, regulatory compliance, customer validation, production readiness, guaranteed risk reduction, or a completed assessment for any organization. |

The market rationale supplied with directive `LD-2026-07-22-001` is treated as decision context, not as evidence about a buyer, a customer, or the effectiveness of this protocol. External buyer validation remains an open risk.

## 3. Assessment problem

Organizations may have an agent, agent portfolio, or agent-enabled workflow without a single evidence-backed view of:

- who owns the agent and the decision it supports
- what data and systems it can access
- which tools and actions it can invoke
- where human approval is required
- how failure and abuse are tested
- whether material actions are logged and auditable
- how deployment, monitoring, rollback, and incidents are controlled

The assessment converts that uncertainty into a bounded control picture and a prioritized handoff. It does not operate the agent, redesign the customer’s systems, or decide on the customer’s behalf.

## 4. Intended buyer and explicit non-customer

### Intended buyer

The intended buyer is an organization, business unit, product team, or engineering team that is evaluating, piloting, governing, or expanding one or more AI agents and needs an independent readiness view before a material decision. The buyer must have:

- a named sponsor and decision authority
- a defined agent or bounded agent portfolio
- a stated decision, such as pilot continuation, scope expansion, control remediation, or deployment review
- authority to provide or authorize the evidence in scope
- willingness to preserve unknowns and limitations rather than require a favorable conclusion

The protocol can assess internal, employee-facing, customer-facing, or operational agents when the applicable evidence and authority boundaries are explicit.

### Explicit non-customer

This protocol is not the right engagement for an organization that primarily wants:

- a certification, attestation, legal opinion, or regulatory compliance determination
- a penetration test, red-team exercise, formal security audit, or privacy impact assessment
- a vendor product certification or ranking
- unrestricted access to production systems or customer data without defined authority
- an implementation team, managed operations, custom runtime, or deployment service as part of the assessment
- a generic maturity score with no named decision, evidence owner, or review authority
- a conclusion that treats missing access as a verified governance failure

Such requests require a separate scope decision or a different qualified provider. They must not be silently absorbed into this protocol.

## 5. Prerequisites and authority boundaries

### 5.1 Required prerequisites

The assessment may enter intake only when the following are recorded:

1. **Decision:** the buyer decision the assessment will inform.
2. **Subject:** agent name or bounded agent-portfolio identifier, version if known, purpose, users, and operating context.
3. **Scope:** environments, workflows, systems, data classes, geography or business unit if relevant, review period, and explicit exclusions.
4. **Authority:** accountable sponsor, decision authority, technical owner, data/system owners, evaluator role, and written testing authority where testing is requested.
5. **Evidence plan:** sources, owners, collection method, evidence snapshot date, retention/handling rules, and known access limitations.
6. **Safety boundary:** prohibited actions, no-go data, safe-test conditions, change restrictions, rollback contact, and incident/escalation route.
7. **Independence declaration:** conflicts, vendor relationships, implementation relationships, and any limitation on independent judgment.
8. **DecisionLedger identity:** assessment ID, engagement ID if used, methodology version, protocol version, and record owner.

Missing authority, undefined production impact, prohibited data access, or an unbounded requested test routes the intake to `HALT` until corrected.

### 5.2 Evaluator authority

Unless a separate written authorization says otherwise, the evaluator may:

- review supplied documentation, records, configurations, logs, test results, and demonstrations within scope
- inspect authorized read-only views
- perform explicitly authorized, reversible, non-customer-impacting safe tests
- record evidence, limitations, unknowns, contradictions, findings, priorities, and handoff recommendations
- request clarification or additional evidence

The evaluator may not, under this protocol:

- deploy, modify, configure, patch, or roll back a system
- grant, expand, or revoke permissions
- use secrets or credentials outside the approved access method
- send external communications, create transactions, change records, or trigger customer-impacting actions
- approve production use, certify a control, or accept risk for the buyer
- suppress an inconvenient finding, convert unknown evidence into a gap, or represent a recommendation as authorization
- place customer data, secrets, or restricted evidence in the repository

The buyer retains operational, legal, risk-acceptance, and implementation authority. Assessment `ALLOW` permits the assessment to advance within scope; it does not authorize system change.

### 5.3 Assessment unit

The unit of assessment is a named agent or a bounded agent portfolio plus its connected workflow. A portfolio must have a stated inclusion rule. Each control observation receives one primary domain owner. Cross-domain effects may be referenced, but duplicate weighted ownership is prohibited.

## 6. Evidence contract

### 6.1 Required evidence record

Each evidence item must be represented using the existing Operator Intelligence evidence conventions in [Evidence Register](../templates/evidence-register.md). At minimum, record:

```yaml
evidence_id: OI-EV-YYYY-NNN
assessment_id: ""
source_type: screenshot|document|export|system_record|safe_test|interview|observation|third_party
source_location: ""
source_owner: public|client|evaluator|third_party
evidence_class: A|B|C|D|E
captured_at: "YYYY-MM-DDThh:mm:ssZ"
source_date: null
scope: ""
claim_scope: ""
capture_method: ""
authorization_ref: null
observation: ""
limitations: []
integrity_ref: null
sensitivity: public|internal|confidential|restricted
review_state: accepted|limited|rejected|superseded
confidence_support: high|medium|low|unknown
ledger_refs: []
```

Evidence supports a decision; it does not replace the finding, confidence assignment, review, or authorization decision.

### 6.2 Evidence quality classes

The protocol reuses the repository's existing evidence classes:

| Class | Meaning | Normal use in this assessment |
|---|---|---|
| `A` | Directly observable or testable | May support a verified control or gap when the review is authorized, current, attributable, and in scope. |
| `B` | Comparative evidence against a defined set | May support a control comparison when the comparator, date, scope, and limitations are recorded. |
| `C` | Approved pattern applied to visible evidence | Supports a bounded interpretation only when the pattern and applicability are explicit. |
| `D` | Inferred or plausible, not directly verified | Validation-only by default; cannot independently create a verified gap or implementation route. |
| `E` | Buyer-provided record, export, screenshot, or statement | Use according to completeness, reliability, corroboration, scope, and source-owner authority. |

Evidence class does not mechanically determine confidence. Admission must also consider identity, attribution, recency, relevance, scope, integrity, authorization, traceability, and limitations.

### 6.3 Evidence admission rules

1. Assign one stable Evidence ID per distinct source, test, observation, or record.
2. Freeze the evidence snapshot date before findings are finalized.
3. Preserve source date, capture date, scope, method, owner, and authorization separately.
4. Keep contradictions visible; do not average them into certainty.
5. Treat public absence as “not visible on tested public surfaces,” not proof that an internal control does not exist.
6. Treat missing access as `UNKNOWN` or a blocked condition, not as a negative result.
7. Reject or limit evidence that cannot be attributed, reproduced, handled safely, or connected to the stated decision.
8. Create a DecisionLedger event for material admission, rejection, limitation, contradiction, or supersession.

### 6.4 Confidence rules for every finding

Every finding must include `confidence`, `confidence_basis`, `evidence_refs`, `limitations`, `unknowns`, and `validation_required`. Confidence follows [Confidence Standard](../standards/confidence-standard.md) and cannot modify maturity or priority.

| Confidence | Use when | Finding treatment |
|---|---|---|
| `high` | Direct, current, attributable, authorized evidence covers the required scope with no material unresolved conflict. | May support a direct finding and recommendation handoff when all other gates pass. |
| `medium` | Evidence supports the condition, but one material and bounded limitation remains, such as incomplete internal validation or partial sample coverage. | May support bounded language and `REVIEW` or conditional handoff with the limitation disclosed. |
| `low` | The interpretation depends materially on indirect, stale, narrow, interview-led, or partially accessible evidence. | Normally routes to validation before implementation-related action; no certainty language. |
| `unknown` | Evidence is absent, rejected, materially conflicting, unauthorized, or insufficient to defend a finding state. | No verified gap, control, or implementation recommendation may be asserted. Route to validation, `REVIEW`, or `HALT` as applicable. |

`blocked` is a control/evidence condition, not a confidence level. A blocked review normally records `confidence: unknown` plus the blocking condition.

### 6.5 Evidence quality and confidence floor

The finding's confidence may not exceed the weakest material evidence dependency. A finding may use corroborating evidence of different classes, but the record must explain which evidence carries the conclusion and which is reference-only. A low-confidence or unknown input cannot be concealed by a high-confidence contextual source.

## 7. Exactly seven assessment domains

This protocol has exactly seven assessment domains. No additional domain may be added during an engagement without reopening the protocol scope and recording a governed methodology decision.

| # | Domain ID | Assessment domain | Required control question |
|---:|---|---|---|
| 1 | `AIGR-D1` | Agent purpose and ownership | Is the agent's purpose bounded, accountable, and connected to named business and technical owners? |
| 2 | `AIGR-D2` | Data and system access | Are data sources, system boundaries, data classes, access grants, and retention rules authorized and understood? |
| 3 | `AIGR-D3` | Tool and action authority | Are tools, scopes, actions, approvals, limits, and reversal or containment paths explicit and least-privileged? |
| 4 | `AIGR-D4` | Workflow approvals and human intervention | Are decision points, human approvals, exceptions, overrides, escalation, and handoffs defined for consequential work? |
| 5 | `AIGR-D5` | Evaluation and failure testing | Are expected behaviors, failure cases, adversarial cases, regression tests, thresholds, and evaluation ownership defined? |
| 6 | `AIGR-D6` | Logging, evidence, and auditability | Can the organization reconstruct material inputs, outputs, tool calls, approvals, corrections, versions, and decisions? |
| 7 | `AIGR-D7` | Deployment, monitoring, rollback, and incident response | Are release boundaries, monitoring, alerts, rollback, incident handling, ownership, and learning loops defined? |

### 7.1 Domain evidence map

The following is the minimum evidence focus for each domain. It is a collection plan, not a claim that every buyer will possess every source.

| Domain | Minimum evidence focus | Typical unknown if unavailable |
|---|---|---|
| `AIGR-D1` | Use-case or agent brief, intended users, business owner, technical owner, decision authority, allowed/prohibited purpose, accountability model, version or change history. | Purpose, owner, or decision accountability cannot be confirmed. |
| `AIGR-D2` | System and data-source inventory, data classification, data-flow or retrieval map, permission grants, source owners, retention/deletion rules, access review record. | Actual data exposure, source authority, or least-privilege status cannot be confirmed. |
| `AIGR-D3` | Tool manifest, scopes, action list, allow/deny policy, approval requirements, rate/volume limits, action logs, containment or reversal procedure. | Effective action authority or control over consequential actions cannot be confirmed. |
| `AIGR-D4` | Workflow map, trigger/state definitions, human-in-the-loop points, approval record, exception paths, escalation route, override rules, completion criteria. | Human control may exist in practice but cannot be verified for the reviewed workflow. |
| `AIGR-D5` | Evaluation specification, representative cases, failure and abuse cases, regression results, thresholds, test owner, test date, defect disposition, drift criteria. | Behavior under failure, edge, or changed-context conditions cannot be assessed. |
| `AIGR-D6` | Event/log schema, trace or correlation IDs, input/output and model/tool versions, approval/correction records, retention, access controls, ledger or audit export. | Material actions cannot be reconstructed or independently reviewed. |
| `AIGR-D7` | Environment map, release/change controls, monitoring signals, alert thresholds, rollback runbook, incident process, ownership, exercise or incident evidence, post-incident learning. | Safe release, detection, containment, or recovery cannot be confirmed. |

## 8. Deterministic finding states

### 8.1 Required finding contract

Every finding uses the existing finding-register conventions in [Finding Register](../templates/finding-register.md) and adds the agentic protocol state as a controlled field:

```yaml
finding_id: AIGR-F-DOMAIN-NNN
finding_version: "1.0"
assessment_id: ""
domain_id: AIGR-D1|AIGR-D2|AIGR-D3|AIGR-D4|AIGR-D5|AIGR-D6|AIGR-D7
control_question: ""
state: VERIFIED_GAP|PARTIAL_CONTROL|CONTROLLED|UNKNOWN|NOT_APPLICABLE
observation: ""
interpretation: ""
business_impact: ""
evidence_refs: []
evidence_classes: []
evidence_quality_summary: ""
confidence: high|medium|low|unknown
confidence_basis: ""
assumptions: []
limitations: []
unknowns: []
validation_required: []
contradictory_evidence_refs: []
weighted_owner: ""
reference_only_uses: []
control_gate: ALLOW|REVIEW|HALT
review_state: candidate|validation_required|validated|blocked|suppressed|published|closed|superseded
recommendation_refs: []
ledger_refs: []
```

The protocol state is separate from the existing lifecycle state, confidence, review state, publication state, and control gate. It must not be substituted for any of them.

### 8.2 State definitions

| Finding state | Deterministic rule | Required treatment |
|---|---|---|
| `NOT_APPLICABLE` | The control question does not apply to the explicitly scoped agent/workflow, and the decision authority records the reason and scope test. | No gap or control conclusion; retain the rationale and do not silently remove the item from the audit trail. |
| `UNKNOWN` | Evidence is absent, rejected, unauthorized, materially conflicting, or insufficient to determine whether the control is present and effective. | No negative inference. Record the missing evidence, owner, validation action, and decision effect. Normally `REVIEW`; `HALT` when the missing authority or control boundary prevents safe continuation. |
| `VERIFIED_GAP` | Within the reviewed scope, admissible evidence directly shows a required control is absent, disallowed, or ineffective for the stated control question. | State the observed gap and scope; do not generalize beyond the evidence. Route according to impact, confidence, and authority. |
| `PARTIAL_CONTROL` | Admissible evidence shows that a relevant control exists but is incomplete, inconsistently applied, insufficiently bounded, or missing a material safeguard. | State both the verified control and the bounded deficiency. Identify the validation or remediation condition. |
| `CONTROLLED` | Admissible evidence shows the required control is defined, authorized, operating, and effective for the reviewed scope and sample. | Report as controlled for the reviewed scope only; do not infer certification or production readiness. |

### 8.3 Resolution order

Apply the following order to every domain:

1. Confirm the domain and control question are in scope. If not, assign `NOT_APPLICABLE`.
2. Confirm evidence authorization, identity, scope, integrity, and sufficiency. If the control cannot be determined, assign `UNKNOWN`.
3. If direct admissible evidence shows the required control is absent, disallowed, or ineffective, assign `VERIFIED_GAP`.
4. If a control exists but material limits remain, assign `PARTIAL_CONTROL`.
5. Assign `CONTROLLED` only when the required control and its operation are evidenced for the reviewed scope and sample.
6. Assign confidence, limitations, control gate, and DecisionLedger references after the state is selected.

No evaluator may choose a state because it is commercially attractive, because an agent uses a particular vendor, or because a control is common in the market. A material state change requires a new or superseding record; approved findings are never silently overwritten.

## 9. Risk routing

Risk routing is distinct from finding state. It determines whether the assessment record may advance to the next governed step.

| Route | Meaning | Minimum conditions |
|---|---|---|
| `ALLOW` | The bounded assessment or handoff may advance within the authorized scope. | Evidence and authority are sufficient; no unresolved G4 boundary or prohibited action exists; limitations are visible; ownership, dependencies, and traceability are present. `ALLOW` does not authorize implementation. |
| `REVIEW` | A named human reviewer must resolve, accept, or condition a material limitation before advancement. | Material uncertainty, conflict, high-impact finding, medium/low confidence, cross-domain dependency, external action, sensitive data, or judgment beyond the evaluator's authority is present. |
| `HALT` | Assessment activity or downstream handoff must stop until the boundary is restored. | Missing authority for required access/testing, unsafe or irreversible test, secret/restricted-data exposure, critical action without a safe boundary, broken evidence integrity, absent owner/decision authority, invalid scope, or failed traceability/publication control. |

### 9.1 Routing rules

- A `CONTROLLED` finding may still route to `REVIEW` or `HALT` if the surrounding workflow or authority boundary fails.
- A `VERIFIED_GAP` does not automatically route to `HALT`; severity, scope, confidence, and consequence determine the route.
- `UNKNOWN` normally routes to validation and `REVIEW`; it routes to `HALT` when proceeding would require unsafe inference or unauthorized action.
- Any `HALT` condition blocks dependent recommendation handoff until a superseding record resolves it.
- `ALLOW`, `REVIEW`, and `HALT` are recorded in the DecisionLedger and are not substitutes for finding state or implementation authorization.

## 10. Assessment workflow

The protocol maps to existing Operator Intelligence lifecycle controls and does not create new lifecycle IDs.

| Protocol step | Existing lifecycle alignment | Required actions | Exit evidence and route |
|---|---|---|---|
| **1. Intake** | `OI-LC-01` → `OI-LC-02` | Record decision, subject, scope, owners, authority, data rules, test boundary, exclusions, evidence plan, independence, and initial gate. | Assessment control record; `ALLOW`, `REVIEW`, or `HALT`. |
| **2. Evidence collection** | `OI-LC-03` → `OI-LC-04` | Inventory agent/workflow surfaces; collect authorized evidence; assign Evidence IDs; admit, limit, reject, or block sources; freeze snapshot; register unknowns and contradictions. | Evidence register and snapshot; unresolved material limitations remain visible. |
| **3. Control mapping** | `OI-LC-05` → `OI-LC-06` | Map each evidence item to one or more of the seven domains, assign one primary weighted owner, identify control questions, and preserve reference-only uses. | Seven-domain control map with domain coverage, evidence refs, and unknown/blocker register. |
| **4. Findings** | `OI-LC-06` → `OI-LC-07` | Resolve exactly one deterministic finding state per applicable control question; assign confidence, limitations, impact, gate, review state, and ledger references; suppress or supersede only with a reason. | Governed finding register; `ALLOW`, `REVIEW`, or `HALT` per finding and engagement. |
| **5. Prioritization** | `OI-LC-07` → `OI-LC-08` | Use existing impact, evidence strength, effort inverse, and strategic-fit authorities. Keep confidence separate from priority. Route unknowns to validation; identify dependencies and decision urgency without inventing a new formula. | Prioritized recommendation register or validation queue; no package assignment unless a canonical route exists. |
| **6. Recommendation handoff** | `OI-LC-08` → `OI-LC-10` | Deliver bounded recommendations, validation actions, owners, prerequisites, acceptance evidence, exclusions, and next decision. Record the buyer decision separately. | Executive report, handoff package, and DecisionLedger event. No implementation authorization is created. |

### 10.1 Failure handling

When a gate fails, correct the earliest failed control, preserve the failed record, and create a superseding or follow-up DecisionLedger event. Do not repair a downstream finding by hiding an upstream evidence or authority failure. The standard recovery choices are:

- collect or recapture evidence
- narrow scope
- obtain written authority
- assign a reviewer or decision owner
- mark the control `UNKNOWN` or `NOT_APPLICABLE` with rationale
- route to `REVIEW` or `HALT`
- close the assessment without a recommendation when a defensible conclusion is not possible

## 11. Prioritization and recommendation handoff

### 11.1 Existing authority

Prioritization uses the current Operator Intelligence methodology and recommendation controls. The protocol does not add a score, weight, threshold, or formula. Use the existing authorities for:

- impact
- evidence strength
- effort inverse
- strategic fit
- recommendation class
- package eligibility
- roadmap phase
- acceptance criteria

The existing priority formula remains authoritative where applicable. Confidence is a separate evidence gate and never modifies maturity or priority. A high-priority `UNKNOWN` is a validation priority, not an implementation route.

### 11.2 Recommendation classes

Use the current recommendation vocabulary:

- `validation`: obtain evidence or test a control before a stronger conclusion
- `implementation`: a bounded action may be proposed only after all readiness, authority, dependency, and acceptance gates pass; this protocol does not authorize it
- `monitoring`: track a controlled condition or unresolved low-materiality signal
- `defer`: valid work sequenced behind a prerequisite or higher-priority dependency
- `halt`: stop until a control boundary is restored

Each recommendation must include the source finding IDs, evidence IDs, bounded action, business impact, confidence, limitations, priority inputs, scope, exclusions, prerequisites, acceptance evidence, owner, decision authority, review state, and ledger reference. A package is not assigned merely because it exists; if no canonical package fits, record a methodology or validation gap.

### 11.3 Handoff boundary

The assessment ends at an evidence-backed recommendation and buyer decision. Proposal, pricing, onboarding, implementation authorization, runtime enforcement, deployment, monitoring execution, and incident operations are separate decisions or services. The report must state `implementation_authorized: false` unless a separate authority record exists, and this protocol never creates that record.

## 12. Engagement deliverables

An assessment engagement using this protocol may produce the following buyer-facing package:

1. **Assessment brief and control record:** decision, subject, scope, authority, exclusions, owners, version, gate, and evidence snapshot.
2. **Agent/workflow inventory:** in-scope agents, connected systems, data classes, tools, actions, environments, owners, and dependencies.
3. **Evidence register and unknown/blocker register:** admitted, limited, rejected, superseded, unknown, contradictory, and blocked evidence with provenance.
4. **Seven-domain control map:** domain coverage, control questions, evidence refs, finding states, confidence, and route.
5. **Finding register:** deterministic states, observations, interpretations, bounded impact, evidence quality, confidence, limitations, and ledger refs.
6. **Prioritized recommendation register:** validation, implementation-eligible, monitoring, defer, or halt recommendations with canonical priority inputs and acceptance evidence.
7. **Executive report:** decision-oriented summary, domain posture, prioritized findings, recommendations, limitations, and next gate.
8. **DecisionLedger handoff:** material assessment decisions, buyer decision, unresolved risks, and explicit implementation authorization state.

These are engagement outputs, not additional repository artifacts for this directive. This increment creates only `playbooks/agentic-ai-governance-readiness-assessment.md`.

## 13. Acceptance criteria

### 13.1 Protocol acceptance

The protocol is acceptable for governed review when all conditions below are true:

- [ ] The problem, intended buyer, and explicit non-customer are defined.
- [ ] Prerequisites, evidence requirements, evaluator authority, buyer authority, and prohibited actions are explicit.
- [ ] Exactly seven and only seven assessment domains are defined.
- [ ] Each domain has a control question and minimum evidence focus.
- [ ] Every finding requires evidence references, evidence quality, confidence, limitations, unknowns, and a DecisionLedger reference.
- [ ] Finding state resolution is deterministic and uses only `VERIFIED_GAP`, `PARTIAL_CONTROL`, `CONTROLLED`, `UNKNOWN`, or `NOT_APPLICABLE`.
- [ ] `ALLOW`, `REVIEW`, and `HALT` routing is defined separately from finding state.
- [ ] Intake, evidence collection, control mapping, findings, prioritization, and recommendation handoff are sequenced and mapped to existing lifecycle controls.
- [ ] Existing priority authorities are reused without a new scoring formula or schema change.
- [ ] Deliverables, exclusions, failure handling, risks, rollback, and acceptance evidence are stated.
- [ ] A synthetic sample finding and synthetic sample executive recommendation are included.
- [ ] The final report outline is complete.
- [ ] DiffWall, CASA, PromptBP, VIL, and the Governance Harness Toolkit remain independent and optional.
- [ ] No certification, compliance, customer validation, production-readiness, pricing, or outcome claims are made.

### 13.2 Engagement acceptance

An individual buyer assessment is complete only when:

- [ ] the stated decision, subject, scope, authority, exclusions, and owners are recorded
- [ ] the evidence snapshot is frozen and all material sources have admission states
- [ ] each applicable control question has exactly one protocol finding state or an explicit unresolved validation record
- [ ] all seven domains are represented, including `UNKNOWN` or `NOT_APPLICABLE` where evidence or scope requires it
- [ ] finding confidence and report language match the evidence quality and limitations
- [ ] impact and priority inputs are traceable and confidence remains separate
- [ ] every `REVIEW` or `HALT` condition has an owner and next gate
- [ ] recommendations do not exceed verified evidence or bypass dependencies
- [ ] the executive report discloses scope, evidence date, unknowns, limitations, and implementation authorization state
- [ ] the buyer decision and material exceptions are recorded in the DecisionLedger

## 14. Synthetic sample finding

The following is illustrative only. It is not customer evidence, validation, or a claim about any real agent.

```yaml
finding_id: AIGR-F-D3-EXAMPLE-001
assessment_id: AIGR-EXAMPLE-NOT-A-CUSTOMER
domain_id: AIGR-D3
control_question: "Are consequential tools and actions bounded by explicit scopes and human approval rules?"
state: PARTIAL_CONTROL
observation: >
  In the synthetic review scope, an authorized tool manifest permits external
  email sending and appointment creation. A documented approval rule exists for
  appointment creation but no equivalent approval, recipient restriction, or
  action-level audit requirement is evidenced for external email sending.
interpretation: >
  The workflow has a control for one consequential action, but the external
  communication path is not equivalently bounded in the reviewed scope.
business_impact: >
  The agent may be able to produce an externally consequential communication
  without a consistently recorded human checkpoint; the operational effect and
  exposure outside the reviewed scope are not established by this sample.
evidence_refs:
  - EX-EV-001  # synthetic authorized tool manifest
  - EX-EV-002  # synthetic approval-policy excerpt
evidence_classes: [A]
evidence_quality_summary: >
  Direct and attributable review of the synthetic manifest and policy excerpt;
  no production execution log was supplied.
confidence: medium
confidence_basis: >
  The control difference is directly visible in the reviewed artifacts, but
  operational effectiveness and broader deployment scope remain unverified.
assumptions:
  - The synthetic manifest is current for the stated review scope.
limitations:
  - No production execution log or independent safe-test result is included.
unknowns:
  - Whether an undocumented platform-level control blocks the email action.
validation_required:
  - Confirm effective runtime policy and approved-recipient behavior through an authorized safe test or current execution evidence.
contradictory_evidence_refs: []
weighted_owner: AIGR-D3
reference_only_uses:
  - AIGR-D4
control_gate: REVIEW
review_state: validation_required
recommendation_refs:
  - AIGR-REC-EXAMPLE-001
ledger_refs:
  - OI-DL-EXAMPLE-AIGR-001
```

Why this state is deterministic: the synthetic evidence shows a relevant control exists, but a material action-level safeguard is not evidenced. That is `PARTIAL_CONTROL`, not `VERIFIED_GAP`, because the effective platform-level boundary remains an explicit unknown.

## 15. Synthetic sample executive recommendation

**Recommendation:** Before expanding the agent's authority, require an explicit approval and recipient boundary for external email actions, confirm the effective runtime policy through an authorized safe test or current execution evidence, and retain the approval result and action trace for review.

**Decision posture:** `REVIEW`  
**Recommendation class:** `validation`  
**Source:** `AIGR-F-D3-EXAMPLE-001`  
**Confidence:** medium, limited by unavailable runtime evidence  
**Implementation authorized:** `false`

**Executive rationale:** The reviewed artifacts show a control boundary for appointment creation but do not establish an equivalent boundary for external email actions. The next decision is whether the missing control is provided by an effective platform policy or must be defined before the agent's action scope is expanded. This recommendation does not claim customer harm, noncompliance, or production unsafety.

**Acceptance evidence:** approved action policy, recipient restriction, authorized safe-test result or current execution trace, approval/audit event, named owner, and a recorded buyer decision.

## 16. Final report outline

The final buyer-facing report should use the following outline:

1. **Executive decision**
   - assessment question
   - reviewed agent/workflow scope
   - current route: `ALLOW`, `REVIEW`, or `HALT`
   - top verified conditions and immediate decision required
2. **Scope, authority, and limitations**
   - buyer, sponsor, decision authority, evaluator role
   - environments, workflows, systems, data classes, time window
   - exclusions, access limits, testing authority, evidence snapshot date
3. **Agent and workflow inventory**
   - purpose, owners, users, tools, actions, data sources, dependencies, versions
4. **Seven-domain posture**
   - one row for each of `AIGR-D1` through `AIGR-D7`
   - finding state, confidence, evidence coverage, route, and key limitation
5. **Prioritized findings**
   - observation, evidence, interpretation, bounded impact, confidence, state, owner, and ledger ref
6. **Recommendations and next gates**
   - validation, implementation-eligible, monitoring, defer, or halt actions
   - priority inputs, dependencies, acceptance evidence, and decision authority
7. **Buyer decisions and handoff**
   - accepted, rejected, deferred, conditioned, or unresolved decisions
   - implementation authorization remains separate and explicit
8. **Risks, unknowns, and exclusions**
   - unresolved evidence, authority, scope, privacy, safety, operational, and attribution limits
9. **Appendices**
   - evidence register, control map, finding register, recommendation register, DecisionLedger index, terminology, and change/supersession history

The report's publication state must follow the existing publication standard. A completed report is not automatically official, published, or authorized for implementation.

## 17. Cross-project independence and optionality

Operator Intelligence owns this assessment entry point: intake, evidence, domain mapping, findings, confidence, prioritization, report language, and recommendation handoff.

The following systems remain independent optional downstream or supporting systems:

| System | Independent role | Boundary in this protocol |
|---|---|---|
| DiffWall | Code-change and repository risk governance | Optional downstream system for code-governance work; not a dependency, bundled component, or implementation requirement. |
| CASA | Runtime agent governance and controlled action routing | Optional downstream system for runtime enforcement or evaluation; not required to run this assessment and not bundled into it. |
| PromptBP | Instruction and prompt control layer | Supporting independent capability; no runtime coupling or required handoff is created here. |
| VIL | Signal relevance, evidence strength, confidence, priority, and routing support | Supporting independent capability; existing Operator Intelligence methodology remains the assessment authority. |
| Governance Harness Toolkit | Regression and CI validation infrastructure | Independent supporting capability; no workflow, deployment, or repository modification is included in this increment. |

Cross-project references are descriptive only. This protocol creates no imports, APIs, shared permissions, runtime dependencies, deployment links, or bundled commercial claim across those systems.

## 18. Exclusions for this increment and engagement

This documentation increment and the bounded assessment protocol exclude:

- changes to scoring formulas, weights, criteria, or canonical schemas
- runtime implementation, agent execution, tool integration, deployment, or CI changes
- public-site, Pages, wiki, portfolio, or external publication changes
- DiffWall, CASA, PromptBP, VIL, Toolkit, or Governance Harness repository changes
- pricing, duration, binding commercial terms, or package rates
- certification, attestation, regulatory compliance, legal, security, or privacy conclusions
- customer claims, customer data, testimonials, customer validation, or production-readiness claims
- outreach, sales contact, job applications, or external publication
- new repositories, new permissions, secrets, credentials, or spend
- implementation authorization or acceptance of operational risk

## 19. Risks and mitigations

| Risk | Effect | Mitigation and gate |
|---|---|---|
| No external buyer validation | Protocol may be internally coherent but commercially misaligned. | Keep status proposed; obtain separate buyer validation before claiming market fit. `REVIEW`. |
| Existing terminology or schema drift | Findings may not reconcile with current repository controls. | Reuse linked authorities, run internal-link and terminology checks, and reopen methodology review if a conflict is found. `REVIEW` or `HALT`. |
| Incomplete agent inventory | A clean result may cover only a subset of actual agent authority. | Require bounded inclusion rules, owner sign-off, and explicit unknowns. `REVIEW`. |
| Missing or restricted evidence | Unknowns could be misread as verified gaps. | Use `UNKNOWN`, record the owner and next action, and prohibit negative inference. `REVIEW` or `HALT`. |
| Unsafe or unauthorized testing | Testing could change records, expose data, or create customer impact. | Require written authority and safe-test limits; otherwise stop. `HALT`. |
| Finding-state overclaim | Partial or scoped control could be represented as complete governance. | Apply deterministic state order, evidence-quality floor, confidence rules, and executive-language review. `REVIEW`. |
| Assessment-to-implementation slippage | A recommendation could be treated as approval to deploy or expand. | Keep `implementation_authorized: false`; require a separate authority record. `HALT` if bypassed. |
| Cross-project coupling | Assessment independence or commercial boundary could be weakened. | Keep systems optional and descriptive; reject imports, shared permissions, and bundled claims. `HALT`. |
| Unbounded commercial expectation | Buyer may expect price, delivery time, or guaranteed outcomes. | Exclude pricing and guarantees; restate scope and decision at intake. `REVIEW`. |

## 20. Rollback and change control

### 20.1 Repository rollback for this increment

This increment contains one documentation file on an isolated branch. If review identifies a material defect before merge:

1. keep `main` unchanged
2. record the defect in the draft PR or review record
3. update the same isolated branch only when the correction remains within this bounded scope
4. if the scope changes materially, close the draft PR and create a new governed directive or superseding branch
5. do not merge, deploy, publish, or modify another repository as part of rollback

If the file is ever merged and later found materially wrong, preserve the prior version and create a superseding version with a DecisionLedger reference. Do not silently overwrite an approved or published protocol.

### 20.2 Assessment rollback

An assessment run rolls back to the earliest failed gate, not to a fabricated clean state. Preserve evidence and prior decisions; narrow scope, recapture evidence, assign a reviewer, or close the assessment with `REVIEW`/`HALT`. Any material change to a finding, recommendation, route, or report requires supersession and downstream re-review.

## 21. Protocol control record

This record is a proposed use of existing Operator Intelligence control and ledger conventions. It does not change a canonical repository schema in this increment.

```yaml
assessment_id: OI-AIGR-YYYY-NNN
engagement_id: OI-ENG-YYYY-NNN
protocol_version: "0.1"
methodology_version: ""
buyer: ""
decision_authority: ""
agent_scope: ""
scope_version: ""
evidence_snapshot_date: null
domain_ids:
  - AIGR-D1
  - AIGR-D2
  - AIGR-D3
  - AIGR-D4
  - AIGR-D5
  - AIGR-D6
  - AIGR-D7
finding_states:
  VERIFIED_GAP: []
  PARTIAL_CONTROL: []
  CONTROLLED: []
  UNKNOWN: []
  NOT_APPLICABLE: []
open_unknowns: []
open_blockers: []
recommendation_refs: []
publication_state: internal_only|provisional|range_only|blocked
implementation_authorized: false
implementation_authorization_ref: null
control_gate: ALLOW|REVIEW|HALT
review_state: draft|review_required|approved|blocked|superseded|closed
owner: ""
reviewer: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 22. References

Use these existing repository authorities in order of applicability:

- [Assessment Lifecycle](../framework/assessment-lifecycle.md)
- [Lifecycle and Roadmap Map](../framework/lifecycle-roadmap-map.md)
- [Governance Gate Index](../framework/governance-gate-index.md)
- [Assessment Methodology](../docs/methodology.md)
- [Terminology](../docs/terminology.md)
- [Evidence Standard](../standards/evidence-standard.md)
- [Confidence Standard](../standards/confidence-standard.md)
- [Recommendation Standard](../standards/recommendation-standard.md)
- [Publication Standard](../standards/publication-standard.md)
- [DecisionLedger Standard](../standards/decision-ledger-standard.md)
- [Evidence Register](../templates/evidence-register.md)
- [Finding Register](../templates/finding-register.md)
- [Recommendation Register](../templates/recommendation-register.md)
- [DecisionLedger Record](../templates/decision-ledger.md)
- [Executive Report Template](../templates/executive-report.md)
- [Existing AI Readiness Category](../scoring/category-sheets/ai-readiness.md)
- [Unified Governance Platform Representation](../governance-platform/README.md)

These references provide terminology and control alignment only. They do not create runtime coupling, shared permission, or a bundled product dependency.
