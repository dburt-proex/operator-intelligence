# Operator Intelligence Playbook Index

Version: v1.0 commercial playbook registry  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Canonical playbook registry

## 1. Purpose

This index defines the operating and industry playbooks approved for commercial v1.0 delivery.

Playbooks adapt execution and evidence priorities. They do not create alternate scoring systems, finding IDs, packages, phases, publication states, or authorization rules.

## 2. Operating playbooks

| Playbook | Purpose | Primary trigger |
|---|---|---|
| `engagement-delivery-playbook.md` | End-to-end lifecycle workflow | Qualified engagement begins |
| `evidence-validation-playbook.md` | Evidence admission and downstream-use decision | Evidence is collected or changed |
| `finding-to-recommendation-review.md` | Governed finding-to-action, priority, eligibility, route, and phase | Finding is approved for downstream use |
| `publication-quality-review.md` | Pre-publication QC and separate publication decision | Artifact is ready for client release |

## 3. Industry playbooks

| Playbook | Scope | Required base |
|---|---|---|
| `contractor-base.md` | Cross-industry contractor and local-service assessment | Canonical methodology and templates |
| `painting.md` | Residential, commercial, specialty, and maintenance painting | `contractor-base.md` |
| `tree-service.md` | Tree removal, trimming, storm response, stump, clearing, urgent-service controls | `contractor-base.md` |

## 4. Post-v1 engagement profiles

| Profile | Scope | Required base | Authority |
|---|---|---|---|
| `agentic-ai-governance-readiness-assessment.md` | Bounded seven-domain governance-readiness assessment | Canonical evidence, confidence, recommendation, and DecisionLedger standards | Proposed internal-only profile |
| `agentic-control-platform-readiness/` | Vendor-neutral readiness and implementation-preparation sprint for enterprise AI control platforms | Agentic governance protocol plus canonical evidence and decision controls | Approved post-v1 extension |

## 5. Application order

```text
Engagement Delivery
→ Contractor Base
→ Applicable Industry Playbook
→ Evidence Validation
→ Scoring and Finding Resolution
→ Finding-to-Recommendation Review
→ Registered Reports / Roadmap / Proposal
→ Publication Quality Review
→ Client Decision / Onboarding / Delivery
```

## 6. Shared controls

Every playbook preserves:

- evidence admission and public-absence limits
- unknown/blocked handling
- confidence separation
- one weighted owner
- canonical priority inputs
- package eligibility before assignment
- eight canonical packages
- Phase 0 and phases 1–5
- separate QC/publication/proposal/authorization decisions
- completion versus realized-value separation
- DecisionLedger traceability
- executive-safe language

## 7. Extension rules

A new industry playbook must include:

- purpose, version/stage/folder/status
- inputs/triggers and outputs
- buyer intent and high-value services
- service/page/proof/conversion/automation evidence priorities
- scoring nuances
- candidate finding patterns with required evidence
- package and roadmap routing boundaries
- report language
- failure modes and recovery
- acceptance criteria, usage, and commercial v1.0 connection

New playbooks cannot invent findings or packages.

## 8. Commercial v1.0 connection

This registry provides sufficient operating guidance and initial vertical coverage to deliver, review, and demonstrate the commercial assessment system.
