import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { once } from "node:events";
import { cp, mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";

const directory = await mkdtemp(join(tmpdir(), "chartcoach-eve-output-"));
let child;
let timer;
try {
  await cp(new URL("../.output/", import.meta.url), directory, { recursive: true });
  child = spawn(process.execPath, [join(directory, "server/index.mjs")], {
    cwd: directory,
    env: {
      ...process.env,
      NODE_ENV: "production",
      NITRO_HOST: "127.0.0.1",
      NITRO_PORT: "0",
    },
    stdio: ["ignore", "pipe", "pipe"],
  });
  let output = "";
  const url = await new Promise((resolve, reject) => {
    const inspect = (chunk) => {
      output = (output + chunk.toString()).slice(-8192);
      const address = output.match(/Listening on: (http:\/\/127\.0\.0\.1:\d+\/)/)?.[1];
      if (address) resolve(address);
    };
    child.stdout.on("data", inspect);
    child.stderr.on("data", inspect);
    child.once("error", reject);
    child.once("exit", (code) => reject(new Error(`Built server exited (${code}): ${output}`)));
    timer = setTimeout(() => reject(new Error(`Built server did not start: ${output}`)), 20_000);
  });
  const health = await fetch(new URL("eve/v1/health", url), { signal: AbortSignal.timeout(5000) });
  assert.equal(health.status, 200);
  assert.equal((await health.json()).ok, true);
  const info = await fetch(new URL("eve/v1/info", url), { signal: AbortSignal.timeout(5000) });
  assert.equal(info.status, 401);
  const catalog = await fetch(new URL("eve/v1/catalog", url), {
    signal: AbortSignal.timeout(5000),
  });
  assert.equal(catalog.status, 401);
  const session = await fetch(new URL("eve/v1/session", url), {
    method: "POST",
    signal: AbortSignal.timeout(5000),
  });
  assert.equal(session.status, 401);
  const artifact = await fetch(new URL(`eve/v1/catalog/${"a".repeat(64)}/entries.parquet`, url), {
    signal: AbortSignal.timeout(5000),
  });
  assert.equal(artifact.status, 401);
  console.log("Verified relocated Eve server health and production authentication.");
} finally {
  clearTimeout(timer);
  if (child?.pid && child.exitCode === null && child.signalCode === null) {
    const exited = once(child, "exit");
    child.kill("SIGTERM");
    const force = setTimeout(() => child.kill("SIGKILL"), 6000);
    try {
      await exited;
    } finally {
      clearTimeout(force);
    }
  }
  await rm(directory, { recursive: true, force: true });
}
