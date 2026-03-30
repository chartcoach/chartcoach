import { startTransition, useEffect, useRef, useState } from "react";
import type {
  AnywidgetModelLike,
  ViewerActions,
  ViewerBusyState,
  ViewerController,
  ViewerLayoutSelection,
  ViewerSelection,
  ViewerState,
  ViewerStatePayload,
} from "@/viewer/contract/types";
import { getCatalogIndex, getCatalogSubset } from "@/viewer/controller/catalog";
import { HOVER_HIDE_DELAY_MS, positionHoverCard } from "@/viewer/controller/hover";
import { createRootKeydownHandler } from "@/viewer/controller/keyboard";
import { positionPopover } from "@/viewer/controller/popover";

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

function makeInitialState(model: AnywidgetModelLike): ViewerState {
  const selection = cloneJson(
    (model.get("_selection") as ViewerSelection | null) ?? EMPTY_SELECTION,
  );
  const payload = cloneJson(
    (model.get("_state") as ViewerStatePayload | null) ?? EMPTY_STATE_PAYLOAD,
  );
  const debug = Boolean(model.get("debug"));

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
    activePopoverId: null,
    popoverAnchor: null,
  };
}

export function useViewerController(model: AnywidgetModelLike): ViewerController {
  const stateRef = useRef<ViewerState>(makeInitialState(model));
  const hoverHideTimerRef = useRef<number | null>(null);
  const rootRef = useRef<HTMLDivElement | null>(null);
  const hoverCardRef = useRef<HTMLDivElement | null>(null);
  const popoverRef = useRef<HTMLDivElement | null>(null);
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

  function hydrateFromModel() {
    const nextSelection = cloneJson(
      (model.get("_selection") as ViewerSelection | null) ?? EMPTY_SELECTION,
    );
    const nextPayload = cloneJson(
      (model.get("_state") as ViewerStatePayload | null) ?? EMPTY_STATE_PAYLOAD,
    );
    const nextDebug = Boolean(model.get("debug"));

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
      activePopoverId: null,
      popoverAnchor: null,
    });
  }

  function commitSelection(nextSelection: ViewerSelection, busy: ViewerBusyState) {
    patch({
      selection: nextSelection,
      busy,
      error: null,
      hover: null,
      inspectCellKey: null,
      activePopoverId: null,
      popoverAnchor: null,
    });

    model.set("_selection", nextSelection);
    model.save_changes();
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
    togglePopover(popoverId, anchor) {
      const isOpen = stateRef.current.activePopoverId === popoverId;
      patch({
        activePopoverId: isOpen ? null : popoverId,
        popoverAnchor: isOpen ? null : anchor,
        inspectCellKey: isOpen ? stateRef.current.inspectCellKey : null,
        hover: isOpen ? stateRef.current.hover : null,
      });
    },
    closePopover() {
      patch({
        activePopoverId: null,
        popoverAnchor: null,
      });
    },
    openInspect(cellKey) {
      patch({
        inspectCellKey: cellKey,
        hover: null,
      });
    },
    closeInspect() {
      patch({
        inspectCellKey: null,
      });
    },
    showHover(cell, anchor) {
      if (hoverHideTimerRef.current) {
        window.clearTimeout(hoverHideTimerRef.current);
        hoverHideTimerRef.current = null;
      }
      patch({
        hover: {
          cell,
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

    function onModelSelectionChange() {
      hydrateFromModel();
    }

    function onModelStateChange() {
      hydrateFromModel();
    }

    function onModelDebugChange() {
      hydrateFromModel();
    }

    function onViewportChange() {
      const current = stateRef.current;
      if (current.hover?.anchor && hoverCardRef.current && current.hover.anchor.isConnected) {
        positionHoverCard(hoverCardRef.current, current.hover.anchor);
      }
      if (
        current.activePopoverId &&
        current.popoverAnchor &&
        rootRef.current &&
        popoverRef.current &&
        current.popoverAnchor.isConnected
      ) {
        positionPopover(rootRef.current, popoverRef.current, current.popoverAnchor);
      }
    }

    const onKeydown = createRootKeydownHandler(() => stateRef.current, actions);
    const root = rootRef.current;

    model.on("change:_selection", onModelSelectionChange);
    model.on("change:_state", onModelStateChange);
    model.on("change:debug", onModelDebugChange);
    window.addEventListener("resize", onViewportChange);
    window.addEventListener("scroll", onViewportChange, true);
    root?.addEventListener("keydown", onKeydown);

    hydrateFromModel();
    for (const delay of [50, 150, 350, 800, 1500, 3000]) {
      hydrationRetryTimers.push(
        window.setTimeout(() => {
          if (stateRef.current.overview || stateRef.current.error) {
            return;
          }
          hydrateFromModel();
        }, delay),
      );
    }

    return () => {
      model.off("change:_selection", onModelSelectionChange);
      model.off("change:_state", onModelStateChange);
      model.off("change:debug", onModelDebugChange);
      window.removeEventListener("resize", onViewportChange);
      window.removeEventListener("scroll", onViewportChange, true);
      root?.removeEventListener("keydown", onKeydown);
      for (const timer of hydrationRetryTimers) {
        window.clearTimeout(timer);
      }
    };
  }, [model]);

  useEffect(() => {
    if (state.hover?.anchor && hoverCardRef.current && state.hover.anchor.isConnected) {
      positionHoverCard(hoverCardRef.current, state.hover.anchor);
    }
  }, [state.hover]);

  useEffect(() => {
    if (
      state.activePopoverId &&
      state.popoverAnchor &&
      rootRef.current &&
      popoverRef.current &&
      state.popoverAnchor.isConnected
    ) {
      positionPopover(rootRef.current, popoverRef.current, state.popoverAnchor);
    }
  }, [state.activePopoverId, state.popoverAnchor]);

  return {
    state,
    refs: {
      rootRef,
      hoverCardRef,
      popoverRef,
    },
    actions,
  };
}
