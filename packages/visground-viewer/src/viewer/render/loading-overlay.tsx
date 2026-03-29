import type { ViewerState } from "@/viewer/contract/types";

export function LoadingOverlay({ state }: { state: ViewerState }) {
  const message =
    state.busy === "case"
      ? "Loading next case…"
      : state.busy === "update"
        ? "Updating viewer…"
        : "Loading viewer…";
  return (
    <div className="vg-content-overlay" hidden={!state.busy}>
      <div className="vg-loading-panel">
        <div className="vg-spinner" />
        <p className="vg-muted">{message}</p>
      </div>
    </div>
  );
}
