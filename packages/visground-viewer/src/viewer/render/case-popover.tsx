import { getCatalogSubset } from "@/viewer/controller/catalog";
import type { ViewerActions, ViewerState } from "@/viewer/contract/types";

export function CasePopover({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const jumpEntries = getCatalogSubset(state, {
    searchTerm: state.searchTerm,
  });

  return (
    <section
      className={`vg-popover-section is-case ${state.activePopoverId === "case" ? "" : "is-hidden"}`}
    >
      <div className="vg-popover-section-title">Cases</div>
      <div className="vg-control-band-row vg-control-band-row-nav">
        <label className="vg-control-group">
          <span className="vg-control-label">Search</span>
          <input
            className="vg-search"
            onChange={(event) => actions.updateSearchTerm(event.target.value)}
            placeholder="Search by case ID or request"
            type="search"
            value={state.searchTerm}
          />
        </label>
        <label className="vg-control-group">
          <span className="vg-control-label">Case</span>
          <select
            className="vg-select"
            onChange={(event) => actions.jumpToCase(event.target.value)}
            value={state.selection.vis_id}
          >
            {jumpEntries.map((entry) => (
              <option key={entry.vis_id} value={entry.vis_id}>
                {`${entry.vis_id} · ${entry.label}`}
              </option>
            ))}
          </select>
        </label>
      </div>
    </section>
  );
}
