export type ChartCoachTheme = "light" | "dark" | "auto";
export type ChartCoachMarkMode = "static" | "hero-loop";
export type ChartCoachMarkPose = "start" | "end";

type Tone = "strong" | "mid" | "soft" | "faint";

type RectState = {
  x: number;
  y: number;
  width: number;
  height: number;
  rx: number;
};

type BlockState = {
  id: string;
  tone: Tone;
  start: RectState;
  end: RectState;
};

type Palette = Record<Tone, string>;

const HERO_KEY_TIMES = "0;0.2;0.6;0.8;1";
const HERO_KEY_SPLINES = [
  "0.65 0 0.35 1",
  "0.65 0 0.35 1",
  "0.65 0 0.35 1",
  "0.65 0 0.35 1",
].join(";");
const blockStates: BlockState[] = [
  {
    id: "1",
    tone: "strong",
    start: { x: 10, y: 10, width: 40, height: 15, rx: 1 },
    end: { x: 10, y: 20, width: 80, height: 16, rx: 3 },
  },
  {
    id: "2",
    tone: "strong",
    start: { x: 54, y: 10, width: 36, height: 15, rx: 1 },
    end: { x: 10, y: 20, width: 80, height: 16, rx: 3 },
  },
  {
    id: "3",
    tone: "strong",
    start: { x: 10, y: 29, width: 80, height: 9, rx: 1 },
    end: { x: 10, y: 20, width: 80, height: 16, rx: 3 },
  },
  {
    id: "4",
    tone: "mid",
    start: { x: 10, y: 42, width: 20, height: 16, rx: 1 },
    end: { x: 10, y: 42, width: 38, height: 16, rx: 3 },
  },
  {
    id: "5",
    tone: "mid",
    start: { x: 34, y: 42, width: 14, height: 16, rx: 1 },
    end: { x: 10, y: 42, width: 38, height: 16, rx: 3 },
  },
  {
    id: "6",
    tone: "soft",
    start: { x: 52, y: 42, width: 38, height: 16, rx: 1 },
    end: { x: 52, y: 42, width: 38, height: 16, rx: 3 },
  },
  {
    id: "7",
    tone: "faint",
    start: { x: 10, y: 62, width: 50, height: 28, rx: 1 },
    end: { x: 10, y: 64, width: 80, height: 10, rx: 2 },
  },
  {
    id: "8",
    tone: "faint",
    start: { x: 64, y: 62, width: 26, height: 28, rx: 1 },
    end: { x: 10, y: 64, width: 80, height: 10, rx: 2 },
  },
];

const palettes: Record<ChartCoachTheme, Palette> = {
  light: {
    strong: "#2b241f",
    mid: "#8f6f50",
    soft: "#ab9277",
    faint: "#d9d2c7",
  },
  dark: {
    strong: "#f3ece2",
    mid: "#dcc6a5",
    soft: "#ab9985",
    faint: "#4d433b",
  },
  auto: {
    strong: "var(--cc-brand-high, #2b241f)",
    mid: "var(--cc-brand, #8f6f50)",
    soft: "var(--cc-brand-ink, #ab9277)",
    faint: "var(--ccui-border, #d9d2c7)",
  },
};

export type ChartCoachMarimekkoSvgOptions = {
  mode?: ChartCoachMarkMode;
  pose?: ChartCoachMarkPose;
  theme?: ChartCoachTheme;
  title?: string;
  idPrefix?: string;
  className?: string;
};

export type ChartCoachShareCardSvgOptions = {
  theme?: Exclude<ChartCoachTheme, "auto">;
  title?: string;
  tagline?: string;
};

function escapeAttribute(value: string) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll('"', "&quot;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function rectAttributes(state: RectState) {
  return `x="${state.x}" y="${state.y}" width="${state.width}" height="${state.height}" rx="${state.rx}"`;
}

function rectStateDataAttributes(block: BlockState) {
  return [
    `data-start-x="${block.start.x}"`,
    `data-start-y="${block.start.y}"`,
    `data-start-width="${block.start.width}"`,
    `data-start-height="${block.start.height}"`,
    `data-start-rx="${block.start.rx}"`,
    `data-end-x="${block.end.x}"`,
    `data-end-y="${block.end.y}"`,
    `data-end-width="${block.end.width}"`,
    `data-end-height="${block.end.height}"`,
    `data-end-rx="${block.end.rx}"`,
  ].join(" ");
}

function staticBlockRects(theme: ChartCoachTheme, pose: ChartCoachMarkPose) {
  return blockStates
    .map((block) => {
      const state = pose === "start" ? block.start : block.end;
      return `<rect ${rectAttributes(state)} fill="${palettes[theme][block.tone]}" />`;
    })
    .join("");
}

function animateAttributeMarkup({
  attribute,
  values,
  duration,
  begin,
  keyTimes,
  keySplines,
  repeatCount,
}: {
  attribute: keyof RectState;
  values: string;
  duration: string;
  begin?: string;
  keyTimes?: string;
  keySplines?: string;
  repeatCount?: string;
}) {
  const parts = [
    `<animate attributeName="${attribute}" values="${values}" dur="${duration}" fill="freeze"`,
  ];

  if (begin) parts.push(` begin="${begin}"`);
  if (repeatCount) parts.push(` repeatCount="${repeatCount}"`);
  if (keyTimes) parts.push(` keyTimes="${keyTimes}" calcMode="spline"`);
  if (keySplines) parts.push(` keySplines="${keySplines}"`);

  parts.push(" />");
  return parts.join("");
}

function blockMarkup(block: BlockState, options: Required<Pick<ChartCoachMarimekkoSvgOptions, "mode" | "pose" | "theme" | "idPrefix">>) {
  const palette = palettes[options.theme];
  const baseState =
    options.mode === "hero-loop"
      ? block.start
      : options.pose === "start"
        ? block.start
        : block.end;

  const animations: string[] = [];

  if (options.mode === "hero-loop") {
    (Object.keys(block.start) as (keyof RectState)[]).forEach((attribute) => {
      const start = block.start[attribute];
      const end = block.end[attribute];
      animations.push(
        animateAttributeMarkup({
          attribute,
          values: `${start};${end};${end};${start};${start}`,
          duration: "8s",
          begin: "0s",
          keyTimes: HERO_KEY_TIMES,
          keySplines: HERO_KEY_SPLINES,
          repeatCount: "indefinite",
        }),
      );
    });
  }

  return `<rect ${rectAttributes(baseState)} fill="${palette[block.tone]}" data-cc-block="${block.id}" ${rectStateDataAttributes(block)}>${animations.join("")}</rect>`;
}

function svgScaffold({
  body,
  title,
  idPrefix,
  className,
  viewBox = "0 0 100 100",
}: {
  body: string;
  title?: string;
  idPrefix: string;
  className?: string;
  viewBox?: string;
}) {
  const classAttr = className ? ` class="${escapeAttribute(className)}"` : "";
  const ariaAttrs = title
    ? `role="img" aria-labelledby="${idPrefix}-title"`
    : 'aria-hidden="true" role="presentation"';
  const labelledTitle = title
    ? `<title id="${idPrefix}-title">${escapeAttribute(title)}</title>`
    : "";

  return `<svg xmlns="http://www.w3.org/2000/svg" id="${idPrefix}-svg" viewBox="${viewBox}" fill="none" ${ariaAttrs}${classAttr} preserveAspectRatio="xMidYMid meet" style="display:block;width:100%;height:auto">${labelledTitle}${body}</svg>`;
}

export function renderChartCoachMarimekkoSvg({
  mode = "static",
  pose = "end",
  theme = "auto",
  title,
  idPrefix = "cc-marimekko",
  className,
}: ChartCoachMarimekkoSvgOptions = {}) {
  return svgScaffold({
    body: blockStates.map((block) => blockMarkup(block, { mode, pose, theme, idPrefix })).join(""),
    title,
    idPrefix,
    className,
  });
}

export function renderChartCoachFaviconSvg(theme: Exclude<ChartCoachTheme, "auto"> = "light") {
  const background = theme === "dark" ? "#17181b" : "#f7f4ee";
  const border = theme === "dark" ? "#343840" : "#d9d2c7";
  const mark = staticBlockRects(theme, "end");

  return svgScaffold({
    idPrefix: `cc-favicon-${theme}`,
    viewBox: "0 0 128 128",
    body: `<rect x="8" y="8" width="112" height="112" rx="28" fill="${background}" stroke="${border}" /><g transform="translate(14 14) scale(1)">${mark}</g>`,
    title: "Structured visualization design knowledge",
  });
}

export function renderChartCoachShareCardSvg({
  theme = "light",
  title = "Structured visualization\ndesign knowledge",
  tagline = "For grounding generative reasoning in explicit, inspectable guidance.",
}: ChartCoachShareCardSvgOptions = {}) {
  const background = theme === "dark" ? "#17181b" : "#f7f4ee";
  const panel = theme === "dark" ? "#1d1f23" : "#efebe4";
  const border = theme === "dark" ? "#343840" : "#d9d2c7";
  const titleColor = theme === "dark" ? "#f3ece2" : "#2b241f";
  const taglineColor = theme === "dark" ? "#c8beb2" : "#5d564e";
  const mark = staticBlockRects(theme, "end");
  const titleLines = title.split("\n");
  const titleMarkup = titleLines
    .map((line, index) => {
      const dy = index === 0 ? "0" : "72";
      return `<tspan x="96" dy="${dy}">${escapeAttribute(line)}</tspan>`;
    })
    .join("");
  const titleStartY = titleLines.length > 1 ? 188 : 230;
  const taglineY = titleLines.length > 1 ? 344 : 304;

  return svgScaffold({
    idPrefix: `cc-share-card-${theme}`,
    viewBox: "0 0 1200 630",
    title,
    body: `
      <rect x="0" y="0" width="1200" height="630" fill="${background}" />
      <rect x="44" y="44" width="1112" height="542" rx="28" fill="${panel}" stroke="${border}" />
      <g transform="translate(690 130) scale(3.65)">${mark}</g>
      <text x="96" y="${titleStartY}" fill="${titleColor}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="68" font-weight="700">${titleMarkup}</text>
      <text x="96" y="${taglineY}" fill="${taglineColor}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="30">${escapeAttribute(tagline)}</text>
      <text x="96" y="520" fill="${taglineColor}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="24">Grounded · Structured · Citable</text>
    `.replace(/\s+/g, " "),
  });
}
