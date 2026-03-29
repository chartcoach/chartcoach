import type { ViewerState } from "@/viewer/contract/types";

export function ErrorBanner({ state }: { state: ViewerState }) {
  return (
    <div className="vg-error-banner" hidden={!state.error}>
      {state.error ? (
        <>
          <strong>Viewer error</strong>
          <p className="vg-copy">{state.error}</p>
        </>
      ) : null}
    </div>
  );
}
