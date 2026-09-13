import { SqlClient, Migrator } from "@effect/sql";
import { sqliteLayer } from "./sqlite";
import { Effect, Layer } from "effect";
import { mkdir } from "node:fs/promises";
import { dirname } from "node:path";

const initialSchema = Effect.gen(function* () {
  const sql = yield* SqlClient.SqlClient;
  yield* sql`CREATE TABLE connections (
    id TEXT PRIMARY KEY, owner TEXT NOT NULL, provider TEXT NOT NULL,
    name TEXT NOT NULL, base_url TEXT, model TEXT NOT NULL,
    context_window INTEGER NOT NULL, secret TEXT NOT NULL
  )`;
  yield* sql`CREATE INDEX connections_owner ON connections(owner)`;
  yield* sql`CREATE TABLE threads (
    id TEXT PRIMARY KEY, owner TEXT NOT NULL, title TEXT NOT NULL,
    connection_id TEXT NOT NULL, session_id TEXT UNIQUE,
    knowledge TEXT NOT NULL, resolved_selection TEXT NOT NULL,
    updated_at INTEGER NOT NULL, archived INTEGER NOT NULL DEFAULT 0
  )`;
  yield* sql`CREATE INDEX threads_owner ON threads(owner, updated_at DESC)`;
  yield* sql`CREATE TABLE images (
    thread_id TEXT NOT NULL REFERENCES threads(id) ON DELETE CASCADE,
    filename TEXT NOT NULL, name TEXT NOT NULL, media_type TEXT NOT NULL, bytes BLOB NOT NULL,
    PRIMARY KEY(thread_id, filename)
  )`;
});

export function databaseLayer(filename: string) {
  const sqlite = Layer.unwrapEffect(
    Effect.promise(() => mkdir(dirname(filename), { recursive: true, mode: 0o700 })).pipe(
      Effect.as(sqliteLayer(filename)),
    ),
  );

  const migrate = Layer.effectDiscard(
    Effect.gen(function* () {
      const sql = yield* SqlClient.SqlClient;
      yield* sql`PRAGMA foreign_keys = ON`;
      yield* sql`PRAGMA busy_timeout = 5000`;
      yield* Migrator.make({})({
        loader: Migrator.fromRecord({
          "001_app": initialSchema,
          "002_connection_auth": Effect.gen(function* () {
            const sql = yield* SqlClient.SqlClient;
            yield* sql`ALTER TABLE connections ADD COLUMN auth TEXT NOT NULL DEFAULT 'api-key'`;
          }),
        }),
      });
    }),
  );

  return migrate.pipe(Layer.provideMerge(sqlite));
}
