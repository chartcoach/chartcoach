from __future__ import annotations

import dataclasses as dc


@dc.dataclass(frozen=True, slots=True)
class ParsedLabel:
    """One catalog label split into family, category, and optional modifier."""

    family: str
    category: str
    modifier: str | None = None

    @property
    def value(self) -> str:
        """Return the category plus optional modifier."""

        if self.modifier is None:
            return self.category
        return f"{self.category}:{self.modifier}"

    @property
    def label(self) -> str:
        """Return the normalized label string."""

        if self.modifier is None:
            return f"{self.family}:{self.category}"
        return f"{self.family}:{self.category}:{self.modifier}"


def parse_label(value: object, *, context: str = "label") -> ParsedLabel:
    """Parse a catalog label with two or three colon-separated segments."""

    if not isinstance(value, str):
        raise TypeError(f"{context} must be a string.")
    parts = [part.strip() for part in value.strip().split(":")]
    if len(parts) not in {2, 3} or any(part == "" for part in parts):
        raise ValueError(
            f"{context} must use <family>:<category> or <family>:<category>:<modifier>."
        )
    return ParsedLabel(
        family=parts[0],
        category=parts[1],
        modifier=parts[2] if len(parts) == 3 else None,
    )


def normalize_label(value: object, *, context: str = "label") -> str:
    """Return a label after trimming the label and segment boundaries."""

    return parse_label(value, context=context).label


__all__ = ["ParsedLabel", "normalize_label", "parse_label"]
