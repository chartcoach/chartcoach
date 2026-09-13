import { modelKey, validateStartup } from "./config";
import type { Config } from "./schema";

export async function diagnose(config: Config, version: string) {
  validateStartup(config);
  const { openCatalog } = await import("@chartcoach/catalog/node");

  const catalog = await openCatalog(config.catalog.source, {
    cacheDirectory: config.storage.cacheDir,
    signal: AbortSignal.timeout(30_000),
  });

  const info = await catalog.describe();
  const { DuckDBInstance } = await import("@duckdb/node-api");
  const db = await DuckDBInstance.create(":memory:");
  const connection = await db.connect();

  try {
    await connection.run("SELECT 1");
  } finally {
    connection.closeSync();
    db.closeSync();
  }

  const { SqliteClient } = await import("@effect/sql-sqlite-node");
  const { Effect } = await import("effect");
  await Effect.runPromise(
    Effect.gen(function* () {
      const sql = yield* SqliteClient.SqliteClient;
      yield* sql.unsafe("SELECT 1");
    }).pipe(Effect.provide(SqliteClient.layer({ filename: ":memory:" }))),
  ).catch(() => {
    throw new Error(
      "SQLite could not load. If npm disables install scripts, install with npm install --ignore-scripts=false chartcoach so its SQLite binding can be installed.",
    );
  });
  await Promise.all([import("@lancedb/lancedb"), import("@huggingface/transformers")]);

  return {
    ok: true,
    version,
    node: process.version,
    storage: config.storage,
    catalog: {
      source: config.catalog.source,
      digest: info.release_digest ?? null,
      guidelines: catalog.length,
      profile: config.catalog.profile,
    },
    model: {
      provider: config.model.provider,
      model: config.model.model ?? null,
      baseURL: config.model.baseURL ?? null,
      configured: Boolean(config.model.model),
      credentialAvailable: config.model.auth === "none" || Boolean(modelKey(config)),
    },
    runtime: { duckdb: true, sqlite: true, lancedb: true, embeddings: true },
  };
}
