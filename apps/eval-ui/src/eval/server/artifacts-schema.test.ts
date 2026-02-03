import { describe, expect, it } from "vitest";

import { existsSync } from "node:fs";
import { readdir, readFile } from "node:fs/promises";
import path from "node:path";

import {
  ArtifactsIndexSchema,
  ScenarioBundleArtifactSchema,
} from "@chartcoach/eval-ui/eval/server/artifacts-schema";

function resolveFixtureRoot() {
  const candidates = [
    path.resolve(process.cwd(), "fixtures/eval-artifacts/v1"),
    path.resolve(process.cwd(), "apps/eval-ui/fixtures/eval-artifacts/v1"),
  ];

  for (const candidate of candidates) {
    const indexPath = path.join(candidate, "index.json");
    if (existsSync(indexPath)) {
      return candidate;
    }
  }

  throw new Error("Could not locate eval artifacts fixture root (v1).");
}

describe("Eval Artifacts (fixture drift)", () => {
  it("parses the bundled fixture artifacts with the server zod schemas", async () => {
    const root = resolveFixtureRoot();
    const indexRaw = await readFile(path.join(root, "index.json"), "utf-8");
    const index = ArtifactsIndexSchema.parse(JSON.parse(indexRaw));
    expect(index.schema_version).toBe(1);
    expect(index.scenarios.length).toBeGreaterThan(0);

    const bundlesDir = path.join(root, "bundles");
    const bundleFiles = (await readdir(bundlesDir)).filter((name) =>
      name.endsWith(".json"),
    );
    expect(bundleFiles.length).toBeGreaterThan(0);
    const bundleRaw = await readFile(path.join(bundlesDir, bundleFiles[0]!), "utf-8");
    const bundle = ScenarioBundleArtifactSchema.parse(JSON.parse(bundleRaw));
    expect(bundle.schema_version).toBe(1);
    expect(bundle.strategies.length).toBeGreaterThan(0);
  });
});
