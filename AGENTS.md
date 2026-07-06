# Codex Instructions

Work in English for canonical repository content unless the task explicitly targets a translation. For French translation work, write clear, precise, natural French.

## Translation Maintenance

Before modifying documentation, check whether a French translation exists under `translations/fr/`.

After modifying English docs, prompts, templates, runbooks, examples, adapters, audits, or case studies:

1. Update the matching French file when possible.
2. If the French update cannot be done in the same change, mark the row in `translations/fr/TRANSLATION_STATUS.md` as `fr-sync-needed`.
3. Explain the reason in the status notes.

## Glossary Discipline

Preserve `translations/fr/GLOSSARY.md`.

Do not invent new French terms if glossary terms already exist. If a new recurring term appears, update the glossary deliberately.

Keep English file paths, code references, command names, event names, environment variables, and exact tool names stable.

## Safety Translation Rules

Do not translate sensitive or security concepts loosely.

Keep these concepts explicit and operational:

- red action;
- human approval;
- secret handling;
- production change;
- external side effect;
- destructive command;
- rollback;
- safety gate;
- truth gate;
- cost gate.

Never weaken warnings during localization.

## Status Tracking

Update `translations/fr/TRANSLATION_STATUS.md` whenever a translated file is added, changed, left partial, or marked `fr-sync-needed`.
