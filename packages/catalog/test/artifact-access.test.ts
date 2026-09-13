import { mkdtemp, open, readFile, rename, rm, writeFile } from "node:fs/promises";
import { createReadStream } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createHash } from "node:crypto";
import { afterEach, describe, expect, it, vi } from "vite-plus/test";
import { loadCatalogData, openCatalog } from "@chartcoach/catalog";
import { artifactPath, openCatalog as openNodeCatalog } from "../src/node";
import {
  countingFetch,
  fixtureRelease,
  releaseResponses,
  releaseUrlFor,
  releaseFixtureRoot,
  releaseWithArtifact,
} from "./catalog-testkit";

const directories: string[] = [];

afterEach(async () => {
  vi.restoreAllMocks();
  await Promise.all(
    directories.splice(0).map((path) => rm(path, { recursive: true, force: true })),
  );
});

describe("verified artifact access", () => {
  it("reads cached optional artifacts larger than the core-file bound", async () => {
    const directory = await mkdtemp(join(tmpdir(), "chartcoach-large-cache-"));
    directories.push(directory);
    const large = join(directory, "large.bin");
    const file = await open(large, "wx");

    try {
      await file.truncate(67_108_865);
    } finally {
      await file.close();
    }

    const hash = createHash("sha256");

    for await (const chunk of createReadStream(large)) hash.update(chunk);
    const digest = hash.digest("hex");
    const fixture = await fixtureRelease();

    const release = releaseWithArtifact(fixture.release, "large.bin", {
      sha256: digest,
      bytes: 67_108_865,
    });

    const responses = releaseResponses({ ...fixture, release });

    const catalog = await openNodeCatalog(releaseUrlFor(release.digest), {
      cacheDirectory: directory,
      fetch: async (input) => {
        const value = responses.get(input.toString());

        if (!value) throw new Error("Artifact is offline");

        return new Response(value);
      },
    });

    await rename(large, join(directory, "artifacts", digest));
    const bytes = await catalog.artifact("large.bin");
    expect(bytes.byteLength).toBe(67_108_865);
    expect(bytes.at(-1)).toBe(0);
  });

  it.each(["caller", "deadline"])(
    "cancels a stalled custom artifact stream on %s cancellation",
    async (trigger) => {
      const fixture = await fixtureRelease();
      const content = new TextEncoder().encode("portable artifact");

      const release = releaseWithArtifact(fixture.release, "extra.bin", {
        sha256: createHash("sha256").update(content).digest("hex"),
        bytes: content.length,
      });

      const responses = releaseResponses({ ...fixture, release });
      let ready = () => {};

      const started = new Promise<void>((resolve) => {
        ready = resolve;
      });

      let stalled = true;

      const catalog = await openCatalog(releaseUrlFor(release.digest), {
        fetch: async (input) => {
          if (input.toString().endsWith("extra.bin")) {
            if (stalled) {
              stalled = false;
              ready();

              return new Response(new ReadableStream());
            }

            return new Response(content);
          }

          return new Response(responses.get(input.toString()));
        },
      });

      const controller = new AbortController();

      if (trigger === "deadline")
        vi.spyOn(AbortSignal, "timeout").mockReturnValue(controller.signal);

      const pending = catalog.artifact(
        "extra.bin",
        trigger === "caller" ? { signal: controller.signal } : {},
      );

      await started;
      controller.abort();
      await expect(pending).rejects.toMatchObject({ name: "AbortError" });
      vi.restoreAllMocks();
      expect(await catalog.artifact("extra.bin")).toEqual(content);
    },
  );

  it("streams optional Node artifacts once and reuses their verified file offline", async () => {
    const directory = await mkdtemp(join(tmpdir(), "chartcoach-stream-"));
    directories.push(directory);
    const fixture = await fixtureRelease();
    const content = new Uint8Array(128 * 1024).fill(42);

    const release = releaseWithArtifact(fixture.release, "extra.bin", {
      sha256: createHash("sha256").update(content).digest("hex"),
      bytes: content.length,
    });

    const responses = releaseResponses({ ...fixture, release });
    let reads = 0;

    const catalog = await openNodeCatalog(releaseUrlFor(release.digest), {
      cacheDirectory: directory,
      fetch: async (input) => {
        if (input.toString().endsWith("extra.bin")) {
          reads += 1;

          return new Response(
            new ReadableStream({
              start(controller) {
                controller.enqueue(content.slice(0, 65536));
                controller.enqueue(content.slice(65536));
                controller.close();
              },
            }),
          );
        }

        return new Response(responses.get(input.toString()));
      },
    });

    const path = await artifactPath(catalog, "extra.bin");
    expect(new Uint8Array(await readFile(path))).toEqual(content);

    const offline = await openNodeCatalog(releaseUrlFor(release.digest), {
      cacheDirectory: directory,
      fetch: async () => {
        throw new Error("offline");
      },
    });

    expect(await artifactPath(offline, "extra.bin")).toBe(path);
    expect(reads).toBe(1);
  });

  it("returns independent verified bytes and rejects unknown paths", async () => {
    const fixture = await fixtureRelease();
    const requests = new Map<string, number>();

    const catalog = await openCatalog(releaseUrlFor(fixture.release.digest), {
      fetch: countingFetch(releaseResponses(fixture), requests),
    });

    const first = await catalog.artifact("entries.parquet");
    first.fill(0);
    expect(await catalog.artifact("entries.parquet")).toEqual(new Uint8Array(fixture.entries));
    expect([...requests.values()]).toEqual([1, 1, 1]);
    await expect(catalog.artifact("../secret")).rejects.toMatchObject({ code: "lookup" });

    const bundle = await loadCatalogData({
      entries: fixture.entries,
      manifestText: fixture.manifest,
    });

    await expect(bundle.artifact("entries.parquet")).rejects.toMatchObject({
      code: "unavailable_capability",
    });
  });

  it("reopens an exact Node release offline and repairs corrupt cached bytes", async () => {
    const directory = await mkdtemp(join(tmpdir(), "chartcoach-node-"));
    directories.push(directory);
    const fixture = await fixtureRelease();
    const requests = new Map<string, number>();
    const fetch = countingFetch(releaseResponses(fixture), requests);
    const url = releaseUrlFor(fixture.release.digest);
    const first = await openNodeCatalog(url, { fetch, cacheDirectory: directory });
    const path = await artifactPath(first, "entries.parquet");
    expect(await readFile(path)).toEqual(fixture.entries);

    const offline = await openNodeCatalog(url, {
      cacheDirectory: directory,
      fetch: async () => {
        throw new Error("offline");
      },
    });

    expect(offline.read({ ids: ["direct-labels"] })[0]?.id).toBe("direct-labels");
    await writeFile(path, new Uint8Array(fixture.entries.length));
    const repaired = await openNodeCatalog(url, { fetch, cacheDirectory: directory });
    expect(await repaired.artifact("entries.parquet")).toEqual(new Uint8Array(fixture.entries));
    expect(requests.get(new URL("entries.parquet", url).toString())).toBe(2);
    expect(requests.get(url)).toBe(1);
  });

  it("opens a local Node release and supports caller-owned cloud fetching", async () => {
    const directory = await mkdtemp(join(tmpdir(), "chartcoach-cloud-"));
    directories.push(directory);
    const local = await openNodeCatalog(releaseFixtureRoot, { cacheDirectory: directory });
    expect(local.require("direct-labels").id).toBe("direct-labels");
    const fixture = await fixtureRelease();
    const root = "s3://catalog-bucket/release/";

    const bytes = new Map([
      [`${root}release.json`, JSON.stringify(fixture.release)],
      [`${root}MANIFEST.md`, fixture.manifest],
    ]);

    const cloud = await openCatalog(`${root}release.json`, {
      fetch: async (input) =>
        input.toString().endsWith("entries.parquet")
          ? new Response(Uint8Array.from(fixture.entries))
          : new Response(bytes.get(input.toString()), {
              status: bytes.has(input.toString()) ? 200 : 404,
            }),
    });

    expect(cloud.require("direct-labels").id).toBe("direct-labels");
    expect(await cloud.artifact("MANIFEST.md")).toEqual(new TextEncoder().encode(fixture.manifest));
  });
});
