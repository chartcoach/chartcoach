from __future__ import annotations

import hashlib
import json
import shutil
from collections.abc import Iterable, Mapping
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING

import polars as pl

from .entries import Guideline
from .errors import CatalogValidationError

if TYPE_CHECKING:
    import duckdb as duckdb_module

    from ..duckdb import DuckDBConfigValue
    from .manifest import CatalogManifest
    from .references import ReferenceTables
    from .releases import CatalogRelease


class Catalog:
    """A manifest and its compiled guideline rows."""

    def __init__(
        self,
        frame: pl.DataFrame,
        *,
        manifest: CatalogManifest,
        release: CatalogRelease | None = None,
    ) -> None:
        self._frame = _normalize_catalog_frame(frame)
        self._manifest = manifest
        self._release = release
        self._reference_tables_cache: ReferenceTables | None = None
        _validate_unique_ids(self._frame)

        from .manifest import validate_catalog_manifest

        validate_catalog_manifest(self, manifest)

    @classmethod
    def from_guidelines(
        cls,
        guidelines: Iterable[Guideline],
        *,
        manifest: CatalogManifest,
    ) -> Catalog:
        """Build a catalog from compiled guidelines and a manifest."""

        from .tables import build_catalog_df

        return cls(build_catalog_df(tuple(guidelines)), manifest=manifest)

    @property
    def manifest(self) -> CatalogManifest:
        """Return the catalog vocabulary manifest."""

        return self._manifest

    @property
    def release(self) -> CatalogRelease | None:
        """Return the verified release record for a descriptor-backed catalog."""

        return self._release

    def to_frame(self) -> pl.DataFrame:
        """Return the compiled catalog rows."""

        return self._frame

    def guidelines(self) -> pl.DataFrame:
        """Return one row per guideline with derived markdown bodies."""

        from .tables import build_guidelines_df

        return build_guidelines_df(self.to_frame())

    def sections(self) -> pl.DataFrame:
        """Return one row per guideline section."""

        from .tables import build_sections_df

        return build_sections_df(self.guidelines())

    def guideline_labels(self) -> pl.DataFrame:
        """Return labels attached to each guideline."""

        from .tables import build_guideline_labels_df

        return build_guideline_labels_df(self.guidelines())

    def guideline_references(self) -> pl.DataFrame:
        """Return the links between guidelines and their references."""

        return self._reference_tables().guideline_references

    def guideline_sources(self) -> pl.DataFrame:
        """Return source metadata joined to each guideline-reference edge."""

        from .references import build_guideline_sources_df

        return build_guideline_sources_df(
            self.guideline_references(),
            self.references(),
        )

    def references(self) -> pl.DataFrame:
        """Return parsed structural BibTeX reference entries."""

        return self._reference_tables().references

    def table(self, name: str) -> pl.DataFrame:
        """Return one named catalog table."""

        from .relations import catalog_table

        return catalog_table(self, name)

    def duckdb(
        self,
        *,
        config: Mapping[str, DuckDBConfigValue] | None = None,
    ) -> duckdb_module.DuckDBPyConnection:
        """Return an in-memory DuckDB connection over the catalog tables."""

        from ..duckdb import connect_catalog

        return connect_catalog(self, config=config)

    def entry(self, guideline_id: str) -> dict[str, object]:
        """Return one guideline record with its derived markdown body."""

        guideline = self._guideline(guideline_id)
        return {**guideline.to_record(), "body": guideline.body}

    def content_digest(self) -> str:
        """Return a stable digest of the compiled catalog rows."""

        return _dataframe_digest(self.to_frame())

    def write_bundle(self, root: PathLike[str]) -> Path:
        """Write `MANIFEST.md` and `entries.parquet` to a new directory.

        Raises:
            FileExistsError: The bundle path already exists.
        """

        bundle_path = Path(root)
        bundle_path.parent.mkdir(parents=True, exist_ok=True)
        bundle_path.mkdir()
        try:
            self.manifest.write(bundle_path / "MANIFEST.md")
            self.to_frame().write_parquet(bundle_path / "entries.parquet")
        except BaseException:
            shutil.rmtree(bundle_path, ignore_errors=True)
            raise
        return bundle_path

    def write_duckdb(
        self,
        path: str | PathLike[str],
        *,
        overwrite: bool = False,
    ) -> Path:
        """Write the catalog tables to a DuckDB database file."""

        from ..duckdb import write_duckdb

        return write_duckdb(self, path, overwrite=overwrite)

    def __len__(self) -> int:
        return self.to_frame().height

    def _guideline(self, guideline_id: str) -> Guideline:
        rows = self.to_frame().filter(pl.col("id") == guideline_id)
        if rows.is_empty():
            raise KeyError(guideline_id)
        return Guideline.from_mapping(rows.row(0, named=True))

    def _reference_tables(self) -> ReferenceTables:
        from .references import build_reference_tables

        if self._reference_tables_cache is None:
            self._reference_tables_cache = build_reference_tables(self.to_frame())
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


def _load_catalog_bundle(
    manifest_path: Path,
    entries_path: Path,
    *,
    release: CatalogRelease | None = None,
) -> Catalog:
    from .manifest import CatalogManifest

    return Catalog(
        _read_catalog_parquet(entries_path),
        manifest=CatalogManifest.from_path(manifest_path),
        release=release,
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
        raise ValueError(f"Catalog contains duplicate guideline ids: {joined}.")


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
