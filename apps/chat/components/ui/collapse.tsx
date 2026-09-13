import type { ReactNode } from "react";
import * as stylex from "@stylexjs/stylex";
import { media, motion, motionScope } from "./tokens.stylex";

const styles = stylex.create({
  root: {
    display: "grid",
    gridTemplateRows: "0fr",
    opacity: 0,
    transitionProperty: "grid-template-rows, opacity",
    transitionTimingFunction: motion.easeOut,
    transitionDuration: {
      default: motion.disclosure,
      [media.reducedMotion]: "0ms",
      [stylex.when.ancestor(":has(:focus-visible)", motionScope)]: "0ms",
    },
  },
  open: { gridTemplateRows: "1fr", opacity: 1 },
  content: { minHeight: 0, overflow: "hidden" },
});

export function Collapse({
  open,
  children,
  id,
}: {
  open: boolean;
  children: ReactNode;
  id?: string;
}) {
  return (
    <div
      id={id}
      {...stylex.props(styles.root, open && styles.open)}
      data-open={open}
      aria-hidden={!open}
      inert={!open}
    >
      <div {...stylex.props(styles.content)}>{children}</div>
    </div>
  );
}
