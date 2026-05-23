from __future__ import annotations

import dataclasses as dc
from collections.abc import Callable
from typing import Any, Protocol

from ..tools.catalog import CatalogTools


@dc.dataclass(frozen=True)
class ToolSafety:
    read_only: bool = True
    destructive: bool = False
    idempotent: bool = True
    open_world: bool = False


@dc.dataclass(frozen=True)
class ToolSpec:
    func: Callable[..., Any]
    safety: ToolSafety = ToolSafety()


class SqlToolSurface(Protocol):
    def sql(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...


class SearchToolSurface(Protocol):
    def search(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...

    def search_guidelines(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...

    def get(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...


def tool_specs(
    *,
    catalog_tools: CatalogTools,
    sql_tools: SqlToolSurface,
    search_tools: SearchToolSurface,
) -> tuple[ToolSpec, ...]:
    """Return the public tool surface shared by MCP and other transports."""

    return tuple(
        ToolSpec(func=tool)
        for tool in (
            catalog_tools.relations,
            catalog_tools.schema,
            catalog_tools.values,
            catalog_tools.list_guidelines,
            catalog_tools.get_guideline,
            catalog_tools.retrieve_guidelines,
            sql_tools.sql,
            search_tools.search,
            search_tools.search_guidelines,
            search_tools.get,
        )
    )


__all__ = [
    "SearchToolSurface",
    "SqlToolSurface",
    "ToolSafety",
    "ToolSpec",
    "tool_specs",
]
