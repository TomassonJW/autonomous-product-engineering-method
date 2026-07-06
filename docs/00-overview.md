# Overview

The Autonomous Product Engineering Method turns ordinary-language product intent into structured, reviewable, agent-assisted software engineering work.

It exists because ambitious users often describe product visions in imprecise language, while AI agents tend to execute too literally. The result can be a shallow demo when the user expected a serious product, or an overbuilt system when the user only needed a focused workflow.

The method adds a disciplined translation layer between human intent and autonomous execution.

## What The Method Does

The method helps an agent or team:

1. Understand the user's real intent.
2. Detect ambition gaps and ambiguity.
3. Challenge the idea before building.
4. Split the product into coherent layers.
5. Separate end-user experience from control-plane operations.
6. Model capabilities as reusable, connected units.
7. Define events, artifacts, costs, risks, and permissions.
8. Create bounded worker missions.
9. Apply quality, safety, and cost gates.
10. Integrate feedback without rewriting the whole vision.

## What The Method Does Not Do

It does not:

- guarantee product-market fit;
- make unsafe autonomy safe by default;
- replace domain expertise;
- remove the need for tests;
- turn every vague idea into a complete platform automatically;
- prove that a product is premium without user evidence.

## Who It Is For

The method is useful for:

- founders describing ambitious tools;
- product architects converting vision into layers;
- coding agents preparing build plans;
- documentation engineers creating reusable project memory;
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
- report what is done, fragile, simulated, or blocked.

## Basic Flow

```text
User intent
  -> Product profile
  -> Ambition scale
  -> Challenge report
  -> Product layers
  -> Capability graph
  -> Dual UI model
  -> Architecture and runtime boundaries
  -> Worker missions
  -> Quality gates
  -> Verified report
```

## First Use

Start with [product-brief-template.md](../templates/product-brief-template.md), then use [deductive-product-profiler.md](../prompts/system-prompts/deductive-product-profiler.md). Do not start coding until the challenge gate has either passed or produced a bounded, accepted build slice.
