# Recommendation Map

Version: v0.3 foundation

This document converts weak scoring signals into recommended implementation paths.

It sits between the criteria library and the client roadmap.

## Purpose

The criteria library identifies what is weak. The recommendation map defines what to do next.

A recommendation is valid only when it includes:

1. Observation
2. Evidence
3. Interpretation
4. Business impact
5. Confidence
6. Priority
7. Implementation path
8. Roadmap phase

## Recommendation routing gates

Every finding must pass these gates before entering a client report.

| Gate | Requirement | Fail condition |
|---|---|---|
| Evidence Gate | Evidence class is documented. | Finding is opinion-only. |
| Confidence Gate | Confidence level is assigned. | Finding overstates certainty. |
| Impact Gate | Business impact is stated. | Finding is cosmetic only. |
| Priority Gate | Urgency is justified. | Finding is not sequenced. |
| Implementation Gate | Recommended action is realistic. | Action is vague or not executable. |
| Roadmap Gate | Phase is assigned. | Client cannot see what happens next. |

## Priority formula

Priority is assigned using four inputs:

| Input | Scale | Meaning |
|---|---:|---|
| Impact | 1–5 | Business effect if fixed. |
| Evidence strength | 1–5 | Quality of proof supporting the finding. |
| Effort inverse | 1–5 | Higher score means easier to implement. |
| Strategic fit | 1–5 | Alignment with current phase and client goal. |

Recommended priority score:

```text
Priority Score = Impact + Evidence Strength + Effort Inverse + Strategic Fit
```

| Priority Score | Priority |
|---:|---|
| 17–20 | Critical |
| 13–16 | High |
| 9–12 | Medium |
| 4–8 | Low |

## Roadmap phase routing

| Finding type | Default phase |
|---|---|
| Broken contact path | Phase 1 — Quick Wins |
| Weak primary CTA | Phase 1 — Quick Wins |
| Missing phone visibility | Phase 1 — Quick Wins |
| Weak hero messaging | Phase 1 — Quick Wins |
| Missing review proof near CTA | Phase 1 — Quick Wins |
| Missing service pages | Phase 2 — Growth Foundation |
| Weak local SEO structure | Phase 2 — Growth Foundation |
| Underused Google Business Profile | Phase 2 — Growth Foundation |
| Weak project proof library | Phase 2 — Growth Foundation |
| No CRM or lead tracker | Phase 3 — Automation and Reporting |
| No follow-up system | Phase 3 — Automation and Reporting |
| No review request system | Phase 3 — Automation and Reporting |
| No analytics or conversion tracking | Phase 3 — Automation and Reporting |
| AI use case without workflow control | Phase 4 — Governed AI Enablement |
| Customer-facing AI without review gates | Phase 4 — Governed AI Enablement |

## Implementation packages

### 1. Website Conversion Fix Pack

Use when the client has a website but the buyer journey is unclear, passive, or hard to act on.

Mapped criteria:

- OI-WEB-001
- OI-WEB-005
- OI-WEB-006
- OI-CONV-001
- OI-CONV-002
- OI-CONV-003
- OI-CONV-006
- OI-CONV-007
- OI-CONV-011

Deliverables:

- Homepage hero rewrite
- Primary CTA rewrite
- Mobile phone path improvement
- Service-page CTA placement
- Contact page improvement
- Trust proof placement near action areas
- Form confirmation language

Default phase: Phase 1 — Quick Wins

### 2. Local SEO Expansion Pack

Use when the client has weak service-page coverage or poor local relevance.

Mapped criteria:

- OI-SEO-001
- OI-SEO-002
- OI-SEO-003
- OI-SEO-004
- OI-SEO-005
- OI-SEO-007
- OI-SEO-008
- OI-SEO-014

Deliverables:

- Service-page inventory
- Keyword-to-page map
- Priority service landing pages
- Local relevance sections
- FAQ expansion
- Internal linking plan
- Metadata rewrite

Default phase: Phase 2 — Growth Foundation

### 3. Google Business Authority Pack

Use when the business has a GBP but it is incomplete, underused, or weaker than competitors.

Mapped criteria:

- OI-GBP-002
- OI-GBP-003
- OI-GBP-004
- OI-GBP-005
- OI-GBP-006
- OI-GBP-007
- OI-GBP-008
- OI-GBP-009
- OI-GBP-010
- OI-GBP-011
- OI-GBP-012

Deliverables:

- Category review
- Service list cleanup
- Business description rewrite
- Photo upload plan
- Review response standard
- Q&A seed list
- Monthly update cadence
- Website-to-GBP alignment check

Default phase: Phase 2 — Growth Foundation

### 4. Trust Proof System

Use when the business lacks proof strong enough to reduce buyer hesitation.

Mapped criteria:

- OI-TRUST-001
- OI-TRUST-002
- OI-TRUST-003
- OI-TRUST-004
- OI-TRUST-005
- OI-TRUST-006
- OI-TRUST-007
- OI-TRUST-008
- OI-TRUST-010
- OI-TRUST-012

Deliverables:

- Review highlight sections
- Project gallery structure
- Before-and-after proof format
- Team or owner credibility section
- Credential and risk-reduction copy
- Process explanation
- Local proof placement

Default phase: Phase 2 — Growth Foundation

### 5. CRM and Follow-Up System

Use when leads are scattered, manually handled, or inconsistently followed up.

Mapped criteria:

- OI-AUTO-001
- OI-AUTO-002
- OI-AUTO-003
- OI-AUTO-004
- OI-AUTO-005
- OI-AUTO-006
- OI-AUTO-007
- OI-AUTO-009
- OI-AUTO-010
- OI-AUTO-013

Deliverables:

- Lead tracker or CRM setup
- Pipeline stages
- Inquiry routing
- Owner assignment rule
- Follow-up reminders
- Estimate status tracking
- Lost reason fields
- Response templates

Default phase: Phase 3 — Automation and Reporting

### 6. Review Generation System

Use when reputation is strong but not systematized, or weak relative to competitors.

Mapped criteria:

- OI-GBP-007
- OI-GBP-008
- OI-GBP-009
- OI-TRUST-001
- OI-TRUST-002
- OI-AUTO-008
- OI-AN-007

Deliverables:

- Review request timing rule
- Review request message templates
- Review response standard
- Review tracker
- Testimonial capture process
- Monthly review velocity report

Default phase: Phase 3 — Automation and Reporting

### 7. Operator Dashboard Pack

Use when the owner cannot see lead flow, source performance, estimate outcomes, or review growth.

Mapped criteria:

- OI-AN-001
- OI-AN-002
- OI-AN-003
- OI-AN-004
- OI-AN-005
- OI-AN-006
- OI-AN-008
- OI-AN-009
- OI-AN-010
- OI-AUTO-014

Deliverables:

- Analytics verification
- Search Console setup
- Conversion event list
- Lead source fields
- Estimate outcome tracking
- Monthly dashboard
- Decision review cadence

Default phase: Phase 3 — Automation and Reporting

### 8. Governed AI Intake Assistant

Use only when process clarity, data hygiene, and review gates are strong enough for controlled AI assistance.

Mapped criteria:

- OI-AI-001
- OI-AI-002
- OI-AI-003
- OI-AI-004
- OI-AI-005
- OI-AI-006
- OI-AI-007
- OI-AI-008
- OI-AI-009
- OI-AI-010
- OI-AI-011
- OI-AI-012

Deliverables:

- Approved AI use-case list
- Intake assistant scope
- Knowledge base
- PromptBP instruction block
- Human review gates
- Escalation rules
- AI output log
- Monthly QA review

Default phase: Phase 4 — Governed AI Enablement

## Final recommendation object

Use this object inside reports, ledgers, and future software implementations.

```yaml
recommendation_id: OI-REC-000
finding_id: OI-FINDING-000
package: Website Conversion Fix Pack
criteria_triggered:
  - OI-CONV-001
  - OI-CONV-002
evidence_class: A
confidence: High
business_impact: Conversion
impact_score: 5
evidence_strength: 5
effort_inverse: 4
strategic_fit: 5
priority_score: 19
priority: Critical
roadmap_phase: Phase 1 — Quick Wins
implementation_owner: Operator Intelligence
status: Proposed
```

## Governance rule

Do not recommend implementation packages only because they are sellable.

Recommend packages only when the evidence, score weakness, business impact, and phase alignment justify the work.
