import pathlib
import shutil
from functools import cached_property
from typing import Mapping, Sequence, cast

import chromadb
import duckdb
import platformdirs
import polars as pl
from tqdm import tqdm

from .catalog import Catalog

APP_CACHEDIR = pathlib.Path(platformdirs.user_cache_dir("chartcoach"))
APP_CACHEDIR.mkdir(parents=True, exist_ok=True)


def create_default_chroma_client(*, recreate: bool = False) -> chromadb.ClientAPI:
    path = APP_CACHEDIR / "chroma_db"
    if recreate:
        shutil.rmtree(path, ignore_errors=True)
    return chromadb.PersistentClient(path)


def create_default_duckdb_conn(*, recreate: bool = False) -> duckdb.DuckDBPyConnection:
    path = APP_CACHEDIR / "duckdb_catalog.db"
    if recreate:
        path.unlink(missing_ok=True)
    return duckdb.connect(path)


def destroy_cache():
    shutil.rmtree(APP_CACHEDIR, ignore_errors=True)


class CatalogIndex:
    def __init__(
        self,
        catalog: Catalog,
        collection: chromadb.Collection | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ):
        self._catalog = catalog
        self._collection = (
            collection
            or create_default_chroma_client().get_or_create_collection("catalog")
        )
        self._conn = conn or create_default_duckdb_conn()

    def build(self):
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
        if self.collection.count() == self.catalog.docs_df.height:
            return

        ids = self.catalog.docs_df.get_column("id").to_list()
        documents = self.catalog.docs_df.get_column("doc").to_list()
        metadatas = self.catalog.docs_df.get_column("metadata").to_list()

        for i in tqdm(
            range(0, len(ids), batch_size),
            desc=f"Indexing catalog into ChromaDB in batches of {batch_size}",
        ):
            self.collection.add(
                ids=ids[i : i + batch_size],
                documents=documents[i : i + batch_size],
                metadatas=metadatas[i : i + batch_size],
            )

    def _init_duckdb_conn(self) -> None:
        EMBEDDING_COL = "embedding"
        EMBEDDINGS_TABLE = "embeddings"

        embeddings_df = self.embeddings_df
        ndims: int = embeddings_df.limit(1)[EMBEDDING_COL].dtype.shape[0]  # type: ignore
        self.conn.register("embeddings_df", embeddings_df)
        self.conn.execute(f"""
        -- Enable HNSW extension and create a table for guideline documents with embeddings
        INSTALL vss; LOAD vss; SET hnsw_enable_experimental_persistence = true;
        
        -- Create a table for guideline documents with embeddings and index on it for performant search
        CREATE OR REPLACE TABLE "{EMBEDDINGS_TABLE}" as (
            SELECT id AS slug,
                   parent_id AS id,
                   doc,
                   role,
                   "{EMBEDDING_COL}"::FLOAT[{ndims}] AS "{EMBEDDING_COL}"
            FROM embeddings_df
        );
        
        -- (Re)create Hierarchical Navigable Small World (HNSW) index on the embeddings for efficient similarity search
        DROP INDEX IF EXISTS idx;
        CREATE INDEX idx ON "{EMBEDDINGS_TABLE}" USING HNSW ("{EMBEDDING_COL}");
        """)
        self.conn.unregister("embeddings_df")

        # Register catalog for direct queries / joins to access references, full body, etc.
        self.conn.register("catalog_df", self.catalog_df)

    @cached_property
    def catalog_df(self) -> pl.DataFrame:
        return self.catalog.df.drop("id").unnest("guideline").drop("bibliography")

    @cached_property
    def embeddings_df(self) -> pl.DataFrame:
        res = self._collection.get(include=["documents", "embeddings", "metadatas"])
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
