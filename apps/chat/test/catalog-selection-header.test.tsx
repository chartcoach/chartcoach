import { randomBytes } from "node:crypto";
import { gunzipSync } from "node:zlib";
import { expect, it } from "vite-plus/test";
import { encodeCatalogSelection } from "../lib/catalog-client";

const catalogId = "a".repeat(64);

it("transmits the exact Unicode selection as a compressed ASCII header", async () => {
  const selection = {
    catalogId,
    sql: "SELECT DISTINCT g.id FROM catalog_entries g WHERE g.title = 'Bárbara’s 測定'",
  };
  const header = await encodeCatalogSelection(selection);
  expect(JSON.parse(gunzipSync(Buffer.from(header, "base64")).toString("utf8"))).toEqual(selection);
  expect(header).toMatch(/^[A-Za-z0-9+/]+={0,2}$/);
});

it("bounds the UTF-8 selection before compression", async () => {
  await expect(
    encodeCatalogSelection({ catalogId, sql: `SELECT '${"\u0000".repeat(12_000)}' AS id` }),
  ).rejects.toThrow("selection is too large");
});

it("bounds the encoded header independently of the uncompressed selection", async () => {
  const sql = `SELECT '${randomBytes(10_000).toString("base64")}' AS id`;
  await expect(encodeCatalogSelection({ catalogId, sql })).rejects.toThrow(
    "selection is too large",
  );
});

it("stops encoding an aborted send", async () => {
  const controller = new AbortController();
  controller.abort();
  await expect(
    encodeCatalogSelection({ catalogId, sql: "SELECT id FROM catalog_entries" }, controller.signal),
  ).rejects.toThrow("aborted");
});
