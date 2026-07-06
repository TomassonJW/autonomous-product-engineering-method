# Contributing

Contributions are welcome when they improve the method without weakening safety, clarity, or public usability.

## Contribution Standard

A good contribution is:

- practical enough to use;
- clear enough for a new reader;
- honest about limits;
- safe for a public repository;
- compatible with ordinary-language users and advanced operators;
- testable or reviewable.

Avoid hype, vague enterprise language, and claims that agent autonomy is safe by default.

## Before Opening a Pull Request

Check that your change:

- does not include secrets, credentials, private logs, private paths, or personal data;
- does not imply that the method guarantees production readiness;
- keeps red actions behind explicit human approval;
- updates templates or prompts if the method contract changes;
- includes examples when a concept is hard to apply.

## Documentation Style

Write in clear English.

Prefer:

- short sections with strong headings;
- concrete examples;
- explicit gates;
- plain-language risk statements;
- checklists that can be used in a real run.

Avoid:

- generic agile boilerplate;
- decorative diagrams that add no operational value;
- prompts that encourage agents to act without boundaries;
- private tool assumptions in core documents.

## Review Questions

Reviewers should ask:

- Does this reduce ambiguity?
- Does it help users avoid false success?
- Does it preserve the dual UI distinction?
- Does it improve cost, safety, or testing discipline?
- Does it stay reusable across different agentic tools?
