from __future__ import annotations

from collections.abc import Sequence


class CatalogError(ValueError):
    """Catalog primitive error with optional recovery hints."""

    def __init__(self, message: str, *, hints: Sequence[str] = ()) -> None:
        super().__init__(message)
        self.message = message
        self.hints = tuple(hints)

    def __str__(self) -> str:
        return self.message


class CatalogLookupError(CatalogError):
    """Raised when a catalog id, label, role, or table lookup fails."""


class CatalogValidationError(CatalogError):
    """Raised when catalog input violates a supported contract."""


class CatalogQueryError(CatalogError):
    """Raised when a catalog query cannot be evaluated."""


__all__ = [
    "CatalogError",
    "CatalogLookupError",
    "CatalogQueryError",
    "CatalogValidationError",
]
