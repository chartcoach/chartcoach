// @vitest-environment node

import { describe, expect, it } from "vitest";

import {
  buildRetrievalResultsCacheKey,
  clearRetrievalResultsInMemoryCache,
  computeRetrievalResultsDigest,
  readRetrievalResultsCache,
  writeRetrievalResultsCache,
} from "./retrieval-results-cache.server";

describe("retrieval results cache (in-memory)", () => {
  it("stores and retrieves entries when S3 is not configured", async () => {
    clearRetrievalResultsInMemoryCache();

    const request = { context: [], lang: "en", meta: {}, k: 10 };
    const digest = computeRetrievalResultsDigest({
      scenarioId: "s1",
      strategyId: "dummy@v0",
      catalogUri: "/tmp/catalog.parquet",
      baseUrl: "http://127.0.0.1:8000",
      request,
    });

    const key = buildRetrievalResultsCacheKey({
      scenarioId: "s1",
      strategyId: "dummy@v0",
      digest,
    });

    expect(await readRetrievalResultsCache(key)).toBeUndefined();

    await writeRetrievalResultsCache(key, {
      scenarioId: "s1",
      strategyId: "dummy@v0",
      catalogUri: "/tmp/catalog.parquet",
      request,
      response: { catalog: [], meta: { ok: true } },
    });

    const cached = await readRetrievalResultsCache(key);
    expect(cached?.response.meta.ok).toBe(true);
  });
});
