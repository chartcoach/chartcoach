import { SqlClient } from "@effect/sql";
import { Effect, Redacted } from "effect";
import { randomUUID } from "node:crypto";
import type { Connection, ConnectionInput } from "../../shared/preferences";
import { AppError } from "./errors";
import { Secrets } from "./secrets";
import { providerEndpoint } from "./providers";
import { settings } from "../../runtime/settings";
import { modelKey } from "../../runtime/config";

interface ConnectionRow {
  id: string;
  provider: ConnectionInput["provider"];
  name: string;
  base_url: string | null;
  model: string;
  context_window: number;
  secret: string;
  auth: "api-key" | "none";
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
    auth: row.auth,
  };
}

function managedConnection(): Connection | undefined {
  return settings.model.model
    ? {
        id: "server",
        provider: settings.model.provider,
        name: "Server connection",
        model: settings.model.model,
        baseURL: providerEndpoint(settings.model),
        contextWindow: settings.model.contextWindow,
        auth: settings.model.auth,
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

    if (id === "server" && managed) {
      const key = modelKey(settings);

      if (key === undefined)
        return yield* new AppError({
          status: 503,
          message: "The server model needs its configured API key.",
        });

      return { connection: managed, key: Redacted.make(key) };
    }

    const sql = yield* SqlClient.SqlClient;

    const rows =
      yield* sql<ConnectionRow>`SELECT * FROM connections WHERE owner = ${owner} AND id = ${id}`;

    if (!rows[0])
      return yield* new AppError({ status: 404, message: "Choose an available model connection." });
    const secrets = yield* Secrets;

    return { connection: publicConnection(rows[0]), key: secrets.open(rows[0].secret, owner) };
  });

export const prepareConnection = (owner: string, input: ConnectionInput) =>
  Effect.gen(function* () {
    const endpoint = yield* Effect.try({
      try: () => providerEndpoint(input),
      catch: (error) =>
        error instanceof AppError
          ? error
          : new AppError({ status: 400, message: "Check the API base URL." }),
    });

    const previous = input.id ? yield* resolveConnection(owner, input.id) : undefined;
    const auth = input.auth ?? "api-key";

    if (auth === "none" && input.provider !== "compatible")
      return yield* new AppError({ status: 400, message: "This provider requires an API key." });

    const key =
      auth === "none"
        ? Redacted.make("")
        : input.apiKey
          ? Redacted.make(input.apiKey)
          : previous?.key;

    if (!key || (auth !== "none" && !Redacted.value(key)))
      return yield* new AppError({ status: 400, message: "Enter an API key for this connection." });

    if (
      previous &&
      auth !== "none" &&
      !input.apiKey &&
      (previous.connection.provider !== input.provider || previous.connection.baseURL !== endpoint)
    )
      return yield* new AppError({
        status: 400,
        message: "Enter the API key again when changing provider or endpoint.",
      });

    const { apiKey: _apiKey, ...connection } = input;

    return { connection: { ...connection, baseURL: endpoint, auth }, key };
  });

export const saveConnection = (owner: string, input: ConnectionInput) =>
  Effect.gen(function* () {
    const { connection, key } = yield* prepareConnection(owner, input);
    const sql = yield* SqlClient.SqlClient;
    const secrets = yield* Secrets;

    const row = {
      id: connection.id ?? randomUUID(),
      owner,
      provider: connection.provider,
      name: connection.name,
      base_url: connection.baseURL,
      model: connection.model,
      context_window: connection.contextWindow,
      secret: secrets.seal(key, owner),
      auth: connection.auth,
    };

    yield* sql`INSERT INTO connections ${sql.insert(row)} ON CONFLICT(id) DO UPDATE SET name=excluded.name, provider=excluded.provider, base_url=excluded.base_url, model=excluded.model, context_window=excluded.context_window, secret=excluded.secret, auth=excluded.auth WHERE connections.owner=excluded.owner`;

    return publicConnection(row);
  }).pipe(Effect.withSpan("connection.save"));

export const deleteConnection = (owner: string, id: string) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;
    yield* sql`DELETE FROM connections WHERE owner = ${owner} AND id = ${id}`;
  });
