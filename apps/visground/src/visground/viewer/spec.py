from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, Mapping, Sequence


@dataclass(frozen=True, slots=True)
class ViewerDimensionSpec:
    id: str
    label: str
    null_label: str = "None"
    none_value_mode: Literal["null", "all"] = "null"
    aliases: Mapping[str, str] = field(default_factory=dict)
    order: Mapping[str, int] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ViewerLayout:
    row_dimension: str
    column_dimension: str
    group_dimension: str | None = None


@dataclass(frozen=True, slots=True)
class ViewerConfig:
    case_id_field: str
    dimensions: Sequence[ViewerDimensionSpec]
    filter_dimensions: Sequence[str]
    axis_dimensions: Sequence[str]
    default_filters: Mapping[str, str | None]
    default_layout: ViewerLayout
    image_base_url: str
    guideline_details_by_id: Mapping[str, Mapping[str, Any]] = field(
        default_factory=dict
    )
    case_label_field: str | None = None
    search_fields: Sequence[str] = ()

    def __post_init__(self) -> None:
        dimension_ids = {dimension.id for dimension in self.dimensions}

        if not self.image_base_url.strip():
            raise ValueError("image_base_url must not be empty.")
        if len(dimension_ids) != len(tuple(self.dimensions)):
            raise ValueError("dimension ids must be unique.")

        for dimension_id in [*self.filter_dimensions, *self.axis_dimensions]:
            if dimension_id not in dimension_ids:
                raise ValueError(f"Unknown viewer dimension '{dimension_id}'.")

        if self.default_layout.row_dimension not in self.axis_dimensions:
            raise ValueError("default row_dimension must be in axis_dimensions.")
        if self.default_layout.column_dimension not in self.axis_dimensions:
            raise ValueError("default column_dimension must be in axis_dimensions.")
        if self.default_layout.row_dimension == self.default_layout.column_dimension:
            raise ValueError("default row_dimension and column_dimension must differ.")
        if (
            self.default_layout.group_dimension is not None
            and self.default_layout.group_dimension not in self.axis_dimensions
        ):
            raise ValueError("default group_dimension must be in axis_dimensions.")
        if self.default_layout.group_dimension in {
            self.default_layout.row_dimension,
            self.default_layout.column_dimension,
        }:
            raise ValueError(
                "default group_dimension must differ from row_dimension and column_dimension."
            )

        for dimension_id in self.default_filters:
            if dimension_id not in self.filter_dimensions:
                raise ValueError(
                    f"default filter '{dimension_id}' is not in filter_dimensions."
                )


SCORE_BREAKDOWN_SPECS: tuple[dict[str, str], ...] = (
    {
        "id": "overall",
        "label": "Overall",
        "dimension": "overall",
    },
    {
        "id": "data_fidelity",
        "label": "Data Fidelity",
        "dimension": "faithfulness",
    },
    {
        "id": "semantic_readability",
        "label": "Semantic Readability",
        "dimension": "expressiveness",
    },
    {
        "id": "insight_discovery",
        "label": "Insight Discovery",
        "dimension": "expressiveness",
    },
    {
        "id": "design_style",
        "label": "Design Style",
        "dimension": "aesthetics",
    },
    {
        "id": "visual_composition",
        "label": "Visual Composition",
        "dimension": "aesthetics",
    },
    {
        "id": "color_harmony",
        "label": "Color Harmony",
        "dimension": "aesthetics",
    },
)


def dimension_map(config: ViewerConfig) -> dict[str, ViewerDimensionSpec]:
    return {dimension.id: dimension for dimension in config.dimensions}


def resolved_case_label_field(config: ViewerConfig) -> str:
    return config.case_label_field or config.case_id_field


def resolved_search_fields(config: ViewerConfig) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            [
                config.case_id_field,
                resolved_case_label_field(config),
                *config.search_fields,
            ]
        )
    )


def display_label(config: ViewerConfig, dimension: str, value: Any) -> str:
    spec = dimension_map(config).get(dimension)
    if spec is None:
        return str(value)
    if value is None:
        return spec.null_label
    if value in spec.aliases:
        return str(spec.aliases[value])
    return str(value)


def label_for_dimension(config: ViewerConfig, dimension: str | None) -> str:
    if dimension is None:
        return ""
    spec = dimension_map(config).get(dimension)
    return spec.label if spec is not None else dimension


__all__ = [
    "SCORE_BREAKDOWN_SPECS",
    "ViewerConfig",
    "ViewerDimensionSpec",
    "ViewerLayout",
    "dimension_map",
    "display_label",
    "label_for_dimension",
    "resolved_case_label_field",
    "resolved_search_fields",
]
