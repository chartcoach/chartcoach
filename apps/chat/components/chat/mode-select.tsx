import { ChevronDown } from "lucide-react";
import * as stylex from "@stylexjs/stylex";
import { modeSchema, modes, type Mode } from "../../shared/workflow";
import { colors } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

export function ModeSelect({
  value,
  onChange,
  disabled,
}: {
  value: Mode;
  onChange: (mode: Mode) => void;
  disabled: boolean;
}) {
  return (
    <label {...stylex.props(styles.root)}>
      <span {...stylex.props(ui.srOnly)}>How ChartCoach helps</span>
      <select
        {...stylex.props(ui.focus, styles.select)}
        value={value}
        disabled={disabled}
        title={modes[value].description}
        onChange={(event) => onChange(modeSchema.parse(event.target.value))}
      >
        {modeSchema.options.map((mode) => (
          <option key={mode} value={mode}>
            {modes[mode].label}
          </option>
        ))}
      </select>
      <ChevronDown size={13} {...stylex.props(styles.icon)} aria-hidden="true" />
    </label>
  );
}

const styles = stylex.create({
  root: {
    gridArea: "mode",
    justifySelf: "start",
    position: "relative",
    display: "inline-flex",
    flexShrink: 0,
  },
  select: {
    appearance: "none",
    fieldSizing: "content",
    minHeight: 44,
    paddingLeft: 10,
    paddingRight: 27,
    borderWidth: 0,
    borderRadius: 4,
    backgroundColor: "transparent",
    color: colors.muted,
    fontSize: 13,
    cursor: "pointer",
    maxWidth: 125,
  },
  icon: { position: "absolute", right: 8, top: 16, pointerEvents: "none", color: colors.muted },
});
