# Product-To-Engineering Layers

The method converts user intent into software through layers. This prevents the agent from jumping from vague desire directly to code.

## Layer Chain

```text
Raw intent
  -> Product profile
  -> North Star
  -> Product vision
  -> Principles and non-goals
  -> Domain map
  -> Capability map
  -> Dual UI model
  -> User journeys
  -> Control-plane journeys
  -> UX/UI direction
  -> System architecture
  -> Data model
  -> Capability graph
  -> Event model
  -> Artifact model
  -> Roadmap
  -> Epics
  -> Tasks
  -> Worker missions
  -> Code
  -> Tests
  -> Run reports
  -> Human feedback
  -> Targeted layer updates
```

## Why Layers Matter

Without layers, agents tend to:

- code too early;
- overfit the first phrase;
- miss UX implications;
- build isolated modules;
- forget costs and safety;
- report completion without product evidence.

Layers make the reasoning reviewable.

## Feedback Routing

Feedback should update the right layer.

Examples:

- "This is confusing" may affect UX copy, navigation, or the dual UI split.
- "I want this to be a full agency OS" may affect North Star, domains, and roadmap.
- "Do not touch architecture" constrains the implementation layer.
- "Make it cheaper" affects model routing, cache policy, and worker budgets.

## Layer Discipline

Do not rewrite high-level vision for every small comment.

Do not implement code for every broad ambition.

Map the feedback, identify the affected layers, and produce the smallest coherent update.
