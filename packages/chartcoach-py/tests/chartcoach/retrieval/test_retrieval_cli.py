from __future__ import annotations

import io
import json
import sys
from pathlib import Path

import polars as pl
import pytest

from obstore.store import MemoryStore

from chartcoach.catalog import Catalog, CatalogEntry, Guideline
from chartcoach.env import S3EnvRequired
from chartcoach.retrieval.cli.__main__ import main
from chartcoach.retrieval.service import EvalArtifactsService, RetrievalService
from chartcoach.retrieval.service.artifact_store import (
    create_store,
    default_artifacts_url,
    normalize_prefix,
)
from chartcoach.retrieval.service.eval_artifacts import read_json, write_json
from chartcoach.retrieval.service.retrieval_service import UnknownStrategyError
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse


def test_normalize_prefix() -> None:
    assert normalize_prefix(None) == ""
    assert normalize_prefix("") == ""
    assert normalize_prefix("a") == "a/"
    assert normalize_prefix("a/") == "a/"


def test_create_store_memory_scheme() -> None:
    store = create_store("memory://")
    assert isinstance(store, MemoryStore)


def test_cli_helpers_cover_catalog_and_store_url_branches(monkeypatch) -> None:
    import chartcoach.retrieval.cli.__main__ as cli

    assert cli._require_catalog_uri("manual.parquet") == "manual.parquet"

    monkeypatch.setenv("S3_ACCESS_KEY_ID", "k")
    monkeypatch.setenv("S3_SECRET_ACCESS_KEY", "s")
    monkeypatch.setenv("S3_BUCKET", "bucket")
    monkeypatch.setenv("S3_PREFIX", "prefix")
    assert cli._resolve_store_url(None) == "s3://bucket/prefix/eval-artifacts/v1/"

    store = cli._create_artifacts_store("memory://")
    assert isinstance(store, MemoryStore)


def test_default_artifacts_url_uses_s3_config() -> None:
    s3 = S3EnvRequired(
        access_key_id="k",
        secret_access_key="s",
        bucket="bucket",
        prefix="prefix",
    )
    assert default_artifacts_url(s3=s3) == "s3://bucket/prefix/eval-artifacts/v1/"


def test_create_store_s3_scheme_uses_s3_config() -> None:
    s3 = S3EnvRequired(
        endpoint="http://example.invalid",
        region="us-east-1",
        access_key_id="k",
        secret_access_key="s",
        bucket="bucket",
        prefix="prefix",
        force_path_style=True,
    )
    store = create_store("s3://bucket/prefix/eval-artifacts/v1/", s3=s3)
    assert store.__class__.__name__ == "S3Store"


def test_create_store_s3_scheme_requires_s3_config() -> None:
    with pytest.raises(ValueError, match="S3 configuration"):
        create_store("s3://bucket/prefix/eval-artifacts/v1/")


def test_retrieval_service_filters_and_errors() -> None:
    class A(RetrievalStrategy):
        id = "a"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            return RetrievalResponse(catalog=Catalog(entries=[]))

    class B(RetrievalStrategy):
        id = "b"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            return RetrievalResponse(catalog=Catalog(entries=[]))

    regs = [(A, lambda *, catalog: A(catalog)), (B, lambda *, catalog: B(catalog))]
    retrieval = RetrievalService(
        registrations=regs,
        catalog_loader=lambda _uri: Catalog(entries=[]),
        configure_cache=lambda: None,
    )
    selected = retrieval.instantiate_strategies(
        catalog_uri="file:///tmp/catalog.parquet", strategy_ids=["b"]
    )
    assert [info.id for info, _strategy in selected] == ["b"]

    with pytest.raises(UnknownStrategyError, match="Unknown strategy ids"):
        retrieval.instantiate_strategies(
            catalog_uri="file:///tmp/catalog.parquet", strategy_ids=["missing"]
        )


def test_eval_artifacts_service_writes_bundle_and_index(tmp_path: Path) -> None:
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

    scenarios_path = tmp_path / "spec.yaml"
    scenarios_path.write_text(
        """
scenarios:
  - id: s1
    title: Scenario 1
    lang: en
    chart:
      uri: https://example.invalid/chart.png
      mime: image/png
    query: Retrieve guidelines.
    designer_intent: Improve the chart.
""".lstrip(),
        encoding="utf-8",
    )

    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v0"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            entry = CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="T",
                    description="D",
                    labels=[],
                    body="B",
                ),
                references=[],
            )
            return RetrievalResponse(
                catalog=Catalog(entries=[entry]), meta={"ok": True}
            )

    def create_dummy(*, catalog: Catalog) -> RetrievalStrategy:
        return DummyStrategy(catalog)

    store = MemoryStore()
    retrieval = RetrievalService(
        registrations=[(DummyStrategy, create_dummy)],
        catalog_loader=lambda _uri: Catalog(entries=[]),
        configure_cache=lambda: None,
    )
    svc = EvalArtifactsService(store=store, retrieval=retrieval)
    svc.run(
        scenarios_path=scenarios_path,
        catalog_uri=str(parquet_path),
        strategy_ids=None,
        k=2,
    )
    # Second run hits the digest fast-path.
    svc.run(
        scenarios_path=scenarios_path,
        catalog_uri=str(parquet_path),
        strategy_ids=None,
        k=2,
    )

    # bundle exists
    bundle = read_json(store, "bundles/s1.json")
    assert bundle is not None
    assert bundle["scenario"]["id"] == "s1"
    assert bundle["strategies"][0]["strategy_id"] == "dummy@v0"

    index = read_json(store, "index.json")
    assert index is not None
    assert index["scenarios"][0]["id"] == "s1"


def test_main_list_strategies_json(monkeypatch) -> None:
    buf = io.StringIO()
    monkeypatch.setattr(sys, "stdout", buf)

    main(["list-strategies", "--json"])
    out = buf.getvalue()
    assert "bm25-prf@v1" in out


def test_main_list_strategies_text(monkeypatch) -> None:
    buf = io.StringIO()
    monkeypatch.setattr(sys, "stdout", buf)

    main(["list-strategies"])
    out = buf.getvalue()
    assert "bm25-prf@v1" in out


def test_main_analyze_stability_requires_two_runs() -> None:
    with pytest.raises(SystemExit, match="at least two"):
        main(["analyze-stability", "--runs", "/tmp/run1"])


def test_main_analyze_stability_outputs_table_and_json(monkeypatch, tmp_path: Path) -> None:
    run1 = tmp_path / "run1"
    run2 = tmp_path / "run2"
    (run1 / "bundles").mkdir(parents=True)
    (run2 / "bundles").mkdir(parents=True)

    payload1 = {
        "schema_version": 1,
        "scenario": {"id": "s1", "title": "T", "lang": "en"},
        "strategies": [
            {
                "strategy_id": "hybrid@v1",
                "strategy_name": "Hybrid",
                "meta": {},
                "guidelines": [
                    {"rank": 1, "score": 1.0, "entry": {"guideline": {"id": "a"}, "references": []}},
                ],
            }
        ],
    }
    payload2 = {
        **payload1,
        "strategies": [
            {
                "strategy_id": "hybrid@v1",
                "strategy_name": "Hybrid",
                "meta": {},
                "guidelines": [
                    {"rank": 1, "score": 1.0, "entry": {"guideline": {"id": "a"}, "references": []}},
                ],
            }
        ],
    }
    (run1 / "bundles" / "s1.json").write_text(json.dumps(payload1), encoding="utf-8")
    (run2 / "bundles" / "s1.json").write_text(json.dumps(payload2), encoding="utf-8")

    buf = io.StringIO()
    monkeypatch.setattr(sys, "stdout", buf)

    main(["analyze-stability", "--runs", str(run1), "--runs", str(run2), "-k", "1"])
    out = buf.getvalue()
    assert "hybrid@v1" in out

    buf = io.StringIO()
    monkeypatch.setattr(sys, "stdout", buf)
    main(
        [
            "analyze-stability",
            "--runs",
            str(run1),
            "--runs",
            str(run2),
            "-k",
            "1",
            "--json",
        ]
    )
    out = buf.getvalue()
    assert "hybrid@v1" in out


def test_main_run_uses_injected_registry(monkeypatch, tmp_path: Path) -> None:
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

    scenarios_path = tmp_path / "spec.yaml"
    scenarios_path.write_text(
        """
scenarios:
  - id: s1
    title: Scenario 1
    lang: en
    chart:
      uri: https://example.invalid/chart.png
      mime: image/png
    query: Retrieve guidelines.
    designer_intent: Improve the chart.
""".lstrip(),
        encoding="utf-8",
    )

    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v0"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            entry = CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="T",
                    description="D",
                    labels=[],
                    body="B",
                ),
                references=[],
            )
            return RetrievalResponse(catalog=Catalog(entries=[entry]))

    def create_dummy(*, catalog: Catalog) -> RetrievalStrategy:
        return DummyStrategy(catalog)

    monkeypatch.setattr(
        "chartcoach.retrieval.cli.__main__.create_default_strategy_registrations",
        lambda: [(DummyStrategy, create_dummy)],
    )

    store = MemoryStore()
    monkeypatch.setattr(
        "chartcoach.retrieval.cli.__main__._create_artifacts_store",
        lambda _url: store,
    )
    monkeypatch.setenv("CHARTCOACH_CATALOG_PATH", str(parquet_path))

    main(
        [
            "run",
            "--scenarios",
            str(scenarios_path),
            "--artifacts-url",
            "memory://",
            "--purge",
        ]
    )

    assert read_json(store, "bundles/s1.json") is not None
    assert read_json(store, "index.json") is not None


def test_main_purge_deletes_objects(monkeypatch) -> None:
    store = MemoryStore()
    write_json(store, "a.json", {"a": 1})
    write_json(store, "nested/b.json", {"b": 2})
    assert read_json(store, "a.json") is not None

    monkeypatch.setattr(
        "chartcoach.retrieval.cli.__main__._create_artifacts_store",
        lambda _url: store,
    )
    main(["purge", "--artifacts-url", "memory://"])
    assert read_json(store, "a.json") is None


def test_main_run_requires_catalog_uri(monkeypatch, tmp_path: Path) -> None:
    scenarios_path = tmp_path / "spec.yaml"
    scenarios_path.write_text(
        """
scenarios:
  - id: s1
    title: Scenario 1
    lang: en
    designer_intent: Improve the chart.
""".lstrip(),
        encoding="utf-8",
    )

    monkeypatch.delenv("CHARTCOACH_CATALOG_PATH", raising=False)

    monkeypatch.setattr(
        "chartcoach.retrieval.cli.__main__.create_default_strategy_registrations",
        lambda: [],
    )
    monkeypatch.setattr(
        "chartcoach.retrieval.cli.__main__._create_artifacts_store",
        lambda _url: MemoryStore(),
    )

    with pytest.raises(SystemExit, match="Missing --catalog-uri"):
        main(
            ["run", "--scenarios", str(scenarios_path), "--artifacts-url", "memory://"]
        )


def test_safe_upstream_error_message_branches() -> None:
    from chartcoach.retrieval.service.retrieval_service import (
        _safe_upstream_error_message,
    )

    assert _safe_upstream_error_message(Exception("expired_key")) == (
        "Upstream model authentication failed (expired_key). Check OPENAI_API_KEY."
    )
    assert _safe_upstream_error_message(Exception("Authentication")) == (
        "Upstream model authentication failed. Check OPENAI_API_KEY."
    )
    assert _safe_upstream_error_message(Exception("rate_limit")) == (
        "Upstream model rate limit exceeded."
    )
