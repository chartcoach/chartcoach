import pytest

from chartcoach.catalog.entries import Guideline, Section
from chartcoach.catalog.markdown import parse_guideline


def test_parse_guideline_builds_sections_and_derived_body() -> None:
    guideline = parse_guideline(
        """---
id: direct-labels
title: Use direct labels
description: Label marks directly when space permits.
bibliography: references.bib
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

    assert guideline.labels == ("chart:line", "goal:comparison")
    assert [(section.role, section.title) for section in guideline.sections] == [
        ("__dangling__", ""),
        ("advice", "Advice"),
        ("tradeoffs", "Tradeoffs"),
    ]
    assert guideline.body.startswith("Introductory note.\n\n## Advice")


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


def test_parse_guideline_preserves_unsectioned_guidance() -> None:
    guideline = parse_guideline(
        """---
id: plain-guideline
title: Plain guideline
description: A short guideline.
labels: []
---

Keep the chart focused.
"""
    )

    assert guideline.sections == (
        Section(
            role=Section.DANGLING_ROLE,
            title="",
            content="Keep the chart focused.",
        ),
    )
    assert guideline.body == "Keep the chart focused."


def test_guideline_rejects_nonleading_dangling_sections() -> None:
    with pytest.raises(ValueError, match="dangling section must be first"):
        Guideline(
            id="direct-labels",
            title="Use direct labels",
            description="Label marks directly when space permits.",
            sections=(
                Section(role="advice", title="Advice", content="Place labels."),
                Section(role="__dangling__", title="", content="Late preamble."),
            ),
        )
