import type { Catalog } from "@chartcoach/catalog";
import type { DuckDBInstance } from "@duckdb/node-api";
import { getCatalog } from "./open";
import { catalogData, type CatalogData } from "./metadata";
import { materialize } from "./tables";
import { waitFor } from "../async";
import { resolvedSelectionSchema, type ResolvedSelection } from "./selection";

const maxScopes = 8;
const cache = new WeakMap<CatalogData, Map<string, CachedScope>>();

export type CatalogScope = Readonly<{
  catalog: Catalog;
  selection: ResolvedSelection;
  ids: ReadonlySet<string>;
  lanceWhere: string | undefined;
  database: () => Promise<DuckDBInstance>;
}>;
export type ScopeOptions = {
  catalog?: Catalog;
  selection?: ResolvedSelection;
  signal?: AbortSignal;
};
type CachedScope = {
  value: ScopeData;
  users: number;
};
type ScopeData = CatalogScope & { dispose: () => void };

export async function withCatalogScope<T>(
  { catalog, selection, signal }: ScopeOptions,
  use: (scope: CatalogScope) => Promise<T>,
): Promise<T> {
  signal?.throwIfAborted();
  const selected = catalog ?? (await waitFor(getCatalog(), signal));
  const data = await waitFor(catalogData(selected), signal);
  const known = new Set(selected.table("guidelines").map(({ id }) => id));
  const canonical = resolvedSelectionSchema.parse(
    selection ?? { catalogId: data.metadata.catalogId, ids: [...known] },
  );
  if (canonical.catalogId !== data.metadata.catalogId)
    throw new Error("The catalog changed. Reload the catalog and start a new review.");
  if (canonical.ids.length > selected.length || canonical.ids.some((id) => !known.has(id)))
    throw new Error("The review selection contains unknown guideline IDs. Start a new review.");
  const ids = [...new Set(canonical.ids)].sort();
  let scopes = cache.get(data);
  if (!scopes) {
    scopes = new Map();
    cache.set(data, scopes);
  }
  const key = JSON.stringify(ids);
  let entry = scopes.get(key);
  if (!entry) {
    if (scopes.size === maxScopes) {
      const idle = [...scopes].find(([, scope]) => scope.users === 0);
      if (!idle)
        throw new Error("The catalog is serving several filter selections. Try again shortly.");
      scopes.delete(idle[0]);
      idle[1].value.dispose();
    }
    entry = { value: createScope(data, { catalogId: canonical.catalogId, ids }), users: 0 };
    scopes.set(key, entry);
  } else {
    scopes.delete(key);
    scopes.set(key, entry);
  }
  entry.users++;
  try {
    signal?.throwIfAborted();
    return await use(entry.value);
  } finally {
    entry.users--;
  }
}

export function assertCatalogIds(scope: CatalogScope, ids: readonly string[]) {
  for (const id of ids) {
    if (!scope.ids.has(id))
      throw new Error(`Guideline ${JSON.stringify(id)} is outside this review's catalog filters.`);
  }
}

function createScope(data: CatalogData, selection: ResolvedSelection): ScopeData {
  const ids = new Set(selection.ids);
  let pending: Promise<DuckDBInstance> | undefined;
  let owned: DuckDBInstance | undefined;
  let retired = false;
  return {
    catalog: data.catalog,
    selection,
    ids,
    lanceWhere:
      ids.size === data.catalog.length
        ? undefined
        : ids.size === 0
          ? "false"
          : `parent_id IN (${[...ids].map((id) => `'${id.replaceAll("'", "''")}'`).join(",")})`,
    database() {
      if (ids.size === data.catalog.length) return Promise.resolve(data.db);
      return (pending ??= materialize(data.catalog, [...ids])
        .then((db) => {
          if (retired) {
            db.closeSync();
            throw new Error("The catalog filter selection expired. Try again.");
          }
          owned = db;
          return db;
        })
        .catch((error) => {
          pending = undefined;
          throw error;
        }));
    },
    dispose() {
      retired = true;
      owned?.closeSync();
    },
  };
}
