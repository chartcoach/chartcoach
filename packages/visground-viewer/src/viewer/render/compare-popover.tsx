import type { ViewerActions, ViewerState } from "@/viewer/contract/types";

export function ComparePopover({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const overview = state.overview;
  const variantControls = overview?.ui_schema.variant_controls;
  if (!overview || !variantControls) {
    return null;
  }

  return (
    <section
      className={`vg-popover-section is-compare ${state.activePopoverId === "compare" ? "" : "is-hidden"}`}
    >
      <div className="vg-popover-section-title">Compare</div>
      <div className="vg-segmented-toggle">
        {variantControls.options.map((option) => (
          <button
            className={`vg-segmented-button ${state.selection.overview_variant === option.value ? "is-active" : ""}`.trim()}
            key={option.value}
            onClick={() => actions.changeOverviewVariant(option.value)}
            type="button"
          >
            {option.label}
          </button>
        ))}
      </div>
    </section>
  );
}
