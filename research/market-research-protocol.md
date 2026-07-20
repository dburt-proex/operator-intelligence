# Market Research Protocol

Version: v1.0 commercial research support  
Stage alignment: Stage 8 — `research/`  
Folder alignment: `research/`  
Status: Governed support protocol; not a market-claim library

## 1. Purpose

Define how market context may support Operator Intelligence qualification, service prioritization, opportunity interpretation, and report context without replacing direct client evidence or creating unsupported TAM, demand, revenue, or growth claims.

## 2. Allowed uses

- establish service and buyer context
- identify seasonality or operating constraints for validation
- support strategic-fit review
- define a bounded research question
- provide report context when scope, date, geography, and source limitations are explicit

Market research cannot independently create a negative client finding, score, package route, or ROI claim.

## 3. Source hierarchy

1. authoritative public datasets and agencies
2. official industry associations and standards bodies
3. primary company or platform documentation
4. transparent research firms with methodology
5. reputable trade publications
6. client records and interviews, admitted under the evidence standard
7. secondary commentary, used only as contextual or validation-required evidence

## 4. Research object

```yaml
research_id: OI-RES-MKT-YYYY-NNN
question: ""
geography: ""
industry_or_service: ""
buyer_segment: ""
represented_period: ""
source_refs: []
method: ""
observation: ""
interpretation: ""
confidence: high|medium|low|unknown
limitations: []
client_decision_supported: ""
prohibited_uses: []
review_state: ALLOW|REVIEW|HALT
ledger_ref: null
```

## 5. Required controls

- use current-enough sources for the decision
- distinguish national, regional, and local data
- disclose sample, method, period, and definition differences
- do not translate industry averages into a client baseline
- do not infer demand from keyword volume alone
- do not use generic market growth to justify package scope
- preserve conflicting sources
- mark missing or noncomparable data unknown

## 6. Claim rules

Approved:

- “The cited source reports [bounded observation] for [period/geography/definition].”
- “This provides context but does not establish the client’s demand, capacity, or revenue.”

Prohibited without client-specific evidence:

- market share
- addressable revenue
- expected lead volume
- close rate
- pricing power
- growth rate applied to the client
- ROI or payback

## 7. Research workflow

1. Define the client decision and required market question.
2. Fix geography, service, buyer segment, and period.
3. Collect primary/authoritative sources first.
4. Record definitions, methodology, and limitations.
5. Reconcile conflicts or route to REVIEW.
6. State observation separately from interpretation.
7. Link only to decisions the research can support.
8. Retain source snapshots or resolvable references.

## 8. Failure handling

| Failure | Response |
|---|---|
| Source lacks methodology or date | Limit or reject |
| National data used as local fact | REVIEW and relabel as context |
| Industry average used as client baseline | HALT claim |
| Market claim used to force package scope | Reopen recommendation/routing |
| Conflicting material sources | Preserve and REVIEW |
| Source becomes stale | Revalidate or supersede |

## 9. Commercial v1.0 connection

This protocol allows credible market context while protecting the assessment from speculative demand, revenue, and ROI claims.

## 10. References

- `standards/evidence-standard.md`
- `framework/opportunity-model.md`
- `framework/roi-framework.md`