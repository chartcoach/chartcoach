from __future__ import annotations

from chartcoach.retrieval.server.factory import create_app_from_env
from chartcoach.env import load_env


def main() -> None:
    try:
        import uvicorn
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Install `chartcoach[retrieval-server]` to run the server."
        ) from e

    env = load_env().retrieval_server
    uvicorn.run(create_app_from_env(), host=env.host, port=env.port)


if __name__ == "__main__":  # pragma: no cover
    main()
