from __future__ import annotations

import sys
from types import ModuleType
from typing import Any

import dspy
import polars as pl
import pytest
from pydantic import ValidationError

from chartcoach.catalog import Catalog, CatalogEntry, Guideline
from chartcoach.retrieval.server import (
    create_app,
    create_app_from_env,
    create_default_strategies,
    create_router,
)
from chartcoach.retrieval.server.registry import _catalog_from_path
from chartcoach.retrieval.strategy import RetrievalStrategy
from chartcoach.retrieval.types import (
    ImageItem,
    RetrievalRequest,
    RetrievalResponse,
    TextItem,
)


def _install_fastapi_stub(monkeypatch) -> type:
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
    return HTTPException


def test_catalog_from_path_parquet_and_missing_folder(tmp_path) -> None:
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

    catalog = _catalog_from_path(str(parquet_path))
    assert isinstance(catalog, Catalog)
    assert len(catalog) == 1
    assert catalog.entries[0].guideline.id == "g1"

    with pytest.raises(Exception):  # noqa: BLE001
        _catalog_from_path(str(tmp_path / "missing_folder"))


def test_create_default_strategies_includes_guideline_browser(monkeypatch) -> None:
    _install_fastapi_stub(monkeypatch)
    monkeypatch.setenv("OPENAI_BASE_URL", "http://example.invalid/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    catalog = Catalog(entries=[])
    strategies = create_default_strategies(catalog=catalog)
    assert any(s.id == "guideline-browser@v0" for s in strategies)


def test_create_default_strategies_instantiates(monkeypatch) -> None:
    _install_fastapi_stub(monkeypatch)
    monkeypatch.setenv("OPENAI_BASE_URL", "http://example.invalid/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    catalog = Catalog(entries=[])
    strategies = create_default_strategies(catalog=catalog)
    assert strategies


def test_routes_and_app_use_strategy_instances(tmp_path, monkeypatch) -> None:
    HTTPException = _install_fastapi_stub(monkeypatch)

    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v0"

        def __init__(self, *, catalog: Catalog, lm: dspy.LM) -> None:  # noqa: ARG002
            super().__init__(catalog)

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            assert any(isinstance(i, TextItem) for i in request.context)
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

    lm = dspy.LM(model="m", api_base="http://example.invalid/v1", api_key="k")
    strategies = [DummyStrategy(catalog=Catalog(entries=[]), lm=lm)]

    router = create_router(strategies=strategies)
    get_strategies = next(r for r in router.routes if r["method"] == "GET")["endpoint"]
    out = get_strategies()
    assert any(s.id == "dummy@v0" for s in out)

    post = next(r for r in router.routes if r["method"] == "POST")["endpoint"]
    resp = post(
        "dummy@v0",
        RetrievalRequest(context=[TextItem(role="situation", text="S")]),
    )
    assert resp.meta["ok"] is True
    assert len(resp.catalog) == 1
    assert resp.catalog.entries[0].guideline.id == "g1"

    with pytest.raises(HTTPException) as e:
        post("missing@v0", RetrievalRequest())
    assert e.value.status_code == 404

    app = create_app(strategies=strategies)
    assert len(app.routers) == 1

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
    monkeypatch.setenv("OPENAI_BASE_URL", "http://example.invalid/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    env_app = create_app_from_env()
    assert len(env_app.routers) == 1


def test_create_app_from_env_requires_env_vars(monkeypatch) -> None:
    _install_fastapi_stub(monkeypatch)

    monkeypatch.delenv("CHARTCOACH_CATALOG_PATH", raising=False)
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        create_app_from_env()

    monkeypatch.setenv("CHARTCOACH_CATALOG_PATH", "/tmp/does-not-matter")
    with pytest.raises(RuntimeError):
        create_app_from_env()


def test_retrieval_request_base64_bytes_decode() -> None:
    req = RetrievalRequest(
        context=[
            ImageItem(
                role="chart",
                mime="image/png",
                data="aGk=",  # "hi"
            )
        ]
    )
    image = next(i for i in req.context if isinstance(i, ImageItem))
    assert image.data == b"hi"


def test_bytes_field_accepts_none_and_rejects_invalid_base64() -> None:
    assert ImageItem(data=None).data is None
    with pytest.raises(ValidationError):
        ImageItem(data="not base64")
    with pytest.raises(ValidationError):
        ImageItem(data=123)  # type: ignore[arg-type]


def test_retrieval_response_serializes_catalog() -> None:
    resp = RetrievalResponse(
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
        meta={"m": 1},
    )
    dumped = resp.model_dump(mode="json")
    assert dumped["meta"]["m"] == 1
    assert dumped["catalog"][0]["guideline"]["id"] == "g1"


def test_cli_main_starts_uvicorn(tmp_path, monkeypatch) -> None:
    _install_fastapi_stub(monkeypatch)

    called: dict[str, object] = {}

    uvicorn_stub = ModuleType("uvicorn")

    def run(app, *, host: str, port: int):  # noqa: ANN001
        called["app"] = app
        called["host"] = host
        called["port"] = port

    uvicorn_stub.run = run  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "uvicorn", uvicorn_stub)

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
    monkeypatch.setenv("OPENAI_BASE_URL", "http://example.invalid/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    monkeypatch.setenv("CHARTCOACH_HOST", "0.0.0.0")
    monkeypatch.setenv("CHARTCOACH_PORT", "9999")

    from chartcoach.retrieval.server.__main__ import main

    main()
    assert called["host"] == "0.0.0.0"
    assert called["port"] == 9999
