# Translation Policy

English is the canonical source for this repository.

French is maintained as an official translation, not as a separate fork of the method. The French version should be clear, precise, practical, and faithful to the English source while reading naturally for French-speaking users.

## Canonical Source

The English files remain authoritative for:

- method definitions;
- safety boundaries;
- prompt behavior;
- template structure;
- runbook steps;
- adapter contracts;
- examples;
- audits;
- case studies.

If English and French disagree, update the French translation or open a synchronization task. Do not silently treat the French text as a new source of truth.

## Update Rule

Every meaningful change to English docs, prompts, templates, runbooks, examples, adapters, audits, or case studies should update the matching French file in the same change.

If the French equivalent cannot be updated immediately, mark it in [translations/fr/TRANSLATION_STATUS.md](translations/fr/TRANSLATION_STATUS.md) with status `fr-sync-needed` and explain what changed.

## What Not To Translate

Do not translate:

- code identifiers;
- file names;
- command names;
- environment variable names;
- Git commands;
- exact tool names;
- event names such as `worker.mission.completed`;
- quoted CLI output;
- license boilerplate.

Add a French explanation around these terms when needed, but keep the exact reference stable.

## Translation Standard

Translate meaning over literal wording.

French translation should be:

- natural;
- precise;
- direct;
- readable in Markdown;
- faithful to technical constraints;
- usable by non-technical readers when the English source is non-technical;
- exact when the source is operational or safety-sensitive.

Avoid:

- machine-like literal translation;
- corporate filler;
- softened safety warnings;
- vague risk language;
- over-translated technical terms;
- new terminology when the glossary already provides a term.

## Prompt Translation

Prompts must remain copy-pasteable.

Keep:

- purpose;
- when to use;
- expected output;
- constraints;
- safety boundaries;
- next step.

Do not weaken agent instructions during translation.

## Premium Concept

The French version must preserve the repository's meaning of "premium":

- clarity;
- reliability;
- configurability;
- no hidden cost;
- no bad surprise;
- powerful but safe automation;
- visible limits;
- honest uncertainty.

"Premium" does not mean decorative, luxury, vague polish, or maximum spend.
