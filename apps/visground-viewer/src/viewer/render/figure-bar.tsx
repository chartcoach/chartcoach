import clsx from "clsx";
import { Button } from "@chartcoach/ui/components/button";
import { ChevronLeft, ChevronRight } from "lucide-react";
import type { RefObject } from "react";
import { getCatalogIndex, getCatalogSubset } from "../controller/catalog";
import type {
  ViewerActions,
  ViewerLayoutControl,
  ViewerOption,
  ViewerPopoverId,
  ViewerState,
  ViewerToolbarPill,
} from "../contract/types";

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
  const rowLabel = selectedLabel(row?.options, state.selection.layout.row_dimension);
  const columnLabel = selectedLabel(column?.options, state.selection.layout.column_dimension);
  const groupLabel = selectedLabel(group?.options, state.selection.layout.group_dimension);
  return [
    rowLabel ? `Rows: ${rowLabel}` : null,
    columnLabel ? `Columns: ${columnLabel}` : null,
    groupLabel ? `Groups: ${groupLabel}` : null,
  ]
    .filter((value): value is string => Boolean(value))
    .join(" · ");
}

export function FigureBar({
  state,
  actions,
  triggerRefs,
}: {
  state: ViewerState;
  actions: ViewerActions;
  triggerRefs: Record<ViewerPopoverId, RefObject<HTMLButtonElement | null>>;
}) {
  const filteredCatalog = getCatalogSubset(state, {
    searchTerm: state.searchTerm,
  });
  const filteredIndex = getCatalogIndex(filteredCatalog, state.selection.vis_id);
  const pills = state.overview?.ui_schema.toolbar?.pills ?? [];
  const toolbarPillBase =
    "h-auto min-h-6 rounded-none border-border bg-muted px-2 py-1 font-mono text-[0.66rem] font-bold leading-none text-muted-foreground hover:bg-accent hover:text-accent-foreground";
  const toolbarPillActive = "border-foreground/25 bg-background text-foreground";

  return (
    <div className="grid grid-cols-[minmax(0,1fr)_auto] items-center gap-2 pb-1 pt-px max-[980px]:grid-cols-1 max-[980px]:items-start">
      <div className="flex min-w-0 flex-wrap items-start gap-1.5">
        <Button
          aria-expanded={state.activePopoverId === "case"}
          className={clsx(
            toolbarPillBase,
            "min-w-[4.2rem] bg-background px-2.5 py-1 text-[0.82rem] tracking-[0.01em] text-foreground",
            state.activePopoverId === "case" && toolbarPillActive,
          )}
          onClick={() => actions.togglePopover("case")}
          ref={triggerRefs.case}
          size="sm"
          type="button"
          variant="outline"
        >
          <span className="font-mono text-[0.82rem] font-bold tracking-[0.01em] text-inherit">
            {state.selection.vis_id}
          </span>
        </Button>
        {pills.length > 0 ? (
          <div className="flex min-w-0 flex-wrap items-center gap-1">
            {pills.map((pill) => {
              const text = toolbarPillText(state, pill);
              return (
                <Button
                  aria-expanded={state.activePopoverId === pill.id}
                  className={clsx(
                    toolbarPillBase,
                    state.activePopoverId === pill.id && toolbarPillActive,
                  )}
                  key={pill.id}
                  onClick={() => actions.togglePopover(pill.id)}
                  ref={triggerRefs[pill.id]}
                  size="xs"
                  type="button"
                  variant="secondary"
                >
                  <span className="font-mono text-[0.66rem] font-bold leading-none text-inherit">
                    {text}
                  </span>
                </Button>
              );
            })}
          </div>
        ) : null}
      </div>
      <div className="flex flex-wrap items-center justify-end gap-1 max-[980px]:justify-start">
        <div className="flex min-h-6 items-center gap-2">
          <div className="inline-flex items-center gap-1">
            <Button
              aria-label="Previous case"
              className="size-6 rounded-none"
              disabled={filteredIndex <= 0 || !!state.busy}
              onClick={() => actions.stepCase(-1)}
              size="icon-xs"
              title="Previous case"
              type="button"
              variant="outline"
            >
              <ChevronLeft aria-hidden strokeWidth={1.8} />
            </Button>
            <Button
              aria-label="Next case"
              className="size-6 rounded-none"
              disabled={
                filteredIndex < 0 || filteredIndex >= filteredCatalog.length - 1 || !!state.busy
              }
              onClick={() => actions.stepCase(1)}
              size="icon-xs"
              title="Next case"
              type="button"
              variant="outline"
            >
              <ChevronRight aria-hidden strokeWidth={1.8} />
            </Button>
          </div>
          <div className="inline-flex min-h-6 items-center font-mono text-[0.78rem] font-semibold leading-none text-foreground">
            {filteredIndex >= 0
              ? `${filteredIndex + 1}/${filteredCatalog.length}`
              : `1/${state.catalog.length}`}
          </div>
        </div>
      </div>
    </div>
  );
}
