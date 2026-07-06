# Safe GitHub Workflow

Use this runbook before publishing this method or any project repository to GitHub.

## Preconditions

- Git history is understood.
- Working tree is clean or intentionally staged.
- The repository has a `.gitignore`.
- Obvious secret scan has passed.
- README is public-safe.
- License is present.
- No private source file has been copied accidentally.

## Local Checks

Run:

```text
git status --short --branch
git log --oneline --decorate -n 10
git remote -v
```

Scan for sensitive strings and files before publishing.

## GitHub CLI

If `gh` is installed and authenticated:

```text
gh auth status
gh repo create autonomous-product-engineering-method --public --description "An open method for turning ordinary-language product visions into safe, premium, autonomous AI-assisted software engineering workflows." --source . --remote origin --push
```

Do not paste tokens into chat. If authentication is missing, run `gh auth login` locally.

## Red Actions

Creating a public repository and pushing to it is a red action. It is allowed only when the repository has been scanned and the user explicitly requested public publication.

## After Push

Verify:

- repository URL;
- README rendering;
- files present;
- no private data;
- default branch.
