import clsx from "clsx";
import { MessageSquareText } from "lucide-react";
import type { ViewerActions, ViewerState } from "@/viewer/contract/types";
import {
  getCellByKey,
  getVariantByIndex,
  orientationLabel,
  renderImage,
} from "@/viewer/render/utils";
import { ScoreBreakdownList } from "@/viewer/render/score-ledger";

export function DetailDrawer({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const cell = getCellByKey(state.overview, state.inspectCellKey);
  const variant = getVariantByIndex(cell, state.inspectVariantIndex);
  const candidate = variant?.candidate ?? null;
  if (!cell || !candidate || !variant) {
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
            {state.overview ? (
              <div className="vg-detail-query-row">
                <span aria-label="Query" className="vg-query-key" title="Query">
                  <MessageSquareText aria-hidden className="vg-query-key-icon" strokeWidth={1.8} />
                </span>
                <p className="vg-detail-query-text" title={state.overview.label}>
                  {state.overview.label}
                </p>
              </div>
            ) : null}
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
            {cell.variants.length > 1 ? (
              <div className="vg-detail-variant-list">
                {cell.variants.map((entry, index) => (
                  <button
                    className={clsx(
                      "vg-variant-chip",
                      index === state.inspectVariantIndex && "is-active",
                    )}
                    key={entry.variant_key}
                    onClick={() => actions.openInspect(cell.cell_key, index)}
                    type="button"
                  >
                    <span className="vg-variant-chip-label">
                      {entry.variant_label ?? entry.candidate.visgen_id}
                    </span>
                    <span className="vg-variant-chip-score">
                      {entry.candidate.overall_score?.toFixed(2) ?? "—"}
                    </span>
                  </button>
                ))}
              </div>
            ) : null}
            <div className="vg-detail-overview">
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
              <div className="vg-detail-summary">
                <div className="vg-detail-subhead">Scores</div>
                <ScoreBreakdownList candidate={candidate} mode="detail" />
                <div className="vg-detail-facts">
                  {variant.variant_label ? (
                    <span className="vg-detail-fact">{variant.variant_label}</span>
                  ) : null}
                </div>
              </div>
            </div>
            {candidate.guideline_details.length > 0 ? (
              <section className="vg-detail-guidelines">
                <div className="vg-detail-subhead">
                  {`Guidelines used (${candidate.guideline_details.length})`}
                </div>
                <div className="vg-guideline-list">
                  {candidate.guideline_details.map((guideline) => (
                    <article className="vg-guideline-card" key={guideline.id}>
                      <div className="vg-guideline-card-title">{guideline.title}</div>
                      {guideline.description ? (
                        <p className="vg-guideline-card-description">{guideline.description}</p>
                      ) : null}
                      {guideline.sources.length > 0 ? (
                        <div className="vg-guideline-card-citations">
                          <div className="vg-guideline-card-citations-label">Sources</div>
                          <p className="vg-guideline-card-citations-copy">
                            {guideline.sources.join("; ")}
                          </p>
                        </div>
                      ) : null}
                    </article>
                  ))}
                </div>
              </section>
            ) : null}
          </section>
        </div>
      </aside>
    </section>
  );
}
