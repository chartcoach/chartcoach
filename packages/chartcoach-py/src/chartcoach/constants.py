from __future__ import annotations

CACHE_APP_NAME = "chartcoach"
DEFAULT_CATALOG_URI = (
    "https://files.peter.gy/projects/chartcoach/artifacts/catalog.parquet"
)
DEFAULT_CHROMA_DIRNAME = "chroma_db"
DEFAULT_DUCKDB_FILENAME = "duckdb_catalog.db"
DEFAULT_DUCKDB_ROW_LIMIT = 200
DEFAULT_CHROMA_TOP_K = 10

__all__ = [
    "CACHE_APP_NAME",
    "DEFAULT_CATALOG_URI",
    "DEFAULT_CHROMA_DIRNAME",
    "DEFAULT_CHROMA_TOP_K",
    "DEFAULT_DUCKDB_FILENAME",
    "DEFAULT_DUCKDB_ROW_LIMIT",
]
