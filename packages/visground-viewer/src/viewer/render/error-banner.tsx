import type { ViewerState } from "../contract/types";

export function ErrorBanner({ state }: { state: ViewerState }) {
  return (
    <div
      className="mt-4 grid gap-1 border border-border bg-card px-4 py-3 text-card-foreground"
      hidden={!state.error}
    >
      {state.error ? (
        <>
          <strong>Viewer error</strong>
          <p className="m-0 leading-[1.48] text-muted-foreground">{state.error}</p>
        </>
      ) : null}
    </div>
  );
}
