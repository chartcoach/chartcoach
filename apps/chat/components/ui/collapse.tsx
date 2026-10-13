import type { ReactNode } from "react";
import * as stylex from "@stylexjs/stylex";
import { media, motion } from "./tokens.stylex";

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
    },
  },
  live: {
    transitionTimingFunction: motion.fluid,
    transitionDuration: {
      default: motion.move,
      [media.reducedMotion]: "0ms",
    },
  },
  open: { gridTemplateRows: "1fr", opacity: 1 },
  content: { minHeight: 0, overflow: "hidden" },
});

/**
 * Expands and collapses its content. Disclosures respond to the reader at once;
 * `live` content that the app updates on its own settles in one continuous movement.
 */
export function Collapse({
  open,
  live = false,
  children,
  id,
}: {
  open: boolean;
  live?: boolean;
  children: ReactNode;
  id?: string;
}) {
  return (
    <div
      id={id}
      {...stylex.props(styles.root, live && styles.live, open && styles.open)}
      data-open={open}
      aria-hidden={!open}
      inert={!open}
    >
      <div {...stylex.props(styles.content)}>{children}</div>
    </div>
  );
}
