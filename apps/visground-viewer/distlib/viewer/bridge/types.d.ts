import type { ViewerSelection, ViewerStatePayload } from "../contract/types";
export type ViewerBridgeSnapshot = {
  debug: boolean;
  selection: ViewerSelection;
  state: ViewerStatePayload;
};
export interface ViewerBridge {
  getSnapshot(): ViewerBridgeSnapshot;
  subscribe(listener: () => void): () => void;
  setSelection(selection: ViewerSelection): void | Promise<void>;
  destroy?(): void;
}
//# sourceMappingURL=types.d.ts.map
