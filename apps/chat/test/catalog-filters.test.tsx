import { Catalog, parseCatalogManifest } from "@chartcoach/catalog";
import { connect, Index, rerankers } from "@lancedb/lancedb";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { beforeAll, expect, it } from "vite-plus/test";
import { z } from "zod";
import { getCatalogMetadata } from "../lib/catalog/metadata";
import { assertCatalogIds, withCatalogScope } from "../lib/catalog/scope";
import { queryCatalog } from "../lib/retrieval/sql";
import { and, literal } from "@uwdata/mosaic-sql";
import { sourcePredicates } from "../shared/catalog-predicate";
import { resolveCatalogSelection } from "../lib/catalog/selection";
import { emptyCatalogFilters, type CatalogFilters } from "../shared/catalog-filters";

const references = {
  alice: "@article{alice, author={Able, Alice}, title={Current advice}, year={2020}}",
  oldAlice: "@article{oldalice, author={Able, Alice}, title={Earlier advice}, year={2010}}",
  bea: "@book{bea, author={Baker, Bea}, title={Chart handbook}, year={2024}}",
  cara: "@misc{cara, author={Clark, Cara}, title={Field notes}, year={2018}}",
  undated: "@misc{undated, author={Able, Alice}, title={Unpublished notes}}",
};
const catalog = new Catalog(
  [
    { id: "alice", references: [references.alice] },
    { id: "cross", references: [references.oldAlice, references.bea] },
    { id: "bea", references: [references.bea] },
    { id: "mixed", references: [references.alice, references.cara] },
    { id: "undated", references: [references.undated] },
    { id: "sourceless", references: [] },
  ].map((record) => ({
    ...record,
    title: record.id,
    description: "Keep labels readable.",
    labels: [],
    sections: [{ role: "advice", title: "Advice", content: "Place labels beside their marks." }],
  })),
  parseCatalogManifest(
    "# Catalog\n\n## Section Roles\n\n### advice\n\nChart advice.\n\n## Label Families\n\n### chart\n\nChart types such as `chart:line`.\n",
  ),
);
let defaults: CatalogFilters;
let metadata: Awaited<ReturnType<typeof getCatalogMetadata>>;

beforeAll(async () => {
  metadata = await getCatalogMetadata(catalog);
  defaults = emptyCatalogFilters(metadata.catalogId);
});

async function select(filters: CatalogFilters) {
  const active = Object.values(sourcePredicates(filters, metadata)).filter(
    (part) => part !== undefined,
  );
  return resolveCatalogSelection(
    {
      catalogId: filters.catalogId,
      sql: `SELECT DISTINCT g.id FROM catalog_entries g LEFT JOIN guideline_sources s ON s.guideline_id = g.id WHERE ${String(active.length ? and(...active) : literal(true))} ORDER BY g.id`,
    },
    { catalog },
  );
}

async function ids(filters: CatalogFilters) {
  return (
    await queryCatalog("SELECT id FROM guidelines ORDER BY id", {
      catalog,
      selection: await select(filters),
    })
  ).rows.flat();
}

it("derives authors, source types, year coverage, and schemas from parsed catalog sources", async () => {
  const metadata = await getCatalogMetadata(catalog);
  expect(metadata.totalGuidelines).toBe(6);
  expect(metadata.authors).toEqual([
    { id: 1, name: "Able, Alice", guidelineCount: 4 },
    { id: 2, name: "Baker, Bea", guidelineCount: 2 },
    { id: 3, name: "Clark, Cara", guidelineCount: 1 },
  ]);
  expect(metadata.sourceTypes).toEqual([
    { id: 1, name: "article", guidelineCount: 3 },
    { id: 2, name: "book", guidelineCount: 2 },
    { id: 3, name: "misc", guidelineCount: 2 },
  ]);
  expect(metadata.years).toEqual({ min: 2010, max: 2024, undatedGuidelines: 2 });
  expect(metadata.tables.find(({ name }) => name === "guideline_sources")?.columns).toContainEqual({
    name: "authors",
    type: "List(String)",
  });
});

it("requires positive author, type, and year conditions on the same source", async () => {
  expect(await ids({ ...defaults, includeAuthorIds: [1], yearFrom: 2020 })).toEqual([
    "alice",
    "mixed",
  ]);
  expect(await ids({ ...defaults, includeAuthorIds: [1], sourceTypeIds: [2] })).toEqual([]);
  expect(
    await ids({ ...defaults, includeAuthorIds: [1, 2], sourceTypeIds: [2], yearFrom: 2020 }),
  ).toEqual(["bea", "cross"]);
});

it("excludes a guideline when any attached source has an excluded author", async () => {
  expect(
    await ids({ ...defaults, includeAuthorIds: [1], excludeAuthorIds: [3], yearFrom: 2020 }),
  ).toEqual(["alice"]);
  expect(await ids({ ...defaults, excludeAuthorIds: [1] })).toEqual(["bea", "sourceless"]);
  expect(await ids({ ...defaults, includeAuthorIds: [1], excludeAuthorIds: [1] })).toEqual([]);
});

it("preserves undated and sourceless guidelines until a positive constraint excludes them", async () => {
  expect(await ids(defaults)).toContain("sourceless");
  expect(await ids({ ...defaults, includeAuthorIds: [1], sourceTypeIds: [3] })).toEqual([
    "undated",
  ]);
  expect(
    await ids({ ...defaults, includeAuthorIds: [1], sourceTypeIds: [3], yearFrom: 2010 }),
  ).toEqual([]);
});

it("keeps every authored source and section of an eligible guideline", async () => {
  const filters = { ...defaults, includeAuthorIds: [2] };
  const result = await queryCatalog(
    "SELECT source_title FROM guideline_sources WHERE guideline_id = 'cross' ORDER BY source_title",
    { catalog, selection: await select(filters) },
  );
  expect(result.rows).toEqual([["Chart handbook"], ["Earlier advice"]]);
  await withCatalogScope({ catalog, selection: await select(filters) }, async (scope) => {
    assertCatalogIds(scope, ["cross"]);
    expect(scope.catalog.read({ ids: ["cross"] })[0].sections[0].content).toBe(
      "Place labels beside their marks.",
    );
    expect(() => assertCatalogIds(scope, ["alice"])).toThrow(
      "outside this review's catalog filters",
    );
  });
});

it.each([
  "SELECT id FROM main.guidelines ORDER BY id",
  "SELECT id FROM query_table('guidelines') ORDER BY id",
  "WITH candidates AS (SELECT * FROM guidelines) SELECT DISTINCT candidates.id FROM candidates JOIN guideline_sources ON guideline_id = candidates.id ORDER BY candidates.id",
])("keeps SQL access physically within the selected guidelines: %s", async (sql) => {
  expect(
    (
      await queryCatalog(sql, {
        catalog,
        selection: await select({ ...defaults, includeAuthorIds: [2] }),
      })
    ).rows,
  ).toEqual([["bea"], ["cross"]]);
});

it("rejects stale catalog identities and unknown facet IDs", async () => {
  await expect(
    queryCatalog("SELECT id FROM guidelines", {
      catalog,
      selection: { ...(await select(defaults)), catalogId: "0".repeat(64) },
    }),
  ).rejects.toThrow("catalog changed");
  await expect(ids({ ...defaults, includeAuthorIds: [999] })).rejects.toThrow(
    "author in your selection is unknown",
  );
  await expect(ids({ ...defaults, sourceTypeIds: [999] })).rejects.toThrow(
    "source type in your selection is unknown",
  );
});

it("reuses a canonical database while keeping concurrent filter selections isolated", async () => {
  const filters = { ...defaults, includeAuthorIds: [2, 2] };
  await withCatalogScope({ catalog, selection: await select(filters) }, async (first) => {
    const db = await first.database();
    await withCatalogScope(
      { catalog, selection: await select({ ...filters, includeAuthorIds: [2] }) },
      async (second) => {
        expect(await second.database()).toBe(db);
      },
    );
    const [alice, bea] = await Promise.all([
      ids({ ...defaults, includeAuthorIds: [1], yearFrom: 2020 }),
      ids({ ...defaults, includeAuthorIds: [2] }),
    ]);
    expect(alice).toEqual(["alice", "mixed"]);
    expect(bea).toEqual(["bea", "cross"]);
    const connection = await db.connect();
    try {
      expect(
        (await connection.runAndReadAll("SELECT id FROM guidelines ORDER BY id")).getRowsJson(),
      ).toEqual([["bea"], ["cross"]]);
    } finally {
      connection.closeSync();
    }
  });
});

it("filters native vector, keyword, and hybrid candidates before their result limit", async () => {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-filter-search-"));
  const db = await connect(directory);
  try {
    const table = await db.createTable("documents", [
      ...Array.from({ length: 24 }, (_, index) => ({
        parent_id: "alice",
        text: "legend labels",
        vector: [index / 100, 0],
      })),
      { parent_id: "bea", text: "legend labels", vector: [1, 1] },
    ]);
    try {
      await table.createIndex("text", { config: Index.fts() });
      await withCatalogScope(
        { catalog, selection: await select({ ...defaults, includeAuthorIds: [2] }) },
        async (scope) => {
          const vector = table.vectorSearch([0, 0]).where(scope.lanceWhere!).limit(1);
          const keyword = table
            .query()
            .fullTextSearch("legend", { columns: ["text"] })
            .where(scope.lanceWhere!)
            .limit(1);
          const hybrid = table
            .vectorSearch([0, 0])
            .fullTextSearch("legend", { columns: ["text"] })
            .where(scope.lanceWhere!)
            .rerank(await rerankers.RRFReranker.create())
            .limit(1);
          for (const query of [vector, keyword, hybrid]) {
            const rows = z.array(z.object({ parent_id: z.string() })).parse(await query.toArray());
            expect(rows.map(({ parent_id }) => parent_id)).toEqual(["bea"]);
          }
        },
      );
    } finally {
      table.close();
    }
  } finally {
    db.close();
    await rm(directory, { recursive: true, force: true });
  }
});
