# Setup Hermes

Use this runbook for a Hermes-style autonomous worker environment.

Hermes is treated here as a durable agentic worker pattern, not as a requirement of the method.

## Required Runtime Pieces

- mission charter;
- queue or work list;
- wrapper or supervisor;
- status file;
- logs;
- checkpoints;
- quota policy;
- stop file or stop signal;
- final report channel;
- human approval path.

## Golden Path

1. Human or supervisor creates a mission charter.
2. Worker loads only relevant context.
3. Worker executes one bounded cycle.
4. Worker writes checkpoint and status.
5. Supervisor checks quota, gates, and stop conditions.
6. Worker continues, pauses, or stops.
7. Final report is verified before completion is accepted.

## False-Success Detection

Treat these as failures:

- final message without artifacts;
- "tests pass" without evidence;
- completed status after skipped gates;
- silent quota exhaustion;
- hidden errors in logs;
- reports that omit blocked items.

## Reporting

Reports should include:

- mission;
- cycles run;
- outputs created;
- checks run;
- failures;
- cost or quota notes;
- approvals needed;
- next action.

## Safety

Hermes workers must not perform red actions without approval. Public reports must be sanitized and must not include credentials, private paths, private logs, or sensitive business content.
