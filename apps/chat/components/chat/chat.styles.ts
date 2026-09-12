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
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    paddingBlock: {
      default: 10,
      [media.short]: 8,
      [media.mobile]: { default: 12, [media.short]: 8 },
    },
    paddingRight: { default: 24, [media.mobile]: 12 },
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
  empty: {
    justifyContent: "safe center",
    overflowY: "hidden",
    paddingBottom: 0,
  },
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
  emptyThread: { justifyContent: "flex-start" },
  emptyWorkspace: {
    flexGrow: 0,
    flexShrink: 1,
    gridTemplateRows: "minmax(0, 1fr)",
    minHeight: 0,
    maxHeight: "100%",
  },
  welcome: { maxWidth: 672, marginInline: "auto" },
  title: {
    maxWidth: 600,
    fontSize: "clamp(30px, 3.5vw, 42px)",
    fontWeight: 500,
    lineHeight: 1.12,
    letterSpacing: "-0.045em",
    textWrap: "balance",
    marginTop: 0,
    marginBottom: 12,
  },
  accent: { color: colors.accent },
  intro: { maxWidth: 540, color: colors.muted, lineHeight: 1.65, fontSize: 16, margin: 0 },
  messages: { maxWidth: 672, marginInline: "auto" },
  status: { maxWidth: 672, marginBlock: 12, marginInline: "auto" },
});
