"""Conservative public-safety scan for obvious secrets and private paths."""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTENT_PATTERNS = [
    re.compile(r"C:\\Users\\", re.IGNORECASE),
    re.compile(r"\bOneDrive\b", re.IGNORECASE),
    re.compile(r"BEGIN (RSA|OPENSSH|PRIVATE) KEY"),
    re.compile(r"\bghp_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
]
SENSITIVE_FILE_RE = re.compile(
    r"(^|/)(\.env|auth\.json|id_rsa|id_ed25519|.*\.pem|.*\.key)$",
    re.IGNORECASE,
)


def tracked_files() -> list[pathlib.Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [ROOT / line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    failures: list[str] = []

    for path in tracked_files():
        rel = path.relative_to(ROOT).as_posix()
        if SENSITIVE_FILE_RE.search(rel):
            failures.append(f"Sensitive tracked filename: {rel}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in CONTENT_PATTERNS:
            if pattern.search(text):
                failures.append(f"Sensitive-looking content in {rel}: {pattern.pattern}")

    if failures:
        print("Public-safety scan failed:")
        for failure in failures:
            print(failure)
        return 1

    print("Public-safety scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
