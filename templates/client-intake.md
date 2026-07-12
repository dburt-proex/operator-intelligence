# Governed Client Intake Template

Use this intake to establish assessment scope, evidence access, decision authority, and known limitations before scoring begins. Intake statements are context, not verified evidence, unless supported by an admissible source.

## 1. Intake control

- Client:
- Assessment ID:
- Intake version:
- Intake date:
- Prepared by:
- Primary client contact:
- Executive sponsor:
- Decision authority:
- Intended assessment use:
- Target publication state: `official` / `provisional` / `range_only` / `internal_only`
- DecisionLedger intake record ID:

## 2. Business and operating context

- Business name:
- Website:
- Primary location:
- Service area:
- Operating model:
- Primary services or products:
- Material seasonal or urgent work:
- Primary customer segments:
- Current operating priorities:
- Material constraints:

## 3. Assessment scope

### Included

- Business units:
- Locations:
- Channels:
- Workflows:
- Systems:
- Date range:

### Excluded

- Explicit exclusions:
- Reason for exclusion:
- Known effect on coverage or interpretation:

### Scope gates

- [ ] Scope owner confirmed
- [ ] Included systems identified
- [ ] Exclusions disclosed
- [ ] Assessment date range defined
- [ ] Publication purpose documented
- [ ] Material conflicts of interest disclosed

## 4. Goals and decision questions

Record the decisions this assessment must support. Do not convert aspirations into outcome claims.

- Primary decision question:
- Secondary decision questions:
- Desired operational outcome:
- Current baseline, if verified:
- Claimed baseline, if unverified:
- Required decision date:
- Known dependencies:

## 5. Current channels and systems

For each applicable channel or system, record owner, access state, and available evidence.

| Channel or system | Owner | Access state | Evidence available | Date range | Notes |
|---|---|---|---|---|---|
| Website / CMS |  | `available` / `pending` / `blocked` / `not_applicable` |  |  |  |
| Analytics |  |  |  |  |  |
| Search Console |  |  |  |  |  |
| Business profile / listings |  |  |  |  |  |
| CRM |  |  |  |  |  |
| Scheduling |  |  |  |  |  |
| Email |  |  |  |  |  |
| SMS |  |  |  |  |  |
| Call tracking |  |  |  |  |  |
| Paid media |  |  |  |  |  |
| Social channels |  |  |  |  |  |
| Review platform |  |  |  |  |  |
| Workflow or automation platform |  |  |  |  |  |
| AI systems or agents |  |  |  |  |  |
| Other |  |  |  |  |  |

## 6. Evidence register

Create one row per source. Client statements remain `reported` until corroborated.

| Evidence ID | Source | Source owner | Type | Date range | Collection method | Verification state | Restrictions |
|---|---|---|---|---|---|---|---|
|  |  |  | `system` / `document` / `observation` / `interview` / `public` |  |  | `verified` / `reported` / `pending` / `rejected` |  |

### Evidence declarations

- [ ] Evidence owners are identified
- [ ] Date ranges are recorded
- [ ] Interview claims are marked `reported`
- [ ] Public absence is not treated as proof of internal absence
- [ ] Missing access is recorded as `unknown` or `blocked`, never as failure
- [ ] Superseded or conflicting sources are retained and identified

## 7. Known unknowns and blockers

| ID | Condition | State | Affected criteria or categories | Resolution owner | Required evidence | Publication effect |
|---|---|---|---|---|---|---|
|  |  | `unknown` / `blocked` |  |  |  |  |

Unknown and blocked conditions remain unscored. They must not be converted to zero, inferred failure, or unsupported certainty.

## 8. Current operating conditions

Record client-reported conditions without pre-classifying them as findings.

- Customer acquisition or demand concerns:
- Customer experience concerns:
- Workflow or handoff concerns:
- Data quality or reporting concerns:
- Tooling or integration concerns:
- Governance, privacy, security, or compliance concerns:
- AI use, planned AI use, or prohibited AI use:
- Manual work or owner dependency:
- Other material conditions:

## 9. Access and testing authorization

| Access or test | Authorized | Account owner | Access method | Allowed actions | Prohibited actions | Expiration |
|---|---|---|---|---|---|---|
|  | `yes` / `no` / `pending` |  |  |  |  |  |

- [ ] Least-privilege access is required
- [ ] Credentials will not be stored in the report or DecisionLedger
- [ ] Live changes are prohibited unless separately authorized
- [ ] Destructive, irreversible, or customer-facing tests are prohibited unless explicitly approved
- [ ] Test data handling and deletion requirements are documented
- [ ] Access revocation owner and date are defined

## 10. Data handling and confidentiality

- Data classification:
- Personal or sensitive data present:
- Regulated data present:
- Approved storage location:
- Retention period:
- Redaction requirements:
- Sharing restrictions:
- Client-approved reviewers:
- Required deletion or return date:

## 11. Stakeholders and approvals

| Role | Name | Decision authority | Required review | Approval scope |
|---|---|---|---|---|
| Executive sponsor |  |  |  |  |
| Operational owner |  |  |  |  |
| System owner |  |  |  |  |
| Data owner |  |  |  |  |
| Security / privacy reviewer |  |  |  |  |
| Report approver |  |  |  |  |

## 12. Intake readiness decision

- Evidence coverage estimate:
- Material unknowns:
- Material blockers:
- Scope limitations:
- Proposed assessment gate: `ALLOW` / `REVIEW` / `HALT`
- Gate rationale:
- Required next action:
- Responsible owner:
- DecisionLedger record ID:

### `ALLOW`

Use only when scope, authority, access, and minimum evidence requirements are sufficient to begin the authorized assessment.

### `REVIEW`

Use when bounded gaps exist but work can proceed without misrepresenting coverage, confidence, or conclusions.

### `HALT`

Use when authorization, scope, evidence integrity, data handling, or safety requirements are insufficient. Dependent scoring and publication work must not proceed.

## 13. Client acknowledgement

The client confirms that supplied information is accurate to the best of its knowledge, disclosed limitations are complete, and access authorization is restricted to the stated assessment scope. Intake acceptance does not validate claims, authorize implementation, or guarantee business outcomes.

- Client representative:
- Role:
- Acknowledgement date:
- Assessment lead:
- Intake gate:
- DecisionLedger record ID:

## 14. Pre-assessment validation

- [ ] Scope and exclusions are explicit
- [ ] Decision authority is identified
- [ ] Every evidence source has provenance and a date range
- [ ] Reported claims are separated from verified evidence
- [ ] Unknown and blocked conditions remain visible and unscored
- [ ] Access and testing permissions are explicit
- [ ] Data handling requirements are documented
- [ ] Publication intent and limitations are recorded
- [ ] Intake gate and rationale are logged in the DecisionLedger
- [ ] No unsupported ROI, revenue, conversion, ranking, lead-loss, market-share, competitor-performance, or timeline claim is presented as fact

Any failed authorization, evidence-integrity, data-handling, or scope-control check requires `HALT` until resolved or formally superseded.