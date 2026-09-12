import { startTransition, useEffect, useState } from "react";
import type { Coordinator } from "@uwdata/mosaic-core";
import type { ExplorerData } from "../browser/explorer";
import { catalogMatches, type CatalogMatch } from "../browser/catalog-matches";

export function useCatalogMatches(
  coordinator: Coordinator | undefined,
  selection: ExplorerData | undefined,
  enabled = true,
) {
  const scope = selection?.selection;
  const selectionKey = scope ? JSON.stringify(scope) : "";
  const [position, setPosition] = useState({ key: "", batch: 0 });
  const batch = position.key === selectionKey ? position.batch : 0;

  const [data, setData] = useState<{
    key: string;
    batch: number;
    total: number;
    matches: CatalogMatch[];
  }>();

  const [error, setError] = useState<string>();
  const [attempt, setAttempt] = useState(0);
  const total = selection?.matchedGuidelines;

  useEffect(() => {
    if (!enabled || !coordinator || !scope || total === undefined) return;
    let active = true;
    setError(undefined);
    void catalogMatches(coordinator, scope, batch)
      .then((matches) => {
        if (!active) return;
        startTransition(() =>
          setData((current) => {
            if (!active) return current;

            if (batch === 0) return { key: selectionKey, batch, total, matches };

            if (current?.key !== selectionKey || current.batch !== batch - 1) return current;

            return { key: selectionKey, batch, total, matches: [...current.matches, ...matches] };
          }),
        );
      })
      .catch(() => {
        if (active) setError("Could not load matching guidelines. Try again.");
      });

    return () => {
      active = false;
    };
  }, [coordinator, scope, batch, selectionKey, total, attempt, enabled]);

  const pending =
    enabled && !!selection && !error && (data?.key !== selectionKey || data?.batch !== batch);

  return {
    data: coordinator && selection ? data : undefined,
    pending,
    error: enabled ? error : undefined,
    loadMore: () => {
      if (
        !enabled ||
        pending ||
        error ||
        data?.key !== selectionKey ||
        data.matches.length >= data.total
      )
        return;
      setPosition({ key: selectionKey, batch: data.batch + 1 });
    },
    retry: () => setAttempt((value) => value + 1),
  };
}
