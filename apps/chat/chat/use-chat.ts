import { useCatalogFilters, type CatalogFilterSelection } from "./use-catalog-filters";
import { useChatRuntime } from "./use-chat-runtime";

export function useChat() {
  const catalog = useCatalogFilters();
  const state = useChatRuntime(catalog.selection);
  async function onFiltersChange(selection: CatalogFilterSelection) {
    if (
      catalog.selection &&
      JSON.stringify(selection.filters) === JSON.stringify(catalog.selection.filters)
    )
      return;
    await state.restartKeepingChart();
    catalog.setSelection(selection);
  }
  async function onCatalogReload() {
    await state.restartKeepingChart();
    catalog.reload();
  }
  return { ...state, catalog, onFiltersChange, onCatalogReload };
}
