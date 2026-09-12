import * as stylex from "@stylexjs/stylex";

const DARK = "@media (prefers-color-scheme: dark)";

export const colors = stylex.defineVars({
  background: { default: "#ffffff", [DARK]: "#111113" },
  foreground: { default: "#202023", [DARK]: "#ededee" },
  surface: { default: "#ffffff", [DARK]: "#1b1b1e" },
  navigation: { default: "#f6f6f7", [DARK]: "#171719" },
  border: { default: "#e7e7ea", [DARK]: "#303035" },
  muted: { default: "#686870", [DARK]: "#aaaab3" },
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
  chatWide: "@container chat (min-width: 960px)",
  catalogWide: "@container chat (min-width: 760px)",
  navigationDesktop: "@media (min-width: 1100px)",
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

export const historyRowScope = stylex.defineMarker();
