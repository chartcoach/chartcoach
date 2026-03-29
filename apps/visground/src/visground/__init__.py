"""Public entrypoints for `visground` benchmark assembly."""

from .datasets import VISGROUND_DATA_ROOT, VisEvalDataset, VisJudgeBenchDataset

__all__ = [
    "VISGROUND_DATA_ROOT",
    "VisEvalDataset",
    "VisJudgeBenchDataset",
]

try:
    from .viewer import VisGroundViewer as _VisGroundViewer
except Exception:
    VisGroundViewer: object | None = None
else:
    VisGroundViewer = _VisGroundViewer
    __all__.append("VisGroundViewer")
