import { useEffect, useState } from "react";
import type { openBrowserCatalog } from "../browser/catalog";
import type { ExplorerData } from "../browser/explorer";
import {
  catalogFiltersSchema,
  type CatalogFilters,
  type CatalogMetadata,
} from "../shared/catalog-filters";

type BrowserCatalog = Awaited<ReturnType<typeof openBrowserCatalog>>;
type Explorer = { catalog: BrowserCatalog; metadata: CatalogMetadata };

export function useCatalogExplorer(
  metadata: CatalogMetadata,
  draft: CatalogFilters | undefined,
  enabled = true,
) {
  const [activated, setActivated] = useState(enabled);
  const [engine, setEngine] = useState<Explorer>();
  const [data, setData] = useState<ExplorerData>();
  const [error, setError] = useState<string>();
  const [attempt, setAttempt] = useState(0);
  const key = draft ? JSON.stringify(catalogFiltersSchema.parse(draft)) : undefined;

  useEffect(() => {
    if (enabled) setActivated(true);
  }, [enabled]);

  useEffect(() => {
    if (!activated) return;
    const controller = new AbortController();
    let catalog: BrowserCatalog | undefined;
    setEngine(undefined);
    setData(undefined);
    setError(undefined);
    void import("../browser/catalog")
      .then(({ openBrowserCatalog }) =>
        openBrowserCatalog(metadata.catalogId, controller.signal, (cause) => {
          if (!controller.signal.aborted) {
            setEngine(undefined);
            setError(cause.message);
          }
        }),
      )
      .then((opened) => {
        catalog = opened;
        if (controller.signal.aborted) opened.close();
        else setEngine({ catalog: opened, metadata });
      })
      .catch((cause) => {
        if (!controller.signal.aborted)
          setError(cause instanceof Error ? cause.message : "Could not load the browser catalog.");
      });
    return () => {
      controller.abort();
      if (catalog) catalog.close();
    };
  }, [metadata, attempt, activated]);

  useEffect(() => {
    if (!enabled || !engine || engine.metadata !== metadata || !key) return;
    let active = true;
    let destroy: (() => void) | undefined;
    setError(undefined);
    void import("../browser/explorer")
      .then(({ exploreCatalog }) => {
        if (!active) return;
        destroy = exploreCatalog(
          engine.catalog.coordinator,
          metadata,
          catalogFiltersSchema.parse(JSON.parse(key)),
          (result) => {
            if (active) setData(result);
          },
          (cause) => {
            if (active) setError(cause.message);
          },
        );
      })
      .catch((cause) => {
        if (active)
          setError(cause instanceof Error ? cause.message : "Could not query the catalog.");
      });
    return () => {
      active = false;
      destroy?.();
    };
  }, [engine, metadata, key, enabled]);

  return {
    data,
    pending: enabled && !!key && !error && (!engine || data?.key !== key),
    error,
    retry: () => setAttempt((value) => value + 1),
  };
}
