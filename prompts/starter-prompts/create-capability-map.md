# Create Capability Map

## Purpose

Map product capabilities as connected, bounded, reusable units.

## When To Use

Use after product profiling and before architecture or worker planning.

## Expected Output

Capability list with inputs, outputs, artifacts, events, cost, risk, UI exposure, and triggers.

## Prompt

```text
Create a capability map for this product.

Context:
<paste product brief, vision, or domain map>

For each capability, define:
1. Name.
2. Purpose.
3. Users.
4. Inputs.
5. Outputs.
6. Artifacts.
7. Events emitted.
8. Events consumed.
9. Cost profile.
10. Risk profile.
11. What it can trigger.
12. What it must not trigger.
13. Experience Plane exposure.
14. Control Plane exposure.
15. Quality gates.

Constraints:
- Everything should be connectable.
- Nothing should depend directly on everything.
- Do not create isolated feature silos.
- Do not invent external systems without justification.

Safety boundaries:
- Mark red triggers as approval-required.
- Do not let suggestions become hidden automation.

Next step:
Identify the first capability to specify in detail.
```
