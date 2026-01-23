from __future__ import annotations

from chartcoach.catalog.model import Guideline
from chartcoach.catalog.parse import parse_guideline


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


def test_guideline_sections_property_parses_body() -> None:
    guideline = Guideline(
        id="g1",
        title="T",
        description="D",
        bibliography=None,
        labels=["chart:bar"],
        body="\n".join(
            [
                "Some dangling content.",
                "",
                "## The Advice <!-- role: advice -->",
                "",
                "Do this.",
            ]
        ),
    )
    sections = guideline.sections
    assert sections[0].role == sections[0].DANGLING_ROLE
    assert sections[1].role == "advice"


def test_guideline_to_markdown_roundtrip() -> None:
    md = _guideline_markdown(bibliography="references.bib")
    guideline = parse_guideline(md)
    assert guideline.id == "g1"
    assert guideline.bibliography == "references.bib"
    assert len(guideline.sections) > 0

    md2 = guideline.to_markdown()
    guideline2 = parse_guideline(md2)
    assert guideline2.id == guideline.id
    assert guideline2.title == guideline.title
    assert guideline2.description == guideline.description
    assert guideline2.labels == guideline.labels
