import type { ViewerActions, ViewerState } from "@/viewer/contract/types";
import { fromOptionValue, toOptionValue } from "@/viewer/render/utils";

export function ScopePopover({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const overview = state.overview;
  if (!overview) {
    return null;
  }

  const { scope_filters: scopeFilters } = overview.ui_schema;

  return (
    <section
      className={`vg-popover-section is-scope ${state.activePopoverId === "objective" ? "" : "is-hidden"}`}
    >
      <div className="vg-popover-section-title">Scope</div>
      <div className="vg-control-band-row vg-control-band-row-scope">
        {scopeFilters.map((filter) => (
          <label className="vg-control-group" key={filter.id}>
            <span className="vg-control-label">{filter.label}</span>
            <select
              className="vg-select"
              onChange={(event) =>
                actions.changeScopeFilter(filter.id, fromOptionValue(event.target.value))
              }
              value={toOptionValue(filter.value)}
            >
              {filter.options.map((option) => (
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
