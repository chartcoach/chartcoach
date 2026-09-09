import type { Query, VectorQuery } from "@lancedb/lancedb";
import { z } from "zod";
import { getIndex } from "../catalog/open";
import { withCatalogScope, type ScopeOptions } from "../catalog/scope";
import { waitFor } from "../async";
import { embedQuery } from "./embedding";
import { guidelineCards } from "./cards";

type SearchMethod = "vector" | "keyword" | "hybrid";

export function searchGuidelines(query: string, method: SearchMethod, options: ScopeOptions) {
  const { signal } = options;
  return withCatalogScope(options, async (scope) => {
    if (scope.ids.size === 0) return { method, query, matches: [] };
    const profile = process.env.CATALOG_PROFILE ?? "minilm-l6-v2-cpu";
    const { table, info } = await waitFor(getIndex(scope.catalog, profile), signal);
    const searchConfig = {
      profile,
      model: z.string().safeParse(info.embedding_functions[0]?.model.name).data,
      metric: info.distance_metric,
      dimensions: info.dimensions,
    };
    signal?.throwIfAborted();
    let request: Query | VectorQuery;
    if (method === "keyword") {
      request = table.query().fullTextSearch(query, { columns: ["text"] });
    } else {
      const vectorRequest = table
        .vectorSearch(await waitFor(embedQuery(query, info), signal))
        .distanceType(searchConfig.metric);
      if (method === "hybrid") {
        const { rerankers } = await waitFor(import("@lancedb/lancedb"), signal);
        vectorRequest
          .fullTextSearch(query, { columns: ["text"] })
          .rerank(await waitFor(rerankers.RRFReranker.create(), signal));
      }
      request = vectorRequest;
    }
    signal?.throwIfAborted();
    if (scope.lanceWhere) request.where(scope.lanceWhere);
    const columns =
      method === "keyword"
        ? ["parent_id", "_score"]
        : method === "hybrid"
          ? ["parent_id"]
          : ["parent_id", "_distance"];
    const hits = await waitFor(request.select(columns).limit(20).toArray(), signal);
    signal?.throwIfAborted();
    const rows = z.array(z.object({ parent_id: z.string() })).parse(hits);
    const ids = [...new Set(rows.map((row) => row.parent_id))].slice(0, 5);
    const matches = guidelineCards(scope, ids);
    const config = method === "keyword" ? { profile: searchConfig.profile } : searchConfig;
    return {
      method,
      query,
      ...config,
      ranking: method === "keyword" ? "BM25" : method === "hybrid" ? "RRF" : searchConfig.metric,
      matches,
    };
  });
}
