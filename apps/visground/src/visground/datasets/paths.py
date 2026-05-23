import os
import pathlib

import platformdirs

VISGROUND_DATA_ROOT = pathlib.Path(__file__).parent.parent.parent.parent / "data"


def default_visground_artifacts_root() -> pathlib.Path:
    override = os.getenv("VISGROUND_ARTIFACTS_ROOT")
    if override:
        return pathlib.Path(override).expanduser()
    return pathlib.Path(platformdirs.user_cache_dir("visground")) / "artifacts"


__all__ = ["VISGROUND_DATA_ROOT", "default_visground_artifacts_root"]
