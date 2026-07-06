# Prepare Hermes Worker Run

## Purpose

Prepare a Hermes-style durable worker run with wrapper, checkpoints, quota awareness, and truthful reporting.

## When To Use

Use before launching or supervising a Hermes autonomous workflow.

## Expected Output

Worker mission, wrapper requirements, status files, checkpoints, quota policy, and report contract.

## Prompt

```text
Prepare a Hermes worker run using the Autonomous Product Engineering Method.

Mission:
<paste mission>

Context:
<paste sanitized project context>

Produce:
1. Worker objective.
2. Golden path.
3. Wrapper responsibilities.
4. Queue policy.
5. Checkpoints.
6. Status file contract.
7. Logs and report contract.
8. Quota and pause policy.
9. Stop conditions.
10. False-success detection.
11. Telegram or notification strategy if available.
12. Human approval points.

Constraints:
- Do not let the worker be final authority on completion.
- Do not hide failed cycles.
- Do not run costly loops without budget policy.

Safety boundaries:
- No credentials in prompts or reports.
- Red actions require explicit approval.
- Public reporting must be sanitized.

Next step:
Return a run-ready mission charter and list any required human decisions.
```
