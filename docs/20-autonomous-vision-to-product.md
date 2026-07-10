# Autonomous Vision-to-Product Method

Status: canonical method extension
Version: 0.2.0
Audience: product owners, product architects, engineering leads, autonomous-agent designers, reviewers, and operators

The Autonomous Vision-to-Product Method defines how an agent-assisted team can transform an initial vision into a product that is explicit, challengeable, versioned, incrementally buildable, independently verified, and prepared for supervised operation.

It connects the repository's existing profiling, challenge, product modeling, worker, safety, cost, testing, and feedback practices into one end-to-end operating protocol. It does not replace those practices. It defines when they are used, what they must produce, and which gates prevent premature progression.

## Contents

1. [Definition, purpose, and boundaries](#1-definition-purpose-and-boundaries)
2. [The five movements](#2-the-five-movements)
3. [Vision maturity](#3-vision-maturity)
4. [Human bootstrap](#4-human-bootstrap)
5. [Transition to bounded autonomy](#5-transition-to-bounded-autonomy)
6. [Project inference loop](#6-project-inference-loop)
7. [Functional exploration](#7-functional-exploration)
8. [Product cartography](#8-product-cartography)
9. [Curation and saturation](#9-curation-and-saturation)
10. [Foundation Freeze](#10-foundation-freeze)
11. [Roadmap and build mission portfolio](#11-roadmap-and-build-mission-portfolio)
12. [Parallel development agents](#12-parallel-development-agents)
13. [End-to-end engineering lifecycle](#13-end-to-end-engineering-lifecycle)
14. [Integration and verification](#14-integration-and-verification)
15. [Human gates and autonomy levels](#15-human-gates-and-autonomy-levels)
16. [Security and Privacy by Design](#16-security-and-privacy-by-design)
17. [Private, internal, and public products](#17-private-internal-and-public-products)
18. [Durable autonomous workers](#18-durable-autonomous-workers)
19. [Model governance](#19-model-governance)
20. [Completeness without completion theater](#20-completeness-without-completion-theater)
21. [Sources of truth and artifact scaling](#21-sources-of-truth-and-artifact-scaling)
22. [Independent acceptance](#22-independent-acceptance)
23. [Post-delivery learning loop](#23-post-delivery-learning-loop)
24. [Anti-pattern catalog](#24-anti-pattern-catalog)
25. [Canonical example and final checklists](#25-canonical-example-and-final-checklists)

## 1. Definition, Purpose, And Boundaries

### 1.1 Definition

Vision-to-Product is a governed transformation process:

```text
Initial vision
  -> project profiling
  -> clarification and challenge
  -> traceable inference
  -> functional exploration
  -> product maps and contracts
  -> curated foundation
  -> falsification verticals
  -> versioned Foundation Freeze
  -> build mission portfolio
  -> isolated development agents
  -> integration and independent gates
  -> supervised release
  -> operation, learning, and revision
```

The central rule is:

> The autonomous agent does not code the first formulation of a request. It first transforms the vision into an explicit, falsifiable, versioned product model. It then tests that model through functional verticals, stabilizes a foundation, and coordinates development without losing the original intent.

### 1.2 Purpose

The method is designed to answer five difficult questions:

- What does the user actually want, including what remains uncertain?
- Which product interpretations deserve exploration before one is selected?
- Which concepts are stable enough to become contracts?
- How can multiple workers build safely without fragmenting the product?
- What evidence justifies moving from a model to a real, operated product?

### 1.3 Boundaries

This method:

- supports product and project understanding, not covert behavioral profiling;
- structures decisions, but does not replace product taste or domain expertise;
- supports compliance work, but does not certify legal compliance;
- supports security engineering, but does not certify a system as secure;
- enables bounded autonomy, but does not remove human responsibility;
- treats deployment as a red action unless an explicit operating policy says otherwise;
- does not grant an agent authority merely because it inferred that an action would be useful.

### 1.4 Profiling Boundaries

Project profiling may include three explicitly separated views:

1. **Sponsor profile**: goals, constraints, decision authority, declared preferences, and success criteria of the person or group commissioning the work.
2. **Audience profile**: jobs, contexts, accessibility needs, capability levels, risks, and expected outcomes of the people the product serves.
3. **Situational profile**: market, organization, workflow, technology, regulation, timing, resources, and operating environment.

These views must not be collapsed into a hidden personal dossier. Collect only information needed for the stated product purpose. State why it is needed, obtain consent where appropriate, allow correction, and define retention. A temporary behavior is not an identity. A project inference is not a psychological fact.

## 2. The Five Movements

The method is organized around four sequential movements and one permanent movement.

| Movement | Main question | Typical output | Exit condition |
| --- | --- | --- | --- |
| Understand | What is being sought, by whom, and under which constraints? | Project profile, ambiguity map, decisive questions | The intent is coherent enough to explore |
| Diverge | What valid products, domains, workflows, and risks could follow? | Competing interpretations, domain and capability candidates | New exploration produces little net-new value |
| Stabilize | What can be accepted as a versioned foundation? | Curated maps, contracts, falsification results, Foundation Freeze Candidate | Human gate accepts a bounded foundation |
| Build | How can the product be implemented, integrated, and verified? | Vertical slices, worker missions, tested release candidate | Independent acceptance evidence exists |
| Observe, learn, revise | What did real use invalidate or reveal? | Signals, learning report, change proposals | Permanent loop, no final exit |

Movement is not determined by time spent. It is determined by evidence. A team may return from Build to Diverge when a real integration invalidates the product model.

## 3. Vision Maturity

The profiler adapts its behavior to the maturity of the initial vision.

| Initial state | Agent behavior | Main risk | Exit evidence |
| --- | --- | --- | --- |
| Very vague | Elicit concrete frustrations, desired changes, examples, existing workarounds, actors, and context. Offer several plausible product interpretations. | Imposing the agent's preferred product | User recognizes the problem framing and rejects or ranks interpretations |
| Fragmentary | Reconstruct the intended system from partial features, documents, workflows, and constraints. Find missing links and contradictions. | Treating a feature list as a product model | Major fragments are mapped to domains, journeys, and unresolved decisions |
| Already precise | Audit evidence, non-goals, architecture assumptions, user value, feasibility, and hidden operating obligations. | Obediently formalizing a flawed specification | Assumptions and alternatives have been challenged and accepted or revised |
| Existing partial product | Inspect actual behavior, tests, architecture, user journeys, incidents, and documentation. Separate current state, target state, and migration path. | Believing documentation instead of runtime evidence | A verified gap map and bounded transition plan exist |

The agent must not reward apparent precision with less challenge. A detailed request can still contain false premises, incompatible constraints, or untested architecture.

## 4. Human Bootstrap

### 4.1 Initial Framing

The first pass records:

- the raw vision in the user's own words;
- the desired future state;
- the current problem and existing workaround;
- sponsor, audiences, affected parties, and decision owners;
- context of use;
- known evidence and source quality;
- constraints, non-goals, deadlines, and dependencies;
- expected autonomy and external effects;
- data sensitivity and likely regulatory exposure;
- the ambition range, from a local tool to an operated platform.

Use the [Product Brief Template](../templates/product-brief-template.md), [Product Profiling Template](../templates/product-profiling-template.md), and [Challenge Gate](06-challenge-gate.md) as the starting artifacts.

### 4.2 Status Language

Use status markers when they materially clarify truth:

- `[FACT]`: directly observed or explicitly confirmed.
- `[SIGNAL]`: relevant evidence that supports more than one interpretation.
- `[HYPOTHESIS]`: plausible but unverified explanation or need.
- `[STRONG DEDUCTION]`: converging evidence with no material contradiction found, still revisable.
- `[UNKNOWN]`: missing information that may affect the trajectory.
- `[DECISION]`: accepted choice with owner and date.
- `[CONSTRAINT]`: boundary that the plan must respect.
- `[HUMAN GATE]`: decision that cannot be delegated under the active policy.

Do not tag every sentence. Tags exist to prevent an inference from silently becoming a fact.

### 4.3 Adaptive Questions

A question is justified only when its answer may change at least one of:

- product interpretation;
- target audience;
- first useful journey;
- architecture or data model;
- safety, privacy, or compliance posture;
- cost and resource policy;
- autonomy level;
- Foundation Freeze scope;
- build order or acceptance evidence.

Use a question budget. Start with the smallest set of high-information questions, usually three to seven. After each answer, update the model before asking more.

Stop interviewing when all of the following are true:

- one active interpretation and its rejected alternatives are explicit;
- the main audience, problem, and desired outcome are usable;
- major contradictions are resolved or recorded as decisions needed;
- data and external-action risks have a preliminary class;
- the next exploration step is safe and reversible;
- another question is unlikely to change the next decision.

The criterion is not perfect understanding. It is sufficient understanding for the next bounded movement.

### 4.4 Challenge And Confrontation

The profiler must actively test the vision:

- What evidence supports the problem?
- Which assumption would make the product unnecessary if false?
- Which audience may be harmed, excluded, or misunderstood?
- Is a proposed feature solving the cause or a visible symptom?
- What simpler workflow competes with the proposed system?
- What operating, support, security, moderation, or legal burden appears after launch?
- What would make the product technically complete but practically unusable?
- Which part of the vision is aspiration rather than a current requirement?

Challenge is complete only when important alternatives and counter-hypotheses are visible. It is not complete merely because the agent recommended its preferred option.

## 5. Transition To Bounded Autonomy

Autonomy begins only after a bootstrap packet exists. The packet must contain:

- active product interpretation;
- current uncertainty and inference register;
- allowed sources and forbidden sources;
- data classification;
- safety zone and approval policy;
- current movement and expected output;
- time, cost, model, and tool budgets;
- stop and escalation conditions;
- required checkpoints;
- source-of-truth locations;
- rollback or recovery expectations.

The transition gate fails if the agent would need to invent authority, inspect unrelated personal data, use an undefined external service, or decide a red action on the user's behalf.

Autonomy is scoped to an outcome and a policy. It is never a blanket property of the agent.

## 6. Project Inference Loop

### 6.1 Loop

```text
Observe source
  -> record signal
  -> generate competing hypotheses
  -> seek confirming and disconfirming evidence
  -> assign status and confidence basis
  -> derive product consequence
  -> expose uncertainty
  -> obtain correction or gate decision
  -> retain, revise, supersede, or reject
```

### 6.2 Inference Record

Each consequential inference should record:

| Field | Meaning |
| --- | --- |
| `id` | Stable identifier |
| `statement` | Claim being evaluated |
| `status` | Signal, hypothesis, strong deduction, accepted, rejected, superseded, or unknown |
| `sources` | Durable references, not copied context dumps |
| `support` | Evidence that supports the claim |
| `counter_evidence` | Evidence or reasoning against it |
| `alternatives` | Competing explanations |
| `product_consequence` | What changes if the claim is true |
| `risk_if_wrong` | Harm or waste caused by a false inference |
| `confidence_basis` | Qualitative basis for confidence, not false numerical precision |
| `owner` | Person or role responsible for acceptance |
| `review_after` | Event or date that triggers review |
| `supersedes` | Previous record, if any |

User correction outranks an unverified model inference about the user's goals. Correction does not erase history: supersede the record and preserve why it changed.

### 6.3 Anti-Barnum Rule

An inference fails the anti-Barnum test when it is flattering, generic, difficult to falsify, or applicable to almost any project.

Replace statements such as "users value simplicity" with testable statements such as:

> `[HYPOTHESIS]` First-time operators must be able to complete the publishing review without seeing queue or worker terminology. Validate with five task-based sessions and a defined success threshold.

### 6.4 Inference Red Team

Before a strong deduction becomes a foundation input, a reviewer asks:

- What observation would disprove it?
- Is the source independent or repeated from the same origin?
- Did the system infer a stable need from a temporary state?
- Is an absent objection being treated as consent?
- Does another product interpretation explain the evidence better?
- Is confidence driven by repetition rather than source quality?

## 7. Functional Exploration

Exploration must be broad enough to find the real product, but structured enough to stop.

### 7.1 Exploration Lenses

Explore each plausible interpretation through these lenses:

1. Actors and jobs to be done.
2. End-to-end journeys, including first use, normal use, recovery, and exit.
3. Lifecycle stages before, during, and after the main action.
4. Objects, states, transitions, and invariants.
5. Exceptions, failures, abuse cases, and denied actions.
6. Human decisions and possible automation.
7. Experience Plane and Control Plane surfaces.
8. Data creation, access, retention, deletion, and export.
9. Integrations and external side effects.
10. Operations, support, monitoring, incident response, and rollback.
11. Accessibility, localization, and different expertise levels.
12. Cost, performance, scale, and maintenance.

### 7.2 Divergent Passes

Run at least three passes for ambitious products:

- **Expected product**: the most direct interpretation of the request.
- **Simpler competitor**: the smallest workflow that may solve the real problem.
- **Broader system**: the platform or operating model implied by the long-term ambition.

The goal is not to select the largest interpretation. The goal is to understand the choice.

### 7.3 Candidate Quality

A capability candidate is useful only if it has:

- a specific actor or consumer;
- a recognizable outcome;
- defined inputs and outputs;
- a domain owner;
- a place in at least one journey;
- evidence or an explicit hypothesis;
- known safety and cost implications;
- a reason it should not be merged into an existing capability.

Generic labels such as "AI management", "smart analytics", or "content features" are not accepted capability definitions.

## 8. Product Cartography

The maps form a system. They should not become disconnected inventories.

### 8.1 Domain Atlas

A domain is a coherent responsibility boundary with its own language, rules, objects, and owner. Record:

- purpose and users;
- responsibilities and exclusions;
- core objects and policies;
- inbound and outbound contracts;
- shared concepts;
- lifecycle and failure modes;
- data class and regulatory exposure;
- operational owner.

### 8.2 Capability Atlas

A capability is a reusable product behavior, not a screen or code module. Record the contract defined in [Capability Graph](10-capability-graph.md), plus evidence, maturity, and current disposition.

### 8.3 Module Map

Modules and sub-modules are implementation ownership boundaries that realize capabilities. They may change without redefining user value. Record:

- capabilities realized;
- dependencies and forbidden dependencies;
- public contracts;
- data ownership;
- test boundary;
- migration and extraction risk.

Do not equate domain, capability, and module:

- a domain organizes product responsibility;
- a capability expresses reusable behavior and value;
- a module organizes implementation and ownership.

### 8.4 Object And State Catalog

For each important object, define:

- canonical name and meaning;
- owning domain;
- identity and lifecycle;
- valid states and transitions;
- transition actor and permission;
- invariants;
- retention and deletion behavior;
- events emitted;
- audit requirements.

A workflow is incomplete when it names actions but not the states that make those actions valid.

### 8.5 Cross-Domain Composition Map

Compositions describe end-to-end behavior that crosses capabilities or domains. Each composition states:

- trigger and initiating actor;
- participating capabilities;
- contracts and artifacts exchanged;
- synchronous and asynchronous steps;
- partial failure behavior;
- compensation or rollback;
- final user-visible truth;
- integration evidence.

### 8.6 UI Surface Map

Map surfaces to actors, journeys, objects, decisions, and truth requirements:

| Surface | Plane | Primary actor | Main job | Truth exposed | Advanced path |
| --- | --- | --- | --- | --- | --- |
| Product workspace | Experience | End user | Achieve domain outcome | User-relevant status and uncertainty | Contextual settings |
| Operations console | Control | Operator | Inspect and control runs | Logs, gates, cost, failures, permissions | Full diagnostics |

Apply the [Dual UI Model](08-dual-ui-model.md). Simple defaults must not remove inspectability, and expert controls must not dominate the first-use path.

### 8.7 Permission And Autonomy Map

For every capability and transition, record:

- who may request it;
- who may approve it;
- who or what may execute it;
- applicable autonomy level;
- data classes touched;
- external effects;
- required evidence;
- rollback or compensation;
- audit trail.

## 9. Curation And Saturation

Exploration produces candidates. Curation produces a usable product model.

### 9.1 Curation Operations

For every candidate, choose one disposition:

- `active`: belongs to the accepted model;
- `foundation-candidate`: may become a stable contract;
- `incubator`: valuable but insufficiently evidenced;
- `deferred`: valid but outside the current horizon;
- `merged`: duplicate absorbed into another concept;
- `split`: concept was too broad and became several records;
- `rejected`: evaluated and refused with reason;
- `superseded`: replaced by a later decision.

Curate names, definitions, boundaries, synonyms, ownership, contracts, and traceability. Preserve rejected decisions so the same idea is not rediscovered without new evidence.

### 9.2 Saturation Test

Exploration is saturated for the current decision when two consecutive passes across different lenses produce:

- no new P0 domain;
- no new shared object or state invariant;
- no new red action or material threat;
- no new audience that changes the Experience Plane;
- no new cross-domain composition required by the first release;
- no unresolved contradiction that blocks a foundation decision;
- mostly synonyms, refinements, or later-horizon candidates.

Saturation is local and versioned. It does not mean the product has no future unknowns.

### 9.3 Value-Of-Information Rule

Continue exploring only when the expected value of new information exceeds the cost and delay of obtaining it. If uncertainty can be resolved more cheaply by a reversible functional vertical, build the vertical instead of extending the interview or map.

## 10. Foundation Freeze

### 10.1 Definition

A Foundation Freeze is a versioned, human-accepted baseline of product and technical contracts that parallel work may rely on. It is not a permanent architectural lock and not a claim that the product is complete.

The freeze protects build coherence while allowing uncertain concepts to remain in an incubator.

### 10.2 Required Contents

A Foundation Freeze Candidate includes:

- North Star and active product vision;
- audience and situational boundaries;
- accepted domains and shared language;
- core capabilities and compositions;
- canonical objects, states, and invariants;
- Experience Plane and Control Plane principles;
- permission and autonomy model;
- data classification and privacy constraints;
- architecture decisions and contracts;
- P0 verticals and acceptance evidence;
- excluded, deferred, and incubated concepts;
- known risks and unresolved questions;
- version, owner, date, and supersession policy.

### 10.3 Falsification Verticals

Before freezing, build or otherwise exercise the smallest verticals capable of disproving the foundation's riskiest assumptions. A falsification vertical crosses the real boundaries that matter, for example:

```text
User intent
  -> persisted domain object
  -> policy decision
  -> capability execution
  -> visible Experience Plane result
  -> Control Plane evidence
```

A fixture-only path can validate a contract shape. It cannot prove real integration.

### 10.4 Freeze Gate

The Foundation Freeze Gate requires:

- curated domain and capability maps;
- shared objects and states with owners;
- versioned contracts;
- tested P0 falsification verticals;
- explicit alternatives and rejected decisions;
- threat and privacy review;
- rollback or migration strategy for foundation changes;
- human acceptance by product and engineering owners.

### 10.5 Controlled Change

After freeze, a foundation change requires a proposal containing:

- trigger and evidence;
- affected contracts, domains, journeys, and workers;
- alternatives;
- compatibility and migration impact;
- new tests and rollback;
- decision owner;
- target foundation version.

Exploration may continue in the incubator without changing the active foundation. This separates learning from ungoverned drift.

## 11. Roadmap And Build Mission Portfolio

### 11.1 Roadmap Layers

Keep four horizons explicit:

1. **P0 foundation**: contracts and verticals required to test the product model.
2. **First usable release**: coherent journeys for the primary audience.
3. **Operational release**: reliability, support, security, monitoring, and governance needed for real use.
4. **Incubator and later horizons**: plausible expansions that must not silently widen current scope.

### 11.2 Vertical Slices

A build slice should cross enough layers to produce observable value and evidence. Avoid roadmaps composed only of horizontal technical layers such as "build database", "build API", and "build UI".

A vertical defines:

- target actor and outcome;
- triggering journey;
- domains and capabilities touched;
- contracts and data;
- UI surfaces;
- safety zone;
- tests and observable acceptance;
- rollback;
- learning objective.

### 11.3 Prioritization

Prioritize with explicit reasoning across:

- user value;
- risk reduction;
- information gained;
- dependency unlock;
- reversibility;
- implementation and operating cost;
- security and compliance urgency;
- strategic coherence.

A high-value vertical that depends on an untested foundation may rank below a smaller falsification vertical.

### 11.4 Mission Portfolio

The Build Mission Portfolio translates accepted verticals into bounded worker missions. It records:

- mission ID and objective;
- owning vertical and contracts;
- prerequisites;
- isolated workspace and file ownership;
- inputs and expected artifacts;
- model and tool policy;
- safety zone, budget, timeout, and STOP mechanism;
- test and evidence contract;
- review and integration owner;
- merge dependencies;
- status truth.

Represent dependencies as an execution DAG. Parallelize independent missions, not merely tasks that look separate in a list.

## 12. Parallel Development Agents

Parallel agents increase throughput only when ownership and integration are explicit.

### 12.1 Preconditions

Do not launch parallel build agents until:

- the active foundation is versioned;
- each mission references the same accepted contracts;
- workspaces or branches are isolated;
- file and module ownership does not overlap without an integration plan;
- inputs, outputs, tests, timeout, and stop conditions are explicit;
- an integration owner exists;
- an independent reviewer is assigned;
- conflicts and rejected results can be handled without losing evidence.

### 12.2 Mission Contract

Each agent receives a compact ContextPack containing only:

- mission charter;
- relevant foundation version;
- owned files or modules;
- required contracts and fixtures;
- decisions and constraints;
- safety and data class;
- tests to run;
- expected handoff artifacts;
- forbidden actions;
- escalation route.

Agents must not infer permission to edit shared contracts. They open a Foundation Change Proposal when the mission exposes a contract defect.

### 12.3 Conflict Prevention

Use:

- isolated worktrees, branches, or sandboxes;
- single ownership for shared files during a mission window;
- contract tests before integration;
- generated or versioned fixtures owned by the contract owner;
- explicit merge order in the DAG;
- integration branches only when they have a named owner and disposal policy.

Do not let multiple agents simultaneously rewrite the same architecture, schema, lockfile, navigation root, or shared contract.

### 12.4 Roles

Separate these roles when risk or scope justifies it:

- builder;
- gate runner;
- reviewer or editor;
- proofreader;
- integration owner;
- acceptance owner;
- publisher or deployer.

One person may hold several roles on small work, but the builder must not be the only source of final acceptance evidence.

## 13. End-To-End Engineering Lifecycle

The build movement covers more than code generation.

| Phase | Required result | Minimum evidence |
| --- | --- | --- |
| Technical discovery | Constraints, current state, unknowns | Inspected sources and gap map |
| Architecture comparison | Options and tradeoffs | Decision criteria and rejected options |
| Architecture decision | Accepted structural choice | ADR when the choice is durable or costly to reverse |
| Threat modeling | Assets, actors, trust boundaries, abuse cases | Reviewed threat model |
| Data and contract design | Ownership, schemas, APIs, events, fixtures | Versioned contracts and contract tests |
| UX design | Journeys, surfaces, states, accessibility | Reviewable flows and truth states |
| Design system | Reusable visual and interaction rules | Tested components or documented tokens as applicable |
| Vertical implementation | End-to-end behavior | Running path through relevant layers |
| Independent review | Defects and acceptance decision | Review record separate from builder claim |
| Verification | Unit, integration, end-to-end, accessibility, performance, and security evidence as applicable | Actual command outputs and reports |
| Supply-chain review | Dependency and artifact risks | Inventory, provenance, and vulnerability evidence |
| Visual QA | Rendered states and responsive behavior | Screenshots or recorded review criteria |
| Documentation | Operation, decisions, limits, and handoff | Updated sources of truth |
| Packaging | Reproducible release candidate | Build artifact and provenance |
| Release readiness | Deployment, rollback, monitoring, and incident plan | Passed release gates |
| Supervised release | Authorized external change | Verified target, result, and rollback readiness |
| Operation | Observable service and support | Monitoring and incident evidence |
| Product learning | Real signals and revised hypotheses | Learning report and change proposals |

Use the lightest lifecycle that protects the product. Small local tools may combine phases. Public or safety-sensitive systems must keep their evidence distinct.

## 14. Integration And Verification

### 14.1 Integration Packet

Every mission handoff provides:

- commit or patch reference;
- foundation and contract versions used;
- files and modules changed;
- decisions and deviations;
- tests run with results;
- tests skipped with reason;
- new dependencies;
- security, privacy, and cost impact;
- known failures and rollback;
- proposed next state.

### 14.2 Integration Gate

The integration owner verifies:

- scope belongs to the mission;
- contracts remain compatible;
- migrations are ordered and reversible where required;
- unit and contract tests pass;
- relevant verticals run across real boundaries;
- Experience Plane and Control Plane report compatible truth;
- no sensitive data enters artifacts or logs;
- accessibility, performance, and security checks match risk;
- rejected worker output has not been silently accepted;
- documentation and status reflect reality.

### 14.3 Evidence Vocabulary

Keep these states distinct:

- `specified`: contract exists;
- `implemented`: code or configuration exists;
- `unit-tested`: isolated behavior passed;
- `fixture-integrated`: components passed against controlled substitutes;
- `integrated`: real components exercised together;
- `end-to-end verified`: representative journey passed through its actual boundaries;
- `user-validated`: target users supplied evidence;
- `release-ready`: all applicable release gates passed;
- `released`: authorized deployment was verified;
- `operationally validated`: real operation produced acceptable evidence.

Never call a fixture real integration, readiness authorization, a prototype a finished product, or a local test user validation.

### 14.4 Premium Evidence

Premium is an evidence state, not a design intention. A product may claim a premium level only when applicable evidence shows:

- the primary audience can complete the main journey without internal jargon or avoidable cognitive load;
- beginner defaults and expert controls coexist through progressive disclosure;
- the end-to-end journey works across real boundaries and reports failures honestly;
- loading, empty, partial, error, recovery, permission-denied, and rollback states are designed and exercised;
- accessibility, performance, responsiveness, and content quality meet explicit thresholds;
- costs, uncertainty, model behavior, and external effects are visible to the appropriate actor;
- destructive or consequential actions remain reversible or gated as required;
- support, operation, and incident responsibilities are defined for real use;
- target users and an independent reviewer have accepted the result within stated limits.

Visual polish can strengthen this evidence, but cannot replace a missing journey, false status, weak accessibility, unsafe automation, hidden cost, or untested recovery. Apply the [Premium Standard](03-premium-standard.md) and record its proof in the acceptance packet.

## 15. Human Gates And Autonomy Levels

### 15.1 Human Gates

| Gate family | Human decisions that remain explicit |
| --- | --- |
| Profiling | Consent, correction of sponsor intent, acceptance of consequential inferences, allowed sources |
| Product | Active interpretation, North Star, P0, rejected alternatives, Foundation Freeze |
| Technical | Durable architecture change, security risk acceptance, migration with material impact, dependency policy exception |
| External | Publication, production change, financial action, external message, destructive action, handling of secrets or credentials |

A gate observes evidence and returns pass, fail, or decision needed. It does not silently correct the work and then approve itself.

### 15.2 Autonomy Levels

| Level | Description | Typical authority |
| --- | --- | --- |
| A0 - Advise | Analyze and recommend | No write or execution authority |
| A1 - Draft | Create local proposals and artifacts | Reversible local documents or patches |
| A2 - Execute bounded local work | Implement and test within an accepted mission | Green actions in declared scope |
| A3 - Integrate under supervision | Prepare and combine accepted changes | Orange actions after required proposal or review |
| A4 - Operate with explicit gates | Run recurring workflows under an approved policy | Pre-authorized actions with audit, limits, and human gates |
| A5 - Exceptional delegated operation | Execute narrowly defined consequential actions | Only under explicit governance; red actions still require their designated approval |

Autonomy is assigned per capability and action, not per product or agent. A system may autonomously run tests at A2 while publication remains A0 until a human approves it.

## 16. Security And Privacy By Design

### 16.1 Principles

- Minimize data, permissions, context, retention, and external exposure.
- Separate identity, content, operational, billing, telemetry, and secret data.
- Default to least privilege and deny undeclared actions.
- Keep secrets out of prompts, logs, repositories, examples, and artifacts.
- Make destructive and external effects explicit and reviewable.
- Design deletion, export, revocation, incident response, and rollback before release.
- Treat model and tool outputs as untrusted until validated.

### 16.2 Conservative Data Classification

| Class | Example | Default handling |
| --- | --- | --- |
| S0 - Public | Published documentation and synthetic examples | May enter approved public workflows |
| S1 - Internal | Non-sensitive project planning and ordinary operational metadata | Limit to authorized project participants |
| S2 - Confidential | Unreleased product plans, customer content, commercial information | Need-to-know access, controlled retention, approved processors only |
| S3 - Restricted | Personal data, sensitive user content, security findings, secret-adjacent material | No external model provider under the default policy; strong access and audit controls |
| S4 - Critical | Credentials, private keys, production secrets, highly sensitive or high-impact data | Never place in model context; use dedicated secret and control systems |

An organization may refine the scheme through an approved policy, but may not silently downgrade data to simplify execution.

### 16.3 Threat Model Coverage

At minimum, evaluate:

- prompt injection and instruction smuggling;
- unauthorized tool use;
- privilege escalation;
- data exfiltration through context, logs, artifacts, or model providers;
- cross-project or cross-tenant leakage;
- dependency and supply-chain compromise;
- poisoned source material;
- malicious or accidental external actions;
- unsafe generated code or commands;
- retry storms and cost denial of service;
- false status and evidence fabrication;
- destructive migrations and missing rollback;
- abuse of public endpoints;
- profiling without consent or purpose limitation.

### 16.4 Privacy Controls

For each data flow, record purpose, source, legal or organizational basis, data class, fields, recipients, processing location, retention, deletion, export, access control, audit trail, and incident owner.

Privacy review fails when the product collects data because it may become useful later, retains it indefinitely by default, or uses it for a materially different purpose without a new decision.

## 17. Private, Internal, And Public Products

### 17.1 Private Or Personal Product

Still define:

- local data locations and backups;
- device and account boundaries;
- provider exposure;
- retention and deletion;
- export and portability;
- consequences of loss or compromise;
- which actions remain externally visible.

Private does not mean risk-free. Personal automation can still expose credentials, publish content, spend money, or destroy data.

### 17.2 Internal Product

Also define:

- organizational roles and least privilege;
- employee or contractor data boundaries;
- audit and support ownership;
- change management;
- vendor and processor review;
- business continuity;
- internal incident and access review procedures.

### 17.3 Public Or Commercial Product

Before launch, address as applicable:

- privacy notice and transparent consent or preference controls;
- lawful basis and purpose limitation;
- cookies and tracking choices;
- account lifecycle and user rights;
- accessibility requirements;
- terms and acceptable-use rules;
- abuse prevention and moderation;
- support, complaints, and incident response;
- public security and vulnerability handling;
- vendor and cross-border processing;
- reputation and communications review;
- proof of acceptance for launch-critical journeys.

### 17.4 GDPR-Oriented Review

For products subject to the GDPR, identify the controller and processors; purposes and lawful bases; data categories; sensitive data; recipients; retention; transfers; access, rectification, erasure, portability, objection, and restriction procedures; consent withdrawal where applicable; processing records; processor contracts; breach management; log review; pseudonymization or anonymization opportunities; children-specific obligations; and the need for a DPIA.

Avoid covert profiling and solely automated decisions with legal or similarly significant effects unless a qualified review establishes a lawful basis and appropriate safeguards.

This method provides an engineering checklist, not legal advice or a compliance certificate. Qualified legal review remains a human gate when obligations are material or uncertain.

## 18. Durable Autonomous Workers

A durable worker is an observable runtime, not a long chat session.

It needs:

- external wrapper or supervisor;
- isolated session and workspace;
- mission queue ordered by outcome value;
- live status and append-only decision history;
- logs with sensitive-data redaction;
- heartbeat and stale-run detection;
- STOP file or equivalent kill mechanism;
- timeout for each external call and the whole mission;
- bounded retries with backoff and escalation;
- checkpoints and periodic reports;
- touched-file and dependency records;
- tests and final report;
- recovery after interruption;
- supervised notifications;
- explicit limits on external actions.

The work loop is result-driven:

```text
Select highest-value unblocked outcome
  -> produce bounded result
  -> test and challenge it
  -> record evidence and decisions
  -> integrate or reject
  -> open a gap when needed
  -> re-prioritize from current evidence
```

Duration is not autonomy. A continuous worker must not fill time artificially. Stop or change movement when retries repeat without evidence, marginal value declines, budgets approach limits, or an independent gate is required.

See [Autonomous Worker Runtime](13-autonomous-worker-runtime.md) for the runtime contract.

## 19. Model Governance

Route work by role and evidence need, not by blind dependence on one model.

| Work class | Appropriate strategy |
| --- | --- |
| Ambiguous framing, architecture arbitration, final synthesis, high-risk review | Strong reasoning model plus independent review |
| Exploration, bounded implementation, integration analysis, editorial review | Balanced model selected through representative evaluation |
| Extraction, formatting, fixtures, repetitive tests, deterministic documentation checks | Economical model or deterministic tool with strict contract |

Governance requires:

- data classification before routing;
- compact ContextPacks;
- representative benchmarks rather than generic leaderboards;
- recorded model, version, provider, policy, and date;
- durable handoffs independent of model memory;
- caching where source inputs and policy allow it;
- cost, latency, and retry limits;
- escalation when confidence or verification is insufficient;
- no critical decision entrusted only to an economical model;
- no S3 or S4 data sent to an external provider under the default policy;
- independent audit for foundation changes.

A model recommendation is time-sensitive. Re-evaluate it against current official documentation and representative tasks before making it a durable dependency.

## 20. Completeness Without Completion Theater

### 20.1 Dimensions

Completeness must be assessed across distinct dimensions:

- conceptual coverage;
- domain coherence;
- inference maturity;
- foundation readiness;
- contract coverage;
- integrated P0 verticals;
- UX quality and accessibility;
- security and privacy;
- test evidence;
- real integration;
- deployment readiness;
- operational readiness;
- human and user validation;
- compliance review;
- rollback capability.

File count, card count, test count, token spend, and time spent are not completeness metrics.

### 20.2 Evidence Scale

Score each applicable dimension independently:

| Level | Meaning |
| --- | --- |
| 0 - Unknown | No usable evidence |
| 1 - Framed | Scope and risks described |
| 2 - Specified | Contracts and acceptance criteria exist |
| 3 - Exercised | Representative implementation or process was tested |
| 4 - Independently accepted | Evidence reviewed by the designated acceptance owner |
| 5 - Operationally validated | Real use confirms the result within stated limits |

An overall percentage may be reported only as an explicitly weighted estimate. It must show dimension scores, evidence, confidence, unknowns, and excluded dimensions. Never raise the estimate materially without new integrated evidence.

### 20.3 Periodic Report

Report:

- total weighted estimate and confidence;
- conceptual coverage;
- foundation readiness;
- local alpha status;
- real integration status;
- newly accepted evidence;
- unknowns and hypotheses;
- blocking risks and decisions;
- next milestone that can legitimately change the estimate;
- realism warning.

Do not declare 99 percent without independent acceptance, human validation, verified deployment, operational evidence, and explicit acceptance of remaining limits. In most pre-production work, 99 percent is not a useful or credible status.

## 21. Sources Of Truth And Artifact Scaling

### 21.1 Hierarchy

Use this precedence order when records disagree:

1. North Star.
2. Active product vision.
3. Active Foundation Freeze.
4. Accepted ADRs and contracts.
5. Roadmap.
6. Build Mission Portfolio.
7. Worker specifications.
8. Verified results and reports.
9. Incubator.
10. Superseded history.

Do not use chat as the sole source of truth, backlog as product vision, kanban as architecture, worker report as acceptance proof, or task count as maturity.

### 21.2 Artifact Catalog

An ambitious system may use:

- `PROJECT_CHARTER.md`
- `PROJECT_PROFILE.md`
- `AUDIENCE_PROFILES.md`
- `SITUATIONAL_PROFILE.md`
- `VISION_MAP.md`
- `ASSUMPTION_REGISTER.md`
- `INFERENCE_REGISTRY.jsonl`
- `DOMAIN_ATLAS.md`
- `CAPABILITY_ATLAS.md`
- `MODULE_MAP.md`
- `OBJECT_STATE_CATALOG.md`
- `CROSS_DOMAIN_COMPOSITIONS.md`
- `UI_SURFACE_MAP.md`
- `RISK_REGISTER.md`
- `PRIVACY_AND_DATA_MAP.md`
- `ROADMAP.md`
- `BUILD_MISSION_PORTFOLIO.md`
- `FOUNDATION_FREEZE_CANDIDATE.md`
- `FOUNDATION_CHANGE_PROPOSALS.md`
- `ARCHITECTURE.md`
- `ADR/`
- `EXECUTION_DAG.md`
- `WORKER_SPECS/`
- `TEST_STRATEGY.md`
- `ACCEPTANCE_GATE.md`
- `ROLLBACK.md`
- `LIVE_STATUS.md`
- `DECISIONS_NEEDED.md`
- `COMPLETENESS_ESTIMATE.md`
- `RUN_REPORT.md`
- `LEARNING_REPORT.md`

This is a catalog, not a command to create thirty files. A small project should combine these concerns in the [Vision-to-Product Control Pack Template](../templates/vision-to-product-control-pack-template.md). Split an artifact only when it has a distinct owner, lifecycle, sensitivity, review gate, or update frequency.

## 22. Independent Acceptance

The producer is not the final judge of its own result.

Independent acceptance checks:

- usefulness for the target audience;
- coherence with North Star and Foundation Freeze;
- contract and integration truth;
- UX clarity and accessibility;
- security and privacy;
- performance and operating cost;
- compliance obligations;
- rollback and recovery;
- honest status and limitations;
- absence of unauthorized external effects.

The acceptance owner may return:

- `accepted` with evidence and stated limits;
- `accepted-with-reservations` with owned follow-up;
- `rejected` with blocking findings;
- `decision-needed` when authority or evidence is missing.

A reviewer may identify and propose corrections. The acceptance record must still distinguish the producer's work, reviewer changes, and final decision.

## 23. Post-Delivery Learning Loop

The method continues after release:

```text
Real use
  -> signals and feedback
  -> incidents and performance data
  -> competing explanations
  -> corrected inference records
  -> project profile revision
  -> capability candidate or change proposal
  -> new falsification vertical
  -> next foundation and release
```

Rules:

- one metric does not dictate product direction;
- correlation is not causation;
- isolated feedback is not a universal truth;
- a temporary user state is not identity;
- explicit user correction has priority over unverified inference;
- rejected decisions remain searchable;
- learning is versioned with source and date;
- invalidated hypotheses are retired or superseded;
- production evidence does not bypass privacy purpose limitation;
- urgent incidents may trigger a bounded safety change before broader product revision.

Use [Feedback Integration](15-feedback-integration.md) and capture the result in a learning report or equivalent source of truth.

## 24. Anti-Pattern Catalog

| Anti-pattern | Symptom | Cause and risk | Detection | Correction |
| --- | --- | --- | --- | --- |
| Code before understanding | First artifact is implementation | Raw wording becomes accidental architecture | No profile or challenge evidence | Return to bootstrap and bound a falsification vertical |
| Generic questionnaire | Many questions, little trajectory change | Intake theater and user fatigue | Answers do not alter decisions | Use a question budget and information-value test |
| Covert profiling | Personal inferences appear without purpose or consent | Privacy harm and loss of trust | No source, purpose, correction, or retention rule | Minimize, disclose, obtain required consent, and remove unjustified data |
| Barnum inference | Statements sound insightful but fit almost any project | False confidence | Claim has no disproof condition | Rewrite as testable hypothesis with counter-evidence |
| Profile dump | Large context is copied into every worker | Leakage, cost, and contradiction | ContextPack has unrelated material | Load compact references by mission |
| Endless exploration | Maps grow without decisions | No saturation or curation rule | New candidates are synonyms or later-horizon ideas | Run saturation test and curate dispositions |
| Synonym capability explosion | Hundreds of overlapping capabilities | Vocabulary mistaken for architecture | Candidates lack unique actors, outcomes, or contracts | Merge, rename, split, and assign owners |
| Recursive micro-gates | Every minor action waits for approval | Risk model is not scaled | Green work repeatedly stops | Assign gates by action and consequence |
| Time-box theater | Worker remains active to satisfy duration | Time mistaken for value | Repeated low-value output | Queue outcomes and stop on marginal-value decline |
| Worker self-congratulation | Final report is the only evidence | Producer self-certifies | No independent review or test output | Separate builder, gate, and acceptance roles |
| File-count completeness | Progress rises when documents are added | Activity mistaken for maturity | No dimension-based evidence | Score independent dimensions and real integration |
| Technical console as product | End users navigate workers and logs | Experience and Control Planes are mixed | Main journey needs internal terminology | Design distinct surfaces with progressive disclosure |
| Mock presented as real | Fixture data appears as live capability | Status vocabulary is weak | No provenance or integration state | Label fixture truth and run real boundary tests |
| Single global status | "Done" hides incompatible states | Reporting compresses truth | Tests, release, and validation cannot be separated | Report evidence states independently |
| Deployment without rollback | External change has no recovery route | Release pressure overrides safety | Rollback is absent or untested | Block release and test recovery |
| Worker without STOP | Run cannot be interrupted safely | Runtime treated as a prompt | No kill or timeout path | Add wrapper, STOP, timeout, and stale-run detection |
| Parallel agents on shared files | Changes conflict or silently overwrite | Ownership is missing | Overlapping write scope | Isolate workspaces and assign single ownership |
| Local agent changes foundation | Shared contract drifts inside a mission | Mission authority is too broad | Contract changed without proposal | Revert or isolate change and open Foundation Change Proposal |
| Uninspected dependency | Package or service is added for convenience | Supply-chain and maintenance costs ignored | No provenance or alternative review | Perform dependency review and explicit acceptance |
| Secret in prompt or artifact | Credential appears in context or logs | Unsafe handling path | Secret scan or provider log finds it | Revoke as needed, remove exposure, and use secret systems |
| Personal data without purpose | Data is kept because it may help later | Violates minimization and trust | No declared purpose or retention | Delete or isolate, then define lawful purpose and controls |
| Human refusal ignored | Agent retries a rejected direction | Optimization overrides authority | Rejected decision reappears without new evidence | Preserve refusal and require a new human decision |
| Tests claimed but not run | Report says verified without output | Completion pressure | No command, result, or artifact | Mark unverified and run the applicable check |
| Technically complete, unusable | Components exist but journeys fail | Horizontal build replaced product evidence | No end-to-end user outcome | Re-plan around vertical journeys and user tests |
| Automating a bad decision | System scales an unvalidated workflow | Automation treated as progress | No evidence of usefulness | Reopen challenge and test a reversible alternative |

## 25. Canonical Example And Final Checklists

The complete synthetic example is [From a Creative Activity Vision to a Supervised Product](../examples/example-vision-to-product.md). It demonstrates separate profiles, competing product interpretations, inference corrections, product maps, a Foundation Freeze Candidate, three parallel development missions, integration, supervised release, rejection decisions, and a post-release revision.

### 25.1 Before Autonomy

- [ ] Vision is framed well enough for the next movement.
- [ ] Audience is identified or explicitly unknown.
- [ ] Sponsor, audience, and situation are not conflated.
- [ ] Allowed and forbidden sources are explicit.
- [ ] Data is classified and minimized.
- [ ] Mission charter and autonomy level are accepted.
- [ ] Human gates are named.
- [ ] STOP, timeout, recovery, and rollback exist as applicable.
- [ ] Reporting, cost, model, and tool policies are defined.
- [ ] Tests, expected evidence, and out-of-scope work are explicit.

### 25.2 Before Foundation Freeze

- [ ] Required domains have owners and boundaries.
- [ ] Synonyms and duplicate candidates are curated.
- [ ] Shared objects, states, transitions, and invariants are explicit.
- [ ] Truth layers and evidence states are defined.
- [ ] Permissions and autonomy are mapped.
- [ ] P0 and falsification verticals have been exercised.
- [ ] Contracts and compatibility checks exist.
- [ ] Security, privacy, and cost risks are reviewed.
- [ ] Alternatives and rejected decisions are preserved.
- [ ] Incubator work is separated from the active foundation.
- [ ] Product and engineering owners accept the candidate.

### 25.3 Before Parallel Development Workers

- [ ] Foundation version is referenced.
- [ ] Workspaces and write scopes are isolated.
- [ ] Shared file and contract ownership is explicit.
- [ ] Mission inputs and outputs are defined.
- [ ] Contract fixtures and tests are versioned.
- [ ] Budget, timeout, retry, and STOP rules exist.
- [ ] Merge order and dependencies are represented.
- [ ] Integration and independent review owners are assigned.
- [ ] Workers cannot alter foundation contracts silently.

### 25.4 Before Integration

- [ ] Unit and contract tests have actual results.
- [ ] Relevant integration and end-to-end paths have actual results.
- [ ] Contracts and migrations are compatible.
- [ ] Security, privacy, accessibility, performance, and cost checks match risk.
- [ ] Experience Plane and Control Plane show compatible truth.
- [ ] Rollback or compensation is available.
- [ ] No sensitive data is exposed in code, artifacts, logs, or prompts.
- [ ] Worker results can be rejected without corrupting source-of-truth state.
- [ ] Documentation and status have been updated.

### 25.5 Before External Action

- [ ] Designated human approval exists.
- [ ] Exact target and environment are verified.
- [ ] Payload or change set is reviewed.
- [ ] Data is minimized and its basis is documented.
- [ ] Dry-run or sandbox evidence exists when feasible.
- [ ] Rollback, compensation, or recovery is ready.
- [ ] Logs are redacted and auditable.
- [ ] Executable gate checks the authorized perimeter.
- [ ] No secret is visible or copied into the approval channel.
- [ ] Result verification is defined before execution.

### 25.6 Before Any 99 Percent Claim

- [ ] Real product has been executed across representative journeys.
- [ ] P0 verticals are integrated, not only mocked.
- [ ] Applicable tests have passed with retained evidence.
- [ ] Independent review and acceptance are complete.
- [ ] UX and accessibility have been validated.
- [ ] Security, privacy, and compliance reviews match the product's risk.
- [ ] Deployment and monitoring have been verified.
- [ ] Incident response and rollback have been exercised.
- [ ] Operating and user documentation is current.
- [ ] Human validation exists.
- [ ] Remaining limits are explicit and accepted.
- [ ] The weighted estimate, confidence, and evidence remain credible after challenge.

## Operating Entry Points

- Use the [Vision-to-Product Control Pack Template](../templates/vision-to-product-control-pack-template.md) to run the method in one compact artifact.
- Use the [Vision-to-Product Orchestrator](../prompts/system-prompts/vision-to-product-orchestrator.md) to configure an agent for this protocol.
- Use the [canonical example](../examples/example-vision-to-product.md) to review expected depth and evidence.
- Use [Quality Gates](14-quality-gates.md), [Testing and Sandboxing](17-testing-and-sandboxing.md), and [Public Method Limitations](19-public-method-limitations.md) before making maturity, safety, compliance, or release claims.

## Reference Frameworks

Use current, authoritative sources when a project turns these method concerns into binding requirements:

- [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32016R0679) for the applicable European data-protection obligations;
- [EDPB guidelines on automated decision-making and profiling](https://www.edpb.europa.eu/documents/guideline/automated-decision-making-and-profiling_en) for the interpretation of GDPR profiling and significant automated decisions;
- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) for testable web-accessibility criteria;
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and its [Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) for voluntary AI risk-management practices.

These references do not automatically apply in every jurisdiction or context, and following them does not itself prove legal compliance, accessibility conformance, security, or responsible operation. Record which version, scope, target, and qualified reviewer apply to the product.
