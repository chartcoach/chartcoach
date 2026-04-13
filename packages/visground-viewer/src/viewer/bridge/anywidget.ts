import type { AnywidgetModelLike } from "../contract/types";
import type { ViewerBridge } from "./types";
import { createParquetViewerBridge } from "./parquet";
import { parseViewerRuntimeConfig } from "../data/runtime-config";

function cloneJson<T>(value: T): T {
  return JSON.parse(JSON.stringify(value));
}

function resolveRuntimeConfig(model: AnywidgetModelLike) {
  return parseViewerRuntimeConfig(model.get("_viewer_config"));
}

export function createAnywidgetViewerBridge(
  model: AnywidgetModelLike,
  artifactUrl: string,
): ViewerBridge {
  return createParquetViewerBridge({
    artifactUrl,
    runtimeConfig: resolveRuntimeConfig(model),
    initialDebug: Boolean(model.get("debug")),
    initialSelection: cloneJson(model.get("_selection") as object | null) as never,
    getExternalSnapshot() {
      return {
        debug: Boolean(model.get("debug")),
        runtimeConfig: resolveRuntimeConfig(model),
        selection: cloneJson(model.get("_selection") as object | null) as never,
      };
    },
    onExternalChange(listener) {
      model.on("change:_selection", listener);
      model.on("change:_viewer_config", listener);
      model.on("change:debug", listener);
      return () => {
        model.off("change:_selection", listener);
        model.off("change:_viewer_config", listener);
        model.off("change:debug", listener);
      };
    },
    onSelectionChange(selection) {
      model.set("_selection", selection);
      model.save_changes();
    },
  });
}
