import { readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { brandCssColorTokens } from "../src/colors.ts";
import { packageRoot } from "./public-brand-assets.mjs";

const check = process.argv.includes("--check");
const outputPath = join(packageRoot, "styles", "tokens.css");

const renderVarLines = (tokens) =>
  Object.entries(tokens)
    .map(([name, value]) => `  ${name}: ${value};`)
    .join("\n");

const css = `@theme static {
${renderVarLines(brandCssColorTokens.light)}

  --font-sans:
    "Poppins", -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu",
    "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
  --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;

  --container-content: 72rem;
}

.dark {
${renderVarLines(brandCssColorTokens.dark)}
}
`;

const existing = await readFile(outputPath, "utf8").catch(() => undefined);

if (check) {
  if (existing !== css) {
    console.error("stale CSS tokens: styles/tokens.css");
    console.error("Run `pnpm --dir packages/brand render:tokens`.");
    process.exitCode = 1;
  } else {
    console.log("generated CSS tokens are current");
  }
} else if (existing !== css) {
  await writeFile(outputPath, css);
  console.log("rendered styles/tokens.css");
}
