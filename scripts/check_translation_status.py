"""Check that French translation status covers meaningful Markdown sources."""

from __future__ import annotations

import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
STATUS_FILE = ROOT / "translations" / "fr" / "TRANSLATION_STATUS.md"
VALID_STATUSES = {"translated", "partial", "missing", "fr-sync-needed"}
SOURCE_DIRS = [
    "docs",
    "templates",
    "prompts",
    "runbooks",
    "adapters",
    "examples",
    "case-studies",
    "audits",
]


def parse_rows() -> dict[str, tuple[str, str]]:
    rows: dict[str, tuple[str, str]] = {}
    for line in STATUS_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0] in {"English source file", "---"}:
            continue
        rows[cells[0]] = (cells[1], cells[2])
    return rows


def expected_sources() -> set[str]:
    sources = {"README.md"}
    for directory in SOURCE_DIRS:
        for path in (ROOT / directory).rglob("*.md"):
            sources.add(path.relative_to(ROOT).as_posix())
    return sources


def main() -> int:
    rows = parse_rows()
    expected = expected_sources()
    failures: list[str] = []

    for source in sorted(expected):
        if source not in rows:
            failures.append(f"Missing translation status row for {source}")
            continue
        translated, status = rows[source]
        if status not in VALID_STATUSES:
            failures.append(f"Invalid status for {source}: {status}")
        if not (ROOT / source).exists():
            failures.append(f"Source path does not exist: {source}")
        if status in {"translated", "partial", "fr-sync-needed"} and not (ROOT / translated).exists():
            failures.append(f"French path for {source} does not exist: {translated}")

    extra = sorted(set(rows) - expected)
    for source in extra:
        failures.append(f"Unexpected translation status row: {source}")

    if failures:
        print("Translation status check failed:")
        for failure in failures:
            print(failure)
        return 1

    print(f"Translation status check passed for {len(expected)} source files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
