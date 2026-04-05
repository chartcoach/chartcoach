import clsx from "clsx";
import type {
  MatrixCell as MatrixCellPayload,
  MatrixGroup,
  ViewerActions,
  ViewerState,
} from "../contract/types";
import { AxisHeader } from "./axis-header";
import { MatrixCell } from "./matrix-cell";
import { spotlightClass, toOptionValue } from "./utils";

function groupHeaderClass(hoverCell: MatrixCellPayload | null, groupValue: string | null): string {
  return clsx(
    "vg-group-head",
    spotlightClass(Boolean(hoverCell), hoverCell?.group_value === groupValue),
  );
}

function columnHeaderClass(
  hoverCell: MatrixCellPayload | null,
  columnValue: string | null,
): string {
  return clsx(
    "vg-column-head",
    spotlightClass(Boolean(hoverCell), hoverCell?.column_value === columnValue),
  );
}

function rowHeaderClass(hoverCell: MatrixCellPayload | null, rowValue: string | null): string {
  return clsx("vg-row-head", spotlightClass(Boolean(hoverCell), hoverCell?.row_value === rowValue));
}

function GroupedSection({
  group,
  groupIndex,
  state,
  actions,
}: {
  group: MatrixGroup;
  groupIndex: number;
  state: ViewerState;
  actions: ViewerActions;
}) {
  const axes = state.overview!.ui_schema.matrix_axes;
  const hoverCell = state.hover?.cell ?? null;

  return (
    <section className="vg-overview-group" key={group.value}>
      <div
        className="vg-overview-group-header"
        style={{ ["--vg-overview-group-cols" as string]: String(group.columns.length) }}
      >
        <AxisHeader
          className={groupHeaderClass(hoverCell, group.value)}
          dimensionLabel={axes.group_label || ""}
          extraProps={{
            "data-group-value": toOptionValue(group.value),
          }}
          kind="group"
          metaKind={group.meta_kind}
          metaLabel={group.meta_label}
          showDimension
          valueLabel={group.label}
        />
      </div>
      <div
        className="vg-overview-group-grid"
        style={{ ["--vg-overview-group-cols" as string]: String(group.columns.length) }}
      >
        <div className={clsx("vg-overview-corner", hoverCell && "is-recessed")} />
        {group.columns.map((column, columnIndex) => (
          <AxisHeader
            className={columnHeaderClass(hoverCell, column.value)}
            dimensionLabel={axes.column_label}
            extraProps={{
              "data-column-value": toOptionValue(column.value),
              "data-group-value": toOptionValue(group.value),
            }}
            key={`column-${toOptionValue(group.value)}-${toOptionValue(column.value)}`}
            kind="column"
            metaKind={column.meta_kind}
            metaLabel={column.meta_label}
            showDimension={groupIndex === 0 && columnIndex === 0}
            valueLabel={column.label}
          />
        ))}
        {group.rows.flatMap((row, rowIndex) => [
          <AxisHeader
            className={rowHeaderClass(hoverCell, row.value)}
            dimensionLabel={axes.row_label}
            extraProps={{
              "data-row-value": toOptionValue(row.value),
            }}
            key={`row-${toOptionValue(group.value)}-${toOptionValue(row.value)}`}
            kind="row"
            metaKind={row.meta_kind}
            metaLabel={row.meta_label}
            showDimension={groupIndex === 0 && rowIndex === 0}
            valueLabel={row.label}
          />,
          ...row.cells.map((cell) => (
            <MatrixCell
              actions={actions}
              cell={cell}
              key={`${cell.cell_key}-chart`}
              state={state}
              variant="chart"
            />
          )),
          <div
            className={clsx("vg-row-footer-spacer", hoverCell && "is-recessed")}
            key={`row-footer-spacer-${toOptionValue(group.value)}-${toOptionValue(row.value)}`}
          />,
          ...row.cells.map((cell) => (
            <MatrixCell
              actions={actions}
              cell={cell}
              key={`${cell.cell_key}-footer`}
              state={state}
              variant="footer"
            />
          )),
        ])}
      </div>
    </section>
  );
}

export function OverviewMatrix({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const matrix = state.overview?.matrix;
  if (!matrix) {
    return null;
  }

  const hoverCell = state.hover?.cell ?? null;
  const hasHover = Boolean(hoverCell);
  const axes = state.overview!.ui_schema.matrix_axes;

  if (matrix.kind === "grouped") {
    return (
      <div
        className={clsx(
          "vg-matrix-wrap",
          "vg-matrix-wrap-overview",
          hasHover && "is-spotlight-active",
        )}
      >
        <div className="vg-overview-stack">
          {matrix.groups.map((group, groupIndex) => (
            <GroupedSection
              actions={actions}
              group={group}
              groupIndex={groupIndex}
              key={group.value}
              state={state}
            />
          ))}
        </div>
      </div>
    );
  }

  return (
    <div
      className={clsx(
        "vg-matrix-wrap",
        "vg-matrix-wrap-overview",
        hasHover && "is-spotlight-active",
      )}
    >
      <div
        className="vg-overview-flat-grid"
        style={{ ["--vg-overview-cols" as string]: String(matrix.columns.length) }}
      >
        <div className={clsx("vg-overview-corner", hoverCell && "is-recessed")} />
        {matrix.columns.map((column, columnIndex) => (
          <AxisHeader
            className={columnHeaderClass(hoverCell, column.value)}
            dimensionLabel={axes.column_label}
            extraProps={{
              "data-column-value": toOptionValue(column.value),
            }}
            key={`flat-column-${toOptionValue(column.value)}`}
            kind="column"
            metaKind={column.meta_kind}
            metaLabel={column.meta_label}
            showDimension={columnIndex === 0}
            valueLabel={column.label}
          />
        ))}
        {matrix.rows.flatMap((row, rowIndex) => [
          <AxisHeader
            className={rowHeaderClass(hoverCell, row.value)}
            dimensionLabel={axes.row_label}
            extraProps={{
              "data-row-value": toOptionValue(row.value),
            }}
            key={`flat-row-${toOptionValue(row.value)}`}
            kind="row"
            metaKind={row.meta_kind}
            metaLabel={row.meta_label}
            showDimension={rowIndex === 0}
            valueLabel={row.label}
          />,
          ...row.cells.map((cell) => (
            <MatrixCell
              actions={actions}
              cell={cell}
              key={`${cell.cell_key}-chart`}
              state={state}
              variant="chart"
            />
          )),
          <div
            className={clsx("vg-row-footer-spacer", hoverCell && "is-recessed")}
            key={`flat-row-footer-spacer-${toOptionValue(row.value)}`}
          />,
          ...row.cells.map((cell) => (
            <MatrixCell
              actions={actions}
              cell={cell}
              key={`${cell.cell_key}-footer`}
              state={state}
              variant="footer"
            />
          )),
        ])}
      </div>
    </div>
  );
}
