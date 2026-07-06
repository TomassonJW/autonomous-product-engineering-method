# Challenge Gate

The challenge gate prevents shallow execution, false scope, hidden cost, and unsafe autonomy.

It is not a permission ritual. It is a structured pause before consequential work.

## When To Use It

Use the challenge gate when a request involves:

- a new product or major capability;
- a vague but ambitious intent;
- architecture changes;
- external side effects;
- public release;
- expensive models or repeated runs;
- user data or secrets;
- production infrastructure;
- a claim of "premium", "autonomous", or "done".

## What To Challenge

The gate must cover:

- ambition mismatch;
- scope ambiguity;
- UX risk;
- technical risk;
- cost risk;
- autonomy risk;
- safety risk;
- maintenance risk;
- scaling risk;
- user misunderstanding;
- alternatives;
- limits of each solution.

## Challenge Levels

Use a level appropriate to the risk:

- **Light**: small local correction with low risk.
- **Medium**: new workflow, screen, or behavior.
- **Structured**: new capability, public-facing feature, or shared abstraction.
- **Strict**: external side effects, destructive actions, production, secrets, money, or publication.

## Challenge Report Shape

A good challenge report includes:

1. What I think you want.
2. Where this may be underspecified.
3. What can go wrong.
4. Options and tradeoffs.
5. Recommended scope.
6. What I will not do without approval.
7. Acceptance gates.

## Plain-Language Rule

The challenge should be understandable to the person who expressed the idea. Use technical terms only when they are necessary, and explain their consequence.

## Failure Modes

The challenge gate fails if it:

- blocks minor work with heavy process;
- hides behind vague risk language;
- avoids making a recommendation;
- asks too many low-value questions;
- ignores cost;
- ignores user experience;
- lets red actions proceed without approval.
