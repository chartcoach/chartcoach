from __future__ import annotations

import json
import os
import shutil
import tempfile
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import platformdirs

from .catalog import (
    CATALOG_DF_RELATION,
    EMBEDDINGS_TABLE,
    GUIDELINE_LABELS_RELATION,
    GUIDELINE_REFERENCES_RELATION,
    REFERENCES_RELATION,
    SECTIONS_RELATION,
    Catalog,
    CatalogIndex,
)
from .catalog.clients import create_chroma_client, create_duckdb_conn
from .tools import CatalogIndexTools

REQUIRED_DUCKDB_RELATIONS = frozenset(
    {
        CATALOG_DF_RELATION,
        EMBEDDINGS_TABLE,
        GUIDELINE_LABELS_RELATION,
        GUIDELINE_REFERENCES_RELATION,
        REFERENCES_RELATION,
        SECTIONS_RELATION,
    }
)


def _default_cache_dir() -> Path:
    return Path(platformdirs.user_cache_dir("chartcoach"))


@dataclass(frozen=True)
class ChartCoachConfig:
    cache_dir: Path = field(default_factory=_default_cache_dir)
    collection_name: str = "catalog"
    catalog_uri: str | None = None
    catalog_filename: str = "catalog.parquet"
    manifest_filename: str = "manifest.json"
    chroma_dirname: str = "chroma_db"
    duckdb_filename: str = "duckdb_catalog.db"

    @classmethod
    def from_env(cls) -> "ChartCoachConfig":
        raw_cache_dir = os.getenv("CHARTCOACH_CACHE_DIR")
        cache_dir = Path(raw_cache_dir) if raw_cache_dir else _default_cache_dir()
        collection_name = os.getenv("CHARTCOACH_COLLECTION_NAME", "catalog")
        catalog_uri = os.getenv("CHARTCOACH_CATALOG_PATH")
        return cls(
            cache_dir=cache_dir,
            collection_name=collection_name,
            catalog_uri=catalog_uri,
        )

    def require_catalog_uri(self) -> str:
        if self.catalog_uri is None:
            raise ValueError(
                "CHARTCOACH_CATALOG_PATH must be set before starting the ChartCoach MCP server."
            )
        return self.catalog_uri

    @property
    def catalog_cache_path(self) -> Path:
        return self.cache_dir / self.catalog_filename

    @property
    def manifest_path(self) -> Path:
        return self.cache_dir / self.manifest_filename

    @property
    def chroma_cache_path(self) -> Path:
        return self.cache_dir / self.chroma_dirname

    @property
    def duckdb_path(self) -> Path:
        return self.cache_dir / self.duckdb_filename


class ChartCoach:
    """Catalog-backed façade for bootstrap, cache, indexing, and tools."""

    def __init__(
        self,
        catalog: Catalog,
        *,
        config: ChartCoachConfig | None = None,
    ) -> None:
        self.catalog = catalog
        self.config = config or ChartCoachConfig()
        self._index: CatalogIndex | None = None

    @classmethod
    def from_uri(
        cls,
        catalog_uri: str | Path,
        *,
        config: ChartCoachConfig | None = None,
    ) -> "ChartCoach":
        return cls(Catalog.from_uri(catalog_uri), config=config)

    @classmethod
    def from_cache(
        cls,
        *,
        config: ChartCoachConfig | None = None,
    ) -> "ChartCoach":
        resolved_config = config or ChartCoachConfig()
        manifest = _load_manifest(resolved_config.manifest_path)
        if manifest is None:
            raise FileNotFoundError(
                f"ChartCoach cache manifest not found at {resolved_config.manifest_path}."
            )
        if not resolved_config.catalog_cache_path.exists():
            raise FileNotFoundError(
                f"Cached catalog parquet not found at {resolved_config.catalog_cache_path}."
            )
        if not _has_required_duckdb_relations(resolved_config.duckdb_path):
            raise ValueError(
                "Cached DuckDB file does not expose the required ChartCoach relations."
            )

        expected_collection = str(
            manifest.get("collection_name", resolved_config.collection_name)
        )
        if expected_collection != resolved_config.collection_name:
            raise ValueError(
                "Configured collection_name does not match the cached manifest."
            )

        return cls(
            Catalog.from_uri(resolved_config.catalog_cache_path), config=resolved_config
        )

    @classmethod
    def cache_status(
        cls,
        *,
        config: ChartCoachConfig | None = None,
    ) -> dict[str, Any]:
        resolved_config = config or ChartCoachConfig()
        manifest = _load_manifest(resolved_config.manifest_path)
        duckdb_ready = _has_required_duckdb_relations(resolved_config.duckdb_path)

        return {
            "cache_dir": str(resolved_config.cache_dir),
            "collection_name": resolved_config.collection_name,
            "catalog_uri": resolved_config.catalog_uri,
            "ready": (
                manifest is not None
                and resolved_config.manifest_path.exists()
                and resolved_config.catalog_cache_path.exists()
                and resolved_config.chroma_cache_path.exists()
                and resolved_config.duckdb_path.exists()
                and duckdb_ready
            ),
            "artifacts": {
                "manifest": str(resolved_config.manifest_path),
                "catalog": str(resolved_config.catalog_cache_path),
                "chroma": str(resolved_config.chroma_cache_path),
                "duckdb": str(resolved_config.duckdb_path),
            },
            "exists": {
                "manifest": resolved_config.manifest_path.exists(),
                "catalog": resolved_config.catalog_cache_path.exists(),
                "chroma": resolved_config.chroma_cache_path.exists(),
                "duckdb": resolved_config.duckdb_path.exists(),
            },
            "manifest": manifest,
        }

    @classmethod
    def init_cache(
        cls,
        catalog_uri: str | Path,
        *,
        config: ChartCoachConfig | None = None,
    ) -> dict[str, Any]:
        resolved_config = config or ChartCoachConfig()
        catalog = Catalog.from_uri(catalog_uri)
        return cls._write_cache_atomically(
            catalog=catalog,
            catalog_uri=str(catalog_uri),
            config=resolved_config,
            catalog_digest=catalog.hexdigest(),
        )

    @classmethod
    def ensure_cache(
        cls,
        *,
        config: ChartCoachConfig | None = None,
    ) -> dict[str, Any]:
        resolved_config = config or ChartCoachConfig()
        catalog_uri = resolved_config.require_catalog_uri()
        catalog = Catalog.from_uri(catalog_uri)
        catalog_digest = catalog.hexdigest()
        if _cache_matches(
            config=resolved_config,
            manifest=_load_manifest(resolved_config.manifest_path),
            catalog_digest=catalog_digest,
        ):
            return cls.cache_status(config=resolved_config)

        return cls._write_cache_atomically(
            catalog=catalog,
            catalog_uri=catalog_uri,
            config=resolved_config,
            catalog_digest=catalog_digest,
        )

    @classmethod
    def _write_cache_atomically(
        cls,
        *,
        catalog: Catalog,
        catalog_uri: str,
        config: ChartCoachConfig,
        catalog_digest: str,
    ) -> dict[str, Any]:
        config.cache_dir.parent.mkdir(parents=True, exist_ok=True)
        staged_dir = Path(
            tempfile.mkdtemp(
                prefix=f"{config.cache_dir.name}-build-",
                dir=str(config.cache_dir.parent),
            )
        )
        staged_config = replace(config, cache_dir=staged_dir)
        staged_coach = cls(catalog, config=staged_config)

        try:
            staged_config.cache_dir.mkdir(parents=True, exist_ok=True)
            staged_coach.catalog.df.write_parquet(staged_config.catalog_cache_path)
            staged_coach.build_index()
            manifest = {
                "catalog_uri": catalog_uri,
                "built_at": datetime.now(timezone.utc).isoformat(),
                "collection_name": staged_config.collection_name,
                "catalog_digest": catalog_digest,
                "entry_count": len(staged_coach.catalog),
            }
            staged_config.manifest_path.write_text(
                json.dumps(manifest, indent=2, sort_keys=True)
            )
            if staged_coach._index is not None:
                staged_coach._index.conn.close()
            _swap_cache_dirs(staged_dir=staged_dir, target_dir=config.cache_dir)
        except Exception:
            shutil.rmtree(staged_dir, ignore_errors=True)
            raise

        return cls.cache_status(config=config)

    def build_index(self) -> CatalogIndex:
        self.config.cache_dir.mkdir(parents=True, exist_ok=True)
        self.config.chroma_cache_path.mkdir(parents=True, exist_ok=True)
        collection = create_chroma_client(
            self.config.chroma_cache_path
        ).get_or_create_collection(self.config.collection_name)
        conn = create_duckdb_conn(self.config.duckdb_path)
        self._index = CatalogIndex(self.catalog, collection=collection, conn=conn)
        self._index.build()
        return self._index

    def load_index(self) -> CatalogIndex:
        if self._index is not None:
            return self._index

        if not self.config.catalog_cache_path.exists():
            raise FileNotFoundError(
                f"Cached catalog parquet not found at {self.config.catalog_cache_path}."
            )
        if not self.config.chroma_cache_path.exists():
            raise FileNotFoundError(
                f"Cached Chroma directory not found at {self.config.chroma_cache_path}."
            )
        if not self.config.duckdb_path.exists():
            raise FileNotFoundError(
                f"Cached DuckDB file not found at {self.config.duckdb_path}."
            )

        collection = create_chroma_client(
            self.config.chroma_cache_path
        ).get_or_create_collection(self.config.collection_name)
        conn = create_duckdb_conn(self.config.duckdb_path, read_only=True)
        self._index = CatalogIndex(self.catalog, collection=collection, conn=conn)
        return self._index

    def tools(self, *, auto_build: bool = True) -> CatalogIndexTools:
        if self._index is None:
            if auto_build and not self.cache_status(config=self.config)["ready"]:
                self.build_index()
            else:
                self.load_index()
        index = self._index
        if index is None:
            raise RuntimeError("ChartCoach failed to resolve a CatalogIndex.")
        return CatalogIndexTools(index, auto_build=False)


def _load_manifest(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def _cache_matches(
    *,
    config: ChartCoachConfig,
    manifest: dict[str, Any] | None,
    catalog_digest: str,
) -> bool:
    if manifest is None:
        return False

    return (
        config.manifest_path.exists()
        and config.catalog_cache_path.exists()
        and config.chroma_cache_path.exists()
        and config.duckdb_path.exists()
        and _has_required_duckdb_relations(config.duckdb_path)
        and manifest.get("collection_name") == config.collection_name
        and manifest.get("catalog_uri") == config.catalog_uri
        and manifest.get("catalog_digest") == catalog_digest
    )


def _has_required_duckdb_relations(path: Path) -> bool:
    if not path.exists():
        return False

    conn = None
    try:
        conn = create_duckdb_conn(path, read_only=True)
        relation_rows = conn.execute("show all tables").fetchall()
    except Exception:
        return False
    finally:
        if conn is not None:
            conn.close()

    relation_names = {str(row[2]) for row in relation_rows}
    return REQUIRED_DUCKDB_RELATIONS.issubset(relation_names)


def _swap_cache_dirs(*, staged_dir: Path, target_dir: Path) -> None:
    backup_dir = target_dir.with_name(f"{target_dir.name}.backup")
    shutil.rmtree(backup_dir, ignore_errors=True)

    try:
        if target_dir.exists():
            target_dir.rename(backup_dir)
        staged_dir.rename(target_dir)
    except Exception:
        if target_dir.exists():
            shutil.rmtree(target_dir, ignore_errors=True)
        if backup_dir.exists():
            backup_dir.rename(target_dir)
        raise
    finally:
        shutil.rmtree(backup_dir, ignore_errors=True)


__all__ = [
    "ChartCoach",
    "ChartCoachConfig",
]
