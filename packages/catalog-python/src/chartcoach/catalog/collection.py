from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from os import PathLike
from pathlib import Path

import dataclasses as dc
import hashlib
import json
from typing import TYPE_CHECKING, cast

import polars as pl

from ..guideline.core import Guideline

if TYPE_CHECKING:
    import duckdb as duckdb_module

    from ..duckdb import DuckDBConfigValue

    from .tables import ReferenceTables


@dc.dataclass(frozen=True, slots=True)
class CatalogEntry:
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
    def from_mapping(cls, data: object) -> "CatalogEntry":
        """Build an entry from a raw mapping."""
        if isinstance(data, cls):
            return data
        if not isinstance(data, Mapping):
            raise TypeError("CatalogEntry data must be a mapping.")
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
    table as the source of truth. Python `CatalogEntry` objects are built only
    when a caller asks for one entry.
    """

    def __init__(self, frame: pl.DataFrame) -> None:
        self._frame = _normalize_catalog_frame(frame)
        self._tables: dict[str, pl.DataFrame] = {}
        self._reference_tables_cache: ReferenceTables | None = None
        self._formatted_references_cache: pl.DataFrame | None = None
        self._digest_cache: str | None = None
        _validate_unique_ids(self._frame)

    @classmethod
    def from_frame(cls, df: pl.DataFrame) -> "Catalog":
        """Build a catalog from a serialized dataframe."""

        return cls(df)

    @classmethod
    def from_entries(cls, entries: Iterable[CatalogEntry]) -> "Catalog":
        """Build a catalog from entry objects."""

        from .tables import build_catalog_df

        catalog_entries = tuple(CatalogEntry.from_mapping(entry) for entry in entries)
        return cls(build_catalog_df(catalog_entries))

    @classmethod
    def from_folder(cls, folder_path: PathLike[str]) -> "Catalog":
        """Load a catalog from ChartCoach's folder layout on disk."""

        from .storage import load_catalog

        return load_catalog(folder_path)

    @classmethod
    def from_parquet(cls, path: str | PathLike[str]) -> "Catalog":
        """Load a serialized catalog parquet file without building entry objects."""

        return cls.from_frame(pl.read_parquet(Path(path)))

    def to_frame(self) -> pl.DataFrame:
        """Return the serialized catalog table."""

        return self._frame

    def guidelines(self) -> pl.DataFrame:
        """Return one row per guideline."""

        if "guidelines" in self._tables:
            return self._tables["guidelines"]
        from .tables import build_guidelines_df

        frame = build_guidelines_df(self.to_frame())
        self._tables["guidelines"] = frame
        return frame

    def sections(self) -> pl.DataFrame:
        """Return one row per guideline section."""

        if "sections" in self._tables:
            return self._tables["sections"]
        from .tables import build_sections_df

        frame = build_sections_df(self.guidelines())
        self._tables["sections"] = frame
        return frame

    def labels(self) -> pl.DataFrame:
        """Return the unique labels used across guidelines."""

        if "labels" in self._tables:
            return self._tables["labels"]
        from .tables import build_labels_df

        frame = build_labels_df(self.guidelines())
        self._tables["labels"] = frame
        return frame

    def guideline_labels(self) -> pl.DataFrame:
        """Return labels attached to each guideline."""

        if "guideline_labels" in self._tables:
            return self._tables["guideline_labels"]
        from .tables import build_guideline_labels_df

        frame = build_guideline_labels_df(self.guidelines())
        self._tables["guideline_labels"] = frame
        return frame

    def guideline_references(self) -> pl.DataFrame:
        """Return the links between guidelines and their references."""

        return self._reference_tables().guideline_references

    def guideline_sources(self) -> pl.DataFrame:
        """Return source metadata joined to each guideline-reference edge."""

        if "guideline_sources" in self._tables:
            return self._tables["guideline_sources"]
        from .tables import build_guideline_sources_df

        frame = build_guideline_sources_df(
            self.guideline_references(),
            self.formatted_references(),
        )
        self._tables["guideline_sources"] = frame
        return frame

    def references(self) -> pl.DataFrame:
        """Return parsed structural BibTeX reference entries."""

        return self._reference_tables().references

    def formatted_references(self) -> pl.DataFrame:
        """Return parsed reference entries with formatted citations."""

        if self._formatted_references_cache is None:
            from .tables import build_formatted_references_df

            reference_tables = self._reference_tables()
            self._formatted_references_cache = build_formatted_references_df(
                reference_tables.references,
                reference_tables.references_by_id,
            )
        return self._formatted_references_cache

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

    def _entries(self) -> tuple[CatalogEntry, ...]:
        """Build catalog entry objects from the serialized dataframe."""

        return tuple(
            CatalogEntry.from_mapping(row) for row in self.to_frame().to_dicts()
        )

    def entry(self, guideline_id: str) -> CatalogEntry:
        """Return one catalog entry by guideline id."""

        rows = self.to_frame().filter(pl.col("id") == guideline_id)
        if rows.is_empty():
            raise KeyError(guideline_id)
        return CatalogEntry.from_mapping(rows.row(0, named=True))

    def digest(self) -> str:
        """Return a stable digest of the serialized catalog table."""

        if self._digest_cache is None:
            self._digest_cache = _dataframe_digest(self.to_frame())
        return self._digest_cache

    def write_folder(self, root: PathLike[str]) -> None:
        """Write the catalog back to the folder layout used on disk."""

        from .storage import write_catalog_entries

        write_catalog_entries(self._entries(), root)

    def write_parquet(self, path: str | PathLike[str]) -> None:
        """Write the catalog to a serialized parquet file."""

        self.to_frame().write_parquet(Path(path))

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

        return Catalog.from_frame(pl.concat([self.to_frame(), other.to_frame()]))

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
        return Catalog.from_frame(selected.cast(CATALOG_SCHEMA))

    def __add__(self, other: "Catalog") -> "Catalog":
        return self.merge(other)

    def __len__(self) -> int:
        return self.to_frame().height

    def _reference_tables(self) -> "ReferenceTables":
        if self._reference_tables_cache is None:
            from .tables import build_reference_tables

            self._reference_tables_cache = build_reference_tables(self.to_frame())
        return self._reference_tables_cache


__all__ = ["Catalog", "CatalogEntry"]


def _str_sequence(value: object, field: str) -> tuple[str, ...]:
    if not isinstance(value, Sequence) or isinstance(value, str | bytes):
        raise TypeError(f"{field} must be a list of strings.")
    parsed: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise TypeError(f"{field} must be a list of strings.")
        parsed.append(item)
    return tuple(parsed)


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
