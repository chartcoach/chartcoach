import type { Coordinator } from "@uwdata/mosaic-core";
import type { CatalogSelection } from "../shared/catalog-selection";

const matchesPerBatch = 100;

export type CatalogMatch = { id: string; title: string };

function matchQuery(selection: CatalogSelection, batch: number) {
  if (!Number.isSafeInteger(batch) || batch < 0 || !Number.isSafeInteger(batch * matchesPerBatch)) {
    throw new Error("Choose a valid guideline batch.");
  }

  return `SELECT g.id, g.title FROM catalog_entries g WHERE g.id IN (${selection.sql}) ORDER BY g.title, g.id LIMIT ${matchesPerBatch} OFFSET ${batch * matchesPerBatch}`;
}

export async function catalogMatches(
  coordinator: Coordinator,
  selection: CatalogSelection,
  batch: number,
): Promise<CatalogMatch[]> {
  const result = await coordinator.query(matchQuery(selection, batch));
  const rows = result.toArray().map((row) => ({ id: String(row.id), title: String(row.title) }));

  if (rows.length === matchesPerBatch) {
    void coordinator.prefetch(matchQuery(selection, batch + 1)).catch(() => {});
  }

  return rows;
}
