from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Iterable, Mapping, Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Literal

import polars as pl

from ..constants import DEFAULT_GUIDELINE_URL_TEMPLATE
from .errors import CatalogCapabilityError, CatalogValidationError
from .guidelines import Guideline

if TYPE_CHECKING:
    import duckdb as duckdb_module
    from lancedb import Table

    from ..duckdb import DuckDBConfigValue
    from .description import CatalogInfo
    from .manifest import CatalogManifest
    from .profiles import ProfileMetadata
    from .read import GuidelineEntryRecord, SourceDetail
    from .references import CitationRecord, ReferenceTables
    from .releases import CatalogRelease
    from .search import SearchResult
    from .sql import SqlResult


class Catalog:
    """A Guideline Catalog with entries, a manifest, and query operations."""

    def __init__(
        self,
        frame: pl.DataFrame,
        *,
        manifest: CatalogManifest,
    ) -> None:
        self._frame = _normalize_catalog_frame(frame)
        self._manifest = manifest
        self._release: CatalogRelease | None = None
        self._resolved_location: str | None = None
        self._profile_names: tuple[str, ...] = ()
        self._profile_loader: Callable[[str], ProfileMetadata] | None = None
        self._index_loader: Callable[[str, Path | None, bool], Table] | None = None
        self._reference_tables_cache: ReferenceTables | None = None
        _validate_unique_ids(self._frame)

        from .manifest import validate_catalog_manifest

        validate_catalog_manifest(self, manifest)

    @classmethod
    def _from_runtime(
        cls,
        catalog: Catalog,
        *,
        release: CatalogRelease | None,
        resolved_location: str | None,
        profile_names: Sequence[str] = (),
        profile_loader: Callable[[str], ProfileMetadata] | None = None,
        index_loader: Callable[[str, Path | None, bool], Table] | None = None,
    ) -> Catalog:
        if not isinstance(catalog, cls):
            raise TypeError("Runtime catalog must be a Catalog instance.")
        catalog._release = release
        catalog._resolved_location = resolved_location
        catalog._profile_names = tuple(profile_names)
        catalog._profile_loader = profile_loader
        catalog._index_loader = index_loader
        return catalog

    @classmethod
    def from_guidelines(
        cls,
        guidelines: Iterable[Guideline],
        *,
        manifest: CatalogManifest,
    ) -> Catalog:
        """Build an in-memory catalog from compiled guidelines and a manifest."""

        from .tables import build_catalog_df

        return cls(build_catalog_df(tuple(guidelines)), manifest=manifest)

    @property
    def manifest(self) -> CatalogManifest:
        """Return the immutable catalog vocabulary manifest."""

        return self._manifest

    @property
    def release(self) -> CatalogRelease | None:
        """Return the verified release descriptor attached by the runtime."""

        return self._release

    def to_frame(self) -> pl.DataFrame:
        """Return an isolated frame containing the six stored columns."""

        return self._frame.clone()

    def table(self, name: str) -> pl.DataFrame:
        """Return an isolated catalog table by name."""

        from .relations import catalog_table

        return catalog_table(self, name)

    def query(
        self,
        *,
        ids: Sequence[str] = (),
        labels: Sequence[str] = (),
        label_prefixes: Sequence[str] = (),
        contains: str | None = None,
        limit: int = 50,
    ) -> pl.DataFrame:
        """Return compact guideline entry candidates matching filters and text."""

        from .query import query_entries

        return query_entries(
            self,
            ids=ids,
            labels=labels,
            label_prefixes=label_prefixes,
            contains=contains,
            limit=limit,
            include_body=False,
        )

    def read(
        self,
        *,
        ids: Sequence[str],
        roles: Sequence[str] = (),
        source_detail: SourceDetail = "minimal",
    ) -> list[GuidelineEntryRecord]:
        """Return complete guideline entry records for exact guideline entry IDs."""

        from .read import retrieve_entry_records

        return retrieve_entry_records(
            self,
            ids=ids,
            roles=roles,
            source_detail=source_detail,
        )

    def cite(
        self,
        *,
        ids: Sequence[str],
        url_template: str = DEFAULT_GUIDELINE_URL_TEMPLATE,
    ) -> list[CitationRecord]:
        """Return guideline links and source citations for exact guideline entry IDs."""

        from .references import citation_records

        return citation_records(self, ids=ids, url_template=url_template)

    def describe(self, *, profile: str | None = None) -> CatalogInfo:
        """Return catalog identity, tables, vocabulary, and profile information."""

        from .description import describe_catalog

        return describe_catalog(self, profile=profile)

    def duckdb(
        self,
        *,
        config: Mapping[str, DuckDBConfigValue] | None = None,
    ) -> duckdb_module.DuckDBPyConnection:
        """Return a fresh caller-owned DuckDB connection over catalog tables."""

        from ..duckdb import connect_catalog

        return connect_catalog(self, config=config)

    def sql(self, statement: str, *, limit: int = 100) -> SqlResult:
        """Run one bounded read-only SELECT over the catalog tables."""

        from .sql import catalog_sql

        return catalog_sql(self, statement, limit=limit)

    def index(self, profile: str, *, directory: Path | None = None) -> Table:
        """Return the selected profile's index as a LanceDB table."""

        if self._index_loader is None:
            raise CatalogCapabilityError(
                "This catalog has no release-backed index loader.",
                hints=["Open a catalog release that publishes an index profile."],
            )
        return self._index_loader(profile, directory, True)

    def search(
        self,
        text: str,
        *,
        profile: str,
        mode: Literal["fts", "vector", "hybrid"] = "fts",
        limit: int = 10,
        where: str | None = None,
    ) -> SearchResult:
        """Return bounded guideline matches from one index profile."""

        from .search import catalog_search

        return catalog_search(
            self,
            text,
            profile=profile,
            mode=mode,
            limit=limit,
            where=where,
        )

    def entries_digest(self) -> str:
        """Return a stable digest of the canonical guideline entry records."""

        return _dataframe_digest(self._frame)

    def __len__(self) -> int:
        return self._frame.height

    def _profile_metadata(self, profile: str) -> ProfileMetadata:
        if self._profile_loader is None:
            raise CatalogCapabilityError(
                "This catalog has no release-backed profile metadata.",
                hints=["Open a catalog release that publishes an index profile."],
            )
        return self._profile_loader(profile)

    def _search_table(self, profile: str) -> Table:
        if self._index_loader is None:
            raise CatalogCapabilityError(
                "This catalog has no release-backed index loader.",
                hints=["Open a catalog release that publishes an index profile."],
            )
        return self._index_loader(profile, None, False)

    def _reference_tables(self) -> ReferenceTables:
        from .references import build_reference_tables

        if self._reference_tables_cache is None:
            self._reference_tables_cache = build_reference_tables(self._frame)
        return self._reference_tables_cache


def _normalize_catalog_frame(frame: pl.DataFrame) -> pl.DataFrame:
    from .schemas import CATALOG_SCHEMA
    from .tables import build_catalog_df

    expected = list(CATALOG_SCHEMA)
    actual = set(frame.columns)
    if actual != set(expected):
        raise CatalogValidationError(
            "Catalog dataframe columns must be: " + ", ".join(expected) + "."
        )

    guidelines: list[Guideline] = []
    for row_number, row in enumerate(
        frame.select(expected).iter_rows(named=True), start=1
    ):
        try:
            guidelines.append(Guideline.from_mapping(row))
        except (TypeError, ValueError) as exc:
            raise CatalogValidationError(
                f"Catalog row {row_number} (id={row.get('id')!r}) is invalid: {exc}"
            ) from exc
    return build_catalog_df(guidelines)


def _read_catalog_parquet(path: Path) -> pl.DataFrame:
    from .schemas import CATALOG_SCHEMA

    frame = pl.read_parquet(path)
    canonical = _normalize_catalog_frame(frame)
    try:
        serialized = frame.select(CATALOG_SCHEMA.names()).cast(CATALOG_SCHEMA)
    except (TypeError, ValueError) as exc:
        raise CatalogValidationError(
            f"Catalog parquet schema is invalid: {exc}"
        ) from exc
    if not serialized.equals(canonical):
        raise CatalogValidationError("Catalog parquet rows must use canonical values.")
    return canonical


def _load_catalog_bundle(manifest_path: Path, entries_path: Path) -> Catalog:
    from .manifest import CatalogManifest

    return Catalog(
        _read_catalog_parquet(entries_path),
        manifest=CatalogManifest.from_path(manifest_path),
    )


def _validate_unique_ids(frame: pl.DataFrame) -> None:
    duplicates = (
        frame.group_by("id")
        .len("rows")
        .filter(pl.col("rows") > 1)
        .get_column("id")
        .to_list()
    )
    if duplicates:
        joined = ", ".join(str(item) for item in sorted(duplicates))
        raise CatalogValidationError(
            f"Catalog contains duplicate guideline entry IDs: {joined}."
        )


def _dataframe_digest(frame: pl.DataFrame) -> str:
    hasher = hashlib.sha256()
    for row in frame.sort("id").to_dicts():
        payload = json.dumps(
            row,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        hasher.update(payload.encode("utf-8"))
    return hasher.hexdigest()


__all__ = ["Catalog"]
