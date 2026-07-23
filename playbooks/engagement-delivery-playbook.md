# Engagement Delivery Playbook

Version: v1.1 post-v1 field-learning extension  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Governed end-to-end engagement workflow

## 1. Purpose

This playbook defines the operating sequence for delivering Operator Intelligence from qualification through assessment, client decision, authorized implementation, completion, realized-value review, monitoring, renewal, and closure.

It does not replace source standards or authorize work. Every lifecycle advancement requires its own evidence, owner, gate, and record.

## 2. Inputs

- qualified opportunity and discovery record
- governed intake, scope, exclusions, and access
- registered templates
- criteria/category sheets and finding libraries
- standards and package registry
- industry playbook
- engagement authorization
- baseline and measurement authority when realized-value review is opened

## 3. Outputs

- complete assessment evidence and score objects
- governed findings/recommendations/routes
- executive and contractor reports
- roadmap and proposal where eligible
- QC/publication/client decision records
- onboarding and implementation authorization when approved
- completion evidence
- realized-value register when measurement is opened
- monitoring, renewal, or closure evidence
- complete DecisionLedger history

## 4. Canonical lifecycle states

| ID | State | Exit evidence |
|---|---|---|
| OI-LC-01 | Qualification | fit gate and next action |
| OI-LC-02 | Intake | scope, authority, access, data controls |
| OI-LC-03 | Surface Mapping | applicable surface/system inventory |
| OI-LC-04 | Evidence Collection | admitted snapshot and gaps |
| OI-LC-05 | Scoring | reproducible score objects/publication state |
| OI-LC-06 | Finding Resolution | governed finding register |
| OI-LC-07 | Risk and Opportunity Synthesis | canonical impact/effort/opportunity decisions |
| OI-LC-08 | Recommendation Routing | priority, eligibility, route, phase |
| OI-LC-09 | Report and Roadmap Build | versioned artifacts ready for QC |
| OI-LC-10 | Delivery and Decision | publication and client decisions |
| OI-LC-11 | Proposal and Onboarding | accepted scope and start prerequisites |
| OI-LC-12 | Implementation | separately authorized work and completion evidence |
| OI-LC-13 | Monitoring and Realized Value | separate baseline, outcome evidence, attribution confidence, and next decision |
| OI-LC-14 | Renewal or Closure | renewed scope or controlled closure |

A downstream artifact cannot cure an upstream failure.

## 5. Stage workflow

### 5.1 Qualification and intake

- establish fit, decision question, owner, authority, scope, exclusions, evidence/access feasibility, data rules, and intended use
- remove unsupported outcome expectations
- issue ALLOW/REVIEW/HALT

### 5.2 Surface mapping and evidence

- inventory public and authorized internal surfaces
- assign evidence IDs and collection plan
- capture provenance, scope, date, integrity, and authorization
- retain contradictions and unknowns
- freeze evidence snapshot

### 5.3 Scoring

- apply canonical criteria/category sheets
- preserve scored/unknown/blocked/not-applicable states
- calculate scores, coverage, confidence index, and bounds
- apply publication gates and duplicate controls

### 5.4 Finding resolution

- validate, split, merge, suppress, block, close, or supersede candidate findings
- preserve observation/evidence/interpretation/impact/confidence/limitations
- assign one primary owner

### 5.5 Risk, opportunity, and recommendation routing

- use canonical impact, evidence strength, effort inverse, strategic fit, and priority
- determine class and package eligibility
- assign one primary package only when eligible
- route validation to Phase 0
- define phases 1–5, owners, dependencies, exclusions, and acceptance evidence

### 5.6 Report and roadmap build

- assemble approved source objects only
- disclose scope, score type, coverage, bounds, unknowns, findings, recommendations, eligibility, route, phases, and authorization state
- generate contractor companion from the same governed records

### 5.7 QC and publication

- run `quality-control-checklist.md`
- correct earliest failed controls
- ledger QC result
- issue separate publication decision

### 5.8 Client delivery and decision

- restate scope/evidence/limitations/publication state
- explain decisions and dependencies
- record validation requests, acceptance, deferral, rejection, monitoring, or closure
- do not change material recommendations live without re-review

### 5.9 Proposal and onboarding

- propose only eligible package scope
- record commercial terms and proposal acceptance
- verify access, authority, prerequisites, testing, rollback, escalation, and owners
- obtain separate implementation authorization

### 5.10 Implementation and completion

- execute only authorized scope
- maintain change control and DecisionLedger events
- test acceptance criteria
- retain completion evidence and defects/exceptions
- record client acceptance/rejection
- do not represent completion as a business outcome

### 5.11 Monitoring and realized-value review

Use `templates/realized-value-register.md` when a stable recommendation, roadmap item, package, completion state, or no-action decision enters outcome measurement.

- define baseline metric, source, owner, period, and evidence refs
- define measurement window and comparison method
- separate implementation adoption from business effects
- record observed direction, confounders, unintended effects, attribution confidence, and limitations
- use the approved ROI framework before any financial assertion
- retain `not_measured` and `insufficient_evidence` without treating either as failure
- record client acceptance, dispute, correction, or unknown state
- prevent the record from changing the original score or silently authorizing more work

### 5.12 Renewal and closure

- decide validate, optimize, maintain, renew, defer, or close
- ensure the decision is supported by the realized-value state and client authority
- revoke access and retain, return, or delete records as required
- transfer open risks and unknowns to named owners
- ledger the final state

## 6. Engagement control record

```yaml
engagement_id: OI-ENG-YYYY-NNN
assessment_id: ""
client: ""
current_lifecycle_state: OI-LC-01|OI-LC-02|OI-LC-03|OI-LC-04|OI-LC-05|OI-LC-06|OI-LC-07|OI-LC-08|OI-LC-09|OI-LC-10|OI-LC-11|OI-LC-12|OI-LC-13|OI-LC-14
scope_version: ""
methodology_version: ""
evidence_snapshot_date: null
score_run_id: null
report_id: null
publication_state: internal_only|official|provisional|range_only|blocked
qc_ref: null
package_scope_refs: []
implementation_authorized: false
authorization_ref: null
completion_evidence_refs: []
realized_value_record_refs: []
realized_value_state: null
measurement_owner: null
measurement_review_date: null
open_unknowns: []
open_blockers: []
owner: ""
decision_authority: ""
review_state: ALLOW|REVIEW|HALT
ledger_ref: OI-DL-YYYY-NNN
```

## 7. Escalation and failure handling

Use REVIEW for bounded evidence, sample, recency, owner, scope, attribution, or exception questions.

Use HALT for missing authority, broken evidence integrity, unreproducible score, unknown-as-zero, unsupported confidence or outcome claims, duplicate ownership, invalid eligibility or route, bypassed phase, uncontrolled AI, missing authorization, unsupported ROI, or broken traceability.

Correct the earliest failed control, supersede material records, and rerun downstream checks.

## 8. Completion checklist

- [ ] Every lifecycle state has exit evidence and owner.
- [ ] Scope, evidence, scoring, findings, and recommendations reproduce.
- [ ] Package eligibility and phases are valid.
- [ ] Registered templates are used.
- [ ] QC, publication, client, proposal, and authorization decisions are separate.
- [ ] Completion and realized value are separate.
- [ ] Realized-value assertions trace to baseline and outcome evidence.
- [ ] Attribution confidence and confounders are explicit.
- [ ] Material changes and decisions are ledgered.
- [ ] Open risks and unknowns transfer to an owner at closure.

## 9. Usage instructions

1. Maintain the engagement control record.
2. Advance one lifecycle state only after its exit gate passes.
3. Use the industry playbook plus contractor base.
4. Use the delivery checklist as the working execution record.
5. Use the Realized Value Register only when the measurement trigger and authority pass.
6. Stop and reopen upstream decisions when evidence or scope changes materially.

## 10. Commercial v1.0 and post-v1 connection

This playbook preserves the complete paid-assessment and governed implementation lifecycle required for commercial-v1 delivery. The post-v1 extension adds a bounded field-learning loop without reopening approved scores, findings, packages, publication states, or authorization rules.

## 11. References

- `framework/assessment-lifecycle.md`
- `framework/lifecycle-roadmap-map.md`
- `framework/roi-framework.md`
- `templates/index.md`
- `templates/delivery-checklist.md`
- `templates/realized-value-register.md`
- `playbooks/publication-quality-review.md`
