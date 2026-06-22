import pytest

from chartcoach.catalog.entries import Guideline, Section
from chartcoach.catalog.markdown import (
    guideline_to_markdown,
    parse_guideline,
    parse_guideline_sections,
)


def test_parse_guideline_frontmatter_and_sections() -> None:
    guideline = parse_guideline(
        """---
id: direct-labels
title: Use direct labels
description: Label marks directly when space permits.
labels:
  - chart:line
  - goal:comparison
---

Introductory note.

## Advice <!-- role: advice -->

Place the label close to the mark it names.

## Tradeoffs <!-- role: tradeoffs -->

Dense charts may still need a legend.
"""
    )

    assert guideline.id == "direct-labels"
    assert guideline.labels == ("chart:line", "goal:comparison")
    assert [(section.role, section.title) for section in guideline.sections] == [
        ("__dangling__", ""),
        ("advice", "Advice"),
        ("tradeoffs", "Tradeoffs"),
    ]


def test_parse_guideline_rejects_non_mapping_frontmatter() -> None:
    with pytest.raises(ValueError, match="frontmatter must be a mapping"):
        parse_guideline(
            """---
- direct-labels
---

## Advice <!-- role: advice -->

Place the label close to the mark it names.
"""
        )


def test_guideline_markdown_roundtrip_preserves_core_fields() -> None:
    original = parse_guideline(
        """---
id: small-multiples
title: Use small multiples for repeated comparisons
description: Split repeated comparisons into aligned panels.
labels:
  - chart:small-multiple
---

## Advice <!-- role: advice -->

Use the same scale across panels when direct comparison is required.
"""
    )

    reparsed = parse_guideline(guideline_to_markdown(original))

    assert reparsed.id == original.id
    assert reparsed.title == original.title
    assert reparsed.description == original.description
    assert parse_guideline_sections(reparsed.body)[0].role == "advice"


def test_guideline_accepts_body_and_derives_sections() -> None:
    guideline = Guideline(
        id="direct-labels",
        title="Use direct labels",
        description="Label marks directly when space permits.",
        body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
    )

    assert [(section.role, section.title) for section in guideline.sections] == [
        ("advice", "Advice")
    ]
    assert guideline.to_record()["sections"] == [
        {
            "role": "advice",
            "title": "Advice",
            "content": "Place labels near marks.",
        }
    ]


def test_guideline_accepts_sections_and_derives_body() -> None:
    guideline = Guideline(
        id="direct-labels",
        title="Use direct labels",
        description="Label marks directly when space permits.",
        sections=(
            Section(
                role="advice",
                title="Advice",
                content="Place labels near marks.",
            ),
        ),
    )

    assert (
        guideline.body == "## Advice <!-- role: advice -->\n\nPlace labels near marks."
    )
    assert guideline.to_record()["body"] == guideline.body


def test_guideline_requires_body_or_sections() -> None:
    with pytest.raises(ValueError, match="body or sections"):
        Guideline(
            id="direct-labels",
            title="Use direct labels",
            description="Label marks directly when space permits.",
        )
