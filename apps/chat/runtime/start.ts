import { fork, type ChildProcess } from "node:child_process";
import { randomBytes } from "node:crypto";
import { mkdir, mkdtemp } from "node:fs/promises";
import { once } from "node:events";
import { join } from "node:path";
import { z } from "zod";
import { createInterface } from "node:readline";
import { setTimeout as delay } from "node:timers/promises";
import lockfile from "proper-lockfile";
import { createGateway } from "./gateway";
import { embedKey, validateStartup, modelKey, embeddingKey } from "./config";
import type { Config } from "./schema";

export async function startChat(
  config: Config,
  {
    distribution,
    signal,
    log = () => {},
    verbose = false,
  }: {
    distribution: string;
    signal: AbortSignal;
    log?: (message: string) => void;
    verbose?: boolean;
  },
) {
  const password = validateStartup(config);
  const key = embedKey();
  signal.throwIfAborted();
  const { openCatalog } = await import("@chartcoach/catalog/node");

  const catalog = await openCatalog(config.catalog.source, {
    cacheDirectory: config.storage.cacheDir,
    signal: AbortSignal.any([signal, AbortSignal.timeout(60_000)]),
  });

  if (!catalog.release || !catalog.releaseUrl)
    throw new Error(
      "Chat requires a catalog release. Choose a release directory or a release.json URL.",
    );
  config = { ...config, catalog: { ...config.catalog, source: catalog.releaseUrl } };

  await mkdir(config.storage.dataDir, { recursive: true, mode: 0o700 });
  await mkdir(config.storage.cacheDir, { recursive: true, mode: 0o700 });
  const controller = new AbortController();
  const lifetime = AbortSignal.any([signal, controller.signal]);
  const local = ["127.0.0.1", "::1"].includes(config.server.host) && !config.server.publicURL;

  await using resources = new AsyncDisposableStack();

  const workspace = await lockWorkspace(
    config.storage.dataDir,
    lifetime,
    () => controller.abort(new Error("The workspace lock was lost. Restart ChartCoach.")),
    log,
    local,
  ).catch((error) => {
    lifetime.throwIfAborted();
    throw error;
  });

  resources.defer(workspace.release);
  lifetime.throwIfAborted();

  if (workspace.directory !== config.storage.dataDir)
    log(
      `Starting an independent session with separate conversations and connections.\nResume it later with --data-dir ${shellPath(workspace.directory)} --port 0.`,
    );

  config = { ...config, storage: { ...config.storage, dataDir: workspace.directory } };

  const token = randomBytes(32).toString("hex");

  const secrets = [
    token,
    password,
    key,
    config.model.model ? modelKey(config) : undefined,
    embeddingKey(config),
    process.env.LANGFUSE_SECRET_KEY,
  ].filter((value): value is string => Boolean(value));

  const child = fork(join(distribution, "server/index.mjs"), [], {
    cwd: config.storage.dataDir,
    execArgv: [],
    silent: true,
    env: {
      ...process.env,
      NODE_ENV: "production",
      EVE_DEV: "0",
      VERCEL: "",
      VERCEL_ENV: "",
      CHARTCOACH_RUNTIME_CONFIG: JSON.stringify(config),
      CHARTCOACH_RUNTIME_TOKEN: token,
      CHARTCOACH_SANDBOX_PLAN: join(distribution, "sandbox.json"),
      WORKFLOW_LOCAL_BASE_URL: "",
    },
  });

  const diagnostics: string[] = [];
  const lines = createInterface({ input: child.stderr! });
  lines.on("line", (line) => {
    for (const secret of secrets) line = line.replaceAll(secret, "[redacted]");
    diagnostics.push(line.slice(-4096));

    if (diagnostics.length > 12) diagnostics.shift();

    if (verbose) log(`[runtime] ${line}`);
  });
  const exited = new Promise<void>((resolve) => child.once("exit", () => resolve()));
  child.once("error", () =>
    controller.abort(
      new Error("Could not start the chat runtime. Check the Node.js installation."),
    ),
  );
  child.once("exit", (code) =>
    controller.abort(
      new Error(
        `The chat runtime stopped (${code ?? "signal"}). ${diagnostics.join("\n") || "Run chartcoach doctor to check the installation."}`,
      ),
    ),
  );
  resources.defer(async () => {
    if (child.pid && child.exitCode === null && child.signalCode === null) {
      if (child.connected) child.disconnect();
      else child.kill("SIGTERM");
      const force = setTimeout(() => child.kill("SIGKILL"), 5000);

      try {
        await exited;
      } finally {
        clearTimeout(force);
      }
    }

    lines.close();
    child.stdin?.destroy();
    child.stdout?.destroy();
    child.stderr?.destroy();
  });

  const agentURL = await workerURL(child, AbortSignal.any([lifetime, AbortSignal.timeout(60_000)]));

  const gateway = createGateway({
    config,
    assets: join(distribution, "public"),
    agentURL,
    token,
    password,
    embedKey: key,
  });

  resources.defer(() => gateway.close());

  const url = await gateway.listen().catch((error) => {
    if (error instanceof Error && "code" in error && error.code === "EADDRINUSE") {
      if (local) {
        log(`Port ${config.server.port} is in use; choosing an available port…`);

        return gateway.listen(0);
      }

      throw new Error(
        `Port ${config.server.port} is in use. Choose another --port, or use --port 0.`,
      );
    }

    throw error;
  });

  lifetime.throwIfAborted();
  const running = resources.move();

  return {
    url,
    dataDir: config.storage.dataDir,
    catalog: { guidelines: catalog.length, digest: catalog.release.digest },
    [Symbol.asyncDispose]: () => running.disposeAsync(),
    async wait() {
      if (!lifetime.aborted) await once(lifetime, "abort");

      if (!signal.aborted) throw lifetime.reason;
    },
  };
}

async function lockWorkspace(
  directory: string,
  signal: AbortSignal,
  onCompromised: () => void,
  log: (message: string) => void,
  parallel: boolean,
) {
  // Cover the lock's 10-second stale threshold and filesystem timestamp rounding.
  for (let attempt = 0; ; attempt++) {
    signal.throwIfAborted();

    try {
      const release = await lockfile.lock(directory, {
        lockfilePath: join(directory, ".lock"),
        onCompromised,
      });

      return { directory, release };
    } catch (error) {
      if (!(error instanceof Error && "code" in error && error.code === "ELOCKED")) throw error;

      if (attempt === 12) {
        if (parallel) {
          const sessions = join(directory, "sessions");
          await mkdir(sessions, { recursive: true, mode: 0o700 });
          const session = await mkdtemp(join(sessions, "session-"));
          signal.throwIfAborted();

          const release = await lockfile.lock(session, {
            lockfilePath: join(session, ".lock"),
            onCompromised,
          });

          return { directory: session, release };
        }

        const windows = process.platform === "win32";

        const find = windows
          ? "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*chartcoach*' } | Select-Object ProcessId, CommandLine"
          : `lsof -nP -a -d cwd ${shellPath(directory)}`;

        const stop = windows ? "Stop-Process -Id PID" : "kill -TERM PID";

        throw new Error(
          [
            `The data directory is still locked:\n  ${directory}`,
            `Press Ctrl+C in the other ChartCoach terminal, or find its background runtime${windows ? " in PowerShell" : ""}:`,
            `  ${find}`,
            ...(windows ? [] : ["Inspect the listed PID: ps -p PID -o command="]),
            `Stop ChartCoach with ${stop}, replacing PID with its process ID, then retry.`,
            "PID is a process ID, not a port number.",
            "For a separate session, use --data-dir <directory> --port 0.",
            "If --public-url is configured, choose a distinct public URL for that session.",
          ].join("\n"),
        );
      }

      if (attempt === 0) log("Waiting for the previous ChartCoach session to release its data…");
    }

    await delay(1000, undefined, { signal });
  }
}

function shellPath(directory: string) {
  return `'${directory.replaceAll("'", process.platform === "win32" ? "''" : "'\"'\"'")}'`;
}

async function workerURL(child: ChildProcess, signal: AbortSignal) {
  const ready = Promise.withResolvers<string>();
  const messageSchema = z.object({ type: z.literal("ready"), url: z.url() });

  const receive = (message: Parameters<NonNullable<typeof child.send>>[0]) => {
    const parsed = messageSchema.safeParse(message);

    if (parsed.success) ready.resolve(parsed.data.url);
    else ready.reject(new Error("The chat runtime sent an invalid readiness message."));
  };

  const abort = () => ready.reject(signal.reason);
  child.on("message", receive);
  child.stdout!.resume();
  signal.addEventListener("abort", abort, { once: true });

  try {
    signal.throwIfAborted();

    return await ready.promise;
  } finally {
    signal.removeEventListener("abort", abort);
    child.off("message", receive);
  }
}
