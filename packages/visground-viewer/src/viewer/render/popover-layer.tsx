import type { ViewerActions, ViewerRefs, ViewerState } from "@/viewer/contract/types";
import { CasePopover } from "@/viewer/render/case-popover";
import { FiltersPopover } from "@/viewer/render/filters-popover";
import { LayoutPopover } from "@/viewer/render/layout-popover";

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
          <FiltersPopover actions={actions} state={state} />
          <LayoutPopover actions={actions} state={state} />
        </div>
      </div>
    </>
  );
}
