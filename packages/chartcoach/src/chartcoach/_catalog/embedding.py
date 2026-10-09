from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path

from .errors import CatalogCapabilityError, CatalogValidationError

_MAX_VARIABLE_FILE_BYTES = 65_536


def embedding_environment(environment: Mapping[str, str]) -> dict[str, str]:
    """Snapshot provider variables, respecting the dedicated key selector."""
    values = dict(environment)
    name = environment.get("CHARTCOACH_EMBEDDING_API_KEY_ENV")
    if name:
        values.pop("CHARTCOACH_EMBEDDING_API_KEY", None)
        if environment.get(name):
            values["CHARTCOACH_EMBEDDING_API_KEY"] = environment[name]
    return values


def apply_embedding_variables(path: Path | str) -> None:
    """Set caller-owned LanceDB registry variables, without selecting a model."""

    values = read_embedding_variables(path)
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


__all__ = ["apply_embedding_variables", "read_embedding_variables"]
