# Competitor Research Protocol

Version: v1.0 commercial research support  
Stage alignment: Stage 8 — `research/`  
Folder alignment: `research/`  
Status: Governed comparative-observation protocol

## 1. Purpose

Define how competitor and peer evidence may support comparative scoring, positioning analysis, service architecture review, and validation without making unsupported claims about competitor performance, revenue, market share, quality, or customer outcomes.

## 2. Comparable-set contract

A competitor set must record:

```yaml
research_id: OI-RES-COMP-YYYY-NNN
client_service: ""
geography: ""
buyer_segment: ""
observation_date: YYYY-MM-DD
selection_method: ""
competitor_sample:
  - entity_label: ""
    comparison_basis: ""
    public_surface_refs: []
excluded_entities: []
limitations: []
review_state: ALLOW|REVIEW|HALT
```

Entities are comparable only when service, geography, buyer segment, and reviewed surface are sufficiently aligned.

## 3. Permitted evidence

- public websites and service/location pages
- Google Business Profile and public listings
- public reviews and response patterns
- public social profiles
- observable contact paths and public offers
- public documentation, case studies, policies, or credentials
- authorized client-provided competitor research

Public observations do not reveal internal workflow, profitability, capacity, close rate, quality, or strategy.

## 4. Comparison dimensions

| Dimension | Observable question |
|---|---|
| Service architecture | Which verified services have dedicated public paths? |
| Local relevance | How explicitly are real areas and local proof represented? |
| Conversion | What public action paths are visible and functional? |
| Trust | What authentic proof types are publicly visible? |
| GBP | Which public profile fields and activity are observable? |
| Messaging | How are service, buyer, process, and differentiation expressed? |
| Content | What buyer questions and service contexts are publicly covered? |
| Consistency | Do public identity, services, areas, and links align? |

## 5. Claim boundaries

Allowed:

- “Two of the three reviewed comparable sites had a dedicated page for the verified service as of the observation date.”
- “The client’s reviewed public path contains less service-specific proof than the defined sample.”

Prohibited:

- “Competitors are winning more business.”
- “The client is losing market share.”
- “The competitor converts better.”
- “The competitor ranks because of this feature.”
- quality, revenue, staffing, capacity, profitability, or performance claims without direct admissible evidence

## 6. Scoring and finding use

- Comparative evidence is Class B and must document the set and date.
- It may support a criterion only when that criterion permits comparative evidence.
- The client condition still requires direct client evidence.
- Competitor appearance alone cannot create a client implementation recommendation.
- One comparison signal has one weighted owner.
- Narrow samples lower confidence and must remain visible.

## 7. Workflow

1. Define the service, geography, buyer segment, and decision.
2. Select the comparable set using an explicit method.
3. Capture equivalent surfaces on the same observation date where practical.
4. Record only observable facts.
5. Normalize definitions and note exclusions.
6. Separate client evidence from competitor evidence.
7. State limitations and confidence.
8. Admit the evidence through the register and DecisionLedger when material.

## 8. Failure handling

| Failure | Response |
|---|---|
| Competitors selected for appearance rather than comparability | Rebuild sample |
| Search position treated as stable performance | Remove claim |
| Internal condition inferred from public surface | HALT claim |
| Client weakness derived only from competitor feature | Require client evidence |
| Material sample conflict | REVIEW |
| Observation becomes stale | Recapture or supersede |

## 9. Commercial v1.0 connection

This protocol provides repeatable competitive context while preventing appearance-based performance claims and package-first recommendations.

## 10. References

- `standards/evidence-standard.md`
- `scoring/category-sheets/competitive.md`
- `framework/findings/competitive-findings.md`