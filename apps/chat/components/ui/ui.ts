import * as stylex from "@stylexjs/stylex";
import { colors, media, motion, motionScope } from "./tokens.stylex";

export const ui = stylex.create({
  srOnly: {
    position: "absolute",
    width: 1,
    height: 1,
    padding: 0,
    margin: -1,
    overflow: "hidden",
    clipPath: "inset(50%)",
    whiteSpace: "nowrap",
    borderWidth: 0,
  },
  focus: {
    outlineWidth: { default: null, ":focus-visible": 2 },
    outlineStyle: { default: null, ":focus-visible": "solid" },
    outlineColor: { default: null, ":focus-visible": colors.accent },
    outlineOffset: { default: null, ":focus-visible": 4 },
  },
  button: {
    cursor: { default: "pointer", ":disabled": "default" },
    opacity: { default: 1, ":disabled": 0.45 },
    WebkitTapHighlightColor: "transparent",
  },
  quietButton: {
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    gap: 7,
    backgroundColor: {
      default: "transparent",
      ":hover:enabled": { default: null, [media.hover]: colors.border },
    },
    borderWidth: 0,
    borderRadius: 6,
    color: {
      default: colors.muted,
      ":hover:enabled": { default: null, [media.hover]: colors.foreground },
    },
    minHeight: 44,
    minWidth: 44,
    padding: 8,
    fontSize: 14,
  },
  icon: { flexShrink: 0 },
  error: {
    overflowWrap: "anywhere",
    color: colors.error,
    fontSize: 13,
    lineHeight: 1.5,
    marginTop: 10,
  },
  activity: {
    display: "flex",
    alignItems: "center",
    gap: 8,
    fontSize: 13,
    color: colors.muted,
    marginBlock: 8,
  },
  chevron: {
    flexShrink: 0,
    transitionProperty: "transform",
    transitionTimingFunction: motion.easeOut,
    transitionDuration: {
      default: motion.control,
      [media.reducedMotion]: "0ms",
      [stylex.when.ancestor(":has(:focus-visible)", motionScope)]: "0ms",
    },
  },
  mono: { fontFamily: "var(--font-geist-mono), monospace" },
});
