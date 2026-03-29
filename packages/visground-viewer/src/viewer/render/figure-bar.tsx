import { getCatalogIndex, getCatalogSubset } from "@/viewer/controller/catalog";
import type {
  ViewerActions,
  ViewerOption,
  ViewerState,
  ViewerToolbarPill,
  ViewerVariantOption,
} from "@/viewer/contract/types";

function selectedLabel<T extends ViewerOption | ViewerVariantOption>(
  options: T[] | undefined,
  value: string | null,
): string | null {
  return options?.find((option) => option.value === value)?.label ?? null;
}

function toolbarPillText(state: ViewerState, pill: ViewerToolbarPill): string {
  const schema = state.overview?.ui_schema;

  if (pill.id === "objective") {
    const control = schema?.scope_filters.find((item) => item.id === "objective");
    return selectedLabel(control?.options, state.selection.objective) ?? pill.label;
  }

  const controls = schema?.variant_controls;
  return selectedLabel(controls?.options, state.selection.overview_variant) ?? pill.label;
}

export function FigureBar({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const filteredCatalog = getCatalogSubset(state, {
    requestChart: state.selection.request_chart,
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
