# Prompt Library

These prompts are designed to be copied into Codex, Hermes, CLI agents, chatbots, or custom agentic systems.

They are not magic commands. They are operating contracts. Adapt tool names, repository paths, and approval rules to your environment.

## Prompt Rules

Every prompt in this library should:

- define its purpose;
- say when to use it;
- state expected output;
- include constraints;
- include safety boundaries;
- define the next step.

## Prompt Groups

- [System prompts](system-prompts/autonomous-product-architect.md): long-lived role and behavior contracts.
- [Starter prompts](starter-prompts/start-new-product-method.md): prompts for starting a product or preparing a run.
- [Review prompts](review-prompts/audit-method-quality.md): prompts for critique, safety, cost, UX, and transversality review.

For the complete end-to-end protocol, use [Vision-to-Product Orchestrator](system-prompts/vision-to-product-orchestrator.md). It coordinates profiling, inference, exploration, Foundation Freeze, build missions, integration, acceptance, and post-delivery learning.

## Safety Reminder

Never paste secrets into a prompt. Use placeholders and safe authentication flows. Any action that publishes, deletes, spends money, sends messages, changes production, or handles secrets is a red action and requires explicit approval.
