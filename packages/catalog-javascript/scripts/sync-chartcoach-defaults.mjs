import { spawnSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const packageRoot = resolve(scriptDir, "..");
const repoRoot = resolve(packageRoot, "..", "..");
const outputPath = join(packageRoot, "src", "catalog", "chartcoach-defaults.ts");
const checkOnly = process.argv.includes("--check");

const python = [
  "import json",
  "from chartcoach.constants import CHARTCOACH_DEFAULTS",
  "print(json.dumps(CHARTCOACH_DEFAULTS.to_record(), indent=2, sort_keys=True))",
].join("; ");

const result = spawnSync("uv", ["run", "python", "-c", python], {
  cwd: repoRoot,
  encoding: "utf8",
});

if (result.status !== 0) {
  process.stderr.write(result.stderr || result.stdout);
  process.exit(result.status ?? 1);
}

const defaults = JSON.parse(result.stdout);
const next = [
  "export type ChartCoachDefaults = {\n",
  "  catalogArtifactBaseUrl: string;\n",
  "  catalogDigest: string;\n",
  "  catalogVersion: string;\n",
  "  guidelineUrlTemplate: string;\n",
  "  indexTopK: number;\n",
  "  lanceDocumentTable: string;\n",
  "};\n",
  "\n",
  "export const CHARTCOACH_DEFAULTS = {\n",
  ...Object.entries(defaults)
    .sort(([left], [right]) => left.localeCompare(right))
    .map(([key, value]) => `  ${key}: ${JSON.stringify(value)},\n`),
  "} as const satisfies ChartCoachDefaults;\n",
].join("");

if (checkOnly) {
  const current = readFileSync(outputPath, "utf8");
  if (current !== next) {
    console.error(
      "chartcoach-defaults.ts is stale. Run `pnpm --dir packages/catalog-javascript sync:defaults`.",
    );
    process.exit(1);
  }
  process.exit(0);
}

writeFileSync(outputPath, next);
