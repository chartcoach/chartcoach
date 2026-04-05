import { MessageSquareText } from "lucide-react";
import type { ViewerState } from "../contract/types";

export function QueryBand({ state }: { state: ViewerState }) {
  if (!state.overview) {
    return null;
  }

  return (
    <div className="py-2 pb-3">
      <div className="w-full border border-border bg-muted px-4 py-3 max-[860px]:px-3 max-[860px]:py-3">
        <div className="grid grid-cols-[1.4rem_minmax(0,1fr)] items-center gap-3 max-[860px]:grid-cols-1 max-[860px]:gap-1.5">
          <span
            aria-label="Query"
            className="inline-flex w-6 items-center justify-start text-muted-foreground max-[860px]:w-auto"
            title="Query"
          >
            <MessageSquareText aria-hidden className="size-[1.12rem]" strokeWidth={1.8} />
          </span>
          <p
            className="m-0 text-[1.03rem] font-semibold leading-[1.44] tracking-[-0.01em] text-foreground max-[860px]:text-[0.98rem] max-[860px]:leading-[1.42]"
            title={state.overview.label}
          >
            {state.overview.label}
          </p>
        </div>
      </div>
    </div>
  );
}
