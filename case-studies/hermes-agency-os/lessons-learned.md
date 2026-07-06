# Lessons Learned

## UI Scaffolds Are Not Products

A screen, route, or mock flow can create the feeling of progress without delivering a real journey. The Journey Gate must require end-to-end evidence.

## Truth-Safe Status Matters

Status should distinguish:

- generated;
- tested;
- failed;
- blocked;
- simulated;
- approved;
- published.

Compressing these states into "done" creates false confidence.

## Workers Need Wrappers

A worker can execute a cycle, but a wrapper or supervisor should enforce:

- quota;
- stop conditions;
- checkpoints;
- report format;
- final authority.

## Reporting Is A Product Feature

For long runs, reporting is not an add-on. It is how the user knows whether autonomy is useful, stuck, costly, or risky.

## Quota Changes Autonomy

An agent that can work for ten minutes and an agent that can work for hours need different governance. Quota-aware execution prevents silent degradation.
