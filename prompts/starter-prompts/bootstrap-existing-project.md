# Bootstrap An Existing Project

## Purpose

Apply the method to a project that already has code, docs, or partial architecture.

## When To Use

Use before restructuring or extending an existing repository.

## Expected Output

Current-state map, gaps, risks, method alignment, and bounded next steps.

## Prompt

```text
I want to apply the Autonomous Product Engineering Method to an existing project.

First, inspect the available public-safe project files. Do not read secrets, credentials, private logs, local profiles, .env files, auth files, or vaults.

Produce:
1. Current product interpretation.
2. Existing documentation map.
3. Existing capability map if inferable.
4. Dual UI status.
5. Safety and cost risks.
6. Missing artifacts.
7. Quality gate gaps.
8. Recommended first bounded improvement.

Constraints:
- Do not rewrite the project yet.
- Do not change architecture without proposing an ADR.
- Do not assume generated scaffolds equal real product journeys.

Safety boundaries:
- Never print secrets.
- Treat publication, deletion, production changes, and external messaging as red actions.

Next step:
Recommend the smallest documentation or planning artifact needed before implementation.
```
