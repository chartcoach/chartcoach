import {
  FloatingFocusManager,
  autoUpdate,
  flip,
  offset,
  shift,
  useDismiss,
  useFloating,
  useInteractions,
} from "@floating-ui/react";
import { useEffect } from "react";
import type { ViewerActions, ViewerState } from "@/viewer/contract/types";
import { CasePopover } from "@/viewer/render/case-popover";
import { FiltersPopover } from "@/viewer/render/filters-popover";
import { LayoutPopover } from "@/viewer/render/layout-popover";

export function PopoverLayer({
  state,
  actions,
  anchor,
}: {
  state: ViewerState;
  actions: ViewerActions;
  anchor: HTMLElement | null;
}) {
  const isOpen = Boolean(state.overview && state.activePopoverId && anchor);
  const { refs, floatingStyles, context } = useFloating({
    open: isOpen,
    onOpenChange(nextOpen) {
      if (!nextOpen) {
        actions.closePopover();
      }
    },
    placement: "bottom-start",
    strategy: "fixed",
    whileElementsMounted: autoUpdate,
    middleware: [offset(10), flip({ padding: 12 }), shift({ padding: 12 })],
  });
  const dismiss = useDismiss(context);
  const { getFloatingProps } = useInteractions([dismiss]);

  useEffect(() => {
    refs.setReference(anchor);
  }, [anchor, refs]);

  if (!state.overview || !isOpen) {
    return null;
  }

  return (
    <FloatingFocusManager context={context} modal={false} returnFocus>
      <div
        className="vg-pill-popover"
        ref={refs.setFloating}
        style={floatingStyles}
        {...getFloatingProps()}
      >
        <div className="vg-pill-popover-card">
          <CasePopover actions={actions} state={state} />
          <FiltersPopover actions={actions} state={state} />
          <LayoutPopover actions={actions} state={state} />
        </div>
      </div>
    </FloatingFocusManager>
  );
}
