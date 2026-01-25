import { describe, expect, it } from "vitest";

import { ChartCoachRetrievalClient } from "./chartcoach-retrieval-client";

function createMockFetch(handler: (url: string, init?: RequestInit) => Promise<Response>) {
  return async (input: RequestInfo | URL, init?: RequestInit) => {
    const url = typeof input === "string" ? input : input.toString();
    return await handler(url, init);
  };
}

describe("ChartCoachRetrievalClient", () => {
  it("lists strategies", async () => {
    const client = new ChartCoachRetrievalClient({
      baseUrl: "http://example.invalid",
      fetch: createMockFetch(async (url) => {
        expect(url).toBe("http://example.invalid/v1/strategies");
        return new Response(JSON.stringify([{ id: "s@v0", name: "S", description: "" }]), {
          status: 200,
          headers: { "content-type": "application/json" },
        });
      }),
    });

    const strategies = await client.listStrategies();
    expect(strategies).toEqual([{ id: "s@v0", name: "S", description: "" }]);
  });

  it("runs a strategy with catalog_uri and request", async () => {
    const client = new ChartCoachRetrievalClient({
      baseUrl: "http://example.invalid/",
      fetch: createMockFetch(async (url, init) => {
        expect(url).toBe("http://example.invalid/v1/strategies/guideline-browser@v0");
        expect(init?.method).toBe("POST");
        expect(init?.headers).toEqual({ "content-type": "application/json" });
        expect(init?.body).toBe(
          JSON.stringify({
            catalog_uri: "/tmp/catalog.parquet",
            request: { context: [], lang: "en", meta: {}, k: 10 },
          }),
        );

        return new Response(JSON.stringify({ catalog: [], meta: { ok: true } }), {
          status: 200,
          headers: { "content-type": "application/json" },
        });
      }),
    });

    const resp = await client.runStrategy({
      strategyId: "guideline-browser@v0",
      catalogUri: "/tmp/catalog.parquet",
      request: { context: [], lang: "en", meta: {}, k: 10 },
    });

    expect(resp.meta.ok).toBe(true);
    expect(resp.catalog).toEqual([]);
  });
});
