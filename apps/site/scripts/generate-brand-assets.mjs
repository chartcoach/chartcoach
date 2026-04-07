import { mkdir, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import sharp from "sharp";

import { renderChartCoachFaviconSvg } from "../../../packages/ui/src/lib/chartcoach-marimekko.ts";

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

await Promise.all([
  writeTextFile(resolve(siteRoot, "public/brand/chartcoach-favicon.svg"), faviconSvg),
  writeTextFile(resolve(siteRoot, "public/favicon.svg"), faviconSvg),
  writePng(resolve(siteRoot, "public/brand/chartcoach-favicon.png"), faviconSvg, 512, 512),
]);

console.log("Generated structured visualization design knowledge assets:");
console.log("- public/brand/chartcoach-favicon.svg");
console.log("- public/brand/chartcoach-favicon.png");
console.log("- public/favicon.svg");
