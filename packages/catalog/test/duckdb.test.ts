import { DuckDBInstance } from "@duckdb/node-api";
import { expect, it } from "vite-plus/test";
import { Catalog, CatalogError } from "@chartcoach/catalog";
import { registerCatalog } from "../src/duckdb";
import { fixtureCatalog } from "./catalog-testkit";

it("keeps catalog registration inside the caller's transaction", async () => {
  const catalog = await fixtureCatalog();
  const db = await DuckDBInstance.create(":memory:");
  const connection = await db.connect();

  try {
    await connection.run("CREATE TABLE guidelines AS SELECT 'retained' AS id");
    await connection.run("BEGIN TRANSACTION");
    await registerCatalog(connection, catalog);
    await connection.run("ROLLBACK");
    expect((await connection.runAndReadAll("SELECT * FROM guidelines")).getRowsJson()).toEqual([
      ["retained"],
    ]);
    expect(
      (
        await connection.runAndReadAll("SELECT table_name FROM information_schema.tables")
      ).getRowsJson(),
    ).toEqual([["guidelines"]]);
  } finally {
    connection.closeSync();
    db.closeSync();
  }
});

it("leaves the caller connection usable after a native table replacement error", async () => {
  const catalog = await fixtureCatalog();
  const db = await DuckDBInstance.create(":memory:");
  const connection = await db.connect();

  try {
    await connection.run("CREATE VIEW guidelines AS SELECT 'retained' AS id");
    await expect(registerCatalog(connection, catalog)).rejects.toThrow();
    expect((await connection.runAndReadAll("SELECT * FROM guidelines")).getRowsJson()).toEqual([
      ["retained"],
    ]);
  } finally {
    connection.closeSync();
    db.closeSync();
  }
});

it("validates catalog inputs before replacing tables and preserves caller connection ownership", async () => {
  const catalog = await fixtureCatalog();
  const db = await DuckDBInstance.create(":memory:");
  const connection = await db.connect();

  try {
    await connection.run("CREATE TABLE guidelines AS SELECT 'retained' AS id");
    await connection.run("CREATE TABLE application_state AS SELECT 42 AS value");
    await expect(registerCatalog(connection, catalog, { ids: ["missing"] })).rejects.toMatchObject({
      code: "lookup",
    });

    const invalid = new Catalog(
      [{ ...catalog.guidelines[0]!, references: ["not a BibTeX entry"] }],
      catalog.manifest,
    );

    await expect(registerCatalog(connection, invalid)).rejects.toBeInstanceOf(CatalogError);
    expect((await connection.runAndReadAll("SELECT * FROM guidelines")).getRowsJson()).toEqual([
      ["retained"],
    ]);
    expect(await registerCatalog(connection, catalog)).toBe(connection);
    expect(
      (await connection.runAndReadAll("SELECT * FROM application_state")).getRowsJson(),
    ).toEqual([[42]]);
  } finally {
    connection.closeSync();
    db.closeSync();
  }
});
