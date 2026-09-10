import { SqlClient } from "@effect/sql";
import { Effect, Redacted } from "effect";
import { randomUUID } from "node:crypto";
import type { Connection, ConnectionInput } from "../../shared/preferences";
import { AppError } from "./errors";
import { Secrets } from "./secrets";
import { providerEndpoint } from "./providers";
import { env } from "../env";

interface ConnectionRow {
  id: string;
  provider: ConnectionInput["provider"];
  name: string;
  base_url: string | null;
  model: string;
  context_window: number;
  secret: string;
}
function publicConnection(row: ConnectionRow): Connection {
  return {
    id: row.id,
    provider: row.provider,
    name: row.name,
    baseURL: row.base_url ?? undefined,
    model: row.model,
    contextWindow: row.context_window,
    managed: false,
  };
}
function managedConnection(): Connection | undefined {
  return env.OPENAI_API_KEY
    ? {
        id: "server",
        provider: env.OPENAI_BASE ? "compatible" : "openai",
        name: "Server connection",
        model: env.OPENAI_MODEL,
        contextWindow: 128_000,
        managed: true,
      }
    : undefined;
}
export const listConnections = (owner: string) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;
    const rows =
      yield* sql<ConnectionRow>`SELECT * FROM connections WHERE owner = ${owner} ORDER BY name`;
    const managed = managedConnection();
    return [...(managed ? [managed] : []), ...rows.map(publicConnection)];
  });
export const resolveConnection = (owner: string, id: string) =>
  Effect.gen(function* () {
    const managed = managedConnection();
    if (id === "server" && managed && env.OPENAI_API_KEY)
      return { connection: managed, key: Redacted.make(env.OPENAI_API_KEY) };
    const sql = yield* SqlClient.SqlClient;
    const rows =
      yield* sql<ConnectionRow>`SELECT * FROM connections WHERE owner = ${owner} AND id = ${id}`;
    if (!rows[0])
      return yield* new AppError({ status: 404, message: "Choose an available model connection." });
    const secrets = yield* Secrets;
    return { connection: publicConnection(rows[0]), key: secrets.open(rows[0].secret, owner) };
  });
export const saveConnection = (owner: string, input: ConnectionInput) =>
  Effect.gen(function* () {
    const endpoint = yield* Effect.try({
      try: () => providerEndpoint(input),
      catch: (error) =>
        error instanceof AppError
          ? error
          : new AppError({ status: 400, message: "Check the API base URL." }),
    });
    const sql = yield* SqlClient.SqlClient;
    const secrets = yield* Secrets;
    const id = input.id ?? randomUUID();
    const previous = input.id ? yield* resolveConnection(owner, id) : undefined;
    const key = input.apiKey ? Redacted.make(input.apiKey) : previous?.key;
    if (!key)
      return yield* new AppError({ status: 400, message: "Enter an API key for this connection." });
    if (
      previous &&
      !input.apiKey &&
      (previous.connection.provider !== input.provider || previous.connection.baseURL !== endpoint)
    )
      return yield* new AppError({
        status: 400,
        message: "Enter the API key again when changing provider or endpoint.",
      });
    const row = {
      id,
      owner,
      provider: input.provider,
      name: input.name,
      base_url: endpoint,
      model: input.model,
      context_window: input.contextWindow,
      secret: secrets.seal(key, owner),
    };
    yield* sql`INSERT INTO connections ${sql.insert(row)} ON CONFLICT(id) DO UPDATE SET name=excluded.name, provider=excluded.provider, base_url=excluded.base_url, model=excluded.model, context_window=excluded.context_window, secret=excluded.secret WHERE connections.owner=excluded.owner`;
    return publicConnection(row);
  }).pipe(Effect.withSpan("connection.save"));
export const deleteConnection = (owner: string, id: string) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;
    yield* sql`DELETE FROM connections WHERE owner = ${owner} AND id = ${id}`;
  });
