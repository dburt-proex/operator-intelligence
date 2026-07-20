# Northstar Painting Co. — Synthetic Evidence Register

Version: v1.0 sample record  
Stage alignment: Stage 7 — `examples/`  
Status: Synthetic evidence only

## 1. Register control

```yaml
assessment_id: OI-ASSESS-2026-EX001
register_version: "1.0"
methodology_version: commercial-v1.0
evidence_snapshot_date: 2026-07-20
register_owner: Sample Evaluator
reviewer: Sample QC Reviewer
publication_state: provisional
ledger_ref: OI-DL-2026-EX001
```

## 2. Evidence inventory

| Evidence ID | Class | Source / synthetic observation | Scope | Strength | Confidence support | Review state | Primary uses |
|---|---|---|---|---|---|---|---|
| `OI-EV-2026-EX001` | A | Desktop homepage capture shows clear phone and estimate CTA | Homepage | high | high | accepted | Website, conversion |
| `OI-EV-2026-EX002` | A | Mobile safe test confirms phone link works | Mobile homepage | high | high | accepted | Conversion |
| `OI-EV-2026-EX003` | A | Estimate form accepts name, phone, email, and message only; no service/project qualification | Estimate form | high | high | accepted | Conversion, website |
| `OI-EV-2026-EX004` | A | Synthetic test submission displays generic success message; downstream owner cannot be observed publicly | Form confirmation | medium | medium | limited | Conversion, automation |
| `OI-EV-2026-EX005` | A | URL inventory contains interior, exterior, and commercial pages but no cabinet-painting page | Website inventory | high | high | accepted | SEO, messaging |
| `OI-EV-2026-EX006` | A | Homepage promotes cabinet painting as a priority service | Homepage offer copy | high | high | accepted | Messaging, SEO |
| `OI-EV-2026-EX007` | A | Project gallery contains 18 images; 11 lack service type, location, or project context | Gallery sample | medium | medium | accepted | Trust, messaging |
| `OI-EV-2026-EX008` | B | Defined sample of three fictional local painters shows cabinet-service pages on two sites | Competitor sample | medium | medium | accepted | Competitive, SEO |
| `OI-EV-2026-EX009` | A | Synthetic GBP record has accurate name, hours, service area, website link, and painting categories | GBP | high | high | accepted | GBP |
| `OI-EV-2026-EX010` | A | Synthetic review sample contains 42 reviews; recent reviews cite cleanliness and communication | Review sample | medium | medium | accepted | Trust, GBP |
| `OI-EV-2026-EX011` | E | Owner interview states inquiries are copied manually into a spreadsheet | Intake workflow | medium | medium | accepted | Automation |
| `OI-EV-2026-EX012` | E | Ten-record synthetic lead sample shows source recorded in 6/10 and next action in 4/10 | Lead sample | medium | medium | accepted | Automation, analytics |
| `OI-EV-2026-EX013` | E | Owner reports follow-up depends on estimator preference; no approved cadence exists | Follow-up workflow | low | low | limited | Automation |
| `OI-EV-2026-EX014` | E | Synthetic analytics export includes sessions and form events but no reconciled lead/estimate outcomes | Analytics | medium | medium | accepted | Analytics |
| `OI-EV-2026-EX015` | E | AI-readiness interview identifies interest in intake assistance but no approved privacy, escalation, or QA records | AI readiness | low | low | limited | AI readiness |
| `OI-EV-2026-EX016` | A | Social account access and current content sample are unavailable | Social | insufficient | unknown | limited | Social unknown state |
| `OI-EV-2026-EX017` | E | No approved data-retention or AI incident-escalation record supplied | AI controls | insufficient | unknown | limited | AI blocked state |

## 3. Material limitations

- All evidence is synthetic and cannot support real-world claims.
- Internal workflow records are narrow samples.
- Social-channel evidence is unavailable.
- AI privacy, retention, escalation, logging, and QA controls are not established.
- Competitor evidence is a fictional comparative fixture, not market research.

## 4. Unknown and blocked register

| Item ID | Condition | State | Decision effect | Resolution requirement | Gate |
|---|---|---|---|---|---|
| `OI-UNK-2026-EX001` | Social presence cannot be evaluated | unknown | Social category coverage 0%; no negative finding | Obtain authorized profile/content sample | REVIEW |
| `OI-BLK-2026-EX001` | Form-submission ownership and SLA are not verified | blocked | Automation conclusion limited; Phase 0 validation | Inspect routing/system records and test with owner | REVIEW |
| `OI-BLK-2026-EX002` | AI privacy, retention, escalation, logging, and QA controls are incomplete | blocked | AI implementation ineligible | Approve control records and test cases | HALT |

## 5. Duplicate ownership decisions

| Signal | Weighted owner | Reference-only use |
|---|---|---|
| Estimate form field sufficiency | Conversion | Website context |
| Missing cabinet page | SEO | Messaging offer context |
| Project gallery context | Trust | Messaging context |
| Incomplete lead fields | Automation | Analytics dependency |
| AI control gaps | AI readiness | Automation dependency context |

## 6. Admission decision

```yaml
accepted_records: 13
limited_records: 4
rejected_records: 0
superseded_records: 0
review_state: ALLOW
conditions:
  - retain social as unknown
  - retain AI implementation as blocked
  - publish only provisional score and bounded conclusions
ledger_ref: OI-DL-2026-EX002
```

## 7. Usage boundary

These evidence records may support only this synthetic regression example. They do not authorize real-client publication or implementation.