import { type DuckDBInstance, JsonDuckDBValueConverter, type Json } from "@duckdb/node-api";
import { waitFor } from "../async";
import { z } from "zod";
import { guidelineCards } from "./cards";
import { describeTables } from "../catalog/tables";
import { withCatalogScope, type ScopeOptions } from "../catalog/scope";
import { withSelect, sqlTimeoutMs } from "../catalog/sql";

const maxResponseBytes = 64 * 1024;
type QueryOptions = ScopeOptions & { limit?: number };

export async function queryCatalog(
  sql: string,
  { limit = 20, signal, catalog, selection }: QueryOptions = {},
) {
  if (!sql.trim() || sql.length > 8_000) {
    throw new Error("Write a SQL query between 1 and 8000 characters.");
  }
  if (!Number.isInteger(limit) || limit < 1 || limit > 50) {
    throw new Error("Choose a row limit between 1 and 50.");
  }
  return withCatalogScope({ catalog, selection, signal }, async (scope) => {
    const result = await executeSQL(await waitFor(scope.database(), signal), sql, limit, signal);
    const idColumns = result.columns.flatMap(({ name }, index) =>
      name === "id" || name === "guideline_id" ? [index] : [],
    );
    const ids = new Set<string>();
    for (const row of result.rows) {
      for (const index of idColumns) {
        const id = z.string().safeParse(row[index]);
        if (id.success && ids.size < limit && scope.ids.has(id.data)) ids.add(id.data);
      }
    }
    return { ...result, matches: guidelineCards(scope, [...ids]) };
  });
}

async function executeSQL(db: DuckDBInstance, sql: string, limit: number, signal?: AbortSignal) {
  return withSelect(
    db,
    sql,
    async (result) => {
      if (result.columnCount > 64) throw new Error("Select at most 64 columns.");
      const columns = result.columnNames().map((name, index) => ({
        name,
        type: result.columnType(index).toString(),
      }));
      const rows: Json[][] = [];
      let bytes = Buffer.byteLength(JSON.stringify(columns));
      if (bytes > maxResponseBytes / 2) throw new Error("Use shorter column names and types.");
      let truncated = false;
      read: for await (const chunk of result) {
        for (let index = 0; index < chunk.rowCount; index++) {
          if (rows.length === limit) {
            truncated = true;
            break read;
          }
          const row = chunk.convertRowValues(index, JsonDuckDBValueConverter);
          bytes += Buffer.byteLength(JSON.stringify(row)) + 1;
          if (bytes > maxResponseBytes - 256) {
            if (rows.length === 0) {
              throw new Error("The first row exceeds 64 KiB. Select fewer or shorter fields.");
            }
            truncated = true;
            break read;
          }
          rows.push(row);
        }
      }
      return { method: "sql" as const, columns, rows, row_count: rows.length, truncated, limit };
    },
    signal,
  );
}

export async function describeCatalog(options: ScopeOptions = {}) {
  return withCatalogScope(options, async (scope) => {
    const info = await scope.catalog.describe();
    return {
      tables: await describeTables(await waitFor(scope.database(), options.signal), info.tables),
      matchedGuidelines: scope.ids.size,
      profiles: info.profiles,
      label_families: info.label_families,
      section_roles: info.section_roles,
      limits: {
        default_rows: 20,
        max_rows: 50,
        max_response_bytes: maxResponseBytes,
        timeout_ms: sqlTimeoutMs,
      },
    };
  });
}
