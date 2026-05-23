from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .spec import ViewerConfig


def guideline_detail(
    guideline_id: str,
    *,
    config: ViewerConfig,
) -> dict[str, Any]:
    detail = config.guideline_details_by_id.get(guideline_id, {})
    title = detail.get("title") or guideline_id.replace("-", " ").strip().title()
    description = detail.get("description") or ""
    sources = [
        str(value).strip()
        for value in (detail.get("sources") or [])
        if str(value).strip()
    ]
    return {
        "id": guideline_id,
        "title": str(title),
        "url": _guideline_url(detail=detail),
        "description": str(description),
        "sources": sources,
    }


def _guideline_url(
    *,
    detail: Mapping[str, Any],
) -> str | None:
    if url := str(detail.get("url") or "").strip():
        return url
    return None
