import { autoUpdate, flip, offset, shift, useFloating } from "@floating-ui/react";
import { useLayoutEffect } from "react";
import type { ViewerActions, ViewerState } from "../contract/types";
import { ScoreBreakdownList } from "./score-ledger";
import { getVariantByIndex, orientationLabel } from "./utils";

const HOVER_CARD_OFFSET_PX = 16;
const HOVER_CARD_PADDING_PX = 16;

export function HoverCard({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const hover = state.hover;
  const variant = hover ? getVariantByIndex(hover.cell, hover.variantIndex) : null;
  const hoverKey = hover ? `${hover.cell.cell_key}:${hover.variantIndex}` : null;
  const candidate = variant?.candidate;
  const label = hover
    ? orientationLabel([hover.cell.group_label, hover.cell.row_label, hover.cell.column_label])
    : null;
  const { refs, floatingStyles, update } = useFloating({
    open: true,
    placement: "right-start",
    strategy: "fixed",
    whileElementsMounted: autoUpdate,
    middleware: [
      offset(HOVER_CARD_OFFSET_PX),
      flip({
        padding: HOVER_CARD_PADDING_PX,
      }),
      shift({
        crossAxis: true,
        padding: HOVER_CARD_PADDING_PX,
      }),
    ],
  });

  useLayoutEffect(() => {
    refs.setReference(hover?.anchor ?? null);
  }, [hover, refs]);

  useLayoutEffect(() => {
    if (!hoverKey || !hover || !variant || !hover.anchor.isConnected) {
      return;
    }
    void update();
  }, [hover, hoverKey, update, variant]);

  if (!hover || !variant || !hover.anchor.isConnected || !hoverKey || !candidate || !label) {
    return null;
  }

  return (
    <aside
      className="fixed z-[60] box-border grid w-[clamp(17rem,22vw,19rem)] max-h-[min(72vh,34rem)] gap-2 overflow-x-hidden overflow-y-auto border border-border bg-background px-3 py-3 shadow-[var(--ccui-shadow)] max-[860px]:w-[min(19rem,calc(100vw-1.25rem))]"
      data-hover-key={hoverKey}
      onMouseEnter={() => actions.cancelHoverHide()}
      onMouseLeave={() => actions.scheduleHoverHide()}
      ref={refs.setFloating}
      style={floatingStyles}
    >
      <div className="grid gap-2">
        <div className="font-mono text-[0.76rem] font-semibold lowercase text-foreground">
          {label}
        </div>
        {variant.variant_label ? (
          <div className="font-mono text-[0.66rem] leading-[1.18] text-muted-foreground">
            {variant.variant_label}
          </div>
        ) : null}
        <ScoreBreakdownList candidate={candidate} mode="compact" />
      </div>
    </aside>
  );
}
