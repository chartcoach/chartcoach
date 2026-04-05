import type { ViewerSelection, ViewerStatePayload } from "../contract/types";
import type { ViewerBridge, ViewerBridgeSnapshot } from "./types";
import { createViewerRuntime, deriveViewerState } from "../data/derive";
import { loadViewerArtifactFromParquetUrl } from "../data/parquet";

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

function cloneJson<T>(value: T): T {
  return JSON.parse(JSON.stringify(value));
}

export function createParquetViewerBridge({
  artifactUrl,
  initialDebug = false,
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
}): ViewerBridge {
  const listeners = new Set<() => void>();
  let runtime = null as ReturnType<typeof createViewerRuntime> | null;
  let disposeExternal: (() => void) | null = null;
  let snapshot: ViewerBridgeSnapshot = {
    debug: initialDebug,
    selection: cloneJson(initialSelection ?? EMPTY_SELECTION),
    state: EMPTY_STATE_PAYLOAD,
  };

  const notify = () => {
    for (const listener of listeners) {
      listener();
    }
  };

  const applyExternalSnapshot = () => {
    const external = getExternalSnapshot?.();
    if (!external) return;
    if (typeof external.debug === "boolean" && external.debug !== snapshot.debug) {
      snapshot = { ...snapshot, debug: external.debug };
    }
    if (external.selection) {
      applySelection(external.selection, false);
      return;
    }
    notify();
  };

  const applySelection = (requested: Partial<ViewerSelection>, syncHost: boolean) => {
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
      ...snapshot.selection,
      ...requested,
      filters: requested.filters ?? snapshot.selection.filters,
      layout: requested.layout ?? snapshot.selection.layout,
    });
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

  void (async () => {
    try {
      const records = await loadViewerArtifactFromParquetUrl(artifactUrl, undefined, {
        resolveImageUrl,
      });
      runtime = createViewerRuntime(records);
      applySelection(snapshot.selection, true);
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
