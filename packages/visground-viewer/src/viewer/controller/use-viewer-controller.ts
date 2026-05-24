import { startTransition, useEffect, useRef, useState } from "react";
import type {
  ViewerActions,
  ViewerBusyState,
  ViewerController,
  ViewerLayoutSelection,
  ViewerSelection,
  ViewerState,
  ViewerStatePayload,
} from "../contract/types";
import type { ViewerBridge } from "../bridge/types";
import { getCatalogIndex, getCatalogSubset } from "./catalog";
import { createRootKeydownHandler } from "./keyboard";

const HOVER_HIDE_DELAY_MS = 220;

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

function isEqualJson(left: unknown, right: unknown): boolean {
  return JSON.stringify(left) === JSON.stringify(right);
}

function makeInitialState(bridge: ViewerBridge): ViewerState {
  const snapshot = bridge.getSnapshot();
  const selection = cloneJson(snapshot.selection ?? EMPTY_SELECTION);
  const payload = cloneJson(snapshot.state ?? EMPTY_STATE_PAYLOAD);
  const debug = snapshot.debug;

  return {
    catalog: payload.catalog,
    debug,
    selection,
    overview: payload.overview,
    searchTerm: "",
    busy: payload.overview ? null : "initial",
    error: payload.error,
    hover: null,
    inspectCellKey: null,
    inspectVariantIndex: 0,
    activePopoverId: null,
  };
}

export function useViewerController(bridge: ViewerBridge): ViewerController {
  const stateRef = useRef<ViewerState>(makeInitialState(bridge));
  const hoverHideTimerRef = useRef<number | null>(null);
  const rootRef = useRef<HTMLDivElement | null>(null);
  const [state, setState] = useState<ViewerState>(stateRef.current);

  function sync(next: ViewerState) {
    stateRef.current = next;
    startTransition(() => {
      setState(next);
    });
  }

  function patch(partial: Partial<ViewerState>) {
    sync({
      ...stateRef.current,
      ...partial,
    });
  }

  function loadFromBridge() {
    const snapshot = bridge.getSnapshot();
    const nextSelection = cloneJson(snapshot.selection ?? EMPTY_SELECTION);
    const nextPayload = cloneJson(snapshot.state ?? EMPTY_STATE_PAYLOAD);
    const nextDebug = snapshot.debug;

    if (
      nextDebug === stateRef.current.debug &&
      isEqualJson(nextSelection, stateRef.current.selection) &&
      isEqualJson(nextPayload.catalog, stateRef.current.catalog) &&
      isEqualJson(nextPayload.overview, stateRef.current.overview) &&
      nextPayload.error === stateRef.current.error
    ) {
      return;
    }

    patch({
      catalog: nextPayload.catalog,
      debug: nextDebug,
      selection: nextSelection,
      overview: nextPayload.overview,
      busy: nextPayload.overview || nextPayload.error ? null : stateRef.current.busy,
      error: nextPayload.error,
      hover: null,
      inspectCellKey: null,
      inspectVariantIndex: 0,
      activePopoverId: null,
    });
  }

  function commitSelection(nextSelection: ViewerSelection, busy: ViewerBusyState) {
    patch({
      selection: nextSelection,
      busy,
      error: null,
      hover: null,
      inspectCellKey: null,
      inspectVariantIndex: 0,
      activePopoverId: null,
    });

    void bridge.setSelection(nextSelection);
  }

  const actions: ViewerActions = {
    stepCase(delta) {
      const filteredCatalog = getCatalogSubset(stateRef.current, {
        searchTerm: stateRef.current.searchTerm,
      });
      const currentIndex = getCatalogIndex(filteredCatalog, stateRef.current.selection.vis_id);
      const nextEntry =
        currentIndex >= 0 ? filteredCatalog[currentIndex + delta] : filteredCatalog[0];
      if (!nextEntry) {
        return;
      }
      commitSelection(
        {
          ...stateRef.current.selection,
          vis_id: nextEntry.vis_id,
        },
        "case",
      );
    },
    jumpToCase(visId) {
      if (!visId) {
        return;
      }
      commitSelection(
        {
          ...stateRef.current.selection,
          vis_id: visId,
        },
        "case",
      );
    },
    changeFilter(filterId, value) {
      commitSelection(
        {
          ...stateRef.current.selection,
          filters: {
            ...stateRef.current.selection.filters,
            [filterId]: value,
          },
        },
        "update",
      );
    },
    changeLayout(controlId, value) {
      const nextLayout: ViewerLayoutSelection = {
        ...stateRef.current.selection.layout,
        [controlId]: value,
      };
      commitSelection(
        {
          ...stateRef.current.selection,
          layout: nextLayout,
        },
        "update",
      );
    },
    togglePopover(popoverId) {
      const isOpen = stateRef.current.activePopoverId === popoverId;
      patch({
        activePopoverId: isOpen ? null : popoverId,
        inspectCellKey: isOpen ? stateRef.current.inspectCellKey : null,
        inspectVariantIndex: isOpen ? stateRef.current.inspectVariantIndex : 0,
        hover: isOpen ? stateRef.current.hover : null,
      });
    },
    closePopover() {
      patch({
        activePopoverId: null,
      });
    },
    openInspect(cellKey, variantIndex = 0) {
      patch({
        inspectCellKey: cellKey,
        inspectVariantIndex: variantIndex,
        hover: null,
      });
    },
    closeInspect() {
      patch({
        inspectCellKey: null,
        inspectVariantIndex: 0,
      });
    },
    showHover(cell, variantIndex, anchor) {
      if (hoverHideTimerRef.current) {
        window.clearTimeout(hoverHideTimerRef.current);
        hoverHideTimerRef.current = null;
      }
      patch({
        hover: {
          cell,
          variantIndex,
          anchor,
        },
      });
    },
    scheduleHoverHide() {
      if (hoverHideTimerRef.current) {
        window.clearTimeout(hoverHideTimerRef.current);
      }
      hoverHideTimerRef.current = window.setTimeout(() => {
        patch({
          hover: null,
        });
        hoverHideTimerRef.current = null;
      }, HOVER_HIDE_DELAY_MS);
    },
    cancelHoverHide() {
      if (hoverHideTimerRef.current) {
        window.clearTimeout(hoverHideTimerRef.current);
        hoverHideTimerRef.current = null;
      }
    },
    hideHover(immediate = true) {
      if (hoverHideTimerRef.current) {
        window.clearTimeout(hoverHideTimerRef.current);
        hoverHideTimerRef.current = null;
      }
      if (immediate) {
        patch({
          hover: null,
        });
        return;
      }
      actions.scheduleHoverHide();
    },
    updateSearchTerm(value) {
      patch({
        searchTerm: value,
      });
    },
  };

  useEffect(() => {
    const hydrationRetryTimers: number[] = [];

    const onKeydown = createRootKeydownHandler(() => stateRef.current, actions);
    const root = rootRef.current;
    const unsubscribe = bridge.subscribe(() => {
      loadFromBridge();
    });
    root?.addEventListener("keydown", onKeydown);

    loadFromBridge();
    for (const delay of [50, 150, 350, 800, 1500, 3000]) {
      hydrationRetryTimers.push(
        window.setTimeout(() => {
          if (stateRef.current.overview || stateRef.current.error) {
            return;
          }
          loadFromBridge();
        }, delay),
      );
    }

    return () => {
      unsubscribe();
      bridge.destroy?.();
      root?.removeEventListener("keydown", onKeydown);
      for (const timer of hydrationRetryTimers) {
        window.clearTimeout(timer);
      }
    };
  }, [bridge]);

  return {
    state,
    refs: {
      rootRef,
    },
    actions,
  };
}
