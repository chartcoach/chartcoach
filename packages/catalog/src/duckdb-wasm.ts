import type { AsyncDuckDBConnection } from "@duckdb/duckdb-wasm";
import type { Catalog } from "./catalog/model";
import { registrationPlan, type RegisterCatalogOptions } from "./catalog/registration";

export type { RegisterCatalogOptions } from "./catalog/registration";

/** Create or replace canonical catalog tables in a caller-owned DuckDB-WASM connection. */
export async function registerCatalog(
  connection: AsyncDuckDBConnection,
  catalog: Catalog,
  options: RegisterCatalogOptions = {},
): Promise<AsyncDuckDBConnection> {
  for (const { sql, rows } of registrationPlan(catalog, options, "file")) {
    const file = `chartcoach-${crypto.randomUUID()}.json`;
    // DuckDB-WASM copies string parameters onto its fixed-size Emscripten stack.
    // File buffers carry catalog payloads through heap memory instead.
    await connection.bindings.registerFileBuffer(file, new TextEncoder().encode(rows));
    try {
      const statement = await connection.prepare(sql);
      try {
        await statement.query(file);
      } finally {
        await statement.close();
      }
    } finally {
      await connection.bindings.dropFile(file);
    }
  }
  return connection;
}
