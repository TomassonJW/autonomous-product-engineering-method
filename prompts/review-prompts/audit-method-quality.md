# Audit Method Quality

## Purpose

Review whether a method, document, or product plan is useful, concrete, and honest.

## When To Use

Use before publishing method documentation or relying on it for worker execution.

## Expected Output

Findings, severity, affected docs, and concrete fixes.

## Prompt

```text
Audit this method or documentation for quality.

Material:
<paste or reference material>

Check:
1. Is it concrete enough to use?
2. Does it overpromise?
3. Does it distinguish assumptions from facts?
4. Does it define outputs clearly?
5. Does it include examples where needed?
6. Does it avoid vague startup language?
7. Does it preserve safety, cost, and testing gates?
8. Can another agent resume from it?

Output findings first, ordered by severity. Include file or section references when available.

Constraints:
- Do not summarize before findings.
- Do not praise vaguely.
- Recommend specific fixes.

Safety boundaries:
- Flag any instruction that may expose secrets or authorize red actions.

Next step:
Return a fix list grouped by must-fix and should-fix.
```
