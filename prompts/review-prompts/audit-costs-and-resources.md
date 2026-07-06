# Audit Costs And Resources

## Purpose

Review cost, quota, model routing, runtime, and repeated-loop risks.

## When To Use

Use before autonomous runs, expensive model calls, production workflows, or public demos.

## Expected Output

Cost risks, budget policy, model routing recommendations, cache opportunities, and stop conditions.

## Prompt

```text
Audit this plan, capability, or worker mission for cost and resource risk.

Material:
<paste plan or mission>

Check:
1. Token cost.
2. Model cost.
3. API cost.
4. Runtime.
5. Repeated loop risk.
6. Cache potential.
7. Local deterministic alternatives.
8. Human review cost.
9. Maintenance cost.
10. Value-to-cost ratio.

Constraints:
- Premium does not mean maximal.
- Recommend cheaper reliable paths where appropriate.
- Do not hide uncertainty in cost estimates.

Safety boundaries:
- Costly or repeated external actions require explicit budget policy.
- Red financial actions require explicit human approval.

Next step:
Return a budget policy and any required cost gates.
```
