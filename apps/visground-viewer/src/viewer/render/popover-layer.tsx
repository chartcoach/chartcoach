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
import type { ViewerActions, ViewerState } from "../contract/types";
import { CasePopover } from "./case-popover";
import { FiltersPopover } from "./filters-popover";
import { LayoutPopover } from "./layout-popover";

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
        className="z-[31] w-[min(23rem,calc(100%-1rem))] max-w-[calc(100vw-1rem)]"
        ref={refs.setFloating}
        style={floatingStyles}
        {...getFloatingProps()}
      >
        <div className="grid gap-3 rounded-[4px] border border-border bg-background px-4 py-4 shadow-[var(--ccui-shadow)]">
          <CasePopover actions={actions} state={state} />
          <FiltersPopover actions={actions} state={state} />
          <LayoutPopover actions={actions} state={state} />
        </div>
      </div>
    </FloatingFocusManager>
  );
}
