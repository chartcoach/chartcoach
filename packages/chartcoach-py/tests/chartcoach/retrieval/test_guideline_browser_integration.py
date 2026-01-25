from __future__ import annotations

import base64
import os
from pathlib import Path

import dspy
import pytest

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.retrieval import (
    GuidelineBrowserStrategy,
    ImageItem,
    RetrievalRequest,
    TextItem,
)


def _read_dotenv(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    env: dict[str, str] = {}
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, value = line.partition("=")
        if sep != "=":
            continue
        env[key.strip()] = value.strip()
    return env


@pytest.mark.skipif(
    os.environ.get("CHARTCOACH_RUN_INTEGRATION_TESTS") != "1",
    reason="Set CHARTCOACH_RUN_INTEGRATION_TESTS=1 to run.",
)
def test_react_grounded_vis_feedback_strategy_integration() -> None:
    repo_root = Path(__file__).resolve().parents[5]
    env = _read_dotenv(repo_root / ".env")
    api_base = env.get("OPENAI_BASE_URL")
    api_key = env.get("OPENAI_API_KEY")
    if not api_base or not api_key:
        pytest.skip("Missing OPENAI_BASE_URL/OPENAI_API_KEY in repo-root .env")

    model = os.environ.get("CHARTCOACH_TEST_MODEL", "gpt-5.2")

    catalog = Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="Use descriptive titles",
                    description="Add a clear title.",
                    labels=["topic:annotation"],
                    body="Use a title.",
                ),
                references=["@article{a, title={A}}"],
            )
        ]
    )

    chart_bytes = base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+0pV0AAAAASUVORK5CYII="
    )
    request = RetrievalRequest(
        context=[
            ImageItem(role="chart", data=chart_bytes, mime="image/png"),
            TextItem(
                role="situation",
                text="I want to communicate a key comparison to seniors.",
            ),
            TextItem(role="chart_spec", text="{}"),
            TextItem(role="existing_chart_feedback", text=""),
        ]
    )

    lm = dspy.LM(model=model, api_base=api_base, api_key=api_key, cache=False)
    strategy = GuidelineBrowserStrategy(catalog=catalog, lm=lm)
    out = strategy(request=request)

    assert isinstance(out.catalog, Catalog)
    assert isinstance(out.meta.get("used_guideline_ids"), list)
