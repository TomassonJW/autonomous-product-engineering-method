# Convert Idea To Product Layers

## Purpose

Transform a product idea into product, UX, architecture, capability, and execution layers.

## When To Use

Use after profiling when the ambition is clear enough to structure.

## Expected Output

Layer map from raw intent to worker missions.

## Prompt

```text
Convert this product idea into Autonomous Product Engineering Method layers.

Idea:
<paste product idea or brief>

Produce:
1. Raw intent.
2. Product profile.
3. North Star.
4. Product vision.
5. Principles and non-goals.
6. Domain map.
7. Capability map.
8. Dual UI model.
9. User journeys.
10. Control-plane journeys.
11. Architecture implications.
12. Event and artifact model.
13. Roadmap slices.
14. Worker missions.
15. Tests and quality gates.

Constraints:
- Keep each layer concise.
- Mark assumptions.
- Do not create code yet.
- Do not skip UX, cost, or safety.

Safety boundaries:
- No external action.
- Red actions require approval.

Next step:
Recommend which layer should be expanded first and why.
```
