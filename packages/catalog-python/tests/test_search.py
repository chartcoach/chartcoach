from __future__ import annotations

from pathlib import Path
import sys
from types import SimpleNamespace
from typing import TYPE_CHECKING, cast

import pytest

from chartcoach import Catalog

pytestmark = pytest.mark.search

if TYPE_CHECKING:
    from lancedb import Table
    from lancedb.embeddings import EmbeddingFunction


def _embedding_vector(text: str) -> list[float]:
    lowered = text.lower()
    return [
        1.0 if "direct" in lowered else 0.0,
        1.0 if "label" in lowered else 0.0,
        1.0 if "axis" in lowered else 0.0,
        1.0 if "bar" in lowered else 0.0,
    ]


def _test_embedding() -> "EmbeddingFunction":
    registry_module = pytest.importorskip("lancedb.embeddings")
    TextEmbeddingFunction = pytest.importorskip(
        "lancedb.embeddings.base"
    ).TextEmbeddingFunction

    registry = registry_module.get_registry()
    try:
        embedding_class = registry.get("chartcoach-test-embedding")
    except Exception:

        @registry.register("chartcoach-test-embedding")
        class chartcoachTestEmbedding(TextEmbeddingFunction):
            def ndims(self) -> int:
                return 4

            def generate_embeddings(
                self,
                texts: list[str],
            ) -> list[list[float]]:
                return [_embedding_vector(text) for text in texts]

        embedding_class = chartcoachTestEmbedding

    return cast("EmbeddingFunction", embedding_class.create())


def test_documents_return_lancedb_document_rows(sample_catalog: Catalog) -> None:
    from chartcoach.search.lance import documents

    frame = documents(sample_catalog)

    assert frame.columns == [
        "id",
        "parent_id",
        "role",
        "labels",
        "content_hash",
        "text",
    ]
    rows = frame.filter(frame["id"] == "direct-labels---overview").to_dicts()
    assert rows == [
        {
            "id": "direct-labels---overview",
            "parent_id": "direct-labels",
            "role": "overview",
            "labels": ["chart:line", "component:label", "task:lookup"],
            "content_hash": rows[0]["content_hash"],
            "text": "Use direct labels\n\nLabel marks directly when space permits.",
        }
    ]
    assert isinstance(rows[0]["content_hash"], str)


def test_model_uses_lancedb_embedding_metadata(tmp_path: Path) -> None:
    import lancedb
    from chartcoach.search import model

    schema = model(_test_embedding())
    db = lancedb.connect(tmp_path / "index")
    table = db.create_table("docs", schema=schema)
    table.add(
        [
            {
                "id": "direct-labels---overview",
                "parent_id": "direct-labels",
                "role": "overview",
                "labels": ["chart:line"],
                "content_hash": "hash",
                "text": "direct labels",
            }
        ]
    )

    assert table.embedding_functions
    rows = table.search("direct labels", query_type="vector").limit(1).to_list()
    assert rows[0]["id"] == "direct-labels---overview"


def test_index_returns_native_table_and_open_reads_it(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.search import index, open as open_index

    path = tmp_path / "index"
    table = index(sample_catalog, path, table_name="docs")
    opened = open_index(path, table_name="docs")

    assert table.name == "docs"
    assert opened.name == "docs"
    assert opened.count_rows() == table.count_rows()
    rows = (
        opened.search(
            "direct labels",
            query_type="fts",
            fts_columns="text",
        )
        .limit(2)
        .to_list()
    )
    assert rows[0]["parent_id"] == "direct-labels"


def test_chartcoach_facade_exposes_catalog_index_and_native_table(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    import chartcoach
    from chartcoach.search import index

    index_path = tmp_path / "index"
    index(sample_catalog, index_path)
    cc = chartcoach.open(catalog=sample_catalog, index=index_path)

    rows = cc.index.query(
        "direct labels",
        limit=1,
        where="role = 'overview'",
        mode="fts",
    )
    hits = cc.search(
        "direct labels",
        limit=1,
        where="role = 'overview'",
        mode="fts",
    )

    assert cc.catalog is sample_catalog
    assert cc.index.path == index_path
    assert cc.index.table.name == "catalog_documents"
    assert not hasattr(cc.index, "search")
    assert rows[0]["parent_id"] == "direct-labels"
    assert hits.rows[0].guideline_id == "direct-labels"


def test_chartcoach_search_validates_index_once(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach
    import chartcoach.facade as facade
    from chartcoach.search import index

    index_path = tmp_path / "index"
    index(sample_catalog, index_path)
    calls = 0

    def validate(catalog: Catalog, table: object) -> None:
        nonlocal calls
        assert catalog is sample_catalog
        assert getattr(table, "name") == "catalog_documents"
        calls += 1

    monkeypatch.setattr(facade, "validate_table_documents", validate)
    cc = chartcoach.open(catalog=sample_catalog, index=index_path)

    for _ in range(2):
        result = cc.search(
            "direct labels",
            limit=1,
            where="role = 'overview'",
            mode="fts",
        )
        assert result.rows[0].guideline_id == "direct-labels"

    assert calls == 1


def test_chartcoach_facade_resolves_default_index_path_for_default_catalog(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.facade as facade

    calls: dict[str, object] = {}

    class FakeTable:
        name = "docs"

    def default_path(
        *,
        table_name: str,
        reporter: object,
    ) -> Path:
        calls["table_name"] = table_name
        calls["reporter"] = reporter
        return tmp_path / "default-index"

    def open_index(uri: object, *, table_name: str) -> FakeTable:
        calls["uri"] = uri
        calls["opened_table"] = table_name
        return FakeTable()

    monkeypatch.setattr(facade, "default_index_path", default_path)
    monkeypatch.setattr(facade, "open_lance_index", open_index)
    monkeypatch.setattr(
        facade,
        "open_catalog",
        lambda source, *, reporter: sample_catalog,
    )

    chartcoach = facade.open(table_name="docs")

    assert chartcoach.index.path == tmp_path / "default-index"
    assert chartcoach.index.table.name == "docs"
    assert calls == {
        "table_name": "docs",
        "reporter": None,
        "uri": tmp_path / "default-index",
        "opened_table": "docs",
    }


def test_chartcoach_facade_requires_index_for_injected_catalog(
    sample_catalog: Catalog,
) -> None:
    import chartcoach

    cc = chartcoach.open(catalog=sample_catalog)

    with pytest.raises(ValueError, match="Pass index=.*custom catalog"):
        _ = cc.index.table


def test_chartcoach_facade_requires_index_for_custom_source(
    sample_catalog_path: Path,
) -> None:
    import chartcoach

    cc = chartcoach.open(sample_catalog_path)

    with pytest.raises(ValueError, match="Pass index=.*custom catalog"):
        _ = cc.index.table


def test_chartcoach_facade_accepts_injected_table_without_index_path(
    sample_catalog: Catalog,
) -> None:
    import chartcoach

    class FakeTable:
        name = "catalog_documents"

    table = cast("Table", FakeTable())
    cc = chartcoach.open(catalog=sample_catalog, table=table)

    assert cc.index.table is table
    with pytest.raises(ValueError, match="Pass index=.*custom catalog"):
        _ = cc.index.location


def test_catalog_index_path_accepts_windows_drive_strings(
    sample_catalog: Catalog,
) -> None:
    from chartcoach.facade import CatalogIndex

    assert CatalogIndex(sample_catalog, location="C:\\index").path == Path("C:\\index")
    assert CatalogIndex(sample_catalog, location="D:/index").path == Path("D:/index")


def test_catalog_index_path_rejects_remote_uri(
    sample_catalog: Catalog,
) -> None:
    from chartcoach.facade import CatalogIndex

    index = CatalogIndex(sample_catalog, location="s3://bucket/index")

    with pytest.raises(ValueError, match="URI-backed"):
        _ = index.path


def test_chartcoach_open_rejects_source_and_catalog(
    sample_catalog: Catalog,
) -> None:
    import chartcoach

    with pytest.raises(ValueError, match="Pass source or catalog, not both"):
        chartcoach.open("catalog.parquet", catalog=sample_catalog)


def test_index_passes_remote_uri_to_lancedb(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.search.lance as lance

    captured: dict[str, object] = {}

    class FakeTable:
        name = "catalog_documents"

        def create_fts_index(self, column: str, *, replace: bool) -> None:
            captured["fts"] = (column, replace)

    class FakeDB:
        def create_table(self, name: str, *args: object, **kwargs: object) -> FakeTable:
            captured["table"] = name
            captured["mode"] = kwargs["mode"]
            return FakeTable()

    def connect(uri: object) -> FakeDB:
        captured["uri"] = uri
        return FakeDB()

    monkeypatch.setitem(sys.modules, "lancedb", SimpleNamespace(connect=connect))
    monkeypatch.chdir(tmp_path)

    table = lance.index(sample_catalog, "s3://bucket/chartcoach-index")

    assert table.name == "catalog_documents"
    assert captured["uri"] == "s3://bucket/chartcoach-index"
    assert captured["table"] == "catalog_documents"
    assert captured["mode"] == "overwrite"
    assert captured["fts"] == ("text", True)

    lance.index(sample_catalog, "~/chartcoach-index")

    assert captured["uri"] == "~/chartcoach-index"
    assert not (tmp_path / "~").exists()


def test_index_uses_lancedb_embedding_function(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.search import index, query
    from chartcoach.search.index import search

    table = index(
        sample_catalog,
        tmp_path / "index",
        embedding=_test_embedding(),
    )

    assert table.embedding_functions
    rows = table.search("direct labels", query_type="vector").limit(1).to_list()
    assert rows[0]["parent_id"] == "direct-labels"
    vector_rows = (
        table.search([1.0, 1.0, 0.0, 0.0], query_type="vector").limit(1).to_list()
    )
    assert vector_rows[0]["parent_id"] == "direct-labels"
    raw_rows = query(table, "direct labels", mode="vector", limit=1)
    assert "vector" not in raw_rows[0]
    assert "_distance" in raw_rows[0]
    result = search(sample_catalog, table, "direct labels", mode="vector")
    assert result.rows[0].score is not None


def test_query_returns_bounded_raw_document_rows(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.search import index, query

    table = index(sample_catalog, tmp_path / "index")
    rows = query(
        table,
        "direct labels",
        limit=1,
        where="role = 'overview'",
        mode="fts",
    )

    assert rows == [
        {
            "_score": rows[0]["_score"],
            "id": "direct-labels---overview",
            "parent_id": "direct-labels",
            "role": "overview",
            "labels": ["chart:line", "component:label", "task:lookup"],
            "content_hash": rows[0]["content_hash"],
            "text": "Use direct labels\n\nLabel marks directly when space permits.",
        }
    ]


def test_query_fts_mode_does_not_parse_embedding_metadata() -> None:
    from chartcoach.search import query

    class FakeSearch:
        def limit(self, _limit: int) -> "FakeSearch":
            return self

        def to_list(self) -> list[dict[str, object]]:
            return [
                {
                    "id": "direct-labels---overview",
                    "parent_id": "direct-labels",
                    "role": "overview",
                    "labels": ["chart:line"],
                    "content_hash": "hash",
                    "text": "direct labels",
                }
            ]

    class FakeTable:
        name = "catalog_documents"

        @property
        def embedding_functions(self) -> object:
            raise ValueError("embedding metadata should not be parsed for FTS")

        def search(self, *_args: object, **kwargs: object) -> FakeSearch:
            assert kwargs["query_type"] == "fts"
            return FakeSearch()

    rows = query(cast("Table", FakeTable()), "direct labels", mode="fts")

    assert rows[0]["id"] == "direct-labels---overview"


def test_query_auto_mode_falls_back_to_fts_when_embedding_metadata_is_unavailable() -> (
    None
):
    from chartcoach.search import query

    class FakeSearch:
        def limit(self, _limit: int) -> "FakeSearch":
            return self

        def to_list(self) -> list[dict[str, object]]:
            return [
                {
                    "id": "direct-labels---overview",
                    "parent_id": "direct-labels",
                    "role": "overview",
                    "labels": ["chart:line"],
                    "content_hash": "hash",
                    "text": "direct labels",
                }
            ]

    class FakeTable:
        name = "catalog_documents"

        @property
        def embedding_functions(self) -> object:
            raise ValueError("Variable 'openrouter_api_key' not found in registry")

        def search(self, *_args: object, **kwargs: object) -> FakeSearch:
            assert kwargs["query_type"] == "fts"
            return FakeSearch()

    rows = query(cast("Table", FakeTable()), "direct labels", mode="auto")

    assert rows[0]["id"] == "direct-labels---overview"


def test_query_rejects_empty_text_and_invalid_limits(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.search import index, query

    table = index(sample_catalog, tmp_path / "index")

    with pytest.raises(ValueError, match="query must be a non-empty string"):
        query(table, " ")
    with pytest.raises(ValueError, match="limit must be at least 1"):
        query(table, "axis", limit=0)


def test_query_explains_hybrid_mode_on_full_text_index(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.search import index, query

    table = index(sample_catalog, tmp_path / "index")

    with pytest.raises(ValueError, match="--mode fts"):
        query(table, "axis", mode="hybrid")


def test_search_returns_guideline_level_hits(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.search import index
    from chartcoach.search.index import search

    table = index(sample_catalog, tmp_path / "index")
    result = search(
        sample_catalog,
        table,
        "zero",
        where="role = 'section.advice'",
        mode="fts",
    )

    assert result.row_count == 1
    assert result.to_dict()["rows"] == [
        {
            "rank": 1,
            "id": "full-axis-bars",
            "title": "Use full value axes for bars",
            "description": "Keep bar axes on the honest baseline.",
            "labels": ["chart:bar", "component:axis"],
            "matched_document_id": "full-axis-bars---role---advice",
            "matched_role": "section.advice",
            "score": result.rows[0].score,
            "matched_text": "Start bar value axes at zero.",
        }
    ]


def test_search_rejects_rows_that_do_not_match_catalog(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.search import index
    from chartcoach.search.index import search

    table = index(sample_catalog, tmp_path / "index")
    stale_record = dict(sample_catalog.entry("full-axis-bars"))
    stale_record["labels"] = ["chart:bar", "component:axis", "review:updated"]
    current_catalog = Catalog.from_entries(
        [
            sample_catalog.entry("direct-labels"),
            stale_record,
        ]
    )

    with pytest.raises(ValueError, match="do not match the current catalog"):
        search(
            current_catalog,
            table,
            "zero",
            where="role = 'section.advice'",
            mode="fts",
        )


def test_search_rejects_malformed_lancedb_rows(sample_catalog: Catalog) -> None:
    from chartcoach.search.index import search
    from chartcoach.search.lance import documents

    catalog_documents = documents(sample_catalog)

    class FakeQuery:
        def select(self, _columns: list[str]) -> "FakeQuery":
            return self

        def where(self, _where: str) -> "FakeQuery":
            return self

        def limit(self, _limit: int) -> "FakeQuery":
            return self

        def to_list(self) -> list[dict[str, object]]:
            return [{"id": "broken", "role": "overview", "text": "missing parent"}]

    class FakeTable:
        embedding_functions: dict[str, object] = {}

        def count_rows(self) -> int:
            return 1

        def to_arrow(self) -> object:
            return catalog_documents.to_arrow()

        def search(self, *_args: object, **_kwargs: object) -> FakeQuery:
            return FakeQuery()

    with pytest.raises(ValueError, match="parent_id"):
        search(sample_catalog, cast("Table", FakeTable()), "axis")
