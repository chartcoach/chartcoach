import type { ViewerSelection } from "../contract/types";
import type { ViewerBridge, ViewerBridgeSnapshot } from "./types";
export declare function createParquetViewerBridge({
  artifactUrl,
  initialDebug,
  initialSelection,
  getExternalSnapshot,
  onExternalChange,
  onSelectionChange,
  resolveImageUrl,
}: {
  artifactUrl: string;
  initialDebug?: boolean;
  initialSelection?: ViewerSelection | null;
  getExternalSnapshot?: () => Partial<ViewerBridgeSnapshot> | null;
  onExternalChange?: (listener: () => void) => () => void;
  onSelectionChange?: (selection: ViewerSelection) => void | Promise<void>;
  resolveImageUrl?: (url: string | null) => string | null;
}): ViewerBridge;
//# sourceMappingURL=parquet.d.ts.map
