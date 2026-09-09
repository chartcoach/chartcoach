import { Catalog, parseCatalogManifest } from "@chartcoach/catalog";
import { Coordinator, type Connector } from "@uwdata/mosaic-core";
import { afterAll, beforeAll, expect, it } from "vite-plus/test";
import { exploreCatalog, type ExplorerData } from "../browser/explorer";
import { catalogData } from "../lib/catalog/metadata";
import { emptyCatalogFilters, type CatalogFilters } from "../shared/catalog-filters";

const catalog = new Catalog(
  [
    { id: "current", references: ["@article{a,author={O'Neil, Ada},title={Labels},year={2020}}"] },
    {
      id: "mixed",
      references: [
        "@article{b,author={O'Neil, Ada},title={Axes},year={2010}}",
        "@book{c,author={Baker, Bea},title={Marks},year={2024}}",
      ],
    },
    { id: "source-free", references: [] },
  ].map((record) => ({
    ...record,
    title: record.id,
    description: "Chart advice.",
    labels: [],
    sections: [{ role: "advice", title: "Advice", content: "Place labels beside their marks." }],
  })),
  parseCatalogManifest(
    "# Catalog\n\n## Section Roles\n\n### advice\n\nChart advice.\n\n## Label Families\n\n### chart\n\nChart types such as `chart:line`.\n",
  ),
);
let data: Awaited<ReturnType<typeof catalogData>>;
let coordinator: Coordinator;
const queries: string[] = [];
let delayed:
  | {
      started: ReturnType<typeof Promise.withResolvers<void>>;
      release: ReturnType<typeof Promise.withResolvers<void>>;
    }
  | undefined;

beforeAll(async () => {
  data = await catalogData(catalog);
  // SAFETY: These SQL consumers read toArray. Native DuckDB supplies its row values here.
  coordinator = new Coordinator(
    {
      async query({ sql }: { sql: string }) {
        queries.push(sql);
        const gate = delayed;
        const connection = await data.db.connect();
        try {
          const rows = (await connection.runAndReadAll(sql)).getRowObjectsJson();
          if (gate) {
            gate.started.resolve();
            await gate.release.promise;
          }
          return { toArray: () => rows };
        } finally {
          connection.closeSync();
        }
      },
    } as Connector,
    { logger: null, preagg: { enabled: false } },
  );
});

afterAll(() => {
  coordinator?.clear();
  data?.db.closeSync();
});

async function explore(patch: Partial<CatalogFilters> = {}) {
  const pending = Promise.withResolvers<ExplorerData>();
  const stop = exploreCatalog(
    coordinator,
    data.metadata,
    {
      ...emptyCatalogFilters(data.metadata.catalogId),
      ...patch,
    },
    pending.resolve,
    pending.reject,
  );
  try {
    return await pending.promise;
  } finally {
    stop();
  }
}

it("crossfilters source facets while counting and previewing the complete selection", async () => {
  const ada = data.metadata.authors.find(({ name }) => name === "O'Neil, Ada")!.id;
  const article = data.metadata.sourceTypes.find(({ name }) => name === "article")!.id;
  const result = await explore({
    includeAuthorIds: [ada],
    yearFrom: 2020,
    sourceTypeIds: [article],
  });
  expect(result.matchedGuidelines).toBe(1);
  expect(result.selection.catalogId).toBe(data.metadata.catalogId);
  expect(queries).toContain(
    `SELECT count(*)::INTEGER AS count FROM (${result.selection.sql}) selection`,
  );
  const connection = await data.db.connect();
  try {
    expect((await connection.runAndReadAll(result.selection.sql)).getRowObjectsJson()).toEqual([
      { id: "current" },
    ]);
  } finally {
    connection.closeSync();
  }
  expect(result.matches).toEqual([{ id: "current", title: "current" }]);
  expect(result.authors.find(({ id }) => id === ada)?.count).toBe(1);
  expect(result.years.filter(({ count }) => count > 0)).toEqual([
    { from: 2010, to: 2010, count: 1 },
    { from: 2020, to: 2020, count: 1 },
  ]);
  const incompatible = await explore({
    includeAuthorIds: [ada],
    sourceTypeIds: [data.metadata.sourceTypes.find(({ name }) => name === "book")!.id],
  });
  expect(incompatible.matchedGuidelines).toBe(0);
  expect(incompatible.matches).toEqual([]);
});

it("applies author exclusions to every facet and retains sourceless matches", async () => {
  expect((await explore()).matchedGuidelines).toBe(3);
  const ada = data.metadata.authors.find(({ name }) => name === "O'Neil, Ada")!.id;
  const result = await explore({ excludeAuthorIds: [ada] });
  expect(result.matchedGuidelines).toBe(1);
  expect(result.matches).toEqual([{ id: "source-free", title: "source-free" }]);
  expect(result.authors.every(({ count }) => count === 0)).toBe(true);
  expect(result.sourceTypes.every(({ count }) => count === 0)).toBe(true);
  expect(result.years.every(({ count }) => count === 0)).toBe(true);
});

it("exports the full matching selection independently of preview pagination", async () => {
  const connection = await data.db.connect();
  try {
    await connection.run(
      "INSERT INTO guidelines (id, title, description) SELECT 'extra-' || range, 'Extra', '' FROM range(8)",
    );
    coordinator.clear();
    const result = await explore();
    expect(result.matches).toHaveLength(6);
    expect(result.matchedGuidelines).toBe(11);
    expect((await connection.runAndReadAll(result.selection.sql)).getRowObjectsJson()).toHaveLength(
      11,
    );
  } finally {
    await connection.run("DELETE FROM guidelines WHERE id LIKE 'extra-%'");
    connection.closeSync();
    coordinator.clear();
  }
});

it("disconnects pending consumers before another draft publishes", async () => {
  coordinator.clear();
  const gate = { started: Promise.withResolvers<void>(), release: Promise.withResolvers<void>() };
  delayed = gate;
  const published: ExplorerData[] = [];
  const stop = exploreCatalog(
    coordinator,
    data.metadata,
    emptyCatalogFilters(data.metadata.catalogId),
    (value) => published.push(value),
    () => {},
  );
  await gate.started.promise;
  stop();
  delayed = undefined;
  const ada = data.metadata.authors.find(({ name }) => name === "O'Neil, Ada")!.id;
  const current = explore({ includeAuthorIds: [ada] });
  gate.release.resolve();
  expect((await current).matchedGuidelines).toBe(2);
  expect(published).toEqual([]);
});
