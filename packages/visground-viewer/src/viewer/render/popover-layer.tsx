import type { ViewerActions, ViewerRefs, ViewerState } from "@/viewer/contract/types";
import { CasePopover } from "@/viewer/render/case-popover";
import { ComparePopover } from "@/viewer/render/compare-popover";
import { ScopePopover } from "@/viewer/render/scope-popover";

export function PopoverLayer({
  state,
  actions,
  refs,
}: {
  state: ViewerState;
  actions: ViewerActions;
  refs: ViewerRefs;
}) {
  if (!state.overview) {
    return null;
  }

  return (
    <>
      <button
        className="vg-controls-scrim"
        hidden={state.activePopoverId == null}
        onClick={() => actions.closePopover()}
        type="button"
      />
      <div className="vg-pill-popover" hidden={state.activePopoverId == null} ref={refs.popoverRef}>
        <div className="vg-pill-popover-card">
          <CasePopover actions={actions} state={state} />
          <ScopePopover actions={actions} state={state} />
          <ComparePopover actions={actions} state={state} />
        </div>
      </div>
    </>
  );
}
