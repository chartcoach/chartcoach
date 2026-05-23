from __future__ import annotations

from pathlib import Path
from typing import TypedDict

from .spec import ViewerConfig, ViewerDimensionSpec


class ViewerRuntimeDimensionSpec(TypedDict):
    id: str
    label: str
    nullLabel: str
    noneValueMode: str
    aliases: dict[str, str]
    order: dict[str, int]


class ViewerRuntimeLayout(TypedDict):
    row_dimension: str
    column_dimension: str
    group_dimension: str | None


class ViewerRuntimeConfig(TypedDict):
    dimensions: list[ViewerRuntimeDimensionSpec]
    filter_dimensions: list[str]
    axis_dimensions: list[str]
    default_filters: dict[str, str | None]
    default_layout: ViewerRuntimeLayout


def serialize_viewer_runtime_dimension(
    dimension: ViewerDimensionSpec,
) -> ViewerRuntimeDimensionSpec:
    return {
        "id": dimension.id,
        "label": dimension.label,
        "nullLabel": dimension.null_label,
        "noneValueMode": dimension.none_value_mode,
        "aliases": dict(dimension.aliases),
        "order": dict(dimension.order),
    }


def serialize_viewer_runtime_config(config: ViewerConfig) -> ViewerRuntimeConfig:
    return {
        "dimensions": [
            serialize_viewer_runtime_dimension(dimension)
            for dimension in config.dimensions
        ],
        "filter_dimensions": list(config.filter_dimensions),
        "axis_dimensions": list(config.axis_dimensions),
        "default_filters": dict(config.default_filters),
        "default_layout": {
            "row_dimension": config.default_layout.row_dimension,
            "column_dimension": config.default_layout.column_dimension,
            "group_dimension": config.default_layout.group_dimension,
        },
    }


def viewer_runtime_config_sidecar_path(artifact_path: str | Path) -> Path:
    path = Path(artifact_path)
    return path.with_name(f"{path.stem}.config.json")


__all__ = [
    "ViewerRuntimeConfig",
    "ViewerRuntimeDimensionSpec",
    "ViewerRuntimeLayout",
    "serialize_viewer_runtime_config",
    "serialize_viewer_runtime_dimension",
    "viewer_runtime_config_sidecar_path",
]
