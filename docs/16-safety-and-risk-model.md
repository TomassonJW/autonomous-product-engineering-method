# Safety And Risk Model

The method uses a three-zone safety model.

The goal is to maximize useful autonomy while preventing irreversible harm, public mistakes, hidden costs, secret exposure, and production damage.

## Green Actions

Green actions are local, reversible, testable, low risk, and have no external side effect.

Examples:

- create or edit local documentation;
- add a local test;
- run a local formatter;
- draft a report;
- generate a local template;
- prepare a dry-run command;
- inspect public-safe files.

Green actions may be autonomous when the mission allows them.

## Orange Actions

Orange actions are structural, costly, ambiguous, or potentially impactful.

Examples:

- change architecture;
- introduce a new dependency;
- change a public API;
- expand worker permissions;
- run expensive evaluations;
- prepare publication;
- change roadmap or product scope.

Orange actions require a proposal before execution.

## Red Actions

Red actions are irreversible, destructive, public, financial, secret-related, production-changing, or externally messaging.

Examples:

- delete data;
- publish externally;
- send email or messages;
- spend money;
- change production;
- expose services;
- read, print, commit, or rotate secrets;
- force push;
- modify credentials;
- execute irreversible migrations.

Red actions require explicit human approval and observable safeguards.

## Secret Handling

Agents must never ask users to paste secrets into chat.

Use safer authentication flows, environment variables, local secret stores, or provider-specific auth mechanisms. Documentation examples must use placeholders only.

## Risk Report

For orange and red work, produce:

- action description;
- risk class;
- possible harm;
- rollback or recovery plan;
- required approval;
- verification evidence;
- stop conditions.
