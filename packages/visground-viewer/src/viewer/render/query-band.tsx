import type { ViewerState } from "@/viewer/contract/types";

export function QueryBand({ state }: { state: ViewerState }) {
  if (!state.overview) {
    return null;
  }

  return (
    <div className="vg-query-band">
      <div className="vg-query-block">
        <p className="vg-query-text" title={state.overview.nl_query}>
          {state.overview.nl_query}
        </p>
      </div>
    </div>
  );
}
