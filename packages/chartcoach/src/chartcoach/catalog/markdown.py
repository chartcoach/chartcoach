from __future__ import annotations

import re
from collections.abc import Mapping, Sequence

from .entries import Guideline, Section

SECTION_HEADING_RE = re.compile(r"^##\s+(.+?)\s*<!--\s*role:\s*(.*?)\s*-->\s*$")
GUIDELINE_FRONTMATTER_FIELDS = frozenset({"id", "title", "description", "labels"})


def parse_guideline(markdown: str) -> Guideline:
    """Parse an authored guideline Markdown document."""

    frontmatter, body = parse_markdown_with_frontmatter(markdown)
    metadata = dict(frontmatter)
    _pop_bibliography(metadata)
    return _guideline_from_source(metadata, body, ())


def parse_guideline_sections(body: str) -> list[Section]:
    """Parse guideline section headings and content."""

    sections: list[Section] = []
    current_role: str | None = None
    current_title = ""
    current_content: list[str] = []

    def flush() -> None:
        nonlocal current_role, current_title, current_content
        content = "\n".join(current_content).strip()
        if current_role is None:
            if content:
                sections.append(
                    Section(role=Section.DANGLING_ROLE, title="", content=content)
                )
        else:
            sections.append(
                Section(role=current_role, title=current_title, content=content)
            )
        current_role = None
        current_title = ""
        current_content = []

    for line in body.splitlines():
        match = SECTION_HEADING_RE.match(line)
        if match is None:
            current_content.append(line)
            continue
        flush()
        current_title = match.group(1).strip()
        current_role = match.group(2).strip()

    flush()
    return sections


def parse_markdown_with_frontmatter(markdown: str) -> tuple[dict[str, object], str]:
    """Parse Markdown and its YAML frontmatter."""

    import yaml

    if not markdown.startswith("---"):
        return {}, markdown

    parts = markdown.split("---", 2)
    if len(parts) < 3:
        return {}, markdown

    frontmatter = yaml.safe_load(parts[1].strip()) or {}
    if not isinstance(frontmatter, Mapping):
        raise ValueError("Guideline frontmatter must be a mapping.")
    return dict(frontmatter), parts[2].strip()


def _guideline_from_source(
    metadata: Mapping[str, object],
    body: str,
    references: Sequence[str],
) -> Guideline:
    fields = set(metadata)
    unexpected = sorted(fields - GUIDELINE_FRONTMATTER_FIELDS)
    if unexpected:
        raise ValueError(
            "Guideline frontmatter has unsupported field(s): "
            + ", ".join(unexpected)
            + "."
        )
    return Guideline.from_mapping(
        {
            "id": metadata.get("id"),
            "title": metadata.get("title"),
            "description": metadata.get("description"),
            "labels": metadata.get("labels", []),
            "sections": [
                section.to_record() for section in parse_guideline_sections(body)
            ],
            "references": list(references),
        }
    )


def _pop_bibliography(metadata: dict[str, object]) -> str | None:
    bibliography = metadata.pop("bibliography", None)
    if bibliography is not None and not isinstance(bibliography, str):
        raise TypeError("bibliography must be a string or null.")
    return bibliography


__all__ = ["parse_guideline", "parse_guideline_sections"]
