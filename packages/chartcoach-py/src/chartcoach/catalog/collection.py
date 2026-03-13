from __future__ import annotations

from functools import cache, cached_property
from io import BytesIO
from os import PathLike
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

import polars as pl
from pydantic import BaseModel, Field, computed_field

from ..guideline.core import Guideline


class CatalogEntry(BaseModel):
    """Entry in the catalog with a guideline and its bibliography content."""

    guideline: Guideline = Field(
        description="The guideline entry associated with this catalog entry."
    )
    references: list[str] = Field(
        default_factory=list,
        description="BibTeX-formatted bibliography content for citations used in the guideline.",
    )

    @computed_field
    @property
    def id(self) -> str:
        """Get the unique identifier of the catalog entry."""
        return self.guideline.id


class Catalog:
    """Wrap a collection of catalog entries."""

    def __init__(self, entries: list[CatalogEntry] | None = None) -> None:
        self._entries = entries or []

    @classmethod
    def from_df(cls, df: pl.DataFrame) -> "Catalog":
        entries = [CatalogEntry.model_validate(row) for row in df.to_dicts()]
        return cls(entries=entries)

    @classmethod
    def from_disk(cls, folder_path: PathLike[str]) -> "Catalog":
        from .storage import load_catalog

        return load_catalog(folder_path)

    @classmethod
    def from_uri(cls, uri: str | PathLike[str]) -> "Catalog":
        """Load a catalog from a local path, file:// URL, http(s) URL, or s3:// URL."""
        if not isinstance(uri, str):
            return cls._from_path(Path(uri))

        if uri.startswith("file://"):
            return cls._from_path(Path(uri.removeprefix("file://")))

        parsed = urlparse(uri)
        if parsed.scheme in {"http", "https"}:
            if not parsed.path.endswith(".parquet"):
                raise ValueError("Remote catalog_uri must be a .parquet file.")
            return cls.from_df(cls._read_parquet_df_from_url(uri))

        if parsed.scheme == "s3":
            if not parsed.path.endswith(".parquet"):
                raise ValueError("Remote catalog_uri must be a .parquet file.")
            return cls.from_df(pl.read_parquet(uri))

        return cls._from_path(Path(uri))

    @classmethod
    def _from_path(cls, path: Path) -> "Catalog":
        if path.suffix == ".parquet":
            return cls.from_df(pl.read_parquet(path))
        return cls.from_disk(path)

    @staticmethod
    def _read_parquet_df_from_url(url: str) -> pl.DataFrame:
        with urlopen(url) as resp:  # noqa: S310
            data = resp.read()
        return pl.read_parquet(BytesIO(data))

    @property
    def entries(self) -> list[CatalogEntry]:
        return self._entries

    @cached_property
    def _df(self) -> pl.DataFrame:
        from .tables import build_catalog_df

        return build_catalog_df(self._entries)

    @property
    def df(self) -> pl.DataFrame:
        return self._df.clone()

    @cached_property
    def _guidelines_df(self) -> pl.DataFrame:
        from .tables import build_guidelines_df

        return build_guidelines_df(self._df)

    @property
    def guidelines_df(self) -> pl.DataFrame:
        return self._guidelines_df.clone()

    @cached_property
    def _sections_df(self) -> pl.DataFrame:
        from .tables import build_sections_df

        return build_sections_df(self._guidelines_df)

    @property
    def sections_df(self) -> pl.DataFrame:
        return self._sections_df.clone()

    @cached_property
    def _references_df(self) -> pl.DataFrame:
        from .tables import build_references_df

        return build_references_df(self._df)

    @property
    def references_df(self) -> pl.DataFrame:
        return self._references_df.clone()

    @cached_property
    def _labels_df(self) -> pl.DataFrame:
        from .tables import build_labels_df

        return build_labels_df(self._guidelines_df)

    @property
    def labels_df(self) -> pl.DataFrame:
        return self._labels_df.clone()

    @cached_property
    def _docs_df(self) -> pl.DataFrame:
        from .documents import build_docs_df

        return build_docs_df(self._guidelines_df, self._references_df)

    @property
    def docs_df(self) -> pl.DataFrame:
        return self._docs_df.clone()

    @cache
    def hexdigest(self) -> str:
        import hashlib

        hasher = hashlib.sha256()
        for entry in self.entries:
            refs = "\n".join(entry.references)
            hasher.update(refs.encode("utf-8"))
            hasher.update(entry.guideline.to_markdown().encode("utf-8"))
        return hasher.hexdigest()

    def write_folders(self, root: PathLike[str]) -> None:
        from .storage import write_catalog_entries

        write_catalog_entries(self.entries, root)

    def merge(self, other: "Catalog") -> "Catalog":
        return Catalog(entries=self._entries + other.entries)

    def __add__(self, other: "Catalog") -> "Catalog":
        return self.merge(other)

    def __len__(self) -> int:
        return len(self._entries)

    def __getitem__(self, index: int) -> CatalogEntry:
        return self._entries[index]

    def __iter__(self):
        return iter(self._entries)
