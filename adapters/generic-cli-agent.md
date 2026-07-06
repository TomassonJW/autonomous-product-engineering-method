# Generic CLI Agent Adapter

A generic CLI agent can operate locally, but its safety depends on command discipline, context boundaries, and verification.

## Strengths

- File inspection.
- Local edits.
- Script execution.
- Test runs.
- Git workflow.

## Risks

- Destructive shell commands.
- Broad file reads.
- Environment leakage.
- Network calls.
- Hidden writes.
- Weak final evidence.

## Method Adaptation

Require:

- working directory confirmation;
- secret exclusion;
- Git status before edits;
- plan before non-trivial changes;
- scoped file edits;
- tests or checks;
- diff review;
- final report.

## Safe Command Bias

Prefer read-only inspection before mutation. Avoid commands that print environment variables, upload data, delete recursively, or modify external systems.

## Useful Runbook

Use [setup-generic-cli-agent.md](../runbooks/setup-generic-cli-agent.md).
