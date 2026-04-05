import type { ViewerState } from "../contract/types";

export function LoadingOverlay({ state }: { state: ViewerState }) {
  const message =
    state.busy === "case"
      ? "Loading next case…"
      : state.busy === "update"
        ? "Updating viewer…"
        : "Loading viewer…";
  return (
    <div
      className="absolute inset-0 z-10 grid place-items-center bg-[color:color-mix(in_srgb,var(--ccui-paper)_72%,transparent)]"
      hidden={!state.busy}
    >
      <div className="grid place-items-center gap-3 border border-border bg-background px-5 py-4 shadow-[var(--ccui-shadow)]">
        <div className="size-8 animate-spin rounded-full border-2 border-border border-t-foreground" />
        <p className="m-0 leading-[1.48] text-muted-foreground">{message}</p>
      </div>
    </div>
  );
}
