# Agentic Control Platform Readiness Evidence Requirements

Version: 0.1.0
Authority: `standards/evidence-standard.md` and `templates/evidence-register.md`

## Evidence decision

Every readiness conclusion must be reproducible from identified, authorized, in-scope evidence. Missing access is `UNKNOWN` or `blocked`; it is not proof that a control fails.

## Evidence tiers

| Tier | Evidence | Normal use |
|---|---|---|
| Operating | Current configuration, entitlement, log, trace, export, approval, test, incident, or system record | May support `CONTROLLED`, `PARTIAL_CONTROL`, or `VERIFIED_GAP` when admission passes |
| Designed | Approved architecture, policy, workflow, control design, RACI, or runbook | Supports design readiness; cannot independently prove operation |
| Reported | Interview, questionnaire, owner statement, vendor representation, or uncorroborated screenshot | Supports discovery and validation requests |
| External context | Law, standard, framework, product documentation, market research, or benchmark | Supports mapping and requirements; cannot prove buyer state |

## Minimum evidence record

```yaml
evidence_id: OI-EV-YYYY-NNN
assessment_id: ""
source_type: document|export|system_record|safe_test|interview|observation|third_party
source_location: ""
source_owner: public|client|evaluator|third_party
captured_at: YYYY-MM-DDThh:mm:ssZ
source_date: null
scope: ""
claim_scope: ""
capture_method: ""
authorization_ref: null
observation: ""
limitations: []
integrity_ref: null
sensitivity: public|internal|confidential|restricted
review_state: accepted|limited|rejected|superseded
confidence_support: high|medium|low|unknown
ledger_refs: []
```

## Material-finding threshold

A material finding may enter `validated` only when:

1. at least one admitted evidence record directly supports the observed condition;
2. evidence identity, attribution, recency, relevance, scope, integrity, authority, and traceability pass or have bounded limitations;
3. the observation is separated from interpretation and business impact;
4. contradictory evidence is referenced;
5. the finding has an owner, decision effect, control gate, and validation or remediation condition;
6. confidence does not exceed the weakest material dependency; and
7. the DecisionLedger records material admission, limitation, contradiction, suppression, and supersession decisions.

Designed, reported, inferred, or external-context evidence cannot independently produce a verified operating-control conclusion.

## Domain evidence matrix

| Domain | Required minimum | Strong corroboration | Blocker example |
|---|---|---|---|
| `AIGR-D1` | AI asset inventory plus named owners | Lifecycle and approval history | No accountable decision owner |
| `AIGR-D2` | Identity/entitlement and data-source inventory | Access-review and deprovisioning results | Unauthorized restricted-data access |
| `AIGR-D3` | Tool/action registry and effective permissions | Boundary-test and action-log results | Unbounded consequential actions |
| `AIGR-D4` | Approval/state map and sample decisions | Exception and supersession records | No reviewer for high-impact action |
| `AIGR-D5` | Evaluation specification and current results | Regression, drift, abuse, and defect records | No test boundary for material behavior |
| `AIGR-D6` | Event schema and reconstructable sample trace | Integrity, retention, export, and ledger proof | Material action cannot be reconstructed |
| `AIGR-D7` | Release, monitoring, rollback, and incident controls | Exercise and recovery evidence | No containment or recovery for critical action |

## Evidence handling

- Store only references, metadata, or approved sanitized excerpts in this repository.
- Do not commit client records, secrets, credentials, personal data, restricted logs, or proprietary exports.
- Record the authoritative external location, custodian, sensitivity, retention, access rule, and integrity reference.
- Restrict or redact only with a documented traceability-preserving method.
- Stop collection and route to `HALT` when authority or safe handling cannot be established.

## Coverage

Evidence coverage is calculated separately from readiness:

```text
weighted_known_points / weighted_applicable_points × 100
```

`UNKNOWN`, rejected, and blocked observations do not add known points. `NOT_APPLICABLE` items are removed only with recorded rationale and decision authority.

## Pre-decision checks

- [ ] Every cited Evidence ID resolves.
- [ ] Operating and designed evidence are not conflated.
- [ ] Material findings meet the threshold.
- [ ] Unknowns, blockers, limitations, and contradictions remain visible.
- [ ] Sensitive evidence handling is authorized.
- [ ] Evidence snapshot and relevant versions are frozen.
- [ ] Exported evidence metadata reconciles with the executive brief.
