from __future__ import annotations

import logging
from functools import cached_property
from typing import Mapping, Sequence, cast

import chromadb
import duckdb
import polars as pl
from chromadb.api.types import Metadata
from tqdm import tqdm

from .collection import Catalog

EMBEDDING_COL = "embedding"
EMBEDDINGS_TABLE = "embeddings"
CATALOG_DF_RELATION = "catalog_df"
EMBEDDINGS_DF_RELATION = "embeddings_df"
logger = logging.getLogger(__name__)


def _collection_payload(
    catalog: Catalog,
) -> tuple[list[str], list[str], list[Metadata]]:
    docs_df = catalog.docs_df
    ids = docs_df.get_column("id").to_list()
    documents = docs_df.get_column("doc").to_list()
    metadatas = cast(list[Metadata], docs_df.get_column("metadata").to_list())
    return ids, documents, metadatas


def _batch_add_documents(
    collection: chromadb.Collection,
    ids: list[str],
    documents: list[str],
    metadatas: list[Metadata],
    *,
    batch_size: int,
) -> None:
    logger.debug(
        "Adding %s documents to Chroma collection in batches of %s",
        len(ids),
        batch_size,
    )
    for i in tqdm(
        range(0, len(ids), batch_size),
        desc=f"Indexing catalog into ChromaDB in batches of {batch_size}",
    ):
        collection.add(
            ids=ids[i : i + batch_size],
            documents=documents[i : i + batch_size],
            metadatas=metadatas[i : i + batch_size],
        )


def _embedding_dimensions(embeddings_df: pl.DataFrame) -> int:
    dtype = embeddings_df.limit(1)[EMBEDDING_COL].dtype
    shape = getattr(dtype, "shape", None)
    if shape is not None:
        return shape[0]

    first_embedding = embeddings_df.get_column(EMBEDDING_COL).to_list()[0]
    return len(first_embedding)


def _duckdb_setup_sql(ndims: int) -> str:
    return f"""
    INSTALL vss; LOAD vss; SET hnsw_enable_experimental_persistence = true;

    CREATE OR REPLACE TABLE "{EMBEDDINGS_TABLE}" as (
        SELECT id AS slug,
               parent_id AS id,
               doc,
               role,
               "{EMBEDDING_COL}"::FLOAT[{ndims}] AS "{EMBEDDING_COL}"
        FROM {EMBEDDINGS_DF_RELATION}
    );

    DROP INDEX IF EXISTS idx;
    CREATE INDEX idx ON "{EMBEDDINGS_TABLE}" USING HNSW ("{EMBEDDING_COL}");
    """


def _embeddings_response_to_frame(
    res: Mapping[str, Sequence[object]],
) -> pl.DataFrame:
    return pl.from_dict(
        cast(
            Mapping[str, Sequence[object]],
            {
                "id": res["ids"],
                "doc": res["documents"],
                "embedding": res["embeddings"],
                "metadata": res["metadatas"],
            },
        )
    ).unnest("metadata")


class CatalogIndex:
    def __init__(
        self,
        catalog: Catalog,
        collection: chromadb.Collection,
        conn: duckdb.DuckDBPyConnection,
    ):
        self._catalog = catalog
        self._collection = collection
        self._conn = conn
        logger.debug(
            "Initialized CatalogIndex with %s catalog entries",
            len(self._catalog),
        )

    def build(self):
        logger.debug("Building catalog index for %s entries", len(self.catalog))
        self._init_collection()
        self._init_duckdb_conn()

    @property
    def catalog(self) -> Catalog:
        return self._catalog

    @property
    def collection(self) -> chromadb.Collection:
        return self._collection

    @property
    def conn(self) -> duckdb.DuckDBPyConnection:
        return self._conn

    def _init_collection(self, batch_size: int = 768) -> None:
        existing_count = self.collection.count()
        target_count = self.catalog.docs_df.height

        if existing_count == target_count:
            logger.debug(
                "Skipping Chroma indexing; collection already has %s documents",
                existing_count,
            )
            return

        logger.debug(
            "Preparing Chroma indexing: existing=%s target=%s batch_size=%s",
            existing_count,
            target_count,
            batch_size,
        )
        ids, documents, metadatas = _collection_payload(self.catalog)
        _batch_add_documents(
            self.collection,
            ids,
            documents,
            metadatas,
            batch_size=batch_size,
        )

    def _init_duckdb_conn(self) -> None:
        embeddings_df = self.embeddings_df
        ndims = _embedding_dimensions(embeddings_df)
        logger.debug(
            "Registering %s embeddings with DuckDB using %s dimensions",
            embeddings_df.height,
            ndims,
        )
        self.conn.register(EMBEDDINGS_DF_RELATION, embeddings_df)
        self.conn.execute(_duckdb_setup_sql(ndims))
        self.conn.unregister(EMBEDDINGS_DF_RELATION)
        self.conn.register(CATALOG_DF_RELATION, self.catalog_df)
        logger.debug(
            "Registered %s in DuckDB with %s rows",
            CATALOG_DF_RELATION,
            self.catalog_df.height,
        )

    @cached_property
    def catalog_df(self) -> pl.DataFrame:
        return self.catalog.df.drop("id").unnest("guideline").drop("bibliography")

    @cached_property
    def embeddings_df(self) -> pl.DataFrame:
        res = self._collection.get(include=["documents", "embeddings", "metadatas"])
        return _embeddings_response_to_frame(cast(Mapping[str, Sequence[object]], res))

    def embedding_atlas(self):
        from embedding_atlas.projection import compute_vector_projection
        from embedding_atlas.widget import EmbeddingAtlasWidget

        df = self.embeddings_df.to_pandas()
        compute_vector_projection(df, vector="embedding")
        return EmbeddingAtlasWidget(
            df,
            x="projection_x",
            y="projection_y",
            neighbors="neighbors",
        )


__all__ = [
    "CATALOG_DF_RELATION",
    "CatalogIndex",
    "EMBEDDING_COL",
    "EMBEDDINGS_DF_RELATION",
    "EMBEDDINGS_TABLE",
]
