# Example Capability Graph

## Product

AI-assisted product builder.

## Capability: Create Product Brief

Inputs:

- raw user statement;
- optional existing context.

Outputs:

- product brief;
- assumptions;
- decisive questions.

Artifacts:

- `product-brief.md`

Events:

- `product.intent.received`
- `product.brief.created`

Cost:

- low to medium token cost;
- cacheable when input is unchanged.

Risks:

- over-inference;
- underestimating ambition.

Can trigger:

- challenge report suggestion;
- product layer mapping suggestion.

Must not trigger:

- code generation;
- GitHub publication;
- external worker execution.

Experience Plane:

- shows reformulated intent and questions.

Control Plane:

- shows assumptions, confidence, source references, and prompt version.
