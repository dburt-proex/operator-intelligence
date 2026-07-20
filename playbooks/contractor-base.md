# Contractor and Local-Service Base Playbook

Version: v1.0 commercial playbook foundation  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Canonical cross-industry assessment playbook

## 1. Purpose

This playbook adapts Operator Intelligence to contractor and local-service businesses without changing the canonical methodology, scoring engine, finding libraries, standards, package registry, or roadmap phases.

Use it as the base layer for industry-specific playbooks. Industry files may narrow services, buyer intent, evidence, findings, and routing, but they may not weaken evidence or governance controls.

## 2. Intended actors

- assessment lead
- evidence collector
- scoring reviewer
- client owner/operator
- operations or office manager
- marketing or website owner
- implementation owner
- quality-control reviewer

## 3. Inputs and triggers

Use this playbook when:

- the business sells location-dependent services to homeowners, property managers, commercial buyers, or local institutions
- buyers typically move from search/referral to call, form, estimate, scheduling, and service delivery
- trust, local relevance, speed, proof, and follow-up materially affect the buyer journey
- the engagement requires a repeatable assessment rather than generic marketing advice

Required inputs:

- governed client intake and scope
- verified service and service-area inventory
- public-surface inventory
- authorized internal-system access where available
- evidence register
- applicable scoring criteria
- client decision questions

## 4. Outputs

A completed use produces:

- evidence-backed category scores and publication state
- governed findings and confidence
- priority recommendations
- package eligibility and route
- Phase 0 and phases 1–5 roadmap
- executive and contractor reports
- proposal-ready scope only when eligible
- DecisionLedger and QC records

## 5. Governance rules

1. Client statements are reported evidence until admitted or corroborated.
2. Public absence means not publicly visible within reviewed scope, not internal nonexistence.
3. Unknown and blocked states are not score zero.
4. Service, licensing, insurance, warranty, capacity, response-time, location, and availability claims require verification before publication.
5. Emergency, safety, legal, financial, and regulated-service claims require proportional review.
6. A tool subscription does not prove a workflow works.
7. A package is not recommended because it is sellable.
8. Package eligibility precedes assignment.
9. Phase 0 validation cannot contain implementation authorization.
10. Completion evidence and business-outcome evidence remain separate.

## 6. Contractor buyer-intent model

| Intent state | Typical question | Required public signal | Assessment risk when unclear |
|---|---|---|---|
| Service fit | “Do they do this work?” | Specific service language and examples | Unqualified or lost inquiries |
| Location fit | “Do they serve my property?” | Accurate service area | Friction, false expectations, weak local relevance |
| Urgency fit | “How quickly can they respond?” | Bounded availability/process language | Unsupported promises or abandoned contact |
| Trust | “Are they legitimate and safe?” | Verified reviews, proof, credentials, process | Buyer uncertainty |
| Price/process | “What happens and what affects cost?” | Estimate process and scope factors | Repetitive manual explanation |
| Risk reduction | “Will they protect my property and clean up?” | Process, warranty/policy, proof | Objection and delay |
| Action | “How do I get an estimate?” | Working call/form/booking path | Inquiry leakage risk |
| Follow-up | “Did they receive my request?” | Confirmation, ownership, response expectation | Missed or duplicated inquiries |

Do not assume every industry shares the same urgency, licensing, or price sensitivity. Use the vertical playbook and evidence.

## 7. Service and offer inventory

Create a verified service record for each material service:

```yaml
service_id: OI-SVC-YYYY-NNN
service_name: ""
service_state: active|seasonal|limited|paused|not_offered|unknown
service_area: []
buyer_type: residential|commercial|property_management|public|mixed
urgency: emergency|time_sensitive|planned|mixed
capacity_limitations: []
qualification_requirements: []
estimate_method: on_site|remote|fixed|diagnostic|mixed|unknown
proof_available: []
claim_approval_owner: ""
evidence_refs: []
```

A service page, GBP service, advertisement, or proposal may not claim an unverified service or area.

## 8. Evidence collection priorities

### Public surfaces

- homepage and navigation
- service and location pages
- contact/estimate paths on desktop and mobile
- Google Business Profile and major citations
- reviews and owner responses
- project galleries, case examples, credentials, team, process, FAQ, warranties/policies
- search result appearance and defined competitor sample
- social profiles where applicable

### Internal surfaces, when authorized

- CRM or lead tracker
- call, form, email, SMS, and scheduling records
- estimate stages and outcomes
- follow-up records
- review-request workflow
- analytics and Search Console
- operating SOPs, scripts, policies, credentials, and service records
- automation and AI tools

### Safe tests

- click-to-call and contact-link tests
- form submission and validation
- confirmation and routing tests
- mobile path review
- tracking-event validation
- workflow handoff tests using approved test data

Never create destructive, customer-facing, financial, or safety-impacting test activity without explicit authority.

## 9. Minimum assessment scope

| Domain | Minimum governed scope |
|---|---|
| Website | Homepage, primary service paths, contact path, mobile review |
| Messaging/offer | Primary services, service area, differentiation, process, CTA |
| Conversion | Call, form, confirmation, routing, response expectation |
| SEO | Service architecture, local relevance, metadata, internal linking, indexability sample |
| GBP | Identity, categories, services, hours, area, links, proof, reviews |
| Trust | Reviews, projects, people, credentials, process, policies, local legitimacy |
| Social | Applicable profiles, recency, proof, consistency, action path |
| Automation | Intake, ownership, stages, handoffs, follow-up, exceptions |
| AI readiness | Bounded use case, workflow, data, privacy, review, escalation, logging, QA |
| Analytics | Metrics, sources, definitions, attribution limits, dashboard, decision cadence |
| Competitive | Defined comparable set, service/location relevance, observable differences |

If minimum scope is unavailable, reduce publication state or route to Phase 0.

## 10. Common evidence-backed finding patterns

These are routing prompts, not automatic findings.

| Pattern | Evidence required | Likely finding domain | Common business relevance |
|---|---|---|---|
| Primary service path missing or unclear | URL inventory, page copy, navigation | Website / messaging / SEO | Service-fit ambiguity |
| CTA absent, inconsistent, or broken | Screenshots, mobile test, form/call test | Conversion / website | Inquiry friction |
| Contact request has no confirmed owner | Safe test, CRM/system record, interview | Automation | Response and accountability risk |
| Service area inconsistent | Website/GBP/citation comparison | GBP / SEO / messaging | Local relevance and expectation risk |
| Proof does not support priority services | Page/proof inventory and review sample | Trust / messaging | Buyer uncertainty |
| Follow-up is undocumented or inconsistent | CRM records, SOP, interview, sample | Automation | Lead-handling variability |
| Metrics lack definitions or decision use | Dashboard/export/interview | Analytics | Unreliable management visibility |
| AI use exists without control boundaries | Tool/workflow/policy/log review | AI readiness | Privacy, quality, and accountability risk |

No finding is created until the evidence and finding-library gates pass.

## 11. Scoring nuances

- Do not reward a polished surface that fails the underlying action path.
- Do not score internal workflow maturity from public appearance.
- A missing public credential may affect trust visibility but cannot prove the credential does not exist.
- A CRM subscription does not establish ownership, stage, follow-up, or data quality maturity.
- High review count alone does not establish review recency, relevance, response quality, or process maturity.
- Traffic or ranking data does not establish lead quality or revenue.
- Competitor appearance is comparative evidence only when the set, location, date, and service context are recorded.
- Seasonal or emergency services require applicability and evidence-window care.

## 12. Recommendation and package routing

| Verified root condition | Normal package route | Key prerequisite / boundary |
|---|---|---|
| Buyer-facing action-path friction | `OI-PKG-WEB-001` | Affected path and expected action are known |
| Missing service/local search structure | `OI-PKG-SEO-001` | Service and service area are real and approved |
| Inaccurate or weak GBP | `OI-PKG-GBP-001` | Identity/access/policy-safe facts verified |
| Weak authentic proof | `OI-PKG-TRUST-001` | Proof and claims are authentic and publishable |
| Undefined lead ownership/follow-up | `OI-PKG-CRM-001` | Workflow owner, stages, exceptions, and data rules |
| Inconsistent ethical review process | `OI-PKG-REV-001` | Neutral trigger and escalation path |
| Metrics unobservable or non-actionable | `OI-PKG-DASH-001` | Definitions, sources, owner, cadence, decision use |
| Bounded intake AI use case | `OI-PKG-AI-001` | All AI readiness gates pass |

Unknown, blocked, monitoring, and validation recommendations may remain in Phase 0 with no package.

## 13. Roadmap logic

### Phase 0 — Validation and Access

Resolve identity, service scope, access, data, authority, privacy, credential, workflow, baseline, or control gaps.

### Phase 1 — Quick Wins

Correct verified action-path, accuracy, access, mobile, or critical buyer-friction failures.

### Phase 2 — Growth Foundation

Build verified service architecture, local relevance, trust proof, messaging, GBP, and content foundations.

### Phase 3 — Automation and Reporting

Standardize intake, ownership, stages, handoffs, follow-up, review workflow, metrics, and dashboards.

### Phase 4 — Governed AI Enablement

Add bounded AI assistance only after workflow and control readiness.

### Phase 5 — Optimization and Renewal

Review adoption and measured evidence; decide optimization, maintenance, renewed scope, or closure.

## 14. Report-use rules

Client-facing reports must:

- state reviewed services, areas, systems, and evidence window
- disclose material unavailable internal data
- distinguish observed friction from quantified revenue impact
- use operator-safe language
- show package eligibility rather than forcing every recommendation into a package
- state implementation authorization separately
- avoid ranking, lead, revenue, conversion, savings, or ROI certainty without evidence

## 15. Failure modes and recovery

| Failure mode | Required response |
|---|---|
| Service or location claim cannot be verified | REVIEW/HALT publication; route to validation |
| Live test lacks authorization | Do not test; mark blocked |
| Internal workflow inferred from public surfaces | Remove inference; request internal evidence |
| Duplicate signal affects several domains | Assign one weighted owner; reference elsewhere |
| Package chosen before root condition | Reopen recommendation and routing review |
| Client requests unsupported outcome guarantee | Bound claims; REVIEW commercial fit |
| AI implementation requested before readiness | HALT dependent Phase 4 work |
| Evidence changes after report release | Supersede evidence, affected decisions, QC, and report |

## 16. Acceptance criteria

This playbook is correctly applied when:

- scope and service inventory are verified
- minimum evidence or publication limitations are recorded
- category scoring follows canonical sheets
- findings map to governed libraries
- recommendations use canonical priority and eligibility logic
- roadmap phases respect dependencies
- reports disclose evidence boundaries
- all material decisions are ledgered and reviewed

## 17. Usage instructions

1. Start with governed intake.
2. Complete the service/area inventory.
3. Apply this base across all domains.
4. Add the applicable industry playbook.
5. Record any conflict as a methodology gap; do not silently override canonical controls.
6. Use registered templates for outputs.

## 18. Commercial v1.0 connection

This playbook establishes the reusable contractor assessment layer required for consistent cross-industry delivery and provides the base for painting and tree-service variants.

## 19. References

- `templates/index.md`
- `framework/findings/`
- `scoring/category-sheets/`
- `standards/completion-status.md`
- `templates/package-catalog.md`
- `playbooks/painting.md`
- `playbooks/tree-service.md`