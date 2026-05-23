import type { ViewerRuntimeConfig, ViewerSelection, ViewerStatePayload } from "../contract/types";
import type { ViewerBridge, ViewerBridgeSnapshot } from "./types";
import { createViewerRuntime, deriveViewerState } from "../data/derive";
import {
  loadViewerArtifactRowsFromParquetUrl,
  normalizeViewerArtifactRows,
  type ParquetLoaderDependencies,
  type ViewerArtifactRow,
  type ViewerArtifactRowWire,
} from "../data/parquet";

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

function mergeSelection(
  base: Partial<ViewerSelection>,
  requested: Partial<ViewerSelection>,
): Partial<ViewerSelection> {
  return {
    ...base,
    ...requested,
    filters: requested.filters ?? base.filters,
    layout: requested.layout ?? base.layout,
  };
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
  dependencies,
}: {
  artifactUrl: string;
  runtimeConfig: ViewerRuntimeConfig;
  initialDebug?: boolean;
  initialSelection?: ViewerSelection | null;
  getExternalSnapshot?: () => Partial<ViewerBridgeSnapshot> | null;
  onExternalChange?: (listener: () => void) => () => void;
  onSelectionChange?: (selection: ViewerSelection) => void | Promise<void>;
  resolveImageUrl?: (url: string | null) => string | null;
  dependencies?: Partial<ParquetLoaderDependencies>;
}): ViewerBridge {
  const listeners = new Set<() => void>();
  let rawRows: ViewerArtifactRowWire[] | null = null;
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

  const commitSelection = (
    requested: Partial<ViewerSelection>,
    syncHost: boolean,
    shouldNotify: boolean,
  ) => {
    pendingSelection = mergeSelection(pendingSelection, requested);
    if (!runtime) {
      snapshot = {
        ...snapshot,
        selection: mergeSelection(snapshot.selection, requested) as ViewerSelection,
      };
      if (shouldNotify) notify();
      return;
    }

    const derived = deriveViewerState(runtime, pendingSelection);
    pendingSelection = derived.selection;
    snapshot = {
      ...snapshot,
      selection: derived.selection,
      state: derived.state,
    };
    if (syncHost) {
      void onSelectionChange?.(derived.selection);
    }
    if (shouldNotify) notify();
  };

  const applySelection = (requested: Partial<ViewerSelection>, syncHost: boolean) => {
    commitSelection(requested, syncHost, true);
  };

  const buildRuntime = (rows: ViewerArtifactRowWire[], config: ViewerRuntimeConfig) => {
    const nextRecords = normalizeViewerArtifactRows(rows, {
      runtimeConfig: config,
      resolveImageUrl,
    });
    return {
      records: nextRecords,
      runtime: createViewerRuntime(nextRecords, config),
    };
  };

  const applyExternalSnapshot = () => {
    const external = getExternalSnapshot?.();
    if (!external) {
      return;
    }

    let didChange = false;
    const nextDebug = typeof external.debug === "boolean" ? external.debug : snapshot.debug;
    const nextRuntimeConfig = external.runtimeConfig
      ? cloneJson(external.runtimeConfig)
      : currentRuntimeConfig;
    const runtimeConfigChanged = !isEqualJson(nextRuntimeConfig, currentRuntimeConfig);
    const selectionChanged = Boolean(external.selection);
    const nextSelection = external.selection
      ? mergeSelection(pendingSelection, external.selection)
      : pendingSelection;

    let nextRecords = records;
    let nextRuntime = runtime;
    let nextSnapshotSelection = snapshot.selection;
    let nextState = snapshot.state;

    try {
      if (runtimeConfigChanged && rawRows) {
        const built = buildRuntime(rawRows, nextRuntimeConfig);
        nextRecords = built.records;
        nextRuntime = built.runtime;
      }

      if (runtimeConfigChanged || selectionChanged) {
        if (nextRuntime) {
          const derived = deriveViewerState(nextRuntime, nextSelection);
          nextSnapshotSelection = derived.selection;
          nextState = derived.state;
        } else if (external.selection) {
          nextSnapshotSelection = mergeSelection(
            snapshot.selection,
            external.selection,
          ) as ViewerSelection;
        }
      }
    } catch (error) {
      snapshot = {
        ...snapshot,
        debug: nextDebug,
        state: {
          catalog: [],
          overview: null,
          error: error instanceof Error ? error.message : String(error),
        },
      };
      notify();
      return;
    }

    if (nextDebug !== snapshot.debug || runtimeConfigChanged || selectionChanged) {
      didChange = true;
    }

    if (runtimeConfigChanged) {
      currentRuntimeConfig = nextRuntimeConfig;
      records = nextRecords;
      runtime = nextRuntime;
    }

    if (runtimeConfigChanged || selectionChanged) {
      pendingSelection = nextRuntime ? nextSnapshotSelection : nextSelection;
    }

    if (didChange) {
      snapshot = {
        ...snapshot,
        debug: nextDebug,
        runtimeConfig: currentRuntimeConfig,
        selection: nextSnapshotSelection,
        state: nextState,
      };
      notify();
    }
  };

  void (async () => {
    try {
      rawRows = await loadViewerArtifactRowsFromParquetUrl(artifactUrl, undefined, dependencies);
      const built = buildRuntime(rawRows, currentRuntimeConfig);
      records = built.records;
      runtime = built.runtime;
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
