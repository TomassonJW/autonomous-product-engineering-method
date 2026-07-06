# Run Autonomous Worker

This runbook defines a generic autonomous worker lifecycle.

## 1. Create Mission Charter

Use [worker-mission-charter-template.md](../templates/worker-mission-charter-template.md).

The charter must define objective, scope, safety zone, budget, checkpoints, gates, stop conditions, and final report requirements.

## 2. Prepare Context Packet

Include only:

- mission;
- relevant artifacts;
- accepted decisions;
- constraints;
- allowed tools;
- affected files or systems;
- safety and cost policies.

Do not include secrets or unnecessary history.

## 3. Execute In Cycles

Each cycle should:

1. Select next task.
2. Act within scope.
3. Write artifact or checkpoint.
4. Run relevant checks.
5. Update status.
6. Decide continue, pause, or stop.

## 4. Enforce Gates

Before completion, check:

- Truth Gate;
- Safety Gate;
- Cost Gate;
- Journey Gate;
- Product Honesty Gate.

## 5. Final Report

The final report must distinguish:

- completed with evidence;
- completed with known gaps;
- partially completed;
- blocked;
- failed.

Do not accept "done" as a status without supporting evidence.
