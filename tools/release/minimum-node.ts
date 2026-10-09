import { readFile } from "node:fs/promises";
import { minVersion } from "semver";

const manifest = JSON.parse(
  await readFile(new URL("../../packages/catalog/package.json", import.meta.url), "utf8"),
);

const minimum = minVersion(manifest.engines.node);

if (!minimum) throw new Error("The SDK must declare a valid Node.js version range");

console.log(minimum.version);
