from __future__ import annotations

import base64
import sys
from types import ModuleType
from typing import Any

import dspy
import polars as pl
import pytest

from chartcoach.catalog import Catalog, CatalogEntry, Guideline
from chartcoach.retrieval.server import (
    RetrievalRequestIn,
    _BadRequest,
    _catalog_from_path,
    _decode_b64,
    _to_request,
    create_app,
    create_app_from_env,
    list_strategy_classes,
)
from chartcoach.retrieval.strategy import RetrievalStrategy
from chartcoach.retrieval.types import RetrievalRequest, RetrievalResponse


def test_decode_b64_valid_and_invalid() -> None:
    assert _decode_b64(base64.b64encode(b"hi").decode("ascii")) == b"hi"
    with pytest.raises(_BadRequest):
        _decode_b64("not base64")


def test_to_request_converts_context_items_and_rejects_unknown_kind() -> None:
    req = _to_request(
        RetrievalRequestIn(
            context=[
                {"kind": "text", "role": "situation", "text": "S"},
                {
                    "kind": "image",
                    "role": "chart",
                    "mime": "image/png",
                    "data_b64": base64.b64encode(b"png").decode("ascii"),
                },
                {"kind": "table", "role": "dataset", "uri": "file://x.csv"},
                {
                    "kind": "file",
                    "role": "attachment",
                    "mime": "text/plain",
                    "data_b64": base64.b64encode(b"x").decode("ascii"),
                },
            ],
            lang="en",
            meta={"x": 1},
            k=3,
        )
    )
    assert isinstance(req, RetrievalRequest)
    assert req.lang == "en"
    assert req.meta["x"] == 1
    assert req.k == 3
    assert len(req.context) == 4

    class _Weird:
        kind = "weird"

    class _Req:
        context = [_Weird()]
        lang = "en"
        meta: dict[str, object] = {}
        k = 10

    with pytest.raises(_BadRequest):
        _to_request(_Req())  # type: ignore[arg-type]


def test_catalog_from_path_parquet_and_folder_branch(tmp_path) -> None:
    df = pl.DataFrame(
        [
            {
                "id": "g1",
                "guideline": {
                    "id": "g1",
                    "title": "T",
                    "description": "D",
                    "labels": [],
                    "body": "B",
                    "bibliography": None,
                },
                "references": [],
            }
        ]
    )
    parquet_path = tmp_path / "catalog.parquet"
    df.write_parquet(parquet_path)
    cat = _catalog_from_path(str(parquet_path))
    assert isinstance(cat, Catalog)
    assert len(cat) == 1
    assert cat.entries[0].guideline.id == "g1"

    with pytest.raises(Exception):  # noqa: BLE001
        _catalog_from_path(str(tmp_path / "missing_folder"))


def test_list_strategy_classes_filters_invalid_and_duplicate_ids() -> None:
    class _EmptyId(RetrievalStrategy):
        id = ""

        def __init__(self, *, catalog: Catalog, lm: dspy.LM) -> None:  # noqa: ARG002
            super().__init__(catalog)

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            return RetrievalResponse(catalog=Catalog(entries=[]))

    class _DupId(RetrievalStrategy):
        id = "guideline-browser@v0"

        def __init__(self, *, catalog: Catalog, lm: dspy.LM) -> None:  # noqa: ARG002
            super().__init__(catalog)

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            return RetrievalResponse(catalog=Catalog(entries=[]))

    ids = [cls.id for cls in list_strategy_classes()]
    assert "guideline-browser@v0" in ids
    assert "" not in ids
    assert ids.count("guideline-browser@v0") == 1


def test_create_app_and_env_factory_with_fastapi_stub(tmp_path, monkeypatch) -> None:
    class HTTPException(Exception):
        def __init__(self, status_code: int, detail: str) -> None:
            super().__init__(detail)
            self.status_code = status_code
            self.detail = detail

    class APIRouter:
        def __init__(self, *, prefix: str = "") -> None:
            self.prefix = prefix
            self.routes: list[dict[str, Any]] = []

        def get(self, path: str, *, response_model: object | None = None):
            def decorator(fn):
                self.routes.append(
                    {
                        "method": "GET",
                        "path": self.prefix + path,
                        "endpoint": fn,
                        "response_model": response_model,
                    }
                )
                return fn

            return decorator

        def post(self, path: str, *, response_model: object | None = None):
            def decorator(fn):
                self.routes.append(
                    {
                        "method": "POST",
                        "path": self.prefix + path,
                        "endpoint": fn,
                        "response_model": response_model,
                    }
                )
                return fn

            return decorator

    class FastAPI:
        def __init__(self, *, title: str, version: str) -> None:  # noqa: ARG002
            self.routers: list[APIRouter] = []

        def include_router(self, router: APIRouter) -> None:
            self.routers.append(router)

    fastapi_stub = ModuleType("fastapi")
    fastapi_stub.APIRouter = APIRouter
    fastapi_stub.FastAPI = FastAPI
    fastapi_stub.HTTPException = HTTPException
    monkeypatch.setitem(sys.modules, "fastapi", fastapi_stub)

    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v0"

        def __init__(self, *, catalog: Catalog, lm: dspy.LM) -> None:  # noqa: ARG002
            super().__init__(catalog)

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            return RetrievalResponse(
                catalog=Catalog(
                    entries=[
                        CatalogEntry(
                            guideline=Guideline(
                                id="g1",
                                title="T",
                                description="D",
                                labels=[],
                                body="B",
                            ),
                            references=[],
                        )
                    ]
                ),
                meta={"ok": True},
            )

    app = create_app(
        catalog=Catalog(entries=[]), lm=dspy.LM(model="m", api_base="b", api_key="k")
    )
    assert isinstance(app, FastAPI)
    assert len(app.routers) == 1
    router = app.routers[0]

    get_strategies = next(r for r in router.routes if r["method"] == "GET")["endpoint"]
    strategies = get_strategies()
    assert any(s.id == DummyStrategy.id for s in strategies)

    run_route = next(r for r in router.routes if r["method"] == "POST")["endpoint"]
    out = run_route(
        "dummy@v0",
        RetrievalRequestIn(
            context=[{"kind": "text", "role": "situation", "text": "S"}]
        ),
    )
    assert out.meta["ok"] is True
    assert len(out.catalog) == 1
    assert out.catalog[0]["guideline"]["id"] == "g1"

    with pytest.raises(HTTPException) as e:
        run_route("missing@v0", RetrievalRequestIn())
    assert e.value.status_code == 404

    with pytest.raises(HTTPException) as e2:
        run_route(
            "dummy@v0",
            RetrievalRequestIn(
                context=[
                    {
                        "kind": "image",
                        "role": "chart",
                        "mime": "image/png",
                        "data_b64": "not base64",
                    }
                ]
            ),
        )
    assert e2.value.status_code == 400

    df = pl.DataFrame(
        [
            {
                "id": "g1",
                "guideline": {
                    "id": "g1",
                    "title": "T",
                    "description": "D",
                    "labels": [],
                    "body": "B",
                    "bibliography": None,
                },
                "references": [],
            }
        ]
    )
    parquet_path = tmp_path / "catalog.parquet"
    df.write_parquet(parquet_path)
    monkeypatch.setenv("CHARTCOACH_CATALOG_PATH", str(parquet_path))
    monkeypatch.setenv("CHARTCOACH_MODEL", "m")
    monkeypatch.setenv("OPENAI_BASE_URL", "b")
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    env_app = create_app_from_env()
    assert isinstance(env_app, FastAPI)


def test_create_app_from_env_requires_env_vars(monkeypatch) -> None:
    monkeypatch.delenv("CHARTCOACH_CATALOG_PATH", raising=False)
    monkeypatch.delenv("CHARTCOACH_MODEL", raising=False)
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        create_app_from_env()

    monkeypatch.setenv("CHARTCOACH_CATALOG_PATH", "/tmp/does-not-matter")
    monkeypatch.delenv("CHARTCOACH_MODEL", raising=False)
    with pytest.raises(RuntimeError):
        create_app_from_env()
