# Painting Contractor Playbook

Version: v1.0 commercial industry playbook  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Governed painting-industry assessment playbook

## 1. Purpose

Apply Operator Intelligence to residential, commercial, specialty, and maintenance painting contractors. Use this playbook with `contractor-base.md`; it adds painting-specific buyer intent, evidence, scoring nuances, finding patterns, package routes, roadmap logic, and report language.

## 2. Inputs and triggers

Required inputs:

- verified painting service and service-area inventory
- residential/commercial mix
- project-size, seasonality, and capacity constraints
- estimate and scheduling process
- authentic project proof
- verified prep, product, warranty, cleanup, and crew claims
- governed intake and evidence register

## 3. Buyer intent

| Buyer need | Questions to resolve | High-value public evidence |
|---|---|---|
| Interior refresh | Rooms, occupied-home process, protection, cleanup, timing | Interior examples, process, reviews |
| Exterior protection | Surface condition, prep, products, weather, durability | Before/after, prep details, warranty limits |
| Cabinet refinishing | Finish quality, process, downtime, durability | Cabinet-specific proof and process |
| Commercial work | Scheduling, disruption, safety, documentation, scale | Commercial projects, process, capacity evidence |
| Deck/fence staining | Surface prep, product compatibility, weather window | Service-specific proof and process |
| Repair + paint | Drywall/wood/rot scope and trade boundary | Verified included/excluded repair scope |
| Maintenance | Recurring needs, property portfolio, budget cycle | Maintenance workflow and account ownership |

Do not infer service capability from generic gallery images. Service and project relevance must be verified.

## 4. Service inventory

Common service candidates:

- interior painting
- exterior painting
- cabinet painting/refinishing
- commercial painting
- multi-unit/HOA painting
- deck and fence staining
- drywall repair and painting
- specialty coatings
- industrial coatings
- maintenance programs

Every service requires state, area, buyer type, capacity, estimate method, proof, and claim approval under the base playbook.

## 5. Evidence priorities

### Public evidence

- service-page coverage and specificity
- city/service relevance
- before/after project sets tied to service type
- prep, protection, cleanup, product, color, and scheduling explanations
- reviews mentioning communication, prep, cleanliness, finish, schedule, and issue resolution
- warranty or satisfaction language with verified terms
- estimate form fields and photo-upload path
- team, insurance, credential, and commercial-capability claims
- GBP categories/services/photos and website alignment

### Internal evidence, when authorized

- lead source and requested service
- room/project type, square footage, photos, condition, occupied/vacant state
- estimate status and follow-up
- scheduling and weather delays
- change orders and callbacks
- review-request trigger
- project profitability or close-rate data only when defined and authorized

## 6. Conversion intake model

A painting estimate path may collect:

- service type
- property type
- address/service area
- room count or approximate scope
- interior/exterior/cabinet/commercial selection
- surface condition or known repairs
- desired timing
- occupied/vacant state when material
- photo upload
- preferred contact method

Do not add fields without a decision use. Sensitive or unnecessary data collection is prohibited.

## 7. Minimum evidence by domain

| Domain | Painting-specific minimum |
|---|---|
| Messaging/offer | Priority service, buyer type, area, process/differentiation, CTA |
| Website/SEO | Core service pages, internal links, local relevance, project proof |
| Conversion | Estimate CTA, mobile call/form, service qualification, confirmation/routing |
| Trust | Authentic painting projects, reviews, prep/process, verified claims |
| GBP | Correct categories/services, project photos, area/hours/links |
| Automation | Service-aware intake, ownership, estimate/follow-up stages, exceptions |
| Analytics | Source, service requested, estimate outcome, review flow, page actions |
| Competitive | Comparable painters by service, geography, buyer segment, observation date |

## 8. Common finding patterns

These are candidate patterns only.

| Pattern | Required evidence | Likely finding domain | Normal route |
|---|---|---|---|
| Generic “painting services” architecture | URL/page inventory and service verification | SEO / messaging | `OI-PKG-SEO-001` when eligible |
| Cabinet/commercial/high-priority service lacks proof | Service page + project/proof inventory | Trust / messaging | `OI-PKG-TRUST-001` |
| Prep and cleanup process is not visible | Page copy, reviews, client-confirmed process | Messaging / trust | Trust or Website dependency |
| Estimate form cannot qualify project type | Form/mobile safe test | Conversion | `OI-PKG-WEB-001` |
| Photo intake is absent despite defined use | Intake workflow and owner confirmation | Conversion / automation | Website primary; CRM dependent if internal route is root |
| Estimate follow-up varies by person | CRM/SOP/sample/interview | Automation | `OI-PKG-CRM-001` |
| Review requests are inconsistent after completion | Workflow/system sample | Automation/trust | `OI-PKG-REV-001` |
| No service-level performance view | Metric/source/decision review | Analytics | `OI-PKG-DASH-001` |

## 9. Scoring nuances

- Before/after volume does not establish authenticity, service relevance, or permission.
- Product-brand mentions do not prove correct specification or workmanship.
- Warranty language cannot be scored as strong proof without terms and applicability.
- Exterior service availability may be seasonal; score the verified operating state and evidence window.
- Cabinet painting is a distinct buyer journey when materially offered.
- Commercial capability cannot be inferred from residential projects.
- A “free estimate” CTA does not prove routing, response, or follow-up maturity.
- Photo upload improves intake only when someone reviews it and the workflow defines its use.

## 10. Package routing guidance

| Root condition | Primary package | Common dependency |
|---|---|---|
| Estimate-path friction or weak qualification | `OI-PKG-WEB-001` | CRM if routing/ownership is also undefined |
| Missing verified service architecture | `OI-PKG-SEO-001` | Website for CTA integration |
| Weak painting-specific proof/process | `OI-PKG-TRUST-001` | Website for placement |
| GBP service/photo/profile mismatch | `OI-PKG-GBP-001` | Trust or Review Generation |
| Inconsistent estimate ownership/follow-up | `OI-PKG-CRM-001` | Dashboard for outcome visibility |
| Inconsistent post-job review process | `OI-PKG-REV-001` | CRM trigger and Dashboard monitoring |
| Missing source/service/estimate reporting | `OI-PKG-DASH-001` | CRM/source cleanup |
| AI-assisted intake | `OI-PKG-AI-001` | CRM/workflow prerequisite; all readiness controls |

## 11. Roadmap sequence

- **Phase 0:** verify service scope, areas, proof permissions, warranty/process claims, workflow, baselines, and access.
- **Phase 1:** correct broken/mobile CTA, contact accuracy, form and confirmation friction.
- **Phase 2:** build priority service pages, local relevance, painting-specific proof, GBP alignment, and offer/process clarity.
- **Phase 3:** standardize intake, estimate stages, follow-up, review requests, and service-level reporting.
- **Phase 4:** consider bounded intake assistance only after workflow/data/privacy/review/logging/QA gates pass.
- **Phase 5:** review adoption, service demand, estimate workflow, quality signals, and renewed scope using measured evidence.

## 12. Report language

Approved examples:

- “The site confirms general painting capability, but the reviewed service architecture does not yet distinguish the priority service paths.”
- “Project proof is present, although the reviewed sample does not consistently identify service type, scope, or location.”
- “The estimate form captures contact information but does not yet provide a structured path for the project details the team uses to qualify work.”
- “Internal validation is required before describing warranty, product, response-time, or commercial-capacity claims.”

## 13. Failure modes

| Failure | Control response |
|---|---|
| Generic photo assumed to represent a service | Mark relevance unknown; request source context |
| Warranty or durability claim unverified | REVIEW/HALT publication |
| Repair work assumed included | Clarify trade/scope boundary in Phase 0 |
| Seasonal service treated as always available | Correct service state and date context |
| Commercial scale inferred without evidence | Bound claim or route to validation |
| AI estimator proposed from photos alone | HALT unsupported pricing/decision automation; define human-reviewed use case |

## 14. Acceptance criteria

The painting playbook is correctly applied when:

- priority services, areas, capacity, and claims are verified
- service-relevant proof is mapped
- estimate intake and follow-up are tested or marked unknown
- findings use governed libraries
- routes and phases are proportional
- reports disclose seasonality, proof, warranty, repair, and data limitations
- completion and outcome validation remain separate

## 15. Usage instructions

1. Apply `contractor-base.md` first.
2. Build the painting service and proof inventory.
3. Collect and admit evidence.
4. Apply scoring and finding libraries.
5. Route recommendations through the canonical package catalog.
6. Use registered report and delivery templates.

## 16. Commercial v1.0 connection

This playbook provides the first governed trade-specific assessment variant and demonstrates how Operator Intelligence adapts without creating a separate methodology.

## 17. References

- `playbooks/contractor-base.md`
- `templates/package-catalog.md`
- `framework/findings/`
- `scoring/category-sheets/`