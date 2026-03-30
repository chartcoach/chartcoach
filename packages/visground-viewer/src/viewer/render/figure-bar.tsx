import { getCatalogIndex, getCatalogSubset } from "@/viewer/controller/catalog";
import type {
  ViewerActions,
  ViewerLayoutControl,
  ViewerOption,
  ViewerState,
  ViewerToolbarPill,
} from "@/viewer/contract/types";

function selectedLabel(options: ViewerOption[] | undefined, value: string | null): string | null {
  return options?.find((option) => option.value === value)?.label ?? null;
}

function layoutControl(
  state: ViewerState,
  id: ViewerLayoutControl["id"],
): ViewerLayoutControl | undefined {
  return state.overview?.ui_schema.layout_controls.find((control) => control.id === id);
}

function toolbarPillText(state: ViewerState, pill: ViewerToolbarPill): string {
  const schema = state.overview?.ui_schema;
  if (!schema) {
    return pill.label;
  }

  if (pill.id === "filters") {
    const activeLabels = schema.filters
      .filter((filter) => filter.value !== null)
      .map((filter) => selectedLabel(filter.options, filter.value))
      .filter((value): value is string => Boolean(value));
    return activeLabels.length > 0 ? activeLabels.join(" · ") : pill.label;
  }

  const row = layoutControl(state, "row_dimension");
  const column = layoutControl(state, "column_dimension");
  const group = layoutControl(state, "group_dimension");
  const parts = [
    selectedLabel(row?.options, state.selection.layout.row_dimension),
    selectedLabel(column?.options, state.selection.layout.column_dimension),
  ];
  const groupLabel = selectedLabel(group?.options, state.selection.layout.group_dimension);
  return groupLabel
    ? `${parts.filter(Boolean).join(" × ")} · ${groupLabel}`
    : parts.filter(Boolean).join(" × ");
}

export function FigureBar({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const filteredCatalog = getCatalogSubset(state, {
    searchTerm: state.searchTerm,
  });
  const filteredIndex = getCatalogIndex(filteredCatalog, state.selection.vis_id);
  const pills = state.overview?.ui_schema.toolbar?.pills ?? [];

  return (
    <div className="vg-figure-bar">
      <div className="vg-figure-meta">
        <button
          aria-expanded={state.activePopoverId === "case"}
          className="vg-toolbar-pill vg-toolbar-pill-case vg-case-trigger"
          onClick={(event) => actions.togglePopover("case", event.currentTarget)}
          type="button"
        >
          <span className="vg-toolbar-pill-value">{state.selection.vis_id}</span>
        </button>
        {pills.length > 0 ? (
          <div className="vg-toolbar-summary">
            {pills.map((pill) => {
              const text = toolbarPillText(state, pill);
              return (
                <button
                  aria-expanded={state.activePopoverId === pill.id}
                  className={`vg-toolbar-pill ${state.activePopoverId === pill.id ? "is-active" : ""}`.trim()}
                  key={pill.id}
                  onClick={(event) => actions.togglePopover(pill.id, event.currentTarget)}
                  type="button"
                >
                  <span className="vg-toolbar-pill-value">{text}</span>
                </button>
              );
            })}
          </div>
        ) : null}
      </div>
      <div className="vg-figure-actions">
        <div className="vg-pager">
          <div className="vg-pager-controls">
            <button
              aria-label="Previous case"
              className="vg-nav-button vg-nav-icon"
              disabled={filteredIndex <= 0 || !!state.busy}
              onClick={() => actions.stepCase(-1)}
              title="Previous case"
              type="button"
            >
              ‹
            </button>
            <button
              aria-label="Next case"
              className="vg-nav-button vg-nav-icon"
              disabled={
                filteredIndex < 0 || filteredIndex >= filteredCatalog.length - 1 || !!state.busy
              }
              onClick={() => actions.stepCase(1)}
              title="Next case"
              type="button"
            >
              ›
            </button>
          </div>
          <div className="vg-pager-meta">
            {filteredIndex >= 0
              ? `${filteredIndex + 1}/${filteredCatalog.length}`
              : `1/${state.catalog.length}`}
          </div>
        </div>
      </div>
    </div>
  );
}
