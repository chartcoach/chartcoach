import { makeClient, Selection, type Coordinator, type MosaicClient } from "@uwdata/mosaic-core";
import { and, literal, type FilterExpr } from "@uwdata/mosaic-sql";
import {
  catalogFiltersSchema,
  type CatalogFilters,
  type CatalogMetadata,
} from "../shared/catalog-filters";
import { sourcePredicates } from "../shared/catalog-predicate";
import type { CatalogSelection } from "../shared/catalog-selection";

export type ExplorerData = {
  key: string;
  selection: CatalogSelection;
  matchedGuidelines: number;
  authors: { id: number; count: number }[];
  sourceTypes: { id: number; count: number }[];
  years: { from: number; to: number; count: number }[];
  matches: { id: string; title: string }[];
};

type Rows = Record<string, string | number | bigint | null>[];
const sourceRows = "FROM catalog_entries g LEFT JOIN guideline_sources s ON s.guideline_id = g.id";

export function exploreCatalog(
  coordinator: Coordinator,
  metadata: CatalogMetadata,
  filters: CatalogFilters,
  onData: (data: ExplorerData) => void,
  onError: (error: Error) => void,
) {
  filters = catalogFiltersSchema.parse(filters);
  const predicates = sourcePredicates(filters, metadata);
  const selection = Selection.crossfilter();
  const clients: MosaicClient[] = [];
  let active = true;
  const parts = new Map<string, Rows>();
  let selectionSql: string | undefined;
  const min = metadata.years.min;
  const max = metadata.years.max;
  const width = min !== null && max !== null ? Math.max(1, Math.ceil((max - min + 1) / 48)) : 1;

  function publish() {
    if (!active || parts.size !== 5 || !selectionSql) return;
    const authorCounts = new Map(parts.get("authors")!.map((row) => [row.name, Number(row.count)]));
    const typeCounts = new Map(parts.get("types")!.map((row) => [row.name, Number(row.count)]));
    const yearCounts = new Map(
      parts.get("years")!.map((row) => [Number(row.start), Number(row.count)]),
    );
    const years: ExplorerData["years"] = [];
    if (min !== null && max !== null) {
      for (let from = min; from <= max; from += width) {
        years.push({ from, to: Math.min(max, from + width - 1), count: yearCounts.get(from) ?? 0 });
      }
    }
    onData({
      key: JSON.stringify(filters),
      selection: { catalogId: metadata.catalogId, sql: selectionSql },
      matchedGuidelines: Number(parts.get("count")![0].count),
      authors: metadata.authors.map(({ id, name }) => ({ id, count: authorCounts.get(name) ?? 0 })),
      sourceTypes: metadata.sourceTypes.map(({ id, name }) => ({
        id,
        count: typeCounts.get(name) ?? 0,
      })),
      years,
      matches: parts
        .get("matches")!
        .map((row) => ({ id: String(row.id), title: String(row.title) })),
    });
  }

  function client(name: string, query: (where: string) => string) {
    const result = makeClient({
      coordinator,
      selection,
      enabled: false,
      filterStable: false,
      query: (filter: FilterExpr) => query(String(and(filter ?? [])) || "TRUE"),
      queryResult: (data) => {
        if (!active) return;
        // SAFETY: Mosaic returns Arrow tables. These queries project string or numeric columns.
        parts.set(name, (data as { toArray(): Rows }).toArray());
        publish();
      },
      queryError: (error) => {
        if (active) onError(error);
      },
    });
    clients.push(result);
    return result;
  }

  client("count", (where) => {
    selectionSql = `SELECT DISTINCT g.id ${sourceRows} WHERE ${where}`;
    return `SELECT count(*)::INTEGER AS count FROM (${selectionSql}) selection`;
  });
  client(
    "matches",
    (where) =>
      `SELECT DISTINCT g.id, g.title ${sourceRows} WHERE ${where} ORDER BY g.title, g.id LIMIT 6`,
  );
  const authors = client(
    "authors",
    (where) =>
      `SELECT names.name, count(DISTINCT g.id)::INTEGER AS count ${sourceRows}, UNNEST(s.authors) AS names(name) WHERE ${where} GROUP BY names.name`,
  );
  const types = client(
    "types",
    (where) =>
      `SELECT s.source_type AS name, count(DISTINCT g.id)::INTEGER AS count ${sourceRows} WHERE (${where}) AND s.source_type IS NOT NULL GROUP BY s.source_type`,
  );
  const years = client("years", (where) =>
    min === null
      ? "SELECT NULL::INTEGER AS start, 0::INTEGER AS count WHERE FALSE"
      : `SELECT (${min} + floor((try_cast(s.year AS INTEGER)::DOUBLE - ${min}) / ${width}) * ${width})::BIGINT AS start, count(DISTINCT g.id)::INTEGER AS count ${sourceRows} WHERE (${where}) AND try_cast(s.year AS INTEGER) IS NOT NULL GROUP BY start ORDER BY start`,
  );
  void (async () => {
    for (const [predicate, facet] of [
      [predicates.authors, authors],
      [predicates.types, types],
      [predicates.years, years],
      // A global active clause makes Mosaic recompute every facet after a draft update.
      [predicates.excludedAuthors ?? literal(true), undefined],
    ] as const) {
      if (!active) return;
      selection.update({
        source: {},
        clients: facet ? new Set([facet]) : undefined,
        fields: [],
        value: filters,
        predicate: predicate ?? null,
      });
      // pending() awaits the current event, so settle each clause before publishing the next.
      await selection.pending("value");
    }
    if (active) for (const item of clients) item.enabled = true;
  })().catch((error) => {
    if (active) onError(error);
  });
  return () => {
    active = false;
    for (const item of clients) item.destroy();
    coordinator.clear({ cache: false });
  };
}
