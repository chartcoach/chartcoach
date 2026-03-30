import type { ViewerActions, ViewerState } from "@/viewer/contract/types";
import { fromOptionValue, toOptionValue } from "@/viewer/render/utils";

export function LayoutPopover({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const overview = state.overview;
  if (!overview || !overview.ui_schema.layout_controls.length) {
    return null;
  }
  const layoutControls = overview.ui_schema.layout_controls;

  return (
    <section
      className={`vg-popover-section is-layout ${state.activePopoverId === "layout" ? "" : "is-hidden"}`}
    >
      <div className="vg-popover-section-title">Layout</div>
      <div className="vg-control-band-row vg-control-band-row-layout">
        {layoutControls.map((control) => (
          <label className="vg-control-group" key={control.id}>
            <span className="vg-control-label">{control.label}</span>
            <select
              className="vg-select"
              onChange={(event) =>
                actions.changeLayout(control.id, fromOptionValue(event.target.value))
              }
              value={toOptionValue(control.value)}
            >
              {control.options.map((option) => (
                <option key={toOptionValue(option.value)} value={toOptionValue(option.value)}>
                  {option.label}
                </option>
              ))}
            </select>
          </label>
        ))}
      </div>
    </section>
  );
}
