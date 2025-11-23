from os import PathLike

import polars as pl

from .model import CatalogEntry


class Catalog:
    """Wraps a collection of catalog entries"""

    def __init__(self, entries: list[CatalogEntry] | None = None) -> None:
        self._entries = entries or []

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
        dicts = [entry.model_dump() for entry in self._entries]
        return (
            pl.from_dicts(dicts)
            .select("id", "guideline", "references")
            .unique("id")
            .sort("id")
        )

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

    def projected_sections_df(
        self,
        select: list[pl.Expr | str] | None = None,
        x: str = "projection_x",
        y: str = "projection_y",
        neighbors: str = "neighbors",
        umap_args: dict = {},
        **kwargs,
    ) -> pl.DataFrame:
        from .embeddings import embed_sections, project_embedded_sections

        df = self.df()
        sections_df = self.sections_df()
        embedded_sections_df = embed_sections(sections_df, **kwargs)

        if select is not None:
            id_df = df.select("id")
            selected_df = df.select(*select)
            join_df = pl.concat([id_df, selected_df], how="horizontal")
            embedded_sections_df = embedded_sections_df.join(
                join_df,
                on="id",
                how="left",
            )

        return project_embedded_sections(
            embedded_sections_df,
            x=x,
            y=y,
            neighbors=neighbors,
            umap_args=umap_args,
        )

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
