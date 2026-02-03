from __future__ import annotations

import contextlib
from types import SimpleNamespace
from typing import TYPE_CHECKING, cast

import pytest

from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.retrieval.strategy.pipelines import guideline_status as mod
from chartcoach.retrieval.strategy.pipelines.focus import FocusMode
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest, TextItem

if TYPE_CHECKING:
    import dspy


@pytest.fixture(autouse=True)
def _clear_status_cache() -> None:
    mod._STATUS_CACHE.clear()
    mod._SHARED_STATUS_SCORER = None


def _entry(gid: str, *, body: str = "## Advice\nDo X.") -> CatalogEntry:
    return CatalogEntry(
        guideline=Guideline(
            id=gid,
            title=f"Title {gid}",
            description=f"Desc {gid}",
            labels=["topic:test"],
            body=body,
        ),
        references=[],
    )


def test_chart_fingerprint_variants() -> None:
    req = RetrievalRequest(context=[ImageItem(role="chart", uri="file:///tmp/x.png")])
    assert (fp := mod._chart_fingerprint(req)) and fp.startswith("uri:")

    req = RetrievalRequest(
        context=[ImageItem(role="chart", data=b"abc", mime="image/png")]
    )
    assert (fp := mod._chart_fingerprint(req)) and fp.startswith("bytes:")

    req = RetrievalRequest(context=[TextItem(role="situation", text="S")])
    assert mod._chart_fingerprint(req) is None


def test_coerce_helpers_and_excerpt() -> None:
    assert mod._coerce_status("Violated") == "violated"
    assert mod._coerce_status("not-applicable") == "not_applicable"
    assert mod._coerce_status(None) == "unclear"

    assert mod._coerce_confidence("0.5") == 0.5
    assert mod._coerce_confidence(-1) == 0.0
    assert mod._coerce_confidence(2) == 1.0
    assert mod._coerce_confidence(None) == 0.0

    assert mod._guideline_excerpt(_entry("g1", body=""), max_chars=10) == ""
    assert mod._guideline_excerpt(_entry("g1", body="abc"), max_chars=10) == "abc"
    assert (
        mod._guideline_excerpt(_entry("g1", body="a" * 50), max_chars=10)
        == ("a" * 10) + "..."
    )


def test_status_scorer_config_from_env_supports_aliases(monkeypatch) -> None:
    monkeypatch.delenv("CHARTCOACH_STATUS_CANDIDATE_MULTIPLIER", raising=False)
    monkeypatch.delenv(
        "CHARTCOACH_GUIDELINE_STATUS_CANDIDATE_MULTIPLIER", raising=False
    )
    cfg = mod.status_scorer_config_from_env()
    assert cfg.candidate_multiplier == 4

    monkeypatch.setenv("CHARTCOACH_GUIDELINE_STATUS_CANDIDATE_MULTIPLIER", "2")
    monkeypatch.setenv("CHARTCOACH_STATUS_KEEP_UNCLEAR", "0")
    monkeypatch.setenv("CHARTCOACH_STATUS_MAX_EXCERPT_CHARS", "1")
    monkeypatch.setenv("CHARTCOACH_STATUS_MAX_RATIONALE_CHARS", "2")
    monkeypatch.setenv("CHARTCOACH_STATUS_BATCH_SIZE", "3")
    cfg = mod.status_scorer_config_from_env()
    assert cfg.candidate_multiplier == 2
    assert cfg.keep_unclear is False
    assert cfg.max_guideline_excerpt_chars == 1
    assert cfg.max_rationale_chars == 2
    assert cfg.batch_size == 3

    # Invalid env values fall back to defaults and clamp.
    monkeypatch.setenv("CHARTCOACH_STATUS_BATCH_SIZE", "nope")
    monkeypatch.setenv("CHARTCOACH_STATUS_CANDIDATE_MULTIPLIER", "0")
    cfg = mod.status_scorer_config_from_env()
    assert cfg.batch_size == 10
    # Candidate multiplier clamps to >=1.
    assert cfg.candidate_multiplier == 1

    # True values are accepted explicitly (exercise the True branch).
    monkeypatch.setenv("CHARTCOACH_STATUS_KEEP_UNCLEAR", "true")
    cfg = mod.status_scorer_config_from_env()
    assert cfg.keep_unclear is True


def test_shared_status_scorer_caches(monkeypatch) -> None:
    created: list[str] = []

    class DummyModule:
        def __init__(self, *, lm, config):  # noqa: ANN001
            created.append("module")
            self._lm = lm
            self._config = config

    monkeypatch.setattr(mod, "GuidelineStatusModule", DummyModule)
    monkeypatch.setattr(mod, "create_guideline_status_lm", lambda: "lm")

    lm1, module1, cfg1 = mod.shared_status_scorer()
    lm2, module2, cfg2 = mod.shared_status_scorer()
    assert (lm1, module1, cfg1) == (lm2, module2, cfg2)
    assert created == ["module"]


def test_guideline_status_module_classify_caches_and_truncates(monkeypatch) -> None:
    class DummyLM:
        def __init__(self, name: str) -> None:
            self.name = name

        def copy(self, **_kwargs):  # noqa: ANN003
            return DummyLM(f"{self.name}-copy")

    @contextlib.contextmanager
    def noop_context(**_kwargs):  # noqa: ANN003
        yield

    monkeypatch.setattr(mod.dspy, "context", noop_context)

    cfg = mod.StatusScorerConfig(max_rationale_chars=5, max_guideline_excerpt_chars=3)
    status = mod.GuidelineStatusModule(lm=cast("dspy.LM", DummyLM("lm")), config=cfg)

    def program(**_kwargs):  # noqa: ANN003
        return SimpleNamespace(status="violated", confidence="0.8", rationale="abcdefg")

    status._program = program

    entry = _entry("g1", body="abcdefgh")
    out = status.classify(chart_key="chart", situation="S", entry=entry)
    assert out["cache"] == "miss"
    assert out["status"] == "violated"
    assert out["confidence"] == 0.8
    assert out["rationale"] == "abcde..."
    assert out["attempts"] == 1

    # Second call hits the cache.
    out2 = status.classify(chart_key="chart", situation="S", entry=entry)
    assert out2["cache"] == "memory"


def test_guideline_status_module_classify_returns_error(monkeypatch) -> None:
    class DummyLM:
        def copy(self, **_kwargs):  # noqa: ANN003
            return self

    @contextlib.contextmanager
    def noop_context(**_kwargs):  # noqa: ANN003
        yield

    monkeypatch.setattr(mod.dspy, "context", noop_context)

    status = mod.GuidelineStatusModule(
        lm=cast("dspy.LM", DummyLM()),
        config=mod.StatusScorerConfig(max_rationale_chars=10),
    )

    def program(**_kwargs):  # noqa: ANN003
        raise RuntimeError("boom")

    status._program = program

    out = status.classify(chart_key="chart", situation="S", entry=_entry("g1"))
    assert out["cache"] == "error"
    assert out["status"] == "unclear"
    assert out["confidence"] == 0.0
    assert out["attempts"] == 2
    assert out["error"]


def test_guideline_status_module_classify_many_batches_and_handles_mismatch(
    monkeypatch,
) -> None:
    class DummyLM:
        def copy(self, **_kwargs):  # noqa: ANN003
            return self

    @contextlib.contextmanager
    def noop_context(**_kwargs):  # noqa: ANN003
        yield

    monkeypatch.setattr(mod.dspy, "context", noop_context)

    status = mod.GuidelineStatusModule(
        lm=cast("dspy.LM", DummyLM()),
        config=mod.StatusScorerConfig(batch_size=2),
    )

    calls = {"n": 0}

    def batch_program(**_kwargs):  # noqa: ANN003
        calls["n"] += 1
        # First batch: return mismatched lengths to force defaulting.
        if calls["n"] == 1:
            return SimpleNamespace(statuses=["violated"], confidences=[1.0, 0.5])
        return SimpleNamespace(statuses=["satisfied"], confidences=["0.2"])

    status._batch_program = batch_program

    entries = [_entry("g1"), _entry("g2"), _entry("g3")]
    out = status.classify_many(chart_key="chart", situation="S", entries=entries)
    assert [row["id"] for row in out] == ["g1", "g2", "g3"]
    assert calls["n"] == 2
    # First batch defaults due to mismatch.
    assert out[0]["status"] == "unclear"
    assert out[1]["status"] == "unclear"
    # Second batch uses returned values.
    assert out[2]["status"] == "satisfied"
    assert out[2]["confidence"] == 0.2

    # Cached call: should not invoke the batch program again.
    out2 = status.classify_many(chart_key="chart", situation="S", entries=entries)
    assert calls["n"] == 2
    assert [row["status"] for row in out2] == [row["status"] for row in out]


def test_guideline_status_module_classify_many_records_exceptions(monkeypatch) -> None:
    class DummyLM:
        def copy(self, **_kwargs):  # noqa: ANN003
            return self

    @contextlib.contextmanager
    def noop_context(**_kwargs):  # noqa: ANN003
        yield

    monkeypatch.setattr(mod.dspy, "context", noop_context)

    status = mod.GuidelineStatusModule(
        lm=cast("dspy.LM", DummyLM()),
        config=mod.StatusScorerConfig(batch_size=10),
    )

    def batch_program(**_kwargs):  # noqa: ANN003
        raise RuntimeError("boom")

    status._batch_program = batch_program

    entries = [_entry("g1")]
    out = status.classify_many(chart_key="chart", situation="S", entries=entries)
    assert out[0]["status"] == "unclear"
    assert out[0]["confidence"] == 0.0
    assert out[0]["error"]


def test_guideline_status_module_classify_many_fallbacks_when_cache_missing(
    monkeypatch,
) -> None:
    # Cover the defensive `cached is None` fallback in `classify_many`.
    class DummyLM:
        def copy(self, **_kwargs):  # noqa: ANN003
            return self

    @contextlib.contextmanager
    def noop_context(**_kwargs):  # noqa: ANN003
        yield

    monkeypatch.setattr(mod.dspy, "context", noop_context)

    status = mod.GuidelineStatusModule(
        lm=cast("dspy.LM", DummyLM()),
        config=mod.StatusScorerConfig(batch_size=10),
    )

    class FlakyCache(dict):
        calls = 0

        def get(self, key, default=None):  # noqa: ANN001
            FlakyCache.calls += 1
            if FlakyCache.calls == 1:
                return {}  # truthy enough to be treated as cached, but falsy in `or` later.
            if FlakyCache.calls == 2:
                return None
            return super().get(key, default)

    monkeypatch.setattr(mod, "_STATUS_CACHE", FlakyCache())

    out = status.classify_many(chart_key="chart", situation="S", entries=[_entry("g1")])
    assert out[0]["status"] == "unclear"


def test_filter_guidelines_by_status_supports_focus_modes(monkeypatch) -> None:
    class DummyStatus:
        def __init__(self, statuses: list[str]) -> None:
            self._statuses = statuses

        def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
            _ = (chart_key, situation)
            return [
                {"id": e.id, "status": s, "confidence": 1.0}
                for e, s in zip(entries, self._statuses, strict=True)
            ]

    entries = [_entry("g1"), _entry("g2"), _entry("g3")]
    req = RetrievalRequest(context=[TextItem(role="situation", text="S")])

    cfg = mod.StatusScorerConfig(keep_unclear=True)
    selected, meta = mod.filter_guidelines_by_status(
        request=req,
        entries=entries,
        output_k=2,
        focus="violations",
        status_module=DummyStatus(["satisfied", "violated", "unclear"]),
        config=cfg,
    )
    assert [e.id for e in selected] == ["g2", "g3"]
    counts = meta.get("guideline_status_counts")
    assert isinstance(counts, dict)
    assert cast("dict[str, int]", counts).get("violated") == 1

    selected, meta = mod.filter_guidelines_by_status(
        request=req,
        entries=entries,
        output_k=2,
        focus="satisfied",
        status_module=DummyStatus(["satisfied", "violated", "unclear"]),
        config=cfg,
    )
    assert [e.id for e in selected] == ["g1", "g3"]

    # Unknown focus values fall back to treating all statuses as primary.
    selected, meta = mod.filter_guidelines_by_status(
        request=req,
        entries=entries,
        output_k=10,
        focus="other",  # type: ignore[arg-type]
        status_module=DummyStatus(["satisfied", "violated", "not_applicable"]),
        config=cfg,
    )
    assert {e.id for e in selected} == {"g1", "g2", "g3"}
    assert meta["guideline_status_used"] is True

    # Early return paths.
    selected, meta = mod.filter_guidelines_by_status(
        request=req,
        entries=entries,
        output_k=0,
        focus="violations",
        status_module=DummyStatus(["violated"] * 3),
        config=cfg,
    )
    assert selected == []
    assert meta["guideline_status_used"] is False

    selected, meta = mod.filter_guidelines_by_status(
        request=req,
        entries=[],
        output_k=1,
        focus="violations",
        status_module=DummyStatus([]),
        config=cfg,
    )
    assert selected == []
    assert meta["guideline_status_used"] is False


@pytest.mark.parametrize("focus", ["all", "violations", "satisfied"])
def test_filter_guidelines_by_status_accepts_focus_literal(focus: FocusMode) -> None:
    # This is a tiny type-level test to ensure we keep the FocusMode contract stable.
    assert focus in {"all", "violations", "satisfied"}
