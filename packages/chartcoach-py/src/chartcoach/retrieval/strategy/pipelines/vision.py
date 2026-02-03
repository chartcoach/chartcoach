from __future__ import annotations

import hashlib
import re
import tempfile
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal
from urllib.request import Request, urlopen

from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.request_text import get_text_by_role
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest, TextItem

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


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


def _chart_image_item_from_request(
    request: RetrievalRequest,
) -> tuple[ImageItem | None, str | None]:
    """Return (chart_image_item, fingerprint) without downloading/decoding."""

    for item in request.context:
        if not isinstance(item, ImageItem) or item.role != "chart":
            continue
        if item.uri:
            return item, f"uri:{_sha256_text(item.uri)[:16]}"
        if item.data:
            return item, f"bytes:{_sha256_bytes(item.data)[:16]}"
    return None, None


def _download_image_to_tempfile(
    *,
    url: str,
    mime: str | None,
    timeout_seconds: float,
    max_bytes: int,
) -> str:
    """Download a remote image to a temp file with a hard timeout.

    A single slow/blocked URL must never stall a full evaluation run.
    """

    suffix = _mime_to_suffix(mime)
    req = Request(url, headers={"User-Agent": "chartcoach/0.1 (chart vision)"})
    with urlopen(req, timeout=timeout_seconds) as resp:  # noqa: S310
        data = resp.read(max(0, max_bytes + 1))
    if len(data) > max_bytes:
        raise ValueError(f"Remote image exceeds max_image_bytes={max_bytes}.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(data)
        return tmp.name


def _dspy_image_from_chart_item(
    item: ImageItem, *, config: ChartVisionConfig
) -> dspy.Image:
    if item.data:
        suffix = _mime_to_suffix(item.mime)
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(item.data)
            return dspy.Image.from_file(tmp.name)

    if item.uri:
        path = _download_image_to_tempfile(
            url=item.uri,
            mime=item.mime,
            timeout_seconds=float(config.download_timeout_seconds),
            max_bytes=int(config.max_image_bytes),
        )
        return dspy.Image.from_file(path)

    raise ValueError("Chart image item has neither uri nor data.")


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
    # Default to "append" to preserve backward-compatible behavior across strategies.
    # "fuse_tokens" is an explicit experiment mode for multi-channel fusion.
    integration: Literal["append", "fuse_tokens"] = "append"
    fusion_weight: float = 0.75
    download_timeout_seconds: float = 20.0
    max_image_bytes: int = 12_000_000
    max_keywords: int = 16
    max_issues: int = 10
    max_visible_text: int = 10
    max_tokens_chars: int = 700
    max_text_chars: int = 1400


class ChartVisionModule:
    def __init__(
        self,
        *,
        vlm: dspy.LM,
        config: ChartVisionConfig,
        cache: dict[str, dict[str, object]] | None = None,
    ) -> None:
        self._vlm = vlm
        self._config = config
        self._cache = cache if cache is not None else {}
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

        # Request-level opt-out: allow callers to pass their own chart_vision.
        existing = (get_text_by_role(request, role="chart_vision") or "").strip()
        if existing:
            return existing, {
                "chart_vision_enabled": True,
                "chart_vision_used": False,
                "chart_vision_reason": "already_present",
            }

        item, fingerprint = _chart_image_item_from_request(request)
        if item is None:
            return None, {
                "chart_vision_enabled": True,
                "chart_vision_used": False,
                "chart_vision_reason": "no_chart_image",
            }

        key = _sha256_text(f"{fingerprint or '<chart>'}\n{base_situation}")[:16]
        cached = self._cache.get(key)
        if cached is not None:
            return str(cached.get("vision_summary") or "").strip() or None, {
                "chart_vision_enabled": True,
                "chart_vision_used": True,
                "chart_vision_cache": "memory",
                "chart_vision_key": key,
                **{k: v for k, v in cached.items() if k != "vision_summary"},
            }

        try:
            image = _dspy_image_from_chart_item(item, config=self._config)
        except Exception as e:  # noqa: BLE001
            return None, {
                "chart_vision_enabled": True,
                "chart_vision_used": False,
                "chart_vision_reason": "chart_image_load_error",
                "chart_vision_error": str(e),
                "chart_vision_key": key,
                "chart_vision_fingerprint": fingerprint,
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
        self._cache[key] = cached_payload

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


_TOKEN_RE = re.compile(r"[^a-z0-9]+")


def _canonical_token(text: str) -> str:
    return _TOKEN_RE.sub("_", (text or "").strip().lower()).strip("_")


def _canonical_chart_type(raw: str) -> str | None:
    text = (raw or "").strip().lower()
    if not text:
        return None
    if "scatter" in text or "point" in text:
        return "scatter"
    if "line" in text:
        return "line"
    if "bar" in text or "column" in text:
        return "bar"
    if "area" in text:
        return "area"
    if "pie" in text or "donut" in text:
        return "pie"
    if "hist" in text:
        return "histogram"
    if "box" in text:
        return "boxplot"
    if "heatmap" in text:
        return "heatmap"
    if "map" in text or "choropleth" in text:
        return "map"
    if "sankey" in text or "flow" in text:
        return "flow"
    return _canonical_token(text) or None


def _canonical_mark(raw: str) -> str | None:
    text = (raw or "").strip().lower()
    if not text:
        return None
    if "bar" in text or "column" in text:
        return "bar"
    if "line" in text:
        return "line"
    if "point" in text or "dot" in text or "circle" in text:
        return "point"
    if "area" in text:
        return "area"
    if "text" in text or "label" in text:
        return "text"
    if "ribbon" in text or "band" in text:
        return "ribbon"
    return _canonical_token(text) or None


_ISSUE_MAP: tuple[tuple[str, str], ...] = (
    ("overplot", "overplotting"),
    ("clutter", "clutter"),
    ("crowd", "clutter"),
    ("low contrast", "low_contrast"),
    ("contrast", "low_contrast"),
    ("legend", "legend_burden"),
    ("missing label", "missing_labels"),
    ("no label", "missing_labels"),
    ("label", "labeling"),
    ("axis", "axes"),
    ("tick", "axes"),
    ("small text", "small_text"),
    ("tiny", "small_text"),
    ("colorblind", "color_accessibility"),
    ("color blind", "color_accessibility"),
    ("palette", "color_accessibility"),
    ("log", "scale"),
    ("scale", "scale"),
)


def _canonical_issue(raw: str) -> str | None:
    text = (raw or "").strip().lower()
    if not text:
        return None
    for needle, label in _ISSUE_MAP:
        if needle in text:
            return label
    return None


def _format_chart_vision_tokens(meta: dict[str, object]) -> str | None:
    """Return a compact token-based representation of VLM outputs.

    The goal is stability (controlled vocabulary-ish) rather than exhaustiveness.
    """

    tokens: list[str] = []

    chart_type = _canonical_chart_type(str(meta.get("chart_type") or ""))
    if chart_type:
        tokens.append(f"chart_type {chart_type}")

    marks = meta.get("marks")
    if isinstance(marks, list):
        for raw in marks:
            mark = _canonical_mark(str(raw))
            if mark:
                tokens.append(f"mark {mark}")

    encodings = meta.get("encodings")
    if isinstance(encodings, list):
        for raw in encodings:
            encoding = str(raw or "").strip().lower()
            if not encoding:
                continue
            encoding = encoding.replace("\t", " ").replace("\n", " ").replace("\r", " ")
            encoding = " ".join(encoding.split())
            if len(encoding) > 80:
                encoding = encoding[:80].rstrip()
            tokens.append(f"encoding {encoding}")

    issues = meta.get("salient_issues")
    if isinstance(issues, list):
        for raw in issues:
            issue = _canonical_issue(str(raw))
            if issue:
                tokens.append(f"issue {issue}")

    keywords = meta.get("search_keywords")
    if isinstance(keywords, list):
        for raw in keywords:
            kw = _canonical_token(str(raw))
            if kw:
                tokens.append(f"keyword {kw}")

    seen: set[str] = set()
    stable: list[str] = []
    for token in tokens:
        if token in seen:
            continue
        seen.add(token)
        stable.append(token)
    stable.sort()

    text = "\n".join(stable).strip()
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


def prepare_chart_vision(
    request: RetrievalRequest,
    *,
    base_situation: str,
    vision: ChartVisionModule,
) -> tuple[RetrievalRequest, str | None, dict[str, object]]:
    """Prepare chart vision data for downstream strategies.

    Returns:
    - request: possibly enriched (integration=append).
    - vision_tokens_query: tokenized query string (integration=fuse_tokens).
    - meta: telemetry.
    """

    summary, meta = vision.analyze(request, base_situation=base_situation)
    meta = {"chart_vision_integration": vision.config.integration, **meta}

    if vision.config.integration == "append":
        vision_text = _format_chart_vision_text(summary, meta)
        if not vision_text:
            return request, None, meta
        max_chars = max(0, int(getattr(vision.config, "max_text_chars", 0)))
        if max_chars and len(vision_text) > max_chars:
            vision_text = vision_text[:max_chars].rstrip() + "..."
        enriched_context = [
            *request.context,
            TextItem(role="chart_vision", text=vision_text, lang=request.lang),
        ]
        return request.model_copy(update={"context": enriched_context}), None, meta

    tokens_text = _format_chart_vision_tokens(meta)
    if not tokens_text:
        return request, None, meta
    max_chars = max(0, int(getattr(vision.config, "max_tokens_chars", 0)))
    if max_chars and len(tokens_text) > max_chars:
        tokens_text = tokens_text[:max_chars].rstrip() + "..."
    meta["chart_vision_tokens_used"] = True
    return request, tokens_text, meta
