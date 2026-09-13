import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { chmod, cp, mkdir, mkdtemp, readdir, readFile, rm, writeFile } from "node:fs/promises";
import { createServer } from "node:http";
import { builtinModules, createRequire, findPackageJSON } from "node:module";
import { parseArgs } from "node:util";
import { tmpdir } from "node:os";
import { dirname, extname, join, resolve, sep } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { chromium } from "playwright";
import { build } from "vite-plus";
import { parse, stringify } from "yaml";
import { minVersion } from "semver";

const here = dirname(fileURLToPath(import.meta.url));

const root = resolve(here, "../..");

const { positionals, values } = parseArgs({
  allowPositionals: true,
  options: {
    node: { type: "string" },
    "minimum-dependencies": { type: "boolean", default: false },
  },
});

const [archive] = positionals;

if (!archive || positionals.length !== 1)
  throw new Error("Usage: verify:npm <tarball> [--node <executable>] [--minimum-dependencies]");

const tarball = resolve(root, archive);

const node = values.node ?? process.execPath;

const require = createRequire(import.meta.url);

const directory = await mkdtemp(join(tmpdir(), "chartcoach-npm-"));

let browser;

let server;

function run(command, args, extraEnv = {}) {
  const result = spawnSync(command, args, {
    cwd: directory,
    env: { ...process.env, NODE_PATH: "", NODE_OPTIONS: "", ...extraEnv },
    stdio: "inherit",
  });

  if (result.error) throw result.error;
  assert.equal(result.status, 0, `${command} ${args.join(" ")} failed`);
}

async function unlock(path) {
  await chmod(path, 0o700);

  for (const entry of await readdir(path, { withFileTypes: true })) {
    if (entry.isDirectory()) await unlock(join(path, entry.name));
  }
}

try {
  const policy = parse(await readFile(join(root, "pnpm-workspace.yaml"), "utf8"));
  await writeFile(
    join(directory, "package.json"),
    JSON.stringify({
      name: "chartcoach-release-consumer",
      private: true,
      type: "module",
      dependencies: { "@chartcoach/catalog": `file:${tarball}` },
    }),
  );
  await writeFile(
    join(directory, "pnpm-workspace.yaml"),
    stringify({
      minimumReleaseAge: policy.minimumReleaseAge,
      minimumReleaseAgeExclude: policy.minimumReleaseAgeExclude,
      minimumReleaseAgeStrict: policy.minimumReleaseAgeStrict,
      blockExoticSubdeps: policy.blockExoticSubdeps,
    }),
  );
  run("pnpm", ["install", "--ignore-scripts", "--no-frozen-lockfile"]);
  assert.equal(
    await readFile(join(directory, "node_modules/@chartcoach/catalog/LICENSE"), "utf8"),
    await readFile(join(root, "LICENSE"), "utf8"),
    "The npm distribution must include the project license",
  );
  await cp(join(here, "node-consumer.mjs"), join(directory, "node-consumer.mjs"));

  const nativeModules = {
    LANCE_MODULE: pathToFileURL(require.resolve("@lancedb/lancedb")).href,
    DUCKDB_MODULE: pathToFileURL(require.resolve("@duckdb/node-api")).href,
    TAR_MODULE: pathToFileURL(require.resolve("tar")).href,
    LANCE_VERSION: JSON.parse(
      await readFile(findPackageJSON("@lancedb/lancedb", import.meta.url), "utf8"),
    ).version,
  };

  run(
    node,
    ["node-consumer.mjs", join(root, "fixtures/catalog-release"), join(directory, "current")],
    nativeModules,
  );
  await cp(join(here, "browser-consumer.ts"), join(directory, "browser-consumer.ts"));
  await cp(join(here, "browser-duckdb-consumer.ts"), join(directory, "browser-duckdb-consumer.ts"));
  const wasmDirectory = dirname(require.resolve("@duckdb/duckdb-wasm"));
  await writeFile(
    join(directory, "tsconfig.json"),
    JSON.stringify({
      compilerOptions: {
        target: "ES2022",
        module: "NodeNext",
        moduleResolution: "NodeNext",
        strict: true,
        noEmit: true,
        types: [],
        lib: ["ES2022", "DOM"],
        paths: { "@duckdb/duckdb-wasm": [join(wasmDirectory, "duckdb-browser.d.ts")] },
      },
      files: ["browser-consumer.ts"],
    }),
  );
  run(node, [require.resolve("typescript/bin/tsc"), "-p", "tsconfig.json"]);
  await writeFile(
    join(directory, "tsconfig.duckdb.json"),
    JSON.stringify({
      extends: "./tsconfig.json",
      // DuckDB-WASM publishes references to its development-only Emscripten declarations.
      compilerOptions: { skipLibCheck: true },
      files: ["browser-duckdb-consumer.ts"],
    }),
  );
  run(node, [require.resolve("typescript/bin/tsc"), "-p", "tsconfig.duckdb.json"]);
  await writeFile(
    join(directory, "index.html"),
    '<!doctype html><html><head><meta charset="utf-8"><title>Catalog consumer</title></head><body><script type="module" src="/browser-consumer.ts"></script></body></html>',
  );
  await writeFile(
    join(directory, "duckdb.html"),
    '<!doctype html><html><head><meta charset="utf-8"><title>DuckDB catalog consumer</title></head><body><p>Checking DuckDB catalog tables</p><script type="module" src="/browser-duckdb-consumer.ts"></script></body></html>',
  );
  await cp(join(root, "fixtures/catalog-release"), join(directory, "public/catalog"), {
    recursive: true,
  });
  await cp(
    join(root, "fixtures/catalog-contract/tables.json"),
    join(directory, "public/tables.json"),
  );
  await mkdir(join(directory, "public/duckdb"), { recursive: true });

  for (const asset of ["duckdb-browser-eh.worker.js", "duckdb-eh.wasm"])
    await cp(join(wasmDirectory, asset), join(directory, "public/duckdb", asset));
  await build({
    configFile: false,
    root: directory,
    resolve: { alias: { "@duckdb/duckdb-wasm": join(wasmDirectory, "duckdb-browser.mjs") } },
    build: {
      target: "es2022",
      rolldownOptions: { input: [join(directory, "index.html"), join(directory, "duckdb.html")] },
    },
    plugins: [
      {
        name: "verify-browser-dependencies",
        generateBundle() {
          for (const id of this.getModuleIds()) {
            assert.ok(
              !id.startsWith("node:") &&
                !builtinModules.includes(id) &&
                !id.includes("__vite-browser-external"),
              `Node builtin in browser: ${id}`,
            );
            assert.ok(
              !id.startsWith(join(root, "packages")),
              `Workspace source in consumer: ${id}`,
            );
            assert.ok(
              !id.includes("@lancedb/") && !/[/\\]node_modules[/\\]tar[/\\]/.test(id),
              `Native dependency in browser: ${id}`,
            );
          }
        },
      },
    ],
  });
  const output = join(directory, "dist");

  const contentTypes = {
    ".html": "text/html",
    ".js": "text/javascript",
    ".wasm": "application/wasm",
    ".json": "application/json",
  };

  server = createServer(async (request, response) => {
    const path = resolve(
      output,
      `.${new URL(request.url, "http://localhost").pathname === "/" ? "/index.html" : new URL(request.url, "http://localhost").pathname}`,
    );

    if (!path.startsWith(`${output}${sep}`)) {
      response.writeHead(403).end();

      return;
    }

    try {
      const bytes = await readFile(path);
      response.writeHead(200, {
        "Content-Type": contentTypes[extname(path)] ?? "application/octet-stream",
        "Content-Security-Policy":
          "default-src 'self'; script-src 'self' 'wasm-unsafe-eval'; connect-src 'self'" +
          (path.endsWith("duckdb.html") || path.startsWith(join(output, "duckdb"))
            ? " https://extensions.duckdb.org"
            : ""),
      });
      response.end(bytes);
    } catch {
      response.writeHead(404).end();
    }
  });
  await new Promise((done) => server.listen(0, "127.0.0.1", done));
  browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const failures = [];
  const wasm = [];
  page.on("pageerror", (error) => failures.push(error.message));
  page.on("requestfailed", (request) => failures.push(request.url()));
  page.on("response", (response) => {
    if (response.url().endsWith(".wasm")) wasm.push(response.status());

    if (response.status() >= 400 && !response.url().endsWith("favicon.ico"))
      failures.push(response.url());
  });
  await page.goto(`http://127.0.0.1:${server.address().port}`);
  await page.locator('body[data-verified="true"]').waitFor();
  assert.deepEqual(failures, []);
  await page.goto(`http://127.0.0.1:${server.address().port}/duckdb.html`);

  try {
    await page.locator('body[data-duckdb-verified="true"]').waitFor();
  } catch (error) {
    assert.deepEqual(failures, []);
    throw error;
  }

  assert.deepEqual(failures, []);
  assert.ok(wasm.length > 0 && wasm.every((status) => status === 200));
  console.log("Verified packed declarations, browser Parquet, RefKit and DuckDB-WASM registration");

  if (values["minimum-dependencies"]) {
    const installed = JSON.parse(
      await readFile(join(directory, "node_modules/@chartcoach/catalog/package.json"), "utf8"),
    );

    const minimum = {};

    for (const [name, range] of Object.entries(installed.dependencies)) {
      minimum[name] = minVersion(range).version;
    }

    const consumer = JSON.parse(await readFile(join(directory, "package.json"), "utf8"));
    consumer.dependencies = { ...consumer.dependencies, ...minimum };
    await writeFile(join(directory, "package.json"), JSON.stringify(consumer));
    const minimumPolicy = parse(await readFile(join(directory, "pnpm-workspace.yaml"), "utf8"));
    minimumPolicy.overrides = minimum;
    await writeFile(join(directory, "pnpm-workspace.yaml"), stringify(minimumPolicy));
    run("pnpm", ["install", "--ignore-scripts", "--no-frozen-lockfile"]);
    run(node, [require.resolve("typescript/bin/tsc"), "-p", "tsconfig.json"]);
    run(
      node,
      ["node-consumer.mjs", join(root, "fixtures/catalog-release"), join(directory, "minimum")],
      nativeModules,
    );
    console.log("Verified minimum direct runtime dependencies");
  }
} finally {
  await browser?.close();

  if (server) await new Promise((done) => server.close(done));
  await unlock(directory);
  await rm(directory, { recursive: true, force: true });
}
