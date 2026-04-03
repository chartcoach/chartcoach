import { autoUpdate, flip, offset, shift, useFloating } from "@floating-ui/react";
import type { ViewerActions, ViewerState } from "@/viewer/contract/types";
import { ScoreBreakdownList } from "@/viewer/render/score-ledger";
import { getVariantByIndex, orientationLabel } from "@/viewer/render/utils";

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
      className="vg-hovercard"
      onMouseEnter={() => actions.cancelHoverHide()}
      onMouseLeave={() => actions.scheduleHoverHide()}
      ref={refs.setFloating}
      style={floatingStyles}
    >
      <div className="vg-hover-footer">
        <div className="vg-hover-orientation">{label}</div>
        {variant.variant_label ? (
          <div className="vg-hover-variant">{variant.variant_label}</div>
        ) : null}
        <ScoreBreakdownList candidate={candidate} mode="compact" />
      </div>
    </aside>
  );
}
