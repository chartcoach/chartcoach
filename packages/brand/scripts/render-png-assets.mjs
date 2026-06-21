import { readFile, readdir, writeFile } from "node:fs/promises";
import { join } from "node:path";
import sharp from "sharp";
import { sourceBrandDir } from "./public-brand-assets.mjs";

const check = process.argv.includes("--check");
const pngScale = 2;
const svgBaseDensity = 72;

const readSvgSize = (svg, filename) => {
  const width = Number(svg.match(/\bwidth="([0-9.]+)"/)?.[1]);
  const height = Number(svg.match(/\bheight="([0-9.]+)"/)?.[1]);

  if (!Number.isFinite(width) || !Number.isFinite(height)) {
    throw new Error(`${filename} must define numeric width and height attributes.`);
  }

  return { height: Math.round(height * pngScale), width: Math.round(width * pngScale) };
};

const pngAssets = (
  await Promise.all(
    (
      await readdir(sourceBrandDir)
    )
      .filter((file) => file.endsWith(".svg"))
      .sort((a, b) => a.localeCompare(b))
      .map(async (svg) => {
        const source = await readFile(join(sourceBrandDir, svg), "utf8");
        const { height, width } = readSvgSize(source, svg);

        return {
          height,
          png: svg.replace(/\.svg$/, ".png"),
          svg,
          width,
        };
      }),
  )
).sort((a, b) => a.png.localeCompare(b.png));

const renderPng = async ({ svg, width, height }) =>
  sharp(join(sourceBrandDir, svg), { density: svgBaseDensity * pngScale })
    .resize({ width, height })
    .png()
    .toBuffer();

const staleFiles = [];

for (const asset of pngAssets) {
  const outputPath = join(sourceBrandDir, asset.png);
  const rendered = await renderPng(asset);

  if (check) {
    const existing = await readFile(outputPath).catch(() => undefined);
    if (!existing?.equals(rendered)) staleFiles.push(asset.png);
    continue;
  }

  await writeFile(outputPath, rendered);
  console.log(`rendered ${asset.png} from ${asset.svg}`);
}

if (check && staleFiles.length > 0) {
  console.error(`stale PNG assets: ${staleFiles.join(", ")}`);
  console.error("Run `pnpm --dir packages/brand render:png`.");
  process.exitCode = 1;
} else if (check) {
  console.log("rendered PNG brand assets are current");
}
