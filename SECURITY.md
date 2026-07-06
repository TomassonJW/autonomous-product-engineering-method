# Security Policy

This repository is public by design. Do not submit secrets, tokens, credentials, private logs, personal profiles, production data, or unpublished business material.

## Supported Scope

This repository contains documentation, templates, prompts, runbooks, and examples. It does not provide a production runtime.

Security issues may include:

- prompts that authorize unsafe actions;
- templates that encourage secret collection;
- workflows that publish or delete without approval;
- examples that reveal private details;
- documentation that makes external side effects look safe by default.

## Reporting

If you find a security issue:

1. Do not post secrets or exploit details in a public issue.
2. Open a minimal report through the maintainer's preferred private channel if one exists.
3. If no private channel exists, open a public issue with a high-level description only.

## Safety Rules for Contributions

- Never commit `.env`, `auth.json`, tokens, API keys, SSH keys, vaults, private logs, or personal profiles.
- Replace private paths with generic placeholders.
- Use examples that are synthetic or explicitly sanitized.
- Keep red actions behind explicit human approval.
- Make dry-run and rollback behavior visible.

## Red Action Definition

The method treats these as red actions:

- irreversible deletion;
- public release or publication;
- sending external messages;
- financial actions;
- production changes;
- secret handling;
- service exposure;
- credential rotation;
- anything that can harm users, data, money, reputation, or infrastructure.

Red actions require explicit human approval and observable safeguards.
