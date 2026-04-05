import type { AnywidgetModelLike } from "./contract/types";
import type { ViewerBridge } from "./bridge/types";
interface ViewerMount {
  update(next: { bridge?: ViewerBridge; model?: AnywidgetModelLike }): void;
  destroy(): void;
}
export declare function mountVisgroundViewer(
  target: HTMLElement,
  options: {
    bridge: ViewerBridge;
  },
): ViewerMount;
export declare function mountAnywidgetVisgroundViewer(
  target: HTMLElement,
  options: {
    model: AnywidgetModelLike;
    artifactUrl: string;
  },
): ViewerMount;
export {};
//# sourceMappingURL=mount.d.ts.map
