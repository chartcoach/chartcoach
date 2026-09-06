from __future__ import annotations

from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING

from ...constants import LANCE_DOCUMENT_TABLE
from ..documents import document_rows
from ..model import Catalog
from ..profiles import embedding_bindings_from_bytes, validate_embedding_model
from .dependencies import CURATION_EXTRA, missing_curation_dependency

if TYPE_CHECKING:
    from lancedb import DBConnection, Table
    from lancedb.embeddings import EmbeddingFunction, EmbeddingFunctionConfig


def build_lancedb_index(
    catalog: Catalog,
    uri: str | PathLike[str],
    *,
    embedding: EmbeddingFunction,
) -> Table:
    """Build the fixed ChartCoach document table with a LanceDB embedding."""

    embedding = _validated_embedding(embedding)
    frame = document_rows(catalog).with_row_index("row_id")
    rows = frame.to_arrow()
    table = _connect(uri).create_table(
        LANCE_DOCUMENT_TABLE,
        data=rows.to_reader(max_chunksize=128),
        mode="overwrite",
        embedding_functions=[_embedding_config(embedding)],
    )
    if frame.height:
        from lancedb.index import FTS

        table.create_index("text", config=FTS())
    return table


def _embedding_config(embedding: EmbeddingFunction) -> EmbeddingFunctionConfig:
    try:
        from lancedb.embeddings import EmbeddingFunctionConfig
    except ModuleNotFoundError as exc:
        raise missing_curation_dependency(exc.name) from exc
    return EmbeddingFunctionConfig(
        source_column="text",
        vector_column="vector",
        function=embedding,
    )


def _validated_embedding(embedding: EmbeddingFunction) -> EmbeddingFunction:
    from lancedb.embeddings import get_registry

    registry = get_registry()
    metadata = registry.get_table_metadata([_embedding_config(embedding)])
    if metadata is None:
        raise ValueError("LanceDB did not serialize the embedding function.")
    raw = metadata["embedding_functions"]
    bindings = embedding_bindings_from_bytes(raw)
    if len(bindings) != 1:
        raise ValueError("LanceDB must serialize exactly one embedding binding.")
    binding = bindings[0]
    definition = registry.get(binding.name)
    validate_embedding_model(
        binding.model,
        allowed_fields=frozenset(definition.model_fields),
        sensitive_fields=frozenset(definition.sensitive_keys()),
    )
    return registry.parse_functions({b"embedding_functions": raw})["vector"].function


def _connect(uri: str | PathLike[str]) -> DBConnection:
    try:
        import lancedb
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            f"LanceDB index production requires optional `{CURATION_EXTRA}` dependencies.",
            name=exc.name,
        ) from exc
    return lancedb.connect(Path(uri) if isinstance(uri, PathLike) else uri)


__all__ = ["build_lancedb_index"]
