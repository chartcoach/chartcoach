from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict, Field

from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest, TextItem


_CONTEXT_ROLES: tuple[str, ...] = (
    "audience",
    "medium",
    "constraints",
    "domain",
    "risk_tolerance",
    "time_budget",
)

_ROLE_LABELS: dict[str, str] = {
    "audience": "Audience",
    "medium": "Medium",
    "constraints": "Constraints",
    "domain": "Domain",
    "risk_tolerance": "Risk tolerance",
    "time_budget": "Time budget",
}


class SituationArtifact(BaseModel):
    model_config = ConfigDict(frozen=True)

    chart_image: ImageItem | None = None
    chart_spec: str | None = None
    chart_vision: str | None = None


class Situation(BaseModel):
    """Canonical, structured representation of a retrieval situation.

    This is a thin semantic layer over `RetrievalRequest.context` that makes the
    retrieval contract explicit and debuggable.
    """

    model_config = ConfigDict(frozen=True)

    title: str | None = None
    intent: str
    context: dict[str, str] = Field(default_factory=dict)
    query_meta: str | None = None
    lang: str = "en"
    artifact: SituationArtifact = Field(default_factory=SituationArtifact)

    @staticmethod
    def _first_text(request: RetrievalRequest, *, role: str) -> str | None:
        for item in request.context:
            if isinstance(item, TextItem) and item.role == role:
                text = item.text.strip()
                return text or None
        return None

    @staticmethod
    def _first_image(request: RetrievalRequest, *, role: str) -> ImageItem | None:
        for item in request.context:
            if isinstance(item, ImageItem) and item.role == role:
                return item
        return None

    @classmethod
    def from_request(cls, request: RetrievalRequest) -> "Situation":
        title = cls._first_text(request, role="title")
        intent = cls._first_text(request, role="intent") or cls._first_text(
            request, role="situation"
        )
        if not intent:
            raise ValueError("Missing required situation intent text (role=intent).")

        query_meta = cls._first_text(request, role="query")
        chart_spec = cls._first_text(request, role="chart_spec")
        chart_vision = cls._first_text(request, role="chart_vision")
        chart_image = cls._first_image(request, role="chart")

        context: dict[str, str] = {}
        for role in _CONTEXT_ROLES:
            value = cls._first_text(request, role=role)
            if value:
                context[role] = value

        return cls(
            title=title,
            intent=intent,
            context=context,
            query_meta=query_meta,
            lang=request.lang or "en",
            artifact=SituationArtifact(
                chart_image=chart_image,
                chart_spec=chart_spec,
                chart_vision=chart_vision,
            ),
        )

    def to_query_text(self, *, include_chart_vision: bool = True) -> str:
        """Render a stable, debuggable query text used for retrieval."""

        # Keep the title+intent backbone compatible with existing retrieval
        # baselines, then append typed facets in clearly demarcated blocks.
        base = (
            f"{self.title}\n\n{self.intent}".strip()
            if self.title
            else self.intent.strip()
        )

        context_lines: list[str] = []
        for role in _CONTEXT_ROLES:
            value = (self.context.get(role) or "").strip()
            if value:
                label = _ROLE_LABELS.get(role, role)
                context_lines.append(f"{label}: {value}")

        out = base
        if context_lines:
            out = f"{out}\n\nContext:\n" + "\n".join(context_lines)

        if include_chart_vision:
            vision = (self.artifact.chart_vision or "").strip()
            if vision:
                out = f"{out}\n\nChart image notes:\n{vision}"

        return out.strip()


@dataclass(frozen=True, slots=True)
class SituationTextParts:
    base: str
    with_chart_vision: str


def situation_text_parts(request: RetrievalRequest) -> SituationTextParts:
    """Convenience wrapper returning both base and vision-enriched query strings."""

    situation = Situation.from_request(request)
    return SituationTextParts(
        base=situation.to_query_text(include_chart_vision=False),
        with_chart_vision=situation.to_query_text(include_chart_vision=True),
    )


def iter_context_roles() -> Iterable[str]:
    return iter(_CONTEXT_ROLES)
