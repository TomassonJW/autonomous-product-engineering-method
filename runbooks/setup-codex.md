# Setup Codex

Use this runbook when applying the method in a Codex-style local repository workflow.

## Preconditions

- The repository is local and under version control.
- The task is bounded.
- The agent has permission to read public-safe project files.
- Secrets are excluded from context.
- Git status is checked before edits.

## Safe Startup

1. Read the task.
2. Inspect repository status.
3. Read relevant docs and source files.
4. Identify sensitive files that must not be opened.
5. Classify the task as green, orange, or red.
6. Produce a short plan for non-trivial work.

## Codex Operating Rules

- Use existing project patterns.
- Make small scoped edits.
- Add or update tests based on risk.
- Run available checks.
- Review the diff before final report.
- Never revert user changes unless explicitly asked.
- Never force push.
- Never ask the user to paste secrets.

## Evidence To Capture

- files changed;
- commands run;
- test results;
- skipped checks and reasons;
- known risks;
- next recommended action.

## Stop Conditions

Stop and ask before:

- architecture changes without ADR;
- destructive commands;
- public release;
- production changes;
- credential handling;
- expensive external calls;
- uncertain file ownership.
