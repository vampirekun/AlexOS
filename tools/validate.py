"""Validate objective structure and references in the AlexOS repository."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
H1 = re.compile(r"^# (.+)$", re.MULTILINE)
HEADING = re.compile(r"^(#{1,6}) (.+)$", re.MULTILINE)
VALID_DOCUMENT_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")

REQUIRED_SECTIONS = {
    "playbooks": {
        "Use when",
        "Inputs",
        "Method",
        "Completion evidence",
        "Failure modes",
    },
    "heuristics": {"Applicability", "Benefit"},
    "policies": {"Requirements", "Rationale", "Failure modes"},
}

ALLOWED_LAYER_DEPENDENCIES = {
    "kernel": {"kernel"},
    "policies": {"kernel", "policies"},
    "knowledge": {"knowledge"},
    "heuristics": {"knowledge", "heuristics"},
    "playbooks": {
        "kernel",
        "policies",
        "knowledge",
        "heuristics",
        "playbooks",
        "docs",
    },
}


def github_slug(title: str) -> str:
    """Return the GitHub-style anchor used by AlexOS headings."""
    normalized = unicodedata.normalize("NFKD", title).lower().strip()
    normalized = re.sub(r"[^\w\s-]", "", normalized)
    normalized = re.sub(r"[\s-]+", "-", normalized)
    return normalized.strip("-")


def markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def validate_directory_indexes(errors: list[str], files: list[Path]) -> None:
    directories = sorted({path.parent for path in files} | {ROOT / "tools"})
    for directory in directories:
        readme = directory / "README.md"
        if not readme.exists():
            errors.append(f"{directory.relative_to(ROOT)}: missing README.md")
            continue

        if directory == ROOT:
            continue

        text = readme.read_text(encoding="utf-8")
        for child in sorted(directory.glob("*.md")):
            if child.name == "README.md":
                continue
            if f"]({child.name}" not in text:
                errors.append(
                    f"{readme.relative_to(ROOT)}: does not catalog {child.name}"
                )


def validate_document(path: Path, errors: list[str]) -> None:
    relative = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")

    if path.name != "README.md" and not VALID_DOCUMENT_NAME.fullmatch(path.name):
        errors.append(f"{relative}: filename must use lowercase kebab-case")

    h1s = H1.findall(text)
    if len(h1s) != 1:
        errors.append(f"{relative}: expected exactly one level-one heading")

    if path.name == "README.md" and path != ROOT / "README.md":
        for section in ("Contains", "Excludes"):
            if f"## {section}" not in text:
                errors.append(f"{relative}: missing README section '{section}'")

    layer = relative.parts[0] if len(relative.parts) > 1 else ""
    if path.name != "README.md" and layer in REQUIRED_SECTIONS:
        headings = {title.strip() for _, title in HEADING.findall(text)}
        for section in REQUIRED_SECTIONS[layer]:
            if section not in headings:
                errors.append(f"{relative}: missing required section '{section}'")

    if re.search(r"\b(?:TODO|TBD|FIXME)\b", text):
        errors.append(f"{relative}: contains an unresolved work marker")

    validate_links(path, text, errors)


def validate_links(path: Path, text: str, errors: list[str]) -> None:
    for match in MARKDOWN_LINK.finditer(text):
        raw_target = match.group(1).strip()
        if raw_target.startswith(("http://", "https://", "mailto:")):
            continue

        file_part, separator, anchor = raw_target.partition("#")
        target = path if not file_part else (path.parent / unquote(file_part)).resolve()

        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {raw_target}")
            continue

        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link: {raw_target}")
            continue

        validate_dependency(path, target, raw_target, errors)

        if separator and anchor and target.suffix.lower() == ".md":
            target_text = target.read_text(encoding="utf-8")
            anchors = {
                github_slug(title)
                for _, title in HEADING.findall(target_text)
            }
            if anchor not in anchors:
                errors.append(
                    f"{path.relative_to(ROOT)}: missing anchor '{anchor}' "
                    f"in {target.relative_to(ROOT)}"
                )


def validate_dependency(
    source: Path, target: Path, raw_target: str, errors: list[str]
) -> None:
    """Validate semantic layer direction using internal document references."""
    source_relative = source.relative_to(ROOT)
    target_relative = target.relative_to(ROOT)

    if len(source_relative.parts) < 2 or len(target_relative.parts) < 2:
        return

    source_layer = source_relative.parts[0]
    target_layer = target_relative.parts[0]
    allowed = ALLOWED_LAYER_DEPENDENCIES.get(source_layer)
    if allowed is not None and target_layer not in allowed:
        errors.append(
            f"{source_relative}: disallowed {source_layer} -> {target_layer} "
            f"dependency: {raw_target}"
        )


def main() -> int:
    errors: list[str] = []
    files = markdown_files()

    validate_directory_indexes(errors, files)
    for path in files:
        validate_document(path, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"\nValidation failed with {len(errors)} error(s).")
        return 1

    print(f"Validated {len(files)} Markdown files and their directory contracts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
