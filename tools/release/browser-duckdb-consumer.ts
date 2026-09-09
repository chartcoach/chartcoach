import { AsyncDuckDB, VoidLogger, type AsyncDuckDBConnection } from "@duckdb/duckdb-wasm";
import { Catalog, openCatalog, parseCatalogManifest, type JsonValue } from "@chartcoach/catalog";
import { registerCatalog } from "@chartcoach/catalog/duckdb-wasm";

function equal(
  actual: JsonValue | undefined,
  expected: JsonValue | undefined,
  label: string,
): void {
  if (JSON.stringify(actual) !== JSON.stringify(expected))
    throw new Error(`${label}: ${JSON.stringify(actual)} != ${JSON.stringify(expected)}`);
}

async function rows(connection: AsyncDuckDBConnection, table: string): Promise<JsonValue[]> {
  const result = await connection.query(`SELECT to_json(record) AS row FROM "${table}" record`);
  return result.toArray().map((row) => JSON.parse(row.row));
}

async function checkBrowserDuckDB(release: Catalog): Promise<void> {
  const worker = new Worker(new URL("/duckdb/duckdb-browser-eh.worker.js", location.href));
  const db = new AsyncDuckDB(new VoidLogger(), worker);
  try {
    await db.instantiate(new URL("/duckdb/duckdb-eh.wasm", location.href).href);
    const connection = await db.connect();
    try {
      if ((await registerCatalog(connection, release)) !== connection)
        throw new Error("Registration must return the caller connection");
      equal((await rows(connection, "guidelines")).length, 6, "Release guidelines");
      const entries = await release.artifact("entries.parquet");
      await db.registerFileBuffer("entries.parquet", entries);
      const raw = await connection.query(
        "SELECT count(*)::INTEGER AS count FROM 'entries.parquet'",
      );
      equal(raw.get(0)?.count, 6, "Verified Parquet queries");

      const fixture = await (await fetch("/tables.json")).json();
      const catalog = new Catalog(fixture.guidelines, parseCatalogManifest(fixture.manifest));
      const description = (await catalog.describe()).tables;
      await registerCatalog(connection, catalog);
      const schemas = new Map<string, JsonValue>();
      for (const { name } of description) {
        equal(await rows(connection, name), catalog.table(name), `${name} values`);
        schemas.set(
          name,
          (await connection.query(`DESCRIBE "${name}"`)).toArray().map(Object.fromEntries),
        );
      }
      const descriptions = await connection.query(
        "SELECT description FROM guidelines WHERE id = '𐀀'",
      );
      equal(
        descriptions.get(0)?.description,
        'Keep "quoted" content, tabs\tand a literal backslash \\ together.',
        "Escaped content",
      );
      await registerCatalog(connection, catalog, { ids: ["𐀀", "𐀀"] });
      equal((await rows(connection, "guidelines")).length, 1, "Selected guidelines");
      equal((await rows(connection, "references")).length, 2, "Selected sources");
      equal((await rows(connection, "guideline_references")).length, 2, "Selected reference links");

      await connection.query("BEGIN TRANSACTION");
      await registerCatalog(connection, catalog, { ids: [] });
      for (const { name } of description) {
        equal(await rows(connection, name), [], `${name} empty selection`);
        equal(
          (await connection.query(`DESCRIBE "${name}"`)).toArray().map(Object.fromEntries),
          schemas.get(name),
          `${name} empty schema`,
        );
      }
      await connection.query("ROLLBACK");
      equal((await rows(connection, "guidelines")).length, 1, "Caller transaction rollback");
      try {
        await registerCatalog(connection, catalog, { ids: ["missing"] });
        throw new Error("Unknown guideline ID accepted");
      } catch (error) {
        if (!(error instanceof Error) || !("code" in error) || error.code !== "lookup") throw error;
      }
      equal((await rows(connection, "guidelines")).length, 1, "Validation before replacement");
      const large = new Catalog(
        [
          {
            ...catalog.require("𐀀"),
            sections: [
              {
                role: "advice",
                title: "Labels",
                content: 'Keep "quoted" labels.\n'.repeat(150_000) + "End.",
              },
            ],
          },
        ],
        catalog.manifest,
      );
      await registerCatalog(connection, large);
      const content = await connection.query(
        "SELECT length(content)::INTEGER AS length, right(content, 4) AS ending FROM sections",
      );
      equal(content.get(0)?.length, 3_300_004, "Large catalog content length");
      equal(content.get(0)?.ending, "End.", "Large catalog content ending");
      equal(
        (await db.globFiles("*")).map(({ fileName }) => fileName),
        ["entries.parquet"],
        "Registration file cleanup",
      );
      await connection.query(
        "DROP TABLE guidelines; CREATE VIEW guidelines AS SELECT 'retained' AS id",
      );
      let rejected = false;
      try {
        await registerCatalog(connection, catalog);
      } catch {
        rejected = true;
      }
      equal(rejected, true, "Native replacement error");
      equal(await rows(connection, "guidelines"), [{ id: "retained" }], "Connection after error");
      equal(
        (await db.globFiles("*")).map(({ fileName }) => fileName),
        ["entries.parquet"],
        "Registration error file cleanup",
      );
    } finally {
      await connection.close();
    }
  } finally {
    await db.terminate();
    worker.terminate();
  }
}

await checkBrowserDuckDB(await openCatalog(new URL("/catalog/release.json", location.href)));
document.body.dataset.duckdbVerified = "true";
