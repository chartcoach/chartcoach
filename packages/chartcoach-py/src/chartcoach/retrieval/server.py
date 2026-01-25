from __future__ import annotations

import base64
import inspect
import os
from pathlib import Path
from typing import Any, Literal, cast

import dspy
import polars as pl
from pydantic import BaseModel, Field

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy import RetrievalStrategy
from chartcoach.retrieval.types import (
    FileItem,
    ImageItem,
    RetrievalRequest,
    RetrievalResponse,
    TableItem,
    TextItem,
)


class TextItemIn(BaseModel):
    kind: Literal["text"] = "text"
    role: str = "note"
    text: str = ""
    lang: str | None = None


class ImageItemIn(BaseModel):
    kind: Literal["image"] = "image"
    role: str = "chart"
    uri: str | None = None
    mime: str | None = None
    data_b64: str | None = Field(
        default=None,
        description="Base64-encoded binary image payload. Prefer `uri` for large payloads.",
    )


class TableItemIn(BaseModel):
    kind: Literal["table"] = "table"
    role: str = "dataset"
    uri: str | None = None
    mime: str | None = None


class FileItemIn(BaseModel):
    kind: Literal["file"] = "file"
    role: str = "attachment"
    uri: str | None = None
    mime: str | None = None
    data_b64: str | None = None


ContextItemIn = TextItemIn | ImageItemIn | TableItemIn | FileItemIn


class RetrievalRequestIn(BaseModel):
    context: list[ContextItemIn] = Field(default_factory=list)
    lang: str = "en"
    meta: dict[str, object] = Field(default_factory=dict)
    k: int = 10


class StrategyInfo(BaseModel):
    id: str
    name: str
    description: str


class RetrievalResponseOut(BaseModel):
    catalog: list[dict[str, Any]]
    meta: dict[str, object]


class _BadRequest(ValueError):
    pass


def _decode_b64(data_b64: str) -> bytes:
    try:
        return base64.b64decode(data_b64, validate=True)
    except Exception as e:  # noqa: BLE001
        raise _BadRequest("Invalid base64 payload.") from e


def _to_request(req: RetrievalRequestIn) -> RetrievalRequest:
    context = []
    for item in req.context:
        if item.kind == "text":
            item = cast(TextItemIn, item)
            context.append(
                TextItem(
                    role=item.role,
                    text=item.text,
                    lang=item.lang,
                )
            )
        elif item.kind == "image":
            item = cast(ImageItemIn, item)
            context.append(
                ImageItem(
                    role=item.role,
                    uri=item.uri,
                    mime=item.mime,
                    data=_decode_b64(item.data_b64)
                    if item.data_b64 is not None
                    else None,
                )
            )
        elif item.kind == "table":
            item = cast(TableItemIn, item)
            context.append(
                TableItem(
                    role=item.role,
                    uri=item.uri,
                    mime=item.mime,
                    df=None,
                )
            )
        elif item.kind == "file":
            item = cast(FileItemIn, item)
            context.append(
                FileItem(
                    role=item.role,
                    uri=item.uri,
                    mime=item.mime,
                    data=_decode_b64(item.data_b64)
                    if item.data_b64 is not None
                    else None,
                )
            )
        else:
            raise _BadRequest(f"Unknown context kind: {item.kind}")

    return RetrievalRequest(
        context=context,
        lang=req.lang,
        meta=dict(req.meta),
        k=req.k,
    )


def _catalog_from_path(path: str) -> Catalog:
    if path.endswith(".parquet"):
        return Catalog.from_df(pl.read_parquet(path))
    return Catalog.from_disk(Path(path))


def _walk_subclasses(cls: type[RetrievalStrategy]) -> list[type[RetrievalStrategy]]:
    out: list[type[RetrievalStrategy]] = []
    queue: list[type[RetrievalStrategy]] = [cls]
    while queue:
        parent = queue.pop()
        for child in parent.__subclasses__():
            out.append(child)
            queue.append(child)
    return out


def list_strategy_classes() -> list[type[RetrievalStrategy]]:
    """
    Return all registered RetrievalStrategy subclasses.

    Strategy classes are discovered via subclass traversal; importing concrete strategy
    modules is required so they register themselves.
    """
    from chartcoach.retrieval import guideline_browser as _  # noqa: F401

    strategy_classes = _walk_subclasses(RetrievalStrategy)
    seen: set[str] = set()
    unique: list[type[RetrievalStrategy]] = []
    for cls in sorted(strategy_classes, key=lambda c: getattr(c, "id", c.__name__)):
        strategy_id = getattr(cls, "id", None)
        if not isinstance(strategy_id, str) or not strategy_id:
            continue
        if strategy_id in seen:
            continue
        seen.add(strategy_id)
        unique.append(cls)
    return unique


def create_app(*, catalog: Catalog, lm: dspy.LM) -> Any:
    try:
        from fastapi import APIRouter, FastAPI, HTTPException
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Install `chartcoach[retrieval-server]` to use the API server."
        ) from e

    strategies_by_id: dict[str, type[RetrievalStrategy]] = {
        cls.id: cls for cls in list_strategy_classes()
    }

    router = APIRouter(prefix="/v1")

    @router.get("/strategies", response_model=list[StrategyInfo])
    def get_strategies() -> list[StrategyInfo]:
        out: list[StrategyInfo] = []
        for cls in strategies_by_id.values():
            doc = inspect.getdoc(cls) or ""
            out.append(
                StrategyInfo(
                    id=cls.id,
                    name=cls.__name__,
                    description=doc.splitlines()[0] if doc else "",
                )
            )
        return sorted(out, key=lambda s: s.id)

    @router.post("/strategies/{strategy_id}", response_model=RetrievalResponseOut)
    def run_strategy(strategy_id: str, req: RetrievalRequestIn) -> RetrievalResponseOut:
        strategy_cls = strategies_by_id.get(strategy_id)
        if strategy_cls is None:
            raise HTTPException(status_code=404, detail="Unknown strategy id.")

        try:
            strategy = cast(Any, strategy_cls)(catalog=catalog, lm=lm)
            out: RetrievalResponse = strategy(request=_to_request(req))
        except _BadRequest as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
        return RetrievalResponseOut(
            catalog=[entry.model_dump() for entry in out.catalog.entries],
            meta=dict(out.meta),
        )

    app = FastAPI(title="ChartCoach Retrieval Server", version="0.1.0")
    app.include_router(router)
    return app


def create_app_from_env() -> Any:
    catalog_path = os.environ.get("CHARTCOACH_CATALOG_PATH")
    if not catalog_path:
        raise RuntimeError(
            "Set CHARTCOACH_CATALOG_PATH to a catalog folder or .parquet file."
        )

    model = os.environ.get("CHARTCOACH_MODEL")
    api_base = os.environ.get("OPENAI_BASE_URL")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not model or not api_base or not api_key:
        raise RuntimeError("Set CHARTCOACH_MODEL, OPENAI_BASE_URL, and OPENAI_API_KEY.")

    lm = dspy.LM(model=model, api_base=api_base, api_key=api_key)
    return create_app(catalog=_catalog_from_path(catalog_path), lm=lm)
