"""Lightweight local Markdown link checker."""

from __future__ import annotations

import pathlib
import re
import sys
from urllib.parse import unquote


ROOT = pathlib.Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def iter_markdown_files() -> list[pathlib.Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )


def strip_code_fences(text: str) -> list[str]:
    lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            lines.append("")
            continue
        lines.append("" if in_fence else line)
    return lines


def main() -> int:
    failures: list[str] = []

    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(strip_code_fences(text), 1):
            for match in LINK_RE.finditer(line):
                target = match.group(1).strip()
                if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                    continue
                target = target.split("#", 1)[0]
                if not target:
                    continue
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                candidate = (path.parent / unquote(target)).resolve()
                try:
                    candidate.relative_to(ROOT)
                except ValueError:
                    failures.append(f"{path.relative_to(ROOT)}:{line_no}: outside repo: {target}")
                    continue
                if not candidate.exists():
                    failures.append(f"{path.relative_to(ROOT)}:{line_no}: missing: {target}")

    if failures:
        print("Markdown link check failed:")
        for failure in failures:
            print(failure)
        return 1

    print("Markdown link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
