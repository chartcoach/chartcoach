from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from os import PathLike
from pathlib import Path
from urllib.parse import urlparse

import dataclasses as dc
import hashlib
import json
from typing import TYPE_CHECKING, cast

import polars as pl

from ..guideline.core import Guideline

if TYPE_CHECKING:
    import duckdb as duckdb_module

    from ..duckdb import DuckDBConfigValue

    from .manifest import CatalogManifest
    from .tables import ReferenceTables


@dc.dataclass(frozen=True, slots=True)
class _CatalogRecord:
    """One guideline together with the references that support it."""

    guideline: Guideline
    references: tuple[str, ...] = dc.field(default_factory=tuple)

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "references",
            _str_sequence(self.references, "references"),
        )

    @classmethod
    def from_mapping(cls, data: object) -> "_CatalogRecord":
        """Build an entry from a raw mapping."""
        if isinstance(data, cls):
            return data
        if not isinstance(data, Mapping):
            raise TypeError("Catalog record data must be a mapping.")
        values = cast(Mapping[str, object], data)
        parsed_references = _str_sequence(values.get("references") or [], "references")
        guideline = Guideline.from_mapping(values.get("guideline"))
        top_level_id = values.get("id")
        if top_level_id is not None and top_level_id != guideline.id:
            raise ValueError(
                f"catalog row id {top_level_id!r} does not match guideline id {guideline.id!r}."
            )
        return cls(
            guideline=guideline,
            references=parsed_references,
        )

    @property
    def id(self) -> str:
        """Return the stable id of this entry."""

        return self.guideline.id

    def to_record(self) -> dict[str, object]:
        """Return the serialized entry shape used by catalog dataframes."""
        return {
            "id": self.id,
            "guideline": self.guideline.to_record(),
            "references": list(self.references),
        }


class Catalog:
    """Source collection of guidelines and references.

    The catalog is Polars-first. Loading a parquet file keeps the serialized
    table as the source of truth. Python entry objects are built only
    when a caller asks for one entry.
    """

    def __init__(
        self,
        frame: pl.DataFrame,
        *,
        manifest: "CatalogManifest | None" = None,
    ) -> None:
        self._frame = _normalize_catalog_frame(frame)
        self._manifest = manifest
        _validate_unique_ids(self._frame)
        if self._manifest is not None:
            from .manifest import validate_catalog_manifest

            validate_catalog_manifest(self, self._manifest)

    @classmethod
    def from_frame(
        cls,
        df: pl.DataFrame,
        *,
        manifest: "CatalogManifest | None" = None,
    ) -> "Catalog":
        """Build a catalog from a serialized dataframe."""

        return cls(df, manifest=manifest)

    @classmethod
    def from_entries(
        cls,
        entries: Iterable[Guideline | Mapping[str, object]],
        *,
        manifest: "CatalogManifest | None" = None,
    ) -> "Catalog":
        """Build a catalog from guideline objects or flat guideline mappings."""

        from .tables import build_catalog_df

        catalog_records = tuple(_catalog_record(entry) for entry in entries)
        return cls(build_catalog_df(catalog_records), manifest=manifest)

    @classmethod
    def from_folder(cls, folder_path: PathLike[str]) -> "Catalog":
        """Load a catalog from ChartCoach's folder layout on disk."""

        from .storage import load_catalog

        return load_catalog(folder_path)

    @classmethod
    def from_parquet(cls, path: str | PathLike[str]) -> "Catalog":
        """Load a serialized entries parquet file without building entry objects."""

        return cls.from_frame(pl.read_parquet(Path(path)))

    @classmethod
    def from_bundle(cls, path: str | PathLike[str]) -> "Catalog":
        """Load a catalog bundle with `MANIFEST.md`, `entries.parquet`, and optional metadata."""

        from .manifest import CatalogManifest

        bundle_path = Path(path)
        manifest = CatalogManifest.from_path(bundle_path / "MANIFEST.md")
        return cls.from_frame(
            pl.read_parquet(bundle_path / "entries.parquet"),
            manifest=manifest,
        )

    @classmethod
    def open(cls, path: str | PathLike[str] | None = None) -> "Catalog":
        """Load a catalog from a default, remote, local folder, bundle, or parquet file."""

        if path is None:
            from .remote import default_catalog_bundle

            return cls.from_bundle(default_catalog_bundle())
        if isinstance(path, str) and _is_http_url(path):
            from .remote import download_catalog_bundle, metadata_url

            return cls.from_bundle(download_catalog_bundle(metadata_url(path)))

        source = Path(path)
        if source.is_dir():
            if (source / "entries.parquet").exists():
                return cls.from_bundle(source)
            return cls.from_folder(source)
        return cls.from_parquet(source)

    @property
    def manifest(self) -> "CatalogManifest | None":
        """Return the catalog manifest when this catalog was loaded with one."""

        return self._manifest

    def require_manifest(self) -> "CatalogManifest":
        """Return the catalog manifest or raise when only a table was loaded."""

        if self._manifest is None:
            raise ValueError("Catalog does not have a manifest.")
        return self._manifest

    def to_frame(self) -> pl.DataFrame:
        """Return the serialized catalog table."""

        return self._frame

    def guidelines(self) -> pl.DataFrame:
        """Return one row per guideline."""

        from .tables import build_guidelines_df

        return build_guidelines_df(self.to_frame())

    def sections(self) -> pl.DataFrame:
        """Return one row per guideline section."""

        from .tables import build_sections_df

        return build_sections_df(self.guidelines())

    def labels(self) -> pl.DataFrame:
        """Return the unique labels used across guidelines."""

        from .tables import build_labels_df

        return build_labels_df(self.guidelines())

    def guideline_labels(self) -> pl.DataFrame:
        """Return labels attached to each guideline."""

        from .tables import build_guideline_labels_df

        return build_guideline_labels_df(self.guidelines())

    def guideline_references(self) -> pl.DataFrame:
        """Return the links between guidelines and their references."""

        return self._reference_tables().guideline_references

    def guideline_sources(self) -> pl.DataFrame:
        """Return source metadata joined to each guideline-reference edge."""

        from .tables import build_guideline_sources_df

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
        config: Mapping[str, "DuckDBConfigValue"] | None = None,
    ) -> "duckdb_module.DuckDBPyConnection":
        """Return an in-memory DuckDB connection over the catalog tables."""

        from ..duckdb import connect_catalog

        return connect_catalog(self, config=config)

    def _entries(self) -> tuple[_CatalogRecord, ...]:
        """Build catalog entry objects from the serialized dataframe."""

        return tuple(
            _CatalogRecord.from_mapping(row) for row in self.to_frame().to_dicts()
        )

    def _catalog_record(self, guideline_id: str) -> _CatalogRecord:
        """Return one internal storage entry by guideline id."""

        rows = self.to_frame().filter(pl.col("id") == guideline_id)
        if rows.is_empty():
            raise KeyError(guideline_id)
        return _CatalogRecord.from_mapping(rows.row(0, named=True))

    def entry(self, guideline_id: str) -> dict[str, object]:
        """Return one flat guideline record by id."""

        storage_entry = self._catalog_record(guideline_id)
        return {
            **storage_entry.guideline.to_record(),
            "references": list(storage_entry.references),
        }

    def digest(self) -> str:
        """Return a stable digest of the serialized catalog table."""

        return _dataframe_digest(self.to_frame())

    def write_folder(self, root: PathLike[str]) -> None:
        """Write the catalog back to the folder layout used on disk."""

        from .storage import write_catalog_entries

        write_catalog_entries(self._entries(), root, manifest=self.require_manifest())

    def write_parquet(self, path: str | PathLike[str]) -> None:
        """Write the catalog to a serialized parquet file."""

        self.to_frame().write_parquet(Path(path))

    def write_bundle(
        self,
        root: PathLike[str],
        *,
        overwrite: bool = False,
    ) -> Path:
        """Write `MANIFEST.md`, `entries.parquet`, and `metadata.json` to a catalog bundle."""

        bundle_path = Path(root)
        parquet_path = bundle_path / "entries.parquet"
        manifest_path = bundle_path / "MANIFEST.md"
        metadata_path = bundle_path / "metadata.json"
        if not overwrite and (
            parquet_path.exists() or manifest_path.exists() or metadata_path.exists()
        ):
            raise FileExistsError(bundle_path)
        bundle_path.mkdir(parents=True, exist_ok=True)
        self.require_manifest().write(manifest_path)
        self.write_parquet(parquet_path)
        from .remote import write_release_metadata

        write_release_metadata(self, bundle_path)
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

    def merge(self, other: "Catalog") -> "Catalog":
        """Return a new catalog that combines the entries from both catalogs."""

        return Catalog.from_frame(
            pl.concat([self.to_frame(), other.to_frame()]),
            manifest=_merge_manifests(self.manifest, other.manifest),
        )

    def select(self, guideline_ids: Sequence[str]) -> "Catalog":
        """Return a new catalog with the requested guideline ids in order."""

        from .tables import CATALOG_SCHEMA

        wanted = pl.DataFrame(
            {"id": list(guideline_ids), "_order": range(len(guideline_ids))},
            schema={"id": pl.String, "_order": pl.Int64},
        )
        selected = (
            wanted.join(self.to_frame(), on="id", how="left")
            .sort("_order")
            .drop("_order")
        )
        if selected.get_column("guideline").null_count() > 0:
            available = set(self.to_frame().get_column("id").to_list())
            missing = [
                guideline_id
                for guideline_id in guideline_ids
                if guideline_id not in available
            ]
            raise KeyError(", ".join(missing))
        return Catalog.from_frame(selected.cast(CATALOG_SCHEMA), manifest=self.manifest)

    def __add__(self, other: "Catalog") -> "Catalog":
        return self.merge(other)

    def __len__(self) -> int:
        return self.to_frame().height

    def _reference_tables(self) -> "ReferenceTables":
        from .tables import build_reference_tables

        return build_reference_tables(self.to_frame())


__all__ = ["Catalog"]


def _str_sequence(value: object, field: str) -> tuple[str, ...]:
    if not isinstance(value, Sequence) or isinstance(value, str | bytes):
        raise TypeError(f"{field} must be a list of strings.")
    parsed: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise TypeError(f"{field} must be a list of strings.")
        parsed.append(item)
    return tuple(parsed)


def _catalog_record(data: object) -> _CatalogRecord:
    if isinstance(data, Guideline):
        return _CatalogRecord(guideline=data)
    if not isinstance(data, Mapping):
        raise TypeError("Catalog entries must be Guideline objects or mappings.")
    values = cast(Mapping[str, object], data)
    if "guideline" in values:
        return _CatalogRecord.from_mapping(values)
    return _CatalogRecord(
        guideline=Guideline.from_mapping(values),
        references=_str_sequence(values.get("references") or (), "references"),
    )


def _normalize_catalog_frame(df: pl.DataFrame) -> pl.DataFrame:
    from .tables import CATALOG_SCHEMA

    missing = [
        column
        for column in ("id", "guideline", "references")
        if column not in df.columns
    ]
    if missing:
        raise ValueError(
            f"Catalog dataframe is missing column(s): {', '.join(missing)}."
        )
    normalized = df.select("id", "guideline", "references").cast(CATALOG_SCHEMA)
    nested_id = pl.col("guideline").struct.field("id")
    mismatches = (
        normalized.select(
            row_id=pl.col("id"),
            guideline_id=nested_id,
        )
        .filter(
            pl.col("guideline_id").is_null()
            | (pl.col("row_id") != pl.col("guideline_id"))
        )
        .to_dicts()
    )
    if mismatches:
        rows = ", ".join(
            f"{row['row_id']!r} != {row['guideline_id']!r}" for row in mismatches
        )
        raise ValueError(f"Catalog row id must match guideline id: {rows}.")
    return normalized


def _validate_unique_ids(df: pl.DataFrame) -> None:
    duplicates = (
        df.group_by("id")
        .len("rows")
        .filter(pl.col("rows") > 1)
        .get_column("id")
        .to_list()
    )
    if duplicates:
        joined = ", ".join(str(item) for item in sorted(duplicates))
        raise ValueError(f"Catalog contains duplicate guideline ids: {joined}.")


def _merge_manifests(
    first: "CatalogManifest | None",
    second: "CatalogManifest | None",
) -> "CatalogManifest | None":
    if first is None:
        return second
    if second is None or first == second:
        return first
    raise ValueError("Cannot merge catalogs with different manifests.")


def _dataframe_digest(df: pl.DataFrame) -> str:
    hasher = hashlib.sha256()
    for row in df.sort("id").to_dicts():
        payload = json.dumps(
            row,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        hasher.update(payload.encode("utf-8"))
    return hasher.hexdigest()


def _is_http_url(value: str) -> bool:
    scheme = urlparse(value).scheme
    return scheme in {"http", "https"}
