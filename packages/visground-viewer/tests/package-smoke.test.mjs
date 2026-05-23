import assert from "node:assert/strict";
import { test } from "vitest";

test("source package entry exports the viewer API", async () => {
  const publicEntry = await import("@chartcoach/visground-viewer");
  assert.equal(typeof publicEntry.mountVisgroundViewer, "function");
  assert.equal(typeof publicEntry.parseViewerRuntimeConfig, "function");
  assert.equal(typeof publicEntry.createParquetViewerBridge, "function");
});
