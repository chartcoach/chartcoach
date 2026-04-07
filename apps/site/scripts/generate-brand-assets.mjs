import { mkdir, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import sharp from "sharp";

import {
  renderChartCoachFaviconSvg,
  renderChartCoachShareCardSvg,
} from "../../../packages/ui/src/lib/chartcoach-marimekko.ts";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const siteRoot = resolve(scriptDir, "..");

async function writeTextFile(path, content) {
  await mkdir(dirname(path), { recursive: true });
  await writeFile(path, content, "utf8");
}

async function writePng(path, svg, width, height) {
  await mkdir(dirname(path), { recursive: true });
  await sharp(Buffer.from(svg)).resize(width, height).png().toFile(path);
}

const faviconSvg = renderChartCoachFaviconSvg("light");
const defaultShareSvg = renderChartCoachShareCardSvg({
  theme: "light",
  title: "Structured visualization\ndesign knowledge",
  tagline: "For grounding generative reasoning in explicit, inspectable guidance.",
});
const guidelinesShareSvg = renderChartCoachShareCardSvg({
  theme: "light",
  title: "Structured visualization\nguidance",
  tagline: "Browse concise recommendations with context, labels, citations, and structured evidence.",
});

await Promise.all([
  writeTextFile(resolve(siteRoot, "public/brand/chartcoach-favicon.svg"), faviconSvg),
  writeTextFile(resolve(siteRoot, "public/favicon.svg"), faviconSvg),
  writePng(resolve(siteRoot, "public/brand/chartcoach-favicon.png"), faviconSvg, 512, 512),
  writeTextFile(resolve(siteRoot, "public/social/chartcoach-share-default.svg"), defaultShareSvg),
  writeTextFile(resolve(siteRoot, "public/social/chartcoach-share-guidelines.svg"), guidelinesShareSvg),
  writePng(resolve(siteRoot, "public/social/chartcoach-share-default.png"), defaultShareSvg, 1200, 630),
  writePng(resolve(siteRoot, "public/social/chartcoach-share-guidelines.png"), guidelinesShareSvg, 1200, 630),
]);

console.log("Generated structured visualization design knowledge assets:");
console.log("- public/brand/chartcoach-favicon.svg");
console.log("- public/brand/chartcoach-favicon.png");
console.log("- public/favicon.svg");
console.log("- public/social/chartcoach-share-default.svg");
console.log("- public/social/chartcoach-share-default.png");
console.log("- public/social/chartcoach-share-guidelines.svg");
console.log("- public/social/chartcoach-share-guidelines.png");
