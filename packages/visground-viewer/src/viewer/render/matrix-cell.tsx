import type {
  MatrixCell as MatrixCellPayload,
  ViewerActions,
  ViewerState,
} from "@/viewer/contract/types";
import { ScoreLedger } from "@/viewer/render/score-ledger";
import { orientationLabel, renderImage, toOptionValue } from "@/viewer/render/utils";

export function MatrixCell({
  cell,
  state,
  actions,
  variant,
}: {
  cell: MatrixCellPayload;
  state: ViewerState;
  actions: ViewerActions;
  variant: "chart" | "footer";
}) {
  const candidate = cell.candidate;
  const key = cell.cell_key;
  const hoverKey = state.hover?.cell?.cell_key ?? null;
  const classes = ["vg-matrix-cell", variant === "chart" ? "is-chart" : "is-footer"];

  if (state.inspectCellKey && key === state.inspectCellKey) {
    classes.push("is-focused");
  }
  if (!candidate || cell.missing) {
    classes.push("is-missing");
  }
  if (hoverKey && hoverKey === key) {
    classes.push("is-hover-source");
  } else if (hoverKey) {
    classes.push("is-recessed");
  }

  const label = orientationLabel([cell.group_label, cell.row_label, cell.column_label]);

  return (
    <button
      aria-label={label ? `${label} chart` : undefined}
      className={classes.join(" ")}
      data-cell-key={key}
      data-column-value={toOptionValue(cell.column_value)}
      data-group-value={toOptionValue(cell.group_value ?? null)}
      data-row-value={toOptionValue(cell.row_value)}
      disabled={!candidate || cell.missing}
      key={key}
      onBlur={() => actions.scheduleHoverHide()}
      onClick={() => {
        actions.hideHover(true);
        actions.openInspect(cell.cell_key);
      }}
      onFocus={(event) => candidate && actions.showHover(cell, event.currentTarget)}
      onMouseEnter={(event) => candidate && actions.showHover(cell, event.currentTarget)}
      onMouseLeave={() => actions.scheduleHoverHide()}
      title={label}
      type="button"
    >
      {!candidate || cell.missing ? (
        variant === "chart" ? (
          <span className="vg-missing-label">{cell.placeholder_reason || "missing candidate"}</span>
        ) : (
          <span aria-hidden className="vg-footer-placeholder" />
        )
      ) : (
        <div className="vg-cell-stack">
          {variant === "chart" ? (
            <div className="vg-chart-frame">
              <div className="vg-chart-canvas is-panel">
                {candidate.error ? (
                  <p className="vg-error">{candidate.error}</p>
                ) : (
                  renderImage(
                    candidate.image_url || null,
                    label,
                    candidate.image_meta || null,
                    "panel",
                  )
                )}
              </div>
            </div>
          ) : (
            <ScoreLedger candidate={candidate} mode="matrix" />
          )}
        </div>
      )}
    </button>
  );
}
