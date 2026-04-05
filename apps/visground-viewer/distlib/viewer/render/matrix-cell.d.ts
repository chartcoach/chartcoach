import type {
  MatrixCell as MatrixCellPayload,
  ViewerActions,
  ViewerState,
} from "../contract/types";
export declare function MatrixCell({
  cell,
  state,
  actions,
  variant,
}: {
  cell: MatrixCellPayload;
  state: ViewerState;
  actions: ViewerActions;
  variant: "chart" | "footer";
}): import("react/jsx-runtime").JSX.Element;
//# sourceMappingURL=matrix-cell.d.ts.map
