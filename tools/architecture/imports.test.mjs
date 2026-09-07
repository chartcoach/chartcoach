import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import { builtinModules } from "node:module";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

import ts from "typescript";

const repositoryRoot = fileURLToPath(new URL("../../", import.meta.url));
const catalogRoot = path.join(repositoryRoot, "packages/catalog");
const sourceZones = [
  { name: "docs", root: path.join(repositoryRoot, "apps/docs") },
  { name: "site", root: path.join(repositoryRoot, "apps/site") },
  { name: "catalog", root: path.join(catalogRoot, "src") },
];
const sourceExtensions = new Set([".astro", ".js", ".jsx", ".mjs", ".ts", ".tsx"]);
const nodeBuiltins = new Set(builtinModules.flatMap((name) => [name, name.replace(/^node:/, "")]));

void test("source imports preserve the web dependency graph", async () => {
  const violations = [];
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

function importViolation(zone, file, specifier) {
  if (zone.name === "catalog") {
    const builtin = specifier.replace(/^node:/, "");
    const nodeEntry = file === path.join(catalogRoot, "src/node.ts");
    if (!nodeEntry && (specifier.startsWith("node:") || nodeBuiltins.has(builtin)))
      return "Node builtin";
    if (!nodeEntry && specifier.endsWith("/node")) return "Node entry point";
    if (specifier.startsWith("@chartcoach/")) return "workspace dependency";
  }

  if (zone.name === "docs" && specifier.startsWith("@chartcoach/site")) {
    return "cross-app dependency";
  }
  if (zone.name === "site" && specifier.startsWith("@chartcoach/docs")) {
    return "cross-app dependency";
  }
  if (!specifier.startsWith(".") && !path.isAbsolute(specifier)) return undefined;

  const target = path.resolve(path.dirname(file), specifier);
  const owner = zone.name === "catalog" ? catalogRoot : zone.root;
  return isWithin(owner, target) ? undefined : "relative boundary escape";
}

async function sourceFiles(directory) {
  const files = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if ([".next", ".source", "dist", "node_modules", "out"].includes(entry.name)) continue;
    const target = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await sourceFiles(target)));
    } else if (sourceExtensions.has(path.extname(entry.name))) {
      files.push(target);
    }
  }
  return files;
}

function isWithin(root, target) {
  const relative = path.relative(root, target);
  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}
