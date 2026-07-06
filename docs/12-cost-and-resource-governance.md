# Cost And Resource Governance

Cost is a product constraint. Autonomous systems fail when they spend expensive model calls, runtime, and human attention without visible value.

Premium does not mean maximal. Premium means using the right depth for the right job.

## Cost Dimensions

Each capability and worker should consider:

- token cost;
- model cost;
- API cost;
- runtime;
- storage;
- network calls;
- cache potential;
- repeated loop risk;
- human review cost;
- maintenance cost;
- opportunity cost;
- value produced.

## Model Routing

Use the cheapest reliable option for the job:

- deterministic scripts for mechanical checks;
- local parsing for structured data;
- smaller models for drafts and classification;
- stronger models for ambiguous product reasoning;
- stronger models for final safety, architecture, or challenge review;
- human approval for red actions.

## Budget Policy

A worker mission should define:

- maximum cycles;
- maximum runtime;
- maximum external calls;
- maximum context size;
- allowed model class;
- cache policy;
- stop conditions;
- escalation conditions.

## Cost Gate

The Cost Gate fails when:

- an expensive action has no value justification;
- repeated retries continue without new evidence;
- context is loaded broadly without need;
- a strong model is used for a deterministic task;
- a worker cannot explain what budget it consumed;
- a run hides cost-relevant operations from the Control Plane.

## Practical Rule

If a user would be surprised by the cost, latency, or repeated execution, the system must surface it before continuing.
