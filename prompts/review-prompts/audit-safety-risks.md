# Audit Safety Risks

## Purpose

Find unsafe autonomy, publication, secrets, production, deletion, and external side-effect risks.

## When To Use

Use before running workers, publishing repos, or enabling integrations.

## Expected Output

Risk findings with severity, action class, required approvals, and mitigations.

## Prompt

```text
Audit this plan, prompt, repository, or worker mission for safety risks.

Material:
<paste or reference material>

Classify actions as:
- Green: local, reversible, testable, low risk.
- Orange: structural, costly, ambiguous, or impactful.
- Red: irreversible, destructive, public, financial, secret-related, production-changing, or externally messaging.

Check for:
1. Secret exposure.
2. Public publication risk.
3. External side effects.
4. Destructive commands.
5. Production changes.
6. Credential handling.
7. Missing approvals.
8. Missing rollback.
9. False-success claims.
10. Unsafe prompt permissions.

Constraints:
- Findings first.
- Be specific.
- Do not suggest bypassing approval.

Safety boundaries:
- Never ask for secrets.
- Red actions must be approval-gated.

Next step:
Return required mitigations before execution.
```
