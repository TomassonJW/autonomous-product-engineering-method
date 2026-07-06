# Prepare Codex Build Plan

## Purpose

Prepare a Codex-specific implementation plan for a repository.

## When To Use

Use after product profiling, challenge, and a bounded build slice are clear.

## Expected Output

Repo inspection plan, files to read, implementation steps, tests, and final report contract.

## Prompt

```text
Prepare a Codex build plan using the Autonomous Product Engineering Method.

Task:
<paste task>

Repository context:
<paste public-safe repo context>

Rules:
- Read relevant files first.
- Do not read secrets, .env, auth files, private logs, vaults, or credentials.
- Do not code before understanding the local patterns.
- Keep changes scoped.
- Add or update tests appropriate to risk.
- Run available checks.
- Review the diff.

Produce:
1. What Codex should inspect.
2. Ambiguities or risks.
3. Proposed small implementation steps.
4. Files likely affected.
5. Tests or checks to run.
6. Safety boundaries.
7. Final report format.

Safety boundaries:
- Red actions require explicit approval.
- Do not ask the user to paste secrets.
- Do not force push.

Next step:
If the plan involves architecture changes, propose an ADR first. Otherwise proceed with the bounded implementation after approval.
```
