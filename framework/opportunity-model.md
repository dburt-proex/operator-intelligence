# Opportunity Model

Version: v0.3 foundation

The Opportunity Model defines how Operator Intelligence converts findings into prioritized business opportunities.

## Purpose

A finding describes what is happening.

An opportunity defines what value could be created if the finding is addressed.

The opportunity model prevents reports from becoming long lists of disconnected observations.

## Opportunity object

```yaml
opportunity_id: OI-OPP-000
source_findings:
  - OI-FINDING-000
related_criteria:
  - OI-CONV-001
  - OI-CONV-002
category: Conversion
business_outcome: More qualified inquiries
impact_level: High
effort_level: Low
confidence: High
roadmap_phase: Phase 1 — Quick Wins
recommended_package: Website Conversion Fix Pack
```

## Opportunity categories

| Category | Description |
|---|---|
| Visibility | More qualified buyers can find the business. |
| Trust | More buyers feel confident enough to inquire. |
| Conversion | More visitors become leads or estimate requests. |
| Lead Handling | Fewer inquiries are missed, delayed, or forgotten. |
| Follow-Up | More open estimates and prospects receive timely contact. |
| Reputation | More completed work turns into reviews and proof. |
| Retention | More past customers return or refer. |
| Measurement | Leadership can see what is working and what needs action. |
| Automation | Repetitive work becomes more consistent and less owner-dependent. |
| AI Enablement | AI can support defined workflows with controls and review gates. |

## Opportunity scoring

Each opportunity is scored across five dimensions.

| Dimension | Scale | Meaning |
|---|---:|---|
| Impact | 1–5 | Expected business effect if improved. |
| Evidence | 1–5 | Strength of proof supporting the opportunity. |
| Effort | 1–5 | Ease of implementation, where 5 is easiest. |
| Urgency | 1–5 | How quickly the issue should be addressed. |
| Strategic Fit | 1–5 | Alignment with current client goal and roadmap phase. |

Opportunity Score:

```text
Opportunity Score = Impact + Evidence + Effort + Urgency + Strategic Fit
```

| Score | Opportunity level |
|---:|---|
| 21–25 | Priority Opportunity |
| 16–20 | Strong Opportunity |
| 11–15 | Supporting Opportunity |
| 5–10 | Later Opportunity |

## Opportunity routing

| Opportunity pattern | Recommended routing |
|---|---|
| High impact + low effort | Phase 1 quick win |
| High impact + medium effort | Phase 2 foundation build |
| High impact + high effort | Phase 2 or 3 strategic initiative |
| Medium impact + low effort | Bundle into active phase |
| Low impact + high effort | Defer or exclude |
| Low evidence + high impact | Validate before implementation |

## From finding to opportunity

### Step 1 — Identify finding

Example:

The homepage has a weak primary call to action.

### Step 2 — Attach evidence

Example:

Homepage screenshot shows a generic button that does not prompt estimate action.

### Step 3 — Interpret business impact

Example:

Interested buyers may not immediately understand the desired next step.

### Step 4 — Define opportunity

Example:

Improve homepage conversion by replacing passive action language with a clear estimate request path.

### Step 5 — Route to package

Example:

Website Conversion Fix Pack.

## Opportunity quality standard

A valid opportunity must be:

- Evidence-backed
- Business-relevant
- Actionable
- Sequenced
- Connected to a recommendation package
- Written in language a business owner understands

## Anti-patterns

Do not create opportunities that are:

- Purely aesthetic without business impact
- Based on unsupported assumptions
- Too vague to implement
- Not connected to a roadmap phase
- Not connected to a package or owner

## Example opportunity

```yaml
opportunity_id: OI-OPP-001
source_findings:
  - Weak primary CTA
related_criteria:
  - OI-CONV-001
  - OI-CONV-002
category: Conversion
business_outcome: Increase estimate requests
impact: 5
evidence: 5
effort: 4
urgency: 5
strategic_fit: 5
opportunity_score: 24
opportunity_level: Priority Opportunity
recommended_package: Website Conversion Fix Pack
roadmap_phase: Phase 1 — Quick Wins
```

## Governance rule

Do not create an opportunity unless the next action is clear enough to be assigned, estimated, and reviewed later.
