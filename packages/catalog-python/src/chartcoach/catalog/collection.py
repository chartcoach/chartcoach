from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from functools import cache, cached_property
from os import PathLike
from pathlib import Path

import dataclasses as dc
from typing import Iterator, cast
import polars as pl

from ..guideline.core import Guideline


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
    def model_validate(cls, data: object) -> "CatalogEntry":
        """Build an entry from a raw mapping."""
        if isinstance(data, cls):
            return data
        if not isinstance(data, Mapping):
            raise TypeError("CatalogEntry data must be a mapping.")
        values = cast(Mapping[str, object], data)
        parsed_references = _str_sequence(values.get("references") or [], "references")
        guideline = Guideline.model_validate(values.get("guideline"))
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

    def model_dump(self) -> dict[str, object]:
        """Return the serialized entry shape used by catalog dataframes."""
        return {
            "id": self.id,
            "guideline": self.guideline.model_dump(),
            "references": list(self.references),
        }


@dc.dataclass(frozen=True, slots=True)
class CatalogFrames:
    """Canonical dataframe views derived from a catalog."""

    catalog: pl.DataFrame
    guidelines: pl.DataFrame
    sections: pl.DataFrame
    references: pl.DataFrame
    labels: pl.DataFrame
    guideline_labels: pl.DataFrame
    guideline_references: pl.DataFrame


class Catalog:
    """Source collection of guidelines and references."""

    def __init__(self, entries: Iterable[CatalogEntry] | None = None) -> None:
        parsed_entries = tuple(
            CatalogEntry.model_validate(entry) for entry in (entries or ())
        )
        seen: set[str] = set()
        duplicate_ids: list[str] = []
        for entry in parsed_entries:
            if entry.id in seen:
                duplicate_ids.append(entry.id)
            seen.add(entry.id)
        if duplicate_ids:
            joined = ", ".join(sorted(set(duplicate_ids)))
            raise ValueError(f"Catalog contains duplicate guideline ids: {joined}.")
        self._entries = parsed_entries

    @classmethod
    def from_frame(cls, df: pl.DataFrame) -> "Catalog":
        """Build a catalog from serialized entries in a dataframe."""

        entries = [CatalogEntry.model_validate(row) for row in df.to_dicts()]
        return cls(entries=entries)

    @classmethod
    def from_folder(cls, folder_path: PathLike[str]) -> "Catalog":
        """Load a catalog from ChartCoach's folder layout on disk."""

        from .storage import load_catalog

        return load_catalog(folder_path)

    @classmethod
    def from_parquet(cls, path: str | PathLike[str]) -> "Catalog":
        """Load a serialized catalog parquet file."""

        return cls.from_frame(pl.read_parquet(Path(path)))

    @property
    def entries(self) -> tuple[CatalogEntry, ...]:
        """Return the entries that make up this catalog."""

        return self._entries

    @cached_property
    def frame(self) -> pl.DataFrame:
        """Return the serialized catalog entries."""

        from .tables import build_catalog_df

        return build_catalog_df(self._entries)

    def to_frame(self) -> pl.DataFrame:
        """Return the serialized catalog entries."""

        return self.frame

    @cached_property
    def guidelines_df(self) -> pl.DataFrame:
        """Return one row per guideline."""

        from .tables import build_guidelines_df

        return build_guidelines_df(self.frame)

    @cached_property
    def sections_df(self) -> pl.DataFrame:
        """Return one row per guideline section."""

        from .tables import build_sections_df

        return build_sections_df(self.guidelines_df)

    @cached_property
    def references_df(self) -> pl.DataFrame:
        """Return parsed and formatted references used across the catalog."""

        from .tables import build_references_df

        return build_references_df(self.frame)

    @cached_property
    def labels_df(self) -> pl.DataFrame:
        """Return the unique labels used across guidelines."""

        from .tables import build_labels_df

        return build_labels_df(self.guidelines_df)

    @cached_property
    def guideline_labels_df(self) -> pl.DataFrame:
        """Return labels attached to each guideline."""

        from .tables import build_guideline_labels_df

        return build_guideline_labels_df(self.guidelines_df)

    @cached_property
    def guideline_references_df(self) -> pl.DataFrame:
        """Return the links between guidelines and their references."""

        from .tables import build_guideline_references_df

        return build_guideline_references_df(self.frame)

    @cached_property
    def frames(self) -> CatalogFrames:
        """Return all canonical dataframe views."""

        return CatalogFrames(
            catalog=self.frame,
            guidelines=self.guidelines_df,
            sections=self.sections_df,
            references=self.references_df,
            labels=self.labels_df,
            guideline_labels=self.guideline_labels_df,
            guideline_references=self.guideline_references_df,
        )

    @cache
    def hexdigest(self) -> str:
        """Return a stable digest of the catalog contents."""

        import hashlib

        hasher = hashlib.sha256()
        for entry in self.entries:
            refs = "\n".join(entry.references)
            hasher.update(refs.encode("utf-8"))
            hasher.update(entry.guideline.to_markdown().encode("utf-8"))
        return hasher.hexdigest()

    def write_folder(self, root: PathLike[str]) -> None:
        """Write the catalog back to the folder layout used on disk."""

        from .storage import write_catalog_entries

        write_catalog_entries(self.entries, root)

    def write_parquet(self, path: str | PathLike[str]) -> None:
        """Write the catalog to a serialized parquet file."""

        self.frame.write_parquet(Path(path))

    def get(self, guideline_id: str) -> CatalogEntry:
        """Return one catalog entry by guideline id."""

        for entry in self._entries:
            if entry.id == guideline_id:
                return entry
        raise KeyError(guideline_id)

    def merge(self, other: "Catalog") -> "Catalog":
        """Return a new catalog that combines the entries from both catalogs."""

        return Catalog(entries=self._entries + other.entries)

    def select(self, guideline_ids: Sequence[str]) -> "Catalog":
        """Return a new catalog with the requested guideline ids in order."""

        return Catalog(
            entries=[self.get(guideline_id) for guideline_id in guideline_ids]
        )

    def __add__(self, other: "Catalog") -> "Catalog":
        return self.merge(other)

    def __len__(self) -> int:
        return len(self._entries)

    def __getitem__(self, index: int) -> CatalogEntry:
        return self._entries[index]

    def __iter__(self) -> Iterator[CatalogEntry]:
        return iter(self._entries)


__all__ = ["Catalog", "CatalogEntry", "CatalogFrames"]


def _str_sequence(value: object, field: str) -> tuple[str, ...]:
    if not isinstance(value, Sequence) or isinstance(value, str | bytes):
        raise TypeError(f"{field} must be a list of strings.")
    parsed: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise TypeError(f"{field} must be a list of strings.")
        parsed.append(item)
    return tuple(parsed)
