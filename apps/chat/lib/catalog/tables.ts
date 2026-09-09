import type { Catalog, TableInfo } from "@chartcoach/catalog";
import { registerCatalog } from "@chartcoach/catalog/duckdb";
import { DuckDBInstance } from "@duckdb/node-api";

export async function describeTables(db: DuckDBInstance, tables: readonly TableInfo[]) {
  const connection = await db.connect();
  try {
    const scoped: TableInfo[] = [];
    for (const table of tables) {
      const result = await connection.runAndReadAll(
        `SELECT count(*)::INTEGER FROM "${table.name}"`,
      );
      scoped.push({ ...table, rows: Number(result.getRowsJson()[0]![0]) });
    }
    return scoped;
  } finally {
    connection.closeSync();
  }
}

export async function materialize(catalog: Catalog, ids?: readonly string[]) {
  const db = await DuckDBInstance.create(":memory:", {
    threads: "2",
    memory_limit: "256MB",
    temp_directory: "",
    max_temp_directory_size: "0B",
    enable_external_access: "false",
    autoinstall_known_extensions: "false",
    autoload_known_extensions: "false",
    allow_persistent_secrets: "false",
  });
  const connection = await db.connect().catch((error) => {
    db.closeSync();
    throw error;
  });
  let complete = false;
  try {
    await registerCatalog(connection, catalog, { ids });
    await connection.run(
      "CREATE VIEW catalog_entries AS SELECT id, title, description FROM guidelines",
    );
    await connection.run("SET lock_configuration = true");
    complete = true;
    return db;
  } finally {
    connection.closeSync();
    if (!complete) db.closeSync();
  }
}
