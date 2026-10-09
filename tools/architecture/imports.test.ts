import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import { builtinModules } from "node:module";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

import ts from "typescript";

const repositoryRoot = fileURLToPath(new URL("../../", import.meta.url));

const catalogRoot = path.join(repositoryRoot, "packages/catalog");

const chatRoot = path.join(repositoryRoot, "apps/chat");

const sourceZones = [
  { name: "docs", root: path.join(repositoryRoot, "apps/docs") },
  { name: "site", root: path.join(repositoryRoot, "apps/site") },
  { name: "chat", root: chatRoot },
  { name: "catalog", root: path.join(catalogRoot, "src") },
];

const sourceExtensions = new Set([".astro", ".js", ".jsx", ".mjs", ".ts", ".tsx"]);

const nodeBuiltins = new Set(builtinModules.flatMap((name) => [name, name.replace(/^node:/, "")]));

void test("source imports preserve the web dependency graph", async () => {
  const violations: string[] = [];

  for (const zone of sourceZones) {
    for (const file of await sourceFiles(zone.root)) {
      const source = await readFile(file, "utf8");
      const imports = ts.preProcessFile(source, true, true).importedFiles;

      for (const imported of imports) {
        const reason = importViolation(zone, file, imported.fileName);

        if (reason) {
          violations.push(
            `${path.relative(repositoryRoot, file)}: ${imported.fileName} (${reason})`,
          );
        }
      }
    }
  }

  assert.deepEqual(violations, []);
});

void test("the browser catalog rejects both Node builtin spellings", () => {
  const zone = sourceZones.find(({ name }) => name === "catalog");
  assert.ok(zone);
  const file = path.join(catalogRoot, "src/index.ts");

  assert.equal(importViolation(zone, file, "fs"), "Node builtin");
  assert.equal(importViolation(zone, file, "node:fs"), "Node builtin");
});

function importViolation(zone: (typeof sourceZones)[number], file: string, specifier: string) {
  if (zone.name === "chat") {
    const reason = chatImportViolation(file, specifier);

    if (reason) return reason;
  }

  if (zone.name === "catalog") {
    const builtin = specifier.replace(/^node:/, "");

    const nodeEntry =
      file === path.join(catalogRoot, "src/node.ts") ||
      isWithin(path.join(catalogRoot, "src/node"), file);

    const duckdbEntry = file === path.join(catalogRoot, "src/duckdb.ts");

    if (!duckdbEntry && specifier === "@duckdb/node-api") return "optional native dependency";

    if (!nodeEntry && (specifier.startsWith("node:") || nodeBuiltins.has(builtin)))
      return "Node builtin";

    if (!nodeEntry && specifier.endsWith("/node")) return "Node entry point";

    if (
      !nodeEntry &&
      specifier.startsWith(".") &&
      isWithin(path.join(catalogRoot, "src/node"), path.resolve(path.dirname(file), specifier))
    )
      return "Node implementation";

    if (
      !duckdbEntry &&
      specifier.startsWith(".") &&
      ["src/duckdb", "src/duckdb.ts"].some(
        (entry) => path.resolve(path.dirname(file), specifier) === path.join(catalogRoot, entry),
      )
    )
      return "optional native implementation";

    if (specifier.startsWith("@chartcoach/")) return "workspace dependency";
  }

  if (
    ["docs", "site", "chat"].some(
      (name) =>
        name !== zone.name &&
        (specifier === `@chartcoach/${name}` || specifier.startsWith(`@chartcoach/${name}/`)),
    )
  ) {
    return "cross-app dependency";
  }

  if (!specifier.startsWith(".") && !path.isAbsolute(specifier)) return undefined;

  const target = path.resolve(path.dirname(file), specifier);
  const owner = zone.name === "catalog" ? catalogRoot : zone.root;

  return isWithin(owner, target) ? undefined : "relative boundary escape";
}

function chatImportViolation(file: string, specifier: string) {
  const source = path.relative(chatRoot, file).split(path.sep).join("/");

  const browser =
    /^(app|components|chat|shared|browser)\//.test(source) || source === "lib/catalog-client.ts";

  if (
    browser &&
    (nodeBuiltins.has(specifier.replace(/^node:/, "")) ||
      specifier.startsWith("node:") ||
      [
        "@chartcoach/catalog/node",
        "@chartcoach/catalog/duckdb",
        "@duckdb/node-api",
        "@lancedb/lancedb",
        "@huggingface/transformers",
      ].some((name) => specifier === name || specifier.startsWith(`${name}/`)))
  )
    return "server dependency in browser code";

  if (/^lib\/(catalog|retrieval)\//.test(source) && /^(eve|react|next)(\/|$)/.test(specifier))
    return "framework dependency in catalog access";

  if (!specifier.startsWith(".")) return;

  const target = path
    .relative(chatRoot, path.resolve(path.dirname(file), specifier))
    .split(path.sep)
    .join("/");

  if (
    browser &&
    (target.startsWith("agent/") ||
      (target.startsWith("lib/") && !/^lib\/catalog-client(?:\.ts)?$/.test(target)))
  )
    return "server implementation in browser code";

  if (source.startsWith("chat/") && /^(app|components)\//.test(target))
    return "rendering dependency in chat state";

  if (source.startsWith("components/") && /^lib\/catalog-client(?:\.ts)?$/.test(target))
    return "HTTP access in rendering code";

  if (source.startsWith("shared/") && !target.startsWith("shared/"))
    return "app implementation in shared contract";

  if (/^lib\/(catalog|retrieval)\//.test(source) && /^(agent|app|components|chat)\//.test(target))
    return "app orchestration in catalog access";

  if (source.startsWith("lib/catalog/") && target.startsWith("lib/retrieval/"))
    return "retrieval policy in catalog infrastructure";
}

void test("chat boundaries separate rendering, state, retrieval policy, and catalog infrastructure", () => {
  const check = (file: string, specifier: string) =>
    chatImportViolation(path.join(chatRoot, file), specifier);

  assert.equal(
    check("components/chat/message.tsx", "@duckdb/node-api"),
    "server dependency in browser code",
  );
  assert.equal(
    check("chat/runtime.ts", "../lib/catalog/open"),
    "server implementation in browser code",
  );
  assert.equal(check("chat/runtime.ts", "../lib/async"), "server implementation in browser code");
  assert.equal(
    check("chat/runtime.ts", "../components/chat/composer"),
    "rendering dependency in chat state",
  );
  assert.equal(
    check("shared/review.ts", "../chat/evidence"),
    "app implementation in shared contract",
  );
  assert.equal(check("lib/catalog/open.ts", "eve/tools"), "framework dependency in catalog access");
  assert.equal(
    check("lib/catalog/open.ts", "../retrieval/search"),
    "retrieval policy in catalog infrastructure",
  );
  assert.equal(
    check("lib/retrieval/search.ts", "../../agent/agent"),
    "app orchestration in catalog access",
  );
  assert.equal(check("lib/retrieval/search.ts", "../catalog/scope"), undefined);
  assert.equal(check("components/chat/message.tsx", "../../chat/evidence"), undefined);
});

async function sourceFiles(directory: string): Promise<string[]> {
  const files = [];

  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if ([".eve", ".next", ".output", ".source", "dist", "node_modules", "out"].includes(entry.name))
      continue;
    const target = path.join(directory, entry.name);

    if (entry.isDirectory()) {
      files.push(...(await sourceFiles(target)));
    } else if (sourceExtensions.has(path.extname(entry.name))) {
      files.push(target);
    }
  }

  return files;
}

function isWithin(root: string, target: string) {
  const relative = path.relative(root, target);

  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}
