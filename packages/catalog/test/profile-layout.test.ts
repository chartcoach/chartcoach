import { describe, expect, it } from "vite-plus/test";

import type { CatalogRelease, ReleaseArtifact } from "@chartcoach/catalog";
import { releaseProfileNames } from "../src/catalog/profile-layout";

const artifact: ReleaseArtifact = Object.freeze({ sha256: "a".repeat(64), bytes: 1 });

describe("profile artifact layout", () => {
  it("discovers flat profiles from profile metadata", () => {
    const names = releaseProfileNames(
      release({
        "profiles/minilm-normalized/profile.json": artifact,
        "profiles/minilm-normalized/index.tar.gz": artifact,
        "profiles/minilm-normalized/projection.parquet": artifact,
      }),
    );

    expect(names).toEqual(["minilm-normalized"]);
  });

  it("rejects malformed profile inventories", () => {
    expect(() =>
      releaseProfileNames(
        release({
          "profiles/provider/model/profile.json": artifact,
          "profiles/provider/model/index.tar.gz": artifact,
        }),
      ),
    ).toThrow("single-component");
    expect(() =>
      releaseProfileNames(release({ "profiles/minilm/profile.json": artifact })),
    ).toThrow("missing index.tar.gz");
    expect(() =>
      releaseProfileNames(
        release({
          "profiles/minilm/profile.json": artifact,
          "profiles/minilm/index.tar.gz": artifact,
          "profiles/minilm/unknown.bin": artifact,
        }),
      ),
    ).toThrow("Unknown profile artifact");
    expect(() =>
      releaseProfileNames(
        release({
          "profiles/con/profile.json": artifact,
          "profiles/con/index.tar.gz": artifact,
        }),
      ),
    ).toThrow("single-component");
    expect(() =>
      releaseProfileNames(
        release({
          "profiles/minilm/index.tar.gz": artifact,
        }),
      ),
    ).toThrow("missing profile.json");
  });
});

function release(profiles: Readonly<Record<string, ReleaseArtifact>>): CatalogRelease {
  return {
    schema_version: 1,
    digest: "b".repeat(64),
    artifacts: {
      "MANIFEST.md": artifact,
      "entries.parquet": artifact,
      ...profiles,
    },
  };
}
