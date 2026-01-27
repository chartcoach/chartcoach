from __future__ import annotations

import sys
from collections.abc import Callable
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from types import ModuleType
from typing import Protocol, TypedDict, cast

import polars as pl
import pytest
from pydantic import ValidationError

from chartcoach.env import load_env
from chartcoach.catalog import Catalog, CatalogEntry, Guideline
from chartcoach.retrieval.server import (
    create_app,
    create_app_from_env,
    create_router,
)
from chartcoach.retrieval.server.routes import StrategyRunRequest
from chartcoach.retrieval.service import RetrievalService
from chartcoach.retrieval.strategy.base import RetrievalStrategy, StrategyInfo
from chartcoach.retrieval.strategy.registry import create_default_strategy_registrations
from chartcoach.retrieval.strategy.types import (
    ImageItem,
    RetrievalRequest,
    RetrievalResponse,
    TextItem,
)


class _RouteInfo(TypedDict):
    method: str
    path: str
    endpoint: Callable[..., object]
    response_model: object | None


class _RouterStub(Protocol):
    routes: list[_RouteInfo]


class _AppStub(Protocol):
    routers: list[object]


class _HTTPExceptionLike(Protocol):
    status_code: int


def _install_fastapi_stub(monkeypatch) -> type[Exception]:
    class HTTPException(Exception):
        def __init__(self, status_code: int, detail: str) -> None:
            super().__init__(detail)
            self.status_code = status_code
            self.detail = detail

    class APIRouter:
        def __init__(self, *, prefix: str = "") -> None:
            self.prefix = prefix
            self.routes: list[_RouteInfo] = []

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
    setattr(fastapi_stub, "APIRouter", APIRouter)
    setattr(fastapi_stub, "FastAPI", FastAPI)
    setattr(fastapi_stub, "HTTPException", HTTPException)
    monkeypatch.setitem(sys.modules, "fastapi", fastapi_stub)
    return HTTPException


def test_catalog_from_uri_parquet_and_missing_folder(tmp_path) -> None:
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

    catalog = Catalog.from_uri(str(parquet_path))
    assert isinstance(catalog, Catalog)
    assert len(catalog) == 1
    assert catalog.entries[0].guideline.id == "g1"

    with pytest.raises(Exception):  # noqa: BLE001
        Catalog.from_uri(str(tmp_path / "missing_folder"))


def test_catalog_from_uri_supports_pathlike(tmp_path) -> None:
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

    catalog = Catalog.from_uri(parquet_path)
    assert len(catalog) == 1


def test_catalog_from_uri_supports_file_scheme(tmp_path) -> None:
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

    file_uri = f"file://{parquet_path}"
    catalog = Catalog.from_uri(file_uri)
    assert len(catalog) == 1


def test_catalog_from_uri_supports_http_download(tmp_path) -> None:
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

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):  # noqa: ANN002, D401
            super().__init__(*args, directory=str(tmp_path), **kwargs)

        def log_message(self, format: str, *args: object) -> None:  # noqa: A002
            pass

    httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=httpd.serve_forever, daemon=True)
    thread.start()

    try:
        port = httpd.server_address[1]
        url = f"http://127.0.0.1:{port}/{parquet_path.name}"
        catalog = Catalog.from_uri(url)
        assert len(catalog) == 1
    finally:
        httpd.shutdown()


def test_catalog_from_uri_supports_s3_scheme(monkeypatch) -> None:
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
    monkeypatch.setattr(pl, "read_parquet", lambda *_args, **_kwargs: df)
    catalog = Catalog.from_uri("s3://bucket/catalog.parquet")
    assert len(catalog) == 1


def test_catalog_from_uri_rejects_non_parquet_http() -> None:
    with pytest.raises(ValueError, match="\\.parquet"):
        Catalog.from_uri("http://example.invalid/catalog.txt")


def test_catalog_from_uri_rejects_non_parquet_s3() -> None:
    with pytest.raises(ValueError, match="\\.parquet"):
        Catalog.from_uri("s3://bucket/catalog.txt")


def test_default_strategy_registrations_include_guideline_browser(monkeypatch) -> None:
    _install_fastapi_stub(monkeypatch)
    regs = create_default_strategy_registrations()
    assert any(cls.id == "guideline-browser@v0" for cls, _factory in regs)


def test_default_strategy_factory_instantiates_guideline_browser(monkeypatch) -> None:
    _install_fastapi_stub(monkeypatch)
    monkeypatch.setenv("OPENAI_BASE_URL", "http://example.invalid/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    regs = create_default_strategy_registrations()
    cls, factory = next(reg for reg in regs if reg[0].id == "guideline-browser@v0")
    strategy = factory(catalog=Catalog(entries=[]))
    assert isinstance(strategy, RetrievalStrategy)
    assert strategy.id == cls.id


def test_routes_and_app_use_strategy_instances(tmp_path, monkeypatch) -> None:
    HTTPException = _install_fastapi_stub(monkeypatch)

    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v0"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            assert any(isinstance(i, TextItem) for i in request.context)
            return RetrievalResponse(
                catalog=Catalog(entries=[self.catalog.entries[0]]),
                meta={"ok": True},
            )

    def create_dummy_strategy(*, catalog: Catalog) -> RetrievalStrategy:
        return DummyStrategy(catalog)

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

    registrations = [(DummyStrategy, create_dummy_strategy)]
    retrieval = RetrievalService(
        registrations=registrations, configure_cache=lambda: None
    )

    router = create_router(retrieval=retrieval)
    router_stub = cast(_RouterStub, router)
    get_strategies = next(r for r in router_stub.routes if r["method"] == "GET")[
        "endpoint"
    ]
    out = cast(list[StrategyInfo], get_strategies())
    assert any(s.id == "dummy@v0" for s in out)

    post = cast(
        Callable[[str, StrategyRunRequest], RetrievalResponse],
        next(r for r in router_stub.routes if r["method"] == "POST")["endpoint"],
    )
    resp = post(
        "dummy@v0",
        StrategyRunRequest(
            catalog_uri=str(parquet_path),
            request=RetrievalRequest(context=[TextItem(role="situation", text="S")]),
        ),
    )
    assert resp.meta["ok"] is True
    assert len(resp.catalog) == 1
    assert resp.catalog.entries[0].guideline.id == "g1"

    with pytest.raises(HTTPException) as e:
        post(
            "missing@v0",
            StrategyRunRequest(
                catalog_uri=str(parquet_path),
                request=RetrievalRequest(),
            ),
        )
    assert cast(_HTTPExceptionLike, e.value).status_code == 404

    app = create_app(retrieval=retrieval)
    assert len(cast(_AppStub, app).routers) == 1

    env_app = create_app_from_env()
    assert len(cast(_AppStub, env_app).routers) == 1


def test_run_strategy_maps_common_errors_to_http_exceptions(
    tmp_path, monkeypatch
) -> None:
    HTTPException = _install_fastapi_stub(monkeypatch)

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

    class RaisesValueError(RetrievalStrategy):
        id = "raises-value-error@v0"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            raise ValueError("bad request")

    class RaisesUpstreamError(RetrievalStrategy):
        id = "raises-upstream-error@v0"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            raise RuntimeError("upstream exploded")

    def create_raises_value_error(*, catalog: Catalog) -> RetrievalStrategy:
        return RaisesValueError(catalog)

    def create_raises_upstream_error(*, catalog: Catalog) -> RetrievalStrategy:
        return RaisesUpstreamError(catalog)

    def create_raises_runtime_error(*, catalog: Catalog) -> RetrievalStrategy:  # noqa: ARG001
        raise RuntimeError("misconfigured strategy factory")

    # 422: catalog URI is invalid.
    retrieval = RetrievalService(
        registrations=[(RaisesValueError, create_raises_value_error)],
        configure_cache=lambda: None,
    )
    router = create_router(retrieval=retrieval)
    post = cast(
        Callable[[str, StrategyRunRequest], RetrievalResponse],
        cast(_RouterStub, router).routes[-1]["endpoint"],
    )
    with pytest.raises(HTTPException) as e:
        post(
            "raises-value-error@v0",
            StrategyRunRequest(
                catalog_uri="http://example.invalid/catalog.txt",
                request=RetrievalRequest(),
            ),
        )
    assert cast(_HTTPExceptionLike, e.value).status_code == 422

    # 500: strategy factory fails (e.g., missing required env).
    retrieval = RetrievalService(
        registrations=[(RaisesValueError, create_raises_runtime_error)],
        configure_cache=lambda: None,
    )
    router = create_router(retrieval=retrieval)
    post = cast(
        Callable[[str, StrategyRunRequest], RetrievalResponse],
        cast(_RouterStub, router).routes[-1]["endpoint"],
    )
    with pytest.raises(HTTPException) as e:
        post(
            "raises-value-error@v0",
            StrategyRunRequest(
                catalog_uri=str(parquet_path),
                request=RetrievalRequest(),
            ),
        )
    assert cast(_HTTPExceptionLike, e.value).status_code == 500

    # 422: strategy rejects request payload.
    retrieval = RetrievalService(
        registrations=[(RaisesValueError, create_raises_value_error)],
        configure_cache=lambda: None,
    )
    router = create_router(retrieval=retrieval)
    post = cast(
        Callable[[str, StrategyRunRequest], RetrievalResponse],
        cast(_RouterStub, router).routes[-1]["endpoint"],
    )
    with pytest.raises(HTTPException) as e:
        post(
            "raises-value-error@v0",
            StrategyRunRequest(
                catalog_uri=str(parquet_path),
                request=RetrievalRequest(),
            ),
        )
    assert cast(_HTTPExceptionLike, e.value).status_code == 422

    # 502: unexpected upstream error during strategy run.
    retrieval = RetrievalService(
        registrations=[(RaisesUpstreamError, create_raises_upstream_error)],
        configure_cache=lambda: None,
    )
    router = create_router(retrieval=retrieval)
    post = cast(
        Callable[[str, StrategyRunRequest], RetrievalResponse],
        cast(_RouterStub, router).routes[-1]["endpoint"],
    )
    with pytest.raises(HTTPException) as e:
        post(
            "raises-upstream-error@v0",
            StrategyRunRequest(
                catalog_uri=str(parquet_path),
                request=RetrievalRequest(
                    context=[TextItem(role="situation", text="S")],
                ),
            ),
        )
    assert cast(_HTTPExceptionLike, e.value).status_code == 502


def test_create_app_from_env_does_not_require_env_vars(monkeypatch) -> None:
    _install_fastapi_stub(monkeypatch)

    monkeypatch.delenv("CHARTCOACH_CATALOG_PATH", raising=False)
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert create_app_from_env() is not None


def test_env_require_catalog_path_raises() -> None:
    env = load_env(
        {"OPENAI_BASE_URL": "http://example.invalid/v1", "OPENAI_API_KEY": "k"}
    )
    with pytest.raises(RuntimeError, match="CHARTCOACH_CATALOG_PATH"):
        env.retrieval_server.require_catalog_path()


def test_env_require_catalog_path_returns() -> None:
    env = load_env(
        {
            "OPENAI_BASE_URL": "http://example.invalid/v1",
            "OPENAI_API_KEY": "k",
            "CHARTCOACH_CATALOG_PATH": "/tmp/catalog.parquet",
        }
    )
    assert env.retrieval_server.require_catalog_path() == Path("/tmp/catalog.parquet")


def test_env_require_openai_raises() -> None:
    env = load_env({"CHARTCOACH_CATALOG_PATH": "/tmp/catalog.parquet"})
    with pytest.raises(RuntimeError, match="OPENAI_BASE_URL"):
        env.openai.require()


def test_env_require_s3_raises() -> None:
    env = load_env({})
    with pytest.raises(RuntimeError, match="S3_ACCESS_KEY_ID"):
        env.s3.require()


def test_env_require_s3_returns() -> None:
    env = load_env(
        {
            "S3_ACCESS_KEY_ID": "k",
            "S3_SECRET_ACCESS_KEY": "s",
            "S3_BUCKET": "bucket",
            "S3_PREFIX": "p",
        }
    )
    s3 = env.s3.require()
    assert s3.bucket == "bucket"
    assert s3.prefix == "p"


def test_env_parses_force_path_style_false() -> None:
    env = load_env({"S3_FORCE_PATH_STYLE": "false"})
    assert env.s3.force_path_style is False


def test_retrieval_request_base64_bytes_decode() -> None:
    req = RetrievalRequest(
        context=[
            ImageItem.model_validate(
                {"role": "chart", "mime": "image/png", "data": "aGk="}  # "hi"
            )
        ]
    )
    image = next(i for i in req.context if isinstance(i, ImageItem))
    assert image.data == b"hi"


def test_bytes_field_accepts_none_and_rejects_invalid_base64() -> None:
    assert ImageItem.model_validate({"data": None}).data is None
    with pytest.raises(ValidationError):
        ImageItem.model_validate({"data": "not base64"})
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
