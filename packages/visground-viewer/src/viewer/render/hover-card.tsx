import type { ViewerActions, ViewerRefs, ViewerState } from "@/viewer/contract/types";
import { ScoreBreakdownList } from "@/viewer/render/score-ledger";
import { getVariantByIndex, orientationLabel } from "@/viewer/render/utils";

export function HoverCard({
  state,
  actions,
  refs,
}: {
  state: ViewerState;
  actions: ViewerActions;
  refs: ViewerRefs;
}) {
  if (!state.hover) {
    return <div className="vg-hovercard" hidden ref={refs.hoverCardRef} />;
  }

  const variant = getVariantByIndex(state.hover.cell, state.hover.variantIndex);
  if (!variant) {
    return <div className="vg-hovercard" hidden ref={refs.hoverCardRef} />;
  }
  const candidate = variant.candidate;
  const label = orientationLabel([
    state.hover.cell.group_label,
    state.hover.cell.row_label,
    state.hover.cell.column_label,
  ]);

  return (
    <aside
      className="vg-hovercard"
      onMouseEnter={() => actions.cancelHoverHide()}
      onMouseLeave={() => actions.scheduleHoverHide()}
      ref={refs.hoverCardRef}
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
