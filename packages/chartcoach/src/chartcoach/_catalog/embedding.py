from __future__ import annotations

import json
from pathlib import Path

from .errors import CatalogCapabilityError, CatalogValidationError

_MAX_VARIABLE_FILE_BYTES = 65_536


def apply_embedding_variables(path: Path | str) -> None:
    """Load caller-owned LanceDB registry variables from a JSON file."""

    variables = _read_embedding_variables(Path(path))
    try:
        from lancedb.embeddings import get_registry
    except ModuleNotFoundError as exc:
        raise CatalogCapabilityError(
            "Embedding variables require chartcoach[index].",
            hints=["Install chartcoach[index]."],
        ) from exc
    registry = get_registry()
    for name, value in variables.items():
        registry.set_var(name, value)


def _read_embedding_variables(path: Path) -> dict[str, str]:
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
        if len(data) > _MAX_VARIABLE_FILE_BYTES:
            raise CatalogValidationError(
                "Embedding variable file exceeds the 64 KiB limit."
            )
        value = json.loads(data.decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CatalogValidationError(
            "Embedding variable file must be a UTF-8 JSON object."
        ) from exc
    if not isinstance(value, dict) or not all(
        isinstance(name, str) and name and ":" not in name and isinstance(item, str)
        for name, item in value.items()
    ):
        raise CatalogValidationError(
            "Embedding variable file must map names to string values."
        )
    return value


__all__ = ["apply_embedding_variables"]
