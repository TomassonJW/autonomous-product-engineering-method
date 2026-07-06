# Autonomous Worker Runtime

An autonomous worker is not just a model with a long prompt. It is a bounded runtime pattern.

## Required Elements

A durable worker needs:

- mission;
- owner;
- queue or task list;
- scope boundaries;
- safety zone;
- budget policy;
- status file or status endpoint;
- logs;
- checkpoints;
- quality gates;
- stop file or stop condition;
- rollback notes;
- timeout;
- notification strategy;
- final report;
- external approval handling.

## Worker Mission

A worker mission must say:

- what success means;
- what is out of scope;
- what files, systems, or tools may be touched;
- what actions are forbidden;
- what evidence is required;
- when to stop and ask;
- how to report partial progress.

## Supervisor Pattern

The worker should not be the sole judge of success.

A wrapper, supervisor, or human reviewer should be able to:

- reject premature completion;
- enforce time and quota limits;
- capture logs;
- detect repeated failure loops;
- pause or stop the run;
- verify gates;
- send final notifications;
- preserve evidence.

## Checkpoint Pattern

Long work should be split into checkpoints:

1. Context loaded.
2. Plan accepted or bounded.
3. First artifact created.
4. Tests or audits run.
5. Risks updated.
6. Final report prepared.

Each checkpoint should record what changed, what remains uncertain, and what action is allowed next.

## False Success

False success occurs when a worker reports completion without evidence.

Examples:

- "Tests pass" without test output.
- "Production-ready" without deployment gates.
- "Published" without verifying the public URL.
- "Safe" without secret scan or red-action approval.

The runtime must treat false success as a failure mode, not a communication style.
