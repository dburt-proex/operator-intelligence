# SEO Research Protocol

Version: v1.0 commercial research support  
Stage alignment: Stage 8 — `research/`  
Folder alignment: `research/`  
Status: Governed SEO source and claim protocol

## 1. Purpose

Define how search, local SEO, technical SEO, and content research may support Operator Intelligence criteria, findings, validation, page architecture, and acceptance tests without creating unsupported ranking, traffic, lead, market-share, or revenue claims.

## 2. Allowed uses

- verify current search-engine or platform requirements
- support a defined technical or content evaluation expectation
- identify service and local-intent coverage questions
- design bounded indexing, metadata, linking, or page acceptance checks
- interpret authorized Search Console or analytics evidence

SEO research cannot independently establish business priority, service legitimacy, capacity, ranking causation, or ROI.

## 3. Source hierarchy

1. official search-engine documentation and platform policies
2. primary technical standards and protocol documentation
3. client Search Console, analytics, CMS, server, and URL data admitted under the evidence standard
4. transparent experiments or studies with reproducible method
5. reputable technical research publications
6. tool-provider metrics and estimates, treated as modeled/contextual data
7. commentary or anecdote, validation-only

## 4. Research object

```yaml
research_id: OI-RES-SEO-YYYY-NNN
question: ""
seo_domain: crawl|index|render|metadata|content|internal_linking|local_relevance|service_architecture|structured_data|search_performance|other
source_refs: []
platform_or_system: ""
geography: ""
service_intent: ""
represented_period: ""
observation: ""
interpretation: ""
client_applicability: direct|partial|context_only|unknown
confidence: high|medium|low|unknown
limitations: []
allowed_use: criterion_support|finding_context|validation|acceptance_test|monitoring
review_state: ALLOW|REVIEW|HALT
```

## 5. Client evidence required

SEO findings normally require direct evidence such as:

- verified service and service-area inventory
- URL and template inventory
- page content and metadata
- crawl/indexability/rendering checks
- internal-link map
- Search Console or analytics records
- GBP and citation identity
- comparable-set evidence when the criterion permits it

Keyword tools, search-result snapshots, and estimated volume are contextual and cannot replace verified service/buyer relevance.

## 6. Claim boundaries

Approved:

- “The reviewed page is blocked from indexing under the observed configuration.”
- “The verified priority service has no dedicated page in the reviewed architecture.”
- “Search Console data for the stated period shows [bounded observation].”

Prohibited without admissible causal and outcome evidence:

- guaranteed rankings
- expected traffic uplift
- lead or revenue forecasts
- “Google penalty” without verified basis
- market-share conclusions
- competitor performance inferred from rank or appearance
- location/service claims the business cannot support

## 7. Search-result and tool-data controls

- record query, location context, device, date, personalization limits, and sample method
- treat result positions as time-bound observations
- identify modeled metrics and tool definitions
- do not merge tool estimates as independent corroboration when they share underlying data
- preserve zero/no-data as unknown unless the source definition supports another conclusion

## 8. Workflow

1. Define the client service, geography, buyer intent, and decision.
2. Verify the service and area before research.
3. Collect official requirements and direct client evidence.
4. Record technical method, date, source, and limitations.
5. Separate observation from causal interpretation.
6. Use tool estimates only as contextual evidence.
7. Define an observable acceptance test.
8. Monitor outcomes separately from implementation completion.

## 9. Failure handling

| Failure | Response |
|---|---|
| Unverified service/location used for page recommendation | HALT route |
| Ranking snapshot treated as stable outcome | Limit/reject |
| Tool volume used as demand or revenue | Remove claim |
| Technical issue claimed without reproducible test | Validate first |
| Competitor rank used as performance evidence | HALT claim |
| Search policy or documentation becomes stale | Revalidate/supersede |

## 10. Commercial v1.0 connection

This protocol supports defensible SEO evaluation and implementation acceptance while preventing ranking guarantees, fabricated local scope, and unsupported demand forecasts.

## 11. References

- `scoring/category-sheets/seo.md`
- `framework/findings/seo-findings.md`
- `framework/findings/gbp-findings.md`
- `templates/package-catalog.md`