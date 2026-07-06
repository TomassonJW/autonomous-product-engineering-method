# Hermes Adapter

Hermes is treated as a durable autonomous worker environment.

## Strengths

- Long-running missions.
- Wrapper and checkpoint patterns.
- Reporting loops.
- Golden paths for repeated workflows.
- Useful for quota-aware autonomy.

## Risks

- False success.
- Silent quota pauses.
- Worker self-certification.
- Logs without usable status.
- Reports containing private context.
- External notifications without approval.

## Method Adaptation

Hermes work should be defined through:

- mission charter;
- golden path;
- wrapper;
- checkpoint contract;
- status file;
- quota policy;
- final report authority;
- notification policy.

## Control Plane Needs

Expose:

- current mission;
- last checkpoint;
- queue state;
- failed gates;
- quota state;
- final report status;
- approval needs.

## Useful Prompt

Use [prepare-hermes-worker-run.md](../prompts/starter-prompts/prepare-hermes-worker-run.md).
