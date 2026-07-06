# Telegram Reporting Pattern

Telegram or chat notifications can be useful for long-running workers, but they are external messages and must be treated carefully.

## When To Use

Use notifications for:

- worker completion;
- blocked status;
- failed gates;
- quota pauses;
- human approval requests;
- urgent safety stops.

## What To Send

Send short, sanitized summaries:

- mission name;
- status;
- key artifact link or local reference;
- approval needed;
- next action.

## What Not To Send

Do not send:

- secrets;
- private logs;
- raw stack traces with sensitive paths;
- unpublished client data;
- personal information;
- full prompts containing private context.

## Approval

Sending messages is an external side effect. For new reporting channels, require explicit approval before enabling them.

## Message Template

```text
Mission: <name>
Status: <completed | blocked | failed | approval needed>
Evidence: <safe artifact reference>
Risk: <none | low | medium | high>
Next: <action>
```
