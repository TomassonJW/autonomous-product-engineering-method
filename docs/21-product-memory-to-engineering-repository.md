# Product Memory To Engineering Repository

Status: canonical method extension  
Version: 0.3.0  
Audience: product owners, product architects, documentation architects, coding agents, autonomous-agent designers, reviewers, and engineering operators

This extension defines how a rich product memory becomes a versioned engineering repository that an autonomous development agent can safely take over.

It is designed for long-lived, complex, or multi-session products. It does not require Notion specifically: **product memory workspace** means any durable knowledge system used for research, exploration, sources, decisions, and product definition. GitHub is used here as the canonical example of a shared versioned repository.

## 1. The Four Surfaces

| Surface | Primary responsibility | Must not become |
| --- | --- | --- |
| Product owner | Intent, product taste, material trade-offs, visible acceptance | Daily technical project manager |
| Product architect or conversational agent | Discovery, challenge, structured memory, semantic compilation | Permanent implementation owner |
| Product memory workspace | Rich context, research, alternatives, sources, decisions, long-term product memory | Live engineering backlog or implicit runtime contract |
| Engineering repository | Active product constitution, provenance, diffs, engineering state, code, tests, and evidence | Raw mirror of the memory workspace |
| Development agent or team | Clone, operational Git, architecture, planning, implementation, testing, delivery, and handoff | Silent re-author of the product |

The central rule is:

> The memory workspace may be broad and exploratory. The engineering repository must be explicit, versioned, development-ready, and readable without reopening the entire memory workspace.

## 2. Canonical Flow

```text
Ordinary-language exploration
  -> rich product memory
  -> Ready to Compile gate
  -> semantic compilation
  -> versioned engineering repository
  -> Ready to Develop gate
  -> development-agent takeover
  -> operational Git, code, tests, delivery, and learning
```

This flow creates two deliberate transitions instead of one vague handoff.

### Transition A: Ready to Compile

The active product definition is coherent enough to be compiled without inventing the product.

### Transition B: Ready to Develop

The repository contains a complete enough product contract, provenance, authority rules, and initial gates for an engineering agent to start without access to the original conversations or memory workspace.

## 3. Product Memory

The product memory workspace may contain:

- raw user language;
- research and source documents;
- rejected or competing product interpretations;
- historical reasoning;
- product profiling;
- domain vocabulary;
- workflows and journeys;
- UI/UX exploration;
- data and integration inventories;
- legal, security, operational, and economic constraints;
- decisions, hypotheses, unknowns, and counter-arguments;
- sensitive source material that must not enter a repository.

It should distinguish at least:

- `[FACT]`
- `[DECISION]`
- `[HYPOTHESIS]`
- `[PROPOSAL]`
- `[UNKNOWN]`
- `[CONSTRAINT]`
- `[SOURCE]`

The memory may be verbose. Its purpose is durable understanding, not minimum-token execution.

## 4. Ready To Compile Gate

The gate passes only when the active definition makes these functions unambiguous:

- product purpose and value;
- ambition level;
- users, roles, and critical contexts;
- domain vocabulary, objects, states, and rules;
- main journeys, tools, views, actions, and permissions;
- intended UI/UX and acceptance behavior when a UI exists;
- data sources, integrations, ownership, and sensitivity;
- scope, non-goals, phases, and change-of-scale conditions;
- constraints, costs, risks, and reversibility;
- accepted decisions and rejected alternatives;
- open questions classified as blocking or non-blocking;
- product, UX, technical, safety, and human-acceptance gates;
- repository visibility and redaction policy;
- versions of the method and local canons to pin.

The gate fails when compilation would require the compiler to:

- invent a product architecture;
- hide a material contradiction;
- turn a hypothesis into a decision;
- silently shrink the ambition;
- export unnecessary private or secret data;
- choose a public repository without explicit approval.

## 5. Semantic Compilation

Semantic compilation is not export, summarization, or copy-paste.

The compiler may reorganize and compress, but it must preserve:

- intent;
- priorities;
- scope boundaries;
- rejected alternatives that still constrain the product;
- decision ownership;
- uncertainty;
- acceptance evidence;
- source traceability.

The compiler should exclude by default:

- full conversation transcripts;
- duplicate notes;
- obsolete branches with no anti-reference value;
- secrets and credentials;
- unnecessary personal data;
- sensitive source documents not required for engineering;
- large raw snapshots when a verified source map is sufficient.

Every omission that could affect interpretation must be recorded in provenance.

## 6. Default Repository Constitution

A project repository may begin with no application code. The same repository later receives engineering planning, code, tests, and delivery evidence.

```text
AGENTS.md
README.md
product/
  00-index.md
  vision-and-value.md
  users-and-journeys.md
  domain-and-rules.md
  product-experience.md
  data-and-integrations.md
  scope-and-risks.md
  decisions-and-unknowns.md
  acceptance-gates.md
  ui-contract.md              # only when a UI exists
provenance/
  COMPILATION-MANIFEST.yml
  SOURCE-MAP.md
  PRODUCT-CHANGELOG.md
```

The names are defaults, not a cosmetic requirement. The following functions are mandatory:

1. agent authority and operating contract;
2. active product constitution;
3. decisions and unknowns;
4. acceptance gates;
5. provenance and source mapping;
6. pinned method and local-canon versions;
7. explicit start command for the development agent.

After takeover, the development agent adds or adapts:

- roadmap;
- backlog or board;
- current state;
- architecture decisions;
- handoff;
- operations and rollback;
- code, tests, migrations, and deployment assets.

## 7. Compilation Manifest

`COMPILATION-MANIFEST.yml` should record at least:

- project and context identifier;
- product-memory version;
- compilation date;
- compiler identity or role;
- target repository and branch;
- source pages or documents actually read;
- compiled files and their purpose;
- source-to-output mapping;
- omitted, redacted, or deferred material and reasons;
- facts, decisions, hypotheses, and unknowns still active;
- pinned method, UI, security, and local-canon versions;
- repository visibility;
- Ready to Compile result;
- Ready to Develop result;
- baseline commit and optional tag.

A raw memory snapshot is optional. When used for audit or re-compilation, it must be read-only and secondary to the semantic constitution.

## 8. Ready To Develop Gate

The repository is development-ready only when:

- it can be understood without the memory workspace;
- `AGENTS.md` defines authority, Git responsibility, gates, stop conditions, and reporting;
- the active constitution is internally coherent;
- the manifest and source map are complete;
- material contradictions are resolved or explicitly blocking;
- sensitive content is absent;
- method and local-canon versions are pinned;
- a baseline commit is identifiable;
- the development-agent start command exists;
- the first bounded proof is defined;
- if a UI exists, the local UI contract and first visible gate are explicit.

Do not confuse documentation volume with readiness. A small coherent package can pass. A large raw export can fail.

## 9. Development-Agent Takeover

The development agent must:

1. clone or update the repository without destroying local work;
2. verify the expected branch, baseline, and manifest;
3. read `AGENTS.md`, the manifest, and the complete product constitution;
4. produce a coverage map before implementation;
5. raise only material contradictions or missing authority;
6. create or update local planning, state, decisions, and handoff;
7. own operational Git and engineering execution;
8. preserve the active product constitution;
9. propose product-foundation changes explicitly instead of rewriting them for implementation convenience;
10. run the bounded preflight and first authorized proof.

For ordinary sessions, the agent resumes from Git, state, and handoff. It does not reopen the product-memory workspace.

## 10. Git Responsibility

A useful split is:

### Product architect or conversational agent

May:

- create the documentation-first repository;
- compile a product baseline;
- prepare product-amendment branches;
- open pull requests with product diffs;
- review implementation against the constitution.

Must not become the default daily code committer unless explicitly assigned.

### Development agent

Owns by default:

- local clone;
- branches and worktrees;
- implementation commits;
- integration;
- technical tags;
- tests and CI fixes;
- rollback;
- state and handoff.

### Product owner

Approves material product, security, cost, data, public-release, and irreversible decisions. The product owner does not need to operate Git.

## 11. Amendments

A strategic product change follows:

```text
Product discussion
  -> memory update
  -> versioned amendment
  -> repository branch or pull request
  -> readable product diff
  -> review and decision
  -> merge
  -> impact analysis by the development agent
```

Routine engineering discoveries stay in the repository. There is no general continuous bidirectional sync between memory and Git.

A memory edit is not active until compiled and merged.

## 12. Privacy And Repository Visibility

- Internal product repositories are private by default.
- Public release requires explicit approval and a redaction review.
- Method repositories may be public only when examples and sources are sanitized.
- Never copy secrets, credentials, unnecessary personal data, private transcripts, or confidential source files into a repository.
- Preserve references to restricted sources without embedding their content when engineering only needs provenance.

## 13. Lightweight Exception

A direct prompt-to-agent flow may be acceptable for a disposable spike when all are explicit:

- short lifetime;
- no production or external side effect;
- no durable data;
- no multi-session ownership;
- no expectation of reuse;
- planned deletion or absorption.

Once the work becomes durable, shared, operated, regulated, or strategically important, compile it into an engineering repository.

## 14. Anti-Patterns

Reject these patterns:

- raw workspace export presented as a product constitution;
- separate disposable specification repository followed by an unrelated code repository;
- continuous implicit sync between memory and Git;
- development agent reading every historical note before every session;
- product architect committing daily implementation by default;
- development agent silently editing product intent to fit the code;
- public repository selected by convenience;
- undocumented omissions during compilation;
- readiness inferred from file count;
- baseline without method-version pinning.

## 15. Minimal Checklists

### Ready To Compile

- active product interpretation is explicit;
- scope, users, domain, journeys, data, risks, and gates are coherent;
- blocking unknowns are resolved or declared;
- repository privacy is decided;
- redaction rules are known;
- compiler can preserve intent without invention.

### Ready To Develop

- repository constitution is complete enough to read standalone;
- provenance and source map exist;
- method and local canons are pinned;
- authority and Git ownership are explicit;
- baseline commit exists;
- first bounded proof and stop conditions are defined;
- development agent can take over without reopening the memory workspace.

## 16. Relationship To The Wider Method

This extension sits between product stabilization and engineering execution.

It complements:

- [Product-To-Engineering Layers](07-product-to-engineering-layers.md);
- [Autonomous Vision-to-Product Method](20-autonomous-vision-to-product.md);
- [Quality Gates](14-quality-gates.md);
- [Hermes Adapter](../adapters/hermes.md);
- [Engineering Repository Constitution Template](../templates/engineering-repository-constitution-template.md);
- [Compilation Manifest Template](../templates/source-compilation-manifest-template.yml);
- [Compile Product Memory Prompt](../prompts/starter-prompts/compile-product-memory-to-repository.md).

The key distinction is simple:

> Product memory maximizes understanding. The engineering repository maximizes explicit, versioned, shared execution.
