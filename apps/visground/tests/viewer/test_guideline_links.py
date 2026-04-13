from __future__ import annotations

import unittest

from visground.viewer.data import _guideline_detail
from visground.viewer.spec import ViewerConfig, ViewerDimensionSpec, ViewerLayout


def make_viewer_config(
    *, guideline_details_by_id: dict[str, dict[str, object]]
) -> ViewerConfig:
    return ViewerConfig(
        image_base_url="https://example.com/charts/",
        case_id_field="vis_id",
        dimensions=(
            ViewerDimensionSpec(id="model", label="Model"),
            ViewerDimensionSpec(id="grammar", label="Grammar"),
        ),
        filter_dimensions=(),
        axis_dimensions=("model", "grammar"),
        default_filters={},
        default_layout=ViewerLayout(
            row_dimension="model",
            column_dimension="grammar",
            group_dimension=None,
        ),
        guideline_details_by_id=guideline_details_by_id,
    )


class GuidelineLinkTests(unittest.TestCase):
    def test_guideline_detail_defaults_to_chartcoach_guideline_url(self) -> None:
        config = make_viewer_config(guideline_details_by_id={})

        detail = _guideline_detail("my-guideline", config=config)

        self.assertEqual(
            detail["url"],
            "https://chartcoach.github.io/guidelines/my-guideline",
        )

    def test_guideline_detail_keeps_explicit_url_override(self) -> None:
        config = make_viewer_config(
            guideline_details_by_id={
                "my-guideline": {
                    "title": "My Guideline",
                    "url": "https://example.com/custom-guideline",
                }
            }
        )

        detail = _guideline_detail("my-guideline", config=config)

        self.assertEqual(detail["url"], "https://example.com/custom-guideline")


if __name__ == "__main__":
    unittest.main()
