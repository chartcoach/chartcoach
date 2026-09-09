import { useEffect, useState } from "react";
import {
  emptyCatalogFilters,
  type CatalogFilters,
  type CatalogMetadata,
} from "../shared/catalog-filters";
import { loadCatalogMetadata } from "../lib/catalog-client";
import type { CatalogSelection } from "../shared/catalog-selection";

export type CatalogFilterSelection = {
  filters: CatalogFilters;
  selection: CatalogSelection;
  matchedGuidelines: number;
};

export function useCatalogFilters() {
  const [metadata, setMetadata] = useState<CatalogMetadata>();
  const [selection, setSelection] = useState<CatalogFilterSelection>();
  const [error, setError] = useState<string>();
  const [attempt, setAttempt] = useState(0);
  useEffect(() => {
    const controller = new AbortController();
    loadCatalogMetadata(controller.signal)
      .then((catalog) => {
        if (controller.signal.aborted) return;
        setMetadata(catalog);
        setSelection({
          filters: emptyCatalogFilters(catalog.catalogId),
          selection: { catalogId: catalog.catalogId, sql: "SELECT id FROM catalog_entries" },
          matchedGuidelines: catalog.totalGuidelines,
        });
        setError(undefined);
      })
      .catch((cause) => {
        if (!controller.signal.aborted)
          setError(
            cause instanceof Error ? cause.message : "Could not load the catalog. Try again.",
          );
      });
    return () => controller.abort();
  }, [attempt]);

  function reload() {
    setMetadata(undefined);
    setSelection(undefined);
    setError(undefined);
    setAttempt((current) => current + 1);
  }

  return { metadata, selection, error, setSelection, reload };
}
