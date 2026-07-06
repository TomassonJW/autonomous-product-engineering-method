# Example Dual UI Model

## Product

AI-assisted app builder.

## Experience Plane

Primary user:

- founder, product owner, or creator who wants to describe an app.

Primary action:

> Describe the product you want to build.

Default view:

- intent box;
- reformulated understanding;
- three decisive questions;
- start profiling button;
- advanced settings collapsed.

Hidden by default:

- worker logs;
- token counts;
- queue state;
- raw traces;
- model routing;
- Git internals.

## Control Plane

Primary user:

- developer, operator, QA, or advanced builder.

Shows:

- active runs;
- artifacts;
- gate results;
- failed checks;
- cost estimates;
- model routing;
- approval requests;
- rollback notes.

## Gate Test

A non-technical user can create a product brief without understanding workers. An operator can audit the run without asking the end user for hidden details.
