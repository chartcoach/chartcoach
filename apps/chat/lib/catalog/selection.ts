import { JsonDuckDBValueConverter } from "@duckdb/node-api";
import type { Catalog } from "@chartcoach/catalog";
import { z } from "zod";
import { catalogSelectionSchema, type CatalogSelection } from "../../shared/catalog-selection";
import { waitFor } from "../async";
import { catalogData } from "./metadata";
import { getCatalog } from "./open";
import { withSelect } from "./sql";
import { resolvedSelectionSchema, type ResolvedSelection } from "../../shared/resolved-selection";

type SelectionOptions = { catalog?: Catalog; signal?: AbortSignal };

export async function resolveCatalogSelection(
  query: CatalogSelection,
  { catalog, signal }: SelectionOptions = {},
): Promise<ResolvedSelection> {
  signal?.throwIfAborted();
  const selected = catalog ?? (await waitFor(getCatalog(), signal));
  const data = await waitFor(catalogData(selected), signal);
  const selection = catalogSelectionSchema.parse(query);

  if (selection.catalogId !== data.metadata.catalogId)
    throw new Error("The catalog changed. Reload the catalog and start a new review.");
  const known = new Set(selected.table("guidelines").map(({ id }) => id));

  const ids = await withSelect(
    data.db,
    selection.sql,
    async (result) => {
      if (
        result.columnCount !== 1 ||
        result.columnNames()[0] !== "id" ||
        result.columnType(0).toString() !== "VARCHAR"
      )
        throw new Error("The selection query must return one VARCHAR column named id.");
      const ids = new Set<string>();
      let count = 0;

      for await (const chunk of result) {
        for (let index = 0; index < chunk.rowCount; index++) {
          if (++count > selected.length)
            throw new Error(
              "The selection query returned more rows than the catalog. Select distinct guideline IDs.",
            );

          const id = z
            .string()
            .safeParse(chunk.convertRowValues(index, JsonDuckDBValueConverter)[0]);

          if (!id.success || !known.has(id.data))
            throw new Error("The selection query returned an unknown or null guideline ID.");
          ids.add(id.data);
        }
      }

      return [...ids].sort();
    },
    signal,
  );

  return resolvedSelectionSchema.parse({ catalogId: selection.catalogId, ids });
}
