from __future__ import annotations

import json
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import TYPE_CHECKING

from .errors import CatalogCapabilityError, CatalogValidationError

if TYPE_CHECKING:
    from .profiles import EmbeddingBinding

_MAX_VARIABLE_FILE_BYTES = 65_536
_API_KEY = "CHARTCOACH_EMBEDDING_API_KEY"
# Binding fields that carry a provider credential.
_CREDENTIAL_FIELDS = frozenset({"api_key"})


def embedding_environment(environment: Mapping[str, str]) -> dict[str, str]:
    """Snapshot provider variables, respecting the dedicated key selector."""
    values = dict(environment)
    name = environment.get("CHARTCOACH_EMBEDDING_API_KEY_ENV")
    if name:
        values.pop(_API_KEY, None)
        if environment.get(name):
            values[_API_KEY] = environment[name]
    return values


def profile_variables(
    bindings: Iterable[EmbeddingBinding], environment: Mapping[str, str]
) -> dict[str, str]:
    """Resolve the `$var:` names that a profile's bindings declare.

    Each name reads the environment variable of the same name. A credential
    field whose name is unset reads CHARTCOACH_EMBEDDING_API_KEY instead, so a
    deployment sets one documented key whatever name the release chose.
    """
    values = embedding_environment(environment)
    resolved: dict[str, str] = {}
    for binding in bindings:
        for field, value in binding.model.items():
            if not (isinstance(value, str) and value.startswith("$var:")):
                continue
            name = value.removeprefix("$var:")
            if values.get(name):
                resolved[name] = values[name]
            elif field in _CREDENTIAL_FIELDS and values.get(_API_KEY):
                resolved[name] = values[_API_KEY]
    return resolved


def apply_embedding_variables(path: Path | str) -> None:
    """Set caller-owned LanceDB registry variables, without selecting a model."""

    apply_variables(read_embedding_variables(path))


def apply_variables(values: Mapping[str, str]) -> None:
    """Set LanceDB registry variables for this process."""

    if not values:
        return
    try:
        from lancedb.embeddings import get_registry
    except ModuleNotFoundError as exc:
        raise CatalogCapabilityError(
            "Embedding variables require chartcoach[index].",
            hints=["Install chartcoach[index]."],
        ) from exc
    registry = get_registry()
    for name, value in values.items():
        registry.set_var(name, value)


def read_embedding_variables(path: Path | str) -> dict[str, str]:
    """Read a bounded variable file without importing LanceDB."""
    path = Path(path)
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise CatalogValidationError(
            "Embedding variable file could not be read.",
            details={"path": str(path)},
        ) from exc
    if size > _MAX_VARIABLE_FILE_BYTES:
        raise CatalogValidationError(
            "Embedding variable file exceeds the 64 KiB limit."
        )
    try:
        with path.open("rb") as source:
            data = source.read(_MAX_VARIABLE_FILE_BYTES + 1)
    except OSError as exc:
        raise CatalogValidationError(
            "Embedding variable file must be a UTF-8 JSON object."
        ) from exc
    if len(data) > _MAX_VARIABLE_FILE_BYTES:
        raise CatalogValidationError(
            "Embedding variable file exceeds the 64 KiB limit."
        )
    try:
        value = json.loads(data.decode("utf-8"))
    except (ValueError, RecursionError) as exc:
        raise CatalogValidationError(
            "Embedding variable file must be a UTF-8 JSON object."
        ) from exc
    _validate_variables(value)
    return value


def _validate_variables(value: object) -> None:
    if not isinstance(value, dict) or not all(
        isinstance(name, str) and name and ":" not in name and isinstance(item, str)
        for name, item in value.items()
    ):
        raise CatalogValidationError(
            "Embedding variable file must map names to string values."
        )


__all__ = [
    "apply_embedding_variables",
    "apply_variables",
    "profile_variables",
    "read_embedding_variables",
]
