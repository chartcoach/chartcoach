import { ThreadPrimitive, useAuiEvent } from "@assistant-ui/react";
import { ArrowDown } from "lucide-react";
import type { ReactNode } from "react";
import * as stylex from "@stylexjs/stylex";
import { colors, media } from "../ui/tokens.stylex";
import { useContentScroll } from "../../chat/use-content-scroll";
import { ui } from "../ui/ui";

const styles = stylex.create({
  shell: {
    position: "relative",
    flexGrow: 1,
    flexShrink: 1,
    flexBasis: "0%",
    minHeight: 0,
  },
  viewport: {
    position: "relative",
    width: "100%",
    height: "100%",
    overflowY: "auto",
    overscrollBehaviorY: "contain",
    overflowAnchor: "none",
    scrollbarWidth: "thin",
    scrollbarGutter: { default: "stable both-edges", [media.mobile]: "auto" },
    scrollbarColor: `${colors.scrollThumb} transparent`,
    paddingTop: { default: 32, [media.mobile]: 24 },
    paddingBottom: {
      default: 32,
      [media.mobile]: 24,
    },
    paddingInline: { default: 24, [media.mobile]: 18 },
    outlineOffset: { default: null, ":focus-visible": -2 },
    "::-webkit-scrollbar": { width: 6 },
    "::-webkit-scrollbar-track": { backgroundColor: "transparent" },
    "::-webkit-scrollbar-thumb": { backgroundColor: colors.scrollThumb, borderRadius: 3 },
  },
  content: { width: "min(100%, 672px)", marginInline: "auto", position: "relative" },
  welcome: {
    minHeight: "100%",
    display: "flex",
    flexDirection: "column",
    justifyContent: "safe center",
  },
  latest: {
    position: "absolute",
    bottom: 12,
    left: "50%",
    translate: "-50% 0",
    gap: 8,
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: colors.border,
    borderRadius: 24,
    boxShadow: "0 2px 12px #00000012",
    fontSize: 12,
    paddingInline: 14,
  },
});

export function Conversation({ empty, children }: { empty: boolean; children: ReactNode }) {
  const { viewportRef, atLatest, scrollToLatest } = useContentScroll("bottom", !empty);
  useAuiEvent("thread.runStart", scrollToLatest);

  return (
    <div {...stylex.props(styles.shell)}>
      <ThreadPrimitive.Viewport
        {...stylex.props(ui.focus, styles.viewport)}
        ref={viewportRef}
        role="region"
        aria-label="Conversation"
        tabIndex={0}
        autoScroll={false}
        scrollToBottomOnRunStart={false}
        scrollToBottomOnInitialize={false}
        scrollToBottomOnThreadSwitch={false}
      >
        <div {...stylex.props(styles.content, empty && styles.welcome)}>{children}</div>
      </ThreadPrimitive.Viewport>
      {!empty && !atLatest ? (
        <button
          {...stylex.props(ui.button, ui.focus, ui.appear, styles.latest)}
          onClick={scrollToLatest}
        >
          <ArrowDown size={14} aria-hidden="true" /> Latest response
        </button>
      ) : null}
    </div>
  );
}
