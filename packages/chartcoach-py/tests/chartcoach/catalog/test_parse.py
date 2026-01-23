from __future__ import annotations

from chartcoach.catalog.parse import (
    parse_bibtex,
    parse_guideline,
    parse_guideline_sections,
    parse_markdown_with_frontmatter,
)


def _guideline_markdown(
    *,
    guideline_id: str = "g1",
    title: str = "Use direct labels",
    description: str = "Short description.",
    bibliography: str | None = None,
    labels: list[str] | None = None,
    body: str = "## The Advice <!-- role: advice -->\n\nDo the thing.",
) -> str:
    labels = labels or ["chart:bar", "goal:comparison"]
    bibliography_line = (
        "" if bibliography is None else f"bibliography: {bibliography}\n"
    )
    labels_yaml = "\n".join([f"  - {label}" for label in labels])
    return (
        "---\n"
        f"id: {guideline_id}\n"
        f"title: {title}\n"
        f"{bibliography_line}"
        f"description: {description}\n"
        "labels:\n"
        f"{labels_yaml}\n"
        "---\n\n"
        f"{body}\n"
    )


def test_parse_markdown_with_frontmatter_variants() -> None:
    assert parse_markdown_with_frontmatter("hello") == ({}, "hello")
    assert parse_markdown_with_frontmatter("---\nid: x\n") == ({}, "---\nid: x\n")

    fm, body = parse_markdown_with_frontmatter("---\nid: x\n---\nbody\n")
    assert fm["id"] == "x"
    assert body == "body"


def test_parse_guideline_smoke() -> None:
    md = _guideline_markdown(bibliography="references.bib")
    guideline = parse_guideline(md)
    assert guideline.id == "g1"
    assert guideline.bibliography == "references.bib"


def test_parse_guideline_sections_handles_dangling_and_roles() -> None:
    body = "\n".join(
        [
            "Some dangling content.",
            "",
            "## The Advice <!-- role: advice -->",
            "",
            "Do this.",
            "",
            "## Why <!-- role: reason -->",
            "",
            "Because.",
        ]
    )
    sections = parse_guideline_sections(body)
    assert sections[0].role == sections[0].DANGLING_ROLE
    assert sections[1].role == "advice"
    assert sections[1].content == "Do this."
    assert sections[2].role == "reason"


def test_parse_guideline_sections_all_dangling() -> None:
    sections = parse_guideline_sections("Just text, no headings.")
    assert len(sections) == 1
    assert sections[0].role == sections[0].DANGLING_ROLE


def test_parse_bibtex_strips_comments_and_splits_entries() -> None:
    bib = "\n".join(
        [
            "% a comment",
            "@article{a,",
            "  title={A},",
            "}",
            "",
            "@article{b,",
            "  title={B},",
            "}",
        ]
    )
    entries = parse_bibtex(bib)
    assert len(entries) == 2
    assert entries[0].startswith("@article{a")
    assert entries[1].startswith("@article{b")
