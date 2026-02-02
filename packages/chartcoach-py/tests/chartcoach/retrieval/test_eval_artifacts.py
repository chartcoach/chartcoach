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
    )
    request = build_retrieval_request(scenario, k=5)
    assert request.k == 5
    assert any(i.role == "chart" for i in request.context)
    assert any(i.role == "situation" for i in request.context)
    assert any(i.role == "chart_spec" for i in request.context)


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
                meta={"k": request.k},
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
        config={"repo_commit": "deadbeef", "catalog_digest": "cafe", "scenario_digest": "babe"},
    )
    assert bundle.schema_version == 1
    assert bundle.scenario.id == scenario.id
    assert bundle.strategies[0].strategy_id == "dummy@v0"
    assert bundle.strategies[0].meta["k"] == 3
    assert bundle.strategies[0].guidelines[0].rank == 1
    assert bundle.strategies[0].guidelines[0].entry.guideline.id == "g1"
    assert bundle.meta["repo_commit"] == "deadbeef"
    assert bundle.meta["catalog_digest"] == "cafe"
    assert bundle.meta["scenario_digest"] == "babe"

    # bundle is JSON-serializable
    json.dumps(bundle.model_dump(mode="json"))


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
            return RetrievalResponse(catalog=Catalog(entries=[]), meta={})

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
    )
    assert bundle.strategies[0].strategy_id == "failing@v0"
    assert "boom" in str(bundle.strategies[0].meta.get("error"))
    assert bundle.strategies[0].guidelines == []


def test_resolve_strategy_timeout_seconds_parses_env(monkeypatch) -> None:
    from chartcoach.retrieval.service.eval_artifacts import (
        _resolve_strategy_timeout_seconds,
    )

    monkeypatch.delenv("CHARTCOACH_STRATEGY_TIMEOUT_SECONDS", raising=False)
    assert _resolve_strategy_timeout_seconds() is not None

    monkeypatch.setenv("CHARTCOACH_STRATEGY_TIMEOUT_SECONDS", "not-a-number")
    assert _resolve_strategy_timeout_seconds() is not None

    monkeypatch.setenv("CHARTCOACH_STRATEGY_TIMEOUT_SECONDS", "-1")
    assert _resolve_strategy_timeout_seconds() is None

    monkeypatch.setenv("CHARTCOACH_STRATEGY_TIMEOUT_SECONDS", "0.1")
    assert _resolve_strategy_timeout_seconds() == 1.0


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
    )

    meta = bundle.strategies[0].meta
    assert meta.get("error")
    assert isinstance(meta.get("elapsed_ms"), int)


def test_bundle_has_errors_handles_non_list_and_non_dict() -> None:
    from chartcoach.retrieval.service.eval_artifacts import EvalArtifactsService
    from chartcoach.retrieval.service.retrieval_service import RetrievalService

    svc = EvalArtifactsService(
        store=MemoryStore(),
        retrieval=RetrievalService(registrations=[], configure_cache=lambda: None),
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


def test_git_helpers_cover_edge_branches(tmp_path, monkeypatch) -> None:
    import chartcoach.retrieval.service.eval_artifacts as eval_artifacts

    repo = tmp_path / "repo"
    repo.mkdir()
    assert eval_artifacts._find_repo_root(repo) is None

    (repo / ".git").mkdir()
    assert eval_artifacts._find_repo_root(repo) == repo

    # _run_git: subprocess errors / non-zero / empty stdout.
    def boom_run(*_args, **_kwargs):  # noqa: ANN001
        raise OSError("no git")

    monkeypatch.setattr(eval_artifacts.subprocess, "run", boom_run)
    assert eval_artifacts._run_git(["rev-parse", "HEAD"], cwd=repo) is None

    class Proc:
        def __init__(self, returncode: int, stdout: str) -> None:
            self.returncode = returncode
            self.stdout = stdout

    monkeypatch.setattr(
        eval_artifacts.subprocess,
        "run",
        lambda *_args, **_kwargs: Proc(1, "abc\n"),
    )
    assert eval_artifacts._run_git(["rev-parse", "HEAD"], cwd=repo) is None

    monkeypatch.setattr(
        eval_artifacts.subprocess,
        "run",
        lambda *_args, **_kwargs: Proc(0, ""),
    )
    assert eval_artifacts._run_git(["rev-parse", "HEAD"], cwd=repo) is None

    monkeypatch.setattr(
        eval_artifacts.subprocess,
        "run",
        lambda *_args, **_kwargs: Proc(0, "abc\n"),
    )
    assert eval_artifacts._run_git(["rev-parse", "HEAD"], cwd=repo) == "abc"


def test_resolve_repo_commit_covers_unknown_and_dirty(monkeypatch, tmp_path) -> None:
    import chartcoach.retrieval.service.eval_artifacts as eval_artifacts

    # Unknown when no repo root.
    monkeypatch.setattr(eval_artifacts, "_find_repo_root", lambda _p: None)
    assert eval_artifacts.resolve_repo_commit() == "unknown"

    # Unknown when commit can't be read.
    repo = tmp_path / "repo"
    repo.mkdir()
    monkeypatch.setattr(eval_artifacts, "_find_repo_root", lambda _p: repo)
    monkeypatch.setattr(eval_artifacts, "_run_git", lambda _args, *, cwd: None)
    assert eval_artifacts.resolve_repo_commit() == "unknown"

    # Dirty branch when git diff returns non-zero.
    monkeypatch.setattr(eval_artifacts, "_run_git", lambda _args, *, cwd: "1234567890abcdef")

    class Proc:
        def __init__(self, returncode: int) -> None:
            self.returncode = returncode

    calls: list[list[str]] = []

    def fake_run(cmd, **_kwargs):  # noqa: ANN001
        calls.append(list(cmd))
        if cmd[:2] == ["git", "diff"] and cmd[-1] == "--quiet":
            return Proc(1)
        return Proc(0)

    monkeypatch.setattr(eval_artifacts.subprocess, "run", fake_run)
    assert eval_artifacts.resolve_repo_commit().endswith("-dirty")

    # Clean branch when both diff checks return 0 (and tolerate OSError).
    def fake_run_clean(cmd, **_kwargs):  # noqa: ANN001
        if cmd[:2] == ["git", "diff"] and cmd[-1] == "--quiet":
            raise OSError("ignore")
        return Proc(0)

    monkeypatch.setattr(eval_artifacts.subprocess, "run", fake_run_clean)
    assert eval_artifacts.resolve_repo_commit() == "1234567890ab"


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
    assert resolve_catalog_digest(f"file://{path}") == hashlib.sha256(b"x").hexdigest()[:16]

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


def test_resolve_artifacts_config_includes_commit(monkeypatch) -> None:
    import chartcoach.retrieval.service.eval_artifacts as eval_artifacts

    monkeypatch.setattr(eval_artifacts, "resolve_repo_commit", lambda: "cafebabe")
    cfg = eval_artifacts.resolve_artifacts_config()
    assert cfg["repo_commit"] == "cafebabe"
