from __future__ import annotations

import dataclasses as dc
from collections.abc import Mapping, Sequence
from typing import ClassVar, cast

from .labels import normalize_label


@dc.dataclass(frozen=True, slots=True)
class Guideline:
    """One guideline with a synchronized markdown body and section list."""

    id: str
    title: str
    description: str
    body: str = ""
    bibliography: str | None = None
    labels: tuple[str, ...] = dc.field(default_factory=tuple)
    sections: tuple["Section", ...] = dc.field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not isinstance(self.body, str):
            raise TypeError("body must be a string.")
        object.__setattr__(
            self,
            "labels",
            tuple(
                normalize_label(label, context="guideline label")
                for label in _str_sequence(self.labels, "labels")
            ),
        )
        body, sections = _normalize_body_and_sections(self.body, self.sections)
        object.__setattr__(self, "body", body)
        object.__setattr__(
            self,
            "sections",
            sections,
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
            body=_optional_field_str(values, "body"),
            bibliography=_optional_str(values.get("bibliography")),
            labels=_str_sequence(values.get("labels") or [], "labels"),
            sections=(
                _section_sequence(values["sections"]) if "sections" in values else ()
            ),
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


@dc.dataclass(frozen=True, slots=True)
class CatalogEntry:
    """One catalog entry with a guideline and its raw BibTeX references."""

    guideline: Guideline
    references: tuple[str, ...] = dc.field(default_factory=tuple)

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "references",
            _str_sequence(self.references, "references"),
        )

    @classmethod
    def from_mapping(cls, data: object) -> "CatalogEntry":
        """Build an entry from a serialized catalog row."""
        if isinstance(data, cls):
            return data
        if not isinstance(data, Mapping):
            raise TypeError("Catalog entry data must be a mapping.")
        values = cast(Mapping[str, object], data)
        guideline = Guideline.from_mapping(values.get("guideline"))
        top_level_id = values.get("id")
        if top_level_id is not None and top_level_id != guideline.id:
            raise ValueError(
                f"catalog row id {top_level_id!r} does not match guideline id {guideline.id!r}."
            )
        return cls(
            guideline=guideline,
            references=_str_sequence(values.get("references") or [], "references"),
        )

    @property
    def id(self) -> str:
        """Return the stable id of this catalog entry."""

        return self.guideline.id

    def to_record(self) -> dict[str, object]:
        """Return the serialized entry shape used by catalog dataframes."""
        return {
            "id": self.id,
            "guideline": self.guideline.to_record(),
            "references": list(self.references),
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


def _optional_field_str(data: Mapping[str, object], key: str) -> str:
    value = data.get(key, "")
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


def _normalize_body_and_sections(
    body: str,
    sections: object,
) -> tuple[str, tuple[Section, ...]]:
    parsed_sections = _section_sequence(sections)
    normalized_body = body.strip()
    if normalized_body and parsed_sections:
        return normalized_body, parsed_sections
    if normalized_body:
        parsed_from_body = _parse_body_sections(normalized_body)
        if not parsed_from_body:
            raise ValueError("body must contain at least one section.")
        return normalized_body, parsed_from_body
    if parsed_sections:
        return _sections_to_body(parsed_sections), parsed_sections
    raise ValueError("body or sections must be provided.")


def _parse_body_sections(body: str) -> tuple[Section, ...]:
    from .markdown import parse_guideline_sections

    return tuple(parse_guideline_sections(body))


def _sections_to_body(sections: Sequence[Section]) -> str:
    return "\n\n".join(_section_to_body(section) for section in sections).strip()


def _section_to_body(section: Section) -> str:
    content = section.content.strip()
    if section.role == Section.DANGLING_ROLE:
        return content
    return (
        f"## {section.title.strip()} <!-- role: {section.role} -->\n\n{content}".strip()
    )


__all__ = ["CatalogEntry", "Guideline", "Section"]
