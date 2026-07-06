# Setup Generic CLI Agent

Use this runbook for terminal-first agents that can inspect files, edit repositories, and run commands.

## Startup Checklist

- Confirm working directory.
- Check Git status.
- Identify safe files to read.
- Exclude secret and private files.
- Read docs before code for non-trivial work.
- Classify safety zone.
- Define verification commands.

## Execution Pattern

```text
inspect -> plan -> edit -> test -> diff -> report
```

## Command Safety

The agent should avoid:

- destructive commands;
- broad recursive deletes;
- force pushes;
- commands that print environment variables;
- commands that upload, publish, or send messages;
- package installs without approval when they add risk or network cost.

## Output Contract

The final report must include:

- changed files;
- decisions;
- commands;
- evidence;
- skipped checks;
- limits;
- risks;
- next action.

## Stop Conditions

Stop when:

- the task needs a secret;
- repo state does not match assumptions;
- a red action is required;
- tests cannot run and no alternative evidence exists;
- scope expands beyond the mission.
