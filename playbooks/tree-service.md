# Tree Service Contractor Playbook

Version: v1.0 commercial industry playbook  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Governed tree-service assessment playbook

## 1. Purpose

Apply Operator Intelligence to tree removal, trimming, storm response, stump grinding, lot clearing, and related tree-service contractors. Use with `contractor-base.md`; this file adds urgency, safety, property-protection, intake, evidence, routing, and reporting controls.

This is not an arboricultural, insurance, utility, emergency-response, or legal standard. Technical and safety claims require qualified client evidence and appropriate authority.

## 2. Inputs and triggers

Required inputs:

- verified service and service-area inventory
- emergency/after-hours operating state
- insurance, credential, equipment, safety, and crew claims
- dispatch/intake and escalation workflow
- photo/address/hazard intake process
- estimate/site-review process
- governed scope and evidence register

## 3. Buyer intent and risk state

| Intent | Typical condition | Required signal | Governance concern |
|---|---|---|---|
| Emergency/storm | Immediate obstruction or property risk | Accurate contact and response process | Do not promise response or safety outcomes without evidence |
| Hazard concern | Dead/leaning/damaged tree | Qualified assessment path | Website/AI must not make unsupported hazard decisions |
| Planned removal | Space, property, construction, maintenance | Scope/process/equipment/proof | Clear estimate and site-review path |
| Trimming | Clearance, health, appearance, prevention | Service boundaries and proof | Do not imply qualifications not verified |
| Stump grinding | Access, size, utilities, cleanup | Scope factors and exclusions | Underground/utility and restoration boundaries |
| Lot clearing | Scale, access, disposal, equipment | Capacity and commercial proof | Environmental/permit/scope dependencies |

## 4. Service inventory

Common candidates:

- tree removal
- emergency tree service
- storm-damage cleanup
- tree trimming/pruning
- stump grinding/removal
- lot/land clearing
- crane-assisted removal
- commercial/property-management tree service
- debris hauling/chipping where actually offered

Record whether each service is active, emergency, seasonal, limited, subcontracted, paused, or unknown.

## 5. High-priority evidence

### Public evidence

- exact emergency availability and contact language
- service and service-area coverage
- click-to-call behavior on mobile
- tree/photo/address intake path
- safety/process/equipment/team statements
- authentic before/after and complex-project proof
- cleanup and property-protection expectations
- insurance/credential claims with verification status
- GBP categories/services/hours/photos/links
- reviews mentioning safety, communication, cleanup, timeliness, and property protection

### Internal evidence, when authorized

- call/form intake fields
- urgency and hazard escalation rules
- site-visit and dispatch ownership
- missed-call handling
- estimate stages and follow-up
- weather/storm surge exceptions
- job completion and review trigger
- incident, complaint, or callback process
- source/service/estimate/job metrics

## 6. Controlled intake model

A tree-service intake may require:

- contact and service address
- service requested
- urgency state
- photos
- tree location and access context
- visible nearby structures, vehicles, utilities, roadways, or obstructions
- storm/insurance context as reported
- preferred contact method

Controls:

- Intake data supports routing; it does not replace a qualified site or safety assessment.
- An AI or form must not diagnose hazard, guarantee safety, set binding price, or direct emergency action beyond approved escalation language.
- Customer-reported hazard information remains reported evidence.

## 7. Minimum evidence by domain

| Domain | Tree-service minimum |
|---|---|
| Website | Emergency and planned-service paths, mobile call, service pages, contact accuracy |
| Messaging | Service/urgency boundaries, process, area, property-protection and cleanup language |
| Conversion | Click-to-call, form/photo/address, confirmation, urgency escalation, routing |
| SEO | Removal, emergency, trimming, stump, storm, clearing architecture as applicable |
| GBP | Identity, service categories, hours/availability, services, photos, reviews, links |
| Trust | Verified insurance/credentials, safety process, crew/equipment/project proof |
| Automation | Intake, urgency, dispatch/site review, ownership, estimate/follow-up, exceptions |
| Analytics | Source, service, urgency, estimate/job outcome, missed calls, review process |
| AI readiness | Bounded triage assistance only, human review, escalation, privacy, logs, QA |

## 8. Common finding patterns

| Pattern | Required evidence | Domain | Normal route |
|---|---|---|---|
| Emergency claim lacks defined contact/response path | Page copy, mobile call test, interview/SOP | Messaging / conversion | Website primary; CRM dependent |
| Click-to-call or form fails on mobile | Safe test/screenshots | Conversion | `OI-PKG-WEB-001` |
| Hazard/photo intake has no owner or escalation | Workflow/system/interview/test | Automation | `OI-PKG-CRM-001` |
| Safety/insurance/equipment claims are unverified or invisible | Documents + public surfaces | Trust | Validation or `OI-PKG-TRUST-001` |
| Core service pages are missing | Verified service inventory + URL review | SEO | `OI-PKG-SEO-001` |
| GBP hours/services conflict with actual response state | Profile + approved operating record | GBP | `OI-PKG-GBP-001` |
| Missed calls and estimates are not tracked | Call/CRM/workflow evidence | Automation/analytics | CRM primary; Dashboard dependent |
| Review process lacks neutral trigger/escalation | Workflow records | Trust/automation | `OI-PKG-REV-001` |

## 9. Scoring nuances

- “24/7,” emergency, immediate, fast, insured, certified, safe, or crane-capable claims require direct evidence and scoped language.
- Equipment photos do not prove ownership, availability, capacity, qualification, or safe use.
- Public absence of insurance proof does not prove uninsured status; it affects visibility and routes to validation.
- Review count does not establish emergency response, safety performance, or cleanup quality.
- Storm periods may distort normal operating data; evidence windows must be stated.
- Photo intake is not mature unless routing, ownership, escalation, and privacy are defined.
- Hazard decisions and binding estimates remain human-controlled unless an independently approved system permits otherwise.

## 10. Package routing guidance

| Root condition | Primary package | Boundary |
|---|---|---|
| Emergency/mobile action path is unclear or broken | `OI-PKG-WEB-001` | Do not promise response time |
| Missing removal/storm/stump/trimming service structure | `OI-PKG-SEO-001` | Verify services/areas/capacity |
| GBP services/hours/links are inaccurate | `OI-PKG-GBP-001` | Verify operating state and policy compliance |
| Safety/process/project proof is weak | `OI-PKG-TRUST-001` | Authenticate every claim/asset |
| Urgency routing, missed calls, ownership, or follow-up are undefined | `OI-PKG-CRM-001` | Define human escalation and exceptions |
| Review request/response process is inconsistent | `OI-PKG-REV-001` | Neutral trigger; service-recovery path |
| Lead/urgency/estimate/job visibility is absent | `OI-PKG-DASH-001` | Metric/source/owner/decision definitions |
| AI-supported intake or triage | `OI-PKG-AI-001` | Never autonomous hazard/pricing; all controls pass |

## 11. Roadmap sequence

- **Phase 0:** verify service/emergency state, claims, credentials, access, intake fields, escalation, safety boundaries, and data authority.
- **Phase 1:** fix contact accuracy, mobile click-to-call, urgent/planned path clarity, form failures, and confirmation/routing defects.
- **Phase 2:** build service/local structure, GBP alignment, authentic safety/process/equipment/project proof, and bounded expectations.
- **Phase 3:** standardize urgency intake, ownership, missed-call response, estimate follow-up, review workflow, and dashboards.
- **Phase 4:** deploy only bounded, human-reviewed AI intake assistance after readiness gates.
- **Phase 5:** review adoption and measured operational evidence; optimize, renew, maintain, or close.

## 12. Executive-safe report language

- “The reviewed public surfaces provide a contact path, but the emergency and planned-service paths are not yet clearly separated.”
- “Insurance and safety statements were not publicly visible within the reviewed scope; internal status requires validation.”
- “The current intake captures contact details, although urgency ownership and escalation were not verified.”
- “Photo intake may improve context for human review, but it should not be represented as a hazard assessment or binding estimate.”

## 13. Failure modes

| Failure | Required response |
|---|---|
| Emergency response promise cannot be verified | Remove/limit claim; REVIEW/HALT publication |
| Safety, insurance, credential, or equipment claim unsupported | Route to Phase 0; do not publish as fact |
| Live emergency test would affect operations | Do not test; use approved records/interviews |
| AI triage implies hazard decision | HALT; redesign as bounded human-reviewed intake |
| Storm-period data generalized to normal operations | Limit evidence window and conclusion |
| Utility/permit/insurance advice implied | Remove; route to qualified authority |

## 14. Acceptance criteria

The tree-service playbook is correctly applied when:

- service, area, emergency, capacity, and claim states are verified or explicitly unknown
- urgent and planned buyer paths are safely reviewed
- safety and proof claims remain evidence-bound
- intake/dispatch/follow-up maturity is supported internally or marked unknown
- package routes preserve human control and phase order
- reports avoid hazard, response-time, safety, price, insurance, or outcome certainty

## 15. Usage instructions

1. Apply `contractor-base.md`.
2. Verify the service/emergency/claim inventory.
3. Collect public and authorized internal evidence.
4. Apply category sheets and finding libraries.
5. Route through canonical packages and phases.
6. Run QC before publication or authorization.

## 16. Commercial v1.0 connection

This playbook supplies a governed urgent-service vertical with stronger safety, escalation, and AI boundaries than the general contractor model.

## 17. References

- `playbooks/contractor-base.md`
- `templates/package-catalog.md`
- `standards/ai-readiness-standard.md`
- `framework/findings/`
- `scoring/category-sheets/`