# Capability Graph

The capability graph describes how product capabilities relate without turning the system into a tangled set of direct dependencies.

## What A Capability Declares

Each capability should declare:

- name;
- purpose;
- users;
- inputs;
- outputs;
- artifacts;
- events emitted;
- events consumed;
- cost profile;
- risk profile;
- safety zone;
- reusable context;
- related domains;
- possible suggestions;
- allowed triggers;
- forbidden triggers;
- Experience Plane exposure;
- Control Plane exposure;
- quality gates.

## Example

```text
Capability: Create project brief

Purpose:
Turn ordinary-language intent into a structured product brief.

Inputs:
- raw user statement
- optional existing product context
- desired ambition level if known

Outputs:
- product brief
- assumptions
- decisive questions
- recommended challenge level

Artifacts:
- product-brief.md
- profiling-notes.md

Events:
- product.intent.received
- product.profile.created

Cost profile:
- low to medium token cost
- cacheable if source intent is unchanged

Risks:
- over-inference
- missing a high-ambition interpretation

Must not trigger:
- implementation
- external publication
- irreversible changes

Experience Plane:
- shows reformulated intent and questions

Control Plane:
- shows assumptions, confidence, source references, and profiling trace
```

## Graph Use

Use the graph to answer:

- What can this capability reuse?
- What can it trigger?
- What should it never trigger?
- Which UI plane should expose it?
- What event tells the rest of the system that something changed?
- What gates must pass before the next step?

## Anti-Pattern

A capability is not complete if it only names a feature. It must describe behavior, boundaries, evidence, cost, and relation to the rest of the product.
