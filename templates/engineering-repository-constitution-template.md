# Engineering Repository Constitution Template

Use this template when compiling a rich product memory into a repository that a development agent can take over.

The template defines functions, not mandatory file counts. Small products may merge sections. Complex products may split them further. Preserve the order of authority and provenance.

## Repository Status

- Project:
- Repository:
- Visibility: private / public
- Product memory identifier:
- Product memory version:
- Compilation date:
- Method version:
- Local canon versions:
- Baseline branch:
- Baseline commit:
- Baseline tag:
- Ready to Compile: pass / fail
- Ready to Develop: pass / fail
- Development owner:
- Product acceptance owner:

## `AGENTS.md`

Define:

- repository mission;
- authority order;
- operational Git owner;
- branch and worktree policy;
- product-foundation change policy;
- safety and secret rules;
- required reading order;
- session opening and closure;
- stop conditions;
- reporting expectations;
- first bounded proof;
- UI gate and explicit stop when a UI exists.

## `README.md`

Include:

- one-paragraph product summary;
- current maturity;
- repository map;
- canonical reading order;
- development-agent start command;
- current baseline;
- privacy statement;
- links to product constitution and provenance.

## `product/00-index.md`

- Active product version:
- Purpose:
- Ambition level:
- Scope:
- Non-goals:
- Canonical documents:
- Reading order:
- Blocking decisions:
- First bounded proof:
- Product acceptance owner:
- Product amendment procedure:

## `product/vision-and-value.md`

### Current problem

### Desired future state

### Product purpose

### Value by user group

### Critical situations

### Success evidence

### Failure and drift signals

### Serious alternatives

## `product/users-and-journeys.md`

For each user or role:

- responsibilities;
- context and devices;
- capability level;
- critical jobs;
- primary journeys;
- permissions;
- accessibility needs;
- failure and recovery needs.

## `product/domain-and-rules.md`

### Canonical vocabulary

### Objects and ownership

### States and transitions

### Invariants

### Rules and exceptions

### Human responsibilities

### Sources of truth

### Ambiguities that must not become automatic technical concepts

## `product/product-experience.md`

### Information architecture

### Tools, modules, views, and pages

### Actions and permissions

### Empty, loading, error, and confirmation states

### Desktop, tablet, and mobile behavior

### Density, themes, accessibility, and preferences

### Representative fixtures

### Save, draft, undo, history, and recovery behavior

### UI capability decisions

Explicitly accept, defer, or reject capabilities such as tabs, split view, command palette, workspaces, session restore, deep links, focus mode, batch actions, drag and drop, and actionable notifications.

## `product/ui-contract.md`

Omit this file when no user interface exists.

Pin:

- applicable UI canon and version;
- local exceptions;
- navigation model;
- persistent shell;
- page registry;
- responsive policy;
- preferences and persistence;
- first visible gate;
- explicit stop condition;
- acceptance evidence.

## `product/data-and-integrations.md`

### Existing sources

### Data ownership

### Master, derived, calculated, and temporary data

### Import, export, migration, and synchronization

### Required and optional APIs

### Sensitive data

### Retention, deletion, and portability

### Unknowns requiring audit

## `product/scope-and-risks.md`

### Included

### Excluded

### Current ambition level

### Expected first prototype coverage

### Change-of-scale conditions

### Security and privacy

### Compliance

### Hosting and operation

### Costs and paid dependencies

### Maintenance and reversibility

### Human dependencies

### Active risks

## `product/decisions-and-unknowns.md`

Use explicit status markers:

- `[FACT]`
- `[DECISION]`
- `[HYPOTHESIS]`
- `[PROPOSAL]`
- `[UNKNOWN]`
- `[CONSTRAINT]`

For each material item record:

- statement;
- owner;
- rationale or sources;
- alternatives;
- product consequence;
- risk if wrong;
- blocking status;
- review trigger.

## `product/acceptance-gates.md`

Keep separate when relevant:

- memory coherence;
- Ready to Compile;
- Ready to Develop;
- feasibility;
- product conformity;
- UX and readability;
- coverage;
- data coherence;
- technical correctness;
- safety and operation;
- explicit product-owner acceptance.

A technical pass is not product acceptance.

## `provenance/COMPILATION-MANIFEST.yml`

Use [source-compilation-manifest-template.yml](source-compilation-manifest-template.yml).

## `provenance/SOURCE-MAP.md`

For each compiled function record:

| Compiled file or section | Source identifiers | Status | Notes |
| --- | --- | --- | --- |
| | | fact / decision / hypothesis / mixed | |

Also list:

- sources not read;
- restricted sources referenced but not copied;
- omitted branches;
- redactions;
- unresolved contradictions;
- known freshness limits.

## `provenance/PRODUCT-CHANGELOG.md`

Record product baselines and amendments:

| Version | Date | Baseline or PR | Product change | Source memory version | Decision owner |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Ready To Develop Checklist

- [ ] The repository is understandable without the memory workspace.
- [ ] `AGENTS.md` defines authority and operational Git ownership.
- [ ] The product constitution is coherent and complete enough for the first bounded proof.
- [ ] Blocking contradictions are resolved or explicit.
- [ ] Provenance and source mapping exist.
- [ ] Secrets and unnecessary private data are absent.
- [ ] Method and local-canon versions are pinned.
- [ ] The baseline commit is identifiable.
- [ ] The development-agent start command exists.
- [ ] UI contract and first visible stop gate exist when applicable.
- [ ] Product-owner acceptance is not pre-claimed.

## Development-Agent Start Command

```text
Take over this project from repository [OWNER/REPO], baseline [TAG OR COMMIT]. Clone or update the local checkout, then read AGENTS.md, the compilation manifest, and the full product constitution in the stated order. Verify Ready to Develop. You own operational Git, local planning, and implementation. Do not reopen the product-memory workspace unless an explicit amendment requires it. Run the bounded preflight and only the first authorized proof. Respect every explicit human stop gate.
```
