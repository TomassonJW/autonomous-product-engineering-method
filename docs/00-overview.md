# Overview

The Autonomous Product Engineering Method turns ordinary-language product intent into structured, reviewable, agent-assisted software engineering work.

It exists because ambitious users often describe product visions in imprecise language, while AI agents tend to execute too literally. The result can be a shallow demo when the user expected a serious product, or an overbuilt system when the user only needed a focused workflow.

The method adds a disciplined translation layer between human intent, durable product memory, versioned engineering contracts, and autonomous execution.

## What The Method Does

The method helps an agent or team:

1. Understand the user's real intent.
2. Detect ambition gaps and ambiguity.
3. Challenge the idea before building.
4. Separate facts, decisions, hypotheses, proposals, and unknowns.
5. Split the product into coherent layers.
6. Separate end-user experience from control-plane operations.
7. Model domains, capabilities, objects, states, events, artifacts, costs, risks, and permissions.
8. Stabilize versioned foundations.
9. Keep rich product memory without forcing every development session to reread it.
10. Compile the active product definition into a development-ready repository.
11. Create bounded worker missions.
12. Integrate and verify worker results independently.
13. Prepare supervised delivery and operation.
14. Integrate feedback without silently rewriting the whole vision.

## What The Method Does Not Do

It does not:

- guarantee product-market fit;
- make unsafe autonomy safe by default;
- replace domain expertise;
- remove the need for tests;
- turn every vague idea into a complete platform automatically;
- prove that a product is premium without user evidence;
- treat raw documentation export as an engineering contract;
- grant an agent authority merely because it can access a repository.

## Who It Is For

The method is useful for:

- founders describing ambitious tools;
- product architects converting vision into layers;
- coding agents preparing build plans;
- documentation engineers creating reusable product memory;
- teams compiling product definitions into engineering repositories;
- operators supervising autonomous workers;
- teams that want agentic speed without hidden chaos.

## The Central Contract

The user may speak naturally.

The system must respond with structured product truth.

That means the agent should:

- reformulate what it understood;
- mark assumptions as assumptions;
- ask only questions that change the trajectory;
- challenge hidden risks;
- define the right scope level;
- avoid false completion;
- report what is done, fragile, simulated, or blocked;
- preserve provenance when transforming memory into execution;
- distinguish product acceptance from technical success.

## Two Complementary Artifacts

### Product Memory

Product memory maximizes understanding. It can contain research, alternatives, sources, historical reasoning, sensitive references, decisions, hypotheses, and long-term context.

### Engineering Repository

The engineering repository maximizes explicit, versioned, shared execution. It contains the active product constitution, provenance, authority rules, gates, engineering state, code, tests, and evidence.

The repository is not a dump of the memory. It is a semantic compilation of the active product definition.

## Basic Flow

```text
User intent
  -> Product profile
  -> Challenge and competing interpretations
  -> Traceable inference
  -> Functional exploration
  -> Product maps and contracts
  -> Curated foundation
  -> Falsification verticals
  -> Foundation Freeze
  -> Product memory baseline
  -> Ready to Compile
  -> Engineering repository compilation
  -> Ready to Develop
  -> Isolated workers
  -> Integration and independent acceptance
  -> Supervised release
  -> Operational learning
```

## Authority Transitions

1. Before compilation, the approved product-memory version is authoritative for the definition to compile.
2. After the Ready to Develop baseline, the engineering repository is authoritative for the active product contract.
3. During operation, code, tests, data, services, and runtime evidence determine what actually works.
4. Product intent must not be silently rewritten by implementation convenience.
5. A memory change is not active until it is compiled and merged.

## First Use

Start with [product-brief-template.md](../templates/product-brief-template.md), then use [deductive-product-profiler.md](../prompts/system-prompts/deductive-product-profiler.md). For an ambitious product, continue with the [Autonomous Vision-to-Product Method](20-autonomous-vision-to-product.md) and its [Control Pack](../templates/vision-to-product-control-pack-template.md).

When the active product memory is coherent, use [Product Memory To Engineering Repository](21-product-memory-to-engineering-repository.md), the [Engineering Repository Constitution Template](../templates/engineering-repository-constitution-template.md), and the [Compilation Prompt](../prompts/starter-prompts/compile-product-memory-to-repository.md).

Do not start coding until the challenge gate and the Ready to Develop gate have passed, or an explicitly bounded falsification vertical has been approved.
