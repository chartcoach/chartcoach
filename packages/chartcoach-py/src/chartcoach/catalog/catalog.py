from os import PathLike

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
