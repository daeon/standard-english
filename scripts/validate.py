#!/usr/bin/env python3
"""Validate the standalone Standard English skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

REQUIRED_FILES = [
    SKILL,
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "references" / "selection-matrix.md",
    ROOT / "references" / "standards-catalog.md",
    ROOT / "references" / "output-contract.md",
]

REQUIRED_HEADINGS = [
    "# Standard English",
    "## Default posture",
    "## Workflow",
    "## Required output",
]

REFERENCE_HEADINGS = {
    "references/selection-matrix.md": "# Selection Matrix",
    "references/standards-catalog.md": "# Standards Catalog",
    "references/output-contract.md": "# Output Contract",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_required_files() -> None:
    for path in REQUIRED_FILES:
        require(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")
        require(path.stat().st_size > 0, f"empty required file: {path.relative_to(ROOT)}")


def validate_frontmatter(text: str) -> None:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    require(match is not None, "SKILL.md missing YAML frontmatter")
    frontmatter = match.group(1)
    require(re.search(r"(?m)^name:\s*standard-english\s*$", frontmatter) is not None,
            "SKILL.md frontmatter must declare name: standard-english")
    require(re.search(r"(?m)^description:\s*.+$", frontmatter) is not None,
            "SKILL.md frontmatter missing description")


def validate_skill_contract(text: str) -> None:
    for heading in REQUIRED_HEADINGS:
        require(heading in text, f"SKILL.md missing required heading: {heading}")

    require("`standard-english`" in text, "SKILL.md missing renamed invocation")
    require("standardized-language" not in text, "SKILL.md contains stale skill name: standardized-language")


def validate_reference_documents() -> None:
    for rel_path, heading in REFERENCE_HEADINGS.items():
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        require(heading in text, f"{rel_path} missing heading: {heading}")
        require("standardized-language" not in text,
                f"{rel_path} contains stale skill name: standardized-language")


def validate_local_links(text: str) -> None:
    # Validate backticked local Markdown paths, which agent skills commonly use as load instructions.
    pattern = re.compile(r"`((?:\./)?(?:references|templates)/[^`\n]+\.md)`")
    for link in sorted(set(pattern.findall(text))):
        normalized = link[2:] if link.startswith("./") else link
        target = ROOT / normalized
        require(target.is_file(), f"SKILL.md links missing local document: {link}")

    # Require explicit root-relative notation so validators do not resolve links against another skill.
    bare_pattern = re.compile(r"`((?:references|templates)/[^`\n]+\.md)`")
    bare_links = sorted(set(bare_pattern.findall(text)))
    require(not bare_links,
            "use validator-safe ./references/... or ./templates/... paths: " + ", ".join(bare_links))


def validate_repository_name_leaks() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix not in {".md", ".py", ".yml", ".yaml"}:
            continue
        text = path.read_text(encoding="utf-8")
        require("skills/standardized-language" not in text,
                f"{path.relative_to(ROOT)} contains old repository path")


def main() -> int:
    try:
        validate_required_files()
        skill_text = SKILL.read_text(encoding="utf-8")
        validate_frontmatter(skill_text)
        validate_skill_contract(skill_text)
        validate_reference_documents()
        validate_local_links(skill_text)
        validate_repository_name_leaks()
    except (AssertionError, OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("Standard English skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
