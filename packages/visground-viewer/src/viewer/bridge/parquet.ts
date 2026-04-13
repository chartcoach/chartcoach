import type { ViewerRuntimeConfig, ViewerSelection, ViewerStatePayload } from "../contract/types";
import type { ViewerBridge, ViewerBridgeSnapshot } from "./types";
import { createViewerRuntime, deriveViewerState } from "../data/derive";
import { loadViewerArtifactFromParquetUrl, type ViewerArtifactRow } from "../data/parquet";

const EMPTY_SELECTION: ViewerSelection = {
  vis_id: "",
  filters: {},
  layout: {
    row_dimension: "",
    column_dimension: "",
    group_dimension: null,
  },
};

const EMPTY_STATE_PAYLOAD: ViewerStatePayload = {
  catalog: [],
  overview: null,
  error: null,
};

const EMPTY_SELECTION_REQUEST: Partial<ViewerSelection> = {};

function cloneJson<T>(value: T): T {
  return JSON.parse(JSON.stringify(value));
}

function isEqualJson(left: unknown, right: unknown): boolean {
  return JSON.stringify(left) === JSON.stringify(right);
}

export function createParquetViewerBridge({
  artifactUrl,
  runtimeConfig,
  initialDebug = false,
  initialSelection,
  getExternalSnapshot,
  onExternalChange,
  onSelectionChange,
  resolveImageUrl,
}: {
  artifactUrl: string;
  runtimeConfig: ViewerRuntimeConfig;
  initialDebug?: boolean;
  initialSelection?: ViewerSelection | null;
  getExternalSnapshot?: () => Partial<ViewerBridgeSnapshot> | null;
  onExternalChange?: (listener: () => void) => () => void;
  onSelectionChange?: (selection: ViewerSelection) => void | Promise<void>;
  resolveImageUrl?: (url: string | null) => string | null;
}): ViewerBridge {
  const listeners = new Set<() => void>();
  let records: ViewerArtifactRow[] | null = null;
  let runtime = null as ReturnType<typeof createViewerRuntime> | null;
  let currentRuntimeConfig = cloneJson(runtimeConfig);
  let disposeExternal: (() => void) | null = null;
  let pendingSelection = cloneJson(initialSelection ?? EMPTY_SELECTION_REQUEST);
  let snapshot: ViewerBridgeSnapshot = {
    debug: initialDebug,
    runtimeConfig: currentRuntimeConfig,
    selection: cloneJson(initialSelection ?? EMPTY_SELECTION),
    state: EMPTY_STATE_PAYLOAD,
  };

  const notify = () => {
    for (const listener of listeners) {
      listener();
    }
  };

  const applySelection = (requested: Partial<ViewerSelection>, syncHost: boolean) => {
    pendingSelection = {
      ...pendingSelection,
      ...requested,
      filters: requested.filters ?? pendingSelection.filters,
      layout: requested.layout ?? pendingSelection.layout,
    };

    if (!runtime) {
      snapshot = {
        ...snapshot,
        selection: {
          ...snapshot.selection,
          ...requested,
          filters: requested.filters ?? snapshot.selection.filters,
          layout: requested.layout ?? snapshot.selection.layout,
        },
      };
      notify();
      return;
    }

    const derived = deriveViewerState(runtime, {
      ...pendingSelection,
    });
    pendingSelection = derived.selection;
    snapshot = {
      ...snapshot,
      selection: derived.selection,
      state: derived.state,
    };
    if (syncHost) {
      void onSelectionChange?.(derived.selection);
    }
    notify();
  };

  const rebuildRuntime = () => {
    if (!records) {
      return false;
    }
    runtime = createViewerRuntime(records, currentRuntimeConfig);
    applySelection(snapshot.selection, false);
    return true;
  };

  const applyExternalSnapshot = () => {
    const external = getExternalSnapshot?.();
    if (!external) {
      return;
    }

    let didChange = false;

    if (typeof external.debug === "boolean" && external.debug !== snapshot.debug) {
      snapshot = { ...snapshot, debug: external.debug };
      didChange = true;
    }

    if (external.runtimeConfig && !isEqualJson(external.runtimeConfig, currentRuntimeConfig)) {
      currentRuntimeConfig = cloneJson(external.runtimeConfig);
      snapshot = { ...snapshot, runtimeConfig: currentRuntimeConfig };
      if (rebuildRuntime()) {
        return;
      }
      didChange = true;
    }

    if (external.selection) {
      applySelection(external.selection, false);
      return;
    }

    if (didChange) {
      notify();
    }
  };

  void (async () => {
    try {
      records = await loadViewerArtifactFromParquetUrl(artifactUrl, undefined, {
        resolveImageUrl,
      });
      runtime = createViewerRuntime(records, currentRuntimeConfig);
      applySelection(pendingSelection, true);
      applyExternalSnapshot();
    } catch (error) {
      snapshot = {
        ...snapshot,
        state: {
          catalog: [],
          overview: null,
          error: error instanceof Error ? error.message : String(error),
        },
      };
      notify();
    }
  })();

  if (onExternalChange) {
    disposeExternal = onExternalChange(() => {
      applyExternalSnapshot();
    });
  }

  return {
    getSnapshot() {
      return snapshot;
    },
    subscribe(listener) {
      listeners.add(listener);
      return () => {
        listeners.delete(listener);
      };
    },
    setSelection(selection) {
      applySelection(selection, true);
    },
    destroy() {
      listeners.clear();
      disposeExternal?.();
    },
  };
}
