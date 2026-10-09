import assert from "node:assert/strict";
import type { PathLike } from "node:fs";
import fs from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test } from "node:test";

// SAFETY: Eve vendors Workflow with a local world that exposes byte streams and shutdown.
const { createWorld } = (await import(
  new URL("./compiled/@workflow/world-local/index.js", import.meta.resolve("eve")).href
)) as {
  createWorld(
    this: void,
    options: { dataDir: string },
  ): {
    streams: {
      write(run: string, stream: string, content: string): Promise<void>;
      close(run: string, stream: string): Promise<void>;
      get(run: string, stream: string, cursor: number): Promise<ReadableStream<Uint8Array>>;
    };
    close(): Promise<void>;
  };
};

for (const startIndex of [0, 1]) {
  await test(`stream catch-up preserves order and deduplicates live events at cursor ${startIndex}`, async (t) => {
    const directory = await fs.mkdtemp(join(tmpdir(), "chartcoach-stream-"));
    const world = createWorld({ dataDir: directory });
    const writer = createWorld({ dataDir: directory });
    const readdir = fs.readdir;
    let stream;

    try {
      await world.streams.write("run_test", "stream_test", "initial");
      t.mock.method(
        fs,
        "readdir",
        async (path: PathLike, options?: Parameters<typeof fs.readdir>[1]) => {
          assert.equal(options, undefined, "The chunk scan requests names with default encoding");

          if (String(path) === join(directory, "streams/chunks/stream_test")) {
            fs.readdir = readdir;
            // A live event arrives while the reader catches up with persisted events.
            await world.streams.write("run_test", "stream_test", "user");
            await writer.streams.write("run_test", "stream_test", "assistant");
            await world.streams.close("run_test", "stream_test");
          }

          return readdir(path);
        },
      );

      stream = await world.streams.get("run_test", "stream_test", startIndex);
      const messages = await Array.fromAsync(stream, (chunk) => new TextDecoder().decode(chunk));
      assert.deepEqual(messages, ["initial", "user", "assistant"].slice(startIndex));
    } finally {
      fs.readdir = readdir;
      await stream?.cancel();
      await Promise.all([world.close(), writer.close()]);
      await fs.rm(directory, { recursive: true, force: true });
    }
  });
}
