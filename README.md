# Operator Intelligence™

## Governed Business Growth Systems Assessment

**Current repository state:** Commercial v1.0 content complete and release-gated  
**Primary market:** Contractor and local-service businesses  
**Method:** Evidence → Score → Finding → Recommendation → Package → Roadmap → Decision → Controlled implementation

Operator Intelligence is a repeatable consulting-product system for evaluating how a contractor or local-service business converts market attention into qualified inquiries, estimates, booked work, customer proof, and operational learning.

It is not a generic website audit or a package catalog disguised as diagnosis. The repository defines the methodology, evidence rules, scoring engine, finding libraries, recommendation logic, implementation packages, client templates, delivery playbooks, sample engagement, research protocols, visual specifications, and release controls required to run a governed assessment.

## Product objective

A second qualified evaluator using the same evidence should be able to reach materially similar scores, findings, and recommendations while preserving uncertainty, review states, and audit history.

Every material recommendation must trace:

```text
Evidence
→ Criterion evaluation
→ Category and Operator Score
→ Governed finding
→ Risk / impact / opportunity interpretation
→ Recommendation priority
→ Package eligibility and routing
→ Phase 0 or phases 1–5
→ Report / proposal decision
→ Separate implementation authorization
→ Completion evidence
→ Monitoring / realized-value evidence
→ Renewal or closure
→ DecisionLedger
```

## Commercial v1.0 inventory

| Layer | Commercial v1.0 state |
|---|---|
| Finding libraries | 11 domain libraries; 217 registered finding patterns |
| Scoring | 140 unique criteria across 11 weighted categories |
| Framework | Finding/recommendation indexes, risk, effort, opportunity, ROI, lifecycle, and gate models |
| Standards | 9 reconciled control standards |
| Templates | 15 registered commercial engagement artifacts |
| Playbooks | 4 operating playbooks and 3 initial contractor-industry playbooks |
| Examples | 1 complete 10-artifact fictional painting-contractor engagement |
| Research | 4 governed support-research protocols |
| Assets | 6 production visual and brand specifications |
| Root/docs | Commercial usage, methodology, roadmap, changelog, and release gate |

## Assessment domains

- Website structure and UX
- Messaging and offer clarity
- Conversion infrastructure
- Local SEO
- Google Business Profile
- Reputation and trust
- Social presence
- Automation maturity
- AI readiness
- Analytics and reporting
- Competitive position

The weighted `messaging_offer` category combines messaging and offer criteria for scoring while preserving separate finding domains for diagnosis and routing.

## Operator Score controls

The scoring engine preserves:

- score anchors of 0, 25, 50, 75, and 100
- explicit `scored`, `unknown`, `blocked`, and `not_applicable` criterion states
- active category weights totaling 100%
- evidence coverage separate from observed performance
- confidence separate from maturity and priority
- category and Operator Score bounds
- official, provisional, range-only, blocked, and internal-only publication states
- duplicate-signal ownership controls
- immutable score objects and supersession

**Unknown is never zero.** A blocked result is uncertainty plus a governance condition, not an automatic failure score.

## Governance model

### Control gates

- `ALLOW` — the bounded action or artifact may advance to the next separate governed decision
- `REVIEW` — qualified judgment, validation, correction, or accepted limitation is required
- `HALT` — evidence, authority, safety, privacy, scope, dependency, publication, or traceability prevents advancement

### Non-negotiable boundaries

- Confidence never modifies performance or priority.
- Package eligibility precedes package assignment.
- Exactly one primary package is required only for eligible implementation work.
- Phase 0 is validation and access, not implementation.
- QC, publication, roadmap approval, proposal acceptance, and implementation authorization are separate decisions.
- Completion evidence and realized-value evidence are separate.
- Unsupported ROI, revenue, lead, ranking, conversion, savings, market-share, competitor-performance, and timeline certainty are prohibited.
- Approved and published records are superseded, never silently overwritten.

## Canonical implementation packages

| Package ID | Canonical name |
|---|---|
| `OI-PKG-WEB-001` | Website Conversion Fix Pack |
| `OI-PKG-SEO-001` | Local SEO Expansion Pack |
| `OI-PKG-GBP-001` | Google Business Authority Pack |
| `OI-PKG-TRUST-001` | Trust Proof System |
| `OI-PKG-CRM-001` | CRM and Follow-Up System |
| `OI-PKG-REV-001` | Review Generation System |
| `OI-PKG-DASH-001` | Operator Dashboard Pack |
| `OI-PKG-AI-001` | Governed AI Intake Assistant |

Packages are delivery containers, not automatic recommendations. The root condition, evidence, score weakness, impact, confidence, priority, dependencies, and phase must justify the route.

## Repository architecture

```text
operator-intelligence/
├── methodology/            # Product method and assessment foundations
├── framework/              # Findings, routing, risk, effort, opportunity, ROI, lifecycle, gates
│   └── findings/           # 11 governed domain finding libraries
├── scoring/                # Criteria, weights, category sheets, calculator, objects, fixtures, completion gate
├── standards/              # Evidence, confidence, recommendation, package, roadmap, publication, ledger, AI, QC
├── templates/              # Intake, evidence, findings, reports, roadmap, proposal, onboarding, delivery, QC
├── playbooks/              # Operating workflows and contractor/painting/tree-service variants
├── examples/               # Complete fictional sample engagement
├── research/               # Market, competitor, conversion, and SEO research protocols
├── assets/                 # Design, score, report, roadmap, diagram, and brand specifications
├── docs/                   # Methodology and commercial operating documentation
├── governance-platform/    # Supporting architecture representation
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
└── COMMERCIAL_V1_COMPLETION.md
```

## How to run an assessment

1. Qualify the business and intended decision.
2. Complete discovery and governed intake.
3. Define scope, exclusions, access, data rules, and testing authority.
4. Map public and authorized internal surfaces.
5. Capture and admit evidence.
6. Score applicable criteria and categories.
7. Resolve candidate findings.
8. Apply risk, impact, opportunity, effort, confidence, and priority logic.
9. Determine package eligibility and route only eligible work.
10. Build the Phase 0 and phases 1–5 roadmap.
11. Assemble the executive and contractor reports.
12. Run quality control and issue a separate publication decision.
13. Record client decisions.
14. Propose only bounded eligible scope.
15. Complete onboarding and obtain separate implementation authorization.
16. Validate completion, monitor realized value separately, and renew or close.

See `docs/commercial-v1-usage.md` for the detailed operating sequence.

## Templates and records

The canonical template registry is `templates/index.md`. It includes:

- sales notes and discovery
- client intake
- evidence, finding, recommendation, and DecisionLedger records
- executive and contractor reports
- roadmap and package catalog
- proposal
- onboarding and delivery checklists
- quality-control checklist

Do not create alternate client records that change controlled IDs, states, packages, phases, or authorization boundaries without reopening the template gate.

## Initial playbooks

- `playbooks/contractor-base.md`
- `playbooks/painting.md`
- `playbooks/tree-service.md`
- `playbooks/engagement-delivery-playbook.md`
- `playbooks/evidence-validation-playbook.md`
- `playbooks/finding-to-recommendation-review.md`
- `playbooks/publication-quality-review.md`

## Sample engagement

`examples/sample-painting-contractor/` contains the fictional Northstar Painting Co. regression example:

- provisional indicator: 50
- uncertainty range: 34–67
- weighted evidence coverage: 86.5%
- Operator confidence index: 0.779
- social state: unknown, with no invented social finding
- AI package route: HALT
- implementation authorized: false

The example is synthetic and must never be represented as evidence about a real business.

## System primitives

- **DiffWall / CASA** — gates, boundaries, escalation, review states, auditability
- **VIL** — signal relevance, evidence strength, confidence, priority, and routing
- **PromptBP** — role, objective, inputs, constraints, output contract, rules, recursive checks
- **DecisionLedger** — immutable evidence-to-decision traceability and supersession
- **Operator Score** — category reliability, coverage, confidence, uncertainty, and publication usefulness

## Release status

The repository content has passed folder gates for:

- framework
- scoring
- standards
- templates
- playbooks
- examples
- research
- assets
- root/docs reconciliation

See `COMMERCIAL_V1_COMPLETION.md` for the final release decision, known boundaries, and post-v1 backlog.

## License and commercial use

Repository ownership, licensing, client confidentiality, trademark use, and distribution terms must be defined and applied before public commercial distribution. The methodology does not grant permission to use client or third-party data, marks, credentials, testimonials, or confidential records.