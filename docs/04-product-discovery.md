# Product Discovery

Product discovery in this method starts from ordinary language, not from a corporate intake form.

The goal is to understand what the user is really asking for, what they are not saying yet, and what would make the product useful rather than merely generated.

## Discovery Outputs

A useful discovery pass produces:

- a reformulated product intent;
- target users and user maturity levels;
- primary jobs to be done;
- the expected ambition level;
- known constraints;
- non-goals;
- hidden assumptions;
- likely risks;
- missing decisions;
- the first testable product slice.

## Ordinary-Language Inputs

Users may say:

- "I want a tool that builds apps for me."
- "This should feel premium."
- "The UI is bad."
- "I want deep settings but the main action should stay simple."
- "I want it to do the whole thing, not a toy version."

The system should not punish imprecision. It should translate it.

## Discovery Rules

1. Reformulate before structuring.
2. Separate what is explicit from what is inferred.
3. Do not ask questions that do not change the build path.
4. Detect ambition gaps early.
5. Identify the first useful slice without shrinking the long-term vision.
6. Name the risks in plain language.

## Example Translation

User statement:

> "I want software that generates 3D games."

Possible interpretations:

- a prompt-to-prototype generator;
- a level editor;
- a game-engine plugin;
- an asset pipeline;
- an autonomous game-studio workflow;
- a full production operating system for games.

The discovery pass must make that ambiguity visible before a worker starts building a small demo and calls it success.

## Discovery Artifact

Use [product-brief-template.md](../templates/product-brief-template.md) and [product-profiling-template.md](../templates/product-profiling-template.md) to capture the result.

The artifact should be short enough to read quickly, but concrete enough for another agent or developer to continue without oral context.
