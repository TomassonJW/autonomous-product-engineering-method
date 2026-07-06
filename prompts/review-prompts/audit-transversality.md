# Audit Transversality

## Purpose

Review whether capabilities form a coherent mesh without unsafe coupling.

## When To Use

Use after capability mapping or before architecture implementation.

## Expected Output

Findings on silos, coupling, events, artifacts, triggers, suggestions, and shared context.

## Prompt

```text
Audit this product map or architecture for transversality.

Material:
<paste domain map, capability map, or architecture notes>

Check:
1. Does each capability declare inputs and outputs?
2. Are artifacts explicit?
3. Are events explicit?
4. Are costs and risks attached?
5. Are suggestions filtered?
6. Are triggers allowed and forbidden?
7. Is shared context loaded on demand?
8. Is there direct coupling between unrelated domains?
9. Can the Control Plane observe the mesh?

Constraints:
- Everything should be connectable.
- Nothing should depend directly on everything.
- Avoid abstraction without operational use.

Safety boundaries:
- Suggestions must not trigger red actions automatically.

Next step:
Return a corrected capability-mesh recommendation.
```
