import { mkdtemp, mkdir, writeFile, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { expect, it } from "vite-plus/test";
import { loadConfig } from "../runtime/config";
import { startChat } from "../runtime/start";

it("releases the worker and workspace on scope exit and startup failure", async () => {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-lifecycle-"));
  await mkdir(join(directory, "server"));
  await mkdir(join(directory, "public"));
  await writeFile(join(directory, "public/index.html"), "ChartCoach");
  const entry = join(directory, "server/index.mjs");

  const worker = `
    import { createServer } from "node:http";
    import { writeFileSync } from "node:fs";
    writeFileSync("worker.pid", String(process.pid));
    const server = createServer((req, res) => res.end("ready"));
    server.listen(0, "127.0.0.1", () => process.send({ type: "ready", url: "http://127.0.0.1:" + server.address().port }));
    process.once("disconnect", () => server.close(() => process.exit(0)));
  `;

  await writeFile(entry, worker);

  const config = loadConfig({
    environment: {},
    userConfig: join(directory, "absent.json"),
    overrides: {
      catalog: { source: new URL("../../../fixtures/catalog-release", import.meta.url).href },
      storage: { dataDir: join(directory, "data"), cacheDir: join(directory, "cache") },
      server: { port: 0 },
    },
  });

  const options = { distribution: directory, signal: new AbortController().signal };

  try {
    let pid: number;
    {
      await using app = await startChat(config, options);
      expect(await (await fetch(app.url)).text()).toBe("ChartCoach");
      pid = Number(await readFile(join(config.storage.dataDir, "worker.pid"), "utf8"));
      await expect(startChat(config, options)).rejects.toThrow("already in use");
    }

    expect(() => process.kill(pid!, 0)).toThrow();
    await writeFile(entry, 'process.stderr.write("startup failed\\n"); process.exit(1);');
    await expect(startChat(config, options)).rejects.toThrow("startup failed");
    await writeFile(entry, worker);
    await using recovered = await startChat(config, options);
    expect(await (await fetch(recovered.url)).text()).toBe("ChartCoach");
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
}, 20_000);
