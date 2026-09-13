import assert from "node:assert/strict";
import fs from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test } from "node:test";

// Eve vendors Workflow. Exercise the patched reader at its actual dependency boundary.
const { createWorld } = await import(
  new URL("./compiled/@workflow/world-local/index.js", import.meta.resolve("eve"))
);

for (const startIndex of [0, 1]) {
  await test(`stream catch-up preserves order and deduplicates live events at cursor ${startIndex}`, async () => {
    const directory = await fs.mkdtemp(join(tmpdir(), "chartcoach-stream-"));
    const world = createWorld({ dataDir: directory });
    const writer = createWorld({ dataDir: directory });
    const readdir = fs.readdir;
    let stream;

    try {
      await world.streams.write("run_test", "stream_test", "initial");
      fs.readdir = async (...args) => {
        if (String(args[0]) === join(directory, "streams/chunks/stream_test")) {
          fs.readdir = readdir;
          // A live event arrives while the reader catches up with persisted events.
          await world.streams.write("run_test", "stream_test", "user");
          await writer.streams.write("run_test", "stream_test", "assistant");
          await world.streams.close("run_test", "stream_test");
        }

        return readdir(...args);
      };

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
