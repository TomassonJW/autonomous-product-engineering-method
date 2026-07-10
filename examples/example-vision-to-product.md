# Example: From A Creative Activity Vision To A Supervised Product

This example is synthetic and public-safe. It demonstrates method decisions and evidence states. It does not claim that the fictional product was built or legally validated.

## 1. Initial Vision

A user says:

> "I want an intelligent system to manage the content, photos, website, and development of my creative activity."

Initial maturity: fragmentary. The statement names several areas but does not define the main problem, audience, operating model, or autonomy boundary.

## 2. First Interpretation

`[HYPOTHESIS]` The user wants one workspace that turns raw creative material into reviewed website updates while preserving control over publication.

This is not yet accepted because "development" may mean business development, website development, software development, or all three.

## 3. Adaptive Questions

The profiler asks five questions.

| Question | Decision It Can Change | Answer |
| --- | --- | --- |
| Which result currently consumes the most time: organizing material, producing content, updating the website, or coordinating technical work? | P0 journey and active interpretation | Producing and publishing coherent website content from scattered photos and notes |
| Who uses the system first, and who consumes its result? | Sponsor and audience profiles, Experience Plane | One studio owner uses it; existing and prospective clients consume the public result |
| May the system publish by itself? | Autonomy and external-action gate | No. It may prepare a draft, but the owner must approve every publication |
| What does "development" mean in this first version? | Domain scope and roadmap | Improving the website and planning future digital tools, not autonomously building a business strategy |
| Where do photos and notes currently live? | Data flow, integrations, and privacy | Local folders and a cloud drive; access policy is not yet defined |

Interview exit decision:

- The main problem and primary audience are explicit.
- Publication is a red action requiring human approval.
- Cloud-drive access remains `[UNKNOWN]`, so the first vertical will use a local import folder.
- Further questions are more cheaply answered through a reversible prototype and usability review.

## 4. Separate Profiles

### 4.1 Sponsor Profile

- `[FACT]` The studio owner is the initial operator and publication approver.
- `[FACT]` The owner wants less repetitive preparation work.
- `[CONSTRAINT]` The owner does not authorize autonomous publication.
- `[SIGNAL]` The owner wants a system that may later coordinate digital product work.
- `[UNKNOWN]` The acceptable recurring operating cost has not been quantified.

No personality or psychological traits are inferred.

### 4.2 Audience Profile

Primary public audience:

- prospective clients reviewing recent work;
- existing clients checking portfolio updates;
- mobile visitors with limited time.

Needs:

- fast loading;
- clear project context;
- accessible images and captions;
- truthful publication dates;
- no exposure to internal drafts or operational notes.

### 4.3 Situational Profile

- `[FACT]` Source material is split across local folders, cloud storage, and notes.
- `[FACT]` The current website requires manual updates.
- `[HYPOTHESIS]` Content delay is caused more by curation and review than by writing alone.
- `[CONSTRAINT]` The first alpha must run locally and produce drafts only.
- `[UNKNOWN]` The current website's publishing API and rollback behavior have not been audited.

## 5. Inference Register

| ID | Status | Statement | Support | Counter-Evidence | Product Consequence | Risk If Wrong |
| --- | --- | --- | --- | --- | --- | --- |
| INF-001 | FACT | Publication requires owner approval | Explicit answer | None | Publishing capability stays A0 until approval, then a bounded external action | Unauthorized public change |
| INF-002 | HYPOTHESIS | One workspace should cover content, media, and website review | User grouped these activities | Separate specialized tools may be clearer | Explore a unified Experience Plane with modular domains | Overbuilt workspace |
| INF-003 | HYPOTHESIS | Photo curation is the main bottleneck | Material is scattered and publication is delayed | Writing quality may be the larger problem | First falsification vertical includes real photo selection | Wrong P0 priority |
| INF-004 | STRONG DEDUCTION | Internal operations must be separated from the public content workflow | One non-technical operator, multiple internal steps, public audience | None found | Separate Experience and Control Planes | Confusing or unsafe UI if ignored |
| INF-005 | UNKNOWN | Cloud-drive integration is appropriate for P0 | Existing source location | Access, cost, provider, and retention are undefined | Keep integration in incubator | Premature dependency and data exposure |

### Red Team Result

INF-002 initially read "The user needs a unified operating system for the whole activity." The reviewer rejected it as too broad and weakly falsifiable. It was replaced by the narrower workspace hypothesis above.

## 6. Three Product Interpretations

### Interpretation A: Publishing Assistant

A focused tool imports selected photos and notes, proposes a structured article, and prepares a website draft for approval.

- Advantage: small and testable.
- Risk: does not address curation across the broader activity.

### Interpretation B: Creative Activity Workspace

A modular workspace manages source material, content projects, review, and website delivery, with future extensions for digital project planning.

- Advantage: matches the grouped workflow and long-term ambition.
- Risk: may become a broad internal console instead of a usable product.

### Interpretation C: Autonomous Digital Agency

A multi-agent system manages content strategy, media, website, development, analytics, and business growth.

- Advantage: captures the maximum implied ambition.
- Risk: unsupported scope, unsafe autonomy, high operating burden, and no current evidence.

### Decision

`[DECISION]` Interpretation B is the active vision, implemented first through the publishing vertical from Interpretation A. Interpretation C moves to the incubator. It is not treated as a committed roadmap.

## 7. Challenge Record

Strongest counter-hypothesis:

> A disciplined folder convention plus a website drafting template may solve most of the problem without a new product.

Falsification approach:

- Run one manual structured workflow using the proposed objects and states.
- Measure preparation time, missing information, revision cycles, and user confusion.
- If the workflow creates little improvement, do not automate it.

Rejected request expansion:

- autonomous publication: rejected by the sponsor;
- automatic cloud ingestion: deferred until access and privacy review;
- business-development recommendations: incubated, not P0;
- multi-user collaboration: deferred until a second real operator exists.

## 8. Domain Atlas

| Domain | Purpose | Inside | Outside | Owner |
| --- | --- | --- | --- | --- |
| Source Library | Register and curate approved source material | Imports, metadata, selection, provenance | Public publication | Product owner |
| Editorial Projects | Turn selected material into structured drafts | Brief, draft, review, revision | Website credentials | Editorial owner |
| Delivery | Prepare and verify publishable packages | Preview, validation, approval request, release evidence | Content strategy | Integration owner |
| Operations | Expose runs, failures, cost, permissions, and audit | Jobs, logs, gates, rollback state | End-user writing journey | Operator |
| Project Incubator | Preserve later digital product candidates | Hypotheses, proposals, rejected ideas | Active P0 contracts | Product owner |

## 9. Capability Atlas

| Capability | Domain | Actor And Outcome | Inputs And Outputs | Safety Zone | Disposition |
| --- | --- | --- | --- | --- | --- |
| Register source material | Source Library | Owner creates traceable usable material | Files and notes -> source records | Green locally | Foundation candidate |
| Curate project set | Source Library | Owner selects relevant material | Source records -> approved selection | Green | Foundation candidate |
| Create editorial brief | Editorial Projects | Owner frames the intended page or article | Selection and intent -> brief | Green | Foundation candidate |
| Generate structured draft | Editorial Projects | Owner receives a reviewable proposal | Brief -> draft with provenance | Green | Active P0 |
| Review and revise | Editorial Projects | Owner corrects and accepts content | Draft -> accepted revision | Green | Active P0 |
| Build preview package | Delivery | Owner sees the exact proposed result | Accepted revision -> preview package | Green | Active P0 |
| Request publication approval | Delivery | Owner receives an explicit release gate | Preview -> approval record | Orange proposal | Active P0 |
| Publish website update | Delivery | Approved content reaches the verified target | Approved package -> public result | Red | Deferred until integration audit |
| Inspect run truth | Operations | Operator sees status, errors, cost, and gates | Run records -> Control Plane | Green | Foundation candidate |
| Suggest digital project | Incubator | Owner sees a traceable later-horizon candidate | Learning signal -> proposal | Green proposal only | Incubator |

## 10. Module Map

| Module | Capabilities | Owns | Must Not Own |
| --- | --- | --- | --- |
| `source-registry` | Register and curate source material | Source records and provenance | Website publication |
| `editorial-workbench` | Brief, draft, review, revise | Editorial project and revision state | Credentials or public deployment |
| `delivery-package` | Preview and approval request | Immutable release candidate package | Source library mutation |
| `operations-ledger` | Inspect run truth | Events, gate results, cost, failure evidence | End-user editorial content |
| `incubator` | Suggest digital projects | Unaccepted candidates | Active foundation contracts |

The modules are examples of ownership boundaries, not mandated technology packages.

## 11. Objects And States

### SourceItem

```text
discovered -> registered -> reviewed -> approved
                         -> rejected
approved -> archived
```

Invariant: only `approved` source items may enter an editorial release candidate.

### EditorialProject

```text
idea -> framed -> drafting -> in_review -> accepted
                       -> changes_requested -> drafting
accepted -> packaged
```

Invariant: every accepted revision references its source selection and approval actor.

### ReleaseCandidate

```text
prepared -> previewed -> approval_requested -> approved
                                      -> rejected
approved -> released -> verified
                  -> failed -> rolled_back
```

Invariant: `released` requires a separate, unexpired approval tied to the exact payload and target.

## 12. Cross-Domain Composition

Composition: Create a reviewed website update.

```text
Owner selects approved SourceItems
  -> Editorial Project creates a brief
  -> drafting produces a revision with provenance
  -> owner requests changes or accepts
  -> Delivery builds an immutable preview package
  -> Operations records checks and cost
  -> owner approves or rejects the exact package
  -> publication remains blocked in the local alpha
```

Partial failure behavior:

- If an image lacks rights or provenance, packaging fails with a specific source record.
- If draft generation fails, the editorial project remains `drafting`; no release state changes.
- If preview generation fails, the accepted revision remains valid and can be repackaged.
- If approval expires, the package returns to `previewed` and must be reviewed again.

## 13. UI Surface Map

### Experience Plane

Primary screen: "Create a website update"

1. Select material.
2. Describe the intended result.
3. Review the proposed structure.
4. Edit and approve content.
5. Inspect the exact preview.
6. Request publication approval.

The default path does not show workers, model routing, token cost, queue names, or raw logs.

Advanced paths expose source provenance, revision comparison, accessibility warnings, and estimated operating cost.

### Control Plane

Operator surfaces expose:

- run and queue state;
- model and tool use;
- errors and retry count;
- gate results;
- data class;
- approval and expiration state;
- package hash and target;
- rollback readiness.

## 14. P0 And Falsification Verticals

### P0-1: Manual Structured Workflow

Goal: test whether the object model and review journey reduce friction without building automation.

Evidence required:

- one real synthetic-safe content project;
- timed steps;
- missing fields;
- revision count;
- owner feedback;
- rejected or changed states.

### P0-2: Local Draft Vertical

Goal: cross the actual local boundaries from selected files to a persisted draft and preview.

Boundaries:

```text
local import
  -> source registry
  -> editorial project
  -> generated draft
  -> owner revision
  -> local preview
  -> operations evidence
```

Explicit exclusion: no cloud integration and no public website call.

### P0-3: Approval Contract Probe

Goal: prove that approval is tied to the exact target and payload, expires, can be rejected, and does not imply execution.

This probe may use a fake publication adapter. Its result is labeled `fixture-integrated`, not real integration.

## 15. Foundation Freeze Candidate 0.1

Accepted foundation:

- North Star: help a creative operator turn traceable source material into coherent, reviewed digital publications without losing control of external action.
- Active domains: Source Library, Editorial Projects, Delivery, Operations.
- Incubator: Project Incubator and broader digital-agency functions.
- Core objects: SourceItem, EditorialProject, Revision, ReleaseCandidate, Approval, RunEvidence.
- UI rule: one simple editorial Experience Plane and a separate operational Control Plane.
- Autonomy: local preparation A2; integration preparation A3; publication remains red and requires exact human approval.
- Data rule: local-only P0; no secret or cloud credential enters model context.
- P0 contracts: source provenance, revision state, immutable release package, scoped approval, run evidence.

Not frozen:

- website provider;
- cloud-drive provider;
- multi-user roles;
- business analytics;
- automatic publication;
- long-running autonomous operation.

Freeze Gate result: `accepted-with-reservations` for local alpha. The publication domain contract remains specified but not authorized or integrated.

## 16. Roadmap

### Foundation P0

- exercise manual structured workflow;
- build local draft vertical;
- validate object states and provenance;
- validate scoped approval contract with fixture;
- run privacy and threat review.

### First Usable Release

- support repeatable local editorial projects;
- accessible preview and correction flow;
- versioned exports;
- truthful operations evidence;
- backup and restore.

### Operational Release

- audit real website adapter;
- define credentials boundary outside model context;
- run sandbox integration;
- test rollback and target verification;
- define monitoring, incident response, and support;
- complete public-product legal and accessibility review.

### Incubator

- cloud source synchronization;
- multi-user editorial review;
- digital project planning;
- analytics-informed learning;
- broader agent portfolio.

## 17. Three Parallel Development Missions

Parallel work starts only after Foundation Freeze Candidate 0.1 is accepted.

### Mission DEV-01: Source Registry

- Owns: `source-registry` module and its tests.
- Inputs: SourceItem contract, local import policy, synthetic fixture set.
- Outputs: registration, provenance, review states, contract tests.
- Must not edit: shared state definitions or delivery contracts.

### Mission DEV-02: Editorial Workbench

- Owns: `editorial-workbench` module and Experience Plane slice.
- Inputs: EditorialProject and Revision contracts, UX state map.
- Outputs: brief, draft, revision, accepted state, accessibility evidence.
- Must not edit: operations ledger or approval policy.

### Mission DEV-03: Operations Ledger

- Owns: run events, gate evidence, cost and error truth.
- Inputs: event contract and Control Plane requirements.
- Outputs: append-only run records and operator inspection view.
- Must not edit: editorial content or model prompts.

Execution DAG:

```text
Foundation 0.1
  -> DEV-01
  -> DEV-02
  -> DEV-03

DEV-01 + DEV-02 + DEV-03
  -> INT-01 Local Draft Integration
  -> REV-01 Independent Review
  -> ACC-01 Local Alpha Acceptance
```

The agents use isolated workspaces. A defect in a shared contract creates a Foundation Change Proposal instead of a local contract rewrite.

## 18. Integration Gate

INT-01 must prove:

- SourceItem provenance survives through the preview;
- invalid source states cannot enter a package;
- editorial revisions preserve history;
- Experience Plane and Control Plane show compatible state;
- a failed draft does not advance release state;
- logs contain no source content beyond approved metadata;
- accessibility checks cover keyboard flow, labels, errors, and image alternatives;
- cost and model use are visible to the operator;
- all claims distinguish local integration from real website integration.

Rejected result example:

DEV-02 initially returns a beautiful preview that reads images directly from an untracked temporary folder. The integration owner rejects it because provenance and reproducibility fail. The builder must use approved SourceItem references.

## 19. Local Alpha Acceptance

Evidence states after a successful local alpha could be:

| Area | Evidence State |
| --- | --- |
| Source registry | Integrated locally |
| Editorial workbench | End-to-end verified locally |
| Operations ledger | Integrated locally |
| Approval contract | Fixture-integrated |
| Website publishing | Specified only |
| Cloud import | Unknown and incubated |
| Target-user validation | One sponsor session, insufficient for broader user validation |
| Public release readiness | Not ready |

Verdict: `accepted-with-reservations` as a local alpha. It is not a production-ready or publicly validated product.

## 20. Gates Before Real Publication

Before publication can be proposed:

- inspect the real website's API, preview, authentication, rate limits, and rollback;
- keep credentials in a dedicated secret mechanism outside prompts and logs;
- verify exact site, environment, route, payload, and media set;
- implement a dry-run or staging path;
- test package identity and approval expiration;
- run security, privacy, accessibility, performance, and link checks;
- define public privacy information, support, and incident handling as applicable;
- assign publisher and acceptance owners;
- obtain explicit approval for the exact release candidate;
- verify the public result and retain rollback evidence.

Readiness is not authorization. A green technical gate does not replace publication approval.

## 21. Post-Release Learning

Suppose supervised releases show:

- users reach project pages but rarely open long descriptions;
- the owner spends more time selecting images than revising text;
- mobile images load too slowly;
- one accessibility review finds inconsistent alternative text.

Competing explanations:

- descriptions may be too long;
- visitors may primarily seek visual evidence;
- page hierarchy may hide the narrative;
- the audience sample may be unrepresentative.

Decisions:

- `[STRONG DEDUCTION]` Image selection remains a major operator cost across repeated releases.
- `[HYPOTHESIS]` A guided curation capability may reduce that cost.
- `[DECISION]` Create a curation-assistant candidate in the incubator; do not auto-select or auto-publish.
- `[DECISION]` Treat image performance and alternative-text quality as operational release gates.
- `[REJECTED]` Do not remove descriptions based only on click depth.

## 22. Foundation 0.2 Proposal

Proposed changes:

- add an ImageVariant object and performance contract;
- add accessibility evidence to ReleaseCandidate;
- add a guided curation capability as an A1 suggestion workflow;
- preserve manual final selection;
- add real performance and accessibility thresholds.

Unchanged:

- North Star;
- separate Experience and Control Planes;
- human publication approval;
- source provenance;
- immutable release candidate package.

The proposal requires product, accessibility, and engineering review before Foundation 0.2 becomes active.

## 23. Completeness Snapshot

| Dimension | Level 0-5 | Evidence |
| --- | --- | --- |
| Conceptual coverage | 4 | Independent review of active domains and exclusions |
| Inference maturity | 3 | Key hypotheses exercised locally; public audience evidence remains weak |
| Foundation readiness | 4 for local alpha | Candidate accepted with stated reservations |
| Integrated P0 verticals | 3 | Local real components integrated; website adapter remains fixture-only |
| UX and accessibility | 3 | Local journey tested; broader user validation incomplete |
| Security and privacy | 2 | Policies specified; real provider and deployment boundaries not exercised |
| Deployment and operation | 1 | Framed only |
| Human and user validation | 2 | Sponsor evidence only |
| Rollback capability | 1 | Local recovery framed; public rollback untested |

No global 99 percent claim is credible. The next legitimate progress event is a sandboxed real website integration with rollback evidence, followed by independent public-release review.

## 24. What The Example Proves

This example shows how the method:

- starts from ambiguous ordinary language;
- asks a bounded set of decisive questions;
- avoids covert personal profiling;
- separates facts, hypotheses, and unknowns;
- compares three product interpretations;
- preserves rejected scope;
- maps domains, capabilities, modules, objects, states, compositions, and UI;
- tests a foundation through falsification verticals;
- launches isolated agents against shared contracts;
- rejects attractive but invalid output;
- distinguishes fixture integration from real integration;
- keeps publication behind a human gate;
- revises the foundation from real evidence without rewriting the North Star.
