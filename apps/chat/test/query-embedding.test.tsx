import { afterEach, expect, it, vi } from "vite-plus/test";
import { z } from "zod";
import type { ProfileInfo } from "@chartcoach/catalog";
import { createQueryEmbedder } from "../lib/retrieval/embedding";
import { loadConfig } from "../runtime/config";

const config = loadConfig({
  userConfig: "/missing/config.json",
  environment: {
    CHARTCOACH_EMBEDDING_MODEL: "provider/embedding-model",
    CHARTCOACH_EMBEDDING_BASE_URL: "https://vectors.example/v1",
    CHARTCOACH_EMBEDDING_DIMENSIONS: "4",
  },
});

const profile: ProfileInfo = {
  name: "compatible",
  profile_schema_version: 1,
  documents_version: 1,
  embedding_functions: [
    {
      name: "chartcoach-openai-compatible",
      source_column: "text",
      vector_column: "vector",
      model: {
        name: "provider/embedding-model",
        base_url: "https://vectors.example/v1",
        dim: 4,
        api_key: "$var:CHARTCOACH_EMBEDDING_API_KEY",
      },
    },
  ],
  dimensions: 4,
  distance_metric: "cosine",
  python_requirements: {},
  lancedb_version: "0.38.0",
  projection: null,
};

afterEach(() => {
  vi.unstubAllGlobals();
  vi.unstubAllEnvs();
});

it("imports the injectable factory without reading ambient app configuration", async () => {
  vi.stubEnv("CHARTCOACH_RUNTIME_CONFIG", "invalid unrelated configuration");
  vi.resetModules();
  const { createQueryEmbedder: create } = await import("../lib/retrieval/embedding");
  expect(() => create(config, { CHARTCOACH_EMBEDDING_API_KEY: "secret" })).not.toThrow();
});

function response(vector: number[] = [1, 0, 1, 0]) {
  return Response.json({
    data: [{ index: 0, embedding: vector }],
    model: "provider/embedding-model",
    usage: { prompt_tokens: 1, total_tokens: 1 },
  });
}

it("uses a dedicated provider connection and returns native SDK query vectors", async () => {
  const request = vi.fn(async (url: string | URL, options?: RequestInit) => {
    expect(String(url)).toBe("https://vectors.example/v1/embeddings");
    expect(new Headers(options?.headers).get("authorization")).toBe("Bearer vector-secret");
    expect(JSON.parse(z.string().parse(options?.body))).toMatchObject({
      model: "provider/embedding-model",
      input: ["direct labels"],
      dimensions: 4,
    });

    return response();
  });

  vi.stubGlobal("fetch", request);

  const embed = createQueryEmbedder(config, {
    CHARTCOACH_EMBEDDING_API_KEY: "vector-secret",
    CHARTCOACH_TEXT_API_KEY: "unused-text-secret",
  });

  expect(request).not.toHaveBeenCalled();
  await expect(embed("direct labels", profile)).resolves.toEqual([1, 0, 1, 0]);
  expect(request).toHaveBeenCalledTimes(1);
});

it("honors the native OpenAI default endpoint and Ada dimension semantics", async () => {
  const nativeConfig = loadConfig({
    userConfig: "/missing/config.json",
    environment: {},
    overrides: {
      embedding: {
        model: "text-embedding-ada-002",
        baseURL: "https://api.openai.com/v1",
        dimensions: 1536,
      },
    },
  });

  const request = vi.fn(async (url: string | URL, options?: RequestInit) => {
    expect(String(url)).toBe("https://api.openai.com/v1/embeddings");
    expect(JSON.parse(z.string().parse(options?.body))).toEqual({
      model: "text-embedding-ada-002",
      input: ["query"],
      encoding_format: "float",
    });

    return response(Array(1536).fill(0));
  });

  vi.stubGlobal("fetch", request);

  const nativeProfile: ProfileInfo = {
    ...profile,
    dimensions: 1536,
    embedding_functions: [
      {
        ...profile.embedding_functions[0],
        name: "openai",
        model: { name: "text-embedding-ada-002", base_url: null, dim: null },
      },
    ],
  };

  await expect(
    createQueryEmbedder(nativeConfig, { CHARTCOACH_EMBEDDING_API_KEY: "secret" })(
      "query",
      nativeProfile,
    ),
  ).resolves.toHaveLength(1536);
});

it.each([
  { ...profile, dimensions: 3 },
  {
    ...profile,
    embedding_functions: [
      {
        ...profile.embedding_functions[0],
        model: { name: "other-model", base_url: "https://vectors.example/v1" },
      },
    ],
  },
  {
    ...profile,
    embedding_functions: [
      {
        ...profile.embedding_functions[0],
        model: { name: "provider/embedding-model", base_url: "https://other.example/v1" },
      },
    ],
  },
] satisfies ProfileInfo[])(
  "rejects mismatched profile identity before contacting a provider",
  async (info) => {
    const request = vi.fn();
    vi.stubGlobal("fetch", request);
    await expect(
      createQueryEmbedder(config, { CHARTCOACH_EMBEDDING_API_KEY: "secret" })("query", info),
    ).rejects.toThrow("must match");
    expect(request).not.toHaveBeenCalled();
  },
);

it("rejects wrong vector dimensions and hides provider error content", async () => {
  vi.stubGlobal(
    "fetch",
    vi.fn(async () => response([1, 0])),
  );
  await expect(
    createQueryEmbedder(config, { CHARTCOACH_EMBEDDING_API_KEY: "secret" })("query", profile),
  ).rejects.toThrow("Embedding request failed");
  vi.stubGlobal(
    "fetch",
    vi.fn(async () => Response.json({ error: { message: "secret" } }, { status: 400 })),
  );
  await expect(
    createQueryEmbedder(config, { CHARTCOACH_EMBEDDING_API_KEY: "secret" })("query", profile),
  ).rejects.toThrow("Embedding request failed");
});

it("cancels a provider request with the caller's signal", async () => {
  const request = vi.fn(async (_url: RequestInfo | URL, options?: RequestInit) => {
    await new Promise<void>((_resolve, reject) =>
      options?.signal?.addEventListener("abort", () => reject(options.signal?.reason), {
        once: true,
      }),
    );

    return response();
  });

  vi.stubGlobal("fetch", request);
  const controller = new AbortController();

  const query = createQueryEmbedder(config, { CHARTCOACH_EMBEDDING_API_KEY: "secret" })(
    "query",
    profile,
    controller.signal,
  );

  await vi.waitFor(() => expect(request).toHaveBeenCalled());
  controller.abort(new Error("cancelled"));
  await expect(query).rejects.toThrow("cancelled");
});
