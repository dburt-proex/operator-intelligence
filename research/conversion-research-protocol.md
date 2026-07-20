# Conversion Research Protocol

Version: v1.0 commercial research support  
Stage alignment: Stage 8 — `research/`  
Folder alignment: `research/`  
Status: Governed conversion-evidence protocol

## 1. Purpose

Define how external conversion research may inform evaluation criteria, testing plans, form and CTA review, and recommendation rationale without creating unsupported client conversion, lead-loss, revenue, or uplift claims.

## 2. Allowed uses

- support an approved evaluation expectation
- define a safe usability or action-path test
- explain a known friction mechanism
- identify a validation question
- inform acceptance criteria for a bounded implementation

External conversion research does not prove that a client is losing leads or that a change will increase conversion.

## 3. Source hierarchy

1. primary controlled experiments and peer-reviewed research
2. official platform/browser/accessibility documentation
3. transparent studies with sample, method, metric, and period
4. credible usability research organizations
5. vendor case studies, treated as contextual and limitation-heavy
6. expert commentary, validation-only unless independently supported

## 4. Research object

```yaml
research_id: OI-RES-CONV-YYYY-NNN
question: ""
mechanism: clarity|friction|accessibility|trust|form_completion|mobile_use|response_expectation|other
source_refs: []
population_or_context: ""
metric_definition: ""
method: ""
observation: ""
client_applicability: direct|partial|context_only|unknown
confidence: high|medium|low|unknown
limitations: []
allowed_use: criterion_support|test_design|acceptance_criteria|context|validation
prohibited_claims: []
review_state: ALLOW|REVIEW|HALT
```

## 5. Applicability controls

Before use, compare:

- device and browser context
- buyer intent and task
- traffic/source context
- form or page type
- business model and service complexity
- baseline maturity
- metric definition
- sample and study period

A result from another context cannot be applied as the client’s expected uplift.

## 6. Client evidence required

A conversion finding requires direct client evidence such as:

- screenshot or page copy
- mobile/desktop action-path review
- click-to-call test
- safe form test
- validation/error/confirmation behavior
- authorized analytics or event records
- CRM or lead records when the claim concerns downstream outcomes

External research may explain why a verified condition matters; it cannot replace the verified condition.

## 7. Claim rules

Approved:

- “The tested form contains [verified friction]. Research supports reviewing this mechanism, but the client-specific conversion effect is unknown.”
- “The implementation acceptance test should confirm [observable behavior].”

Prohibited without client data and approved method:

- percentage uplift
- leads recovered
- revenue gained or lost
- close-rate change
- payback period
- guaranteed response improvement

## 8. Workflow

1. Define the client condition or test question.
2. Collect primary and transparent sources.
3. Record context, metric, sample, and limitations.
4. Test applicability to the client scope.
5. Separate mechanism evidence from client evidence.
6. Bound recommendation and acceptance criteria.
7. Record unsupported outcome claims as prohibited.
8. Revalidate stale or superseded sources.

## 9. Failure handling

| Failure | Response |
|---|---|
| Vendor uplift used as client forecast | HALT claim |
| Form best practice applied without task context | REVIEW applicability |
| External research replaces client test | Require direct evidence |
| Correlation represented as causation | Rewrite or reject |
| Completion metric confused with business outcome | Separate acceptance and realized value |

## 10. Commercial v1.0 connection

This protocol supports evidence-aware conversion recommendations and testable acceptance criteria without manufacturing uplift or revenue claims.

## 11. References

- `scoring/category-sheets/conversion.md`
- `framework/findings/conversion-findings.md`
- `templates/package-catalog.md`