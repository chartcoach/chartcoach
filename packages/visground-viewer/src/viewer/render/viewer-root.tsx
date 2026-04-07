import { useRef } from "react";
import type { ViewerBridge } from "../bridge/types";
import { useViewerController } from "../controller/use-viewer-controller";
import { AgentationDebug } from "./agentation-debug";
import { DetailDrawer } from "./detail-drawer";
import { ErrorBanner } from "./error-banner";
import { FigureBar } from "./figure-bar";
import { HoverCard } from "./hover-card";
import { LoadingOverlay } from "./loading-overlay";
import { OverviewMatrix } from "./overview-matrix";
import { CasePopover } from "./case-popover";
import { FiltersPopover } from "./filters-popover";
import { LayoutPopover } from "./layout-popover";
import { QueryBand } from "./query-band";

export function ViewerRoot({ bridge }: { bridge: ViewerBridge }) {
  const controller = useViewerController(bridge);
  const { state, refs, actions } = controller;
  const caseTriggerRef = useRef<HTMLButtonElement | null>(null);
  const filtersTriggerRef = useRef<HTMLButtonElement | null>(null);
  const layoutTriggerRef = useRef<HTMLButtonElement | null>(null);
  return (
    <div className="vg-root bg-background text-foreground" ref={refs.rootRef} tabIndex={0}>
      <div className="mx-auto w-full max-w-[84rem] px-3 pb-3 pt-1 md:px-4 lg:max-w-[74rem]">
        <AgentationDebug enabled={state.debug} />
        <header className="relative grid gap-px">
          <FigureBar
            actions={actions}
            state={state}
            triggerRefs={{
              case: caseTriggerRef,
              filters: filtersTriggerRef,
              layout: layoutTriggerRef,
            }}
          />
          {state.overview && state.activePopoverId ? (
            <div className="mt-2 grid gap-3 rounded-[4px] border border-border bg-background px-4 py-4 shadow-[var(--ccui-shadow)]">
              <CasePopover actions={actions} state={state} />
              <FiltersPopover actions={actions} state={state} />
              <LayoutPopover actions={actions} state={state} />
            </div>
          ) : null}
        </header>
        <ErrorBanner state={state} />
        <div className="relative pb-0.5">
          <LoadingOverlay state={state} />
          {state.overview ? (
            <>
              <QueryBand state={state} />
              <div className="relative z-[1] min-h-56">
                <section className="vg-matrix-section">
                  <OverviewMatrix actions={actions} state={state} />
                </section>
                <DetailDrawer actions={actions} state={state} />
              </div>
            </>
          ) : null}
        </div>
        <HoverCard actions={actions} state={state} />
      </div>
    </div>
  );
}
