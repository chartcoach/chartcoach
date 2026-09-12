import assert from "node:assert/strict";
import { execFile, spawn } from "node:child_process";
import { once } from "node:events";
import { cp, mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { promisify } from "node:util";
import { parseSkill } from "../agent/skill-source.ts";

const directory = await mkdtemp(join(tmpdir(), "chartcoach-eve-output-"));

let child;

let timer;

try {
  await cp(new URL("../.output/", import.meta.url), directory, { recursive: true });
  await promisify(execFile)(
    process.execPath,
    [
      "--input-type=module",
      "--eval",
      `
    import { SqliteClient } from "@effect/sql-sqlite-node";
    import * as Effect from "effect/Effect";
    const rows = await Effect.runPromise(Effect.gen(function* () {
      const sql = yield* SqliteClient.SqliteClient;
      return yield* sql.unsafe("SELECT 42 AS value");
    }).pipe(Effect.provide(SqliteClient.layer({ filename: ":memory:" }))));
    if (rows[0]?.value !== 42) throw new Error("SQLite query failed");
  `,
    ],
    { cwd: join(directory, "server"), timeout: 10_000 },
  );

  const manifest = JSON.parse(
    await readFile(join(directory, ".eve/compile/compiled-agent-manifest.json"), "utf8"),
  );

  const core = parseSkill(
    await readFile(new URL("../../../skills/core/SKILL.md", import.meta.url), "utf8"),
  );

  assert.ok(
    manifest.instructions.some(
      (entry) => entry.role === "system" && entry.content.includes(core.markdown),
    ),
    "Built system instructions contain the canonical core skill",
  );

  for (const name of ["discuss", "visfeedback", "visrec"]) {
    const compiled = manifest.skills.find((entry) => entry.name === name);

    const canonical = parseSkill(
      await readFile(new URL(`../../../skills/${name}/SKILL.md`, import.meta.url), "utf8"),
    );

    assert.equal(compiled?.markdown, canonical.markdown, `${name} instructions match their source`);
    assert.equal(
      compiled?.description,
      canonical.description,
      `${name} description matches its source`,
    );
  }

  assert.ok(manifest.tools.some((entry) => entry.name === "load_skill"));
  assert.ok(manifest.tools.some((entry) => entry.name === "present_answer"));

  child = spawn(process.execPath, [join(directory, "server/index.mjs")], {
    cwd: directory,
    env: {
      ...process.env,
      NODE_ENV: "production",
      EVE_DEV: "0",
      VERCEL_ENV: "production",
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

  for (const path of ["eve/v1/preferences", "eve/v1/threads"]) {
    const response = await fetch(new URL(path, url), { signal: AbortSignal.timeout(5000) });
    assert.equal(response.status, 401);
    await response.body?.cancel();
  }

  console.log(
    "Verified relocated Eve server, SQLite runtime, production authentication, and canonical skills.",
  );
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
