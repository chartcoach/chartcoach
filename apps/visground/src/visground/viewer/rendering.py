from __future__ import annotations

import base64
import io
from dataclasses import dataclass, field
from typing import Any, Final

from PIL import Image

from visground.datasets import VisEvalDataset, VisGroundDataset
from visground.generation.backends import resolve_visualization_backend

_DEFAULT_IMAGE_VARIANTS: Final[dict[str, tuple[tuple[int, int], int, bool]]] = {
    "panel": ((720, 540), 82, True),
    "hover": ((1800, 1400), 86, False),
    "detail": ((2200, 1800), 88, False),
}


def read_or_render_chart_image(
    store: VisGroundDataset,
    dataset: VisEvalDataset,
    *,
    visgen_id: str,
    vis_id: str,
    grammar: str,
    code: str,
) -> Image.Image:
    if store.chart_exists(visgen_id):
        with store.read_chart_image(visgen_id) as cached_image:
            return cached_image.copy()

    backend = resolve_visualization_backend(grammar, dataset)
    chart = backend.materialize_visualization(vis_id, code)
    image = backend.rasterize(chart)
    store.write_chart_image(visgen_id, image)
    return image


@dataclass
class ChartImageService:
    store: VisGroundDataset
    dataset: VisEvalDataset
    image_variants: dict[str, tuple[tuple[int, int], int, bool]] = field(
        default_factory=lambda: dict(_DEFAULT_IMAGE_VARIANTS)
    )

    def __post_init__(self) -> None:
        self._encoded_cache: dict[tuple[str, str], str] = {}
        self._metadata_cache: dict[str, dict[str, Any]] = {}
        self._backend_cache: dict[str, Any] = {}

    def _backend(self, grammar: str) -> Any:
        if grammar not in self._backend_cache:
            self._backend_cache[grammar] = resolve_visualization_backend(
                grammar,
                self.dataset,
            )
        return self._backend_cache[grammar]

    def image_data_url(self, candidate: dict[str, Any], variant: str) -> str:
        if variant not in self.image_variants:
            raise ValueError(f"Unsupported viewer image variant '{variant}'.")
        cache_key = (candidate["visgen_id"], variant)
        if cache_key not in self._encoded_cache:
            size, quality, pad_to_canvas = self.image_variants[variant]
            image = self._read_or_render(candidate)
            self._encoded_cache[cache_key] = image_to_data_url(
                image,
                max_size=size,
                quality=quality,
                pad_to_canvas=pad_to_canvas,
            )
        return self._encoded_cache[cache_key]

    def image_metadata(self, candidate: dict[str, Any]) -> dict[str, Any]:
        cache_key = candidate["visgen_id"]
        if cache_key not in self._metadata_cache:
            image = self._read_or_render(candidate)
            self._metadata_cache[cache_key] = image_metadata(image)
        return self._metadata_cache[cache_key]

    def _read_or_render(self, candidate: dict[str, Any]) -> Image.Image:
        if self.store.chart_exists(candidate["visgen_id"]):
            with self.store.read_chart_image(candidate["visgen_id"]) as image:
                return image.copy()

        backend = self._backend(candidate["grammar"])
        chart = backend.materialize_visualization(
            candidate["vis_id"],
            candidate["code"],
        )
        image = backend.rasterize(chart)
        self.store.write_chart_image(candidate["visgen_id"], image)
        return image


def image_to_data_url(
    image: Image.Image,
    *,
    max_size: tuple[int, int],
    quality: int,
    pad_to_canvas: bool = False,
) -> str:
    normalized = _normalize_image(image)
    contained = normalized.copy()
    contained.thumbnail(max_size, Image.Resampling.LANCZOS)
    output = contained
    if pad_to_canvas:
        output = Image.new("RGB", max_size, "white")
        x = (max_size[0] - contained.size[0]) // 2
        y = (max_size[1] - contained.size[1]) // 2
        output.paste(contained, (x, y))
    buffer = io.BytesIO()
    output.save(
        buffer,
        format="JPEG",
        quality=quality,
        optimize=False,
        progressive=False,
    )
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


def image_metadata(image: Image.Image) -> dict[str, Any]:
    width, height = image.size
    aspect_ratio = width / height if height else 1.0
    aspect_kind = "standard"
    if aspect_ratio > 1.35:
        aspect_kind = "landscape"
    elif aspect_ratio < 0.75:
        aspect_kind = "portrait"
    return {
        "width": width,
        "height": height,
        "aspect_ratio": round(aspect_ratio, 4),
        "aspect_kind": aspect_kind,
        "is_extreme_aspect": aspect_ratio > 3 or aspect_ratio < (1 / 3),
    }


def _normalize_image(image: Image.Image) -> Image.Image:
    if image.mode == "RGB":
        return image
    if image.mode not in {"RGBA", "LA"}:
        return image.convert("RGB")

    background = Image.new("RGB", image.size, "white")
    alpha = image.getchannel("A")
    background.paste(image.convert("RGBA"), mask=alpha)
    return background
