# Quota-Aware Execution

Autonomous runs must account for quota, rate limits, budgets, and repeated-loop risk.

## Quota Policy

Define before execution:

- maximum cycles;
- maximum runtime;
- maximum model calls;
- maximum external API calls;
- retry limits;
- pause rules;
- escalation triggers.

## Repeated Loop Detection

Stop or pause when:

- the same error repeats;
- no new evidence is produced;
- retries consume budget without progress;
- context grows without better decisions;
- the worker keeps changing strategy without verification.

## Cost-Aware Routing

Prefer:

- deterministic local checks for mechanical validation;
- cached artifacts when inputs are unchanged;
- smaller models for classification and draft work;
- stronger review only for high-risk reasoning.

## Report Cost

A run report should include:

- approximate model/API calls;
- skipped expensive checks;
- cache use;
- quota pauses;
- budget overruns or warnings.

## Premium Rule

Premium means right depth, not maximum spend.
