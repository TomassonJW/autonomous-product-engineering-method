# Dual UI Model

Every serious product must distinguish two interface planes.

The dual UI model prevents a common failure: exposing end users to internal machinery while hiding operational truth from the people responsible for the system.

## Experience Plane UI

The Experience Plane is for end users who want to use the product's capabilities.

It should be:

- simple;
- action-based;
- written in ordinary language;
- focused on outcomes;
- clear about what the system understood;
- capable of progressive disclosure;
- free from internal logs, worker details, queue mechanics, and admin jargon.

Example primary action:

> "Describe the product you want to build."

Advanced controls may exist, but they should not dominate the default path.

## Control Plane UI

The Control Plane is for developers, operators, admins, QA, product owners, and advanced users.

It should expose:

- runs;
- workers;
- queues;
- logs;
- traces;
- quality gates;
- costs;
- failures;
- decisions;
- permissions;
- configuration;
- rollback state;
- source-of-truth references.

The Control Plane may be technical, but it must still be clear and truthful.

## Forbidden Hybrid

Do not mix:

- end-user actions;
- raw logs;
- admin configuration;
- worker internals;
- technical labels;
- cost debugging;
- final user outcomes;
- unfiltered pipeline status;

inside one confused screen.

If a UI forces a non-technical user to understand internal operations to complete their primary task, the Dual UI Gate fails.

## Design Rule

Simple first screen. Deep control behind a deliberate path.

The beginner should not be punished by complexity. The expert should not be trapped by simplicity.
