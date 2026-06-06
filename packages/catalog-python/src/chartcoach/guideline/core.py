from __future__ import annotations

import dataclasses as dc
from collections.abc import Mapping, Sequence
from typing import ClassVar, cast

from .labels import normalize_label


@dc.dataclass(frozen=True, slots=True)
class Guideline:
    """One piece of chart guidance, with its summary, labels, and full text."""

    id: str
    title: str
    description: str
    body: str
    bibliography: str | None = None
    labels: tuple[str, ...] = dc.field(default_factory=tuple)
    sections: tuple["Section", ...] = dc.field(default_factory=tuple)

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "labels",
            tuple(
                normalize_label(label, context="guideline label")
                for label in _str_sequence(self.labels, "labels")
            ),
        )
        object.__setattr__(
            self,
            "sections",
            _section_sequence(self.sections),
        )

    @classmethod
    def from_mapping(cls, data: object) -> "Guideline":
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
            labels=_str_sequence(values.get("labels") or [], "labels"),
            sections=_section_sequence(_required_field(values, "sections")),
        )

    def to_record(self) -> dict[str, object]:
        """Return the serialized shape used by catalog dataframes."""
        return {
            "id": self.id,
            "title": self.title,
            "bibliography": self.bibliography,
            "description": self.description,
            "labels": list(self.labels),
            "body": self.body,
            "sections": [section.to_record() for section in self.sections],
        }

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

    def __post_init__(self) -> None:
        if not isinstance(self.role, str):
            raise TypeError("role must be a string.")
        role = self.role.strip()
        if not role:
            raise ValueError("role must not be empty.")
        object.__setattr__(self, "role", role)

    @classmethod
    def from_mapping(cls, data: object) -> "Section":
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

    def to_record(self) -> dict[str, str]:
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


def _required_field(data: Mapping[str, object], key: str) -> object:
    if key not in data:
        raise TypeError(f"{key} is required.")
    return data[key]


def _optional_str(value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise TypeError("bibliography must be a string or null.")
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


__all__ = ["Guideline", "Section"]
