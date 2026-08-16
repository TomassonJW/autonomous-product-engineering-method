# Autonomous Product Engineering Method

An open method for turning ordinary-language product visions into safe, premium, autonomous AI-assisted software engineering workflows.

This repository is the public foundation for the **Autonomous Product Engineering Method**. It helps a person express an ambitious product idea in ordinary language, build a durable product memory, challenge and stabilize the product, compile the active definition into a versioned engineering repository, and then hand that repository to AI coding agents, autonomous workers, or human teams.

The method is intentionally tool-agnostic. It can be adapted to Codex, Hermes, CLI agents, chatbots, custom multi-agent systems, or human teams using AI as a product engineering partner.

## What This Is

This is a documentation, template, and prompt repository. It provides:

- a product-to-engineering method;
- product-memory and repository-handoff rules;
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
- domain and data contracts;
- capability maps;
- acceptance gates;
- repository authority;
- worker missions;
- tests;
- cost boundaries;
- safe execution plans.

## Product Memory And Engineering Repository

Complex products benefit from two distinct artifacts:

- **Product memory** maximizes understanding. It may contain research, alternatives, sources, historical reasoning, sensitive references, decisions, hypotheses, and long-term context.
- **Engineering repository** maximizes explicit, versioned, shared execution. It contains the active product constitution, provenance, authority rules, gates, engineering state, code, tests, and evidence.

The canonical bridge is:

```text
Ordinary-language exploration
  -> rich product memory
  -> Ready to Compile
  -> semantic compilation
  -> versioned engineering repository
  -> Ready to Develop
  -> development-agent takeover
  -> operational Git, implementation, delivery, and learning
```

Read [Product Memory To Engineering Repository](docs/21-product-memory-to-engineering-repository.md) for the complete contract.

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
  -> Clarification and challenge
  -> Traceable project inference
  -> Functional exploration
  -> Product maps and contracts
  -> Curation and falsification verticals
  -> Versioned Foundation Freeze
  -> Product memory baseline
  -> Engineering repository compilation
  -> Ready to Develop gate
  -> Isolated development agents
  -> Integration and independent gates
  -> Supervised delivery and operation
  -> Learning and foundation revision
```

The complete product operating protocol is defined in [Autonomous Vision-to-Product Method](docs/20-autonomous-vision-to-product.md). The memory-to-repository transition is defined in [Product Memory To Engineering Repository](docs/21-product-memory-to-engineering-repository.md).

## Start Here

1. Read [Overview](docs/00-overview.md).
2. Read [Core Principles](docs/02-core-principles.md).
3. Use the [Product Brief Template](templates/product-brief-template.md).
4. Run the [Autonomous Product Architect prompt](prompts/system-prompts/autonomous-product-architect.md).
5. Apply the [Challenge Gate](docs/06-challenge-gate.md) before building.
6. For an ambitious end-to-end product, use the [Vision-to-Product Control Pack](templates/vision-to-product-control-pack-template.md) and [Vision-to-Product Orchestrator](prompts/system-prompts/vision-to-product-orchestrator.md).
7. When the product memory is stable, use the [Engineering Repository Constitution Template](templates/engineering-repository-constitution-template.md) and [Compile Product Memory prompt](prompts/starter-prompts/compile-product-memory-to-repository.md).
8. Apply [Quality Gates](docs/14-quality-gates.md) before calling anything done.

## Repository Map

- [docs/](docs/00-overview.md): the method, principles, Vision-to-Product protocol, product-memory bridge, gates, runtime model, risks, and limitations.
- [templates/](templates/product-brief-template.md): reusable product, repository, manifest, and worker artifacts.
- [prompts/](prompts/README.md): copy-pasteable prompts for discovery, compilation, agents, and reviews.
- [runbooks/](runbooks/setup-codex.md): operational guides for common environments.
- [adapters/](adapters/codex.md): tool-specific adaptation notes, including [Hermes](adapters/hermes.md).
- [examples/](examples/README.md): public-safe examples.
- [case-studies/](case-studies/hermes-agency-os/README.md): sanitized lessons from Hermes Agency OS.
- [audits/](audits/method-self-audit.md): self-critique, risk register, anti-patterns, and alternatives.

## Translations

English is the canonical source. French is maintained as an official translation:

- [French README](translations/fr/README.md)
- [Translation policy](TRANSLATION_POLICY.md)
- [French glossary](translations/fr/GLOSSARY.md)
- [French translation status](translations/fr/TRANSLATION_STATUS.md)

## Safety Position

The method separates actions into three zones:

- **Green**: local, reversible, testable, low risk, no external side effect.
- **Orange**: structural, costly, impactful, or ambiguous; requires proposal before execution.
- **Red**: irreversible, destructive, public, financial, secret-related, production-changing, or externally messaging; requires explicit human approval.

No agent should publish, delete, spend money, expose services, send messages, change production, or handle secrets without explicit authorization and verifiable safeguards.

Internal product repositories are private by default. Public release requires explicit approval and a redaction review.

## Current Status

This repository is **v0.3**, an expanded public foundation. It adds the Product Memory To Engineering Repository contract, a documentation-first repository constitution, a compilation manifest, an operational compilation prompt, and an updated Hermes takeover model.

The method still requires field validation across diverse products, teams, memory systems, and agent environments. It is not a final standard, certification, framework, or guarantee of safe autonomy.

## License

MIT. See [LICENSE](LICENSE).

MIT was chosen because this repository includes reusable templates, prompts, and operational snippets that people should be able to copy, adapt, and embed in their own workflows. A Creative Commons license can still be considered later if the project becomes primarily essay-style documentation.
