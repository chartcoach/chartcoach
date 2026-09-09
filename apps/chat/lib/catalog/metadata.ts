import type { Catalog } from "@chartcoach/catalog";
import type { DuckDBInstance } from "@duckdb/node-api";
import { createHash } from "node:crypto";
import { catalogMetadataSchema, type CatalogMetadata } from "../../shared/catalog-filters";
import { getCatalog } from "./open";
import { materialize } from "./tables";
import { waitFor } from "../async";

const cache = new WeakMap<Catalog, Promise<CatalogData>>();

export type CatalogData = {
  catalog: Catalog;
  db: DuckDBInstance;
  metadata: CatalogMetadata;
};

export async function getCatalogMetadata(catalog?: Catalog, signal?: AbortSignal) {
  const selected = catalog ?? (await waitFor(getCatalog(), signal));
  return (await waitFor(catalogData(selected), signal)).metadata;
}

export function catalogData(catalog: Catalog) {
  let pending = cache.get(catalog);
  if (!pending) {
    pending = loadData(catalog).catch((error) => {
      cache.delete(catalog);
      throw error;
    });
    cache.set(catalog, pending);
  }
  return pending;
}

async function loadData(catalog: Catalog): Promise<CatalogData> {
  const db = await materialize(catalog);
  const connection = await db.connect().catch((error) => {
    db.closeSync();
    throw error;
  });
  let complete = false;
  try {
    const authors = (
      await connection.runAndReadAll(`SELECT row_number() OVER (ORDER BY name)::INTEGER AS id,
      name, count(DISTINCT guideline_id)::INTEGER AS "guidelineCount"
      FROM guideline_sources, UNNEST(authors) AS names(name)
      GROUP BY name ORDER BY name`)
    ).getRowObjectsJson();
    const sourceTypes = (
      await connection.runAndReadAll(`SELECT row_number() OVER (ORDER BY source_type)::INTEGER AS id,
      source_type AS name, count(DISTINCT guideline_id)::INTEGER AS "guidelineCount"
      FROM guideline_sources WHERE source_type IS NOT NULL GROUP BY source_type ORDER BY source_type`)
    ).getRowObjectsJson();
    const years = (
      await connection.runAndReadAll(`SELECT min(try_cast(year AS INTEGER)) AS min,
      max(try_cast(year AS INTEGER)) AS max,
      (SELECT count(*)::INTEGER FROM guidelines g WHERE NOT EXISTS (
        SELECT 1 FROM guideline_sources s WHERE s.guideline_id = g.id AND try_cast(s.year AS INTEGER) IS NOT NULL
      )) AS "undatedGuidelines" FROM guideline_sources`)
    ).getRowObjectsJson()[0];
    const info = await catalog.describe();
    const catalogId =
      info.release_digest ??
      createHash("sha256")
        .update(info.entries_digest + info.manifest_digest)
        .digest("hex");
    const metadata = catalogMetadataSchema.parse({
      catalogId,
      totalGuidelines: catalog.length,
      authors,
      sourceTypes,
      years,
      tables: info.tables,
    });
    complete = true;
    return { catalog, db, metadata };
  } finally {
    connection.closeSync();
    if (!complete) db.closeSync();
  }
}
