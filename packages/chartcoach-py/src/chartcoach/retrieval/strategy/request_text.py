from __future__ import annotations

from chartcoach.retrieval.strategy.types import RetrievalRequest, TextItem


def get_text_by_role(request: RetrievalRequest, *, role: str) -> str | None:
    for item in request.context:
        if isinstance(item, TextItem) and item.role == role:
            return item.text
    return None


def require_text_by_role(request: RetrievalRequest, *, role: str) -> str:
    text = get_text_by_role(request, role=role)
    if text is None:
        raise ValueError(f"Missing required TextItem with role={role!r}.")
    return text


def build_situation_with_query(
    request: RetrievalRequest,
    *,
    situation_role: str = "situation",
    query_role: str = "query",
) -> str:
    """Build the primary query text from a request.

    This mirrors the guideline-browser adapter behavior: treat "situation" as the
    main prompt and append the optional "query" field in a consistent format.
    """

    situation = require_text_by_role(request, role=situation_role)
    query = (get_text_by_role(request, role=query_role) or "").strip()
    if not query:
        return situation
    return f"{situation}\n\nQuery:\n{query}"
