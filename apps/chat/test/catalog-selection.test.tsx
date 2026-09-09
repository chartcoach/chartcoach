import { gzipSync } from "node:zlib";
import { afterAll, beforeAll, expect, it, vi } from "vite-plus/test";
import { routeAuth } from "eve/channels/auth";
import { getCatalogMetadata } from "../lib/catalog/metadata";
import { catalogRouteAuth, reviewRouteAuth } from "../agent/auth";
import { sessionSelection } from "../agent/selection-context";
import { withCatalogScope } from "../lib/catalog/scope";
import { resolveCatalogSelection, resolvedSelectionSchema } from "../lib/catalog/selection";
import { getCatalog } from "../lib/catalog/open";
import { Catalog } from "@chartcoach/catalog";
import { queryCatalog } from "../lib/retrieval/sql";
import type { CatalogSelection } from "../shared/catalog-selection";

let catalogId: string;
const caller = { authenticator: "test", principalType: "user", principalId: "reviewer" };
const selection = (sql: string): CatalogSelection => ({ catalogId, sql });
const encode = (value: Partial<CatalogSelection>) =>
  gzipSync(JSON.stringify(value)).toString("base64");
const request = (header: string) =>
  new Request("http://localhost/eve/v1/session", {
    method: "POST",
    headers: { "x-chartcoach-selection": header },
  });

beforeAll(async () => {
  vi.stubEnv("CATALOG_SOURCE", new URL("../../../fixtures/catalog-release/", import.meta.url).href);
  vi.stubEnv("EVE_DEV", "1");
  catalogId = (await getCatalogMetadata()).catalogId;
});
afterAll(() => vi.unstubAllEnvs());

it("validates the submitted query during authentication and stores its immutable selection", async () => {
  const query = selection(
    "SELECT id FROM catalog_entries WHERE id IN ('axis-labels', 'bar-labels') ORDER BY id",
  );
  const auth = await routeAuth(request(encode(query)), reviewRouteAuth);
  if (auth instanceof Response) throw new Error("Expected authenticated selection.");
  const resolved = resolvedSelectionSchema.parse(
    JSON.parse(String(auth.attributes["chartcoach.selection"])),
  );
  expect(resolved).toEqual({ catalogId, ids: ["axis-labels", "bar-labels"] });
  await expect(
    withCatalogScope({ selection: resolved }, async (scope) => [...scope.ids]),
  ).resolves.toEqual(["axis-labels", "bar-labels"]);
});

it("keeps empty selections empty through authentication and the scoped database", async () => {
  const query = selection("SELECT id FROM catalog_entries WHERE false");
  const auth = await routeAuth(request(encode(query)), reviewRouteAuth);
  if (auth instanceof Response) throw new Error("Expected authenticated selection.");
  await withCatalogScope({ selection: await resolveCatalogSelection(query) }, async (scope) => {
    const connection = await (await scope.database()).connect();
    try {
      expect(
        (
          await connection.runAndReadAll("SELECT count(*)::INTEGER FROM catalog_entries")
        ).getRowsJson(),
      ).toEqual([[0]]);
    } finally {
      connection.closeSync();
    }
  });
});

it.each([
  "SELECT id FROM catalog_entries; SELECT id FROM catalog_entries",
  "DELETE FROM guidelines",
  "CREATE TABLE changed AS SELECT 1",
  "COPY guidelines TO '/tmp/chartcoach-selection.csv'",
  "SET enable_external_access = true",
  "SELECT * FROM read_text('/etc/passwd')",
  "SELECT * FROM read_parquet('https://example.com/private.parquet')",
  "SELECT * FROM query('DELETE FROM guidelines')",
  "INSTALL json",
  "ATTACH ':memory:' AS other",
  "SELECT ?::VARCHAR AS id",
  "SELECT id, title FROM catalog_entries",
  "SELECT id AS guideline_id FROM catalog_entries",
  "SELECT 1 AS id",
  "SELECT NULL::VARCHAR AS id",
  "SELECT 'invented-guideline' AS id",
  "SELECT id FROM catalog_entries CROSS JOIN range(2)",
])("rejects invalid selection queries before starting the agent: %s", async (sql) => {
  const response = await routeAuth(request(encode(selection(sql))), reviewRouteAuth);
  expect(response).toBeInstanceOf(Response);
  if (!(response instanceof Response)) throw new Error("Expected authentication rejection.");
  expect(response.status).toBe(403);
  expect(await response.json()).toMatchObject({ code: "invalid_catalog_selection" });
});

it.each([
  ["invalid base64", "%invalid"],
  ["noncanonical base64 padding", "Zh=="],
  ["oversized header", "A".repeat(8_004)],
  ["invalid gzip", Buffer.from("plain text").toString("base64")],
  ["truncated gzip", gzipSync("{}").subarray(0, 12).toString("base64")],
  ["decompression overflow", gzipSync("x".repeat(64_001)).toString("base64")],
  ["invalid UTF-8", gzipSync(Buffer.from([0xff])).toString("base64")],
  ["invalid JSON", gzipSync("{").toString("base64")],
  ["invalid selection shape", encode({ sql: "SELECT 1" })],
])("rejects %s at the authenticated header boundary", async (_name, header) => {
  const response = await routeAuth(request(header), reviewRouteAuth);
  expect(response).toBeInstanceOf(Response);
  if (!(response instanceof Response)) throw new Error("Expected authentication rejection.");
  expect(response.status).toBe(403);
});

it("rejects a selection from another catalog release", async () => {
  const response = await routeAuth(
    request(encode({ catalogId: "0".repeat(64), sql: "SELECT id FROM catalog_entries" })),
    reviewRouteAuth,
  );
  if (!(response instanceof Response)) throw new Error("Expected authentication rejection.");
  expect(response.status).toBe(403);
  expect(await response.json()).toMatchObject({
    error: expect.stringContaining("catalog changed"),
  });
});

it("cancels selection work while keeping other catalog queries available", async () => {
  const expensive = resolveCatalogSelection(
    selection(
      "SELECT id FROM catalog_entries WHERE (SELECT sum(sin(i)) FROM range(10000000000) AS t(i)) > 0",
    ),
    { signal: AbortSignal.timeout(50) },
  );
  await expect(expensive).rejects.toMatchObject({ name: "TimeoutError" });
  await expect(
    withCatalogScope(
      { selection: await resolveCatalogSelection(selection("SELECT id FROM catalog_entries")) },
      async (scope) => scope.ids.size,
    ),
  ).resolves.toBe(6);
});

it("preserves native caller authentication on follow-up requests", async () => {
  const followup = new Request("http://localhost/eve/v1/session/review/messages", {
    method: "POST",
    headers: { "x-chartcoach-selection": "%invalid" },
  });
  const auth = await routeAuth(followup, catalogRouteAuth);
  expect(await routeAuth(followup, reviewRouteAuth)).toEqual(auth);
});

it("preserves a resolved volatile selection across eviction and catalog reconstruction", async () => {
  const fixture = await getCatalog();
  const catalog = new Catalog(fixture.guidelines, fixture.manifest);
  const identity = (await getCatalogMetadata(catalog)).catalogId;
  const resolved = await resolveCatalogSelection(
    {
      catalogId: identity,
      sql: "SELECT id FROM catalog_entries ORDER BY random() LIMIT 3",
    },
    { catalog },
  );
  expect(resolved.ids).toHaveLength(3);
  const saved = JSON.stringify(resolved);
  const rows = resolved.ids.map((id) => [id]);
  expect(
    (await queryCatalog("SELECT id FROM guidelines ORDER BY id", { catalog, selection: resolved }))
      .rows,
  ).toEqual(rows);
  const ids = catalog.guidelines.map(({ id }) => id);
  for (let mask = 0; mask < 10; mask++) {
    await queryCatalog("SELECT id FROM guidelines", {
      catalog,
      selection: { catalogId: identity, ids: ids.filter((_id, index) => mask & (1 << index)) },
    });
  }
  const restored = resolvedSelectionSchema.parse(JSON.parse(saved));
  expect(
    (await queryCatalog("SELECT id FROM guidelines ORDER BY id", { catalog, selection: restored }))
      .rows,
  ).toEqual(rows);
  const reconstructed = new Catalog(catalog.guidelines, catalog.manifest);
  expect(
    (
      await queryCatalog("SELECT id FROM guidelines ORDER BY id", {
        catalog: reconstructed,
        selection: restored,
      })
    ).rows,
  ).toEqual(rows);
});

it("requires an immutable initiating selection before tools can access the catalog", () => {
  const initiator = { ...caller, attributes: {} };
  expect(() =>
    sessionSelection({
      id: "review",
      turn: { id: "turn", sequence: 1 },
      auth: {
        initiator,
        current: {
          ...caller,
          attributes: {
            "chartcoach.selection": JSON.stringify(selection("SELECT id FROM catalog_entries")),
          },
        },
      },
    }),
  ).toThrow("Start a new review");
});
