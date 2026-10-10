import { mkdtemp, mkdir, writeFile, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { expect, it, vi } from "vite-plus/test";
import { loadConfig } from "../runtime/config";
import { startChat } from "../runtime/start";

it("recovers abandoned locks, isolates parallel sessions, and releases their resources", async () => {
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
      storage: { dataDir: join(directory, "data's space"), cacheDir: join(directory, "cache") },
      server: { port: 0 },
    },
  });

  const log = vi.fn();
  const options = { distribution: directory, signal: new AbortController().signal, log };

  try {
    // An ungraceful exit can leave a lock that has not reached its stale threshold.
    await mkdir(config.storage.dataDir, { recursive: true });
    await mkdir(join(config.storage.dataDir, ".lock"));
    let pid: number;
    {
      await using app = await startChat(config, options);
      expect(app.dataDir).toBe(config.storage.dataDir);
      expect(await (await fetch(app.url)).text()).toBe("ChartCoach");
      expect(log).toHaveBeenCalledTimes(1);
      pid = Number(await readFile(join(config.storage.dataDir, "worker.pid"), "utf8"));

      const controller = new AbortController();
      const waiting = Promise.withResolvers<void>();

      const stopped = startChat(config, {
        ...options,
        signal: controller.signal,
        log: () => waiting.resolve(),
      });

      await Promise.race([waiting.promise, stopped]);
      controller.abort();
      await expect(stopped).rejects.toBe(controller.signal.reason);
      expect(await (await fetch(app.url)).text()).toBe("ChartCoach");

      const busy = { ...config, server: { ...config.server, port: Number(new URL(app.url).port) } };
      let session: string;
      let sessionPID: number;
      {
        await using parallel = await startChat(busy, options);
        session = parallel.dataDir;
        expect(session).toMatch(`${join(config.storage.dataDir, "sessions", "session-")}`);
        expect(parallel.url).not.toBe(app.url);
        expect(await (await fetch(parallel.url)).text()).toBe("ChartCoach");
        sessionPID = Number(await readFile(join(session, "worker.pid"), "utf8"));
        expect(sessionPID).not.toBe(pid);
        await writeFile(join(session, "saved.txt"), "independent session");
        await expect(readFile(join(app.dataDir, "saved.txt"))).rejects.toThrow();
      }

      expect(() => process.kill(sessionPID!, 0)).toThrow();
      {
        await using resumed = await startChat(
          { ...busy, storage: { ...config.storage, dataDir: session! } },
          options,
        );

        expect(resumed.dataDir).toBe(session!);
        expect(await readFile(join(resumed.dataDir, "saved.txt"), "utf8")).toBe(
          "independent session",
        );
        expect(await (await fetch(resumed.url)).text()).toBe("ChartCoach");
      }

      expect(await (await fetch(app.url)).text()).toBe("ChartCoach");

      // A fixed public URL must not silently route a second session to the first one.
      const fixed = { ...busy, server: { ...busy.server, publicURL: app.url } };
      const blocked = startChat(fixed, options);

      await expect(blocked).rejects.toThrow("still locked");
      await expect(blocked).rejects.toThrow(config.storage.dataDir);
      await expect(blocked).rejects.toThrow("Ctrl+C");
      await expect(blocked).rejects.toThrow(
        process.platform === "win32" ? "Get-CimInstance Win32_Process" : "lsof -nP -a -d cwd '",
      );

      if (process.platform !== "win32")
        await expect(blocked).rejects.toThrow("data'\"'\"'s space'");

      await expect(blocked).rejects.toThrow(
        process.platform === "win32" ? "Stop-Process -Id PID" : "kill -TERM PID",
      );
      await expect(blocked).rejects.toThrow("--data-dir <directory> --port 0");
      await expect(blocked).rejects.toThrow("choose a distinct public URL");

      await expect(
        startChat(
          { ...fixed, storage: { ...config.storage, dataDir: join(directory, "fixed") } },
          options,
        ),
      ).rejects.toThrow(`Port ${busy.server.port} is in use`);
      const failedPID = Number(await readFile(join(directory, "fixed", "worker.pid"), "utf8"));
      expect(() => process.kill(failedPID, 0)).toThrow();
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
}, 50_000);
