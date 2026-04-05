import { autoUpdate, flip, offset, shift, useFloating } from "@floating-ui/react";
import type { ViewerActions, ViewerState } from "../contract/types";
import { ScoreBreakdownList } from "./score-ledger";
import { getVariantByIndex, orientationLabel } from "./utils";

export function HoverCard({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  if (!state.hover) {
    return null;
  }

  const variant = getVariantByIndex(state.hover.cell, state.hover.variantIndex);
  if (!variant || !state.hover.anchor.isConnected) {
    return null;
  }
  const candidate = variant.candidate;
  const label = orientationLabel([
    state.hover.cell.group_label,
    state.hover.cell.row_label,
    state.hover.cell.column_label,
  ]);
  const { refs, floatingStyles } = useFloating({
    elements: {
      reference: state.hover.anchor,
    },
    open: true,
    placement: "right",
    strategy: "fixed",
    whileElementsMounted: autoUpdate,
    middleware: [offset(24), flip({ padding: 24 }), shift({ padding: 24 })],
  });

  return (
    <aside
      className="fixed z-[60] grid w-[clamp(17rem,22vw,19rem)] max-h-[min(72vh,34rem)] gap-2 overflow-hidden border border-border bg-background px-3 py-3 shadow-[var(--ccui-shadow)] max-[860px]:w-[min(19rem,calc(100vw-1.25rem))]"
      onMouseEnter={() => actions.cancelHoverHide()}
      onMouseLeave={() => actions.scheduleHoverHide()}
      ref={refs.setFloating}
      style={floatingStyles}
    >
      <div className="grid gap-2">
        <div className="font-mono text-[0.76rem] font-semibold lowercase text-foreground">
          {label}
        </div>
        {variant.variant_label ? (
          <div className="font-mono text-[0.66rem] leading-[1.18] text-muted-foreground">
            {variant.variant_label}
          </div>
        ) : null}
        <ScoreBreakdownList candidate={candidate} mode="compact" />
      </div>
    </aside>
  );
}
