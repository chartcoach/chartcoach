from __future__ import annotations

from collections.abc import Sequence


class CatalogError(ValueError):
    """Catalog operation error with optional recovery hints."""

    def __init__(self, message: str, *, hints: Sequence[str] = ()) -> None:
        super().__init__(message)
        self.message = message
        self.hints = tuple(hints)

    def __str__(self) -> str:
        if not self.hints:
            return self.message
        guidance = "\n".join(f"  - {hint}" for hint in self.hints)
        return f"{self.message}\n\nGuidance:\n{guidance}"


class CatalogLookupError(CatalogError):
    """Raised when a catalog id, label, role, or table lookup fails."""


class CatalogValidationError(CatalogError):
    """Raised when catalog input violates a supported contract."""


def require_string_sequence(name: str, values: Sequence[str]) -> None:
    """Reject a scalar string or a sequence containing non-string values."""

    if isinstance(values, str):
        raise CatalogValidationError(
            f"{name} must be a sequence of strings, not one string.",
            hints=[f"Pass {name}=[{values!r}]."],
        )
    if not all(isinstance(value, str) for value in values):
        raise CatalogValidationError(
            f"{name} must contain strings.",
            hints=[f"Pass {name} as a list or tuple of strings."],
        )


__all__ = [
    "CatalogError",
    "CatalogLookupError",
    "CatalogValidationError",
    "require_string_sequence",
]
