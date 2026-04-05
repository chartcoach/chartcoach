import type { CatalogEntry, ViewerState } from "../contract/types";
export declare function getCatalogSubset(
  state: Pick<ViewerState, "catalog" | "searchTerm">,
  {
    searchTerm,
  }?: {
    searchTerm?: string;
  },
): CatalogEntry[];
export declare function getCatalogIndex(
  entries: Pick<CatalogEntry, "vis_id">[],
  visId: string,
): number;
//# sourceMappingURL=catalog.d.ts.map
