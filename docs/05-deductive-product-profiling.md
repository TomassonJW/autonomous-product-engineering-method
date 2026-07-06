# Deductive Product Profiling

Deductive product profiling is the method's first strong filter against shallow execution.

It turns rough intent into an actionable product profile by inferring likely meaning, detecting ambiguity, and asking only high-value questions.

## What The Profiler Must Detect

The profiler must identify:

- product type;
- ambition level;
- target users;
- user maturity range;
- core jobs;
- workflow depth;
- autonomy expectations;
- quality expectations;
- configuration depth;
- safety sensitivity;
- cost sensitivity;
- integration needs;
- non-goals;
- contradictions;
- missing decisions.

## Ambition Scale

Use this scale when a request could be interpreted at different depths:

1. Demo: proves an idea.
2. Prototype: tests a concept.
3. Local tool: solves a narrow problem.
4. Usable product: supports serious use.
5. Premium product: clear, robust, polished, deep.
6. Platform: multiple connected domains.
7. Autonomous system: plans, builds, tests, reports.
8. Autonomous factory: produces systems or content repeatedly.
9. Industry-grade system: strong security, scale, governance.
10. Open-world ambition: large creative or operational ecosystem.

If the user statement spans distant levels, the profiler must stop and clarify.

## Question Quality

Bad question:

> "Who is your target audience?"

Better question:

> "Is this meant for a beginner who wants one simple action, an expert who wants full control, or both through separate modes?"

Bad question:

> "What features do you want?"

Better question:

> "When you say 'do the whole thing', should the system only prepare a plan, generate files locally, open pull requests, or operate a long-running worker with reports and checkpoints?"

## Profiler Output

The profiler should produce:

- a one-paragraph product interpretation;
- explicit assumptions;
- ambiguity map;
- ambition level with reasoning;
- risk preview;
- recommended challenge depth;
- a small set of decisive questions;
- the likely first build slice if the questions are answered.

## Stop Condition

Do not let a build agent proceed if the request has a large ambition gap, unclear user type, unclear external side effects, or unclear safety zone.
