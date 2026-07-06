# Codex Adapter

Codex is suited to repository-local engineering work: reading files, editing code or docs, running tests, inspecting diffs, and producing final reports.

## Strengths

- Local repository awareness.
- Patch-based edits.
- Test execution.
- Git status and diff review.
- Strong fit for documentation, code, and structured refactors.

## Risks

- Reading too broadly.
- Coding before understanding local patterns.
- Overwriting user changes.
- Treating generated code as verified.
- Running commands with hidden external side effects.

## Method Adaptation

Use this sequence:

1. Inspect task and repo status.
2. Read relevant docs and files.
3. Identify safety zone.
4. Plan non-trivial work.
5. Implement small changes.
6. Add tests or checks.
7. Run verification.
8. Review diff.
9. Report files, decisions, tests, limits, risks, and next action.

## Required Boundaries

- No secrets.
- No force push.
- No destructive actions without explicit approval.
- No architecture changes without ADR or accepted decision.
- No final "done" without evidence.

## Useful Prompt

Use [prepare-codex-build-plan.md](../prompts/starter-prompts/prepare-codex-build-plan.md).
