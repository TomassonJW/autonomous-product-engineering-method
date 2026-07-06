# Generic Chatbot Adapter

A chatbot usually lacks direct filesystem access, durable logs, tests, and execution authority. Treat it as a reasoning and artifact-drafting interface unless connected to tools.

## Strengths

- Ordinary-language interaction.
- Product profiling.
- Challenge reports.
- Prompt drafting.
- Documentation drafting.
- Review and critique.

## Risks

- No direct verification.
- User may paste secrets.
- False confidence.
- Hard to preserve durable state.
- Weak execution evidence.

## Method Adaptation

Use chatbots for:

- product discovery;
- deductive profiling;
- challenge gates;
- dual UI modeling;
- capability mapping;
- template completion;
- review prompts.

Do not rely on a chatbot alone for:

- code verification;
- production changes;
- secret handling;
- publication;
- destructive operations.

## Output Contract

Ask for structured artifacts that can be moved into a repository or execution environment.
