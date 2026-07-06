# Event And Artifact Model

Events and artifacts let the system stay coherent without direct coupling between every module.

## Artifact

An artifact is a durable output that can be reviewed, reused, versioned, or referenced.

Examples:

- product brief;
- challenge report;
- UX model;
- capability spec;
- worker mission charter;
- test report;
- run summary;
- decision record;
- generated code patch;
- cost report.

Artifacts should include:

- title;
- purpose;
- source;
- version or date;
- author or worker;
- status;
- confidence;
- dependencies;
- known limits.

## Event

An event records something that happened.

Examples:

- `product.intent.received`
- `product.profile.created`
- `challenge.gate.failed`
- `capability.spec.accepted`
- `worker.mission.started`
- `worker.checkpoint.created`
- `quality_gate.failed`
- `feedback.submitted`
- `public_release.requested`

Events should include:

- name;
- timestamp;
- actor;
- related artifact;
- affected domain;
- safety zone;
- result;
- next allowed actions.

## Status Truth

Status must not compress incompatible states.

Bad:

> Done

Better:

> Draft generated. Tests not run. External publication not approved.

## Event Discipline

Events should inform downstream capabilities, not secretly execute them. A suggestion layer may propose next actions based on events, but red actions still require explicit approval.
