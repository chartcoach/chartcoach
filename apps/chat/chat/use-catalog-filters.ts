import { useEffect, useRef, useState } from "react";
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

export function useCatalogFilters(initialSelection?: CatalogFilterSelection) {
  const savedSelection = useRef(initialSelection);
  const [metadata, setMetadata] = useState<CatalogMetadata>();
  const [selection, setSelection] = useState<CatalogFilterSelection | undefined>(initialSelection);
  const [error, setError] = useState<string>();
  const [attempt, setAttempt] = useState(0);
  useEffect(() => {
    const controller = new AbortController();
    loadCatalogMetadata(controller.signal)
      .then((catalog) => {
        if (controller.signal.aborted) return;
        setMetadata(catalog);

        if (
          savedSelection.current &&
          savedSelection.current.selection.catalogId !== catalog.catalogId
        ) {
          setSelection(undefined);
          setError(
            "This conversation uses another catalog. Reload guidelines to start a new conversation.",
          );

          return;
        }

        setSelection(
          savedSelection.current ?? {
            filters: emptyCatalogFilters(catalog.catalogId),
            selection: { catalogId: catalog.catalogId, sql: "SELECT id FROM catalog_entries" },
            matchedGuidelines: catalog.totalGuidelines,
          },
        );
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
    savedSelection.current = undefined;
    setMetadata(undefined);
    setSelection(undefined);
    setError(undefined);
    setAttempt((current) => current + 1);
  }

  return { metadata, selection, error, setSelection, reload };
}
