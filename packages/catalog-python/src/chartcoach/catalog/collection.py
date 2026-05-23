from __future__ import annotations

from functools import cache, cached_property
from os import PathLike
from pathlib import Path
from urllib.parse import urlparse

import dataclasses as dc
from collections.abc import Mapping
from typing import cast
import polars as pl

from ..guideline.core import Guideline


@dc.dataclass(frozen=True, slots=True)
class Entry:
    """One guideline together with the references that support it."""

    guideline: Guideline
    references: list[str] = dc.field(default_factory=list)

    @classmethod
    def model_validate(cls, data: object) -> "Entry":
        """Build an entry from a raw mapping."""
        if isinstance(data, cls):
            return data
        if not isinstance(data, Mapping):
            raise TypeError("Entry data must be a mapping.")
        values = cast(Mapping[str, object], data)
        references = values.get("references") or []
        if not isinstance(references, list):
            raise TypeError("references must be a list of strings.")
        parsed_references: list[str] = []
        for item in references:
            if not isinstance(item, str):
                raise TypeError("references must be a list of strings.")
            parsed_references.append(item)
        return cls(
            guideline=Guideline.model_validate(values.get("guideline")),
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
            "references": self.references,
        }


class Catalog:
    """Source collection of guidelines and references before search data is built."""

    def __init__(self, entries: list[Entry] | None = None) -> None:
        self._entries = entries or []

    @classmethod
    def from_df(cls, df: pl.DataFrame) -> "Catalog":
        """Build a catalog from serialized entries in a dataframe."""

        entries = [Entry.model_validate(row) for row in df.to_dicts()]
        return cls(entries=entries)

    @classmethod
    def from_disk(cls, folder_path: PathLike[str]) -> "Catalog":
        """Load a catalog from ChartCoach's folder layout on disk."""

        from .storage import load_catalog

        return load_catalog(folder_path)

    @classmethod
    def from_uri(cls, uri: str | PathLike[str]) -> "Catalog":
        """Load a catalog from a folder, a local parquet file, or a remote parquet file."""

        if not isinstance(uri, str):
            return cls._from_path(Path(uri))

        if uri.startswith("file://"):
            return cls._from_path(Path(uri.removeprefix("file://")))

        parsed = urlparse(uri)
        if parsed.scheme in {"http", "https", "s3"}:
            if not parsed.path.endswith(".parquet"):
                raise ValueError(
                    "Remote catalog sources must point to a .parquet file."
                )
            return cls.from_df(pl.read_parquet(uri))

        return cls._from_path(Path(uri))

    @classmethod
    def _from_path(cls, path: Path) -> "Catalog":
        if path.suffix == ".parquet":
            return cls.from_df(pl.read_parquet(path))
        return cls.from_disk(path)

    @property
    def entries(self) -> list[Entry]:
        """Return the entries that make up this catalog."""

        return self._entries

    @cached_property
    def df(self) -> pl.DataFrame:
        """Return the catalog as a dataframe."""

        from .tables import build_catalog_df

        return build_catalog_df(self._entries)

    @cached_property
    def guidelines_df(self) -> pl.DataFrame:
        """Return one row per guideline."""

        from .tables import build_guidelines_df

        return build_guidelines_df(self.df)

    @cached_property
    def sections_df(self) -> pl.DataFrame:
        """Return one row per guideline section."""

        from .tables import build_sections_df

        return build_sections_df(self.guidelines_df)

    @cached_property
    def references_df(self) -> pl.DataFrame:
        """Return parsed and formatted references used across the catalog."""

        from .tables import build_references_df

        return build_references_df(self.df)

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

        return build_guideline_references_df(self.df)

    @cached_property
    def docs_df(self) -> pl.DataFrame:
        """Return the text records used for semantic search."""

        from .documents import build_docs_df

        return build_docs_df(self.guidelines_df, self.references_df)

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

    def write_folders(self, root: PathLike[str]) -> None:
        """Write the catalog back to the folder layout used on disk."""

        from .storage import write_catalog_entries

        write_catalog_entries(self.entries, root)

    def merge(self, other: "Catalog") -> "Catalog":
        """Return a new catalog that combines the entries from both catalogs."""

        return Catalog(entries=self._entries + other.entries)

    def subset(self, doc_ids: list[str]) -> "Catalog":
        """Return a new catalog that contains only the entries corresponding to the given doc_ids."""

        df = (
            pl.from_dict({"id": doc_ids})
            .join(self.docs_df, how="left", on="id")
            .select(id=pl.col("metadata").struct.field("parent_id"))
            .unique("id", maintain_order=True)
            .join(self.df, how="left", on="id")
        )
        return Catalog.from_df(df)

    def __add__(self, other: "Catalog") -> "Catalog":
        return self.merge(other)

    def __len__(self) -> int:
        return len(self._entries)

    def __getitem__(self, index: int) -> Entry:
        return self._entries[index]

    def __iter__(self):
        return iter(self._entries)


__all__ = ["Catalog", "Entry"]
