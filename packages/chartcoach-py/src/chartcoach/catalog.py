from __future__ import annotations

import pathlib
from functools import cached_property, cache
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
        from .utils import load_catalog

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
    def df(self) -> pl.DataFrame:
        if self._df_cache is None:
            if not self._entries:
                section_schema = pl.Struct(
                    [
                        pl.Field("role", pl.String),
                        pl.Field("title", pl.String),
                        pl.Field("content", pl.String),
                    ]
                )
                guideline_schema = pl.Struct(
                    [
                        pl.Field("id", pl.String),
                        pl.Field("title", pl.String),
                        pl.Field("bibliography", pl.String),
                        pl.Field("description", pl.String),
                        pl.Field("labels", pl.List(pl.String)),
                        pl.Field("body", pl.String),
                        pl.Field("sections", pl.List(section_schema)),
                    ]
                )
                self._df_cache = pl.DataFrame(
                    schema={
                        "id": pl.String,
                        "guideline": guideline_schema,
                        "references": pl.List(pl.String),
                    }
                )
            else:
                dicts = [entry.model_dump() for entry in self._entries]
                self._df_cache = (
                    pl.from_dicts(dicts)
                    .select("id", "guideline", "references")
                    .unique("id")
                    .sort("id")
                )
        return self._df_cache.clone()

    @cached_property
    def sections_df(self) -> pl.DataFrame:
        return (
            self.df.select("guideline")
            .unnest("guideline")
            .select("id", "sections")
            .explode("sections")
            .unnest("sections")
            .select("id", "role", "content")
        )

    @cached_property
    def guidelines_df(self) -> pl.DataFrame:
        return self.df.select("guideline").unnest("guideline")

    @cached_property
    def references_df(self) -> pl.DataFrame:
        from .utils import format_bibtex_entry, parse_bibtex_entry

        return (
            self.df.select("references")
            .explode("references")
            .drop_nulls()
            .unique()
            .select(
                bibtex="references",
                obj=pl.col("references").map_elements(
                    lambda it: {
                        "id": parse_bibtex_entry(it)["ID"],
                        "formatted": format_bibtex_entry(it),
                    },
                    return_dtype=pl.Struct(
                        [
                            pl.Field("id", pl.String),
                            pl.Field("formatted", pl.String),
                        ]
                    ),
                ),
            )
            .select(
                id=pl.col("obj").struct.field("id"),
                bibtex="bibtex",
                formatted=pl.col("obj").struct.field("formatted"),
            )
            .sort("id")
        )

    @cached_property
    def labels_df(self) -> pl.DataFrame:
        df = self.df
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

    @cached_property
    def docs_df(self) -> pl.DataFrame:
        import polars_hash as plh

        return (
            pl.concat(
                [
                    self._toplevel_docs_df,
                    self._section_docs_df,
                ],
                how="vertical",
            )
            .sort("id")
            .with_columns(
                metadata=pl.struct(
                    parent_id=pl.col("metadata").struct.field("parent_id"),
                    role=pl.col("metadata").struct.field("role"),
                    labels=pl.col("metadata").struct.field("labels"),
                    content_hash=plh.col("doc").chash.sha2_256(),
                )
            )
        )

    @cache
    def hexdigest(self) -> str:
        import hashlib

        hasher = hashlib.sha256()
        for entry in self.entries:
            refs = "\n".join(entry.references)
            hasher.update(refs.encode("utf-8"))

            guideline = entry.guideline.to_markdown()
            hasher.update(guideline.encode("utf-8"))

        return hasher.hexdigest()

    @cached_property
    def _toplevel_docs_df(self) -> pl.DataFrame:
        return (
            self.guidelines_df.select(
                "id",
                overview=pl.concat_str(["title", "description"], separator="\n\n"),
                labels="labels",
            )
            .unpivot(
                index=["id", "labels"],
                variable_name="role",
                value_name="doc",
            )
            .select(
                id=pl.concat_str(["id", "role"], separator="---"),
                doc="doc",
                metadata=pl.struct(
                    parent_id="id",
                    role="role",
                    labels="labels",
                ),
            )
        )

    @cached_property
    def _section_docs_df(self) -> pl.DataFrame:
        return (
            self.guidelines_df.select(
                "id", "sections", "labels", guideline_title="title"
            )
            .explode("sections")
            .unnest("sections")
            .select(
                id=pl.concat_str(["id", pl.lit("role"), "role"], separator="---"),
                doc="content",
                metadata=pl.struct(
                    parent_id="id",
                    role=pl.concat_str([pl.lit("section"), "role"], separator="."),
                    labels="labels",
                ),
            )
            .with_columns(
                # Replace [@citeKey] occurrences in section docs with the formatted reference entries for better embeddings
                doc=pl.when(pl.col("doc").str.contains("[@", literal=True))
                .then(
                    pl.concat_str(
                        [
                            "doc",
                            pl.lit("\n**References**\n"),
                            pl.col("doc")
                            .str.extract_all((r"@[\w\.-]+"))
                            .list.eval(pl.element().str.replace_all(r"^@", ""))
                            .map_elements(
                                lambda it: "\n".join(
                                    pl.from_dict({"id": it})
                                    .join(self.references_df, on="id", how="left")
                                    .drop_nulls()
                                    .unique()
                                    .sort("id")
                                    .select(
                                        refmap=pl.concat_str(
                                            [
                                                pl.lit("- "),
                                                "id",
                                                pl.lit(": "),
                                                "formatted",
                                            ],
                                            separator="",
                                        )
                                    )
                                    .get_column("refmap")
                                    .to_list()
                                ),
                                return_dtype=pl.String,
                            ),
                        ],
                        separator="\n",
                    )
                )
                .otherwise("doc")
            )
        )

    def write_folders(self, root: PathLike[str]) -> None:
        folder_path = pathlib.Path(root)
        folder_path.mkdir(parents=True, exist_ok=True)

        for entry in self.entries:
            entry_folder = folder_path / entry.guideline.id
            entry_folder.mkdir(parents=True, exist_ok=True)

            # Write guideline markdown
            guideline_md_path = entry_folder / "guideline.md"
            guideline_md_path.write_text(entry.guideline.to_markdown())

            # Write bibliography if present
            if entry.guideline.bibliography is not None:
                bib_path = entry_folder / "references.bib"
                bib_content = "\n".join(ref for ref in entry.references)
                bib_path.write_text(bib_content)

    def merge(self, other: "Catalog") -> "Catalog":
        merged_entries = self._entries + other.entries
        return Catalog(entries=merged_entries)

    def __add__(self, other: "Catalog") -> "Catalog":
        return self.merge(other)

    def __len__(self) -> int:
        return len(self._entries)

    def __getitem__(self, index: int) -> CatalogEntry:
        return self._entries[index]

    def __iter__(self):
        return iter(self._entries)
