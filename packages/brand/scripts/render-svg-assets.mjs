import { readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { brandAssetTheme } from "../src/colors.ts";
import { sourceBrandDir } from "./public-brand-assets.mjs";

const check = process.argv.includes("--check");
const horizontalLogo = await readFile(join(sourceBrandDir, "chartcoach-horizontal.svg"), "utf8");
const wordmarkPath = horizontalLogo.match(/<path[^>]* d="([^"]+)"/)?.[1];

if (!wordmarkPath) {
  console.error("Could not find the chartcoach wordmark path.");
  process.exit(1);
}

const svgColor = (color) => color.toUpperCase();
const colors = {
  accent: svgColor(brandAssetTheme.accent),
  border: svgColor(brandAssetTheme.border),
  dark: svgColor(brandAssetTheme.dark),
  darkBorder: svgColor(brandAssetTheme.darkBorder),
  muted: svgColor(brandAssetTheme.muted),
  white: svgColor(brandAssetTheme.white),
};

const baseRotations = [140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340];
const accentRotations = [0, 20, 40];
const wordmarkAspect = 5741 / 749;

const formatNumber = (value) => Number(value.toFixed(3)).toString();

const dashRects = (rotations) =>
  rotations
    .map(
      (rotation) =>
        `    <rect x="47.9" y="5" width="4.2" height="13" rx="2.1" transform="rotate(${rotation} 50 50)"></rect>`,
    )
    .join("\n");

const dashGroup = (fill, rotations) => `  <g fill="${fill}">
${dashRects(rotations)}
  </g>`;

const dashRing = ({ accentColor, accentOn = true, dashColor, size, x, y }) => {
  const scale = formatNumber(size / 100);
  const rotations = accentOn ? baseRotations : [...baseRotations, ...accentRotations];
  const groups = [dashGroup(dashColor, rotations)];

  if (accentOn) groups.push(dashGroup(accentColor, accentRotations));

  return `<g transform="translate(${formatNumber(x)} ${formatNumber(y)}) scale(${scale})">
${groups.join("\n")}
</g>`;
};

const wordmark = ({ fill, width, x, y }) => {
  const scale = formatNumber(width / 5741);

  return `<g transform="translate(${formatNumber(x)} ${formatNumber(y)}) scale(${scale})" fill="${fill}">
    <path transform="translate(-37 740)" d="${wordmarkPath}"></path>
  </g>`;
};

const squareLockup = ({
  accentColor,
  accentOn,
  background,
  dashColor,
  filename,
  stroke,
  title,
  wordmarkFill,
}) => {
  const size = 512;
  const sourceSize = 207;
  const ringSize = (84 / sourceSize) * size;
  const wordmarkWidth = (138 / sourceSize) * size;
  const wordmarkHeight = wordmarkWidth / wordmarkAspect;
  const gap = (18 / sourceSize) * size;
  const stackHeight = ringSize + gap + wordmarkHeight;
  const ringX = (size - ringSize) / 2;
  const ringY = (size - stackHeight) / 2;
  const wordmarkX = (size - wordmarkWidth) / 2;
  const wordmarkY = ringY + ringSize + gap;
  const strokeWidth = stroke ? 2.5 : 0;
  const rectInset = strokeWidth / 2;
  const rect = stroke
    ? `<rect x="${rectInset}" y="${rectInset}" width="${size - strokeWidth}" height="${size - strokeWidth}" rx="15" fill="${background}" stroke="${stroke}" stroke-width="${strokeWidth}"></rect>`
    : `<rect width="${size}" height="${size}" rx="15" fill="${background}"></rect>`;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${size} ${size}" width="${size}" height="${size}" role="img" aria-label="${title}">
  <title>${title}</title>
  ${rect}
  ${dashRing({
    accentColor,
    accentOn,
    dashColor,
    size: ringSize,
    x: ringX,
    y: ringY,
  })}
  ${wordmark({
    fill: wordmarkFill,
    width: wordmarkWidth,
    x: wordmarkX,
    y: wordmarkY,
  })}
</svg>`;

  return { filename, svg };
};

const assets = [
  squareLockup({
    accentColor: colors.accent,
    accentOn: true,
    background: colors.white,
    dashColor: colors.dark,
    filename: "chartcoach-square-light.svg",
    stroke: colors.border,
    title: "chartcoach - square light logo",
    wordmarkFill: colors.dark,
  }),
  squareLockup({
    accentColor: colors.accent,
    accentOn: true,
    background: colors.muted,
    dashColor: colors.dark,
    filename: "chartcoach-square-muted.svg",
    title: "chartcoach - square muted logo",
    wordmarkFill: colors.dark,
  }),
  squareLockup({
    accentColor: colors.accent,
    accentOn: true,
    background: colors.dark,
    dashColor: colors.white,
    filename: "chartcoach-square-dark.svg",
    stroke: colors.darkBorder,
    title: "chartcoach - square dark logo",
    wordmarkFill: colors.white,
  }),
  squareLockup({
    accentColor: colors.white,
    accentOn: false,
    background: colors.accent,
    dashColor: colors.white,
    filename: "chartcoach-square-accent.svg",
    title: "chartcoach - square accent logo",
    wordmarkFill: colors.white,
  }),
];

const staleFiles = [];

for (const asset of assets) {
  const outputPath = join(sourceBrandDir, asset.filename);
  const existing = await readFile(outputPath, "utf8").catch(() => undefined);

  if (check) {
    if (existing !== asset.svg) staleFiles.push(asset.filename);
    continue;
  }

  if (existing === asset.svg) continue;

  await writeFile(outputPath, asset.svg);
  console.log(`rendered ${asset.filename}`);
}

if (check && staleFiles.length > 0) {
  console.error(`stale SVG assets: ${staleFiles.join(", ")}`);
  console.error("Run `pnpm --dir packages/brand render:svg`.");
  process.exitCode = 1;
} else if (check) {
  console.log("generated SVG brand assets are current");
}
