#!/usr/bin/env python3
"""Validate the Standard English skill package and behavioral fixtures."""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
CATALOG = ROOT / "data" / "standards-catalog.yaml"
VALIDATOR = Path(__file__).resolve()

REQUIRED_FILES = [
    SKILL,
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "requirements-dev.txt",
    ROOT / "references" / "routing-algorithm.md",
    ROOT / "references" / "risk-and-escalation.md",
    ROOT / "references" / "selection-matrix.md",
    ROOT / "references" / "standards-catalog.md",
    ROOT / "references" / "output-contract.md",
    CATALOG,
    ROOT / "tests" / "routing-cases.yaml",
    ROOT / "tests" / "conflict-cases.yaml",
    ROOT / "tests" / "claim-boundary-cases.yaml",
    ROOT / "scripts" / "render_catalog.py",
]

REQUIRED_HEADINGS = [
    "# Standard English",
    "## Default posture",
    "## No-profile gate",
    "## Independent assessments",
    "## Workflow",
    "## Required output",
]

REFERENCE_HEADINGS = {
    "references/routing-algorithm.md": "# Routing Algorithm",
    "references/risk-and-escalation.md": "# Risk and Escalation",
    "references/selection-matrix.md": "# Selection Matrix",
    "references/standards-catalog.md": "# Standards Catalog",
    "references/output-contract.md": "# Output Contract",
}

REQUIRED_PROFILE_FIELDS = {
    "id",
    "name",
    "designation",
    "authority",
    "role",
    "status",
    "publication_date",
    "lifecycle_note",
    "official_source",
    "access",
    "scope",
    "exclusions",
    "conformance_prerequisites",
    "last_verified",
}

VALID_ROLES = {
    "governing-framework",
    "document-system",
    "content-language-profile",
    "controlled-language",
    "normative-keyword-system",
    "terminology-method",
    "interchange-format",
    "process-standard",
    "accessibility-requirement",
    "informative-guidance",
    "editorial-guide",
}

PROFILE_REFERENCE_KEYS = {
    "profile",
    "document_profile",
    "language_constraint",
    "delivery_overlay",
    "governing_source",
    "preferred",
    "reject_role_misuse",
    "allowed_primary",
    "allowed_supporting",
    "forbidden",
    "eliminate",
    "forbidden_substitution",
}

NON_REGISTRY_ROUTE_VALUES = {
    "no-external-profile",
    "governing-publication-rules",
    "supplied-company-standard",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def warn(message: str) -> None:
    print(f"WARNING: {message}", file=sys.stderr)


def read_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise AssertionError(f"invalid YAML in {path.relative_to(ROOT)}: {exc}") from exc


def validate_required_files() -> None:
    for path in REQUIRED_FILES:
        require(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")
        require(path.stat().st_size > 0, f"empty required file: {path.relative_to(ROOT)}")


def parse_frontmatter(text: str) -> dict[str, Any]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    require(match is not None, "SKILL.md missing YAML frontmatter")
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise AssertionError(f"SKILL.md frontmatter is invalid YAML: {exc}") from exc
    require(isinstance(data, dict), "SKILL.md frontmatter must be a mapping")
    return data


def validate_frontmatter(text: str) -> None:
    frontmatter = parse_frontmatter(text)
    require(frontmatter.get("name") == "standard-english",
            "SKILL.md frontmatter must declare name: standard-english")
    description = frontmatter.get("description")
    require(isinstance(description, str) and len(description.strip()) >= 100,
            "SKILL.md frontmatter description must be a substantive string")
    required_scope_terms = [
        "controlled-language",
        "requirements language",
        "Do not use for ordinary grammar correction",
        "casual messages",
    ]
    for term in required_scope_terms:
        require(term.lower() in description.lower(),
                f"SKILL.md description missing activation boundary: {term}")


def validate_skill_contract(text: str) -> None:
    for heading in REQUIRED_HEADINGS:
        require(heading in text, f"SKILL.md missing required heading: {heading}")

    required_invariants = [
        "No external profile required",
        "Profile fit",
        "Evidence strength",
        "High consequence alone does not require",
        "CAN-ASC-3.1:2025",
        "ASD-STE100",
        "WCAG",
        "ISO 24495-3",
        "ISO 18587",
    ]
    for invariant in required_invariants:
        require(invariant in text, f"SKILL.md missing invariant: {invariant}")

    require("`standard-english`" in text, "SKILL.md missing invocation name")
    require("standardized-language" not in text,
            "SKILL.md contains stale skill name: standardized-language")


def validate_reference_documents() -> None:
    for rel_path, heading in REFERENCE_HEADINGS.items():
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        require(heading in text, f"{rel_path} missing heading: {heading}")
        require("standardized-language" not in text,
                f"{rel_path} contains stale skill name: standardized-language")


def extract_local_paths(text: str) -> set[str]:
    paths: set[str] = set()
    for match in re.findall(r"`((?:\./)?(?:references|data|tests|templates)/[^`\n]+\.(?:md|yaml|yml))`", text):
        paths.add(match)
    for match in re.findall(r"\[[^\]]+\]\(((?:\./)?(?:references|data|tests|templates)/[^)]+)\)", text):
        paths.add(match)
    return paths


def validate_local_links() -> None:
    for source in [SKILL, ROOT / "README.md"]:
        text = source.read_text(encoding="utf-8")
        for link in sorted(extract_local_paths(text)):
            normalized = link[2:] if link.startswith("./") else link
            target = ROOT / normalized
            require(target.is_file(),
                    f"{source.relative_to(ROOT)} links missing local document: {link}")

    skill_text = SKILL.read_text(encoding="utf-8")
    bare_pattern = re.compile(r"`((?:references|data|tests|templates)/[^`\n]+\.(?:md|yaml|yml))`")
    bare_links = sorted(set(bare_pattern.findall(skill_text)))
    require(not bare_links,
            "use validator-safe ./ paths in SKILL.md: " + ", ".join(bare_links))


def normalize_date(value: Any, field: str) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError as exc:
            raise AssertionError(f"invalid ISO date for {field}: {value}") from exc
    raise AssertionError(f"invalid date value for {field}: {value!r}")


def validate_catalog() -> set[str]:
    data = read_yaml(CATALOG)
    require(isinstance(data, dict), "catalog root must be a mapping")
    require(data.get("schema_version") == 1, "unsupported catalog schema_version")
    require(isinstance(data.get("freshness_warning_days"), int),
            "catalog freshness_warning_days must be an integer")
    normalize_date(data.get("last_reviewed"), "last_reviewed")

    profiles = data.get("profiles")
    require(isinstance(profiles, list) and profiles,
            "catalog profiles must be a non-empty list")

    ids: set[str] = set()
    designations: set[str] = set()
    today = date.today()
    freshness_days = data["freshness_warning_days"]

    for index, profile in enumerate(profiles):
        require(isinstance(profile, dict), f"catalog profile {index} must be a mapping")
        missing = REQUIRED_PROFILE_FIELDS - set(profile)
        require(not missing,
                f"catalog profile {index} missing fields: {', '.join(sorted(missing))}")

        profile_id = profile["id"]
        require(isinstance(profile_id, str) and re.fullmatch(r"[a-z0-9][a-z0-9-]*", profile_id),
                f"invalid profile id: {profile_id!r}")
        require(profile_id not in ids, f"duplicate profile id: {profile_id}")
        ids.add(profile_id)

        designation = profile["designation"]
        require(isinstance(designation, str) and designation.strip(),
                f"{profile_id}: designation must be a non-empty string")
        require(designation not in designations, f"duplicate designation: {designation}")
        designations.add(designation)

        require(profile["role"] in VALID_ROLES,
                f"{profile_id}: invalid role {profile['role']!r}")
        for list_field in ("scope", "exclusions", "conformance_prerequisites"):
            value = profile[list_field]
            require(isinstance(value, list) and value and all(isinstance(item, str) and item.strip() for item in value),
                    f"{profile_id}: {list_field} must be a non-empty string list")

        source = profile["official_source"]
        parsed = urlparse(source)
        require(parsed.scheme == "https" and parsed.netloc,
                f"{profile_id}: official_source must be an HTTPS URL")

        verified = normalize_date(profile["last_verified"], f"{profile_id}.last_verified")
        age = (today - verified).days
        if age > freshness_days:
            warn(f"{profile_id} source verification is {age} days old")

    require("can-asc-3-1" in ids, "catalog missing CAN-ASC profile")
    require("asd-ste100" in ids, "catalog missing ASD-STE100 profile")
    require("iso-24495-3" in ids, "catalog missing ISO 24495-3 profile")
    require("wcag-2-2" in ids, "catalog missing WCAG 2.2 profile")
    return ids


def iter_profile_references(node: Any, parent_key: str | None = None) -> Iterable[tuple[str, str]]:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in PROFILE_REFERENCE_KEYS:
                values = value if isinstance(value, list) else [value]
                for item in values:
                    if isinstance(item, str):
                        yield key, item
            yield from iter_profile_references(value, key)
    elif isinstance(node, list):
        for item in node:
            yield from iter_profile_references(item, parent_key)


def validate_behavioral_tests(profile_ids: set[str]) -> None:
    seen_case_ids: set[str] = set()
    total = 0
    for path in sorted((ROOT / "tests").glob("*.yaml")):
        data = read_yaml(path)
        require(isinstance(data, dict), f"{path.relative_to(ROOT)} root must be a mapping")
        require(data.get("schema_version") == 1,
                f"{path.relative_to(ROOT)} has unsupported schema_version")
        cases = data.get("cases")
        require(isinstance(cases, list) and cases,
                f"{path.relative_to(ROOT)} cases must be non-empty")
        for case in cases:
            require(isinstance(case, dict), f"{path.relative_to(ROOT)} case must be a mapping")
            case_id = case.get("id")
            require(isinstance(case_id, str) and re.fullmatch(r"[a-z0-9][a-z0-9-]*", case_id),
                    f"invalid case id in {path.relative_to(ROOT)}: {case_id!r}")
            require(case_id not in seen_case_ids, f"duplicate behavioral case id: {case_id}")
            seen_case_ids.add(case_id)
            expected = case.get("expected")
            if expected is None and "permitted_claim" in case:
                expected = case
            require(expected is not None, f"{case_id}: missing expected result")
            require("input" in case or "evidence" in case,
                    f"{case_id}: requires input or evidence")
            total += 1

            for key, reference in iter_profile_references(expected):
                if reference in NON_REGISTRY_ROUTE_VALUES or reference.startswith("supplied-"):
                    continue
                require(reference in profile_ids,
                        f"{case_id}: unknown profile reference {reference!r} in {key}")

    require(total >= 35, f"behavioral suite is too small: {total} cases; require at least 35")


def validate_generated_catalog() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "render_catalog.py"), "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    require(result.returncode == 0,
            result.stderr.strip() or result.stdout.strip() or "generated catalog is stale")


def validate_repository_name_leaks() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.resolve() == VALIDATOR:
            continue
        if path.suffix not in {".md", ".py", ".yml", ".yaml", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8")
        require("skills/standardized-language" not in text,
                f"{path.relative_to(ROOT)} contains old repository path")
        require("name: standardized-language" not in text,
                f"{path.relative_to(ROOT)} contains old skill name")


def main() -> int:
    try:
        validate_required_files()
        skill_text = SKILL.read_text(encoding="utf-8")
        validate_frontmatter(skill_text)
        validate_skill_contract(skill_text)
        validate_reference_documents()
        validate_local_links()
        profile_ids = validate_catalog()
        validate_behavioral_tests(profile_ids)
        validate_generated_catalog()
        validate_repository_name_leaks()
    except (AssertionError, OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("Standard English skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
