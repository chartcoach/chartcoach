from __future__ import annotations

from typing import ClassVar

from pydantic import BaseModel, Field, computed_field


class Guideline(BaseModel):
    """One piece of chart guidance, with its summary, labels, and full text."""

    id: str = Field(
        description="Unique, URL-friendly identifier for the guideline.",
        examples=["use-direct-labels-not-legends"],
    )
    title: str = Field(
        description="Short action-oriented title.",
        examples=["Use direct labels, not legends"],
    )
    bibliography: str | None = Field(
        None,
        description="Path to the bibliography file for citations.",
    )
    description: str = Field(
        description="Short summary of what the guideline helps with.",
    )
    labels: list[str] = Field(
        default_factory=list,
        description="Structured tags used for filtering and grouping.",
        examples=[
            [
                "chart:bar",
                "goal:comparison",
                "topic:accessibility",
                "audience:general",
                "impact:credibility",
            ]
        ],
    )
    body: str = Field(
        description="Full markdown body of the guideline.",
    )

    @computed_field
    @property
    def sections(self) -> list["Section"]:
        """Return the titled parts parsed from the guideline body."""

        from .markdown import parse_guideline_section_records

        return [
            Section.model_validate(section)
            for section in parse_guideline_section_records(self.body)
        ]

    def to_markdown(self) -> str:
        """Return the guideline in the markdown format used on disk."""

        from .markdown import guideline_to_markdown

        return guideline_to_markdown(self)


class Section(BaseModel):
    """One titled part of a guideline."""

    DANGLING_ROLE: ClassVar[str] = "__dangling__"

    role: str = Field(
        description="The role of the section.",
        examples=["advice", "reason", "situation"],
    )
    title: str = Field(
        description="Section heading text.",
        examples=["The Advice", "Why This Matters"],
    )
    content: str = Field(
        description="Markdown content for this section.",
    )


__all__ = ["Guideline", "Section"]
