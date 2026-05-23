import assert from "node:assert/strict";
import { access } from "node:fs/promises";
import { test } from "vitest";

test("built package exports include declarations", async () => {
  await access(new URL("../distlib/index.js", import.meta.url));
  await access(new URL("../distlib/index.d.ts", import.meta.url));

  const publicEntry = await import("../distlib/index.js");
  assert.equal(typeof publicEntry.mountVisgroundViewer, "function");
  assert.equal(typeof publicEntry.parseViewerRuntimeConfig, "function");
  assert.equal(typeof publicEntry.createParquetViewerBridge, "function");
});
