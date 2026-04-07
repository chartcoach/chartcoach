import clsx from "clsx";
import { getCatalogSubset } from "../controller/catalog";
import type { ViewerActions, ViewerState } from "../contract/types";
import { ViewerSearchField, ViewerSelectField } from "./control-fields";
import { toOptionValue } from "./utils";

export function CasePopover({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const jumpEntries = getCatalogSubset(state, {
    searchTerm: state.searchTerm,
  });

  return (
    <section className={clsx("grid min-w-0 gap-3", state.activePopoverId !== "case" && "hidden")}>
      <div className="font-mono text-[0.72rem] font-bold lowercase tracking-[0.02em] text-muted-foreground">
        Cases
      </div>
      <div className="grid min-w-0 gap-3">
        <ViewerSearchField
          label="Search"
          onChange={actions.updateSearchTerm}
          placeholder="Search by case ID or request"
          value={state.searchTerm}
        />
        <ViewerSelectField
          label="Case"
          onValueChange={actions.jumpToCase}
          options={jumpEntries.map((entry) => ({
            value: entry.vis_id,
            label: `${entry.vis_id} · ${entry.label}`,
          }))}
          value={toOptionValue(state.selection.vis_id)}
        />
      </div>
    </section>
  );
}
