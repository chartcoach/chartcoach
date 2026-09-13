import { readFile } from "node:fs/promises";
import { minVersion } from "semver";

const manifest = JSON.parse(
  await readFile(new URL("../../packages/catalog/package.json", import.meta.url), "utf8"),
);

console.log(minVersion(manifest.engines.node).version);
