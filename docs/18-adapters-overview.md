# Adapters Overview

The core method is tool-agnostic. Adapters translate the method into the constraints of a specific environment.

## What An Adapter Defines

An adapter should define:

- how the agent receives missions;
- how context is loaded;
- where status is written;
- how files are edited;
- how tests are run;
- how approvals are requested;
- how secrets are avoided;
- how costs are estimated;
- how final reports are produced;
- what the tool must never do automatically.

## Available Adapters

- [Codex](../adapters/codex.md): local repository work, patches, tests, Git hygiene, review reports.
- [Hermes](../adapters/hermes.md): durable worker patterns, wrappers, checkpoints, reporting.
- [Generic CLI Agent](../adapters/generic-cli-agent.md): terminal-first autonomous work.
- [Generic Chatbot](../adapters/generic-chatbot.md): no filesystem by default, prompt-driven planning and review.

## Adapter Boundary

An adapter may change execution mechanics, but it must not weaken the core method:

- no fake completion;
- no red actions without approval;
- no secret exposure;
- no direct code before profiling and challenge for complex work;
- no hybrid UI;
- no uncontrolled cost loops.

## Creating A New Adapter

Start from:

1. tool capabilities;
2. tool limitations;
3. safety model;
4. context loading model;
5. execution evidence;
6. reporting contract.

Then write the smallest runbook that lets a user operate the method safely in that tool.
