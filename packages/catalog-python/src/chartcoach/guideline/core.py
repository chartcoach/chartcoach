from __future__ import annotations

import dataclasses as dc
from collections.abc import Mapping
from typing import ClassVar, cast


@dc.dataclass(frozen=True, slots=True)
class Guideline:
    """One piece of chart guidance, with its summary, labels, and full text."""

    id: str
    title: str
    description: str
    body: str
    bibliography: str | None = None
    labels: list[str] = dc.field(default_factory=list)

    @classmethod
    def model_validate(cls, data: object) -> "Guideline":
        """Build a guideline from a raw mapping."""
        if isinstance(data, cls):
            return data
        if not isinstance(data, Mapping):
            raise TypeError("Guideline data must be a mapping.")
        values = cast(Mapping[str, object], data)

        return cls(
            id=_required_str(values, "id"),
            title=_required_str(values, "title"),
            description=_required_str(values, "description"),
            body=_required_str(values, "body"),
            bibliography=_optional_str(values.get("bibliography")),
            labels=_str_list(values.get("labels") or []),
        )

    def model_dump(self) -> dict[str, object]:
        """Return the serialized shape used by catalog dataframes."""
        return {
            "id": self.id,
            "title": self.title,
            "bibliography": self.bibliography,
            "description": self.description,
            "labels": self.labels,
            "body": self.body,
            "sections": [section.model_dump() for section in self.sections],
        }

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


@dc.dataclass(frozen=True, slots=True)
class Section:
    """One titled part of a guideline."""

    DANGLING_ROLE: ClassVar[str] = "__dangling__"

    role: str
    title: str
    content: str

    @classmethod
    def model_validate(cls, data: object) -> "Section":
        """Build a section from a raw mapping."""
        if isinstance(data, cls):
            return data
        if not isinstance(data, Mapping):
            raise TypeError("Section data must be a mapping.")
        values = cast(Mapping[str, object], data)
        return cls(
            role=_required_str(values, "role"),
            title=_required_str(values, "title"),
            content=_required_str(values, "content"),
        )

    def model_dump(self) -> dict[str, str]:
        """Return the serialized section shape."""
        return {
            "role": self.role,
            "title": self.title,
            "content": self.content,
        }


def _required_str(data: Mapping[str, object], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str):
        raise TypeError(f"{key} must be a string.")
    return value


def _optional_str(value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise TypeError("bibliography must be a string or null.")
    return value


def _str_list(value: object) -> list[str]:
    if not isinstance(value, list):
        raise TypeError("labels must be a list of strings.")
    parsed: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise TypeError("labels must be a list of strings.")
        parsed.append(item)
    return parsed


__all__ = ["Guideline", "Section"]
