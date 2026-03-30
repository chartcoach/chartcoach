import type { AnywidgetModelLike } from "@/viewer/contract/types";
import { useViewerController } from "@/viewer/controller/use-viewer-controller";
import { AgentationDebug } from "@/viewer/render/agentation-debug";
import { DetailDrawer } from "@/viewer/render/detail-drawer";
import { ErrorBanner } from "@/viewer/render/error-banner";
import { FigureBar } from "@/viewer/render/figure-bar";
import { HoverCard } from "@/viewer/render/hover-card";
import { LoadingOverlay } from "@/viewer/render/loading-overlay";
import { OverviewMatrix } from "@/viewer/render/overview-matrix";
import { PopoverLayer } from "@/viewer/render/popover-layer";
import { QueryBand } from "@/viewer/render/query-band";

export function ViewerRoot({ model }: { model: AnywidgetModelLike }) {
  const controller = useViewerController(model);
  const { state, refs, actions } = controller;

  return (
    <div className="vg-root" ref={refs.rootRef} tabIndex={0}>
      <div className="vg-shell">
        <AgentationDebug enabled={state.debug} />
        <header className="vg-header">
          <FigureBar actions={actions} state={state} />
          <PopoverLayer actions={actions} refs={refs} state={state} />
        </header>
        <ErrorBanner state={state} />
        <div className={`vg-content-frame ${state.busy ? "is-loading" : ""}`.trim()}>
          <LoadingOverlay state={state} />
          {state.overview ? (
            <>
              <QueryBand state={state} />
              <div className="vg-matrix-stage">
                <section className="vg-matrix-section">
                  <OverviewMatrix actions={actions} state={state} />
                </section>
                <DetailDrawer actions={actions} state={state} />
              </div>
            </>
          ) : null}
        </div>
        <HoverCard actions={actions} refs={refs} state={state} />
      </div>
    </div>
  );
}
