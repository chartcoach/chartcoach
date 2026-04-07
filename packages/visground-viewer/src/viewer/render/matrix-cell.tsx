import clsx from "clsx";
import type {
  CellVariant,
  MatrixCell as MatrixCellPayload,
  ViewerActions,
  ViewerState,
} from "../contract/types";
import { ScoreLedger } from "./score-ledger";
import { formatScore, orientationLabel, renderImage, toOptionValue } from "./utils";

const MAX_VISIBLE_VARIANTS = 4;

function layoutKind(cell: MatrixCellPayload): "single" | "strip" | "grid" | "gallery" {
  if (cell.variants.length <= 1) {
    return "single";
  }
  if (cell.hidden_axes.length === 1) {
    return "strip";
  }
  if (cell.hidden_axes.length === 2) {
    return "grid";
  }
  return "gallery";
}

function tileLabel(variant: CellVariant, orientation: string): string {
  return variant.variant_label ? `${orientation} · ${variant.variant_label}` : orientation;
}

function footerLabel(variant: CellVariant): string {
  return variant.variant_label ?? variant.candidate.visgen_id;
}

function VariantTile({
  cell,
  variant,
  variantIndex,
  orientation,
  state,
  actions,
}: {
  cell: MatrixCellPayload;
  variant: CellVariant;
  variantIndex: number;
  orientation: string;
  state: ViewerState;
  actions: ViewerActions;
}) {
  const hoverMatch =
    state.hover?.cell?.cell_key === cell.cell_key && state.hover.variantIndex === variantIndex;
  const inspectMatch =
    state.inspectCellKey === cell.cell_key && state.inspectVariantIndex === variantIndex;
  const label = tileLabel(variant, orientation);

  return (
    <button
      aria-label={label}
      className={clsx(
        "vg-variant-tile grid min-w-0 cursor-pointer gap-px border-0 bg-transparent p-0 text-left",
        hoverMatch && "is-hovered",
        inspectMatch && "is-active",
      )}
      onBlur={() => actions.scheduleHoverHide()}
      onClick={() => {
        actions.hideHover(true);
        actions.openInspect(cell.cell_key, variantIndex);
      }}
      onFocus={(event) => actions.showHover(cell, variantIndex, event.currentTarget)}
      onMouseEnter={(event) => actions.showHover(cell, variantIndex, event.currentTarget)}
      onMouseLeave={() => actions.scheduleHoverHide()}
      title={label}
      type="button"
    >
      <div className="vg-chart-frame relative min-h-[5.8rem] w-full min-w-0 overflow-hidden rounded-[2px] bg-[color:color-mix(in_srgb,var(--ccui-paper)_92%,transparent)] shadow-[inset_0_0_0_1px_rgba(17,17,17,0.05)]">
        <div className="vg-chart-canvas is-panel grid h-full w-full place-items-center overflow-hidden px-px py-[0.04rem]">
          {variant.candidate.error ? (
            <p className="m-0 text-destructive">{variant.candidate.error}</p>
          ) : (
            renderImage(
              variant.candidate.image_url || null,
              label,
              variant.candidate.image_meta || null,
              "panel",
            )
          )}
        </div>
      </div>
      {variant.variant_label ? (
        <span className="vg-variant-caption overflow-wrap-anywhere font-mono text-[0.62rem] leading-[1.18] text-muted-foreground [overflow-wrap:anywhere]">
          {variant.variant_label}
        </span>
      ) : null}
    </button>
  );
}

function VariantFooterChip({
  cell,
  variant,
  variantIndex,
  state,
  actions,
}: {
  cell: MatrixCellPayload;
  variant: CellVariant;
  variantIndex: number;
  state: ViewerState;
  actions: ViewerActions;
}) {
  const hoverMatch =
    state.hover?.cell?.cell_key === cell.cell_key && state.hover.variantIndex === variantIndex;
  const inspectMatch =
    state.inspectCellKey === cell.cell_key && state.inspectVariantIndex === variantIndex;
  const overallScore =
    variant.candidate.score_breakdown.find((item) => item.id === "overall")?.score ?? null;

  return (
    <button
      aria-label={footerLabel(variant)}
      className={clsx(
        "vg-variant-chip inline-flex min-h-5 items-center gap-1.5 rounded-[3px] border border-border bg-background px-1.5 py-0.5 font-mono text-[0.62rem] leading-[1.1] text-foreground",
        (hoverMatch || inspectMatch) && "border-foreground/20 bg-muted",
        hoverMatch && "is-hovered",
        inspectMatch && "is-active",
      )}
      onBlur={() => actions.scheduleHoverHide()}
      onClick={() => {
        actions.hideHover(true);
        actions.openInspect(cell.cell_key, variantIndex);
      }}
      onFocus={(event) => actions.showHover(cell, variantIndex, event.currentTarget)}
      onMouseEnter={(event) => actions.showHover(cell, variantIndex, event.currentTarget)}
      onMouseLeave={() => actions.scheduleHoverHide()}
      title={footerLabel(variant)}
      type="button"
    >
      <span className="min-w-0 [overflow-wrap:anywhere]">{footerLabel(variant)}</span>
      <span className="font-bold text-muted-foreground">{formatScore(overallScore) ?? "—"}</span>
    </button>
  );
}

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
  const key = cell.cell_key;
  const hoverKey = state.hover?.cell?.cell_key ?? null;
  const classes = ["vg-matrix-cell", variant === "chart" ? "is-chart" : "is-footer"];
  const kind = layoutKind(cell);
  const visibleVariants = cell.variants.slice(0, MAX_VISIBLE_VARIANTS);
  const overflowCount = Math.max(cell.variant_count - visibleVariants.length, 0);

  if (state.inspectCellKey && key === state.inspectCellKey) {
    classes.push("is-focused");
  }
  if (cell.missing || cell.variants.length === 0) {
    classes.push("is-missing");
  }
  if (cell.variant_count > 1) {
    classes.push("is-multi");
  }
  classes.push(`is-layout-${kind}`);
  if (hoverKey && hoverKey === key) {
    classes.push("is-hover-source");
  } else if (hoverKey) {
    classes.push("is-recessed");
  }

  const orientation = orientationLabel([cell.group_label, cell.row_label, cell.column_label]);

  return (
    <div
      className={clsx(classes)}
      data-cell-key={key}
      data-column-value={toOptionValue(cell.column_value)}
      data-group-value={toOptionValue(cell.group_value ?? null)}
      data-row-value={toOptionValue(cell.row_value)}
      key={key}
      title={orientation}
    >
      {cell.missing || cell.variants.length === 0 ? (
        variant === "chart" ? (
          <span className="font-mono text-[0.78rem] font-bold lowercase tracking-[0.02em] text-muted-foreground">
            {cell.placeholder_reason || "missing candidate"}
          </span>
        ) : (
          <span aria-hidden />
        )
      ) : (
        <div className={clsx("vg-cell-stack", `is-${kind}`)}>
          {variant === "chart" ? (
            <>
              <div className={clsx("vg-variant-grid", `is-${kind}`)}>
                {visibleVariants.map((entry, variantIndex) => (
                  <VariantTile
                    actions={actions}
                    cell={cell}
                    key={entry.variant_key}
                    orientation={orientation}
                    state={state}
                    variant={entry}
                    variantIndex={variantIndex}
                  />
                ))}
                {overflowCount > 0 ? (
                  <div className="grid min-h-[5.1rem] place-items-center rounded-[4px] border border-dashed border-foreground/10 bg-foreground/[0.02] font-mono text-[0.8rem] font-bold text-muted-foreground">
                    {`+${overflowCount}`}
                  </div>
                ) : null}
              </div>
              {cell.hidden_axis_labels.length > 0 ? (
                <div className="vg-cell-meta flex min-w-0 items-center gap-1">
                  <span className="font-mono text-[0.62rem] leading-[1.18] text-muted-foreground [overflow-wrap:anywhere]">
                    {`in cell: ${cell.hidden_axis_labels.join(" + ")}`}
                  </span>
                </div>
              ) : null}
            </>
          ) : cell.variant_count === 1 ? (
            <ScoreLedger candidate={cell.variants[0]!.candidate} mode="matrix" />
          ) : (
            <div className="vg-variant-chip-row flex w-full flex-wrap items-center gap-1 pt-1">
              {visibleVariants.map((entry, variantIndex) => (
                <VariantFooterChip
                  actions={actions}
                  cell={cell}
                  key={entry.variant_key}
                  state={state}
                  variant={entry}
                  variantIndex={variantIndex}
                />
              ))}
              {overflowCount > 0 ? (
                <span className="vg-variant-chip inline-flex min-h-5 items-center gap-1.5 rounded-[3px] border border-border bg-background px-1.5 py-0.5 font-mono text-[0.62rem] leading-[1.1] text-muted-foreground">
                  {`+${overflowCount}`}
                </span>
              ) : null}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
