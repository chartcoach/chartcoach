import { ThreadPrimitive } from "@assistant-ui/react";
import type { ReactNode } from "react";
import * as stylex from "@stylexjs/stylex";
import { colors, media, emptyThreadScope, motionScope } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

const styles = stylex.create({
  shell: {
    position: "relative",
    flexGrow: { default: 1, [stylex.when.ancestor('[data-empty="true"]', emptyThreadScope)]: 0 },
    flexShrink: 1,
    flexBasis: {
      default: "0%",
      [stylex.when.ancestor('[data-empty="true"]', emptyThreadScope)]: "auto",
    },
    minHeight: 0,
  },
  viewport: {
    position: "relative",
    width: "100%",
    height: "100%",
    overflowY: "auto",
    overscrollBehaviorY: "contain",
    scrollbarWidth: "thin",
    scrollbarGutter: { default: "stable both-edges", [media.mobile]: "auto" },
    scrollbarColor: `${colors.scrollThumb} transparent`,
    paddingTop: { default: 32, [media.mobile]: 24 },
    paddingBottom: {
      default: 32,
      [media.mobile]: 24,
      [stylex.when.ancestor('[data-empty="true"]', emptyThreadScope)]: 24,
    },
    paddingInline: { default: 24, [media.mobile]: 18 },
    outlineOffset: { default: null, ":focus-visible": -2 },
    "::-webkit-scrollbar": { width: 6 },
    "::-webkit-scrollbar-track": { backgroundColor: "transparent" },
    "::-webkit-scrollbar-thumb": { backgroundColor: colors.scrollThumb, borderRadius: 3 },
  },
  content: { width: "min(100%, 672px)", marginInline: "auto", position: "relative" },
});

export function Conversation({ children }: { children: ReactNode }) {
  return (
    <div {...stylex.props(styles.shell)}>
      <ThreadPrimitive.Viewport
        {...stylex.props(ui.focus, styles.viewport, motionScope)}
        role="region"
        aria-label="Conversation"
        tabIndex={0}
        turnAnchor="top"
      >
        <div {...stylex.props(styles.content)}>{children}</div>
      </ThreadPrimitive.Viewport>
    </div>
  );
}
