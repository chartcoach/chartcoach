import { MessageSquareText } from "lucide-react";
import type { ViewerState } from "@/viewer/contract/types";

export function QueryBand({ state }: { state: ViewerState }) {
  if (!state.overview) {
    return null;
  }

  return (
    <div className="vg-query-band">
      <div className="vg-query-block">
        <div className="vg-query-row">
          <span aria-label="Query" className="vg-query-key" title="Query">
            <MessageSquareText aria-hidden className="vg-query-key-icon" strokeWidth={1.8} />
          </span>
          <p className="vg-query-text" title={state.overview.label}>
            {state.overview.label}
          </p>
        </div>
      </div>
    </div>
  );
}
