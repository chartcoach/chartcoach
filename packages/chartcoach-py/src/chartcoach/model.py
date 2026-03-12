from typing import ClassVar

from pydantic import BaseModel, Field, computed_field


class Guideline(BaseModel):
    """Structured representation of a visualization design guideline."""

    id: str = Field(
        description="Unique, URL-friendly identifier serving as the guideline's permanent address",
        examples=["use-direct-labels-not-legends"],
    )
    title: str = Field(
        description="Actionable imperative instruction that serves as the main headline",
        examples=["Use direct labels, not legends"],
    )
    bibliography: str | None = Field(
        None,
        description="Path to the bibliography file for citations",
    )
    description: str = Field(
        description="Compelling summary of the advice, its core benefit, and when it's most needed -- optimized for both human and AI relevance determination"
    )
    labels: list[str] = Field(
        default_factory=list,
        description="Structured key:value tags for discoverability and filtering",
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
        description="Full markdown content containing structured sections with role annotations (e.g. advice, reason, situation, considerations, checks, improvements)",
    )

    @computed_field
    @property
    def sections(self) -> list["GuidelineSection"]:
        """Parse the body content into structured sections based on role annotations.

        Returns:
            A list of GuidelineSection objects representing the structured sections of the guideline body.
        """
        from .utils import parse_guideline_sections

        return parse_guideline_sections(self.body)

    def to_markdown(self) -> str:
        """Convert the guideline back to its markdown representation.

        Returns:
            The markdown string representation of the guideline.
        """
        from .utils import guideline_to_markdown

        return guideline_to_markdown(self)


class GuidelineSection(BaseModel):
    """Representation of a specific section within a guideline."""

    DANGLING_ROLE: ClassVar[str] = "__dangling__"

    role: str = Field(
        description="The role or type of the section",
        examples=["advice", "reason", "situation"],
    )
    title: str = Field(
        description="The title of the section",
        examples=["The Advice", "Why This Matters"],
    )
    content: str = Field(
        description="The markdown content of the section",
    )


class CatalogEntry(BaseModel):
    """Base class for entries in the catalog. A catalog entry is a folder that contains a guideline and all its assets, such as the reference .bib file, images, and example code."""

    guideline: Guideline = Field(
        description="The guideline entry associated with this catalog entry."
    )
    references: list[str] = Field(
        default_factory=list,
        description="BibTeX-formatted bibliography content for citations used in the guideline.",
    )

    @computed_field
    @property
    def id(self) -> str:
        """Get the unique identifier of the catalog entry.

        Returns:
            str: The unique identifier of the catalog entry.
        """
        return self.guideline.id
