from __future__ import annotations

import contextlib
import os
from types import SimpleNamespace
from typing import TYPE_CHECKING, cast

import pytest

from chartcoach.retrieval.strategy.pipelines import vision as mod
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest, TextItem

if TYPE_CHECKING:
    import dspy


@pytest.fixture(autouse=True)
def _clear_vision_cache() -> None:
    mod._VISION_CACHE.clear()


def test_mime_to_suffix_variants() -> None:
    assert mod._mime_to_suffix(None) == ".img"
    assert mod._mime_to_suffix("") == ".img"
    assert mod._mime_to_suffix("image/png") == ".png"
    assert mod._mime_to_suffix("image/jpeg") == ".jpg"
    assert mod._mime_to_suffix("image/jpg") == ".jpg"
    assert mod._mime_to_suffix("image/webp") == ".webp"
    assert mod._mime_to_suffix("application/octet-stream") == ".img"


def test_searcher_build_query_text_includes_chart_vision() -> None:
    req = RetrievalRequest(
        context=[
            TextItem(role="title", text="T"),
            TextItem(role="situation", text="S"),
            TextItem(role="chart_vision", text="notes"),
        ]
    )
    assert "Chart image notes:" in GuidelineSearcher.build_query_text(req)


def test_chart_image_from_request_supports_uri_and_bytes(monkeypatch, tmp_path) -> None:
    seen: dict[str, str] = {}

    class DummyImage:
        @staticmethod
        def from_url(url: str) -> str:
            seen["url"] = url
            return f"URL:{url}"

        @staticmethod
        def from_file(path: str) -> str:
            seen["path"] = path
            return f"FILE:{path}"

    monkeypatch.setattr(mod.dspy, "Image", DummyImage)

    req = RetrievalRequest(
        context=[ImageItem(role="chart", uri="http://example.com/x.png")]
    )
    image, fp = mod._chart_image_from_request(req)
    assert image == "URL:http://example.com/x.png"
    assert fp and fp.startswith("uri:")

    # Bytes path writes a temp file; remove it after the call.
    data = b"abc123"
    req = RetrievalRequest(
        context=[ImageItem(role="chart", data=data, mime="image/png")]
    )
    image, fp = mod._chart_image_from_request(req)
    assert isinstance(image, str) and image.startswith("FILE:")
    assert fp and fp.startswith("bytes:")
    assert "path" in seen
    os.unlink(seen["path"])

    req = RetrievalRequest(context=[TextItem(role="situation", text="S")])
    image, fp = mod._chart_image_from_request(req)
    assert image is None
    assert fp is None


def test_clean_list_coerces_strings_and_limits() -> None:
    cfg = mod.ChartVisionConfig(enabled=True)

    class DummyLM:
        def copy(self, **_kwargs):  # noqa: ANN003
            return self

    vision = mod.ChartVisionModule(vlm=cast("dspy.LM", DummyLM()), config=cfg)

    assert vision._clean_list([" a ", "", "b", 1], limit=10) == ["a", "b"]
    assert vision._clean_list(" x ", limit=10) == ["x"]
    assert vision._clean_list(None, limit=10) == []
    assert vision._clean_list(["a", "b"], limit=0) == []


def test_chart_vision_analyze_disabled_and_no_image(monkeypatch) -> None:
    class DummyLM:
        def copy(self, **_kwargs):  # noqa: ANN003
            return self

    vision = mod.ChartVisionModule(
        vlm=cast("dspy.LM", DummyLM()), config=mod.ChartVisionConfig(enabled=False)
    )
    summary, meta = vision.analyze(
        RetrievalRequest(context=[TextItem(role="situation", text="S")]),
        base_situation="S",
    )
    assert summary is None
    assert meta["chart_vision_enabled"] is False
    assert meta["chart_vision_used"] is False

    vision = mod.ChartVisionModule(
        vlm=cast("dspy.LM", DummyLM()), config=mod.ChartVisionConfig(enabled=True)
    )
    summary, meta = vision.analyze(
        RetrievalRequest(context=[TextItem(role="situation", text="S")]),
        base_situation="S",
    )
    assert summary is None
    assert meta["chart_vision_enabled"] is True
    assert meta["chart_vision_used"] is False
    assert meta["chart_vision_reason"] == "no_chart_image"


def test_chart_vision_analyze_respects_existing_chart_vision(monkeypatch) -> None:
    class DummyLM:
        def copy(self, **_kwargs):  # noqa: ANN003
            return self

    # If the request already contains chart_vision, we should not call the program.
    vision = mod.ChartVisionModule(
        vlm=cast("dspy.LM", DummyLM()), config=mod.ChartVisionConfig(enabled=True)
    )

    def boom(**_kwargs):  # noqa: ANN003
        raise AssertionError("Should not be called")

    vision._program = boom

    monkeypatch.setattr(
        mod.dspy, "Image", SimpleNamespace(from_url=lambda _u: object())
    )

    req = RetrievalRequest(
        context=[
            TextItem(role="situation", text="S"),
            TextItem(role="chart_vision", text="Existing notes"),
            ImageItem(role="chart", uri="http://example.invalid/x.png"),
        ]
    )
    summary, meta = vision.analyze(req, base_situation="S")
    assert summary == "Existing notes"
    assert meta["chart_vision_reason"] == "already_present"


def test_chart_vision_analyze_caches_and_retries(monkeypatch) -> None:
    class DummyLM:
        def __init__(self, name: str) -> None:
            self.name = name

        def copy(self, **_kwargs):  # noqa: ANN003
            return DummyLM(f"{self.name}-copy")

    @contextlib.contextmanager
    def noop_context(**_kwargs):  # noqa: ANN003
        yield

    monkeypatch.setattr(mod.dspy, "context", noop_context)
    monkeypatch.setattr(
        mod.dspy, "Image", SimpleNamespace(from_url=lambda _u: object())
    )

    vision = mod.ChartVisionModule(
        vlm=cast("dspy.LM", DummyLM("lm")), config=mod.ChartVisionConfig(enabled=True)
    )
    calls = {"n": 0}

    def program(**_kwargs):  # noqa: ANN003
        calls["n"] += 1
        if calls["n"] == 1:
            raise RuntimeError("boom")
        return SimpleNamespace(
            chart_type="line chart",
            marks=[" lines ", "", "points"],
            encodings="x=time",
            layout=[],
            visible_text=["GDP", " "],
            salient_issues=[" low contrast ", "clutter"],
            search_keywords=["time series", "paired values", "delta encoding"],
            vision_summary="Short summary.",
        )

    vision._program = program

    req = RetrievalRequest(
        context=[
            TextItem(role="situation", text="S"),
            ImageItem(role="chart", uri="http://x"),
        ]
    )
    summary, meta = vision.analyze(req, base_situation="S")
    assert summary == "Short summary."
    assert meta["chart_vision_used"] is True
    assert meta["chart_vision_attempts"] == 2
    assert meta["chart_type"] == "line chart"
    assert meta["marks"] == ["lines", "points"]

    # Second call should hit the in-memory cache (no more program calls).
    summary, meta = vision.analyze(req, base_situation="S")
    assert summary == "Short summary."
    assert meta["chart_vision_cache"] == "memory"
    assert calls["n"] == 2


def test_chart_vision_analyze_returns_error_meta(monkeypatch) -> None:
    class DummyLM:
        def copy(self, **_kwargs):  # noqa: ANN003
            return self

    @contextlib.contextmanager
    def noop_context(**_kwargs):  # noqa: ANN003
        yield

    monkeypatch.setattr(mod.dspy, "context", noop_context)
    monkeypatch.setattr(
        mod.dspy, "Image", SimpleNamespace(from_url=lambda _u: object())
    )

    vision = mod.ChartVisionModule(
        vlm=cast("dspy.LM", DummyLM()), config=mod.ChartVisionConfig(enabled=True)
    )

    def program(**_kwargs):  # noqa: ANN003
        raise RuntimeError("boom")

    vision._program = program

    req = RetrievalRequest(
        context=[
            TextItem(role="situation", text="S"),
            ImageItem(role="chart", uri="http://x"),
        ]
    )
    summary, meta = vision.analyze(req, base_situation="S")
    assert summary is None
    assert meta["chart_vision_used"] is False
    assert meta["chart_vision_attempts"] == 2
    assert meta["chart_vision_error"]


def test_format_and_with_chart_vision_truncates(monkeypatch) -> None:
    class DummyLM:
        def copy(self, **_kwargs):  # noqa: ANN003
            return self

    vision = mod.ChartVisionModule(
        vlm=cast("dspy.LM", DummyLM()),
        config=mod.ChartVisionConfig(enabled=True, max_text_chars=20),
    )

    def analyze(_request, *, base_situation):  # noqa: ANN001, ARG001
        return (
            "This summary is definitely longer than twenty characters.",
            {
                "chart_type": "bar chart",
                "search_keywords": ["a", "b"],
                "encodings": ["x=time", "y=value"],
                "salient_issues": ["c"],
            },
        )

    vision.analyze = analyze  # type: ignore[method-assign]

    req = RetrievalRequest(context=[TextItem(role="situation", text="S")])
    out_req, meta = mod.with_chart_vision(req, base_situation="S", vision=vision)
    assert meta["chart_type"] == "bar chart"
    chart_notes = [
        i
        for i in out_req.context
        if isinstance(i, TextItem) and i.role == "chart_vision"
    ]
    assert chart_notes
    assert chart_notes[0].text.endswith("...")

    # If analysis yields no text, the request is returned unchanged.
    def analyze_empty(_request, *, base_situation):  # noqa: ANN001, ARG001
        return (None, {})

    vision.analyze = analyze_empty  # type: ignore[method-assign]
    out_req, meta = mod.with_chart_vision(req, base_situation="S", vision=vision)
    assert out_req is req
    assert meta == {}
