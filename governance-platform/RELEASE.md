# Unified Governance Platform Architecture

| Field | Release value |
|---|---|
| Version | `v0.2.0` |
| Owner | Drew D. Burt |
| Intended audience | Technical founders, AI platform teams, governance and security leaders |
| Scope | One-page platform architecture and release record |
| Canonical artifact | `governance-platform/index.html` and `governance-platform/architecture.svg` |
| Hosting target | GitHub Pages in `dburt-proex/operator-intelligence` |
| Production URL | `https://dburt-proex.github.io/operator-intelligence/governance-platform/` |
| Release state | Internal release published; public deployment PR prepared |
| Rollback | Revert the deployment merge commit; after first successful deploy, retain its immutable deployment as the `v0.2.0` rollback baseline |

## Platform claim

DiffWall is the deterministic change-enforcement layer. It gates code, configuration, and deployment changes before merge or release. CASA is the runtime governance control plane. It gates a live agent action before it reaches a tool, API, or state-changing system. A versioned policy source and shared decision ledger connect the two. Operator Intelligence remains the assessment and operating-model layer that defines and improves the control criteria.

## Evidence and provenance

- CASA architecture and runtime gate model: [CASA Governance Knowledge Base](https://app.notion.com/p/58c6799b5a494c2ba4b4198c1d657e17)
- DiffWall deterministic enforcement, rule trace, and v1 proof: [DiffWall Guardian Layer](https://app.notion.com/p/38ee941db3bc80b0a9a4d96f598d527f)
- Shared CASA/DiffWall control model and known DiffWall limits: [Project Context File](https://app.notion.com/p/7a3f83708c1e42698504de59804ada3b)

## Evaluation gate

| Check | Result | Notes |
|---|---|---|
| Architecture claims traceable | Pass | CASA and DiffWall claims match the cited Notion source records. |
| Cross-product boundaries clear | Pass | The artifact separates operating model, change enforcement, and runtime governance. |
| Security / privacy review | Pass | Diagram contains no credentials, customer data, private URLs, or implementation secrets. |
| Accessibility | Pass | HTML includes a text alternative; SVG includes title and description. |
| Public release authority | Pass | Hosting target and repository were approved by the owner on 2026-07-14. |

## Deliberate exclusions

- No claim that Operator Intelligence is a deployed enforcement service.
- No claim that DiffWall v1 is a live runtime hook; its current documented boundary is PR/CI and action-object validation.
- No compliance certification claim.
- No private policies, secrets, customer records, or non-public implementation details.

## Next release gate

Before promotion to trusted public reference: merge the deployment PR, confirm GitHub Pages is configured to use GitHub Actions, validate the production rendering, and record the successful deployment URL as the `v0.2.0` rollback baseline.
