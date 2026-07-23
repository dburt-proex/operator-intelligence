# Agentic Control Platform Readiness Sprint

Version: 0.1.0
Status: Proposed post-v1 engagement profile
Directive: `LD-2026-07-23-SNOW-001`
Implementation authorization: `false`

## Decision

This package defines a vendor-neutral, evidence-backed sprint for deciding whether an organization is prepared to implement or expand an enterprise AI governance and control platform.

It prepares the buyer for a platform decision. It does not select a vendor, certify the organization, attest compliance, deploy controls, or authorize implementation.

## Commercial promise

Convert an incomplete AI estate into:

1. a bounded control baseline;
2. an evidence and unknowns register;
3. a platform-readiness score with separate coverage and confidence;
4. a prioritized remediation roadmap;
5. an executive implementation decision; and
6. a machine-readable handoff package.

## Required artifacts

| Artifact | Purpose |
|---|---|
| `readiness-protocol.md` | Engagement boundary, workflow, gates, roles, and completion evidence |
| `assessment-questionnaire.md` | Buyer and technical discovery questions mapped to the seven canonical domains |
| `evidence-requirements.md` | Minimum evidence, admission rules, handling, and material-finding threshold |
| `control-mapping.md` | Vendor-neutral control map separating change-time, runtime, and governance controls |
| `scoring-profile.md` | Deterministic scoring, coverage, confidence, and decision routing |
| `gap-register.md` | Controlled record for verified gaps, partial controls, unknowns, owners, and gates |
| `prioritized-roadmap.md` | Validation and implementation sequencing with dependencies and acceptance evidence |
| `executive-decision-brief.md` | Buyer-facing decision record |
| `diffwall-demonstration.md` | Bounded proof of enforceable change-time controls |
| `export-schema.json` | Machine-readable handoff contract |

## Authority chain

```text
Agentic governance protocol
→ Sprint scope and authority
→ Evidence admission
→ Seven-domain control mapping
→ Finding state and confidence
→ Readiness score and coverage
→ ALLOW / REVIEW / HALT
→ Roadmap and executive decision
→ Separate implementation authorization
```

Canonical controls remain in:

- `playbooks/agentic-ai-governance-readiness-assessment.md`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/recommendation-standard.md`
- `standards/decision-ledger-standard.md`
- `templates/evidence-register.md`
- `templates/finding-register.md`
- `templates/recommendation-register.md`

## Required completion evidence

The sprint is complete only when:

- scope, decision authority, evaluator authority, and exclusions are recorded;
- every applicable domain has evidence or an explicit unknown/blocked record;
- every material finding resolves to admitted evidence;
- change-time and runtime controls are mapped separately;
- coverage and confidence remain separate from the readiness score;
- every remediation item has an owner, dependency, gate, and acceptance evidence;
- the executive decision and machine-readable export reconcile; and
- implementation authorization remains a separate recorded decision.

## Validation

Run:

```bash
python playbooks/agentic-control-platform-readiness/validate_package.py --self-test
```

The validator checks package completeness, schema validity, domain and weight invariants, evidence requirements, enforcement-plane separation, decision routing, and prohibited certification language.
