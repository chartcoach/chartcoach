from __future__ import annotations

from io import BytesIO
from os import PathLike
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

import polars as pl

from .model import CatalogEntry


class Catalog:
    """Wraps a collection of catalog entries"""

    def __init__(self, entries: list[CatalogEntry] | None = None) -> None:
        self._entries = entries or []
        self._df_cache: pl.DataFrame | None = None

    @classmethod
    def from_df(cls, df: pl.DataFrame) -> "Catalog":
        entries = [CatalogEntry.model_validate(row) for row in df.to_dicts()]
        return Catalog(entries=entries)

    @classmethod
    def from_disk(cls, folder_path: PathLike[str]) -> "Catalog":
        from .load import load_catalog

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

    def df(self) -> pl.DataFrame:
        if self._df_cache is None:
            dicts = [entry.model_dump() for entry in self._entries]
            self._df_cache = (
                pl.from_dicts(dicts)
                .select("id", "guideline", "references")
                .unique("id")
                .sort("id")
            )
        return self._df_cache.clone()

    def sections_df(self) -> pl.DataFrame:
        return (
            self.df()
            .select("guideline")
            .unnest("guideline")
            .select("id", "sections")
            .explode("sections")
            .unnest("sections")
            .select("id", "role", "content")
        )

    def merge(self, other: "Catalog") -> "Catalog":
        merged_entries = self._entries + other.entries
        return Catalog(entries=merged_entries)

    def labels_df(self) -> pl.DataFrame:
        df = self.df()
        return (
            df.select("guideline")
            .unnest("guideline")
            .select("labels")
            .explode("labels")
            .select(
                category=pl.col("labels").str.split(":").list.get(0),
                subcategory=pl.col("labels").str.split(":").list.get(1),
            )
            .unique()
            .sort("category", "subcategory")
        )

    def write_folders(self, root: PathLike[str]) -> None:
        from .serialize import catalog_to_disk

        catalog_to_disk(self, root)

    def __add__(self, other: "Catalog") -> "Catalog":
        return self.merge(other)

    def __len__(self) -> int:
        return len(self._entries)

    def __getitem__(self, index: int) -> CatalogEntry:
        return self._entries[index]

    def __iter__(self):
        return iter(self._entries)
