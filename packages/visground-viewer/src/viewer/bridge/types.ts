import type { ViewerRuntimeConfig, ViewerSelection, ViewerStatePayload } from "../contract/types";

export type ViewerBridgeSnapshot = {
  debug: boolean;
  runtimeConfig?: ViewerRuntimeConfig;
  selection: ViewerSelection;
  state: ViewerStatePayload;
};

export interface ViewerBridge {
  getSnapshot(): ViewerBridgeSnapshot;
  subscribe(listener: () => void): () => void;
  setSelection(selection: ViewerSelection): void | Promise<void>;
  destroy?(): void;
}
