"""Public entrypoints for `visground` benchmark assembly."""

from .cohorts import VisEvalCohortBuilder
from .data_profile import compact_profile, interestingness_score, profile_dataframe
from .datasets import VISGROUND_DATA_ROOT, VisEvalDataset, VisJudgeBenchDataset

__all__ = [
    "VISGROUND_DATA_ROOT",
    "VisEvalCohortBuilder",
    "VisEvalDataset",
    "VisJudgeBenchDataset",
    "compact_profile",
    "interestingness_score",
    "profile_dataframe",
]

try:
    from .viewer import VisGroundViewer as _VisGroundViewer
except Exception:
    VisGroundViewer: object | None = None
else:
    VisGroundViewer = _VisGroundViewer
    __all__.append("VisGroundViewer")
