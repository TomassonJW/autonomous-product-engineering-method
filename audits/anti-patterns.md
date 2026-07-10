# Anti-Patterns

This compact list covers recurring failures across the method. The end-to-end [Vision-to-Product anti-pattern catalog](../docs/20-autonomous-vision-to-product.md#24-anti-pattern-catalog) adds symptom, cause, risk, detection, and correction for profiling, exploration, foundation, parallel build, integration, security, and operation failures.

## Coding From Raw Intent

Starting implementation before profiling, challenge, and scope calibration.

## Toy Instead Of Product

Building a tiny demo when the user expected a serious product or platform.

## Platform Instead Of Workflow

Building a large architecture when the user needed a simple useful action.

## Hybrid UI

Mixing end-user workflows, admin controls, logs, worker status, and technical configuration in one confused interface.

## Fake Premium

Adding visual polish while journeys, status truth, errors, and safety remain weak.

## Invisible Cost

Running expensive models, external APIs, or repeated loops without budget policy.

## Worker Self-Certification

Accepting a worker's "done" message without tests, artifacts, or gate evidence.

## Context Flooding

Loading every file, decision, and log into active context instead of using targeted source-of-truth references.

## Suggestion Spam

Generating many cross-capability suggestions that are redundant, risky, costly, or not understandable.

## Documentation Theater

Creating artifacts that do not guide a decision, build step, review, or handoff.

## Foundation Drift

Allowing local missions to change shared contracts without a versioned Foundation Change Proposal.

## Fixture-As-Reality

Presenting mock or fixture integration as evidence that real components, users, or external systems have been validated.

## Completion Percentage Theater

Increasing a global percentage from files, tasks, cards, or test counts instead of independently reviewed product dimensions.
