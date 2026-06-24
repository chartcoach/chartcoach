import { readFileSync } from "node:fs";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const horizontalLogoSvg = readFileSync(
  require.resolve("@chartcoach/brand/assets/brand/chartcoach-horizontal.svg"),
  "utf-8",
);
const wordmarkMatch = horizontalLogoSvg.match(/<path[^>]* d="([^"]+)"/);

if (!wordmarkMatch) {
  throw new Error("Could not extract the chartcoach wordmark path from the brand SVG.");
}

export const CHARTCOACH_WORDMARK_PATH = wordmarkMatch[1];
export const DASH_RING_BASE_ROTATIONS = [
  140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340,
] as const;
export const DASH_RING_ACCENT_ROTATIONS = [0, 20, 40] as const;
