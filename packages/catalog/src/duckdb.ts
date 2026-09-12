import type { DuckDBConnection } from "@duckdb/node-api";
import type { Catalog } from "./catalog/model";
import { registrationPlan, type RegisterCatalogOptions } from "./catalog/registration";

export type { RegisterCatalogOptions } from "./catalog/registration";

/** Create or replace canonical catalog tables in a caller-owned DuckDB connection. */
export async function registerCatalog(
  connection: DuckDBConnection,
  catalog: Catalog,
  options: RegisterCatalogOptions = {},
): Promise<DuckDBConnection> {
  for (const { sql, rows } of registrationPlan(catalog, options, "parameter")) {
    await connection.run(sql, [rows]);
  }

  return connection;
}
