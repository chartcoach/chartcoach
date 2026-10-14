import * as stylex from "@stylexjs/stylex";
import { colors, media } from "../ui/tokens.stylex";

export const styles = stylex.create({
  skip: {
    position: "fixed",
    top: 8,
    left: 8,
    zIndex: 10,
    padding: 12,
    backgroundColor: colors.surface,
    color: colors.foreground,
    transform: { default: "translateY(-160%)", ":focus": "translateY(0)" },
  },
  header: {
    viewTransitionName: "workspace-header",
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    paddingTop: {
      default: "max(10px, env(safe-area-inset-top))",
      [media.short]: "max(8px, env(safe-area-inset-top))",
      [media.mobile]: {
        default: "max(12px, env(safe-area-inset-top))",
        [media.short]: "max(8px, env(safe-area-inset-top))",
      },
    },
    paddingBottom: {
      default: 10,
      [media.short]: 8,
      [media.mobile]: { default: 12, [media.short]: 8 },
    },
    paddingRight: { default: 0, [media.navigationDesktop]: 24 },
    flexShrink: 0,
  },
  headerWithSidebar: {
    backgroundImage: {
      default: null,
      [media.navigationDesktop]: `linear-gradient(to right, ${colors.navigation} 0 255px, ${colors.border} 255px 256px, ${colors.background} 256px)`,
    },
  },
  headerWithRail: {
    backgroundImage: {
      default: null,
      [media.navigationDesktop]: `linear-gradient(to right, ${colors.navigation} 0 63px, ${colors.border} 63px 64px, ${colors.background} 64px)`,
    },
  },
  settingsFallback: { padding: 32, width: "100%", maxWidth: 960, marginInline: "auto" },
  body: { display: "flex", flex: 1, minHeight: 0, minWidth: 0 },
  canvas: {
    flex: 1,
    minWidth: 0,
    minHeight: 0,
    display: "flex",
    containerType: "inline-size",
    containerName: "chat",
  },
  main: { flexGrow: 1, minHeight: 0, display: "flex", flexDirection: "column", minWidth: 0 },
  workspace: {
    display: "grid",
    gridTemplateRows: { default: "auto minmax(0, 1fr)", [media.chatWide]: "minmax(0, 1fr)" },
    flexGrow: 1,
    minHeight: 0,
    minWidth: 0,
  },
  withEvidence: {
    gridTemplateColumns: {
      default: null,
      [media.chatWide]: "minmax(0, 1fr) clamp(360px, 32cqw, 420px)",
    },
  },
  thread: {
    display: "flex",
    flexDirection: "column",
    minHeight: 0,
    minWidth: 0,
    gridRow: { default: "2", [media.chatWide]: "1" },
    gridColumn: { default: null, [media.chatWide]: "1" },
  },
  emptyThread: {
    gridRow: 1,
    justifyContent: { default: null, [media.spacious]: "center" },
    paddingBottom: { default: null, [media.spacious]: "12vh" },
  },
  // The example chips follow the composer in DOM order, so keyboard focus reaches the
  // message box first. Compact layouts draw the chips above the composer.
  composer: { flexShrink: 0, order: { default: null, [media.compact]: 1 } },
  emptyWorkspace: { gridTemplateRows: "minmax(0, 1fr)" },
  welcome: { width: "100%", maxWidth: 672, marginInline: "auto", paddingBlock: 24 },
  lockup: {
    display: "flex",
    flexDirection: { default: "row", [media.mobile]: "column" },
    alignItems: "center",
    justifyContent: "center",
    gap: { default: 14, [media.mobile]: 18 },
    marginBottom: 12,
  },
  title: {
    fontSize: { default: "clamp(32px, 3.5vw, 40px)", [media.compact]: 28 },
    fontWeight: 500,
    lineHeight: 1.12,
    letterSpacing: "-0.045em",
    textWrap: "balance",
    textAlign: "center",
    margin: 0,
  },
  accent: { color: colors.accent },
  intro: {
    maxWidth: { default: 540, [media.mobile]: 280 },
    color: colors.muted,
    lineHeight: 1.65,
    fontSize: { default: 16, [media.mobile]: 14 },
    textWrap: "balance",
    textAlign: "center",
    marginInline: "auto",
    marginBlock: 0,
    display: { default: null, [media.landscape]: "none" },
  },
  messages: { maxWidth: 672, marginInline: "auto" },
  status: { maxWidth: 672, marginBlock: 12, marginInline: "auto" },
});
