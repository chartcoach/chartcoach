import { createHash } from "node:crypto";
import {
  chmod,
  link,
  lstat,
  mkdir,
  mkdtemp,
  readFile,
  readdir,
  rm,
  symlink,
  writeFile,
} from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { create, Header } from "tar";
import { gzipSync, gunzipSync } from "node:zlib";
import { afterEach, describe, expect, it } from "vite-plus/test";
import { indexPath, openCatalog } from "../src/node";
import operations from "../../../fixtures/catalog-contract/operations.json";
import profileFixture from "../../../fixtures/catalog-contract/profile.json";
import {
  fixtureRelease,
  releaseDigest,
  releaseResponses,
  releaseUrlFor,
  responseBytes,
} from "./catalog-testkit";

const directories: string[] = [];
afterEach(async () => {
  async function remove(path: string): Promise<void> {
    if ((await lstat(path)).isDirectory()) {
      await chmod(path, 0o700);
      for (const name of await readdir(path)) await remove(join(path, name));
    }
    await rm(path, { recursive: true, force: true });
  }
  await Promise.all(directories.splice(0).map(remove));
});

async function temporary(): Promise<string> {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-index-"));
  directories.push(directory);
  return directory;
}

async function archive(files = ["documents.lance"], prefix?: string): Promise<Buffer> {
  const directory = await temporary();
  await mkdir(join(directory, "documents.lance"));
  await writeFile(join(directory, "documents.lance", "data"), "indexed documents");
  await writeFile(join(directory, "other.txt"), "other table");
  if (files.includes("documents.lance/symbolic"))
    await symlink("data", join(directory, "documents.lance", "symbolic"));
  if (files.includes("documents.lance/hard"))
    await link(
      join(directory, "documents.lance", "data"),
      join(directory, "documents.lance", "hard"),
    );
  const file = join(directory, "index.tar.gz");
  await create(
    {
      cwd: directory,
      file,
      prefix,
      filter: (path) => files.includes(path) || path.endsWith("/data"),
    },
    files,
  );
  return gzipSync(await readFile(file));
}

async function catalogFor(bytes: Buffer, cacheDirectory: string) {
  const fixture = await fixtureRelease();
  const metadata = Buffer.from(
    JSON.stringify({
      ...profileFixture,
      entries_digest: operations.description.entries_digest,
      manifest_digest: fixture.release.artifacts["MANIFEST.md"]!.sha256,
    }),
  );
  const descriptor = (content: Buffer) => ({
    bytes: content.length,
    sha256: createHash("sha256").update(content).digest("hex"),
  });
  const artifacts = {
    ...fixture.release.artifacts,
    "profiles/test/profile.json": descriptor(metadata),
    "profiles/test/index.tar.gz": descriptor(bytes),
  };
  const release = { schema_version: 1 as const, artifacts, digest: releaseDigest(artifacts) };
  const url = releaseUrlFor(release.digest);
  const responses = releaseResponses({ ...fixture, release });
  responses.set(new URL("profiles/test/profile.json", url).toString(), responseBytes(metadata));
  responses.set(new URL("profiles/test/index.tar.gz", url).toString(), responseBytes(bytes));
  const requests: string[] = [];
  const catalog = await openCatalog(url, {
    cacheDirectory,
    fetch: async (input) => {
      requests.push(input.toString());
      const body = responses.get(input.toString());
      if (body === undefined) throw new Error("offline");
      return new Response(body);
    },
  });
  return { catalog, requests, responses, url };
}

describe("Node index directories", () => {
  it.skipIf(process.platform === "win32")(
    "reuses sealed generations concurrently and offline",
    async () => {
      const cache = await temporary();
      const { catalog, requests, responses, url } = await catalogFor(await archive(), cache);
      const [first, second] = await Promise.all([
        indexPath(catalog, "test"),
        indexPath(catalog, "test"),
      ]);
      expect(second).toBe(first);
      expect(await readFile(join(first, "documents.lance", "data"), "utf8")).toBe(
        "indexed documents",
      );
      expect((await lstat(first)).mode & 0o222).toBe(0);
      expect((await lstat(join(first, "documents.lance", "data"))).mode & 0o222).toBe(0);
      responses.clear();
      const offline = await openCatalog(url, {
        cacheDirectory: cache,
        fetch: async () => {
          throw new Error("offline");
        },
      });
      expect(await indexPath(offline, "test")).toBe(first);
      expect(requests.filter((path) => path.endsWith("index.tar.gz"))).toHaveLength(1);
    },
  );

  it("creates an independent writable caller directory and preserves existing directories", async () => {
    const directory = await temporary();
    const { catalog } = await catalogFor(await archive(), join(directory, "cache"));
    const target = join(directory, "working-index");
    expect(await indexPath(catalog, "test", { directory: target })).toBe(target);
    await writeFile(join(target, "documents.lance", "data"), "edited by the application");
    await expect(indexPath(catalog, "test", { directory: target })).rejects.toThrow(
      "already exists",
    );
    expect(await readFile(join(target, "documents.lance", "data"), "utf8")).toBe(
      "edited by the application",
    );
  });

  it.each([
    ["traversal", ["documents.lance"], "../escaped"],
    ["symlink", ["documents.lance/symbolic"], undefined],
    ["hardlink", ["documents.lance/data", "documents.lance/hard"], undefined],
    ["duplicate file", ["documents.lance/data", "documents.lance/data"], undefined],
    ["reserved device", ["documents.lance"], "CON"],
  ] as const)(
    "rejects %s archives and discards partial extraction",
    async (_name, files, prefix) => {
      const root = await temporary();
      const { catalog } = await catalogFor(await archive([...files], prefix), join(root, "cache"));
      const directory = join(root, "output");
      await expect(indexPath(catalog, "test", { directory })).rejects.toMatchObject({
        code: "integrity",
      });
      await expect(lstat(directory)).rejects.toMatchObject({ code: "ENOENT" });
      await expect(lstat(join(root, "escaped"))).rejects.toMatchObject({ code: "ENOENT" });
    },
  );

  it("rejects declared oversized files before allocating their content", async () => {
    const header = new Header({ path: "documents.lance/data", type: "File", size: 2_147_483_649 });
    header.encode();
    const bytes = gzipSync(header.block!);
    const root = await temporary();
    const { catalog } = await catalogFor(bytes, join(root, "cache"));
    await expect(indexPath(catalog, "test", { directory: join(root, "index") })).rejects.toThrow(
      "2 GiB",
    );
  });

  it("rejects portable case collisions before overwriting file bytes", async () => {
    const directory = await temporary();
    await writeFile(join(directory, "first"), "first value");
    await writeFile(join(directory, "second"), "second value");
    const file = join(directory, "index.tar.gz");
    await create(
      {
        cwd: directory,
        file,
        onWriteEntry: (entry) => {
          entry.path = entry.path === "first" ? "documents.lance/data" : "documents.lance/DATA";
        },
      },
      ["first", "second"],
    );
    const { catalog } = await catalogFor(gzipSync(await readFile(file)), join(directory, "cache"));
    await expect(
      indexPath(catalog, "test", { directory: join(directory, "output") }),
    ).rejects.toThrow("collide");
  });

  it("rejects nested compression", async () => {
    const root = await temporary();
    const { catalog } = await catalogFor(gzipSync(await archive()), join(root, "cache"));
    await expect(
      indexPath(catalog, "test", { directory: join(root, "index") }),
    ).rejects.toMatchObject({ code: "integrity" });
  });

  it("drains padded archives and verifies the gzip trailer after tar entries end", async () => {
    const root = await temporary();
    const padded = gzipSync(
      Buffer.concat([gunzipSync(await archive()), Buffer.alloc(1024 * 1024)]),
    );
    const { catalog } = await catalogFor(padded, join(root, "cache"));
    const path = await indexPath(catalog, "test", { directory: join(root, "index") });
    expect(await readFile(join(path, "documents.lance", "data"), "utf8")).toBe("indexed documents");
    const corrupt = Buffer.from(padded);
    corrupt[corrupt.length - 8] = corrupt[corrupt.length - 8]! ^ 1;
    const invalid = await catalogFor(corrupt, join(root, "other-cache"));
    const target = join(root, "invalid-index");
    await expect(indexPath(invalid.catalog, "test", { directory: target })).rejects.toMatchObject({
      code: "integrity",
    });
    await expect(lstat(target)).rejects.toMatchObject({ code: "ENOENT" });
  });

  it.skipIf(process.platform === "win32")(
    "keeps cancellation of a waiting caller separate from the extraction owner",
    async () => {
      const root = await temporary();
      const bytes = await archive();
      const { catalog, responses, url, requests } = await catalogFor(bytes, join(root, "cache"));
      let release = () => {};
      let started = () => {};
      const fetching = new Promise<void>((resolve) => {
        started = resolve;
      });
      responses.set(
        new URL("profiles/test/index.tar.gz", url).toString(),
        new ReadableStream<Uint8Array>({
          pull(controller) {
            started();
            return new Promise<void>((resolve) => {
              release = () => {
                controller.enqueue(bytes);
                controller.close();
                resolve();
              };
            });
          },
        }),
      );
      const owner = indexPath(catalog, "test");
      await fetching;
      const cancellation = new AbortController();
      const waiting = indexPath(catalog, "test", { signal: cancellation.signal });
      cancellation.abort();
      await expect(waiting).rejects.toMatchObject({ name: "AbortError" });
      const another = indexPath(catalog, "test");
      release();
      const path = await owner;
      expect(await another).toBe(path);
      expect(requests.filter((request) => request.endsWith("index.tar.gz"))).toHaveLength(1);
    },
  );

  it("rejects incomplete archives and archives missing the table", async () => {
    const root = await temporary();
    const bytes = await archive();
    const { catalog } = await catalogFor(bytes.subarray(0, bytes.length - 8), join(root, "cache"));
    await expect(
      indexPath(catalog, "test", { directory: join(root, "index") }),
    ).rejects.toMatchObject({ code: "integrity" });
    const missing = await catalogFor(await archive(["other.txt"]), join(root, "other-cache"));
    await expect(
      indexPath(missing.catalog, "test", { directory: join(root, "other-index") }),
    ).rejects.toMatchObject({ code: "integrity" });
  });

  it.skipIf(process.platform === "win32")(
    "replaces a changed cache generation without following its symlink",
    async () => {
      const root = await temporary();
      const { catalog } = await catalogFor(await archive(), join(root, "cache"));
      const first = await indexPath(catalog, "test");
      const table = join(first, "documents.lance");
      await chmod(table, 0o700);
      await symlink(root, join(table, "outside"));
      await chmod(table, 0o555);
      const replacement = await indexPath(catalog, "test");
      expect(replacement).not.toBe(first);
      expect(await readFile(join(replacement, "documents.lance", "data"), "utf8")).toBe(
        "indexed documents",
      );
      expect((await lstat(join(table, "outside"))).isSymbolicLink()).toBe(true);
    },
  );

  it("validates profile selection and cancellation before index I/O", async () => {
    const root = await temporary();
    const { catalog, requests } = await catalogFor(await archive(), join(root, "cache"));
    await expect(indexPath(catalog, "../test")).rejects.toMatchObject({ code: "lookup" });
    await expect(indexPath(catalog, "test", { signal: AbortSignal.abort() })).rejects.toMatchObject(
      { name: "AbortError" },
    );
    expect(requests.some((path) => path.endsWith("index.tar.gz"))).toBe(false);
  });
});
