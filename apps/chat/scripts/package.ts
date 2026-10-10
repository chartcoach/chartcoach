import { cp, mkdir, readFile, readdir, rm, writeFile, chmod } from "node:fs/promises";
import { findPackageJSON } from "node:module";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../", import.meta.url));

const output = join(root, "dist");

const source = JSON.parse(await readFile(join(root, "package.json"), "utf8"));

async function installedVersion(name: string): Promise<string> {
  const path = findPackageJSON(name, import.meta.url);

  if (!path) throw new Error(`Cannot locate ${name}'s package manifest.`);

  return JSON.parse(await readFile(path, "utf8")).version;
}

await rm(output, { recursive: true, force: true });

await mkdir(output, { recursive: true });

await cp(join(root, ".output/cli"), join(output, "cli"), { recursive: true });

await cp(join(root, ".output/server"), join(output, "server"), {
  recursive: true,
  filter: (path) => !path.split(/[\\/]/).includes("node_modules"),
});

await rm(join(output, "server/package.json"), { force: true });

await cp(join(root, ".output/sandbox"), join(output, "sandbox"), { recursive: true });

await cp(join(root, "out"), join(output, "public"), { recursive: true });

const dependencies: Record<string, string> = {};

// Eve discovers source projects through dependencies. The compiled worker embeds its runtime.
for (const name of Object.keys(source.dependencies)) {
  if (name !== "eve") dependencies[name] = await installedVersion(name);
}

// Preview SDKs live on GitHub rather than npm. Keep a standalone chat install
// tied to the same build, including when no SDK override is supplied.
if (/^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)-dev\.[1-9]\d*$/.test(source.version)) {
  if (dependencies["@chartcoach/catalog"] !== source.version)
    throw new Error("Preview chat and catalog versions must match.");
  dependencies["@chartcoach/catalog"] =
    `https://github.com/chartcoach/chartcoach/releases/download/previews/chartcoach-catalog-${source.version}.tgz`;
}

await writeFile(
  join(output, "package.json"),
  JSON.stringify(
    {
      name: source.name,
      version: source.version,
      description: source.description,
      license: source.license,
      repository: source.repository,
      type: "module",
      engines: source.engines,
      bin: { chartcoach: "./cli/index.mjs" },
      files: ["cli", "server", "public", "sandbox"],
      dependencies,
      publishConfig: source.publishConfig,
    },
    null,
    2,
  ) + "\n",
);

await cp(join(root, "README.md"), join(output, "README.md"));

await cp(resolve(root, "../../LICENSE"), join(output, "LICENSE"));

await chmod(join(output, "cli/index.mjs"), 0o755);

async function inspect(directory: string): Promise<void> {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name);

    if (entry.isSymbolicLink()) throw new Error(`Distribution contains a symlink: ${path}`);

    if (entry.isDirectory()) await inspect(path);
    else if (/\.(node|dylib|so|dll)$/.test(entry.name))
      throw new Error(`Distribution contains a platform binary: ${path}`);
  }
}

await inspect(output);

console.log(
  `Assembled ${source.name}@${source.version}. Pack with npm pack ./apps/chat/dist --ignore-scripts.`,
);
