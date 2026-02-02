from __future__ import annotations

import sys
import types

import numpy as np
import polars as pl
import pytest

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.index import InMemoryVectorIndexBackend
from chartcoach.retrieval.strategy import dspy_adapters
from chartcoach.retrieval.strategy.id_extraction import extract_guideline_ids
from chartcoach.retrieval.strategy.request_text import build_situation_with_query
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest, TextItem
from chartcoach.retrieval.strategy.vector_index import (
    CatalogVectorIndex,
    EmbeddingConfig,
    describe_text_source,
)


def test_build_situation_with_query_formats_and_requires_situation() -> None:
    request = RetrievalRequest(
        context=[
            TextItem(role="situation", text="S"),
            TextItem(role="query", text="Q"),
        ]
    )
    assert build_situation_with_query(request) == "S\n\nQuery:\nQ"
    assert (
        build_situation_with_query(RetrievalRequest(context=[TextItem(role="situation", text="S")]))
        == "S"
    )

    with pytest.raises(ValueError, match="Missing required TextItem"):
        build_situation_with_query(
            RetrievalRequest(context=[TextItem(role="query", text="Q")])
        )


def test_extract_guideline_ids_parses_various_shapes_and_feedback() -> None:
    known = {"g1", "g2"}

    assert extract_guideline_ids(known_ids=known, raw_used=" g1 ", feedback="") == [
        "g1"
    ]
    assert extract_guideline_ids(known_ids=known, raw_used={"g2"}, feedback="") == [
        "g2"
    ]

    # Unknown IDs are ignored; duplicates are de-duped.
    assert extract_guideline_ids(
        known_ids=known, raw_used=["g1", "bad", "g1"], feedback=""
    ) == ["g1"]

    # If `raw_used` doesn't parse, fall back to scanning `feedback` in textual order.
    assert extract_guideline_ids(
        known_ids=known,
        raw_used=123,
        feedback="prefix g2 suffix g1",
    ) == ["g2", "g1"]


def test_dspy_adapters_text_and_image_helpers(
    monkeypatch: pytest.MonkeyPatch, tmp_path
) -> None:
    request = RetrievalRequest(
        context=[
            TextItem(role="situation", text="S"),
            ImageItem(role="chart", uri="https://example.com/chart.png"),
        ]
    )

    assert dspy_adapters.get_text_by_role(request, "situation") == "S"
    assert dspy_adapters.get_text_by_role(request, "missing") is None
    assert dspy_adapters.require_text_by_role(request, "situation") == "S"
    with pytest.raises(ValueError, match="Missing required TextItem"):
        dspy_adapters.require_text_by_role(request, "missing")

    assert dspy_adapters.get_image_item_by_role(request, "chart") is not None
    assert dspy_adapters.get_image_item_by_role(request, "missing") is None
    assert dspy_adapters.require_image_item_by_role(request, "chart").role == "chart"
    with pytest.raises(ValueError, match="Missing required ImageItem"):
        dspy_adapters.require_image_item_by_role(request, "missing")

    # Make dspy.Image a pure identity so we can assert what gets passed in.
    monkeypatch.setattr(dspy_adapters.dspy, "Image", lambda x: x)

    # Data-bytes branch (avoid a hard pillow dependency by stubbing PIL.Image.open).
    class DummyPILImage:
        @staticmethod
        def open(_bio):  # noqa: ANN001
            return "pil-image"

    pil_pkg = types.ModuleType("PIL")
    setattr(pil_pkg, "Image", DummyPILImage)
    monkeypatch.setitem(sys.modules, "PIL", pil_pkg)

    assert dspy_adapters.image_item_to_dspy_image(ImageItem(data=b"123")) == "pil-image"

    with pytest.raises(ValueError, match="must have either `data`"):
        dspy_adapters.image_item_to_dspy_image(ImageItem())

    assert (
        dspy_adapters.image_item_to_dspy_image(ImageItem(uri="file:///tmp/x.png"))
        == "/tmp/x.png"
    )

    img_path = tmp_path / "img.png"
    img_path.write_bytes(b"img")
    assert dspy_adapters.image_item_to_dspy_image(ImageItem(uri=str(img_path))) == str(
        img_path
    )

    assert (
        dspy_adapters.image_item_to_dspy_image(
            ImageItem(uri="https://example.com/x.png")
        )
        == "https://example.com/x.png"
    )


def test_vector_index_text_source_description_variants() -> None:
    from chartcoach.embedding import (
        GuidelineAbstractTextSource,
        GuidelineFieldTextSource,
        SectionsTextSource,
    )

    meta = describe_text_source(SectionsTextSource(roles={"b", "a"}))
    assert meta["type"] == "sections"
    assert meta["roles"] == ["a", "b"]

    meta = describe_text_source(
        GuidelineFieldTextSource(field="title", role="headline")
    )
    assert meta["type"] == "guideline_field"
    assert meta["field"] == "title"
    assert meta["role"] == "headline"

    meta = describe_text_source(GuidelineAbstractTextSource(role="abstract"))
    assert meta["type"] == "guideline_abstract"
    assert meta["role"] == "abstract"

    meta = describe_text_source(object())
    assert meta["type"] == "object"


def test_catalog_vector_index_embed_query_and_search(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.embedding

    def fake_embed_text(
        df: pl.DataFrame, *, embedding_column: str = "embedding", **_kwargs
    ) -> pl.DataFrame:
        assert df.get_column("content").to_list() == ["Q"]
        return df.with_columns(pl.Series(name=embedding_column, values=[[0.25, 0.75]]))

    monkeypatch.setattr(chartcoach.embedding, "embed_text", fake_embed_text)

    catalog = Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="t",
                    description="d",
                    labels=[],
                    body="## Advice <!-- role: advice -->\nX\n",
                ),
                references=[],
            )
        ]
    )
    embedded_text_df = pl.DataFrame(
        {"id": ["g1"], "role": ["advice"], "content": ["X"], "embedding": [[1.0, 0.0]]}
    )
    index = InMemoryVectorIndexBackend().index(
        embedded_text_df.select("id", "role", "embedding")
    )
    vector_index = CatalogVectorIndex(
        catalog=catalog,
        sources=tuple(),
        config=EmbeddingConfig(model="fake"),
        embedded_text_df=embedded_text_df,
        index=index,
    )

    vec = vector_index.embed_query("Q")
    assert np.allclose(vec, np.array([0.25, 0.75]))

    hits = vector_index.search(np.array([1.0, 0.0]), k=1)
    assert hits["id"].to_list() == ["g1"]
