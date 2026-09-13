import { cp, mkdir, readFile, readdir, rm, writeFile, chmod } from "node:fs/promises";
import { findPackageJSON } from "node:module";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../", import.meta.url));

const output = join(root, "dist");

const source = JSON.parse(await readFile(join(root, "package.json"), "utf8"));

async function installedVersion(name) {
  const path = findPackageJSON(name, import.meta.url);

  if (!path) throw new Error(`Cannot locate ${name}'s package manifest.`);

  return JSON.parse(await readFile(path, "utf8")).version;
}

// Capture Eve's compiled template keys and skill seeds while its build tooling is available.
const { prewarmBuiltAppSandboxes } = await import(
  new URL("./execution/sandbox/prewarm.js", import.meta.resolve("eve"))
);

const sandboxPlan = [];

await prewarmBuiltAppSandboxes({
  appRoot: root,
  dispatch: async ({ backend, input }) => {
    if (backend.name !== "just-bash" || input.bootstrap)
      throw new Error("The packaged chat sandbox must use just-bash with compiled skill seeds.");
    sandboxPlan.push({
      templateKey: input.templateKey,
      seedFiles: input.seedFiles.map((file) => ({
        path: file.path,
        content: Buffer.from(file.content).toString("base64"),
      })),
    });

    return { reused: false };
  },
});

await rm(output, { recursive: true, force: true });

await mkdir(output, { recursive: true });

await cp(join(root, ".output/cli"), join(output, "cli"), { recursive: true });

await cp(join(root, ".output/server"), join(output, "server"), {
  recursive: true,
  filter: (path) => !path.split(/[\\/]/).includes("node_modules"),
});

await rm(join(output, "server/package.json"), { force: true });

await cp(join(root, "out"), join(output, "public"), { recursive: true });

const dependencies = {};

// Eve discovers source projects through dependencies. The compiled worker embeds its runtime.
for (const name of Object.keys(source.dependencies)) {
  if (name !== "eve") dependencies[name] = await installedVersion(name);
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
      files: ["cli", "server", "public", "sandbox.json"],
      dependencies,
      publishConfig: source.publishConfig,
    },
    null,
    2,
  ) + "\n",
);

await cp(join(root, "README.md"), join(output, "README.md"));

await cp(resolve(root, "../../LICENSE"), join(output, "LICENSE"));

await writeFile(join(output, "sandbox.json"), JSON.stringify(sandboxPlan) + "\n");

await chmod(join(output, "cli/index.mjs"), 0o755);

async function inspect(directory) {
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
