from __future__ import annotations

from collections.abc import Mapping, Sequence
from types import MappingProxyType
from typing import Literal, TypeAlias

CatalogErrorCode: TypeAlias = Literal[
    "lookup",
    "invalid_input",
    "integrity",
    "unavailable_capability",
    "incompatible_profile",
    "embedding_failure",
    "operation_failed",
    "response_too_large",
]


class CatalogError(ValueError):
    """Catalog operation error with optional recovery hints."""

    default_code: CatalogErrorCode = "invalid_input"

    def __init__(
        self,
        message: str,
        *,
        code: CatalogErrorCode | None = None,
        details: Mapping[str, object] | None = None,
        hints: Sequence[str] = (),
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code or self.default_code
        self.details = MappingProxyType(dict(details or {}))
        self.hints = tuple(hints)

    def __str__(self) -> str:
        return format_error(self.message, self.hints)


class CatalogLookupError(CatalogError):
    """Raised when a catalog id, label, role, or table lookup fails."""

    default_code: CatalogErrorCode = "lookup"


class CatalogValidationError(CatalogError):
    """Raised when catalog input violates a supported contract."""

    default_code: CatalogErrorCode = "invalid_input"


class CatalogIntegrityError(CatalogError):
    """Raised when verified bytes or linked catalog digests disagree."""

    default_code: CatalogErrorCode = "integrity"


class CatalogCapabilityError(CatalogError):
    """Raised when an optional catalog capability is unavailable."""

    default_code: CatalogErrorCode = "unavailable_capability"


class CatalogProfileError(CatalogError):
    """Raised when an index profile cannot be used with its catalog."""

    default_code: CatalogErrorCode = "incompatible_profile"


class CatalogEmbeddingError(CatalogError):
    """Raised when an index embedding query cannot be completed."""

    default_code: CatalogErrorCode = "embedding_failure"


class CatalogOperationError(CatalogError):
    """Raised when a catalog resource or native operation fails."""

    default_code: CatalogErrorCode = "operation_failed"


class CatalogResponseTooLargeError(CatalogError):
    """Raised when a bounded transport result exceeds its byte budget."""

    default_code: CatalogErrorCode = "response_too_large"


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


def format_error(message: str, hints: Sequence[str]) -> str:
    """Render an error message and recovery hints for terminal transports."""

    if not hints:
        return message
    guidance = "\n".join(f"  - {hint}" for hint in hints)
    return f"{message}\n\nGuidance:\n{guidance}"


__all__ = [
    "CatalogCapabilityError",
    "CatalogEmbeddingError",
    "CatalogError",
    "CatalogErrorCode",
    "CatalogIntegrityError",
    "CatalogLookupError",
    "CatalogOperationError",
    "CatalogProfileError",
    "CatalogResponseTooLargeError",
    "CatalogValidationError",
    "format_error",
    "require_string_sequence",
]
