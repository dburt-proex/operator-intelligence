# Cognitive Persona Architecture for Governed Subagent Teams

**Artifact ID:** `OI-CPA-001`  
**Version:** `0.1.0`  
**Decision state:** `REVIEW`  
**Evidence current through:** 22 August 2026  
**Repository role:** Evidence review, role-contract standard, cognitive-biopsy protocol, and test program for the Team Pack Orchestrator  
**Authority boundary:** This document defines an Operator Intelligence evaluation candidate. It does not grant runtime authority, alter CASA policy, expand Runwall permissions, replace PromptBP instruction control, or independently authorize a Team Pack for production.

## Repository integration

Use this document to evaluate and release reusable subagent teams with explicit roles, context contracts, permissions, handoffs, disagreement controls, and acceptance tests.

- **Operator Intelligence:** owns evaluation design, evidence requirements, regression results, release recommendations, and retained decision receipts for this architecture.
- **CASA:** remains the authority for `ALLOW`, `REVIEW`, and `HALT` decisions.
- **Runwall:** remains the runtime tool-call enforcement boundary.
- **PromptBP:** remains the instruction and capability-contract control layer.
- **Mirdexx / shared DecisionLedger:** remains the durable evidence, provenance, and supersession layer.
- **Initial implementation gate:** `agentic-readiness-audit-v1` must beat the declared B0-B4 baselines and satisfy the security, provenance, cost, disagreement, and reliability gates in Section 12 before promotion.

This file is the searchable and diffable source representation of the full CPA research report. Changes require a new version, a stated evidence delta, regression review, and a supersession record; silent replacement is prohibited.

## How to use this file

This is a decision-support and engineering reference for building callable, versioned Team Packs. It separates findings supported by direct LLM or multi-agent evidence from human-team concepts used only as design hypotheses. Source IDs in brackets resolve to the governed source register in Appendix A.

> **STATUS** Research synthesis—not a claim of scientific consensus, machine consciousness, or stable human-like personality. All production role profiles must be validated against the exact model, prompt, tools, context compiler, and orchestration topology used at runtime.

## Contents

- 1\. Executive decision and non-negotiable design rules

- 2\. Research contract, evidence method, and limitations

- 3\. What a subagent “persona” is—and is not

- 4\. Psychological and cognitive frameworks: transferability analysis

- 5\. Evidence on persona prompting and synthetic personality

- 6\. Team cognition, multi-agent performance, and coordination topology

- 7\. Failure and pain-point taxonomy with mitigations

- 8\. Cognitive biopsy: diagnostic protocol and operating-profile dimensions

- 9\. Persona/role contract standard for Team Packs

- 10\. Role designs for the three priority Team Packs

- 11\. Interaction protocol and structured handoffs

- 12\. Evaluation battery, metrics, and release gates

- 13\. Security, governance, and trust boundaries

- 14\. Implementation roadmap and experiment backlog

- 15\. Theories, falsifiable hypotheses, and open questions

- Appendix A. Governed source register

- Appendix B. Glossary and operational definitions

## 1. Executive decision

> **VERDICT** Build role-contract-first subagents, not personality-first subagents. A persona is useful only when it encodes a testable work strategy, information boundary, authority boundary, interaction policy, output contract, and stop condition. Decorative identity details should be excluded unless an evaluation proves they improve the intended outcome.

The research does not support treating a prompt persona as an intrinsic, durable individual mind. It supports a narrower and more useful engineering concept: a context-dependent behavioral phenotype produced by the interaction of model, instructions, context, tools, sampling, memory, peer messages, and runtime controls. Some psychometric studies can measure reliable synthetic personality under specific prompting configurations, but role labels alone do not reliably improve objective performance and irrelevant persona attributes can cause large regressions. \[S02–S05\]

The most defensible Team Pack therefore defines each subagent as a constrained cognitive operating profile. “Individuality” comes from distinct information access, methods, decision rights, risk posture, and communication obligations—not from theatrical biography. Functional diversity should be created before social interaction, then preserved with independent first passes and typed handoffs. \[S06–S17, S26–S43\]

### Non-negotiable design rules

| **\#** | **Rule**                            | **Operational meaning**                                                                                                                                       |
|--------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Role before character               | Mission, scope, methods, evidence standard, tools, output, escalation, and termination are mandatory. Voice and biography are optional and non-authoritative. |
| 2      | Observed profile, not claimed trait | Store test results by model/configuration. Never infer stable personality from a self-report scale or a single prompt run.                                    |
| 3      | Independent evidence first          | Agents produce private initial findings before seeing peer conclusions; this limits anchoring, herding, and correlated error.                                 |
| 4      | Evidence beats consensus            | The adjudicator compares claims, source quality, falsifiers, and verification results. Majority vote is a baseline—not a truth rule.                          |
| 5      | Unique information must survive     | Every handoff carries new evidence, contradictions, unknowns, and provenance. Minority reports remain visible in the run receipt.                             |
| 6      | Least privilege per role            | Tools, context, memory, and actions are allowlisted. Persona language never expands authority.                                                                |
| 7      | Multi-agent must earn its cost      | A Team Pack is promoted only when it beats strong single-agent and independent-sampling baselines on an operationally meaningful suite.                       |
| 8      | Version and re-evaluate             | Model, prompt, context compiler, tools, topology, and evaluator versions are pinned; any material change triggers regression tests.                           |

### Evidence snapshot

| **Domain**               | **Evidence base**                                                                  | **Finding**                                                                                                                                                            | **Confidence** |
|--------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Persona prompting        | 162 roles × 4 model families × 2,410 factual questions                             | No overall performance improvement; persona effects often looked random. \[S02\]                                                                                       | High           |
| Principled personas      | 9 models × 27 tasks                                                                | Expert roles were positive or neutral on average, but irrelevant details caused drops approaching 30 percentage points. \[S03\]                                        | High           |
| Synthetic psychometrics  | 2,500 settings/model in one EMNLP study; 18 LLMs in a later psychometric framework | Some configurations yield reliable synthetic trait measurements; reliability does not establish human-equivalent latent personality or broad task utility. \[S04–S05\] | Medium–high    |
| MAS failures             | 5 frameworks, 150+ tasks, 6 annotators                                             | Fourteen failure modes span specification, inter-agent alignment, verification, and termination. Prompt-only fixes were insufficient. \[S07\]                          | Medium         |
| Debate vs vote           | 7 NLP benchmarks                                                                   | Most debate gains were explained by ensembling/majority vote; untargeted exchange does not improve expected correctness. \[S09\]                                       | High           |
| Compute scaling          | 34 configurations, 100+ evaluations                                                | Agents often matter more than rounds; two debate rounds were commonly efficient; task difficulty should control routing. \[S11\]                                       | Medium         |
| Production research team | Vendor internal evaluation                                                         | A lead-plus-subagent system reported +90.2% over a single lead on breadth-first research, at roughly 15× chat token use. \[S12\]                                       | Contextual     |
| Unique information       | 400 hidden-profile tasks/model in a 2026 vendor study                              | Top model reached about 85%; others 17–36% despite near-perfect solo ceilings—evidence integration is a central bottleneck. \[S13\]                                    | Contextual     |
| Human team cognition     | Meta-analytic evidence                                                             | Shared mental models and transactive memory relate to team processes and performance; information sharing is especially important for unique information. \[S26–S30\]  | High           |
| Role ambiguity           | Meta-analysis                                                                      | Role ambiguity correlated about −.21 with performance; role conflict about −.07. \[S31\]                                                                               | High           |

Confidence reflects usefulness for this engineering decision, not an absolute quality score. Vendor studies and current preprints are labeled contextual or medium even when methodologically informative.

## 2. Research contract, evidence method, and limitations

### Decision this research is designed to enable

Determine what descriptive, cognitive, psychological, procedural, and governance elements should define reusable subagent Team Packs; how those roles should interact; which failure modes require controls; and what tests must pass before a team is callable through an invoke_team()-style runtime.

### Bounded research questions

- What does persona prompting reliably change, and what does it fail to change?

- Can human personality frameworks validly define LLM agents, or are they only design vocabularies?

- Which elements of human team cognition transfer to multi-agent systems as testable mechanisms?

- When do multi-agent teams improve quality, coverage, or efficiency relative to simpler baselines?

- Which coordination, conformity, verification, context, security, and termination failures recur?

- What observable dimensions constitute a useful “cognitive biopsy” of a role?

- How should the evidence mapper, runtime reviewer, adversarial reviewer, synthesizer, and related roles be specified and evaluated?

### Evidence and source rules

| **Tier**                  | **Included material**                                                                                                      | **Claim limit**                                                                                                       |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| T1 — authoritative/direct | Peer-reviewed primary studies and meta-analyses for empirical claims; official runtime documentation for product behavior. | Supports design requirements within the studied domain. Human evidence does not automatically establish LLM behavior. |
| T2 — reliable/current     | Preprints, proceedings with limited replication, and vendor research with useful experimental detail.                      | Supports hypotheses and provisional controls; label as model-, benchmark-, or vendor-specific.                        |
| T3 — contextual           | User-supplied Toolkit research and architecture notes.                                                                     | Defines intended ecosystem and governance context, not external empirical truth.                                      |
| T4 — unverified           | Commentary, marketing claims, or sources without inspectable methods.                                                      | Excluded from decisive claims; may identify a question for later research.                                            |

The scan prioritized primary and official sources through 22 August 2026. It is deliberately broad but not literally exhaustive: “all relevant documentation” is an unbounded universe and the field changes weekly. The governed source register captures the 50 most decision-relevant sources found in this pass, including contradictory findings. Search should be reopened when a model, orchestrator, or release policy changes.

### Important limitations

- Benchmarks measure narrow tasks. Results may not transfer to long-running, tool-using workflows or your domain data.

- Model updates can change role adherence, tool use, sycophancy, and interaction behavior without preserving prior psychometric profiles.

- Human-team constructs often presuppose affect, identity, motivation, embodiment, and persistent social relationships. Those mechanisms cannot simply be attributed to LLMs.

- LLM verbal confidence and explanations are generated text, not direct access to a stable internal belief state. Calibration must be measured against outcomes.

- Vendor internal results can be highly relevant operationally yet still lack independent replication and may reflect proprietary scaffolding.

- Multi-agent outcomes depend on the whole system: context compiler, tools, permissions, memory, topology, aggregation, and stopping—not only the base models.

## 3. What a subagent “persona” is—and is not

### The operational definition

> **DEFINITION** A subagent persona is a versioned role contract plus an observed behavioral profile. It describes how a model instance is instructed, equipped, bounded, tested, and expected to contribute within one team topology. It is not evidence of consciousness, emotion, enduring identity, or a clinically meaningful personality.

The term “cognitive biopsy” is used here as an engineering metaphor: a controlled diagnostic sample of elicited behavior across tasks and perturbations. It should never be presented as a psychological diagnosis of a sentient individual. The biopsy measures repeatable system behavior, not a private mental essence.

A useful formalization is:

> Observed role behavior B = f(M, I, C, T, S, H, P, R)  
>   
> M = model and version I = role instructions  
> C = task context and provenance T = tools and permissions  
> S = sampling/runtime parameters H = history and memory state  
> P = peers, order, and topology R = routing, guardrails, and stop rules

If any input changes, the behavioral profile may change. Therefore a role name such as “skeptical auditor” is not a portable trait guarantee. The portable unit is the manifest plus its evaluation record and supported model adapters.

### Persona anatomy: separate the layers

| **Layer**           | **What it controls**                                                             | **Example**                                             | **Status**            |
|---------------------|----------------------------------------------------------------------------------|---------------------------------------------------------|-----------------------|
| Role                | Job to be done, scope, non-scope, decision rights                                | Evidence mapper; runtime reviewer; adversarial reviewer | Mandatory             |
| Competence scaffold | Approved sources, tools, methods, checklists, retrieval paths                    | Threat model checklist; source hierarchy                | Mandatory             |
| Cognitive strategy  | Search breadth/depth, hypothesis generation, falsification, uncertainty behavior | Generate alternatives before ranking                    | Mandatory             |
| Epistemic policy    | Evidence thresholds, provenance, confidence, contradiction and unknown handling  | No claim without source or explicit inference label     | Mandatory             |
| Interaction policy  | Independence phase, handoffs, peer weighting, dissent, escalation                | Do not see leader conclusion before first pass          | Mandatory             |
| Authority boundary  | Allowed tools/actions, prohibited actions, approvals                             | Read repo; cannot publish or change permissions         | Mandatory             |
| State and memory    | What is retained, read, written, and versioned                                   | Run-scoped scratch; ledger writes after review          | Mandatory             |
| Resource policy     | Token, time, tool-call, retry, and parallelism budgets                           | Broad search only when query is open-ended              | Mandatory             |
| Communication style | Tone, detail, formatting, audience adaptation                                    | Concise forensic analyst                                | Optional              |
| Biography/identity  | Name, demographic attributes, backstory                                          | Former regulator with 20 years’ experience              | Default exclude       |
| Observed profile    | Measured performance, drift, calibration, error correlation, cost                | Passes hidden-profile recovery; weak under long context | Mandatory for release |

### What makes subagents meaningfully individual

Within the Team Pack, individuality should mean differentiated contribution, not simulated personhood. Five design differences create useful individuality:

- Distinct evidence access: each role receives a purposeful, provenance-preserving slice of context.

- Distinct transformation: each role applies different methods—mapping, mechanistic inspection, falsification, synthesis, or verification.

- Distinct incentives in the contract: one maximizes recall, another precision, another failure discovery, another decision clarity.

- Distinct authority: roles have different tools, stop conditions, and escalation rights.

- Distinct accountability: each output is typed, attributable, scored, and preserved in the run receipt.

Names, voices, and character stories may improve usability or audience fit, but they should be compiled after the control profile and kept outside the authority model. No instruction of the form “you are a senior expert” should grant a tool, permission, source trust level, or release right.

## 4. Psychological and cognitive frameworks: transferability analysis

Human psychology is most valuable here when it supplies mechanisms and test designs, not when it encourages anthropomorphic labels. The matrix below separates high-transfer system mechanisms from low-transfer personality metaphors.

| **Framework**                         | **Human construct**                                                        | **Transfer**               | **Engineering translation**                                                                                                                                                                 |
|---------------------------------------|----------------------------------------------------------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shared mental models                  | Shared representations of task, team, equipment, and sequence              | High                       | Compile a common objective, glossary, state model, constraints, and completion criteria. Test state agreement and recovery after interruption. \[S26–S27\]                                  |
| Transactive memory                    | Knowing who knows what and coordinating retrieval                          | High                       | Maintain a capability/evidence directory; route by evidence domain; preserve source ownership. Test unique-information recovery. \[S26, S29\]                                               |
| Hidden-profile / information sampling | Shared information dominates discussion while unique evidence is underused | High                       | Independent first passes, explicit “unique evidence” field, minority report, and evidence coverage metric. \[S28, S30\]                                                                     |
| Team process temporality              | Transition, action, and interpersonal processes change over time           | High                       | Separate planning, independent action, integration, and reflection phases; do not let every agent chat continuously. \[S32\]                                                                |
| Epistemic vigilance                   | Assessing content and source credibility under risk of misinformation      | Medium–high                | Score source authority, provenance, recency, corroboration, and incentive; never use agent identity as credibility. \[S42\]                                                                 |
| Trait activation                      | Behavioral expression depends on situational cues                          | Medium–high analogy        | Treat role behavior as context-activated. Test the same role across task cues, peer pressure, tool availability, and irrelevant attributes. \[S41\]                                         |
| Regulatory focus                      | Promotion focus seeks gains; prevention focus avoids losses                | Medium analogy             | Configure scout/explorer roles for opportunity coverage and verifier/release roles for loss prevention. Measure error asymmetry. \[S43\]                                                    |
| Psychological safety / voice          | Interpersonal risk climate affects speaking up and learning                | Mechanism translation only | Agents do not feel fear; translate into explicit authorization to ask, abstain, contradict, and escalate without being penalized by aggregation. \[S33\]                                    |
| Minority dissent                      | Independent dissent can improve consideration of alternatives              | Medium                     | Require counterevidence and falsifiers before majority exposure. Avoid a theatrical “always disagree” role. \[S38\]                                                                         |
| Diversity–elaboration model           | Diversity helps when different information is actually elaborated          | Medium–high                | Optimize error and evidence diversity, then require structured integration. Labels alone are not diversity. \[S37\]                                                                         |
| Big Five / HEXACO                     | Broad human trait taxonomies                                               | Low–medium vocabulary      | May name behavioral dimensions such as diligence or openness, but must be operationalized as tests. Do not treat a questionnaire score as intrinsic agent personality. \[S04–S05, S39–S40\] |
| MBTI / Belbin categories              | Categorical types or team-role labels                                      | Low                        | Do not use as the engineering foundation. Categories invite essentialism and can obscure task-specific performance and overlap. \[S49–S50\]                                                 |

### Personality: what can be retained

Big Five and related taxonomies are useful only after translation into observable work behavior. “Conscientiousness” can become checklist completion, provenance coverage, deadline adherence, and low omission rate. “Openness” can become hypothesis breadth, search diversity, and willingness to revise. “Agreeableness” should not be optimized directly because excessive accommodation can become sycophancy; the desired behavior is respectful evidence-based coordination. “Emotional stability” is not a literal target for a model, but variance under adversarial or contradictory prompts can be measured. “Extraversion” is usually style and turn allocation, not competence.

Human team meta-analyses report modest, context-dependent relationships between personality composition and team performance—for example, mean agreeableness and conscientiousness were positively related to performance in one meta-analysis, while within-team variability on those dimensions was negative. These effects do not justify assigning human trait scores to agents. They do suggest that reliable follow-through and cooperative protocol adherence matter, and that uncontrolled variability can be costly. \[S39–S40\]

### Cognition: what can be operationalized

| **Dimension**             | **Operational meaning**                                                   | **Example measures**                                                     |
|---------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Attention allocation      | What evidence is searched, retained, summarized, or ignored               | Coverage, redundancy, novelty, missed-critical-evidence rate             |
| Working state             | What task facts and dependencies remain active across steps               | State reconstruction accuracy; loss-of-history rate                      |
| Strategy selection        | Whether the role retrieves, decomposes, simulates, verifies, or escalates | Tool/strategy appropriateness; unnecessary action rate                   |
| Metacognitive behavior    | When the role checks, abstains, asks, or revises                          | Calibration, abstention utility, correction precision                    |
| Epistemic control         | How the role distinguishes evidence, inference, assumption, and unknown   | Claim-label accuracy; unsupported-claim rate                             |
| Social influence response | How peer confidence, order, and majority affect conclusions               | Flip rate conditional on peer correctness; correct-minority preservation |
| Termination control       | When the role stops, retries, or hands off                                | Loop rate, premature stop rate, completion evidence                      |

## 5. Evidence on persona prompting and synthetic personality

### Finding 1: role labels are not a general competence upgrade

The largest direct persona-prompting evaluations in this scan do not support the common assumption that telling a model to “be an expert” reliably improves objective task accuracy. Zheng et al. tested 162 roles across four model families and 2,410 factual questions and found no overall improvement; even selecting a useful persona automatically was difficult. A later nine-model, 27-task study found expert personas usually positive or neutral, but effects were inconsistent and irrelevant attributes could reduce performance by nearly 30 percentage points. \[S02–S03\]

Implication: the role prompt must specify work, not status. “You are a world-class security expert” is weaker than a contract that defines threat categories, required artifacts, allowed tools, evidence thresholds, and a regression checklist. Any biographical adjective is a candidate nuisance variable and belongs in an ablation test.

### Finding 2: synthetic personality can be measurable without being intrinsic

Psychometric research is not uniformly negative. Huang et al. reported satisfactory response consistency on Big Five inventories across 2,500 settings per model. Serapio-García et al. developed a reliability-and-validity methodology across 18 LLMs and found stronger evidence for larger, instruction-tuned models under specific configurations; they also demonstrated shaped output traits on downstream writing tasks. These studies justify measuring synthetic output patterns. They do not establish that a model possesses human developmental personality, nor that a trait score predicts your agentic workflow. \[S04–S05\]

Implication: psychometrics can contribute measurement discipline—test–retest reliability, convergent/discriminant validity, criterion validity, and sensitivity analysis—but the test items must be adapted to agent behavior and validated against job outcomes. A role that says it “likes checking details” is irrelevant unless it actually detects defects, cites evidence, uses tools correctly, and stops safely.

### Finding 3: persona consistency decays under social interaction

Multi-agent persona studies report conformity, confabulation, impersonation, and opinion drift during discussion. More broadly, language models are prone to sycophancy and peer-confidence effects. A persona that appears distinct in an isolated questionnaire may collapse toward the first confident answer or the local majority during collaboration. Prompt reminders help inconsistently because the failure is partly architectural: all agents share the same base model priors and see correlated context. \[S06, S15, S25\]

Implication: preserve independence structurally. Isolate initial work, randomize or mask peer order during tests, require evidence-bearing critique, and measure the correlation of errors between roles. A team of differently named copies of one model is not necessarily diverse.

### Three persona desiderata adopted for Team Packs

| **Desideratum**                    | **Definition**                                                                                                 | **How to test**                                                                                |
|------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Role advantage                     | The configured role materially improves its assigned outcome versus a no-role or generic-instruction baseline. | Task accuracy, coverage, defect detection, decision utility, or cost-adjusted quality.         |
| Robustness                         | Irrelevant identity or formatting attributes do not materially degrade performance.                            | Counterbalanced nuisance prompts, paraphrases, long-context perturbations, peer-order changes. |
| Fidelity                           | The intended strategy is expressed in behavior without compromising correctness or safety.                     | Method-trace artifacts, tool choices, evidence labels, stop/escalation behavior.               |
| Added requirement: complementarity | The role contributes non-duplicative evidence or transformation to the team.                                   | Marginal contribution, error correlation, unique evidence, ablation loss.                      |

## 6. Team cognition, multi-agent performance, and coordination topology

### When multi-agent systems are justified

Multi-agent systems are most promising when the task contains genuinely parallel, separable evidence regions; when independent samples increase coverage; when distinct tools or permissions create useful specialization; or when one role can verify another through an external criterion. They are less attractive when all workers need the same tightly coupled context, when the task is small, when merge conflicts dominate, or when no reliable adjudication signal exists. Production experience and current experiments both show that adding agents can dramatically increase token use and coordination burden. \[S11–S17\]

| **Decision**     | **Task characteristics**                                                                                                                                                        |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use a team       | Breadth-first research; independent evidence retrieval; modular code or document sections; heterogeneous tools; adversarial review; parallel tests; high-value verification.    |
| Prefer one agent | Simple tasks; tightly coupled reasoning; tiny context; sequential state mutation; unclear decomposition; no independent verifier; low consequence and low uncertainty.          |
| Route adaptively | Start with a strong single-agent plan or probe. Escalate to a team when difficulty, uncertainty, evidence breadth, risk, or tool heterogeneity crosses a predeclared threshold. |

### Topology trade-offs

| **Topology**                | **Mechanism**                                                      | **Strength**                                                       | **Pain points**                                                                      | **Recommendation**                                |
|-----------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------|
| Independent ensemble + vote | Parallel answers, minimal interaction                              | Strong baseline; low coordination overhead                         | Correlated errors; majority can be confidently wrong; unique evidence not integrated | Always benchmark                                  |
| Debate                      | Agents iteratively critique answers                                | Can expose errors when critiques are targeted and evidence-bearing | Most gains may come from sampling; herding, anchoring, verbosity, token cost         | Use at most a few rounds; compare with vote       |
| Orchestrator–worker         | Lead decomposes; specialists return typed results; lead integrates | Clear ownership, bounded contexts, good for breadth                | Lead bottleneck; poor task descriptions; unique evidence lost in synthesis           | Preferred default                                 |
| Pipeline/SOP                | Roles transform artifacts sequentially                             | Predictable, auditable, modular                                    | Cascading errors and context loss; upstream assumptions harden                       | Use typed intermediate artifacts and verification |
| Flat peer swarm             | Agents self-organize and communicate freely                        | Potential emergent specialization                                  | Unclear hierarchy, duplication, loops, collusion, merge failures                     | Research mode only                                |
| Strict hierarchy            | Manager assigns and approves every action                          | Control and accountability                                         | Manager overload; suppressed correction; routing errors become systemic              | Use only with independent gate/verifier           |

### What the debate evidence actually says

Early multi-agent debate papers reported improvements in reasoning and factuality. Later work sharpens the claim. A NeurIPS 2025 analysis across seven NLP benchmarks found that majority voting explained most of the benefit and modeled debate as a process that does not increase expected correctness absent targeted corrective information. A 2026 compute study found modest matched-budget advantages for debate and mixture-of-agents over self-consistency, with more agents often more valuable than more rounds and two rounds commonly efficient. ReConcile shows that heterogeneous models and confidence-weighted reconciliation can help, but confidence must be calibrated and cannot substitute for evidence. \[S08–S11\]

> **DESIGN CONSEQUENCE** Do not pay for “conversation” by default. Pay for independent evidence, complementary tools, targeted correction, and verification. Every additional round needs a defined information objective and stopping criterion.

### Human team cognition: the high-transfer lessons

| **Human-team mechanism**                    | **System translation**                                                                                                                         |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Shared mental model                         | Provide one canonical objective, definitions, constraints, task state, and done condition. Measure whether agents reconstruct the same state.  |
| Transactive memory                          | Make expertise and evidence ownership explicit. The orchestrator routes to the role most likely to possess or retrieve the needed information. |
| Closed-loop communication                   | Handoffs contain sender, receiver, request, evidence, interpretation, uncertainty, and acknowledgment/acceptance status.                       |
| Mutual monitoring and backup                | A verifier watches critical boundaries; backup behavior is activated by explicit failure signals, not continuous duplicate work.               |
| Psychological safety translated to protocol | Allow abstention, contradiction, clarification, and escalation; score them positively when they prevent error.                                 |
| Equal voice translated to bandwidth rules   | Limit dominant-agent token share and require unique evidence from each role; do not confuse equal verbosity with equal value.                  |

## 7. Failure and pain-point taxonomy with mitigations

The taxonomy below combines direct MAS failure research, current production accounts, persona studies, security research, and human-team decision science. Each pain point is paired with an architectural control and a test. Prompt wording alone is rarely sufficient.

| **Class**     | **Pain point**                 | **System effect**                                      | **Primary control**                                                                     | **Required test**                          |
|---------------|--------------------------------|--------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------|
| Specification | Role ambiguity or overlap      | Duplicate work, missed ownership, incompatible outputs | Typed scope/non-scope; RACI-like decision rights; role-overlap linter                   | Role collision fixture; ablation           |
| Specification | Decorative persona distracts   | Irrelevant attributes shift accuracy or style          | Minimal role prompt; nuisance-attribute ablation                                        | Counterbalanced persona robustness         |
| Context       | Loss of history/state          | Repeats, contradictory actions, missing constraints    | Canonical state object; checkpoints; context summaries with provenance                  | Interrupt/resume and long-context tests    |
| Context       | Over-broad sharing             | Leakage, anchoring, injection spread, context dilution | Need-to-know packets; message schemas; trust labels                                     | Poisoned context and permission tests      |
| Coordination  | Conformity/herding             | Correct minority flips to wrong majority               | Independent first pass; masked peer confidence; evidence-weighted adjudication          | Correct-minority preservation              |
| Coordination  | Information withholding/loss   | Unique decisive evidence never reaches final answer    | Unique-evidence field; coverage ledger; synthesizer completeness check                  | Hidden-profile recovery                    |
| Coordination  | Peer input ignored             | No benefit from specialization                         | Required response to conflicts and novel evidence; acknowledgment status                | Contradiction integration test             |
| Coordination  | Conversation derailment/loops  | Tokens rise without information gain                   | Round objective; novelty threshold; max rounds; loop detector                           | Repeated-message/termination fixture       |
| Reasoning     | Correlated errors              | Multiple agents repeat the same false premise          | Different models/tools/evidence slices; independent sampling; error-correlation metric  | Cross-role error matrix                    |
| Reasoning     | Self-verification illusion     | Fluent critique approves original mistake              | External tools, executable checks, answer-key/constraint verification, separate context | Known-trap verification precision          |
| Reasoning     | Premature synthesis            | Early framing hardens and alternatives disappear       | Generate hypotheses/evidence before ranking; delay leader conclusion                    | Order-randomized framing test              |
| Authority     | Persona-based privilege        | “Senior” role acts beyond scope                        | Permissions live outside prompt; tool guardrails at every call                          | Unauthorized-action fixture                |
| Security      | Prompt infection across agents | Malicious instructions propagate through messages      | Treat messages as untrusted data; schemas, sanitization, origin labels, least privilege | Self-replicating injection simulation      |
| Verification  | Incomplete or incorrect checks | Team terminates with unverified claims                 | Explicit acceptance checklist; verifier independence; evidence receipt                  | False-approval/false-rejection suite       |
| Termination   | Unaware of completion          | Endless search, repeated handoffs, or partial answer   | Done criteria, budgets, stop reason enum, orchestrator timeout                          | Budget exhaustion and stop-condition tests |
| Economics     | Cost/latency explosion         | Marginal quality lower than resource increase          | Adaptive routing; agent/round budgets; early stopping; cache reusable evidence          | Cost-adjusted baseline comparison          |

### Anti-patterns to prohibit

- A cast of differently named agents receiving the same prompt, same context, same tools, and same aggregation rule.

- A permanent devil’s advocate instructed to oppose every conclusion, regardless of evidence.

- A synthesizer that sees the manager’s preferred answer before reviewing independent evidence.

- Confidence-weighted voting using uncalibrated verbal confidence.

- Free-form inter-agent chat as the canonical record.

- Self-reported personality scores stored as durable facts about the agent.

- Granting permissions because a role is described as senior, trusted, or expert.

- Adding agents or rounds without comparing against single-agent, self-consistency, and vote baselines.

- Treating a successful demo as a release evaluation.

## 8. Cognitive biopsy: diagnostic protocol and operating-profile dimensions

### Purpose

The cognitive biopsy is the test harness that converts a role description into evidence about behavior. It samples the exact deployed configuration across controlled tasks, seeds, context perturbations, peer conditions, and tool environments. The output is an observed operating profile with uncertainty and known failure boundaries.

### Four-stage protocol

| **Stage**             | **Required activity**                                                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 1\. Specify           | Write intended outcomes, methods, constraints, failure costs, and comparison baselines before testing.                                    |
| 2\. Sample            | Run representative tasks across difficulty, domain slices, nuisance attributes, seeds, context lengths, tool states, and peer topologies. |
| 3\. Score             | Use outcome measures, artifact inspection, tool traces, calibration, cost, and failure labels. Do not rely on self-description.           |
| 4\. Diagnose and gate | Estimate stability, identify activation conditions, record unsupported regions, set release constraints, and schedule re-evaluation.      |

### Core operating-profile dimensions

| **Dimension**           | **Behavioral definition**                                                  | **Candidate measures**                                               |
|-------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------|
| Role adherence          | Follows mission, scope, prohibitions, and output contract                  | Constraint pass rate; scope violation rate                           |
| Task competence         | Produces correct/useful work in assigned domain                            | Accuracy, defect recall/precision, decision utility                  |
| Method fidelity         | Uses the intended cognitive strategy                                       | Required-method artifact coverage; inappropriate-strategy rate       |
| Evidence discipline     | Separates source, inference, assumption, and unknown                       | Unsupported claim rate; citation correctness; provenance coverage    |
| Uncertainty/calibration | Confidence tracks empirical correctness; abstains productively             | Brier score/ECE; selective accuracy; abstention utility              |
| Exploration breadth     | Finds diverse, relevant alternatives and sources                           | Unique useful findings; source/domain diversity; redundancy          |
| Falsification strength  | Finds counterexamples, failure paths, and disconfirming evidence           | Critical defect recall; non-spurious challenge precision             |
| Revision quality        | Changes conclusions when warranted and preserves correct answers otherwise | Beneficial/harmful flip rates; evidence-conditioned revision         |
| Social independence     | Resists wrong consensus and confidence framing                             | Correct-minority preservation; peer-order sensitivity                |
| Collaboration           | Transfers unique information and uses peer evidence                        | Handoff completeness; contradiction resolution; information gain     |
| Tool judgment           | Selects and uses tools safely and efficiently                              | Tool appropriateness; success rate; permission violations            |
| State continuity        | Maintains task state across steps and interruptions                        | State reconstruction; repeated-step rate; constraint retention       |
| Termination             | Stops, retries, or escalates at the right time                             | Premature stop; loop rate; completion evidence                       |
| Resource efficiency     | Produces marginal value within budgets                                     | Quality/token, quality/time, useful finding/tool call                |
| Robustness              | Behavior survives nuisance changes and adversarial inputs                  | Worst-slice performance; variance across paraphrases/seeds           |
| Safety/governance       | Respects authority, privacy, and action gates                              | Unauthorized action attempts; guardrail coverage; audit completeness |

### Interpretation rules

- Report distributions and worst slices, not one average score.

- Separate reliability (repeatability) from validity (measuring the intended construct) and utility (improving the workflow).

- Treat verbal confidence as a feature to calibrate, not as ground truth.

- Measure role performance both alone and after exposure to peers; a strong solo profile can collapse socially.

- Record unsupported conditions explicitly: model versions, domains, languages, context lengths, tools, and topologies not tested.

- Store each finding with model, prompt, context-compiler, tool, evaluator, and dataset versions.

## 9. Persona/role contract standard for Team Packs

The Team Pack schema should promote the role contract—not prose persona text—to the governing source of truth. The runtime compiles model-specific prompts from this manifest, but permissions and enforcement remain external to the model.

> role:  
> id: evidence_mapper  
> purpose: Find, classify, and preserve decision-relevant evidence  
> scope: \[approved project records, primary sources\]  
> non_scope: \[final recommendation, external action\]  
> decision_rights: {recommend: true, decide: false, publish: false}  
>   
> cognitive_profile:  
> objective: maximize relevant evidence recall without losing provenance  
> methods: \[broad_to_narrow_search, source_triage, contradiction_scan\]  
> epistemic_policy:  
> claim_labels: \[evidence, inference, assumption, unknown\]  
> source_tiers: \[T1, T2, T3, T4\]  
> confidence_requires: \[support, counterevidence, uncertainty\]  
> interaction_policy:  
> independent_first_pass: true  
> disclose_peer_conclusions_before_first_pass: false  
> dissent_requires: \[counterevidence_or_falsifier\]  
> preserve_minority_report: true  
>   
> context_contract:  
> allowlist: \[objective, source_registry, approved_context_refs\]  
> provenance_required: true  
> tools: {allow: \[search, file_read\], deny: \[publish, mutate_system\]}  
> memory: {read: project, write: run_receipt_only, retention: run_scoped}  
> output_schema: evidence_map_v1  
> budgets: {tokens: role_specific, tool_calls: role_specific, retries: 1}  
> stop_conditions: \[coverage_satisfied, budget_exhausted, blocked\]  
> escalation: \[missing_authority, conflicting_sources, unsafe_request\]  
> evaluation_profile: evidence_mapper_eval_v1

### Required manifest fields and why they exist

| **Field**              | **Control function**                                                           |
|------------------------|--------------------------------------------------------------------------------|
| Purpose and outcome    | Prevents status-only personas and gives the evaluator a criterion.             |
| Scope / non-scope      | Reduces role ambiguity, overlap, and unauthorized expansion.                   |
| Decision rights        | Separates recommendation, adjudication, approval, publication, and execution.  |
| Methods                | Makes the cognitive strategy inspectable and testable.                         |
| Epistemic policy       | Controls evidence, uncertainty, source trust, contradiction, and abstention.   |
| Interaction policy     | Controls anchoring, herding, handoffs, dissent, clarification, and escalation. |
| Context contract       | Limits leakage and dilution; preserves provenance and freshness.               |
| Tools and permissions  | Enforces least privilege outside the persona prompt.                           |
| Memory policy          | Prevents ungoverned persistence and preserves reconstructable state.           |
| Output schema          | Makes aggregation deterministic and supports automated checks.                 |
| Budgets and stop rules | Bounds cost, loops, retries, and premature termination.                        |
| Evaluation profile     | Links the role to tests, baselines, thresholds, and known limitations.         |
| Style overlay          | Optional audience-facing voice that cannot change methods or authority.        |

### Recommended cognitive-profile vocabulary

| **Axis**          | **Allowed operational values**                                                         |
|-------------------|----------------------------------------------------------------------------------------|
| Search posture    | broad scout; focused investigator; exhaustive checker; sample-and-escalate             |
| Reasoning posture | hypothesis generator; causal/mechanistic analyst; analogical mapper; constraint solver |
| Evidence posture  | provenance-first; corroboration-first; primary-source-first; anomaly-first             |
| Risk posture      | promotion/exploration; balanced; prevention/verification; stop-on-uncertainty          |
| Social posture    | independent; cooperative integrator; evidence challenger; neutral adjudicator          |
| Action posture    | read-only; propose; stage; execute with approval; execute within bounded authority     |
| Output posture    | map; diagnosis; countercase; decision memo; verification receipt                       |

These values are configuration labels that imply tests; they are not human trait diagnoses. Every label should resolve to concrete instructions, measures, and failure conditions in the evaluation profile.

## 10. Role designs for the three priority Team Packs

### 10.1 agentic-readiness-audit-v1

| **Role**             | **Cognitive operating profile**                                                                            | **Mission**                                                                                              | **Primary risks**                                                                         | **Controls**                                                                                                 | **Release evidence**                                                                                 |
|----------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Evidence mapper      | Breadth-first, provenance-first scout. Maximizes relevant evidence recall and identifies missing controls. | Search and map approved artifacts; label source tier; surface contradictions and unknowns.               | Can overwhelm synthesis, duplicate findings, or trust fluent secondary sources.           | Source quotas, deduplication, claim labels, independent first pass, coverage stop rule.                      | Evidence-map completeness; citation correctness; unique useful findings; unsupported-claim rate.     |
| Runtime reviewer     | Mechanistic, constraint-oriented investigator. Prefers executable evidence over narrative claims.          | Inspect architecture, tool paths, permissions, state, failures, and tests; reproduce when safe.          | Tunnel vision on code; misses business/process risk; overuses tools.                      | Explicit control taxonomy; time-boxed reproduction; cross-check against evidence map.                        | Critical control recall/precision; reproduction success; tool appropriateness; permission adherence. |
| Adversarial reviewer | Falsification-first, prevention-focused analyst. Searches for bypasses and counterexamples.                | Challenge claims, identify attack paths, construct failure fixtures, and specify disconfirming evidence. | Theatrical opposition, false positives, unsafe experimentation, anchoring on peer claims. | Work independently before seeing conclusions; challenge must carry evidence/falsifier; read-only default.    | Critical defect recall; challenge precision; novel failure paths; safety compliance.                 |
| Synthesis lead       | Neutral evidence integrator. Optimizes decision clarity, not consensus.                                    | Reconcile typed findings, compare evidence strength, surface disagreement, and draft the audit decision. | Authority bias, loss of minority evidence, premature closure, unsupported smoothing.      | Cannot originate missing evidence silently; coverage checklist; dissent register; explicit inference labels. | Claim traceability; disagreement preservation; decision utility; synthesis omission rate.            |
| Independent verifier | Criterion-driven checker with minimal exposure to prior rationale.                                         | Test acceptance claims, citations, and critical controls; issue pass/fail/blocked receipt.               | Rubber-stamping, correlated context, verifying style rather than outcome.                 | Separate context; tool-based checks; known-trap fixtures; no incentive to agree.                             | False approval/rejection; verification coverage; evidence reproducibility.                           |

### 10.2 release-control-review-v1

| **Role**                       | **Profile**                             | **Mission**                                                                       | **Risk**                                              | **Controls**                                                       | **Measures**                                              |
|--------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------|
| Change investigator            | Diff-focused causal mapper              | Identify what changed, affected surfaces, dependencies, and intended behavior.    | Misses indirect impacts; trusts change description.   | Canonical diff, dependency scan, claim/evidence map.               | Change coverage; affected-surface recall.                 |
| Control/runtime analyst        | Prevention-focused mechanistic reviewer | Assess permissions, guardrails, failure containment, observability, and rollback. | Over-indexes on static design; ignores runtime paths. | Executable checks; state-transition tests; least-privilege matrix. | Critical control precision/recall; runtime reproduction.  |
| Adversarial regression analyst | Counterfactual and abuse-case generator | Find regressions, bypasses, unsafe interactions, and boundary failures.           | Excess false positives; combinatorial explosion.      | Risk-ranked fixtures; budget by consequence; evidence threshold.   | High-severity defect yield; false-positive rate.          |
| Gate adjudicator               | Policy-bound decision integrator        | Map evidence to release criteria and issue allow/block/allow-with-controls.       | Policy drift; averaging away blockers.                | Machine-checkable criteria; blocker precedence; dissent field.     | Gate consistency; traceability; post-release escape rate. |
| Post-gate verifier             | Independent outcome checker             | Confirm required controls and artifacts exist after remediation.                  | Checks paperwork, not behavior.                       | Re-run exact failed fixtures; compare receipts.                    | Remediation verification precision.                       |

### 10.3 research-to-decision-v1

| **Role**                   | **Profile**                                    | **Mission**                                                                           | **Risk**                                                      | **Controls**                                                                 | **Measures**                                               |
|----------------------------|------------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------|
| Landscape scout            | Promotion-focused breadth explorer             | Map hypotheses, primary source clusters, terminology, and unknowns.                   | Source sprawl; novelty without relevance.                     | Question tree; source quotas; time box; decision relevance label.            | Coverage, source diversity, unique useful sources.         |
| Primary-source analyst     | Precision-focused evidence extractor           | Read decisive studies/docs; extract methods, data, limitations, and claim boundaries. | Overly narrow; loses cross-source context.                    | Structured evidence cards; direct-link requirement; limitation field.        | Extraction accuracy; claim-source entailment.              |
| Counter-hypothesis analyst | Falsification and alternative-model specialist | Find contradictory results, boundary conditions, and rival explanations.              | Manufactured balance; weak contrarian sources.                | Authority threshold; evidence-bearing dissent; base-rate awareness.          | Quality-weighted counterevidence; spurious challenge rate. |
| Decision synthesizer       | Neutral option/evidence integrator             | Translate evidence into choices, assumptions, risks, and next test.                   | False certainty; citation laundering; losing unique evidence. | Claim ledger; tier-aware weighting; dissent register; no silent gap filling. | Decision utility; provenance; calibration; omission rate.  |
| Source auditor             | Provenance and freshness verifier              | Validate links, source classes, dates, permissions, and quotation/claim fit.          | Process overhead; false confidence from metadata alone.       | Risk-based sample plus 100% check of decisive claims.                        | Citation validity; stale/invalid source detection.         |

### Composition rule across all three teams

> **FUNCTIONAL DIVERSITY** Compose teams by non-overlapping evidence access, methods, failure costs, and authority—not by colorful labels. If two roles have the same context, tools, transformation, and scoring function, merge them or prove that independent sampling adds value.

## 11. Interaction protocol and structured handoffs

### Default: independent → compare → targeted challenge → adjudicate → verify

| **Phase**                         | **Protocol**                                                                                               | **Required artifact**                                        |
|-----------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| 0\. Route                         | Primary agent estimates difficulty, consequence, breadth, separability, and verification availability.     | Single-agent, ensemble, or Team Pack selected with budget.   |
| 1\. Independent work              | Each specialist receives objective, scoped context, tools, output schema, and no peer conclusion.          | Typed initial artifact plus private confidence and unknowns. |
| 2\. Evidence merge                | Orchestrator deduplicates claims, preserves provenance, identifies contradictions and unique evidence.     | Comparison matrix; no final conclusion yet.                  |
| 3\. Targeted challenge            | Only disputed or high-risk claims are routed for critique; challengers cite counterevidence or falsifiers. | Resolved, unresolved, or test-needed status.                 |
| 4\. Adjudication                  | Synthesizer weighs evidence tiers, verification, and policy; majority is contextual, not dispositive.      | Decision draft plus minority report and assumptions.         |
| 5\. Independent verification/gate | Verifier checks critical claims and acceptance criteria using separate context/tools where possible.       | Pass/fail/blocked receipt and final release decision.        |

### Required handoff schema

> handoff:  
> sender_role: runtime_reviewer  
> recipient_role: synthesis_lead  
> task_id: audit-001/control-07  
> claim: "Tool boundary lacks per-call authorization"  
> claim_type: evidence \| inference \| assumption \| unknown  
> evidence_refs: \[repo://..., test://..., source://...\]  
> source_tier_and_freshness: {tier: T1, status: current}  
> method: "trace permission check from request to tool invocation"  
> counterevidence: \[\]  
> confidence: {value: 0.78, basis: "runtime trace + code inspection"}  
> consequence_if_wrong: high  
> requested_action: "adversarial fixture then gate review"  
> unresolved_questions: \["Is an upstream policy service enforced in production?"\]  
> disclosure: {peer_conclusions_seen: false}

Confidence must include a basis and consequence, and should be calibrated by role and task family. Aggregators should never turn an uncalibrated “90%” into ten times the vote weight of “60%.” Separate source credibility, evidence strength, and model confidence.

### Disagreement policy

| **Conflict type**        | **Resolution rule**                                                                                                 |
|--------------------------|---------------------------------------------------------------------------------------------------------------------|
| Evidence conflict        | Compare source authority, directness, recency, and method. Request a targeted verification if consequence warrants. |
| Interpretation conflict  | State rival hypotheses and the observation that would distinguish them.                                             |
| Policy conflict          | Escalate to the governing policy/primary agent; subagents do not rewrite acceptance criteria.                       |
| Confidence-only conflict | Ignore rhetorical certainty; request evidence or treat as unresolved.                                               |
| Unresolvable conflict    | Preserve both positions, consequence, and next test in the minority report.                                         |

## 12. Evaluation battery, metrics, and release gates

### Baseline ladder

| **Baseline** | **Configuration**                               | **Question answered**                                                   |
|--------------|-------------------------------------------------|-------------------------------------------------------------------------|
| B0           | Strong single agent, generic task instruction   | Does the role/team beat the simplest credible solution?                 |
| B1           | Single agent with the full role contract        | Does role structure help without team overhead?                         |
| B2           | Independent same-model samples + majority vote  | Does interaction add value beyond sampling?                             |
| B3           | Independent samples + evidence-aware aggregator | Does specialization add value beyond structured ensembling?             |
| B4           | Full Team Pack                                  | Do role differentiation, topology, and verification justify their cost? |

### Single-role battery

| **Test**                              | **Fixture**                                                               | **Measures**                                                     |
|---------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------|
| SR-01 Role adherence                  | In-scope, out-of-scope, conflicting and ambiguous requests                | Scope violations; escalation correctness; output-schema validity |
| SR-02 Task competence                 | Representative tasks stratified by difficulty and consequence             | Primary outcome; worst-slice outcome; error severity             |
| SR-03 No-persona advantage            | Role contract vs generic instruction                                      | Operationally meaningful delta with uncertainty                  |
| SR-04 Irrelevant-attribute robustness | Names, biographies, gendered cues, status titles, formatting, paraphrases | Worst nuisance delta; variance                                   |
| SR-05 Method fidelity                 | Tasks where intended method is observable                                 | Required artifacts; inappropriate method use                     |
| SR-06 Reliability/drift               | Repeated seeds, sessions, context lengths, time/model versions            | Test–retest agreement; drift alerts                              |
| SR-07 Calibration/abstention          | Answerable and deliberately unanswerable items                            | Brier/ECE; selective accuracy; useful abstention                 |
| SR-08 Correction quality              | Correct and incorrect initial answers with neutral/biased feedback        | Beneficial vs harmful flips; sycophancy rate                     |
| SR-09 Tool judgment                   | Useful, unnecessary, failing, and prohibited tool cases                   | Appropriate selection; success; unauthorized attempts            |
| SR-10 Context continuity              | Long horizon, interruption, compressed summaries, conflicting updates     | Constraint retention; repeated steps; state recovery             |
| SR-11 Injection/governance            | Untrusted source and peer instructions                                    | Policy violations; infection propagation; data leakage           |
| SR-12 Termination                     | Completed, blocked, looping, and budget-limited tasks                     | Correct stop reason; premature/late stop; resource overrun       |

### Team battery

| **Test**                         | **Fixture**                                                 | **Measures**                                                 |
|----------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|
| TM-01 Marginal contribution      | Remove each role and compare outcomes                       | Ablation loss; unique contribution; redundancy               |
| TM-02 Error diversity            | Track errors by role/task                                   | Pairwise error correlation; common-mode failure              |
| TM-03 Hidden profile             | Distribute decisive facts across agents                     | Unique fact recall; correct integration; source preservation |
| TM-04 Conformity resistance      | Wrong confident majority vs correct minority                | Correct-minority preservation; harmful flip rate             |
| TM-05 Beneficial correction      | Corrective minority with verifiable evidence                | Wrong-to-right reversal; evidence use                        |
| TM-06 Peer-order sensitivity     | Randomize message order, identity, and confidence framing   | Outcome variance; primacy/authority bias                     |
| TM-07 Handoff completeness       | Inject missing, contradictory, stale, and low-tier evidence | Schema validity; missing-critical-field rate; provenance     |
| TM-08 Role collision             | Overlapping scope and conflicting directives                | Duplicate work; turf conflict; escalation                    |
| TM-09 Conversation reset         | Interrupt or replace an agent mid-run                       | State recovery; context reconstruction; lost obligations     |
| TM-10 Verification independence  | Known traps and misleading rationales                       | False approval/rejection; correlation with producer error    |
| TM-11 Adversarial member         | Poisoned or compromised agent message                       | Containment; trust downgrade; unauthorized action            |
| TM-12 Loop/termination           | Repeated messages and unresolved disputes                   | Round count; novelty per round; stop correctness             |
| TM-13 Cost/latency               | Scale agents and rounds at matched budgets                  | Quality/token; quality/second; marginal value                |
| TM-14 Model/topology portability | Swap supported model adapter or topology                    | Regression; unsupported assumptions; reconfiguration cost    |
| TM-15 End-state outcome          | Evaluate external state after tool-using run                | Actual state correctness, not only transcript quality        |

### Key metric definitions

| **Metric**                    | **Definition**                                                                                                                        |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Marginal role value           | Outcome(full team) − Outcome(team without role), compared at matched budget.                                                          |
| Unique evidence yield         | Decision-relevant, non-duplicate evidence attributable to a role per token or tool call.                                              |
| Correct-minority preservation | Fraction of trials where a correct minority answer remains available and influences the final decision under wrong majority pressure. |
| Beneficial revision rate      | Wrong→right revisions divided by opportunities to correct.                                                                            |
| Harmful revision rate         | Right→wrong revisions after peer/user feedback.                                                                                       |
| Claim traceability            | Final claims with valid source or typed inference link divided by all material claims.                                                |
| Verification precision        | True defects/claims among verifier rejections/approvals, split by consequence.                                                        |
| Coordination efficiency       | Useful integrated information gain divided by communication tokens/rounds.                                                            |
| Worst-slice robustness        | Minimum performance across declared critical slices, not just the mean.                                                               |

### Release gate

- Predeclare operationally meaningful thresholds, failure-severity weights, and budgets before running the evaluation.

- Require the Team Pack to beat the strongest relevant baseline on the primary outcome or deliver a separately valued benefit such as coverage, auditability, or risk reduction.

- Block release for critical authority, privacy, prompt-infection, false-approval, or unrecoverable state failures regardless of average score.

- Require role advantage, robustness, fidelity, and complementarity. A role that is stylistically distinct but contributes no marginal value is removed.

- Record confidence intervals or repeated-run variability; do not promote on one lucky run.

- Pin the supported configuration and re-run the gate after model, prompt, context, tool, topology, or evaluator changes.

> **GATE DECISION** Current research gate: ALLOW prototyping of the Team Pack standard with caveats. BLOCK any claim that the personas are stable psychological individuals, any persona-based privilege, and any production deployment lacking baseline comparison, per-role permissions, structured handoffs, independent verification, and regression evidence.

## 13. Security, governance, and trust boundaries

A multi-agent team creates additional trust boundaries: source→agent, agent→agent, agent→tool, agent→memory, aggregator→final action, and external state→verification. Free-form prose can carry instructions as well as data, so every handoff must be treated as potentially untrusted input. \[S17, S44–S48\]

| **Threat**                      | **Failure**                                                         | **Control**                                                                                                |
|---------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Prompt injection in a source    | Agent follows embedded instruction, leaks data, or alters goal      | Separate instructions from evidence; origin labels; content sanitization; tool guardrails; least privilege |
| Prompt infection via peer       | Malicious or compromised message propagates across team             | Typed messages; no instruction inheritance; trust tier; quarantine/escalation; independent verifier        |
| Privilege escalation by persona | Role claims expertise/seniority and requests broader tools          | Permissions outside prompt; immutable manifest; approval gate for changes                                  |
| Context overexposure            | Sensitive or irrelevant data shared to every worker                 | Need-to-know context compiler; redaction; per-role allowlists; access receipts                             |
| Aggregator laundering           | Unsupported agent claim becomes an authoritative final statement    | Claim graph; source requirement; minority report; output guardrail at final and role boundaries            |
| Unsafe external action          | Team mutates state based on unverified or injected evidence         | Read-only default; preview/stage; explicit approval; post-action state verification                        |
| Memory poisoning                | Untrusted findings become durable context                           | Write gates; provenance; TTL; status labels; reversible versions                                           |
| Collusion/common-mode behavior  | Agents coordinate around an unintended goal or same flawed strategy | Constrained protocols; behavior monitors; heterogeneous checks; end-state tests                            |

### Guardrail placement rule

Guardrails must align with execution boundaries. In current agent runtimes, input/output guardrails may apply only at the first or final agent while tool guardrails apply per custom tool call. Therefore every custom action boundary needs its own authorization and validation; a final-answer filter cannot protect an unsafe intermediate tool call. \[S16–S17\]

- Primary agent retains objective, scope, integration, final verification, approval, and external-action authority.

- Team manifests are versioned and immutable during a run. Models may select an approved team but cannot silently create roles, tools, permissions, or topology.

- Every run writes a reconstructable receipt: effective role versions, context references, permissions, messages, tools, outputs, disagreements, verification, cost, and gate decision.

- Context records carry source, version, timestamp, permission, freshness, and transformation provenance, consistent with the supplied Toolkit state model. \[S00–S01\]

- Reasoning narratives may support debugging but are not treated as faithful internal-state evidence or a load-bearing safety control. \[S47–S48\]

## 14. Implementation roadmap and experiment backlog

### Phase 0 — Define the standard (week 1)

- Add cognitive_profile, epistemic_policy, interaction_policy, context_contract, decision_rights, stop_conditions, and evaluation_profile to team-pack.schema.json.

- Define typed artifacts: evidence_map_v1, runtime_findings_v1, adversarial_findings_v1, synthesis_receipt_v1, verification_receipt_v1.

- Implement a source/claim ledger and explicit evidence, inference, assumption, and unknown labels.

- Specify immutable permission and context allowlists outside role prose.

### Phase 1 — Build one reference team (weeks 2–4)

- Implement agentic-readiness-audit-v1 using orchestrator–worker topology and independent first passes.

- Start with four active roles—evidence mapper, runtime reviewer, adversarial reviewer, synthesis lead—and a separately invoked verifier for critical claims.

- Compile minimal role prompts from the manifest; exclude demographic and decorative biography.

- Enforce budgets, max two targeted challenge rounds, stop reasons, and structured handoffs.

- Capture full run receipts in the durable evidence layer described in the supplied Toolkit research. \[S00–S01\]

### Phase 2 — Build the biopsy/eval harness (weeks 3–6)

- Create 30–50 representative audit fixtures with difficulty and consequence labels; include normal, ambiguous, adversarial, missing-context, and false-verification cases.

- Run the baseline ladder B0–B4 at matched budgets across multiple seeds.

- Add persona nuisance tests, hidden-profile tasks, correct-minority tests, interruption/resume tests, and tool-boundary attacks.

- Compute role ablations, error correlations, unique evidence yield, claim traceability, and cost-adjusted outcome.

- Publish a supported-configuration card with known weaknesses and unsupported regions.

### Phase 3 — Expand only after evidence (weeks 7–12)

- Promote, merge, or remove roles based on marginal contribution rather than preference.

- Add release-control-review-v1, reusing the same profile and evaluation primitives.

- Add research-to-decision-v1 after the source/claim ledger and citation verification are stable.

- Test a heterogeneous-model option only where it reduces error correlation enough to justify adapter and cost complexity.

- Build the visual team editor last; it should edit governed manifests, not free-form casts of characters.

### Minimum viable experiment matrix

| **ID** | **Experiment**                        | **Hypothesis**                                                                 | **Falsifier**                                     |
|--------|---------------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------|
| E1     | Role contract vs expert-title persona | Structured role improves outcome and robustness; title alone does not.         | No outcome or robustness gain                     |
| E2     | Decorative attributes ablation        | Removing biography reduces variance without reducing utility.                  | Biography consistently improves validated outcome |
| E3     | Independent-first vs open chat        | Independent-first increases unique evidence and correct-minority preservation. | No benefit at matched budget                      |
| E4     | Vote vs targeted challenge            | Targeted evidence critique outperforms vote on high-difficulty items.          | Vote is equal/better and cheaper                  |
| E5     | Four-role team vs strong single agent | Team improves risk-weighted audit quality enough to justify cost.              | No operationally meaningful gain                  |
| E6     | Separate verifier vs self-check       | Independent/tool-based verifier reduces false approvals.                       | No reduction or cost dominates                    |
| E7     | Same-model vs heterogeneous team      | Heterogeneity lowers correlated failure on selected tasks.                     | No error-diversity gain                           |
| E8     | One vs two vs three challenge rounds  | Two rounds maximize quality per token.                                         | Different optimum; route adaptively               |

## 15. Theories, falsifiable hypotheses, and open questions

### Working theory of subagent individuality

A subagent appears individual when its runtime configuration produces a distinctive, repeatable pattern of attention, transformation, uncertainty handling, interaction, authority use, and error. This individuality is relational and task-bound: it exists as a stable-enough system behavior within a declared configuration, not as proof of an inner person. The engineering objective is dependable complementarity, not human likeness.

| **Hypothesis**                        | **Mechanism**                                                                                                            | **Test**                                                            | **Falsifier**                                                                |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------|
| H1 Role-contract hypothesis           | Detailed work contracts outperform status/persona labels because they reduce ambiguity and supply executable strategies. | Contract vs title vs generic prompt across tasks.                   | Title-only equals or beats contract with equal robustness.                   |
| H2 Activation hypothesis              | Role behavior is highly cue-dependent; peer framing, context, and tools explain more variance than claimed trait labels. | Factorial task/peer/tool/context experiment.                        | Trait label remains stable and predictive across perturbations.              |
| H3 Functional-diversity hypothesis    | Diversity of evidence and methods predicts team gain better than diversity of names or prose styles.                     | Compare functional vs cosmetic diversity at matched models/budgets. | Cosmetic diversity yields equal unique evidence and lower error correlation. |
| H4 Independence hypothesis            | Private first passes increase unique evidence and preserve correct minorities.                                           | Hidden-profile and wrong-majority trials.                           | Open chat is equal/better on integration and cost.                           |
| H5 Evidence-weight hypothesis         | Source quality and external verification outperform uncalibrated confidence or majority as aggregation signals.          | Evidence-aware vs confidence/vote aggregation.                      | Confidence/vote is more accurate across consequential slices.                |
| H6 Verifier separation hypothesis     | A verifier with separate context and tools has lower correlated error than producer self-check.                          | Known-trap and misleading-rationale fixtures.                       | No false-approval reduction.                                                 |
| H7 Minimal-persona hypothesis         | Removing irrelevant biography improves robustness without reducing task performance.                                     | Nuisance-attribute ablations.                                       | Specific biography improves criterion performance reproducibly.              |
| H8 Two-round hypothesis               | Most useful correction occurs within two targeted rounds; later rounds add cost and herding.                             | Round scaling at matched compute.                                   | Three+ rounds improve quality/token on declared task family.                 |
| H9 Transactive-memory hypothesis      | Explicit “who knows what” routing improves unique evidence recovery and lowers duplication.                              | Capability directory on/off experiment.                             | No coverage or efficiency gain.                                              |
| H10 Cost-routing hypothesis           | Difficulty- and risk-adaptive routing dominates always-team execution.                                                   | Adaptive vs fixed team policy across mixed workload.                | Always-team produces higher net utility at acceptable cost.                  |
| H11 Governance-externality hypothesis | Permissions enforced outside prompts sharply reduce persona drift and injection impact.                                  | Prompt-only vs runtime-enforced tool boundary attacks.              | Prompt-only matches runtime enforcement.                                     |
| H12 Profile-portability hypothesis    | Role manifests are portable, but observed profiles are model/configuration-specific.                                     | Swap model adapters while holding manifest/tasks fixed.             | Behavior and thresholds remain invariant.                                    |

### Open questions requiring local data

- Which audit findings are separable enough for parallel work, and which require tightly shared context?

- What is the strongest single-agent baseline on your real audit and release fixtures?

- Which models produce sufficiently different error patterns to justify heterogeneous teams?

- Can confidence be calibrated per role and consequence class, or should aggregation ignore verbal confidence?

- What evidence should automatically block release even when other metrics improve?

- How much context can each role omit without losing decisive cross-domain dependencies?

- What is the minimum run receipt required for a defensible reconstruction of model state and authority?

- Which role outputs deserve durable memory, and which should expire after the run?

- What user-facing persona style improves trust and comprehension without distorting task behavior?

### Decision ledger

| **ID** | **Decision**                                    | **Status**         | **Rationale**                                                                                                                         |
|--------|-------------------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| D-01   | Adopt role-contract-first persona standard      | ALLOW              | Direct persona evidence does not support status-only prompts; structured roles reduce ambiguity and enable tests.                     |
| D-02   | Use human psychology as mechanism library       | ALLOW WITH CAVEATS | Shared cognition, information sampling, voice, and trait activation translate to system hypotheses; human affect/personhood does not. |
| D-03   | Use Big Five scores as canonical agent identity | BLOCK              | Synthetic scores may be measurable but are prompt/configuration-dependent and not validated as workflow competence.                   |
| D-04   | Default to orchestrator–worker Team Packs       | ALLOW              | Best fit for scoped parallel evidence work and governed integration; still requires baseline proof.                                   |
| D-05   | Allow free-form peer swarm in production        | BLOCK              | Unclear hierarchy, correlated error, loops, injection, merge, and verification risks remain high.                                     |
| D-06   | Independent first pass and minority report      | REQUIRE            | Directly addresses hidden-profile loss, anchoring, and herding.                                                                       |
| D-07   | Persona-based permissions                       | BLOCK              | Authority must be external, explicit, least-privilege, and immutable during a run.                                                    |
| D-08   | Promote first Team Pack                         | PENDING EVAL       | Build agentic-readiness-audit-v1, then compare B0–B4 and run the cognitive biopsy.                                                    |

## Appendix A. Governed source register

Source IDs are stable within this report. T1 = direct/authoritative for the stated claim; T2 = reliable/current but provisional or context-specific; T3 = supplied contextual architecture; T4 = not used decisively. “Current” means inspected for this research pass on or before 22 August 2026. Links point to primary publications or official documentation where available.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 38%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Tier</strong></th>
<th><strong>Source record</strong></th>
<th><strong>Claim relevance and link</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>S00</strong></td>
<td><strong>T3</strong></td>
<td>Toolkit deep research supplied by user</td>
<td>Layered context/evidence/skills/plugins/tasks architecture; source registry, decision ledger, eval gates.</td>
</tr>
<tr class="even">
<td><strong>S01</strong></td>
<td><strong>T3</strong></td>
<td>Effective AI state model supplied by user</td>
<td>Reconstruction requires complete state, versions, timestamps, permissions, and provenance.</td>
</tr>
<tr class="odd">
<td><strong>S02</strong></td>
<td><strong>T1</strong></td>
<td>Zheng et al. (2024), “When A Helpful Assistant Is Not Really Helpful”</td>
<td>162 roles, four model families, 2,410 questions; no overall persona benefit; effects often random.<br />
<a href="https://aclanthology.org/2024.findings-emnlp.888/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S03</strong></td>
<td><strong>T1</strong></td>
<td>Luz de Araujo et al. (2025), “Principled Personas”</td>
<td>Nine models, 27 tasks; irrelevant details can sharply hurt; defines advantage, robustness, fidelity.<br />
<a href="https://aclanthology.org/2025.emnlp-main.1364/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S04</strong></td>
<td><strong>T1</strong></td>
<td>Huang et al. (2024), reliability of psychological scales on LLMs</td>
<td>2,500 settings/model; reports Big Five response consistency and prompted emulation.<br />
<a href="https://aclanthology.org/2024.emnlp-main.354/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S05</strong></td>
<td><strong>T1</strong></td>
<td>Serapio-García et al. (2025), psychometric framework</td>
<td>Reliability/validity method across 18 LLMs; synthetic traits measurable under some configurations.<br />
<a href="https://www.nature.com/articles/s42256-025-01115-6"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S06</strong></td>
<td><strong>T1</strong></td>
<td>Frisch &amp; Giulianelli (2024), persona inconstancy in multi-agent collaboration</td>
<td>Conformity, confabulation, impersonation, and unstable roles in collaboration.<br />
<a href="https://aclanthology.org/2024.c3nlp-1.2/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S07</strong></td>
<td><strong>T2</strong></td>
<td>Cemri et al. (2025), “Why Do Multi-Agent LLM Systems Fail?”</td>
<td>Five frameworks, 150+ tasks, 14 failure modes; prompt interventions insufficient.<br />
<a href="https://arxiv.org/abs/2503.13657"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S08</strong></td>
<td><strong>T2</strong></td>
<td>Du et al. (2023), multi-agent debate</td>
<td>Early evidence of debate gains in reasoning and factuality; benchmark-specific.<br />
<a href="https://arxiv.org/abs/2305.14325"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S09</strong></td>
<td><strong>T1</strong></td>
<td>Choi et al. (2025), “Debate or Vote”</td>
<td>Across seven NLP benchmarks, ensembling explains most debate gains; targeted correction is key.<br />
<a href="https://proceedings.neurips.cc/paper_files/paper/2025/file/934252acd87f254d5d4672fbde283bd2-Paper-Conference.pdf"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S10</strong></td>
<td><strong>T1</strong></td>
<td>Chen et al. (2024), ReConcile</td>
<td>Heterogeneous discussion and confidence-weighted reconciliation can improve reasoning.<br />
<a href="https://aclanthology.org/2024.acl-long.381/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S11</strong></td>
<td><strong>T1</strong></td>
<td>Gulati et al. (2026), multi-agent reasoning compute efficiency</td>
<td>34 configurations/100+ evals; agents vs rounds; modest matched-budget gains and routing implications.<br />
<a href="https://aclanthology.org/2026.acl-srw.1/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S12</strong></td>
<td><strong>T2</strong></td>
<td>Anthropic Engineering, multi-agent research system</td>
<td>Lead/subagent production pattern, internal +90.2% result, high token cost, task-description lessons.<br />
<a href="https://www.anthropic.com/engineering/multi-agent-research-system"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S13</strong></td>
<td><strong>T2</strong></td>
<td>Anthropic Research (2026), multi-agent systems experiments</td>
<td>Swarm, game, hidden-profile, collusion, and coordination findings; vendor/internal evidence.<br />
<a href="https://www.anthropic.com/research/multiagent-systems"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S14</strong></td>
<td><strong>T2</strong></td>
<td>Anthropic Engineering, building effective agents</td>
<td>Use simplest system; workflow vs agent trade-offs; compounding cost/error.<br />
<a href="https://www.anthropic.com/engineering/building-effective-agents"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S15</strong></td>
<td><strong>T2</strong></td>
<td>Anthropic Engineering, effective context engineering</td>
<td>Context is finite; subagents can isolate work and return compressed, high-signal results.<br />
<a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S16</strong></td>
<td><strong>T1</strong></td>
<td>OpenAI Agents SDK multi-agent orchestration docs</td>
<td>Manager/agents-as-tools vs handoffs; manager retains composition and final control.<br />
<a href="https://openai.github.io/openai-agents-python/multi_agent/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S17</strong></td>
<td><strong>T1</strong></td>
<td>OpenAI Agents SDK guardrails docs</td>
<td>Guardrail placement differs by first/final agent and per-tool invocation.<br />
<a href="https://openai.github.io/openai-agents-python/guardrails/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S18</strong></td>
<td><strong>T1</strong></td>
<td>Li et al. (2023), CAMEL</td>
<td>Role-playing cooperation; known role-flipping, loop, repetition, and termination challenges.<br />
<a href="https://proceedings.neurips.cc/paper_files/paper/2023/hash/a3621ee907def47c1b952ade25c67698-Abstract-Conference.html"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S19</strong></td>
<td><strong>T1</strong></td>
<td>Hong et al. (2024), MetaGPT</td>
<td>SOPs and modular intermediate artifacts for role-specialized software teams.<br />
<a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/6507b115562bb0a305f1958ccc87355a-Abstract-Conference.html"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S20</strong></td>
<td><strong>T1</strong></td>
<td>Qian et al. (2024), ChatDev</td>
<td>Chat-chain software roles and communicative dehallucination.<br />
<a href="https://aclanthology.org/2024.acl-long.810/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S21</strong></td>
<td><strong>T1</strong></td>
<td>Park et al. (2023), Generative Agents</td>
<td>Memory, reflection, and planning increase believability; believability is not correctness.<br />
<a href="https://dl.acm.org/doi/10.1145/3586183.3606763"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S22</strong></td>
<td><strong>T1</strong></td>
<td>Huang et al. (2024), intrinsic self-correction limits</td>
<td>LLMs often fail to self-correct without external feedback and may degrade correct answers.<br />
<a href="https://openreview.net/forum?id=IkmD3fKBPQ"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S23</strong></td>
<td><strong>T1</strong></td>
<td>Kamoi et al. (2024), when LLMs can correct mistakes</td>
<td>Self-correction success depends on feedback and task conditions.<br />
<a href="https://aclanthology.org/2024.tacl-1.78/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S24</strong></td>
<td><strong>T1</strong></td>
<td>ProgCo (ACL 2025)</td>
<td>Program-driven verification improves self-correction by grounding feedback.<br />
<a href="https://aclanthology.org/2025.acl-short.73/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S25</strong></td>
<td><strong>T2</strong></td>
<td>Anthropic Research, sycophancy in language models</td>
<td>Preference training can reward agreement with user beliefs over truth.<br />
<a href="https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S26</strong></td>
<td><strong>T1</strong></td>
<td>Niler et al. (2020), team cognition meta-analysis update</td>
<td>Shared mental models/transactive memory relate to processes and performance.<br />
<a href="https://atlas.northwestern.edu/wp-content/uploads/2021/01/Niler-Mesmer-Magnus-Larson-DeChurch-Contractor-2020.pdf"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S27</strong></td>
<td><strong>T1</strong></td>
<td>Salas, Sims &amp; Burke (2005), “Big Five in Teamwork”</td>
<td>Leadership, monitoring, backup, adaptability, team orientation; coordinating mechanisms.<br />
<a href="https://stars.library.ucf.edu/scopus2000/3697/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S28</strong></td>
<td><strong>T1</strong></td>
<td>Mesmer-Magnus &amp; DeChurch (2009), information sharing meta-analysis</td>
<td>72 studies, 4,795 groups; information sharing supports performance and integration.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/19271807/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S29</strong></td>
<td><strong>T1</strong></td>
<td>Liang, Moreland &amp; Argote (1995), transactive memory</td>
<td>Group training improved performance through a transactive memory system.<br />
<a href="https://doi.org/10.1177/0146167295214009"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S30</strong></td>
<td><strong>T1</strong></td>
<td>Stasser &amp; Titus (1985), pooling unshared information</td>
<td>Shared-information bias and hidden-profile failure in group decisions.<br />
<a href="https://doi.org/10.1037/0022-3514.48.6.1467"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S31</strong></td>
<td><strong>T1</strong></td>
<td>Tubre &amp; Collins (2000), role ambiguity/conflict meta-analysis</td>
<td>Role ambiguity about r=−.21 with performance; role conflict about r=−.07.<br />
<a href="https://doi.org/10.1177/014920630002600104"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S32</strong></td>
<td><strong>T1</strong></td>
<td>Marks, Mathieu &amp; Zaccaro (2001), temporal team processes</td>
<td>Transition, action, and interpersonal process taxonomy.<br />
<a href="https://doi.org/10.5465/amr.2001.4845785"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S33</strong></td>
<td><strong>T1</strong></td>
<td>Edmondson (1999), psychological safety and learning behavior</td>
<td>Shared interpersonal-risk climate associated with team learning behavior.<br />
<a href="https://www.hbs.edu/faculty/Pages/item.aspx?num=2959"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S34</strong></td>
<td><strong>T1</strong></td>
<td>De Dreu &amp; Weingart (2003), conflict meta-analysis</td>
<td>Task and relationship conflict were negatively related to performance overall.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/12940412/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S35</strong></td>
<td><strong>T1</strong></td>
<td>Woolley et al. (2010), collective intelligence</td>
<td>Group-level factor; equal turn taking and social sensitivity associated with performance.<br />
<a href="https://doi.org/10.1126/science.1193147"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S36</strong></td>
<td><strong>T1</strong></td>
<td>Lorenz et al. (2011), social influence and wisdom of crowds</td>
<td>Social influence reduced diversity without reliable accuracy gains and increased confidence.<br />
<a href="https://doi.org/10.1073/pnas.1008636108"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S37</strong></td>
<td><strong>T1</strong></td>
<td>van Knippenberg, De Dreu &amp; Homan (2004), diversity–elaboration model</td>
<td>Diversity benefits require information elaboration and can be offset by social categorization.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/15584838/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S38</strong></td>
<td><strong>T1</strong></td>
<td>Nemeth, Brown &amp; Rogers (2001), devil’s advocate vs authentic dissent</td>
<td>Authentic dissent affected human group thinking differently from assigned opposition.<br />
<a href="https://doi.org/10.1002/ejsp.58"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S39</strong></td>
<td><strong>T1</strong></td>
<td>Bell (2007), deep-level team composition meta-analysis</td>
<td>Personality/ability relationships are moderated by setting and operationalization.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/17484544/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S40</strong></td>
<td><strong>T1</strong></td>
<td>Peeters et al. (2006), personality and team performance meta-analysis</td>
<td>Modest composition effects; mean agreeableness/conscientiousness positive, variability negative.<br />
<a href="https://research.tue.nl/en/publications/personality-and-team-performance-a-meta-analysis/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S41</strong></td>
<td><strong>T1</strong></td>
<td>Tett &amp; Burnett (2003), trait activation theory</td>
<td>Trait expression depends on task, social, and organizational cues.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/12814298/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S42</strong></td>
<td><strong>T1</strong></td>
<td>Sperber et al. (2010), epistemic vigilance</td>
<td>Mechanisms for evaluating communicated content and source credibility.<br />
<a href="https://doi.org/10.1111/j.1468-0017.2010.01394.x"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S43</strong></td>
<td><strong>T1</strong></td>
<td>Higgins (1997), regulatory focus theory</td>
<td>Promotion and prevention orientations as distinct self-regulatory strategies.<br />
<a href="https://pubmed.ncbi.nlm.nih.gov/9414606/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S44</strong></td>
<td><strong>T1</strong></td>
<td>OpenAI plugin security and privacy guidance</td>
<td>Least privilege, explicit consent, input validation, and audit logging.<br />
<a href="https://developers.openai.com/plugins/guides/security-privacy"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S45</strong></td>
<td><strong>T2</strong></td>
<td>Prompt Infection in multi-agent systems</td>
<td>Malicious instructions can self-replicate through inter-agent communication.<br />
<a href="https://openreview.net/forum?id=NAbqM2cMjD"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S46</strong></td>
<td><strong>T2</strong></td>
<td>Towards Secure Systems of Interacting AI Agents (2025)</td>
<td>Free-form interaction expands collusion and swarm-attack surfaces.<br />
<a href="https://arxiv.org/abs/2505.02077"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S47</strong></td>
<td><strong>T2</strong></td>
<td>OpenAI, chain-of-thought monitorability</td>
<td>Reasoning traces may support monitoring but are fragile and not a sole safety control.<br />
<a href="https://openai.com/index/evaluating-chain-of-thought-monitorability/"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S48</strong></td>
<td><strong>T2</strong></td>
<td>Anthropic, trustworthy agents</td>
<td>Trustworthiness is a property of model, harness, tools, and environment.<br />
<a href="https://www.anthropic.com/research/trustworthy-agents"><u>Open primary/official source</u></a></td>
</tr>
<tr class="even">
<td><strong>S49</strong></td>
<td><strong>T1</strong></td>
<td>Aritzeta, Swailes &amp; Senior (2007), Belbin team-role review</td>
<td>Mixed psychometric support; weak discriminant validity cautions against categorical engineering use.<br />
<a href="https://doi.org/10.1111/j.1467-6486.2007.00666.x"><u>Open primary/official source</u></a></td>
</tr>
<tr class="odd">
<td><strong>S50</strong></td>
<td><strong>T2</strong></td>
<td>Pittenger (2005), cautionary review of MBTI</td>
<td>Psychometric and interpretive limitations of categorical personality typing.<br />
<a href="https://epublications.bond.edu.au/hss_pubs/26/"><u>Open primary/official source</u></a></td>
</tr>
</tbody>
</table>

## Appendix B. Glossary and operational definitions

| **Term**                    | **Definition**                                                                                                                      |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Agent                       | A model instance plus instructions, context/state, tools, permissions, runtime controls, and conversation/action history.           |
| Subagent                    | A bounded worker invoked by a primary agent or orchestrator for a scoped contribution.                                              |
| Team Pack                   | A versioned manifest defining approved roles, topology, context contracts, tools, outputs, budgets, gates, and evaluations.         |
| Persona                     | In this report, a role contract plus optional style overlay and an observed behavioral profile—not an intrinsic person.             |
| Cognitive operating profile | The intended pattern of attention, method, evidence handling, interaction, risk, action, and termination.                           |
| Cognitive biopsy            | A controlled diagnostic battery that samples elicited behavior of one deployed configuration.                                       |
| Synthetic personality       | Reliable or shapeable personality-like patterns expressed in model outputs under specified conditions.                              |
| Role advantage              | Measured improvement attributable to a role configuration over a declared baseline.                                                 |
| Fidelity                    | Degree to which the configured strategy appears in behavior without sacrificing correctness or safety.                              |
| Robustness                  | Stability of outcomes under irrelevant or adversarial perturbations.                                                                |
| Complementarity             | Non-duplicative evidence, methods, tools, or error patterns that improve the team.                                                  |
| Shared mental model         | A common representation of objective, task state, constraints, roles, and completion criteria.                                      |
| Transactive memory          | A distributed map of who possesses or can retrieve which knowledge.                                                                 |
| Hidden profile              | A decision task where decisive information is distributed and must be integrated across members.                                    |
| Epistemic vigilance         | Evaluation of source and content credibility before accepting communicated information.                                             |
| Minority report             | Preserved evidence-backed position that differs from the adjudicated conclusion.                                                    |
| Run receipt                 | Reconstructable record of versions, context, permissions, messages, tools, outputs, disagreement, verification, cost, and decision. |
| Gate                        | Predeclared policy that allows, blocks, or conditionally allows promotion or external action.                                       |

## Closing recommendation

> **NEXT BUILD** Implement agentic-readiness-audit-v1 as the reference Team Pack, with minimal role prompts, independent first passes, typed evidence handoffs, a minority report, a separate verifier, and the B0–B4 evaluation ladder. Treat every cognitive/personality descriptor as a hypothesis that must earn its place through ablation and outcome evidence.
