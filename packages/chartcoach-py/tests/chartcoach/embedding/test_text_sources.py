from __future__ import annotations

from chartcoach.catalog.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.embedding import CatalogEmbedder, GuidelineFieldTextSource


def _make_catalog(n: int = 1) -> Catalog:
    entries: list[CatalogEntry] = []
    for i in range(n):
        gid = f"g{i}"
        entries.append(
            CatalogEntry(
                guideline=Guideline(
                    id=gid,
                    title=f"Title {i}",
                    description=f"Desc {i}",
                    bibliography=None,
                    labels=["chart:bar"],
                    body="## The Advice <!-- role: advice -->\n\nHello.",
                ),
                references=[],
            )
        )
    return Catalog(entries)


def test_text_sources_default_and_custom_roles() -> None:
    catalog = _make_catalog(1)
    default_embedder = CatalogEmbedder(catalog)
    roles = set(default_embedder.text_df().select("role").to_series().to_list())
    assert {"advice", "title", "description"}.issubset(roles)

    source = GuidelineFieldTextSource("title", role="headline")
    df = source.text_df(catalog)
    assert df.select("role").to_series().to_list() == ["headline"]

