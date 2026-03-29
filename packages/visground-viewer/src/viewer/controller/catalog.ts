import type { CatalogEntry, ViewerState } from "@/viewer/contract/types";

export function getCatalogSubset(
  state: Pick<ViewerState, "catalog" | "searchTerm" | "selection">,
  {
    requestChart = state.selection.request_chart,
    searchTerm = "",
  }: { requestChart?: string | null; searchTerm?: string } = {},
): CatalogEntry[] {
  const needle = searchTerm.trim().toLowerCase();
  return state.catalog.filter((entry) => {
    const chartMatches = requestChart == null || entry.request_chart === requestChart;
    const searchMatches =
      !needle ||
      entry.vis_id.toLowerCase().includes(needle) ||
      entry.nl_query.toLowerCase().includes(needle);
    return chartMatches && searchMatches;
  });
}

export function getCatalogIndex(entries: Pick<CatalogEntry, "vis_id">[], visId: string): number {
  return entries.findIndex((entry) => entry.vis_id === visId);
}
