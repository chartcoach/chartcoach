from __future__ import annotations

from io import BytesIO
from pathlib import Path

import dspy

from .types import ImageItem, RetrievalRequest, TextItem


def get_text_by_role(request: RetrievalRequest, role: str) -> str | None:
    for item in request.context:
        if isinstance(item, TextItem) and item.role == role:
            return item.text
    return None


def require_text_by_role(request: RetrievalRequest, role: str) -> str:
    text = get_text_by_role(request, role=role)
    if text is None:
        raise ValueError(f"Missing required TextItem with role={role!r}.")
    return text


def get_image_item_by_role(request: RetrievalRequest, role: str) -> ImageItem | None:
    for item in request.context:
        if isinstance(item, ImageItem) and item.role == role:
            return item
    return None


def require_image_item_by_role(request: RetrievalRequest, role: str) -> ImageItem:
    item = get_image_item_by_role(request, role=role)
    if item is None:
        raise ValueError(f"Missing required ImageItem with role={role!r}.")
    return item


def image_item_to_dspy_image(item: ImageItem) -> dspy.Image:
    if item.data is not None:
        from PIL import Image as PILImage

        pil_img = PILImage.open(BytesIO(item.data))
        return dspy.Image(pil_img)

    if not item.uri:
        raise ValueError("ImageItem must have either `data` bytes or a `uri`.")

    if item.uri.startswith("file://"):
        return dspy.Image(item.uri.removeprefix("file://"))

    uri_path = Path(item.uri)
    if uri_path.exists():
        return dspy.Image(str(uri_path))

    return dspy.Image(item.uri)
