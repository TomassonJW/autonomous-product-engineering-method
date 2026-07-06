# Context And Capability Mesh

Agentic products become fragile when every module stores its own truth or every worker loads everything into context.

The method uses a mesh model: capabilities are connected through explicit contracts, shared context, events, artifacts, and registries.

## Core Mesh Concepts

- **Capability**: a reusable product function with declared inputs, outputs, artifacts, costs, risks, and permissions.
- **Context layer**: the active information needed for a run.
- **Shared context layer**: stable facts, preferences, decisions, and references.
- **Suggestion layer**: cross-capability recommendations filtered by relevance, risk, and cost.
- **Source-of-truth registry**: where the system records authoritative artifacts, decisions, and status.
- **Event stream**: what happened, when, and with what effect.

## Mesh Rule

Everything should be connectable, but nothing should depend directly on everything.

Use:

- typed artifacts;
- event names;
- explicit capability contracts;
- small context packets;
- durable references;
- permission checks.

Avoid:

- implicit global state;
- copy-pasted context blobs;
- workers that read every file by default;
- direct imports between unrelated domains;
- suggestions that trigger actions without review.

## Context Loading

The system should know where to look, not carry everything in active context.

A good context packet includes:

- mission;
- relevant product layer;
- source-of-truth links;
- recent decisions;
- constraints;
- affected files or domains;
- safety zone;
- budget policy;
- expected output.

## Suggestion Discipline

A suggestion is useful only if it is:

- relevant;
- understandable;
- safe to propose;
- cost-aware;
- not redundant;
- based on known or clearly marked uncertain data.

Suggestions should not become hidden automation.
