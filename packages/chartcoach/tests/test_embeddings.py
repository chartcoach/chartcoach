from __future__ import annotations

import asyncio
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from importlib.metadata import version
from pathlib import Path
from threading import Thread

import pytest
from chartcoach import Catalog, open_catalog
from chartcoach.curation import EmbeddingProfile, build_release
from chartcoach.embeddings import OpenAICompatibleEmbeddings
from chartcoach.mcp import create_server
from lancedb.embeddings import get_registry
from mcp.types import CallToolResult

pytestmark = [pytest.mark.mcp, pytest.mark.search, pytest.mark.curation]


def test_native_compatible_embedding_profile_uses_environment_credentials(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    requests: list[tuple[str | None, dict[str, object]]] = []

    class Endpoint(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args: object) -> None:
            pass

        def do_POST(self) -> None:
            assert self.path == "/v1/embeddings"
            request = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            requests.append((self.headers.get("Authorization"), request))
            data = [
                {
                    "index": index,
                    "object": "embedding",
                    "embedding": [
                        1.0 if "direct" in text.lower() else 0.0,
                        1.0 if "label" in text.lower() else 0.0,
                        1.0,
                        1.0,
                    ],
                }
                for index, text in enumerate(request["input"])
            ]
            response = json.dumps(
                {
                    "object": "list",
                    "data": data,
                    "model": request["model"],
                    "usage": {"prompt_tokens": 1, "total_tokens": 1},
                }
            ).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

    endpoint = ThreadingHTTPServer(("127.0.0.1", 0), Endpoint)
    thread = Thread(target=endpoint.serve_forever, daemon=True)
    thread.start()
    variable = "CHARTCOACH_TEST_EMBEDDING_KEY"
    registry = get_registry()
    registry.set_var(variable, "producer-secret")
    try:
        embedding = OpenAICompatibleEmbeddings.create(
            name="provider/arbitrary-embedding-model",
            dim=4,
            base_url=f"http://127.0.0.1:{endpoint.server_port}/v1",
            api_key=f"$var:{variable}",
            max_retries=0,
        )
        release = tmp_path / "release"
        build_release(
            sample_catalog,
            release,
            profiles={
                "compatible": EmbeddingProfile(
                    embedding,
                    python_requirements={"openai": version("openai")},
                )
            },
        )
        metadata = (release / "profiles/compatible/profile.json").read_text()
        assert "provider/arbitrary-embedding-model" in metadata
        assert f"$var:{variable}" in metadata
        assert "producer-secret" not in metadata
        requests.clear()
        registry.set_var(variable, "stale-process-secret")

        async def exercise() -> None:
            catalog = open_catalog(release)
            server = create_server(
                catalog,
                profile="compatible",
                embedding_environment={variable: "deployment-secret"},
            )
            described = await server.call_tool("describe", {"profile": "compatible"})
            assert isinstance(described, CallToolResult)
            assert described.is_error is False
            fts = await server.call_tool("search", {"text": "direct labels"})
            assert isinstance(fts, CallToolResult)
            assert fts.is_error is False
            assert requests == []
            for mode in ("vector", "hybrid"):
                result = await server.call_tool(
                    "search", {"text": "direct labels", "mode": mode}
                )
                assert isinstance(result, CallToolResult)
                assert result.is_error is False
                assert result.structured_content["matches"][0]["id"] == "direct-labels"
                assert "deployment-secret" not in result.model_dump_json()
            other = create_server(
                catalog,
                profile="compatible",
                embedding_environment={variable: "other-deployment-secret"},
            )
            parallel = await asyncio.gather(
                server.call_tool("search", {"text": "direct labels", "mode": "hybrid"}),
                other.call_tool("search", {"text": "direct labels", "mode": "vector"}),
            )
            assert all(
                isinstance(result, CallToolResult) and not result.is_error
                for result in parallel
            )

        asyncio.run(exercise())
        assert len(requests) == 4
        assert [authorization for authorization, _ in requests].count(
            "Bearer deployment-secret"
        ) == 3
        assert [authorization for authorization, _ in requests].count(
            "Bearer other-deployment-secret"
        ) == 1
        assert registry.get_var(variable) == "stale-process-secret"
        for _, body in requests:
            assert body["model"] == "provider/arbitrary-embedding-model"
            assert body["dimensions"] == 4
    finally:
        endpoint.shutdown()
        endpoint.server_close()
        thread.join(timeout=5)
