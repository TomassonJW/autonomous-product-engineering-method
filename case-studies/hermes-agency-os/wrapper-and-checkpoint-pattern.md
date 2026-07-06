# Wrapper And Checkpoint Pattern

Long-running workers need a runtime boundary.

## Wrapper Responsibilities

The wrapper should:

- start the worker;
- pass a bounded context packet;
- enforce time and quota;
- collect logs;
- write status;
- detect repeated failure;
- stop on critical risk;
- request human approval when needed;
- verify the final report exists.

## Checkpoint Shape

Each checkpoint should record:

- current task;
- artifacts changed;
- tests or checks run;
- failures;
- quota state;
- next allowed action;
- approval needed.

## Final Authority

The worker can propose completion. The wrapper, supervisor, or human reviewer accepts or rejects it based on gates and evidence.
