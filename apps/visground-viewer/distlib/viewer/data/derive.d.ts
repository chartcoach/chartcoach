import type { ViewerSelection, ViewerStatePayload } from "../contract/types";
import type { ViewerArtifactRow } from "./parquet";
type Registry = {
  visIds: string[];
  dimensionValues: Record<string, Array<string | null>>;
};
type RuntimeContext = {
  records: ViewerArtifactRow[];
  registry: Registry;
  catalog: ViewerStatePayload["catalog"];
};
export declare function createViewerRuntime(records: ViewerArtifactRow[]): RuntimeContext;
export declare function deriveViewerState(
  runtime: RuntimeContext,
  requested: Partial<ViewerSelection> | null | undefined,
): {
  selection: ViewerSelection;
  state: ViewerStatePayload;
};
export {};
//# sourceMappingURL=derive.d.ts.map
