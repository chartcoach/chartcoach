from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

import polars as pl

from chartcoach.catalog import Catalog


@dataclass(frozen=True)
class TextItem:
    kind: Literal["text"] = "text"
    role: str = "note"
    text: str = ""
    lang: str | None = None


@dataclass(frozen=True)
class ImageItem:
    kind: Literal["image"] = "image"
    role: str = "chart"
    uri: str | None = None
    mime: str | None = None
    data: bytes | None = None


@dataclass(frozen=True)
class TableItem:
    kind: Literal["table"] = "table"
    role: str = "dataset"
    df: pl.DataFrame | None = None
    uri: str | None = None
    mime: str | None = None


@dataclass(frozen=True)
class FileItem:
    kind: Literal["file"] = "file"
    role: str = "attachment"
    uri: str | None = None
    mime: str | None = None
    data: bytes | None = None


ContextItem = TextItem | ImageItem | TableItem | FileItem


@dataclass(frozen=True)
class RetrievalRequest:
    """Context-first retrieval request with lean metadata.

    This is intentionally general: all inputs (query text, intent, chart, dataset, etc.)
    should be provided as context items.
    """

    context: list[ContextItem] = field(default_factory=list)
    lang: str = "en"
    meta: dict[str, object] = field(default_factory=dict)
    k: int = 10


@dataclass(frozen=True)
class RetrievalResponse:
    """Retrieved guidelines (as a sub-catalog) plus lean telemetry metadata."""

    catalog: Catalog
    meta: dict[str, object] = field(default_factory=dict)
