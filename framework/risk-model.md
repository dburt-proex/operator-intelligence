# Risk Model

Version: v0.3 foundation

The Risk Model defines how Operator Intelligence identifies, scores, and routes growth constraints that may reduce business performance.

## Purpose

Risk is not limited to technical failure.

In Operator Intelligence, risk includes any condition that may reduce visibility, trust, lead capture, follow-up, customer confidence, operational consistency, or management visibility.

## Risk object

```yaml
risk_id: OI-RISK-000
source_finding: OI-FINDING-000
category: Conversion
risk_type: Revenue Leakage
severity: High
likelihood: Medium
evidence_class: A
confidence: High
recommended_response: Fix in Phase 1
```

## Risk categories

| Category | Description |
|---|---|
| Visibility Risk | Buyers cannot find the company for relevant searches. |
| Trust Risk | Buyers do not receive enough proof to feel confident. |
| Conversion Risk | Interested visitors do not become inquiries. |
| Lead Handling Risk | Inquiries are missed, delayed, or poorly routed. |
| Follow-Up Risk | Open opportunities are not consistently pursued. |
| Reputation Risk | Reviews, testimonials, or public proof are weak or unmanaged. |
| Measurement Risk | Leadership cannot see performance clearly. |
| Automation Risk | Manual workflows create inconsistency or lost work. |
| AI Execution Risk | AI could act without sufficient process, data, or review gates. |
| Competitive Risk | Local competitors present stronger signals to buyers. |

## Risk scoring

Risk Score uses three inputs.

| Input | Scale | Meaning |
|---|---:|---|
| Severity | 1–5 | How damaging the issue could be. |
| Likelihood | 1–5 | How likely the issue is to affect performance. |
| Evidence Strength | 1–5 | How well supported the risk is. |

```text
Risk Score = Severity + Likelihood + Evidence Strength
```

| Risk Score | Risk Level |
|---:|---|
| 13–15 | Critical |
| 10–12 | High |
| 7–9 | Medium |
| 3–6 | Low |

## Risk response types

| Response | Use when |
|---|---|
| Fix immediately | Risk blocks leads, trust, contact, or tracking. |
| Reduce | Risk is material but can be improved through roadmap execution. |
| Monitor | Risk is plausible but requires more data. |
| Accept | Risk is low or not worth addressing now. |
| Escalate | Risk affects legal, privacy, safety, customer commitments, or AI boundaries. |

## Risk-to-phase routing

| Risk type | Default phase |
|---|---|
| Broken website contact path | Phase 1 — Quick Wins |
| Weak CTA or phone visibility | Phase 1 — Quick Wins |
| Missing trust proof | Phase 1 or 2 depending severity |
| Missing service pages | Phase 2 — Growth Foundation |
| Weak GBP profile | Phase 2 — Growth Foundation |
| No CRM or lead tracking | Phase 3 — Automation and Reporting |
| No follow-up process | Phase 3 — Automation and Reporting |
| No analytics | Phase 3 — Automation and Reporting |
| AI without review gates | Phase 4 — Governed AI Enablement |

## Risk examples

### Example 1 — Conversion risk

Observation:

Primary CTA is unclear and not estimate-oriented.

Risk:

Interested visitors may fail to take action.

Response:

Fix in Phase 1 through Website Conversion Fix Pack.

### Example 2 — Measurement risk

Observation:

No conversion tracking exists.

Risk:

The owner cannot tell which channels produce inquiries.

Response:

Reduce in Phase 3 through Operator Dashboard Pack.

### Example 3 — AI execution risk

Observation:

Business wants customer-facing AI but has no documented service rules or escalation path.

Risk:

AI may provide inaccurate, unsupported, or overconfident responses.

Response:

Escalate to governed workflow design before deployment.

## Governance rule

A risk should never be exaggerated to force urgency. Severity must match evidence.
