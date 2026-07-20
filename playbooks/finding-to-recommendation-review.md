# Finding-to-Recommendation Review Playbook

Version: v1.0 commercial operating playbook  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Governed evidence-to-action workflow

## 1. Purpose

Use this playbook to convert a governed finding into a bounded recommendation, priority decision, package-eligibility state, package route, roadmap placement, and acceptance plan without overstating evidence or selling work before it is justified.

## 2. Inputs

- validated or blocked Finding Register entry
- supporting and contradictory evidence
- criterion/category and score treatment
- canonical impact, effort, and opportunity authorities
- recommendation and package standards
- package catalog and roadmap standard
- DecisionLedger

## 3. Outputs

- recommendation class and status
- observation, interpretation, impact, confidence, and limitations
- canonical priority inputs and score
- package eligibility
- one primary package only when eligible
- Phase 0 or phases 1–5 placement
- acceptance criteria/evidence
- ALLOW/REVIEW/HALT and ledger refs

## 4. Review sequence

### 4.1 Confirm finding state

Proceed only when finding identity, evidence, confidence, ownership, limitations, review state, and downstream-use status resolve.

A candidate, unsupported, contradictory, or unauthorized finding cannot support implementation.

### 4.2 Define the verified root condition

State:

- what is observed
- where and when it occurs
- evidence and limits
- affected criterion/control
- business relevance
- remaining unknowns

Do not convert public absence, reported claims, or missing access into verified failure.

### 4.3 Select recommendation class

- `implementation`: controlled action can resolve a verified condition.
- `validation`: evidence, access, authority, or control gap must be resolved first.
- `monitoring`: condition is accepted but requires measured review.
- `defer`: valid action is intentionally delayed.
- `halt`: proceeding violates a material boundary.

Reject generic best practice, duplicate, commercially preferred, out-of-scope, or unsupported actions.

### 4.4 Bound the action

Define action, system/workflow, owner, included/excluded scope, prerequisites, dependencies, risks, acceptance criteria, evidence, and authorization boundary.

### 4.5 Calculate priority

Use:

```text
Priority Score = ((Impact × 0.40) + (Evidence Strength × 0.20) + (Effort Inverse × 0.15) + (Strategic Fit × 0.25)) × 20
```

Import inputs from canonical framework authorities. Confidence is a separate gate and does not modify priority. Priority cannot bypass prerequisites.

### 4.6 Determine package eligibility

| State | Meaning |
|---|---|
| `eligible` | Verified implementation/deferred action can be owned by a canonical package |
| `validation_required` | Missing evidence/access/control prevents package assignment |
| `blocked` | Material boundary prevents routing or implementation |
| `not_applicable` | Recommendation does not require package implementation |

Validation, monitoring, halt, and blocked recommendations may have no primary package.

### 4.7 Route eligible work

When eligible:

1. select exactly one canonical primary package owning the root condition
2. list prerequisite/dependent/reference-only packages separately
3. prevent duplicate deliverables and billing
4. select only evidence-justified catalog scope
5. record exclusions and routing reason

No package fit means methodology/validation gap, not an invented package.

### 4.8 Place on roadmap

- Phase 0: validation/access only; no implementation authorization
- Phase 1: verified quick-win correction
- Phase 2: growth foundation
- Phase 3: automation/reporting
- Phase 4: governed AI after all controls pass
- Phase 5: evidence-backed optimization/renewal/closure

### 4.9 Define acceptance and measurement

Completion evidence proves authorized scope. Realized-value evidence requires separate baselines, sources, windows, and decision review.

### 4.10 Control language and authority

Recommendation language must distinguish fact, interpretation, action, purpose, and unverified outcome. Publication, roadmap approval, proposal acceptance, and implementation authorization remain separate.

## 5. Decision gates

- `ALLOW`: finding-specific, evidence-bounded, priority-valid, eligibility-valid, dependency-compliant, measurable, and traceable.
- `REVIEW`: bounded judgment is required for scope, priority, eligibility, package ownership, phase, or acceptance evidence.
- `HALT`: unsupported finding/action, unknown-as-failure, scope excess, invalid route, bypassed dependency, uncontrolled AI, unsupported claim, or broken traceability.

## 6. Decision record

```yaml
recommendation_id: OI-REC-YYYY-NNN
recommendation_class: implementation|validation|monitoring|defer|halt
finding_refs: []
evidence_refs: []
confidence: high|medium|low|unknown
impact_score: 1-5
evidence_strength_score: 1-5
effort_inverse: 1-5
strategic_fit_score: 1-5
priority_score: 0-100
package_eligibility: eligible|validation_required|blocked|not_applicable
primary_package_id: null
dependent_package_ids: []
roadmap_phase: 0|1|2|3|4|5
implementation_authorized: false
acceptance_criteria: []
acceptance_evidence: []
review_state: ALLOW|REVIEW|HALT
ledger_refs: []
```

## 7. Completion checklist

- [ ] Finding is governed and resolvable.
- [ ] Root condition is narrow and supported.
- [ ] Recommendation class is correct.
- [ ] Priority inputs reproduce.
- [ ] Confidence remains separate.
- [ ] Package eligibility is explicit.
- [ ] Exactly one primary package exists only when eligible.
- [ ] Phase 0 and phases 1–5 are valid.
- [ ] Acceptance and realized value remain separate.
- [ ] Authority boundaries and ledger refs are complete.

## 8. Commercial v1.0 connection

This playbook makes recommendation development repeatable while protecting the system from package-first selling, duplicate ownership, and unsupported scope.

## 9. References

- `templates/finding-register.md`
- `templates/recommendation-register.md`
- `templates/package-catalog.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`