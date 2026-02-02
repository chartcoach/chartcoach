from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from chartcoach.catalog import CatalogEntry
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


GuidelineStatus = Literal["violated", "satisfied", "unclear", "not_applicable"]


_STATUS_CACHE: dict[tuple[str, str], dict[str, object]] = {}


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _chart_fingerprint(request: RetrievalRequest) -> str | None:
    """Return a stable per-chart key without downloading or decoding the image."""

    for item in request.context:
        if not isinstance(item, ImageItem) or item.role != "chart":
            continue

        if item.uri:
            return f"uri:{_sha256_text(item.uri)[:16]}"

        if item.data:
            return f"bytes:{_sha256_bytes(item.data)[:16]}"

    return None


def _coerce_status(raw: object) -> GuidelineStatus:
    if isinstance(raw, str):
        norm = raw.strip().lower().replace("-", "_")
        if norm in {"violated", "satisfied", "unclear", "not_applicable"}:
            return norm  # type: ignore[return-value]
    return "unclear"


def _coerce_confidence(raw: object) -> float:
    try:
        value = float(raw)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0
    return max(0.0, min(1.0, value))


def _guideline_excerpt(entry: CatalogEntry, *, max_chars: int) -> str:
    body = entry.guideline.body or ""
    text = body.strip()
    if not text:
        return ""
    if len(text) <= max_chars:
        return text
    return text[: max(0, int(max_chars))].rstrip() + "..."


class GuidelineStatusSignature(dspy.Signature):
    """Predict whether the described chart violates or satisfies a guideline."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent + optional chart image notes from a vision preprocessor. "
            "Use it only as intent/context; do not invent details that are not stated in the situation."
        )
    )

    guideline_title: str = dspy.InputField(desc="Guideline title (imperative advice).")
    guideline_description: str = dspy.InputField(desc="Guideline summary description.")
    guideline_labels: str = dspy.InputField(desc="Semicolon-separated guideline labels.")
    guideline_excerpt: str = dspy.InputField(
        desc="A short excerpt of the guideline body for extra context (may be empty)."
    )

    status: GuidelineStatus = dspy.OutputField(
        desc=(
            "One of: violated, satisfied, unclear, not_applicable. "
            "Use violated only when the chart likely breaks the guideline. "
            "Use satisfied only when the chart likely follows it. "
            "Use unclear when evidence is insufficient. "
            "Use not_applicable when the guideline is irrelevant to this chart."
        )
    )
    confidence: float = dspy.OutputField(
        desc="Confidence in [0,1]. Prefer low confidence when uncertain."
    )
    rationale: str = dspy.OutputField(
        desc="1-2 short sentences justifying the status based on visible evidence."
    )


@dataclass(frozen=True, slots=True)
class GuidelineStatusConfig:
    mode: Literal["all", "violations", "satisfied"] = "all"
    candidate_multiplier: int = 4
    keep_unclear: bool = True
    max_guideline_excerpt_chars: int = 900
    max_rationale_chars: int = 220


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


def guideline_status_config_from_env() -> GuidelineStatusConfig:
    mode = (os.environ.get("CHARTCOACH_GUIDELINE_STATUS_MODE") or "all").strip().lower()
    if mode not in {"all", "violations", "satisfied"}:
        mode = "all"

    return GuidelineStatusConfig(
        mode=mode,  # type: ignore[arg-type]
        candidate_multiplier=max(
            1, _int_env("CHARTCOACH_GUIDELINE_STATUS_CANDIDATE_MULTIPLIER", 4)
        ),
        keep_unclear=_bool_env("CHARTCOACH_GUIDELINE_STATUS_KEEP_UNCLEAR", True),
        max_guideline_excerpt_chars=max(
            0, _int_env("CHARTCOACH_GUIDELINE_STATUS_MAX_EXCERPT_CHARS", 900)
        ),
        max_rationale_chars=max(
            0, _int_env("CHARTCOACH_GUIDELINE_STATUS_MAX_RATIONALE_CHARS", 220)
        ),
    )


class GuidelineStatusModule:
    def __init__(self, *, lm: dspy.LM, config: GuidelineStatusConfig) -> None:
        self._lm = lm
        self._config = config
        self._program = dspy.Predict(GuidelineStatusSignature)

    def classify(
        self,
        *,
        chart_key: str,
        situation: str,
        entry: CatalogEntry,
    ) -> dict[str, object]:
        cache_key = (chart_key, entry.id)
        cached = _STATUS_CACHE.get(cache_key)
        if cached is not None:
            return {"id": entry.id, "cache": "memory", **cached}

        labels = "; ".join(entry.guideline.labels or [])
        excerpt = _guideline_excerpt(
            entry, max_chars=self._config.max_guideline_excerpt_chars
        )

        pred: dspy.Prediction | None = None
        error: str | None = None
        attempts = 0
        for lm in (self._lm, self._lm.copy(cache=False)):
            attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(
                        situation=situation,
                        guideline_title=entry.guideline.title,
                        guideline_description=entry.guideline.description,
                        guideline_labels=labels,
                        guideline_excerpt=excerpt,
                    )
                error = None
                break
            except Exception as e:  # noqa: BLE001
                error = str(e)

        if pred is None:
            out = {
                "status": "unclear",
                "confidence": 0.0,
                "rationale": (error or "LM request failed.")[
                    : self._config.max_rationale_chars
                ],
                "attempts": attempts,
                "error": error,
            }
            _STATUS_CACHE[cache_key] = out
            return {"id": entry.id, "cache": "error", **out}

        status = _coerce_status(getattr(pred, "status", None))
        confidence = _coerce_confidence(getattr(pred, "confidence", None))
        rationale = str(getattr(pred, "rationale", "") or "").strip()
        if len(rationale) > self._config.max_rationale_chars:
            rationale = rationale[: self._config.max_rationale_chars].rstrip() + "..."

        out = {
            "status": status,
            "confidence": confidence,
            "rationale": rationale,
            "attempts": attempts,
            "error": None,
        }
        _STATUS_CACHE[cache_key] = out
        return {"id": entry.id, "cache": "miss", **out}


def filter_guidelines_by_status(
    *,
    request: RetrievalRequest,
    entries: list[CatalogEntry],
    output_k: int,
    status_module: GuidelineStatusModule,
    config: GuidelineStatusConfig,
) -> tuple[list[CatalogEntry], dict[str, object]]:
    """Stable-filter retrieved guidelines by (likely) violation/satisfaction status.

    The status model is only used when config.mode != "all"; otherwise, we return
    the original ranking unchanged.
    """

    mode = config.mode
    if mode == "all" or output_k <= 0 or not entries:
        return entries[: max(0, int(output_k))], {
            "guideline_status_mode": mode,
            "guideline_status_used": False,
        }

    # Build enriched situation text without requiring a searcher instance.
    situation_text = GuidelineSearcher.build_query_text(request)

    chart_key = _chart_fingerprint(request) or f"text:{_sha256_text(situation_text)[:16]}"

    statuses: list[dict[str, object]] = []
    counts: dict[str, int] = {"violated": 0, "satisfied": 0, "unclear": 0, "not_applicable": 0}
    for entry in entries:
        scored = status_module.classify(
            chart_key=chart_key,
            situation=situation_text,
            entry=entry,
        )
        statuses.append(scored)
        s = str(scored.get("status") or "unclear")
        if s in counts:
            counts[s] += 1

    primary: set[str]
    if mode == "violations":
        primary = {"violated"}
    elif mode == "satisfied":
        primary = {"satisfied"}
    else:
        primary = {"violated", "satisfied", "unclear", "not_applicable"}

    selected: list[CatalogEntry] = []
    selected_ids: set[str] = set()

    def _take(status_set: set[str]) -> None:
        for entry, scored in zip(entries, statuses, strict=True):
            if entry.id in selected_ids:
                continue
            if str(scored.get("status") or "unclear") not in status_set:
                continue
            selected.append(entry)
            selected_ids.add(entry.id)
            if len(selected) >= output_k:
                return

    _take(primary)
    if config.keep_unclear and len(selected) < output_k:
        _take({"unclear"})
    if len(selected) < output_k:
        _take({"violated", "satisfied", "not_applicable"})

    selected = selected[: max(0, int(output_k))]
    status_by_id = {str(s["id"]): s for s in statuses if isinstance(s, dict) and s.get("id")}

    return selected, {
        "guideline_status_mode": mode,
        "guideline_status_used": True,
        "guideline_status_candidate_n": len(entries),
        "guideline_status_output_k": int(output_k),
        "guideline_status_counts": counts,
        "guideline_status_keep_unclear": bool(config.keep_unclear),
        "guideline_statuses": [
            {
                "id": entry.id,
                "status": status_by_id.get(entry.id, {}).get("status"),
                "confidence": status_by_id.get(entry.id, {}).get("confidence"),
            }
            for entry in selected
        ],
    }
