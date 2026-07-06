# Model Dual UI

## Purpose

Create a clear Experience Plane and Control Plane model for a product.

## When To Use

Use before designing screens or reviewing confusing interfaces.

## Expected Output

Dual UI split, user flows, operator flows, hidden complexity, exposed truth, and gate tests.

## Prompt

```text
Model the dual UI for this product or feature.

Context:
<paste product brief, capability, or feature description>

Produce:
1. Experience Plane user types.
2. Experience Plane primary action.
3. Beginner journey.
4. Advanced journey.
5. What complexity is hidden by default.
6. Control Plane user types.
7. Operational truth exposed in Control Plane.
8. Logs, costs, gates, failures, decisions, and rollback states needed.
9. Forbidden hybrid UI risks.
10. Dual UI Gate test.

Constraints:
- Do not mix admin/dev concepts with end-user workflows.
- Do not hide truth from operators.
- Use ordinary language for end-user copy.
- Keep advanced settings behind progressive disclosure.

Safety boundaries:
- Red actions need explicit approval UI.
- Simulated or inferred data must be labeled.

Next step:
Define the first end-to-end UI journey to test.
```
