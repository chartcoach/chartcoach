import { ListTree } from "lucide-react";
import * as stylex from "@stylexjs/stylex";
import { progressLabels, type ProgressPhase } from "../../chat/progress";
import { LoadingMark } from "../ui/loading-mark";
import { media, motion } from "../ui/tokens.stylex";

export function ProgressLabel({ phase }: { phase: ProgressPhase }) {
  return (
    <span {...stylex.props(styles.label)}>
      {Object.entries(progressLabels).map(([key, label]) => (
        <span
          key={key}
          aria-hidden={key !== phase}
          {...stylex.props(styles.text, key === phase && styles.visible)}
        >
          {label}
        </span>
      ))}
    </span>
  );
}

export function ProgressMark({ running }: { running: boolean }) {
  return (
    <span {...stylex.props(styles.mark)} aria-hidden="true">
      <span {...stylex.props(styles.layer, !running && styles.hidden)}>
        <LoadingMark active={running} />
      </span>
      <ListTree size={16} {...stylex.props(styles.layer, running && styles.hidden)} />
    </span>
  );
}

const styles = stylex.create({
  label: { display: "grid", minWidth: 0, overflow: "hidden", lineHeight: "20px" },
  text: {
    gridArea: "1 / 1",
    opacity: 0,
    visibility: "hidden",
    transform: "translateY(-3px)",
    whiteSpace: "nowrap",
    overflow: "hidden",
    textOverflow: "ellipsis",
    transitionProperty: "opacity, transform, visibility",
    transitionDuration: { default: "220ms", [media.reducedMotion]: "0ms" },
    transitionTimingFunction: motion.easeOut,
  },
  visible: { opacity: 1, visibility: "visible", transform: "translateY(0)" },
  mark: { width: 24, height: 24, display: "grid", placeItems: "center", flexShrink: 0 },
  layer: {
    gridArea: "1 / 1",
    display: "flex",
    opacity: 1,
    transitionProperty: "opacity",
    transitionDuration: { default: "220ms", [media.reducedMotion]: "0ms" },
    transitionTimingFunction: motion.easeOut,
  },
  hidden: { opacity: 0 },
});
