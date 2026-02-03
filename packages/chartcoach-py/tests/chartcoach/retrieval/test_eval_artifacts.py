from __future__ import annotations

import hashlib
import json
from typing import cast

import pytest

from obstore.store import MemoryStore

from chartcoach.catalog import Catalog, CatalogEntry, Guideline
from chartcoach.retrieval.service.eval_artifacts import (
    ScenarioChart,
    ScenarioSpec,
    build_bundle_digest,
    build_retrieval_request,
    build_scenario_bundle,
    compute_digest,
    delete_paths,
    entry_score,
    list_paths,
    load_scenarios,
    now_iso,
    read_json,
    resolve_artifacts_config,
    resolve_catalog_digest,
    resolve_repo_commit,
    resolve_scenarios_digest,
    write_json,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy, StrategyInfo
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse


def test_now_iso_is_isoish() -> None:
    value = now_iso()
    assert value.endswith("+00:00")
    assert "T" in value


def test_load_scenarios_parses_yaml(tmp_path) -> None:
    path = tmp_path / "spec.yaml"
    path.write_text(
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

    scenarios = load_scenarios(path)
    assert [s.id for s in scenarios] == ["s1"]
    assert scenarios[0].chart is not None
    assert scenarios[0].chart.uri.startswith("https://")


def test_build_retrieval_request_requires_designer_intent() -> None:
    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="   ",
    )
    with pytest.raises(ValueError, match="designer_intent"):
        build_retrieval_request(scenario, k=None)


def test_build_retrieval_request_shapes_context() -> None:
    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
        audience="general readers",
    )
    request = build_retrieval_request(scenario, k=5)
    assert request.k == 5
    assert any(i.role == "chart" for i in request.context)
    assert any(i.role == "intent" for i in request.context)
    assert any(i.role == "chart_spec" for i in request.context)
    assert any(i.role == "audience" for i in request.context)


def test_compute_digest_is_stable() -> None:
    assert compute_digest({"a": 1, "b": 2}) == compute_digest({"b": 2, "a": 1})


def test_bundle_digest_changes_with_inputs() -> None:
    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )
    d1 = build_bundle_digest(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategy_ids=["a"],
        k=None,
    )
    d2 = build_bundle_digest(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategy_ids=["a"],
        k=10,
    )
    assert d1 != d2


def test_entry_score_monotone() -> None:
    scores = [entry_score(i, 5) for i in range(5)]
    assert scores[0] > scores[1] > scores[2]
    assert scores[-1] >= 0.01


def test_read_write_list_delete_json_roundtrip() -> None:
    store = MemoryStore()
    write_json(store, "index.json", {"ok": True})
    assert read_json(store, "index.json") == {"ok": True}
    assert read_json(store, "missing.json") is None

    write_json(store, "nested/a.json", {"a": 1})
    paths = list_paths(store, prefix="nested/")
    assert paths == ["nested/a.json"]

    delete_paths(store, paths)
    assert read_json(store, "nested/a.json") is None


def test_read_json_requires_object() -> None:
    import obstore

    store = MemoryStore()
    obstore.put(store, "arr.json", b"[]")
    with pytest.raises(ValueError, match="Expected JSON object"):
        read_json(store, "arr.json")


def test_build_scenario_bundle_runs_strategies() -> None:
    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v0"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
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
                catalog=Catalog(entries=[entry]),
                meta={
                    "k": int(request.k or 1),
                    "hits": [
                        {
                            "id": "g1",
                            "score": 1.0,
                            "evidence": [
                                {
                                    "role": "advice",
                                    "text": "Use colorblind-safe palettes.",
                                    "score": 1.0,
                                },
                                {
                                    "role": "reason",
                                    "text": "This improves accessibility.",
                                    "score": 0.5,
                                },
                            ],
                        }
                    ],
                },
            )

    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )
    bundle = build_scenario_bundle(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategies=[
            (
                StrategyInfo(id="dummy@v0", name="DummyStrategy", description=""),
                DummyStrategy(Catalog(entries=[])),
            )
        ],
        k=3,
        strategy_timeout_seconds=None,
        config={
            "repo_commit": "deadbeef",
            "catalog_digest": "cafe",
            "scenario_digest": "babe",
        },
    )
    assert bundle.schema_version == 1
    assert bundle.scenario.id == scenario.id
    assert bundle.strategies[0].strategy_id == "dummy@v0"
    assert bundle.strategies[0].meta["k"] == 3
    assert bundle.strategies[0].guidelines[0].rank == 1
    assert bundle.strategies[0].guidelines[0].entry.guideline.id == "g1"
    assert bundle.strategies[0].guidelines[0].evidence
    assert bundle.meta["repo_commit"] == "deadbeef"
    assert bundle.meta["catalog_digest"] == "cafe"
    assert bundle.meta["scenario_digest"] == "babe"

    # bundle is JSON-serializable
    json.dumps(bundle.model_dump(mode="json"))


def test_build_scenario_bundle_filters_bad_evidence_hits() -> None:
    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v1"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
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
                catalog=Catalog(entries=[entry]),
                meta={
                    "k": int(request.k or 1),
                    "hits": [
                        "not-a-dict",
                        {"id": None, "evidence": []},
                        {"id": "g1", "evidence": "nope"},
                        {
                            "id": "g1",
                            "evidence": [
                                "not-a-dict",
                                {"role": "reason", "text": "   ", "score": 0.1},
                                {"role": "advice", "text": "ok", "score": 1.0},
                            ],
                        },
                    ],
                },
            )

    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )
    with pytest.raises(ValueError, match="did not match the trace schema"):
        build_scenario_bundle(
            scenario=scenario,
            catalog_uri="file:///tmp/catalog.parquet",
            strategies=[
                (
                    StrategyInfo(id="dummy@v1", name="DummyStrategy", description=""),
                    DummyStrategy(Catalog(entries=[])),
                )
            ],
            k=3,
            strategy_timeout_seconds=None,
            config={
                "repo_commit": "deadbeef",
                "catalog_digest": "cafe",
                "scenario_digest": "babe",
            },
        )


def test_build_scenario_bundle_records_lm_usage_meta() -> None:
    class DummyLM:
        def __init__(self) -> None:
            self.history: list[object] = []

    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v0"

        def __init__(self, catalog: Catalog) -> None:
            super().__init__(catalog)
            self._lm = DummyLM()

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            # Simulate an LM call recorded in `dspy.LM.history`-compatible format.
            self._lm.history.append(
                {
                    "usage": {
                        "prompt_tokens": 2,
                        "completion_tokens": 3,
                        "total_tokens": 5,
                    },
                    "cost": 0.01,
                }
            )
            return RetrievalResponse(
                catalog=Catalog(entries=[]),
                meta={"k": int(request.k or 1), "hits": []},
            )

    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )
    bundle = build_scenario_bundle(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategies=[
            (
                StrategyInfo(id="dummy@v0", name="DummyStrategy", description=""),
                DummyStrategy(Catalog(entries=[])),
            )
        ],
        k=3,
        strategy_timeout_seconds=None,
    )

    lm_usage = bundle.strategies[0].meta.get("lm_usage")
    assert isinstance(lm_usage, dict)
    lm_usage_dict = cast("dict[str, object]", lm_usage)
    calls = lm_usage_dict.get("calls")
    total_tokens = lm_usage_dict.get("total_tokens")
    assert isinstance(calls, int)
    assert isinstance(total_tokens, int)
    assert calls == 1
    assert total_tokens == 5


def test_build_scenario_bundle_records_strategy_errors() -> None:
    class FailingStrategy(RetrievalStrategy):
        id = "failing@v0"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            raise ValueError("boom")

    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )
    bundle = build_scenario_bundle(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategies=[
            (
                StrategyInfo(id="failing@v0", name="FailingStrategy", description=""),
                FailingStrategy(Catalog(entries=[])),
            )
        ],
        k=3,
        strategy_timeout_seconds=None,
    )
    assert bundle.strategies[0].strategy_id == "failing@v0"
    assert "boom" in str(bundle.strategies[0].meta.get("error"))
    assert bundle.strategies[0].guidelines == []


def test_timeout_context_manager_is_noop_for_none_or_zero() -> None:
    from chartcoach.retrieval.service.eval_artifacts import _timeout

    with _timeout(None, message="x"):
        pass
    with _timeout(0, message="x"):
        pass


def test_timeout_context_manager_is_noop_off_main_thread() -> None:
    import threading

    from chartcoach.retrieval.service.eval_artifacts import _timeout

    ran: list[bool] = []

    def worker() -> None:
        with _timeout(0.001, message="x"):
            ran.append(True)

    t = threading.Thread(target=worker)
    t.start()
    t.join()
    assert ran == [True]


def test_timeout_context_manager_can_raise(monkeypatch) -> None:
    import time

    from chartcoach.retrieval.service.eval_artifacts import _StrategyTimeout, _timeout

    # Use a tiny timeout; SIGALRM is only installed on the main thread.
    with pytest.raises(_StrategyTimeout):
        with _timeout(0.001, message="boom"):
            time.sleep(0.01)


def test_build_scenario_bundle_records_timeout_branch(monkeypatch) -> None:
    from contextlib import contextmanager

    import chartcoach.retrieval.service.eval_artifacts as eval_artifacts

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
            return RetrievalResponse(catalog=Catalog(entries=[entry]), meta={})

    @contextmanager
    def boom_timeout(_seconds: float | None, *, message: str):  # noqa: ARG001
        raise eval_artifacts._StrategyTimeout(message)
        yield  # pragma: no cover

    monkeypatch.setattr(eval_artifacts, "_timeout", boom_timeout)

    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )

    bundle = build_scenario_bundle(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategies=[
            (
                StrategyInfo(id="dummy@v0", name="DummyStrategy", description=""),
                DummyStrategy(Catalog(entries=[])),
            )
        ],
        k=3,
        strategy_timeout_seconds=None,
    )

    meta = bundle.strategies[0].meta
    assert meta.get("error")
    assert isinstance(meta.get("elapsed_ms"), int)


def test_bundle_has_errors_handles_non_list_and_non_dict(retrieval_run_config) -> None:
    from chartcoach.retrieval.service.eval_artifacts import EvalArtifactsService
    from chartcoach.retrieval.service.retrieval_service import RetrievalService

    svc = EvalArtifactsService(
        store=MemoryStore(),
        retrieval=RetrievalService(
            registrations=[],
            configure_cache=lambda: None,
            run_config=retrieval_run_config,
        ),
    )
    assert svc._bundle_has_errors({"strategies": "nope"}) is False
    assert svc._bundle_has_errors({"strategies": [1, 2]}) is False
    assert svc._bundle_has_errors({"strategies": [{"meta": {"error": "boom"}}]}) is True


def test_extract_lm_usage_delta_sums_tokens_and_cost() -> None:
    from chartcoach.retrieval.service.eval_artifacts import _extract_lm_usage_delta

    class DummyLM:
        def __init__(self) -> None:
            self.history = [
                "oops",
                {
                    "usage": {
                        "prompt_tokens": 2,
                        "completion_tokens": 3,
                        "total_tokens": 5,
                    },
                    "cost": 0.01,
                },
                {
                    "usage": {
                        "prompt_tokens": 1,
                        "completion_tokens": 1,
                        "total_tokens": 2,
                    },
                    "cost": None,
                },
            ]

    out = _extract_lm_usage_delta(lm=DummyLM(), before_len=0)
    assert out["calls"] == 2
    assert out["prompt_tokens"] == 3
    assert out["completion_tokens"] == 4
    assert out["total_tokens"] == 7
    assert out["cost_usd"] == pytest.approx(0.01)


def test_extract_lm_usage_delta_handles_missing_or_invalid_history() -> None:
    from chartcoach.retrieval.service.eval_artifacts import _extract_lm_usage_delta

    class NoHistory:
        pass

    class BadHistory:
        history = "nope"

    assert _extract_lm_usage_delta(lm=NoHistory(), before_len=0) == {}
    assert _extract_lm_usage_delta(lm=BadHistory(), before_len=0) == {}


def test_extract_lm_usage_delta_omits_cost_when_unknown() -> None:
    from chartcoach.retrieval.service.eval_artifacts import _extract_lm_usage_delta

    class DummyLM:
        def __init__(self) -> None:
            self.history = [
                {
                    "usage": {
                        "prompt_tokens": 1,
                        "completion_tokens": 0,
                        "total_tokens": 1,
                    }
                }
            ]

    out = _extract_lm_usage_delta(lm=DummyLM(), before_len=0)
    assert out["calls"] == 1
    assert out.get("cost_usd") is None


def test_get_strategy_lm_history_snapshot_handles_strategy_lm() -> None:
    from chartcoach.retrieval.service.eval_artifacts import (
        _get_strategy_lm_history_snapshot,
    )

    class DummyLM:
        history = [{"usage": {"prompt_tokens": 1}}]

    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v0"

        def __init__(self, catalog: Catalog) -> None:
            super().__init__(catalog)
            self._lm = DummyLM()

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            return RetrievalResponse(catalog=Catalog(entries=[]), meta={})

    lm, before_len = _get_strategy_lm_history_snapshot(
        DummyStrategy(Catalog(entries=[]))
    )
    assert before_len == 1
    assert getattr(lm, "history", None)


def test_resolve_repo_commit_returns_string() -> None:
    value = resolve_repo_commit()
    assert isinstance(value, str)
    assert value


def test_resolve_catalog_digest_hashes_local_file(tmp_path) -> None:
    path = tmp_path / "catalog.parquet"
    path.write_bytes(b"hello")
    digest = resolve_catalog_digest(str(path))
    assert digest == hashlib.sha256(b"hello").hexdigest()[:16]


def test_resolve_scenarios_digest_hashes_file(tmp_path) -> None:
    path = tmp_path / "spec.yaml"
    path.write_text("scenarios: []\n", encoding="utf-8")
    digest = resolve_scenarios_digest(path)
    assert digest == hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def test_resolve_catalog_digest_covers_uri_and_dir_branches(tmp_path) -> None:
    # Empty.
    assert resolve_catalog_digest("") == "unknown"

    # Remote URI falls back to digest of the URI string.
    assert len(resolve_catalog_digest("https://example.invalid/catalog.parquet")) == 16

    # Missing local path falls back to digest of the string.
    assert len(resolve_catalog_digest(str(tmp_path / "missing.parquet"))) == 16

    # file:// URL.
    path = tmp_path / "cat.parquet"
    path.write_bytes(b"x")
    assert (
        resolve_catalog_digest(f"file://{path}")
        == hashlib.sha256(b"x").hexdigest()[:16]
    )

    # Directory with catalog.parquet uses that file.
    d1 = tmp_path / "d1"
    d1.mkdir()
    (d1 / "catalog.parquet").write_bytes(b"y")
    assert resolve_catalog_digest(str(d1)) == hashlib.sha256(b"y").hexdigest()[:16]

    # Directory without parquet hashes the tree.
    d2 = tmp_path / "d2"
    d2.mkdir()
    (d2 / "a.txt").write_text("a", encoding="utf-8")
    (d2 / "b.txt").write_text("b", encoding="utf-8")
    digest1 = resolve_catalog_digest(str(d2))
    digest2 = resolve_catalog_digest(str(d2))
    assert digest1 == digest2


def test_resolve_scenarios_digest_handles_missing_file(tmp_path) -> None:
    assert resolve_scenarios_digest(tmp_path / "missing.yaml") == "unknown"


def test_resolve_artifacts_config_includes_repo_commit(retrieval_run_config) -> None:
    cfg = resolve_artifacts_config(run_config=retrieval_run_config)
    assert isinstance(cfg.get("repo_commit"), str)
    assert cfg["repo_commit"]
