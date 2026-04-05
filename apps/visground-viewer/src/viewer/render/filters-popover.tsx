import clsx from "clsx";
import type { ViewerActions, ViewerState } from "../contract/types";
import { ViewerSelectField } from "./control-fields";
import { fromOptionValue, toOptionValue } from "./utils";

export function FiltersPopover({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const overview = state.overview;
  if (!overview) {
    return null;
  }

  const filters = overview.ui_schema.filters;

  return (
    <section
      className={clsx("grid min-w-0 gap-3", state.activePopoverId !== "filters" && "hidden")}
    >
      <div className="font-mono text-[0.72rem] font-bold lowercase tracking-[0.02em] text-muted-foreground">
        Filters
      </div>
      <div className="grid min-w-0 gap-3">
        {filters.map((filter) => (
          <ViewerSelectField
            key={filter.id}
            label={filter.label}
            onValueChange={(value) => actions.changeFilter(filter.id, fromOptionValue(value))}
            options={filter.options}
            value={toOptionValue(filter.value)}
          />
        ))}
      </div>
    </section>
  );
}
