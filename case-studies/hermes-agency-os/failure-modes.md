# Failure Modes

## False Success

The worker reports completion but the artifact is incomplete, untested, or not connected to a real journey.

Mitigation:

- require evidence;
- verify gates;
- keep final authority outside the worker.

## Quiet Quota Exhaustion

The worker stops because of quota but the status does not make that clear.

Mitigation:

- explicit quota status;
- pause reports;
- resume instructions.

## Log Without Decision

Raw logs exist, but no one can tell what changed or what to do next.

Mitigation:

- structured checkpoint summaries;
- run reports;
- decision and blocker sections.

## Private Context Leakage

Reports include private paths, raw content, or sensitive operational details.

Mitigation:

- sanitize reports;
- use placeholders;
- separate private logs from public artifacts.

## UI Progress Illusion

The UI exists, but no end-to-end workflow works.

Mitigation:

- Journey Gate;
- acceptance tests;
- user-facing examples.
