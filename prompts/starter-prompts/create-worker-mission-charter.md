# Create Worker Mission Charter

## Purpose

Turn a work request into a bounded autonomous worker mission.

## When To Use

Use before launching a Codex run, Hermes worker, CLI agent, or long-running automation.

## Expected Output

Mission charter with scope, budget, checkpoints, gates, stop conditions, and final report requirements.

## Prompt

```text
Create a worker mission charter for this request.

Request:
<paste work request>

Context:
<paste relevant product brief, issue, or repo notes>

Produce:
1. Mission objective.
2. Allowed scope.
3. Out of scope.
4. Safety zone.
5. Required approvals.
6. Budget limits.
7. Context packet.
8. Work queue.
9. Checkpoints.
10. Quality gates.
11. Stop conditions.
12. Rollback or recovery notes.
13. Final report structure.

Constraints:
- Do not allow unbounded autonomy.
- Do not let the worker self-certify final success without evidence.
- Do not permit red actions without approval.

Safety boundaries:
- No secrets in the mission.
- No production, public, financial, destructive, or external messaging action without explicit approval.

Next step:
Ask for acceptance if the mission includes orange or red actions. Otherwise provide the run-ready charter.
```
