# Quality Gates

Quality gates are review contracts. They prevent agents from calling work complete before evidence exists.

## Truth Gate

Fails if:

- simulated data is presented as real;
- inferred information is not labeled;
- uncertainty is hidden;
- a status badge compresses incompatible truths;
- the system claims completion without proof.

## Challenge Gate

Fails if:

- ambitious or ambiguous work starts without challenge;
- alternatives are not considered;
- cost and safety are ignored;
- the system obeys a risky instruction without boundary.

## Dual UI Gate

Fails if:

- end users must understand logs, workers, or pipelines;
- operators cannot inspect truth, cost, or failures;
- one screen mixes admin controls with final user workflows.

## User Simplicity Gate

Fails if:

- the primary action is not clear;
- default settings overwhelm the user;
- copy uses internal jargon;
- advanced options are visible too early.

## Journey Gate

Fails if:

- the feature is only a data model, route, or screen;
- no end-to-end path exists;
- success cannot be observed by a user or operator.

## Transversality Gate

Fails if:

- the capability is a silo;
- relations are implicit;
- events and artifacts are missing;
- direct coupling replaces contracts.

## Cost Gate

Fails if:

- high-cost actions are unbounded;
- repeated loops have no stop condition;
- model choice is unjustified;
- cost is hidden from operators.

## Safety Gate

Fails if:

- red actions can run without explicit human approval;
- secrets may be read, printed, committed, or exposed;
- external systems are changed without authorization;
- rollback is absent for risky changes.

## Product Honesty Gate

Fails if:

- "premium" is claimed without evidence;
- "done" means only generated;
- "autonomous" hides manual requirements;
- limitations are not documented.
