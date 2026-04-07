import clsx from "clsx";
import type { ViewerActions, ViewerState } from "../contract/types";
import { ViewerSelectField } from "./control-fields";
import { fromOptionValue, toOptionValue } from "./utils";

export function LayoutPopover({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const overview = state.overview;
  if (!overview || !overview.ui_schema.layout_controls.length) {
    return null;
  }
  const layoutControls = overview.ui_schema.layout_controls;

  return (
    <section className={clsx("grid min-w-0 gap-3", state.activePopoverId !== "layout" && "hidden")}>
      <div className="font-mono text-[0.72rem] font-bold lowercase tracking-[0.02em] text-muted-foreground">
        Layout
      </div>
      <div className="grid min-w-0 gap-3">
        {layoutControls.map((control) => (
          <ViewerSelectField
            key={control.id}
            label={control.label}
            onValueChange={(value) => actions.changeLayout(control.id, fromOptionValue(value))}
            options={control.options}
            value={toOptionValue(control.value)}
          />
        ))}
      </div>
    </section>
  );
}
