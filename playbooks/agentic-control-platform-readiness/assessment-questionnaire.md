# Agentic Control Platform Readiness Questionnaire

Version: 0.1.0
Use: Structured discovery and evidence request
Default treatment for unanswered material questions: `UNKNOWN`

## Engagement control

| Field | Response | Owner | Evidence ref |
|---|---|---|---|
| Decision this sprint informs | | | |
| In-scope AI assets and workflows | | | |
| Environments and business units | | | |
| Explicit exclusions | | | |
| Executive sponsor | | | |
| Platform owner | | | |
| Governance owner | | | |
| Security / identity owner | | | |
| Evidence snapshot date | | | |
| Testing authority reference | | | |
| Evidence handling classification | | | |
| Conflicts or vendor relationships | | | |

## `AIGR-D1` — Agent purpose and ownership

1. Which agents, models, prompts, tools, datasets, workflows, versions, and environments are in scope?
2. What approved business purpose and prohibited purposes apply to each asset?
3. Who owns the business outcome, technical operation, risk decision, data sources, and retirement decision?
4. What lifecycle states exist from intake through retirement, and who may change each state?
5. How are shadow, duplicated, abandoned, or third-party AI assets discovered?
6. Which evidence proves ownership and lifecycle decisions operate rather than merely being planned?

Minimum evidence: asset register, ownership/RACI record, lifecycle workflow, approval history, change history, and discovery output.

## `AIGR-D2` — Data and system access

1. Which human, machine, service, and agent identities exist?
2. Which data sources, systems, APIs, secrets, and environments can each identity access?
3. How are data classes, purpose limits, residency, retention, deletion, and source ownership represented?
4. How are least privilege, separation of duties, access review, deprovisioning, and break-glass access enforced?
5. Can effective permissions be reconstructed across direct, group, inherited, delegated, and temporary grants?
6. Which controls detect and remediate excessive or stale privileges?

Minimum evidence: identity inventory, entitlement export, data-source registry, classification map, access-review record, deprovisioning evidence, and secrets-handling control.

## `AIGR-D3` — Tool and action authority

1. Which read, create, update, delete, execute, communicate, transact, or approve actions can each agent invoke?
2. Which actions are denied, approval-gated, rate-limited, value-limited, time-limited, or environment-limited?
3. Where are action policies enforced: prompt, application, gateway, platform, identity layer, or downstream system?
4. How are tool schemas, parameters, target resources, and permission scopes validated?
5. What containment, reversal, compensation, or human exception path exists for each consequential action?
6. Can unauthorized, out-of-scope, or malformed actions be deterministically blocked and evidenced?

Minimum evidence: tool registry, scope/permission map, allow/deny policy, approval rule, action log, boundary test, and containment procedure.

## `AIGR-D4` — Workflow approvals and human intervention

1. Which decisions require human review, approval, execution, or risk acceptance?
2. What information must the reviewer receive, and how is reviewer identity recorded?
3. What prevents approval self-escalation, rubber stamping, stale approval reuse, or bypass?
4. How do exceptions, overrides, appeals, timeouts, and unavailable reviewers route?
5. Which completion criteria prove the human decision was applied to the intended version and target?
6. How are material decisions superseded when evidence or scope changes?

Minimum evidence: workflow/state map, approval matrix, review record, exception route, escalation SLA, and supersession history.

## `AIGR-D5` — Evaluation and failure testing

1. What expected behavior, prohibited behavior, failure, abuse, adversarial, and edge cases are defined?
2. Which tests apply before a change is accepted and which run during operation?
3. Which thresholds trigger block, review, alert, rollback, or incident response?
4. How are evaluation datasets versioned, protected from leakage, sampled, and approved?
5. How are regressions, drift, false positives, false negatives, and unresolved defects handled?
6. Who approves evaluation changes and accepts residual test limitations?

Minimum evidence: evaluation specification, versioned fixtures, results, thresholds, defect register, drift rule, and test-owner approval.

## `AIGR-D6` — Logging, evidence, and auditability

1. Can a material action be reconstructed from request through policy decision, approval, tool call, result, verification, and correction?
2. Which correlation IDs bind users, agents, models, prompts, policies, tools, resources, and versions?
3. Are log content, access, integrity, retention, export, and deletion controls defined?
4. Which sensitive inputs are redacted or excluded without destroying decision traceability?
5. Can approved, rejected, overridden, failed, and partially executed actions be distinguished?
6. Can evidence be exported in a stable format for independent review or platform migration?

Minimum evidence: event schema, sample traces, integrity control, access/retention policy, export, and DecisionLedger records.

## `AIGR-D7` — Deployment, monitoring, rollback, and incident response

1. Which code, configuration, policy, prompt, model, data, permission, and workflow changes enter release control?
2. Which change-time controls block unsafe changes before acceptance?
3. Which runtime signals detect permission drift, behavioral drift, policy violations, failure, abuse, or unexpected impact?
4. What kill switch, rollback, isolation, revocation, or compensating action exists?
5. Who owns alerts, incidents, communications, evidence preservation, and recovery decisions?
6. When were rollback and incident routes last exercised, and what changed afterward?

Minimum evidence: release policy, change-control results, monitoring rules, alert/incident samples, rollback test, recovery evidence, and post-incident record.

## Decision and procurement readiness

1. Which platform capabilities are mandatory, optional, prohibited, or already supplied elsewhere?
2. Which systems of record must remain authoritative after implementation?
3. Which integrations require bidirectional mutation versus read-only evidence exchange?
4. What data, identity, audit, portability, exit, and evidence-export requirements are non-negotiable?
5. Which control gaps must be resolved before procurement, before configuration, before pilot, and before expansion?
6. Who can separately authorize procurement, implementation, production use, and residual-risk acceptance?

## Interview close

- [ ] Unanswered material questions are registered as `UNKNOWN`, not scored zero.
- [ ] Reported statements are distinguished from direct evidence.
- [ ] Requested evidence has an owner and due date.
- [ ] Contradictions and access limits remain visible.
- [ ] No interview response is represented as platform certification or operating proof.
