from __future__ import annotations

import dataclasses as dc
from collections.abc import Mapping, Sequence
from typing import ClassVar, cast

from .labels import normalize_label

CATALOG_ROW_FIELDS = frozenset(
    {"id", "title", "description", "labels", "sections", "references"}
)
SECTION_FIELDS = frozenset({"role", "title", "content"})


@dc.dataclass(frozen=True, slots=True)
class Guideline:
    """One compiled guideline and its BibTeX references."""

    id: str
    title: str
    description: str
    labels: tuple[str, ...] = dc.field(default_factory=tuple)
    sections: tuple[Section, ...] = dc.field(default_factory=tuple)
    references: tuple[str, ...] = dc.field(default_factory=tuple)

    def __post_init__(self) -> None:
        for field in ("id", "title", "description"):
            if not isinstance(getattr(self, field), str):
                raise TypeError(f"{field} must be a string.")
        if not self.id:
            raise ValueError("id must not be empty.")

        labels = _str_sequence(self.labels, "labels")
        normalized_labels = tuple(
            normalize_label(label, context="guideline label") for label in labels
        )
        if labels != normalized_labels:
            raise ValueError("labels must use canonical values.")

        sections = _section_sequence(self.sections)
        if not sections:
            raise ValueError("sections must contain at least one section.")
        _validate_dangling_sections(sections)

        object.__setattr__(self, "labels", labels)
        object.__setattr__(self, "sections", sections)
        object.__setattr__(
            self,
            "references",
            _str_sequence(self.references, "references"),
        )

    @classmethod
    def from_mapping(cls, data: object) -> Guideline:
        """Build a guideline from one compiled entry row."""

        if isinstance(data, cls):
            return data
        if not isinstance(data, Mapping):
            raise TypeError("Guideline data must be a mapping.")
        values = cast(Mapping[str, object], data)
        _require_fields(values, CATALOG_ROW_FIELDS, "Catalog row")
        return cls(
            id=_required_str(values, "id"),
            title=_required_str(values, "title"),
            description=_required_str(values, "description"),
            labels=_str_sequence(values["labels"], "labels"),
            sections=_section_sequence(values["sections"]),
            references=_str_sequence(values["references"], "references"),
        )

    @property
    def body(self) -> str:
        """Return markdown derived from the ordered sections."""

        return "\n\n".join(_section_to_body(section) for section in self.sections)

    def to_record(self) -> dict[str, object]:
        """Return one compiled entry row."""

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "labels": list(self.labels),
            "sections": [section.to_record() for section in self.sections],
            "references": list(self.references),
        }


@dc.dataclass(frozen=True, slots=True)
class Section:
    """One titled part of a guideline."""

    DANGLING_ROLE: ClassVar[str] = "__dangling__"

    role: str
    title: str
    content: str

    def __post_init__(self) -> None:
        for field in ("role", "title", "content"):
            value = getattr(self, field)
            if not isinstance(value, str):
                raise TypeError(f"{field} must be a string.")
            if value != value.strip():
                raise ValueError("sections must use canonical values.")
        if not self.role:
            raise ValueError("role must not be empty.")
        if self.role == self.DANGLING_ROLE:
            if self.title or not self.content:
                raise ValueError(
                    "dangling section requires empty title and non-empty content."
                )
        elif not self.title:
            raise ValueError("section title must not be empty.")

    @classmethod
    def from_mapping(cls, data: object) -> Section:
        """Build a section from one compiled section record."""

        if isinstance(data, cls):
            return data
        if not isinstance(data, Mapping):
            raise TypeError("Section data must be a mapping.")
        values = cast(Mapping[str, object], data)
        _require_fields(values, SECTION_FIELDS, "Section")
        return cls(
            role=_required_str(values, "role"),
            title=_required_str(values, "title"),
            content=_required_str(values, "content"),
        )

    def to_record(self) -> dict[str, str]:
        """Return one compiled section record."""

        return {
            "role": self.role,
            "title": self.title,
            "content": self.content,
        }


def _require_fields(
    values: Mapping[str, object], required: frozenset[str], context: str
) -> None:
    fields = set(values)
    missing = sorted(required - fields)
    unexpected = sorted(fields - required)
    if missing:
        raise ValueError(f"{context} is missing field(s): {', '.join(missing)}.")
    if unexpected:
        raise ValueError(
            f"{context} has unsupported field(s): {', '.join(unexpected)}."
        )


def _required_str(data: Mapping[str, object], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str):
        raise TypeError(f"{key} must be a string.")
    return value


def _str_sequence(value: object, field: str) -> tuple[str, ...]:
    if not isinstance(value, Sequence) or isinstance(value, str | bytes):
        raise TypeError(f"{field} must be a list of strings.")
    parsed: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise TypeError(f"{field} must be a list of strings.")
        parsed.append(item)
    return tuple(parsed)


def _section_sequence(value: object) -> tuple[Section, ...]:
    if not isinstance(value, Sequence) or isinstance(value, str | bytes):
        raise TypeError("sections must be a list of section records.")
    return tuple(Section.from_mapping(section) for section in value)


def _validate_dangling_sections(sections: Sequence[Section]) -> None:
    dangling = [
        index
        for index, section in enumerate(sections)
        if section.role == Section.DANGLING_ROLE
    ]
    if dangling and dangling != [0]:
        raise ValueError("dangling section must be first and unique.")


def _section_to_body(section: Section) -> str:
    if section.role == Section.DANGLING_ROLE:
        return section.content
    return f"## {section.title} <!-- role: {section.role} -->\n\n{section.content}"


__all__ = ["Guideline", "Section"]
