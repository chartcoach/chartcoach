import { useCatalogFilters, type CatalogFilterSelection } from "./use-catalog-filters";
import { useChatRuntime } from "./use-chat-runtime";
import type { useWorkspace } from "./use-workspace";
import { useState } from "react";

export function useChat(workspace: ReturnType<typeof useWorkspace>) {
  const catalog = useCatalogFilters(workspace.active?.knowledge);
  const state = useChatRuntime(catalog.selection, workspace);
  const [configuring, setConfiguring] = useState(false);

  async function onFiltersChange(selection: CatalogFilterSelection) {
    if (
      catalog.selection &&
      JSON.stringify(selection.filters) === JSON.stringify(catalog.selection.filters)
    )
      return;
    setConfiguring(true);

    try {
      await state.restartKeepingChart();
      catalog.setSelection(selection);
    } finally {
      setConfiguring(false);
    }
  }

  async function onCatalogReload() {
    setConfiguring(true);

    try {
      await state.restartKeepingChart();
      catalog.reload();
    } finally {
      setConfiguring(false);
    }
  }

  return {
    ...state,
    disabled: state.disabled || configuring,
    catalog,
    onFiltersChange,
    onCatalogReload,
    workspace,
  };
}
