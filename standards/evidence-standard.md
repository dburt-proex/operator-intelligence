# Evidence Standard

Version: v0.1 governance foundation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Draft foundation for commercial v1.0

## 1. Purpose

This standard defines what qualifies as admissible evidence in an Operator Intelligence assessment.

It governs how evidence is captured, identified, dated, attributed, tested, stored, referenced, limited, and connected to scores, findings, recommendations, packages, roadmap phases, and DecisionLedger records.

No score, finding, or recommendation may rely on evidence that cannot be traced to a specific source record.

## 2. Evidence principles

1. Evidence must be observable, attributable, relevant, and reviewable.
2. Public absence may establish that a signal is not publicly visible, but not that the underlying internal capability does not exist.
3. Missing access is `unknown` or `blocked`, not score `0`.
4. Client statements are valid evidence when identified as interview evidence and assigned appropriate confidence.
5. A software subscription, badge, claim, or vendor grade is not proof that a process works.
6. Live tests require authorization and must avoid creating operational, privacy, customer, or financial harm.
7. Evidence strength and maturity score are separate.
8. One evidence record may support multiple criteria only when each use is explicitly referenced and duplicate scoring is prevented.
9. Screenshots and exports must retain enough context to show what was observed, where, and when.
10. Derived conclusions must remain distinguishable from direct observations.

## 3. Evidence record schema

Every retained evidence item must include:

```yaml
evidence_id: OI-EV-YYYY-NNN
assessment_id: ""
captured_at: "YYYY-MM-DDThh:mm:ssZ"
captured_by: ""
source_type: screenshot|url|document|export|system_record|safe_test|interview|observation|third_party
source_location: ""
source_owner: public|client|evaluator|third_party
scope: ""
observation: ""
criterion_ids: []
finding_ids: []
confidence_support: high|medium|low|unknown
limitations: []
authorization_ref: null
storage_ref: ""
integrity_ref: null
review_state: accepted|limited|rejected|superseded
reviewed_by: ""
```

Required fields may not be omitted. Use `null` only where the field is structurally inapplicable.

## 4. Evidence types

| Type | Appropriate use | Minimum requirement |
|---|---|---|
| Screenshot | Visible page, profile, setting, workflow, or interface state | Date, source location, visible context, evidence ID |
| URL | Publicly accessible page or profile | Exact URL, access date, page purpose |
| Document | Policy, SOP, credential, report, contract, or approved record | Title, owner, version/date, relevant section |
| Export | CRM, analytics, review, campaign, or pipeline data | Date range, system, field definitions, export date |
| System record | Lead, task, estimate, customer, or workflow record | Record sample, system, date, field context |
| Safe test | Form, notification, tracking, routing, or confirmation validation | Authorization, test method, expected result, actual result |
| Interview | Owner or staff statement about internal operations | Speaker role, date, question scope, material limitations |
| Observation | Evaluator review not requiring a retained source file | Date, surface reviewed, method, bounded wording |
| Third-party | Directory, search result, platform, registry, or competitor surface | Source, date, relevance, known limitations |

## 5. Admissibility gate

Evidence is admissible only when all applicable conditions pass.

| Gate | Pass requirement | Failure treatment |
|---|---|---|
| Identity | Unique evidence ID exists | Reject until assigned |
| Attribution | Source and owner are known | Mark limited or reject |
| Recency | Capture date and relevant time period are known | Mark stale or limited |
| Relevance | Evidence directly supports the criterion or finding | Reject unrelated use |
| Scope | Reviewed surface, sample, or date range is defined | Limit assertion strength |
| Integrity | Evidence is complete enough to review and not materially altered | Reject or recapture |
| Authorization | Required access or testing permission exists | Mark blocked; do not test |
| Traceability | Criterion, finding, and ledger references can be resolved | Block publication use |
| Limitation | Material gaps are explicitly recorded | Downgrade confidence or publication state |

## 6. Evidence strength

### High-strength evidence

- direct system access
- authorized safe test with documented result
- complete current records across required scope
- attributable review, project, credential, policy, or workflow evidence
- independently verifiable public records
- approved source-of-truth documents

### Medium-strength evidence

- multiple consistent screenshots
- partial exports or representative records
- corroborated client interview
- public evidence with one material internal validation gap
- dated competitor or search observations with controlled scope

### Low-strength evidence

- single screenshots without broader sampling
- uncorroborated interview statements
- stale captures
- incomplete records
- indirect observations
- third-party summaries without underlying data

### Insufficient evidence

- unsupported assumptions
- vendor marketing claims
- tool-presence claims without configured use
- aesthetic preference
- fabricated or altered records
- anonymous statements without role or context
- missing access interpreted as failure

Evidence strength informs confidence. It does not mechanically determine the maturity anchor.

## 7. Minimum evidence rules

Each scored criterion requires at least one admissible evidence record.

A category score additionally requires completion of the minimum evaluation scope defined in its category sheet.

A finding requires:

- at least one direct evidence record
- an observation
- an interpretation
- a business-impact statement
- a confidence assignment
- criterion mapping
- a DecisionLedger reference

A recommendation requires all finding requirements plus:

- priority
- primary package or approved action path
- roadmap phase
- prerequisite and dependency review

Unknown or blocked criteria require a limitation or access record, not fabricated evidence.

## 8. Sample and time-period controls

The evaluator must define the sample used for any statement covering multiple records or events.

Examples:

- review sample count and date span
- lead-record count and pipeline period
- analytics date range
- competitor set and search location
- page inventory reviewed
- workflow-run sample and failure period

Do not generalize beyond the inspected sample.

Use dated language when conditions may change:

> At the time of review, the tested form displayed a confirmation screen but automated email acknowledgement was not verified.

Do not write:

> The form always works.

## 9. Safe testing standard

Before any live or production-adjacent test, document:

1. test objective
2. authorization source
3. systems affected
4. data used
5. expected outcome
6. rollback or cleanup requirement
7. escalation owner

Prohibited without explicit authorization:

- submitting false customer information into production systems
- triggering customer-facing messages
- changing settings
- creating bookings, estimates, transactions, reviews, or public posts
- using sensitive personal or business data outside approved systems
- testing destructive, irreversible, or financially consequential paths

When a safe test cannot be performed, mark the criterion `blocked` or `unknown` and identify the validation required.

## 10. Public absence and internal unknowns

Public evidence may support statements such as:

> No warranty statement was visible on the tested homepage, service pages, or contact page.

Public evidence alone may not support:

> The company has no warranty.

Internal conditions require internal evidence or bounded interview evidence.

Where access is missing:

```yaml
criterion_state: unknown
score: null
confidence: unknown
validation_required: "Review approved internal source or obtain client confirmation."
```

## 11. Supersession and conflicts

When evidence conflicts:

1. retain both records
2. identify the conflict
3. prefer the authoritative and current source
4. downgrade confidence when authority cannot be resolved
5. mark superseded evidence rather than deleting it
6. record the decision in the DecisionLedger when material

No evidence item may be silently replaced after it has supported a published result.

## 12. Duplicate-use control

Before using one evidence record across categories, identify the distinct condition each category owns.

Example:

- a form screenshot may support Conversion for visible friction
- a safe routing test may support Automation for notification reliability
- an event-debug record may support Analytics for conversion tracking

The same observed weakness may not receive multiple weighted scores under different labels.

## 13. Client-safe evidence language

Use:

- `observed`
- `verified`
- `not visible on tested surfaces`
- `not confirmed`
- `appears inconsistent across the reviewed sample`
- `validation required`
- `may reduce reliability`

Avoid without direct proof:

- `always`
- `never`
- `broken everywhere`
- `losing leads`
- `losing revenue`
- `causing poor conversion`
- `competitors are outperforming`
- `guaranteed improvement`

## 14. Publication controls

Evidence-related publication is:

- `official` when minimum scope, admissibility, coverage, confidence, and traceability requirements pass
- `provisional` when findings are defensible but material verification remains incomplete
- `range_only` when unknowns could materially change score interpretation
- `blocked` when authorization, integrity, privacy, access, or traceability failures prevent defensible publication

A polished report does not override an evidence failure.

## 15. DecisionLedger connection

Every reported finding must resolve to:

```text
Evidence ID
→ Criterion ID
→ Observation
→ Interpretation
→ Business impact
→ Confidence
→ Priority
→ Finding ID
→ Package
→ Roadmap phase
→ DecisionLedger ID
```

Broken links block final-report inclusion.

## 16. Validation codes

### Blocking errors

- `EVID-ID-001`: evidence record lacks a unique ID
- `EVID-SRC-001`: source cannot be attributed
- `EVID-SCOPE-001`: evidence scope is undefined
- `EVID-AUTH-001`: required authorization is absent
- `EVID-TRACE-001`: evidence cannot be traced to criterion or ledger record
- `EVID-INTEG-001`: evidence integrity is materially uncertain
- `EVID-DUP-001`: evidence is being used to duplicate a weighted signal

### Warnings

- `EVID-STALE-001`: evidence may no longer represent current state
- `EVID-SAMPLE-001`: sample is too narrow for the assertion
- `EVID-INT-001`: result depends materially on interview evidence
- `EVID-LIMIT-001`: material limitation is not reflected in confidence or publication state
- `EVID-SUP-001`: newer evidence supersedes the cited record

## 17. Completion checklist

Before evidence is accepted, confirm:

- unique evidence ID assigned
- source, owner, date, and location recorded
- observation separated from interpretation
- scope and sample defined
- authorization documented where required
- limitations recorded
- criterion and finding mappings valid
- confidence support assigned
- duplicate-use check passed
- storage reference resolves
- DecisionLedger traceability exists for reported findings
- client language does not exceed the evidence

## 18. v1.0 connection

This standard creates the evidence discipline required for reproducible scoring, defensible findings, controlled recommendations, reliable publication states, and auditable commercial delivery under Operator Intelligence v1.0.