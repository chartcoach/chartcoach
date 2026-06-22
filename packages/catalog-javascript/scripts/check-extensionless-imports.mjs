import { readdirSync, readFileSync } from "node:fs";
import { join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const packageRoot = fileURLToPath(new URL("..", import.meta.url));
const sourceRoot = join(packageRoot, "src");
const importPattern = /(?:from\s*["']|import\(\s*["'])(\.[^"']*\.js)(?=["'])/g;

function* sourceFiles(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const path = join(dir, entry.name);
    if (entry.isDirectory()) {
      yield* sourceFiles(path);
    } else if (entry.isFile() && path.endsWith(".ts")) {
      yield path;
    }
  }
}

let failed = false;
for (const path of sourceFiles(sourceRoot)) {
  const text = readFileSync(path, "utf8");
  for (const match of text.matchAll(importPattern)) {
    const displayPath = relative(packageRoot, path);
    console.error(`${displayPath}: relative TypeScript import must omit .js: ${match[1]}`);
    failed = true;
  }
}

process.exit(failed ? 1 : 0);
