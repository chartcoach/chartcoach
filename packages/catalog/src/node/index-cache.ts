import { randomUUID } from "node:crypto";
import { createReadStream, createWriteStream } from "node:fs";
import {
  chmod,
  lstat,
  mkdir,
  readFile,
  readdir,
  realpath,
  rename,
  rm,
  writeFile,
} from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { Transform, Writable } from "node:stream";
import { pipeline } from "node:stream/promises";
import { createGunzip } from "node:zlib";
import { Parser, type ReadEntry } from "tar";
import { CatalogError } from "../catalog/errors";
import { isJsonObject, isJsonString, parseJson } from "../catalog/json";

type Extraction = {
  archive: () => Promise<string>;
  digest: string;
  cacheDirectory: string;
  directory?: string;
  signal?: AbortSignal;
};

const pending = new Map<string, Promise<string>>();

export async function extractIndex(options: Extraction): Promise<string> {
  if (options.directory !== undefined) {
    const target = resolve(options.directory);
    const archive = await options.archive();
    await mkdir(dirname(target), { recursive: true });

    return unpack(archive, target, options.signal);
  }

  if (process.platform === "win32")
    throw new CatalogError("Protected shared index extraction is unavailable on this platform.", {
      code: "unavailable_capability",
      hints: ["Pass a new caller-owned directory to indexPath(...)."],
    });
  await mkdir(options.cacheDirectory, { recursive: true });
  const cache = await realpath(options.cacheDirectory);
  const root = join(cache, "indexes-v2", options.digest);
  const previous = pending.get(root) ?? Promise.resolve("");
  let active = false;

  const operation = (async () => {
    await previous.catch(() => "");
    active = true;
    options.signal?.throwIfAborted();

    return cachedIndex(root, options);
  })();

  pending.set(root, operation);

  const settled = () => {
    if (pending.get(root) === operation) pending.delete(root);
  };

  void operation.then(settled, settled);

  return wait(operation, () => active, options.signal);
}

async function cachedIndex(root: string, options: Extraction): Promise<string> {
  await safeDirectory(dirname(root));
  await safeDirectory(root);
  const generations = join(root, "generations");
  await safeDirectory(generations);
  const current = await currentGeneration(root, options.digest, options.signal);

  if (current) return current;
  const archive = await options.archive();
  const generation = randomUUID().replaceAll("-", "");
  const staged = join(root, `.${generation}.tmp`);
  const published = join(generations, generation);
  const pointer = join(root, `.current.${generation}.tmp`);
  let committed = false;

  try {
    await unpack(archive, staged, options.signal);
    await writeFile(join(staged, ".complete"), options.digest, { flag: "wx" });
    options.signal?.throwIfAborted();
    await rename(staged, published);
    await seal(published, options.signal);
    await writeFile(pointer, JSON.stringify({ digest: options.digest, generation }), {
      flag: "wx",
    });
    options.signal?.throwIfAborted();
    await rename(pointer, join(root, "current.json"));
    committed = true;

    return published;
  } finally {
    await rm(pointer, { force: true });
    await discard(staged);

    if (!committed) await discard(published);
  }
}

async function currentGeneration(
  root: string,
  digest: string,
  signal?: AbortSignal,
): Promise<string | undefined> {
  try {
    const pointer = join(root, "current.json");
    const status = await lstat(pointer);

    if (!status.isFile() || status.size > 1024) return undefined;
    const value = parseJson(await readFile(pointer, "utf8"));

    if (!isJsonObject(value)) return undefined;

    if (
      value.digest !== digest ||
      !isJsonString(value.generation) ||
      !/^[a-f0-9]{32}$/.test(value.generation)
    )
      return undefined;
    const target = join(root, "generations", value.generation);

    if (!(await validTree(target, signal))) return undefined;
    const marker = join(target, ".complete");
    const markerStatus = await lstat(marker);

    if (
      !markerStatus.isFile() ||
      markerStatus.size !== digest.length ||
      (await readFile(marker, "utf8")) !== digest
    )
      return undefined;

    if (!(await lstat(join(target, "documents.lance"))).isDirectory()) return undefined;

    return target;
  } catch (error) {
    signal?.throwIfAborted();

    if (error instanceof SyntaxError || (error instanceof Error && isMissing(error)))
      return undefined;
    throw error;
  }
}

async function validTree(root: string, signal?: AbortSignal): Promise<boolean> {
  let count = 0;

  const visit = async (path: string): Promise<boolean> => {
    signal?.throwIfAborted();
    const status = await lstat(path);

    if (++count > 100_002 || (status.mode & 0o222) !== 0) return false;

    if (status.isFile()) return true;

    if (!status.isDirectory()) return false;

    for (const name of await readdir(path)) if (!(await visit(join(path, name)))) return false;

    return true;
  };

  const status = await lstat(root);

  return status.isDirectory() && visit(root);
}

async function unpack(archive: string, target: string, signal?: AbortSignal): Promise<string> {
  signal?.throwIfAborted();

  try {
    await mkdir(target);
  } catch (error) {
    if (error instanceof Error && "code" in error && error.code === "EEXIST")
      throw new CatalogError("Index directory already exists. Pass a new directory.");
    throw error;
  }

  const members = new Map<string, { path: string; directory: boolean; explicit: boolean }>();
  let count = 0;
  let total = 0;
  let expanded = 0;
  let ended = false;
  const cancellation = new AbortController();

  const extractionSignal = signal
    ? AbortSignal.any([signal, cancellation.signal])
    : cancellation.signal;

  const jobs: Promise<void>[] = [];

  const extractor = new Parser({
    strict: true,
    maxMetaEntrySize: 1024 * 1024,
    // The outer gzip stream owns decompression and its byte limit.
    maxDecompressionRatio: 0,
    brotli: false,
    zstd: false,
    onReadEntry(entry) {
      const job = writeEntry(entry);
      jobs.push(job);
      void job.catch((error) => cancellation.abort(error));
    },
  });

  async function writeEntry(entry: ReadEntry): Promise<void> {
    extractionSignal.throwIfAborted();
    const directory = entry.type === "Directory";

    if (!directory && entry.type !== "File")
      throw integrity("Index archive must contain regular files and directories.");

    if (++count > 100_000) throw integrity("Index archive contains too many members.");

    if (!Number.isSafeInteger(entry.size) || entry.size < 0 || entry.size > 2 * 1024 ** 3)
      throw integrity("Index archive member exceeds the 2 GiB limit.");
    total += entry.size;

    if (total > 8 * 1024 ** 3) throw integrity("Index archive expands beyond the 8 GiB limit.");
    const parts = portablePath(entry.path, directory);

    for (let length = 1; length <= parts.length; length += 1) {
      const name = parts.slice(0, length).join("/");
      const key = name.normalize("NFKC").toUpperCase();
      const previous = members.get(key);
      const leaf = length === parts.length;

      if (
        previous &&
        (previous.path !== name ||
          !previous.directory ||
          (leaf && (!directory || previous.explicit)))
      )
        throw integrity("Index archive members collide.");

      if (!previous && members.size >= 100_000)
        throw integrity("Index archive contains too many filesystem entries.");
      members.set(key, {
        path: name,
        directory: !leaf || directory,
        explicit: leaf || previous?.explicit === true,
      });
    }

    const output = join(target, ...parts);

    if (directory) {
      await mkdir(output, { recursive: true, mode: 0o700 });
      entry.resume();
    } else {
      await mkdir(dirname(output), { recursive: true, mode: 0o700 });
      await pipeline(entry, createWriteStream(output, { flags: "wx", mode: 0o600 }), {
        signal: extractionSignal,
      });
    }
  }

  const destination = new Writable({
    write(chunk: Buffer, _encoding, callback) {
      // Parser retains chunks after tar EOF. Drain gzip separately so its
      // checksum and decompression limit still cover the complete artifact.
      if (ended) {
        callback();

        return;
      }

      try {
        if (extractor.write(chunk)) callback();
        else extractor.once("drain", callback);
      } catch (error) {
        callback(error instanceof Error ? error : new Error(String(error)));
      }
    },
    final(callback) {
      extractor.once("end", callback);

      try {
        extractor.end();
      } catch (error) {
        callback(error instanceof Error ? error : new Error(String(error)));
      }
    },
  });

  extractor.on("eof", () => {
    ended = true;
  });
  extractor.on("error", (error: Error) => destination.destroy(error));
  extractor.on("ignoredEntry", () =>
    destination.destroy(integrity("Index archive contains an unsupported or oversized member.")),
  );

  const limit = new Transform({
    transform(chunk: Buffer, _encoding, callback) {
      expanded += chunk.length;
      callback(
        expanded > 8 * 1024 ** 3 + 100_000 * 1024
          ? integrity("Index archive decompression exceeds the size limit.")
          : null,
        chunk,
      );
    },
  });

  try {
    await pipeline(createReadStream(archive), createGunzip(), limit, destination, {
      signal: extractionSignal,
    });
    await Promise.all(jobs);

    if (!(await lstat(join(target, "documents.lance"))).isDirectory())
      throw integrity("Index archive must contain the documents LanceDB table.");
    signal?.throwIfAborted();

    return target;
  } catch (error) {
    cancellation.abort(error);
    await Promise.allSettled(jobs);
    await discard(target);
    signal?.throwIfAborted();

    if (cancellation.signal.reason instanceof CatalogError) throw cancellation.signal.reason;

    if (error instanceof CatalogError) throw error;
    throw integrity("Index archive could not be extracted as a complete LanceDB database.");
  }
}

function portablePath(path: string, directory: boolean): string[] {
  const normalized = directory && path.endsWith("/") ? path.slice(0, -1) : path;
  const parts = normalized.split("/");

  if (
    Buffer.byteLength(normalized) > 4096 ||
    parts.length > 64 ||
    parts.some(
      (part) =>
        !part ||
        Buffer.byteLength(part) > 255 ||
        part === "." ||
        part === ".." ||
        /[\p{Cc}\\:<>"|?*]/u.test(part) ||
        /[. ]$/.test(part) ||
        /^(?:CON|PRN|AUX|NUL|CONIN\$|CONOUT\$|COM[1-9]|LPT[1-9])(?:\.|$)/i.test(
          part.normalize("NFKC"),
        ),
    ) ||
    parts[0]?.normalize("NFKC").toUpperCase() === ".COMPLETE"
  )
    throw integrity("Index archive contains an unsafe path.");

  return parts;
}

async function safeDirectory(path: string): Promise<void> {
  try {
    await mkdir(path);
  } catch (error) {
    if (!(error instanceof Error && "code" in error && error.code === "EEXIST")) throw error;
  }

  if (!(await lstat(path)).isDirectory())
    throw integrity("Index cache path must be a directory, not a link.");
}

async function seal(root: string, signal?: AbortSignal): Promise<void> {
  signal?.throwIfAborted();
  const status = await lstat(root);

  if (status.isDirectory()) {
    for (const name of await readdir(root)) await seal(join(root, name), signal);
    await chmod(root, 0o555);
  } else await chmod(root, 0o444);
}

async function discard(root: string): Promise<void> {
  try {
    const status = await lstat(root);

    if (status.isDirectory()) {
      await chmod(root, 0o700);

      for (const name of await readdir(root)) await discard(join(root, name));
    }

    await rm(root, { recursive: true, force: true });
  } catch (error) {
    if (!(error instanceof Error && isMissing(error))) throw error;
  }
}

function isMissing(error: Error): boolean {
  return "code" in error && error.code === "ENOENT";
}

function integrity(message: string): CatalogError {
  return new CatalogError(message, { code: "integrity" });
}

async function wait<T>(
  operation: Promise<T>,
  active: () => boolean,
  signal?: AbortSignal,
): Promise<T> {
  if (!signal) return operation;
  signal.throwIfAborted();
  let abort = () => {};

  try {
    return await Promise.race([
      operation,
      new Promise<never>((_resolve, reject) => {
        abort = () => {
          if (!active()) reject(signal.reason);
        };

        signal.addEventListener("abort", abort, { once: true });
      }),
    ]);
  } finally {
    signal.removeEventListener("abort", abort);
  }
}
