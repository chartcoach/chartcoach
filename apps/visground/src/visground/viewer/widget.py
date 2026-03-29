from __future__ import annotations

import os
from pathlib import Path

from .backend import VisGroundViewerBackend


def _resolve_viewer_esm() -> str | Path:
    dev_url = os.getenv("VISGROUND_VIEWER_DEV_URL")
    if dev_url:
        return dev_url
    return Path(__file__).parent / "_static" / "anywidget" / "index.js"


class VisGroundViewer(VisGroundViewerBackend):
    _esm = _resolve_viewer_esm()
    _css = ""


__all__ = ["VisGroundViewer"]
