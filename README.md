# Autonomous Product Engineering Method

An open method for turning ordinary-language product visions into safe, premium, autonomous AI-assisted software engineering workflows.

This repository is the initial public foundation for the **Autonomous Product Engineering Method**. It helps a person express an ambitious product idea in ordinary language, then guides AI agents, coding agents, or autonomous workers through product profiling, challenge, architecture, UX/UI modeling, capability mapping, safety gates, cost governance, execution, testing, reporting, and feedback integration.

The method is intentionally tool-agnostic. It can be adapted to Codex, Hermes, CLI agents, chatbots, custom multi-agent systems, or human teams using AI as a product engineering partner.

## What This Is

This is a documentation and prompt repository. It provides:

- a product-to-engineering method;
- reusable templates;
- copy-pasteable prompts;
- safety and quality gates;
- runbooks for autonomous workers;
- adapters for common agentic environments;
- a sanitized case study;
- self-audits and known risks.

This is **not** a magic automation claim. The method does not remove the need for judgment, testing, product taste, security review, or human approval for dangerous actions.

## Core Idea

Users should not need to speak like product managers, software architects, UX researchers, or DevOps engineers.

They can say:

> "I want a tool that builds apps for me."

or:

> "The UI feels poor. I want something premium but still powerful."

The method forces the system to translate that language into:

- product intent;
- ambition level;
- user types;
- non-goals;
- risks;
- product layers;
- UX implications;
- architecture implications;
- capability maps;
- worker missions;
- tests;
- quality gates;
- cost boundaries;
- safe execution plans.

## Premium Means Clarity, Not Decoration

In this method, **premium** does not mean ornamental design, vague polish, or expensive models everywhere.

Premium means:

- immediate clarity;
- low cognitive load;
- reliable behavior;
- honest status;
- visible uncertainty;
- no hidden cost;
- strong defaults;
- deep configurability when needed;
- powerful but safe automation;
- testable journeys;
- user trust.

The target is the best of two worlds:

- Apple-like clarity, coherence, smoothness, and UX quality;
- Windows-like depth, configurability, control, and openness.

Avoid both extremes: beautiful but closed and limited, or powerful but cognitively heavy and messy.

## Method Flow

```text
Ordinary language
  -> Product profiling
  -> Ambition calibration
  -> Challenge gate
  -> North Star and product layers
  -> Domain and capability maps
  -> Dual UI model
  -> Architecture and event/artifact model
  -> Cost and safety policies
  -> Worker mission charters
  -> Implementation plan
  -> Tests and quality gates
  -> Run reports
  -> Feedback integration
```

## Start Here

1. Read [Overview](docs/00-overview.md).
2. Read [Core Principles](docs/02-core-principles.md).
3. Use the [Product Brief Template](templates/product-brief-template.md).
4. Run the [Autonomous Product Architect prompt](prompts/system-prompts/autonomous-product-architect.md).
5. Apply the [Challenge Gate](docs/06-challenge-gate.md) before building.
6. Use [Quality Gates](docs/14-quality-gates.md) before calling anything done.

## Repository Map

- [docs/](docs/00-overview.md): the method, principles, gates, runtime model, risks, and limitations.
- [templates/](templates/product-brief-template.md): reusable structured artifacts.
- [prompts/](prompts/README.md): copy-pasteable prompts for agents and review flows.
- [runbooks/](runbooks/setup-codex.md): operational guides for common environments.
- [adapters/](adapters/codex.md): tool-specific adaptation notes.
- [examples/](examples/README.md): public-safe examples.
- [case-studies/](case-studies/hermes-agency-os/README.md): sanitized lessons from Hermes Agency OS.
- [audits/](audits/method-self-audit.md): self-critique, risk register, anti-patterns, and alternatives.

## Safety Position

The method separates actions into three zones:

- **Green**: local, reversible, testable, low risk, no external side effect.
- **Orange**: structural, costly, impactful, or ambiguous; requires proposal before execution.
- **Red**: irreversible, destructive, public, financial, secret-related, production-changing, or externally messaging; requires explicit human approval.

No agent should publish, delete, spend money, expose services, send messages, change production, or handle secrets without explicit authorization and verifiable safeguards.

## Current Status

This repository is **v0.1**, an initial public foundation. It is meant to be used, challenged, and improved. It is not a final standard, certification, framework, or guarantee of safe autonomy.

## License

MIT. See [LICENSE](LICENSE).
