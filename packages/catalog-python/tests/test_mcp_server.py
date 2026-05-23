from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import pytest

from chartcoach import Catalog, CatalogEntry, Guideline
from chartcoach.mcp import server as mcp_server
from chartcoach.search.registry import tool_specs
from chartcoach.tools.catalog import CatalogTools


def _catalog() -> Catalog:
    return Catalog(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line",),
                )
            )
        ]
    )


def test_mcp_settings_support_cache_mode() -> None:
    config = mcp_server.resolve_config(
        catalog="catalog.parquet",
        cache_dir="cache",
        cache_mode="reuse_only",
    )

    assert config.settings == {
        "catalog": "catalog.parquet",
        "cache_dir": Path("cache"),
        "cache_mode": "reuse_only",
    }

    with pytest.raises(ValueError, match="Unsupported MCP cache mode"):
        mcp_server.resolve_config(cache_mode="bad")
    with pytest.raises(ValueError, match="only supports --cache-mode reuse_only"):
        mcp_server.resolve_config(cache_mode="reuse_or_create")
    with pytest.raises(ValueError, match="only supports --cache-mode reuse_only"):
        mcp_server.resolve_config(cache_mode="force_rebuild")


def test_mcp_server_exposes_shared_catalog_and_search_tools(
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
            added_tools[getattr(tool, "__name__")] = annotations

    fake_server = FakeServer()

    def fake_fast_mcp(*_: object, **__: object) -> FakeServer:
        return fake_server

    monkeypatch.setattr(mcp_server, "_load_fast_mcp", lambda: fake_fast_mcp)

    class FakeSqlTools:
        def sql(self, *args: object, **kwargs: object) -> dict[str, object]:
            return {"rows": []}

    class FakeSearchTools:
        def search(self, *args: object, **kwargs: object) -> dict[str, object]:
            return {"ids": []}

        def search_guidelines(
            self, *args: object, **kwargs: object
        ) -> dict[str, object]:
            return {"rows": []}

        def get(self, *args: object, **kwargs: object) -> dict[str, object]:
            return {"ids": []}

    catalog = _catalog()
    specs = tool_specs(
        catalog_tools=CatalogTools(catalog),
        sql_tools=FakeSqlTools(),
        search_tools=FakeSearchTools(),
    )

    server = mcp_server._build_server(
        specs,
        mcp_server.RuntimeConfig(
            transport="stdio",
            host="127.0.0.1",
            port=8000,
            log_level="INFO",
        ),
    )

    assert server is fake_server
    assert set(added_tools) == {
        "relations",
        "schema",
        "values",
        "list_guidelines",
        "get_guideline",
        "retrieve_guidelines",
        "sql",
        "search",
        "search_guidelines",
        "get",
    }


def test_mcp_main_registers_catalog_tools_without_opening_search(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    catalog_path = tmp_path / "catalog.parquet"
    _catalog().write_parquet(catalog_path)
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
        mcp_server,
        "open_search_session",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("search cache should open lazily")
        ),
    )

    mcp_server.main(
        settings={"catalog": catalog_path, "cache_mode": "reuse_only"},
        runtime=mcp_server.RuntimeConfig(),
    )

    assert "relations" in added_tools
    assert "search_guidelines" in added_tools
