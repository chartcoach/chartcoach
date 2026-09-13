import { fork, type ChildProcess } from "node:child_process";
import { randomBytes } from "node:crypto";
import { mkdir } from "node:fs/promises";
import { once } from "node:events";
import { join } from "node:path";
import { z } from "zod";
import { createInterface } from "node:readline";
import lockfile from "proper-lockfile";
import { createGateway } from "./gateway";
import { validateStartup, modelKey } from "./config";
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
  signal.throwIfAborted();
  log("Loading catalog…");
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

  await using resources = new AsyncDisposableStack();

  const release = await lockfile
    .lock(config.storage.dataDir, {
      lockfilePath: join(config.storage.dataDir, ".lock"),
      onCompromised: () =>
        controller.abort(new Error("The workspace lock was lost. Restart ChartCoach.")),
    })
    .catch((error) => {
      if (error instanceof Error && "code" in error && error.code === "ELOCKED")
        throw new Error(
          "This data directory is already in use. Stop the other ChartCoach process or choose --data-dir.",
        );
      throw error;
    });

  resources.defer(release);

  const token = randomBytes(32).toString("hex");

  const secrets = [
    token,
    password,
    config.model.model ? modelKey(config) : undefined,
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
  });

  resources.defer(() => gateway.close());

  const url = await gateway.listen().catch((error) => {
    if (error instanceof Error && "code" in error && error.code === "EADDRINUSE")
      throw new Error(
        `Port ${config.server.port} is in use. Choose another --port, or use --port 0.`,
      );
    throw error;
  });

  lifetime.throwIfAborted();
  log(
    `ChartCoach is running at ${url}\n\nCatalog   ${catalog.length} guidelines · ${catalog.release.digest}\nModel     ${config.model.model ?? "Choose a connection in the browser"}\nData      ${config.storage.dataDir}\n\nPress Ctrl+C to stop.`,
  );

  const running = resources.move();

  return {
    url,
    [Symbol.asyncDispose]: () => running.disposeAsync(),
    async wait() {
      if (!lifetime.aborted) await once(lifetime, "abort");

      if (!signal.aborted) throw lifetime.reason;
    },
  };
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
