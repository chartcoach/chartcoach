import * as stylex from "@stylexjs/stylex";

const DARK = "@media (prefers-color-scheme: dark)";

export const colors = stylex.defineVars({
  background: { default: "#fafafa", [DARK]: "#0a0a0a" },
  foreground: { default: "#171717", [DARK]: "#ededed" },
  surface: { default: "#ffffff", [DARK]: "#141414" },
  border: { default: "#e5e5e5", [DARK]: "#333333" },
  muted: { default: "#666666", [DARK]: "#a1a1a1" },
  accent: { default: "var(--brand-crimson)", [DARK]: "var(--brand-crimson-bright)" },
  accentText: {
    default: "color-mix(in srgb, var(--brand-crimson) 85%, #000)",
    [DARK]: "var(--brand-crimson-bright)",
  },
  scrollThumb: { default: "#8c8c8c", [DARK]: "#666666" },
  positive: { default: "#267049", [DARK]: "#85b79a" },
  caution: { default: "#856016", [DARK]: "#c8ae72" },
  error: { default: "#b3261e", [DARK]: "#ffa49c" },
});

export const media = stylex.defineConsts({
  dark: DARK,
  mobile: "@media (max-width: 520px)",
  narrow: "@media (max-width: 1099px)",
  desktop: "@media (min-width: 1100px), (min-width: 720px) and (max-height: 600px)",
  short: "@media (max-height: 620px)",
  shortNarrow: "@media (max-width: 719px) and (max-height: 600px)",
  hover: "@media (hover: hover) and (pointer: fine)",
  reducedMotion: "@media (prefers-reduced-motion: reduce)",
});

export const motion = stylex.defineConsts({
  easeOut: "cubic-bezier(0.23, 1, 0.32, 1)",
  disclosure: "200ms",
  control: "160ms",
});

export const motionScope = stylex.defineMarker();
export const disclosureScope = stylex.defineMarker();
export const emptyThreadScope = stylex.defineMarker();
