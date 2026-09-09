import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

import { DuckDBInstance } from "@duckdb/node-api";
import { describe, expect, it } from "vite-plus/test";

import { Catalog, parseCatalogManifest } from "@chartcoach/catalog";
import fixture from "../../../fixtures/catalog-contract/tables.json";
import { registerCatalog } from "../src/duckdb";
import { fixtureCatalog } from "./catalog-testkit";

describe("Python and JavaScript catalog tables", () => {
  it("preserves canonical rows and logical schemas across authored and released catalogs", async () => {
    const python = JSON.parse(
      execFileSync(
        "uv",
        [
          "run",
          "--locked",
          "--package",
          "chartcoach",
          "--no-dev",
          "python",
          "packages/chartcoach/tests/catalog_tables_contract.py",
        ],
        {
          cwd: fileURLToPath(new URL("../../..", import.meta.url)),
          encoding: "utf8",
          timeout: 120_000,
        },
      ),
    );
    const manifest = parseCatalogManifest(fixture.manifest);
    const cases = {
      release: await fixtureCatalog(),
      empty: new Catalog([], manifest),
      relational: new Catalog(fixture.guidelines, manifest),
      reversed: new Catalog([...fixture.guidelines].reverse(), manifest),
    };
    for (const [name, catalog] of Object.entries(cases)) {
      const description = (await catalog.describe()).tables;
      const tables = Object.fromEntries(
        description.map((table) => [table.name, catalog.table(table.name)]),
      );
      expect({ description, tables }, name).toEqual({
        description: python[name].description,
        tables: python[name].tables,
      });
      const db = await DuckDBInstance.create(":memory:");
      const connection = await db.connect();
      try {
        const registrations = [];
        const selectedIds = catalog
          .table("guidelines")
          .slice(0, 1)
          .flatMap(({ id }) => [id, id]);
        for (const ids of [undefined, [], selectedIds]) {
          expect(await registerCatalog(connection, catalog, { ids })).toBe(connection);
          const registeredTables = Object.fromEntries(
            await Promise.all(
              description.map(async ({ name }) => {
                const rows = await connection.runAndReadAll(`SELECT * FROM "${name}" ORDER BY ALL`);
                const schema = await connection.runAndReadAll(`DESCRIBE "${name}"`);
                return [name, { rows: rows.getRowsJson(), schema: schema.getRowsJson() }];
              }),
            ),
          );
          registrations.push({ ids: ids ?? null, tables: registeredTables });
        }
        expect(registrations, `${name} DuckDB registrations`).toEqual(python[name].registrations);
      } finally {
        connection.closeSync();
        db.closeSync();
      }
    }

    expect(cases.relational.table("references")).toHaveLength(3);
    expect(cases.relational.table("guideline_references")).toHaveLength(4);
    expect(cases.relational.table("guideline_labels")).toHaveLength(3);
    expect(cases.relational.table("references")).toEqual(cases.reversed.table("references"));
    expect(cases.empty.table("guidelines")).toEqual([]);
    expect(cases.empty.table("references")).toEqual([]);
  }, 150_000);
});
