from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Protocol

from chartcoach.catalog import CatalogEntry
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.pipelines.focus import FocusMode
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


GuidelineStatus = Literal["violated", "satisfied", "unclear", "not_applicable"]


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
    guideline_labels: str = dspy.InputField(
        desc="Semicolon-separated guideline labels."
    )
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


class GuidelineStatusBatchSignature(dspy.Signature):
    """Predict statuses for a small batch of guidelines for the same chart."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent + optional chart image notes from a vision preprocessor. "
            "Use it only as intent/context; do not invent details that are not stated in the situation."
        )
    )
    guidelines: list[str] = dspy.InputField(
        desc=(
            "A list of guideline snippets. Each snippet starts with an `ID:` line, "
            "followed by Title/Description/Labels and an optional excerpt."
        )
    )

    statuses: list[GuidelineStatus] = dspy.OutputField(
        desc=(
            "A list of statuses aligned 1:1 with `guidelines` (same order, same length). "
            "Valid values: violated, satisfied, unclear, not_applicable."
        )
    )
    confidences: list[float] = dspy.OutputField(
        desc="A list of confidences in [0,1] aligned 1:1 with `guidelines`."
    )


@dataclass(frozen=True, slots=True)
class StatusScorerConfig:
    candidate_multiplier: int = 4
    keep_unclear: bool = True
    max_guideline_excerpt_chars: int = 900
    max_rationale_chars: int = 220
    batch_size: int = 10


@dataclass(frozen=True, slots=True)
class StatusScorer:
    lm: dspy.LM
    module: "GuidelineStatusModule"
    config: StatusScorerConfig


def create_status_scorer(*, lm: dspy.LM, config: StatusScorerConfig) -> StatusScorer:
    return StatusScorer(
        lm=lm, module=GuidelineStatusModule(lm=lm, config=config), config=config
    )


class GuidelineStatusModule:
    def __init__(
        self,
        *,
        lm: dspy.LM,
        config: StatusScorerConfig,
        cache: dict[tuple[str, str], dict[str, object]] | None = None,
    ) -> None:
        self._lm = lm
        self._config = config
        self._cache = cache if cache is not None else {}
        self._program = dspy.Predict(GuidelineStatusSignature)
        self._batch_program = dspy.Predict(GuidelineStatusBatchSignature)

    def _render_guideline_snippet(self, entry: CatalogEntry) -> str:
        labels = "; ".join(entry.guideline.labels or [])
        excerpt = _guideline_excerpt(
            entry, max_chars=self._config.max_guideline_excerpt_chars
        )
        parts = [
            f"ID: {entry.id}",
            f"Title: {entry.guideline.title}",
            f"Description: {entry.guideline.description}",
        ]
        if labels:
            parts.append(f"Labels: {labels}")
        if excerpt:
            parts.append(f"Excerpt: {excerpt}")
        return "\n".join(parts)

    def classify(
        self,
        *,
        chart_key: str,
        situation: str,
        entry: CatalogEntry,
    ) -> dict[str, object]:
        cache_key = (chart_key, entry.id)
        cached = self._cache.get(cache_key)
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
            self._cache[cache_key] = out
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
        self._cache[cache_key] = out
        return {"id": entry.id, "cache": "miss", **out}

    def classify_many(
        self,
        *,
        chart_key: str,
        situation: str,
        entries: list[CatalogEntry],
    ) -> list[dict[str, object]]:
        """Classify a list of entries, using a cached + batched LM strategy."""

        cached_by_id: dict[str, dict[str, object]] = {}
        missing: list[CatalogEntry] = []
        for entry in entries:
            cached = self._cache.get((chart_key, entry.id))
            if cached is not None:
                cached_by_id[entry.id] = cached
            else:
                missing.append(entry)

        if missing:
            batch_size = max(1, int(self._config.batch_size))
            for start in range(0, len(missing), batch_size):
                batch = missing[start : start + batch_size]
                snippets = [self._render_guideline_snippet(entry) for entry in batch]

                pred: dspy.Prediction | None = None
                error: str | None = None
                attempts = 0
                for lm in (self._lm, self._lm.copy(cache=False)):
                    attempts += 1
                    try:
                        with dspy.context(lm=lm):
                            pred = self._batch_program(
                                situation=situation, guidelines=snippets
                            )
                        error = None
                        break
                    except Exception as e:  # noqa: BLE001
                        error = str(e)

                raw_statuses = (
                    getattr(pred, "statuses", None) if pred is not None else None
                )
                raw_confidences = (
                    getattr(pred, "confidences", None) if pred is not None else None
                )

                statuses: list[GuidelineStatus] = []
                if isinstance(raw_statuses, list):
                    statuses = [_coerce_status(item) for item in raw_statuses]
                confidences: list[float] = []
                if isinstance(raw_confidences, list):
                    confidences = [_coerce_confidence(item) for item in raw_confidences]

                if len(statuses) != len(batch) or len(confidences) != len(batch):
                    statuses = [_coerce_status(None) for _ in batch]
                    confidences = [0.0] * len(batch)

                for entry, status, confidence in zip(
                    batch, statuses, confidences, strict=True
                ):
                    out = {
                        "status": status,
                        "confidence": confidence,
                        "rationale": "",
                        "attempts": attempts,
                        "error": error,
                    }
                    self._cache[(chart_key, entry.id)] = out
                    cached_by_id[entry.id] = out

        results: list[dict[str, object]] = []
        for entry in entries:
            cached = cached_by_id.get(entry.id) or self._cache.get(
                (chart_key, entry.id)
            )
            if cached is None:
                cached = {"status": "unclear", "confidence": 0.0, "rationale": ""}
            results.append({"id": entry.id, "cache": "memory", **cached})

        return results


class GuidelineStatusScorer(Protocol):
    def classify_many(
        self,
        *,
        chart_key: str,
        situation: str,
        entries: list[CatalogEntry],
    ) -> list[dict[str, object]]: ...


def filter_guidelines_by_status(
    *,
    request: RetrievalRequest,
    entries: list[CatalogEntry],
    output_k: int,
    focus: FocusMode,
    status_module: GuidelineStatusScorer,
    config: StatusScorerConfig,
) -> tuple[list[CatalogEntry], dict[str, object]]:
    """Stable-filter retrieved guidelines by (likely) violation/satisfaction status.

    The caller controls whether the returned set prioritizes violated or satisfied
    guidelines via `focus`. This function is intended to be invoked inside a
    strategy pipeline (not as a global eval post-processor).
    """

    if focus == "all" or output_k <= 0 or not entries:
        return entries[: max(0, int(output_k))], {
            "guideline_status_focus": focus,
            "guideline_status_used": False,
        }

    # Build enriched situation text without requiring a searcher instance.
    situation_text = GuidelineSearcher.build_query_text(request)

    chart_key = (
        _chart_fingerprint(request) or f"text:{_sha256_text(situation_text)[:16]}"
    )

    statuses = status_module.classify_many(
        chart_key=chart_key, situation=situation_text, entries=entries
    )
    counts: dict[str, int] = {
        "violated": 0,
        "satisfied": 0,
        "unclear": 0,
        "not_applicable": 0,
    }
    for scored in statuses:
        s = str(scored.get("status") or "unclear")
        if s in counts:
            counts[s] += 1

    primary: set[str]
    if focus == "violations":
        primary = {"violated"}
    elif focus == "satisfied":
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
    status_by_id = {
        str(s["id"]): s for s in statuses if isinstance(s, dict) and s.get("id")
    }

    return selected, {
        "guideline_status_focus": focus,
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
