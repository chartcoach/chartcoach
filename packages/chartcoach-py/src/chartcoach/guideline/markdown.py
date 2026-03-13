from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .core import Guideline


SECTION_HEADING_RE = re.compile(r"^##\s+(.+?)\s*<!--\s*role:\s*(\S+)\s*-->\s*$")


def parse_guideline(markdown: str):
    """Parse markdown with YAML frontmatter into a Guideline model."""
    from .core import Guideline

    frontmatter, body = parse_markdown_with_frontmatter(markdown)
    return Guideline.model_validate({**frontmatter, "body": body})


def parse_guideline_section_records(body: str) -> list[dict[str, str]]:
    """Parse section headings and content into raw section records."""
    from .core import GuidelineSection

    sections: list[dict[str, str]] = []
    current_section: dict[str, str] | None = None
    current_content_lines: list[str] = []

    def flush_dangling() -> None:
        content = "\n".join(current_content_lines).strip()
        if not content:
            return
        sections.append(
            {
                "role": GuidelineSection.DANGLING_ROLE,
                "title": "",
                "content": content,
            }
        )

    def flush_section() -> None:
        nonlocal current_section, current_content_lines
        if current_section is None:
            flush_dangling()
            current_content_lines = []
            return

        sections.append(
            {
                **current_section,
                "content": "\n".join(current_content_lines).strip(),
            }
        )
        current_section = None
        current_content_lines = []

    for line in body.splitlines():
        match = SECTION_HEADING_RE.match(line)
        if not match:
            current_content_lines.append(line)
            continue

        flush_section()
        current_section = {
            "title": match.group(1).strip(),
            "role": match.group(2).strip(),
        }

    flush_section()
    return sections


def parse_guideline_sections(body: str):
    """Parse the guideline body into GuidelineSection models."""
    from .core import GuidelineSection

    return [
        GuidelineSection.model_validate(section)
        for section in parse_guideline_section_records(body)
    ]


def parse_markdown_with_frontmatter(markdown: str) -> tuple[dict[str, Any], str]:
    """Parse markdown with optional YAML frontmatter."""
    import yaml

    if not markdown.startswith("---"):
        return {}, markdown

    parts = markdown.split("---", 2)
    if len(parts) < 3:
        return {}, markdown

    frontmatter_str = parts[1].strip()
    body = parts[2].strip()
    frontmatter = yaml.safe_load(frontmatter_str) or {}
    return frontmatter, body


def guideline_to_markdown(guideline: Guideline) -> str:
    """Serialize a Guideline model back to markdown."""
    import mdformat
    import yaml

    frontmatter = {
        "id": guideline.id,
        "title": guideline.title,
        "bibliography": guideline.bibliography,
        "description": guideline.description,
        "labels": guideline.labels,
    }
    frontmatter = {
        key: value for key, value in frontmatter.items() if value is not None
    }
    frontmatter_yaml = yaml.dump(frontmatter, sort_keys=False).strip()
    formatted_body = mdformat.text(guideline.body)
    return "\n".join(["---", frontmatter_yaml, "---", "", formatted_body])
