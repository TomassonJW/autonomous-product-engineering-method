# Testing And Sandboxing

Autonomous work must be testable. A generated artifact is not enough.

## Test Types

Use the tests appropriate to the product slice:

- unit tests;
- integration tests;
- smoke tests;
- HTTP checks;
- UI journey tests;
- accessibility checks;
- static security checks;
- no-external-write tests;
- rollback tests;
- truth-status tests;
- cost-budget checks;
- documentation structure checks;
- link checks.

## Sandbox Rule

External effects should be replaced by sandbox, dry-run, or mock modes until the user approves real action.

Examples:

- draft a message instead of sending it;
- prepare a GitHub release instead of publishing it;
- run against a test database instead of production;
- simulate a payment workflow instead of charging;
- produce a migration plan before applying it.

## Evidence

A final report should include:

- commands run;
- outputs or summarized evidence;
- tests skipped and why;
- known gaps;
- manual checks needed, if any.

Do not write "test manually" without exact steps, expected results, and pass/fail criteria.

## Failure Is Data

A failed test is not a reason to hide status. It is an artifact that should update the plan, risk register, or worker mission.
