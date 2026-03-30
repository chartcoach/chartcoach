import type { ViewerActions, ViewerState } from "@/viewer/contract/types";
import { getCellByKey, orientationLabel, renderImage } from "@/viewer/render/utils";
import { ScoreLedger } from "@/viewer/render/score-ledger";

export function DetailDrawer({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const cell = getCellByKey(state.overview, state.inspectCellKey);
  const candidate = cell?.candidate;
  if (!cell || !candidate) {
    return <section className="vg-detail-section" hidden />;
  }

  const labelParts = [cell.group_label, cell.row_label, cell.column_label].filter(
    (part): part is string => Boolean(part),
  );
  const label = orientationLabel(labelParts);

  return (
    <section className="vg-detail-section is-open">
      <button className="vg-detail-scrim" onClick={() => actions.closeInspect()} type="button" />
      <aside className="vg-detail-drawer">
        <div className="vg-detail-drawer-head">
          <div className="vg-detail-head-copy">
            <div className="vg-detail-selection">
              {labelParts.map((part) => (
                <span className="vg-detail-selection-part" key={part}>
                  {part}
                </span>
              ))}
            </div>
          </div>
          <button
            aria-label="Close"
            className="vg-nav-button vg-detail-close"
            onClick={() => actions.closeInspect()}
            title="Close"
            type="button"
          >
            ×
          </button>
        </div>
        <div className="vg-detail-drawer-body">
          <section className="vg-detail-block">
            <div className="vg-detail-image-frame">
              <div className="vg-chart-canvas is-detail">
                {candidate.error ? (
                  <p className="vg-error">{candidate.error}</p>
                ) : (
                  renderImage(
                    candidate.image_url || null,
                    label,
                    candidate.image_meta || null,
                    "detail",
                  )
                )}
              </div>
            </div>
            <ScoreLedger candidate={candidate} mode="floating" />
            <div className="vg-detail-facts">
              {candidate.guideline_count > 0 ? (
                <span className="vg-detail-fact">
                  {`${candidate.guideline_count} ${candidate.guideline_count === 1 ? "guideline" : "guidelines"}`}
                </span>
              ) : null}
            </div>
          </section>
        </div>
      </aside>
    </section>
  );
}
