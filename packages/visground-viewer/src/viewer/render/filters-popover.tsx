import clsx from "clsx";
import type { ViewerActions, ViewerState } from "@/viewer/contract/types";
import { fromOptionValue, toOptionValue } from "@/viewer/render/utils";

export function FiltersPopover({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const overview = state.overview;
  if (!overview) {
    return null;
  }

  const filters = overview.ui_schema.filters;

  return (
    <section
      className={clsx(
        "vg-popover-section",
        "is-filters",
        state.activePopoverId !== "filters" && "is-hidden",
      )}
    >
      <div className="vg-popover-section-title">Filters</div>
      <div className="vg-control-band-row vg-control-band-row-filters">
        {filters.map((filter) => (
          <label className="vg-control-group" key={filter.id}>
            <span className="vg-control-label">{filter.label}</span>
            <select
              className="vg-select"
              onChange={(event) =>
                actions.changeFilter(filter.id, fromOptionValue(event.target.value))
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
