# Operator Intelligence Discovery Form

Version: v0.1 commercial v1.0 form  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Pre-intake qualification and discovery template

## 1. Purpose

Use this form before governed client intake to collect business context, decision needs, system visibility, access expectations, urgency, and fit signals.

Responses are client-reported context, not verified evidence. This form does not authorize testing, scoring, publication, or implementation.

## 2. Contact and business profile

- Business name:
- Contact name / role:
- Email / phone:
- Website:
- Primary location:
- Service area:
- Years operating:
- Team size / operating structure:
- Primary services:
- Highest-value or highest-priority services:
- Seasonal, emergency, or capacity constraints:

## 3. Current business decision

- What decision should this assessment help you make?
- What changed or triggered the assessment now?
- What would a useful assessment deliverable enable?
- Who will approve recommendations, budget, and implementation?
- Is there a required decision date? Why?
- What is explicitly out of scope?

## 4. Buyer journey and offer

- How do prospects usually discover the business?
- What action should a qualified prospect take?
- Which offers or services create the most confusion?
- Where do prospects commonly hesitate, drop out, or require manual explanation?
- What claims, guarantees, credentials, warranties, or service areas require verification?

## 5. Channels and systems

Mark each state: `used`, `not used`, `unknown`, `access available`, `access blocked`.

| Surface / system | State | Owner | Primary purpose | Known concern |
|---|---|---|---|---|
| Website / CMS | | | | |
| Google Business Profile | | | | |
| Analytics / Search Console | | | | |
| CRM / lead tracker | | | | |
| Scheduling / estimating | | | | |
| Email / SMS / phone | | | | |
| Review platform | | | | |
| Social channels | | | | |
| Automation platform | | | | |
| AI tools / agents | | | | |

## 6. Evidence and access expectations

- Which internal records could be shared?
- Which systems can be reviewed with least-privilege access?
- Are analytics, lead, estimate, sales, review, or call records available?
- Are screenshots/exports preferred over account access?
- Are any systems, data, locations, or staff interviews unavailable?
- Are there privacy, confidentiality, legal, security, or customer-impact restrictions?
- Who can authorize bounded tests?

## 7. Current concerns

Rate each: `not a concern`, `possible`, `known`, `urgent`, `unknown`.

| Domain | State | Client-reported context |
|---|---|---|
| Website / mobile experience | | |
| Messaging / offer clarity | | |
| Conversion / inquiry path | | |
| Local SEO | | |
| Google Business Profile | | |
| Reviews / trust proof | | |
| Social presence | | |
| Lead handling / follow-up | | |
| Automation / workflow | | |
| AI readiness / governance | | |
| Analytics / reporting | | |
| Competitive position | | |

## 8. Implementation context

- Internal implementation capacity:
- Existing vendors or agency relationships:
- Preferred delivery model:
- Budget authority and decision process:
- Tool constraints or required platforms:
- Change-management or training needs:
- Work that must not be automated:
- Known safety, privacy, compliance, or reputation boundaries:

## 9. Qualification gate

```yaml
fit_state: qualified|conditional|not_qualified|more_information_required
assessment_use_clear: false
decision_authority_identified: false
minimum_scope_available: false
evidence_access_plausible: false
material_conflicts: []
material_blockers: []
next_action: governed_intake|clarify_scope|decline|refer|defer
owner: ""
```

## 10. Handoff to governed intake

Transfer only relevant discovery context into `templates/client-intake.md`. Mark all client claims as reported until admitted through the evidence standard.

## 11. Commercial v1.0 connection

This form creates a repeatable front door for qualifying assessment fit and preparing a controlled intake without treating sales discovery as evidence.