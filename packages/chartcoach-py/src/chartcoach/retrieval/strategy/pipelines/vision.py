from __future__ import annotations

import hashlib
import os
import tempfile
from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.request_text import get_text_by_role
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest, TextItem

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


_VISION_CACHE: dict[str, dict[str, object]] = {}


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _mime_to_suffix(mime: str | None) -> str:
    if not mime:
        return ".img"
    lowered = mime.lower()
    if lowered in {"image/png"}:
        return ".png"
    if lowered in {"image/jpeg", "image/jpg"}:
        return ".jpg"
    if lowered in {"image/webp"}:
        return ".webp"
    return ".img"


def _chart_image_from_request(
    request: RetrievalRequest,
) -> tuple[dspy.Image | None, str | None]:
    """Return a DSPy image primitive for the chart image (if present), plus a stable fingerprint."""

    for item in request.context:
        if not isinstance(item, ImageItem) or item.role != "chart":
            continue

        if item.uri:
            return dspy.Image.from_url(item.uri), f"uri:{_sha256_text(item.uri)[:16]}"

        if item.data:
            suffix = _mime_to_suffix(item.mime)
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(item.data)
                return dspy.Image.from_file(
                    tmp.name
                ), f"bytes:{_sha256_bytes(item.data)[:16]}"

    return None, None


class ChartVisionSignature(dspy.Signature):
    """Extract retrieval-oriented chart characteristics from a chart image."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent describing the chart to improve. "
            "Use it to disambiguate the chart's intent, but do not hallucinate details not visible in the chart."
        )
    )
    image: dspy.Image = dspy.InputField(desc="The chart image to analyze.")

    chart_type: str = dspy.OutputField(
        desc="Best-effort chart type label (e.g., line chart, grouped bars, choropleth, sankey)."
    )
    marks: list[str] = dspy.OutputField(
        desc="Visible mark types (e.g., bars, lines, points, areas, ribbons, text)."
    )
    encodings: list[str] = dspy.OutputField(
        desc=(
            "Likely encodings as short phrases (e.g., 'x=time', 'y=rate', 'color=country', 'width=flow'). "
            "Only include what is visible or strongly implied by chart scaffolding (axes/legends)."
        )
    )
    layout: list[str] = dspy.OutputField(
        desc="Layout/structure cues (small multiples, facets, stacked panels, split axes, annotations)."
    )
    visible_text: list[str] = dspy.OutputField(
        desc="Short list of notable visible words/phrases (axis titles, legend items, units). Keep it short."
    )
    salient_issues: list[str] = dspy.OutputField(
        desc=(
            "Likely design issues detectable from the image (clutter, legend burden, low contrast, "
            "missing labels, confusing encodings). Avoid unverifiable claims."
        )
    )
    search_keywords: list[str] = dspy.OutputField(
        desc=(
            "Compact retrieval keywords/phrases that would help find visualization guidelines. "
            "Include chart-type terms and key task terms (compare, rank, show change, map, flows, etc)."
        )
    )
    vision_summary: str = dspy.OutputField(
        desc=(
            "A short paragraph summarizing the chart form and likely design concerns, written as retrieval context. "
            "Keep it concise (3-6 sentences)."
        )
    )


@dataclass(frozen=True, slots=True)
class ChartVisionConfig:
    enabled: bool = False
    max_keywords: int = 16
    max_issues: int = 10
    max_visible_text: int = 10
    max_text_chars: int = 1400


def _bool_env(name: str, default: bool) -> bool:
    raw = (os.environ.get(name) or "").strip().lower()
    if not raw:
        return default
    if raw in {"1", "true", "t", "yes", "y", "on"}:
        return True
    if raw in {"0", "false", "f", "no", "n", "off"}:
        return False
    return default


def _int_env(name: str, default: int) -> int:
    raw = (os.environ.get(name) or "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def chart_vision_config_from_env() -> ChartVisionConfig:
    return ChartVisionConfig(
        enabled=_bool_env("CHARTCOACH_CHART_VISION_ENABLED", False),
        max_keywords=_int_env("CHARTCOACH_CHART_VISION_MAX_KEYWORDS", 16),
        max_issues=_int_env("CHARTCOACH_CHART_VISION_MAX_ISSUES", 10),
        max_visible_text=_int_env("CHARTCOACH_CHART_VISION_MAX_VISIBLE_TEXT", 10),
        max_text_chars=_int_env("CHARTCOACH_CHART_VISION_MAX_TEXT_CHARS", 1400),
    )


class ChartVisionModule:
    def __init__(self, *, vlm: dspy.LM, config: ChartVisionConfig) -> None:
        self._vlm = vlm
        self._config = config
        self._program = dspy.Predict(ChartVisionSignature)

    @property
    def config(self) -> ChartVisionConfig:
        return self._config

    @staticmethod
    def _clean_list(raw: object, *, limit: int) -> list[str]:
        out: list[str] = []
        if isinstance(raw, list):
            for item in raw:
                if isinstance(item, str):
                    s = item.strip()
                    if s:
                        out.append(s)
        elif isinstance(raw, str) and raw.strip():
            out.append(raw.strip())
        return out[: max(0, int(limit))]

    def analyze(
        self, request: RetrievalRequest, *, base_situation: str
    ) -> tuple[str | None, dict[str, object]]:
        """Return (vision_summary_text, meta)."""

        if not self._config.enabled:
            return None, {"chart_vision_enabled": False, "chart_vision_used": False}

        image, fingerprint = _chart_image_from_request(request)
        if image is None:
            return None, {
                "chart_vision_enabled": True,
                "chart_vision_used": False,
                "chart_vision_reason": "no_chart_image",
            }

        # Request-level opt-out: allow callers to pass their own chart_vision.
        existing = (get_text_by_role(request, role="chart_vision") or "").strip()
        if existing:
            return existing, {
                "chart_vision_enabled": True,
                "chart_vision_used": False,
                "chart_vision_reason": "already_present",
            }

        key = _sha256_text(f"{fingerprint or '<chart>'}\n{base_situation}")[:16]
        cached = _VISION_CACHE.get(key)
        if cached is not None:
            return str(cached.get("vision_summary") or "").strip() or None, {
                "chart_vision_enabled": True,
                "chart_vision_used": True,
                "chart_vision_cache": "memory",
                "chart_vision_key": key,
                **{k: v for k, v in cached.items() if k != "vision_summary"},
            }

        pred: dspy.Prediction | None = None
        error: str | None = None
        attempts = 0
        for lm in (self._vlm, self._vlm.copy(cache=False)):
            attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(situation=base_situation, image=image)
                error = None
                break
            except Exception as e:  # noqa: BLE001
                error = str(e)

        if pred is None:
            return None, {
                "chart_vision_enabled": True,
                "chart_vision_used": False,
                "chart_vision_error": error,
                "chart_vision_attempts": attempts,
            }

        chart_type = str(getattr(pred, "chart_type", "") or "").strip()
        marks = self._clean_list(getattr(pred, "marks", None), limit=12)
        encodings = self._clean_list(getattr(pred, "encodings", None), limit=14)
        layout = self._clean_list(getattr(pred, "layout", None), limit=10)
        visible_text = self._clean_list(
            getattr(pred, "visible_text", None), limit=self._config.max_visible_text
        )
        issues = self._clean_list(
            getattr(pred, "salient_issues", None), limit=self._config.max_issues
        )
        keywords = self._clean_list(
            getattr(pred, "search_keywords", None), limit=self._config.max_keywords
        )
        summary = str(getattr(pred, "vision_summary", "") or "").strip()

        # Store a minimal cached payload (avoid huge blobs).
        cached_payload: dict[str, object] = {
            "chart_type": chart_type,
            "marks": marks,
            "encodings": encodings,
            "layout": layout,
            "visible_text": visible_text,
            "salient_issues": issues,
            "search_keywords": keywords,
        }
        if summary:
            cached_payload["vision_summary"] = summary
        _VISION_CACHE[key] = cached_payload

        return summary or None, {
            "chart_vision_enabled": True,
            "chart_vision_used": True,
            "chart_vision_cache": "miss",
            "chart_vision_key": key,
            "chart_vision_attempts": attempts,
            "chart_vision_error": None,
            **{k: v for k, v in cached_payload.items() if k != "vision_summary"},
        }


def _format_chart_vision_text(
    summary: str | None, meta: dict[str, object]
) -> str | None:
    chart_type = str(meta.get("chart_type") or "").strip()
    keywords = meta.get("search_keywords")
    encodings = meta.get("encodings")
    issues = meta.get("salient_issues")

    lines: list[str] = []
    if chart_type:
        lines.append(f"Chart type: {chart_type}")
    if isinstance(keywords, list) and keywords:
        joined = ", ".join(str(k).strip() for k in keywords if str(k).strip())
        if joined:
            lines.append(f"Search keywords: {joined}")
    if isinstance(encodings, list) and encodings:
        joined = ", ".join(str(e).strip() for e in encodings if str(e).strip())
        if joined:
            lines.append(f"Encodings: {joined}")
    if isinstance(issues, list) and issues:
        top: list[str] = []
        for item in issues:
            s = str(item).strip()
            if not s:
                continue
            top.append(s)
            if len(top) >= 5:
                break
        if top:
            lines.append(f"Likely issues: {', '.join(top)}")

    if summary and summary.strip():
        lines.append(summary.strip())

    text = "\n".join(lines).strip()
    return text or None


def with_chart_vision(
    request: RetrievalRequest,
    *,
    base_situation: str,
    vision: ChartVisionModule,
) -> tuple[RetrievalRequest, dict[str, object]]:
    summary, meta = vision.analyze(request, base_situation=base_situation)
    vision_text = _format_chart_vision_text(summary, meta)
    if not vision_text:
        return request, meta
    max_chars = max(0, int(getattr(vision.config, "max_text_chars", 0)))
    if max_chars and len(vision_text) > max_chars:
        vision_text = vision_text[:max_chars].rstrip() + "..."

    enriched_context = [
        *request.context,
        TextItem(role="chart_vision", text=vision_text, lang=request.lang),
    ]
    return request.model_copy(update={"context": enriched_context}), meta
