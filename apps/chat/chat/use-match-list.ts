import { useRef, useState } from "react";
import type { VListHandle } from "virtua";
import type { useCatalogExplorer } from "./use-catalog-explorer";
import { useCatalogMatches } from "./use-catalog-matches";

export function useMatchList(explorer: ReturnType<typeof useCatalogExplorer>, disabled: boolean) {
  const matches = useCatalogMatches(
    explorer.coordinator,
    explorer.data,
    !explorer.pending && !explorer.error,
  );

  const list = useRef<VListHandle>(null);
  const [focused, setFocused] = useState<{ key: string; index: number }>();
  const data = matches.data;

  return {
    data,
    list,
    pending: explorer.pending || matches.pending,
    error: explorer.error ?? matches.error,
    retry: explorer.error ? undefined : matches.retry,
    total: data?.total ?? 0,
    keepMounted: focused && focused.key === data?.key ? [focused.index] : undefined,
    focus: (index: number) => {
      if (data) setFocused({ key: data.key, index });
    },
    blur: () => setFocused(undefined),
    scroll: () => {
      const viewport = list.current;

      if (
        !disabled &&
        viewport &&
        viewport.scrollSize - viewport.scrollOffset < 2 * viewport.viewportSize
      )
        matches.loadMore();
    },
  };
}
