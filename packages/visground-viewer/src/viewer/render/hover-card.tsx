import type { ViewerActions, ViewerRefs, ViewerState } from "@/viewer/contract/types";
import { ScoreLedger } from "@/viewer/render/score-ledger";
import { orientationLabel, renderImage } from "@/viewer/render/utils";

export function HoverCard({
  state,
  actions,
  refs,
}: {
  state: ViewerState;
  actions: ViewerActions;
  refs: ViewerRefs;
}) {
  if (!state.hover || !state.hover.cell?.candidate) {
    return <div className="vg-hovercard" hidden ref={refs.hoverCardRef} />;
  }

  const candidate = state.hover.cell.candidate;
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
      <div className="vg-hover-image">
        <div className="vg-chart-canvas is-hover">
          {candidate.error ? (
            <p className="vg-error">{candidate.error}</p>
          ) : (
            renderImage(candidate.image_url || null, label, candidate.image_meta || null, "hover")
          )}
        </div>
      </div>
      <div className="vg-hover-footer">
        <div className="vg-hover-orientation">{label}</div>
        <ScoreLedger candidate={candidate} mode="floating" />
      </div>
    </aside>
  );
}
