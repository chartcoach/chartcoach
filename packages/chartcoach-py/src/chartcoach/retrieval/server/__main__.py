from __future__ import annotations

import os

from chartcoach.retrieval.server.factory import create_app_from_env


def main() -> None:
    try:
        import uvicorn
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Install `chartcoach[retrieval-server]` to run the server."
        ) from e

    host = os.environ.get("CHARTCOACH_HOST", "127.0.0.1")
    port = int(os.environ.get("CHARTCOACH_PORT", "8000"))
    uvicorn.run(create_app_from_env(), host=host, port=port)


if __name__ == "__main__":  # pragma: no cover
    main()
