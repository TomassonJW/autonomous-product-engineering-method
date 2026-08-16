# Hermes Adapter

Hermes is treated as a durable autonomous engineering environment that takes over a versioned repository, not as a chatbot that reconstructs the product from every historical note.

## Preferred Intake

For a long-lived or complex project, Hermes should start from an engineering repository that has passed the Ready to Develop gate.

The repository should already contain:

- `AGENTS.md`;
- an active product constitution;
- acceptance gates;
- a compilation manifest and source map;
- pinned method and local-canon versions;
- a baseline commit;
- the first bounded proof and stop conditions.

Hermes should not need ordinary access to the original product-memory workspace.

## Takeover Sequence

1. Clone or update the repository without destroying local work.
2. Verify the remote, branch, baseline commit, and compilation manifest.
3. Read `AGENTS.md`, the manifest, and the complete product constitution.
4. Produce a coverage map.
5. Raise only material contradictions, missing authority, or unavailable required access.
6. Create or update local roadmap, backlog, state, ADRs, and handoff.
7. Own operational Git, implementation, tests, integration, deployment, and rollback.
8. Preserve product-foundation documents and propose material product changes explicitly.
9. Run the bounded preflight.
10. Execute only the first authorized proof and respect every human stop gate.

## Ordinary Sessions

Resume from:

- Git live state;
- current state file;
- current handoff;
- active backlog or board;
- relevant ADRs and product contracts.

Do not reopen the product-memory workspace unless an explicit product amendment requires it.

## Git Responsibility

Hermes owns by default:

- local clone;
- branches and worktrees;
- implementation commits;
- integration;
- technical tags;
- test and CI fixes;
- rollback;
- state and handoff.

A product architect or conversational agent may compile product baselines and product-amendment pull requests. This does not transfer daily engineering Git ownership away from Hermes.

## UI Projects

When a UI exists:

- read the pinned UI canon and local UI contract before design;
- load the environment's canonical UI procedure;
- implement only the first visible gate authorized by the repository;
- stop when the contract requires human acceptance;
- do not infer that a green build is product approval.

## Strengths

- Long-running missions.
- Persistent Git and project state.
- Wrapper and checkpoint patterns.
- Reporting loops.
- Golden paths for repeated workflows.
- Useful for quota-aware autonomy.
- Capable of maintaining roadmap, state, handoff, and delivery evidence inside the repository.

## Risks

- False success.
- Silent quota pauses.
- Worker self-certification.
- Logs without usable status.
- Reports containing private context.
- External notifications without approval.
- Product drift when implementation convenience silently changes the constitution.
- Re-reading raw memory instead of using the compiled baseline.
- Ambiguous ownership between product-compilation Git and engineering Git.

## Method Adaptation

Hermes work should be defined through:

- development-ready repository;
- mission charter;
- product constitution;
- golden path;
- wrapper;
- checkpoint contract;
- state file;
- handoff;
- quota policy;
- final report authority;
- notification policy.

## Control Plane Needs

Expose:

- repository and baseline;
- current mission;
- last checkpoint;
- queue state;
- failed gates;
- quota state;
- final report status;
- approval needs;
- product-amendment status.

## Useful References

- [Product Memory To Engineering Repository](../docs/21-product-memory-to-engineering-repository.md)
- [Engineering Repository Constitution Template](../templates/engineering-repository-constitution-template.md)
- [Compile Product Memory Prompt](../prompts/starter-prompts/compile-product-memory-to-repository.md)
- [Prepare Hermes Worker Run](../prompts/starter-prompts/prepare-hermes-worker-run.md)
