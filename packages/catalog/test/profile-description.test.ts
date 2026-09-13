import { createHash } from "node:crypto";

import { describe, expect, it } from "vite-plus/test";

import { openCatalog, type FetchLike, type JsonObject } from "@chartcoach/catalog";
import operations from "../../../fixtures/catalog-contract/operations.json";
import profileFixture from "../../../fixtures/catalog-contract/profile.json";
import {
  catalogResponses,
  catalogUrl,
  type CatalogFixture,
  countingFetch,
  fetchFrom,
  fixtureRelease,
  releaseDigest,
  releaseResponses,
  releaseUrlFor,
  releaseWithArtifact,
} from "./catalog-testkit";

const profileName = "minilm-normalized";

describe("published profile description", () => {
  it("loads and caches metadata from the opened release", async () => {
    const fixture = await fixtureRelease();
    const profiled = profileRelease(fixture);
    const responses = catalogResponses(profiled);
    responses.set(profileUrl(profiled.release.digest), profiled.profile);
    const requests = new Map<string, number>();
    const fetch = countingFetch(responses, requests);

    const catalog = await openCatalog(catalogUrl, { fetch });

    const changedSelection = releaseWithArtifact(profiled.release, "selection-marker", {
      sha256: "f".repeat(64),
      bytes: 1,
    });

    responses.set(catalogUrl, JSON.stringify(changedSelection));

    expect((await catalog.describe()).profiles).toEqual([profileName]);
    const first = await catalog.describe({ profile: profileName });
    const second = await catalog.describe({ profile: profileName });

    expect(first.profile).toEqual({
      name: profileName,
      profile_schema_version: 1,
      documents_version: 1,
      embedding_functions: profileFixture.embedding_functions,
      dimensions: 4,
      distance_metric: "cosine",
      python_requirements: {},
      lancedb_version: "0.38.0",
      projection: null,
    });
    expect(second.profile).toEqual(first.profile);
    expect(requests.get(catalogUrl)).toBe(1);
    expect(requests.get(profileUrl(profiled.release.digest))).toBe(1);
    expect(requests.get(indexUrl(profiled.release.digest))).toBeUndefined();
  });

  it("retries missing and corrupt metadata", async () => {
    const fixture = await fixtureRelease();
    const profiled = profileRelease(fixture);
    const responses = releaseResponses(profiled);

    const catalog = await openCatalog(releaseUrlFor(profiled.release.digest), {
      fetch: fetchFrom(responses),
    });

    await expect(catalog.describe({ profile: profileName })).rejects.toMatchObject({
      code: "integrity",
    });
    responses.set(profileUrl(profiled.release.digest), "corrupt");
    await expect(catalog.describe({ profile: profileName })).rejects.toThrow(/byte count|SHA-256/);
    responses.set(profileUrl(profiled.release.digest), profiled.profile);

    expect((await catalog.describe({ profile: profileName })).profile?.distance_metric).toBe(
      "cosine",
    );
  });

  it("keeps concurrent cancellation isolated", async () => {
    const fixture = await fixtureRelease();
    const profiled = profileRelease(fixture);
    const responses = releaseResponses(profiled);
    const url = profileUrl(profiled.release.digest);
    let profileRequests = 0;
    let startRequest = () => {};

    const started = new Promise<void>((resolve) => {
      startRequest = () => resolve();
    });

    const fetch: FetchLike = async (input, init) => {
      if (input.toString() !== url) return fetchFrom(responses)(input, init);
      profileRequests += 1;

      if (profileRequests > 1) return new Response(profiled.profile);
      startRequest();

      return new Promise<Response>((_resolve, reject) => {
        const signal = init?.signal;

        if (signal?.aborted) {
          reject(signal.reason);

          return;
        }

        signal?.addEventListener("abort", () => reject(signal.reason), { once: true });
      });
    };

    const catalog = await openCatalog(releaseUrlFor(profiled.release.digest), { fetch });
    const controller = new AbortController();
    const cancelled = catalog.describe({ profile: profileName, signal: controller.signal });
    await started;
    const successful = catalog.describe({ profile: profileName });
    controller.abort();

    await expect(cancelled).rejects.toMatchObject({ name: "AbortError" });
    expect((await successful).profile?.distance_metric).toBe("cosine");
    expect((await catalog.describe({ profile: profileName })).profile?.distance_metric).toBe(
      "cosine",
    );
    expect(profileRequests).toBe(2);
  });

  it.each([
    ["entries_digest", "entries digest"],
    ["manifest_digest", "manifest digest"],
  ])("rejects metadata whose %s links another catalog", async (field, message) => {
    const fixture = await fixtureRelease();
    const profiled = profileRelease(fixture, profileMetadata(fixture, { [field]: "0".repeat(64) }));
    const responses = releaseResponses(profiled);
    responses.set(profileUrl(profiled.release.digest), profiled.profile);

    const catalog = await openCatalog(releaseUrlFor(profiled.release.digest), {
      fetch: fetchFrom(responses),
    });

    await expect(catalog.describe({ profile: profileName })).rejects.toThrow(message);
  });

  it("rejects projection metadata that disagrees with the release inventory", async () => {
    const fixture = await fixtureRelease();

    const profiled = profileRelease(
      fixture,
      profileMetadata(fixture, { projection: { algorithm: "linear", options: {} } }),
    );

    const responses = releaseResponses(profiled);
    responses.set(profileUrl(profiled.release.digest), profiled.profile);

    const catalog = await openCatalog(releaseUrlFor(profiled.release.digest), {
      fetch: fetchFrom(responses),
    });

    await expect(catalog.describe({ profile: profileName })).rejects.toMatchObject({
      code: "incompatible_profile",
    });
  });

  it("rejects oversized metadata before fetching it", async () => {
    const fixture = await fixtureRelease();
    const profiled = profileRelease(fixture);
    const release = releaseWithArtifact(profiled.release, profilePath(), { bytes: 65_537 });
    const responses = releaseResponses({ ...profiled, release });
    const requests = new Map<string, number>();

    const catalog = await openCatalog(releaseUrlFor(release.digest), {
      fetch: countingFetch(responses, requests),
    });

    await expect(catalog.describe({ profile: profileName })).rejects.toThrow("64 KiB");
    expect(requests.get(profileUrl(release.digest))).toBeUndefined();
  });
});

function profileRelease(fixture: CatalogFixture, metadata = profileMetadata(fixture)) {
  const profile = new TextEncoder().encode(JSON.stringify(metadata));

  const artifacts = {
    ...fixture.release.artifacts,
    [profilePath()]: {
      sha256: createHash("sha256").update(profile).digest("hex"),
      bytes: profile.byteLength,
    },
    [`profiles/${profileName}/index.tar.gz`]: {
      sha256: "e".repeat(64),
      bytes: 1,
    },
  };

  return {
    ...fixture,
    profile,
    release: {
      schema_version: 1 as const,
      artifacts,
      digest: releaseDigest(artifacts),
    },
  };
}

function profileMetadata(fixture: CatalogFixture, patch: JsonObject = {}): JsonObject {
  return {
    ...profileFixture,
    entries_digest: operations.description.entries_digest,
    manifest_digest: fixture.release.artifacts["MANIFEST.md"]!.sha256,
    ...patch,
  };
}

function profilePath(): string {
  return `profiles/${profileName}/profile.json`;
}

function profileUrl(digest: string): string {
  return new URL(profilePath(), releaseUrlFor(digest)).toString();
}

function indexUrl(digest: string): string {
  return new URL(`profiles/${profileName}/index.tar.gz`, releaseUrlFor(digest)).toString();
}
