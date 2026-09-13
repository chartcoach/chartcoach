import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { cp, mkdir, readFile, rename, stat, writeFile } from "node:fs/promises";
import { createRequire } from "node:module";
import { join } from "node:path";

import { loadCatalog, parseCatalogRelease } from "@chartcoach/catalog";
import { artifactPath, indexPath, openCatalog } from "@chartcoach/catalog/node";
import { registerCatalog } from "@chartcoach/catalog/duckdb";

const [fixture, directory] = process.argv.slice(2);

const require = createRequire(import.meta.url);

assert.throws(() => require.resolve("@lancedb/lancedb"), { code: "MODULE_NOT_FOUND" });

assert.throws(() => require.resolve("@duckdb/node-api"), { code: "MODULE_NOT_FOUND" });

await assert.rejects(stat(new URL("node_modules/@duckdb", import.meta.url)), { code: "ENOENT" });

await mkdir(directory, { recursive: true });

const catalog = await openCatalog(fixture, { cacheDirectory: join(directory, "cache") });

assert.ok(catalog.length >= 3, "The consumer fixture needs entries for native search");

const ids = catalog.query({ limit: catalog.length }).map(({ id }) => id);

assert.deepEqual(
  catalog.read({ ids }).map(({ id }) => id),
  ids,
);

assert.ok(catalog.cite({ ids }).some(({ sources }) => sources.some(({ citation }) => citation)));

const core = await loadCatalog({
  releaseUrl: catalog.releaseUrl,
  release: parseCatalogRelease(JSON.parse(await readFile(join(fixture, "release.json"), "utf8"))),
  entries: await readFile(await artifactPath(catalog, "entries.parquet")),
  manifest: await readFile(await artifactPath(catalog, "MANIFEST.md")),
});

assert.deepEqual(core.query({ limit: core.length }), catalog.query({ limit: catalog.length }));

const info = await catalog.describe();

assert.equal(info.tables.length, 6);

assert.equal(catalog.table("references").length, 1);

const { DuckDBInstance } = await import(process.env.DUCKDB_MODULE);

const database = await DuckDBInstance.create(":memory:");

const sql = await database.connect();

try {
  assert.equal(await registerCatalog(sql, catalog, { ids: [ids[0]] }), sql);
  const result = await sql.runAndReadAll("SELECT id FROM guidelines");
  assert.deepEqual(result.getRowsJson(), [[ids[0]]]);
  const references = await sql.runAndReadAll('SELECT count(*)::INTEGER FROM "references"');
  assert.deepEqual(references.getRowsJson(), [[1]]);
} finally {
  sql.closeSync();
  database.closeSync();
}

// The application supplies its native SDK independently of the catalog installation.
const lance = await import(process.env.LANCE_MODULE);

const { default: tar } = await import(process.env.TAR_MODULE);

const source = join(directory, "index-source");

const connection = await lance.connect(source);

const rows = [
  { parent_id: ids[0], text: "direct labels", vector: [1, 0] },
  { parent_id: ids[1], text: "color contrast", vector: [0, 1] },
  { parent_id: ids[2], text: "size", vector: [0.5, 0.5] },
].map((row, row_id) => ({
  ...row,
  row_id,
  id: `${row.parent_id}---overview`,
  role: "overview",
  labels: [...catalog.require(row.parent_id).labels],
  content_hash: createHash("sha256").update(row.text).digest("hex"),
}));

const table = await connection.createTable("documents", rows.slice(0, 2));

await table.createIndex("text", { config: lance.Index.fts() });

table.close();

connection.close();

const releaseDirectory = join(directory, "release");

await cp(fixture, releaseDirectory, { recursive: true });

const profileDirectory = join(releaseDirectory, "profiles", "local");

await mkdir(profileDirectory, { recursive: true });

await tar.create({ cwd: source, file: join(profileDirectory, "index.tar.gz"), gzip: true }, [
  "documents.lance",
]);

await writeFile(
  join(profileDirectory, "profile.json"),
  JSON.stringify({
    schema_version: 1,
    documents_version: 1,
    entries_digest: info.entries_digest,
    manifest_digest: info.manifest_digest,
    embedding_functions: [
      { name: "manual", model: {}, source_column: "text", vector_column: "vector" },
    ],
    dimensions: 2,
    distance_metric: "cosine",
    python_requirements: {},
    lancedb_version: process.env.LANCE_VERSION,
    projection: null,
  }),
);

const artifacts = {};

for (const path of [
  "MANIFEST.md",
  "entries.parquet",
  "profiles/local/index.tar.gz",
  "profiles/local/profile.json",
]) {
  const bytes = await readFile(join(releaseDirectory, path));
  artifacts[path] = {
    bytes: bytes.length,
    sha256: createHash("sha256").update(bytes).digest("hex"),
  };
}

const release = { artifacts, schema_version: 1 };

const digest = createHash("sha256").update(JSON.stringify(release)).digest("hex");

await writeFile(join(releaseDirectory, "release.json"), JSON.stringify({ ...release, digest }));

const indexed = await openCatalog(releaseDirectory, { cacheDirectory: join(directory, "cache") });

const index = await indexPath(indexed, "local");

assert.equal(await indexPath(indexed, "local"), index);

await rename(releaseDirectory, `${releaseDirectory}-offline`);

assert.equal(await indexPath(indexed, "local"), index);

const db = await lance.connect(index);

const documents = await db.openTable("documents");

await documents.checkout(await documents.version());

assert.equal((await documents.vectorSearch([1, 0]).limit(1).toArray())[0].parent_id, ids[0]);

assert.equal(
  (await documents.query().fullTextSearch("contrast").limit(1).toArray())[0].parent_id,
  ids[1],
);

documents.close();

db.close();

const owned = await indexPath(indexed, "local", { directory: join(directory, "owned-index") });

assert.notEqual(owned, index);

const writable = await lance.connect(owned);

const ownedTable = await writable.openTable("documents");

await ownedTable.add(rows.slice(2));

assert.equal(await ownedTable.countRows(), 3);

ownedTable.close();

writable.close();

console.log(
  `Verified Node ${process.versions.node} catalog tables, citations, cache, DuckDB and LanceDB composition`,
);
