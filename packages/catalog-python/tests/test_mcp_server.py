from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import pytest

from chartcoach import Catalog, CatalogEntry, Guideline, Section
from chartcoach.mcp import server as mcp_server
from chartcoach.tools.catalog import CatalogTools


def _catalog() -> Catalog:
    return Catalog.from_entries(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line",),
                    sections=(
                        Section(
                            role="advice",
                            title="Advice",
                            content="Place labels near marks.",
                        ),
                    ),
                )
            )
        ]
    )


def test_mcp_settings_support_index_dir() -> None:
    config = mcp_server.resolve_config(
        source="catalog.parquet",
        index_dir="index",
    )

    assert config.settings == {
        "source": "catalog.parquet",
        "index_dir": Path("index"),
    }


def test_mcp_settings_use_default_index_dir() -> None:
    config = mcp_server.resolve_config(source="catalog.parquet")

    assert config.settings["source"] == "catalog.parquet"
    assert Path(config.settings["index_dir"]).name == "index"


def test_mcp_server_exposes_catalog_and_guideline_search(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    added_tools: dict[str, Any] = {}

    class FakeServer:
        def __init__(self) -> None:
            self.settings = SimpleNamespace(
                host=None,
                port=None,
                log_level=None,
            )

        def add_tool(self, tool: object, **kwargs: object) -> None:
            annotations = cast(Any, kwargs["annotations"])
            assert annotations.readOnlyHint is True
            assert annotations.destructiveHint is False
            assert annotations.idempotentHint is True
            assert annotations.openWorldHint is False
            added_tools[cast(str, kwargs["name"])] = annotations
            assert kwargs["description"]

    fake_server = FakeServer()

    def fake_fast_mcp(*_: object, **__: object) -> FakeServer:
        return fake_server

    monkeypatch.setattr(mcp_server, "_load_fast_mcp", lambda: fake_fast_mcp)

    class FakeGuidelineSearch:
        def search_guidelines(
            self, *args: object, **kwargs: object
        ) -> dict[str, object]:
            return {"rows": []}

        def chroma_query(self, *args: object, **kwargs: object) -> dict[str, object]:
            return {"ids": [[]]}

        def chroma_get(self, *args: object, **kwargs: object) -> dict[str, object]:
            return {"ids": []}

    catalog = _catalog()
    server = mcp_server._build_server(
        mcp_server.RuntimeConfig(
            transport="stdio",
            host="127.0.0.1",
            port=8000,
            log_level="INFO",
        ),
    )
    mcp_server._register_tools(
        server,
        catalog_tools=CatalogTools(catalog),
        artifact_tools=mcp_server._ArtifactTools(
            catalog,
            source="catalog.parquet",
            index_dir="index",
        ),
        search=FakeGuidelineSearch(),
    )

    assert server is fake_server
    assert set(added_tools) == {
        "catalog_artifacts",
        "tables_list",
        "tables_schema",
        "tables_values",
        "guidelines_list",
        "guidelines_get",
        "guidelines_retrieve",
        "guidelines_search",
        "chroma_query",
        "chroma_get",
    }


def test_mcp_main_registers_catalog_tools_without_opening_search(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source_path = tmp_path / "catalog.parquet"
    _catalog().write_parquet(source_path)
    added_tools: list[str] = []

    class FakeServer:
        def __init__(self) -> None:
            self.settings = SimpleNamespace(host=None, port=None, log_level=None)

        def add_tool(self, tool: object, **_: object) -> None:
            added_tools.append(getattr(tool, "__name__"))

        def run(self, *, transport: str) -> None:
            assert transport == "stdio"

    fake_server = FakeServer()
    monkeypatch.setattr(
        mcp_server,
        "_load_fast_mcp",
        lambda: lambda *_, **__: fake_server,
    )
    monkeypatch.setattr(
        mcp_server.ChromaIndex,
        "from_cache",
        staticmethod(
            lambda *_args, **_kwargs: (_ for _ in ()).throw(
                AssertionError("search cache should open lazily")
            )
        ),
    )

    mcp_server.main(settings={"source": source_path}, runtime=mcp_server.RuntimeConfig())

    assert "list_tables" in added_tools
    assert "describe_tables" in added_tools
    assert "count_values" in added_tools
    assert "list_guidelines" in added_tools
    assert "retrieve_guidelines" in added_tools
    assert "catalog_artifacts" in added_tools
    assert "search_guidelines" in added_tools
    assert "chroma_query" in added_tools
    assert "chroma_get" in added_tools


def test_chroma_mcp_tools_pass_native_params() -> None:
    class FakeCollection:
        def __init__(self) -> None:
            self.query_params: dict[str, Any] | None = None
            self.get_params: dict[str, Any] | None = None

        def query(self, **params: object) -> dict[str, object]:
            self.query_params = dict(params)
            return {"ids": [["doc"]]}

        def get(self, **params: object) -> dict[str, object]:
            self.get_params = dict(params)
            return {"ids": ["doc"]}

    collection = FakeCollection()
    search = mcp_server._ChromaTools(
        _catalog(),
        cache_dir="index",
        cache_mode="reuse_only",
    )
    cast(Any, search)._index = SimpleNamespace(collection=collection)

    assert search.chroma_query(
        query_texts=["axis", "labels"],
        n_results=2,
        include=["documents"],
    ) == {"ids": [["doc"]]}
    assert search.chroma_get(ids=["doc"], include=["metadatas"]) == {"ids": ["doc"]}
    assert collection.query_params == {
        "query_texts": ["axis", "labels"],
        "n_results": 2,
        "include": ["documents"],
    }
    assert collection.get_params == {"ids": ["doc"], "include": ["metadatas"]}
