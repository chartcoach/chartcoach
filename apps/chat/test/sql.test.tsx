import { afterAll, beforeAll, expect, it, vi } from "vite-plus/test";
import { describeCatalog, queryCatalog } from "../lib/retrieval/sql";

beforeAll(() => {
  vi.stubEnv("CATALOG_SOURCE", new URL("../../../fixtures/catalog-release/", import.meta.url).href);
});
afterAll(() => vi.unstubAllEnvs());

it("discovers the loaded catalog schema and vocabulary", async () => {
  const info = await describeCatalog();
  expect(info.tables.map(({ name, rows }) => ({ name, rows }))).toEqual([
    { name: "guidelines", rows: 6 },
    { name: "sections", rows: 6 },
    { name: "guideline_labels", rows: 12 },
    { name: "references", rows: 1 },
    { name: "guideline_references", rows: 6 },
    { name: "guideline_sources", rows: 6 },
  ]);
  expect(info.tables.find(({ name }) => name === "guideline_sources")?.columns).toContainEqual({
    name: "authors",
    type: "List(String)",
  });
  expect(info.section_roles).toContainEqual(expect.objectContaining({ name: "advice" }));
  expect(info.label_families).toContainEqual(expect.objectContaining({ name: "chart" }));
});

it("joins guideline labels and parsed sources using native SQL", async () => {
  const result = await queryCatalog(
    `
    SELECT g.id, s.authors, s.year, s.source_title, s.doi
    FROM guidelines g
    JOIN guideline_labels l ON l.guideline_id = g.id
    JOIN guideline_sources s ON s.guideline_id = g.id
    WHERE l.family = 'chart' AND l.category = 'line' AND s.year = '2024'
    ORDER BY g.id`,
    { limit: 2 },
  );
  expect(result.rows).toEqual([
    ["axis-labels", ["Smith, Ada"], "2024", "Readable charts", null],
    ["bar-labels", ["Smith, Ada"], "2024", "Readable charts", null],
  ]);
  expect(result).toMatchObject({ method: "sql", row_count: 2, truncated: true, limit: 2 });
  const counts = await queryCatalog(
    "SELECT role, count(*) AS entries FROM sections GROUP BY role;",
  );
  expect(counts.rows).toEqual([["advice", "6"]]);
  expect(counts.columns).toEqual([
    { name: "role", type: "VARCHAR" },
    { name: "entries", type: "BIGINT" },
  ]);
  expect(counts.truncated).toBe(false);
});

it("keeps native nested and exact numeric values JSON serializable", async () => {
  const result = await queryCatalog(`SELECT DATE '2024-01-02' AS day,
    1234567890123456789::BIGINT AS exact, 1.23::DECIMAL(4,2) AS decimal,
    {'label': 'chart:line', 'values': [1, 2]} AS nested, NULL AS missing`);
  expect(result.rows).toEqual([
    ["2024-01-02", "1234567890123456789", "1.23", { label: "chart:line", values: [1, 2] }, null],
  ]);
  expect(() => JSON.stringify(result)).not.toThrow();
});

it.each([
  "SELECT 1; SELECT 2",
  "CREATE TABLE changed AS SELECT 1",
  "DELETE FROM guidelines",
  "COPY guidelines TO '/tmp/chartcoach-sql-escape.csv'",
  "SET enable_external_access = true",
  "ATTACH ':memory:' AS other",
  "SELECT * FROM read_text('/etc/passwd')",
  "SELECT * FROM read_parquet('https://example.com/private.parquet')",
  "SELECT * FROM glob('/Users/*')",
  "SELECT getenv('CHARTCOACH_SQL_SENTINEL')",
  "SELECT * FROM query('DELETE FROM guidelines')",
])("rejects statements outside the read-only catalog boundary: %s", async (sql) => {
  await expect(queryCatalog(sql)).rejects.toThrow();
  expect((await queryCatalog("SELECT count(*)::INTEGER FROM guidelines")).rows).toEqual([[6]]);
});

it("bounds returned bytes and asks for narrower fields when one row is too large", async () => {
  const result = await queryCatalog("SELECT repeat('x', 40000) AS content FROM range(3)");
  expect(result).toMatchObject({ row_count: 1, truncated: true });
  expect(Buffer.byteLength(JSON.stringify(result))).toBeLessThanOrEqual(65_536);
  await expect(queryCatalog("SELECT repeat('x', 70000)")).rejects.toThrow(
    "Select fewer or shorter fields",
  );
});

it("cancels expensive work while another query can complete", async () => {
  const signal = AbortSignal.timeout(50);
  const expensive = queryCatalog("SELECT sum(sin(i)) FROM range(10000000000) AS t(i)", { signal });
  const healthy = queryCatalog("SELECT count(*)::INTEGER FROM guidelines");
  await expect(expensive).rejects.toMatchObject({ name: "TimeoutError" });
  expect((await healthy).rows).toEqual([[6]]);
  expect((await queryCatalog("SELECT 42")).rows).toEqual([[42]]);
});

it("interrupts queries after the execution deadline and recovers", async () => {
  await expect(queryCatalog("SELECT sum(sin(i)) FROM range(10000000000) AS t(i)")).rejects.toThrow(
    "SQL exceeded 5 seconds",
  );
  expect((await queryCatalog("SELECT 42")).rows).toEqual([[42]]);
}, 10_000);
