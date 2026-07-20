# Northstar Painting Co. — Synthetic Finding Ledger

Version: v1.0 sample finding set  
Stage alignment: Stage 7 — `examples/`  
Status: Synthetic governed findings

## 1. Register control

```yaml
assessment_id: OI-ASSESS-2026-EX001
register_version: "1.0"
methodology_version: commercial-v1.0
evidence_snapshot_date: 2026-07-20
publication_state: provisional
qc_ref: OI-QC-2026-EX001
ledger_ref: OI-DL-2026-EX004
```

## 2. Finding register

| Finding ID | Domain | Observation | Evidence refs | Business impact | Confidence | Severity | State | Package eligibility | Phase | Ledger ref |
|---|---|---|---|---|---|---|---|---|---:|---|
| `OI-FIND-CONV-EX001` | Conversion | Estimate form captures contact details but not the project fields used to qualify painting work | EX003, EX004 | May increase manual clarification and create inconsistent intake context | high | G2 | published | eligible | 1 | EX005 |
| `OI-FIND-SEO-EX001` | SEO | Cabinet painting is promoted as a priority service but has no dedicated service page in the reviewed inventory | EX005, EX006, EX008 | May reduce clarity and discoverability for cabinet-painting intent | high | G2 | published | eligible | 2 | EX006 |
| `OI-FIND-TRUST-EX001` | Trust | Most reviewed project images do not identify service type, location, scope, or result context | EX007, EX010 | Limits the ability of project proof to reduce uncertainty for a specific service | medium | G2 | published | eligible | 2 | EX007 |
| `OI-FIND-AUTO-EX001` | Automation | Lead ownership, required fields, next actions, and follow-up cadence are inconsistent across the limited internal sample | EX011, EX012, EX013 | Creates workflow variability and weak accountability after inquiry | medium | G3 | published | validation_required | 0 | EX008 |
| `OI-FIND-ANALYTICS-EX001` | Analytics | Website activity is observable, but source, service request, estimate status, and job outcome are not reconciled | EX012, EX014 | Limits leadership’s ability to connect activity to operating decisions | medium | G2 | published | validation_required | 0 | EX009 |

No social finding is created. Social evidence is unknown and remains a validation gap rather than a negative condition.

## 3. Finding detail

### `OI-FIND-CONV-EX001` — Estimate intake lacks project qualification

**Observation**  
The tested form requests contact information and an open message but does not capture service type, property type, timing, project scale, surface condition, or photos.

**Interpretation**  
The form provides a working contact path, but it does not consistently collect the project context described in the painting playbook.

**Business impact**  
This may increase manual clarification and reduce consistency before an estimate is scheduled. No lead-loss or conversion-rate amount is claimed.

**Confidence:** high  
**Limitations:** downstream ownership remains blocked; the finding concerns public intake fields only.  
**Weighted owner:** Conversion  
**Reference-only use:** Website

### `OI-FIND-SEO-EX001` — Priority cabinet service lacks a dedicated page

**Observation**  
Cabinet painting appears in homepage offer copy but not as a dedicated page in the reviewed URL inventory.

**Interpretation**  
The current architecture does not provide a focused cabinet-painting path comparable to the other verified core services.

**Business impact**  
This may constrain service-specific buyer clarity and local discoverability. No ranking outcome is claimed.

**Confidence:** high  
**Limitations:** search demand and revenue priority are not quantified.  
**Weighted owner:** SEO  
**Reference-only use:** Messaging and offer

### `OI-FIND-TRUST-EX001` — Project proof lacks service context

**Observation**  
Eleven of eighteen synthetic gallery images lack service type, location, project scope, or outcome context.

**Interpretation**  
The gallery demonstrates activity but only partially supports service-specific trust decisions.

**Business impact**  
Buyers may have less relevant proof when evaluating cabinet, interior, exterior, or commercial work.

**Confidence:** medium  
**Limitations:** asset authenticity and publication permission are assumed in the synthetic fixture.  
**Weighted owner:** Trust  
**Reference-only use:** Messaging

### `OI-FIND-AUTO-EX001` — Lead ownership and follow-up are inconsistent

**Observation**  
The owner reports manual spreadsheet transfer; the synthetic sample records source in 6/10 cases and a next action in 4/10; no approved follow-up cadence exists.

**Interpretation**  
The available evidence supports workflow variability but does not fully map routing, responsibility, exceptions, or SLA behavior.

**Business impact**  
This creates accountability and follow-up consistency risk after inquiry.

**Confidence:** medium  
**Limitations:** limited sample and unverified form-routing owner.  
**Required decision:** Phase 0 workflow validation before package assignment.  
**Weighted owner:** Automation

### `OI-FIND-ANALYTICS-EX001` — Activity and operating outcomes are not reconciled

**Observation**  
Synthetic analytics include sessions and form events, while the lead sample inconsistently records source and next action. No joined source-to-estimate dataset exists.

**Interpretation**  
Website activity can be observed, but it cannot yet be reliably connected to service demand, estimate status, or job outcome.

**Business impact**  
Leadership has limited evidence for source and service-level operating decisions.

**Confidence:** medium  
**Limitations:** no complete CRM or financial dataset.  
**Required decision:** validate source fields, stages, owners, and reconciliation rules before dashboard routing.  
**Weighted owner:** Analytics

## 4. Suppressed and blocked candidates

| Candidate | Treatment | Reason |
|---|---|---|
| “Social presence is weak” | suppressed | Evidence unavailable; unknown is not negative evidence |
| “AI intake should be implemented” | blocked | Privacy, escalation, logging, retention, and QA controls do not pass |
| “The form is losing leads” | suppressed | No admissible lead-loss or conversion evidence |
| “Competitors outperform Northstar” | suppressed | Comparative fixture shows visible features only, not performance |

## 5. Finding release decision

```yaml
validated_findings: 5
published_findings: 5
validation_required_findings: 2
blocked_candidates: 1
suppressed_candidates: 3
review_state: ALLOW
publication_state: provisional
conditions:
  - retain all limitations
  - do not create a social finding
  - do not route AI implementation
```

## 6. Commercial v1.0 connection

This record demonstrates that unknowns, limited internal evidence, duplicate ownership, and unsupported outcome claims are governed before recommendation development.