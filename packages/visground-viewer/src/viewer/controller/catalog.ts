import type { CatalogEntry, ViewerState } from "@/viewer/contract/types";

export function getCatalogSubset(
  state: Pick<ViewerState, "catalog" | "searchTerm">,
  { searchTerm = "" }: { searchTerm?: string } = {},
): CatalogEntry[] {
  const needle = searchTerm.trim().toLowerCase();
  return state.catalog.filter((entry) => {
    if (!needle) {
      return true;
    }
    return (
      entry.vis_id.toLowerCase().includes(needle) ||
      entry.label.toLowerCase().includes(needle) ||
      entry.search_text.toLowerCase().includes(needle)
    );
  });
}

export function getCatalogIndex(entries: Pick<CatalogEntry, "vis_id">[], visId: string): number {
  return entries.findIndex((entry) => entry.vis_id === visId);
}
