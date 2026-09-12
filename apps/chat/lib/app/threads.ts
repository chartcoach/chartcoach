import { SqlClient } from "@effect/sql";
import { Effect } from "effect";
import { randomUUID } from "node:crypto";
import { z } from "zod";
import { threadDetailSchema, type SavedThread, type ThreadDetail } from "../../shared/preferences";
import { resolvedSelectionSchema, type ResolvedSelection } from "../../shared/resolved-selection";
import { AppError } from "./errors";

interface ThreadRow {
  id: string;
  owner: string;
  title: string;
  connection_id: string;
  session_id: string | null;
  knowledge: string;
  resolved_selection: string;
  updated_at: number;
  archived: number;
}

type ThreadMetadataRow = Pick<
  ThreadRow,
  "id" | "title" | "connection_id" | "session_id" | "updated_at" | "archived"
>;

function threadMetadata(row: ThreadMetadataRow): SavedThread {
  return {
    id: row.id,
    title: row.title,
    connectionId: row.connection_id,
    sessionId: row.session_id,
    updatedAt: row.updated_at,
    archived: row.archived === 1,
  };
}

export const listThreads = (owner: string) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;

    const rows =
      yield* sql<ThreadMetadataRow>`SELECT id, title, connection_id, session_id, updated_at, archived FROM threads WHERE owner = ${owner} ORDER BY updated_at DESC`;

    return rows.map(threadMetadata);
  });

export const getThread = (owner: string, id: string) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;
    const rows = yield* sql<ThreadRow>`SELECT * FROM threads WHERE id = ${id} AND owner = ${owner}`;
    const row = rows[0];

    if (!row) return yield* new AppError({ status: 404, message: "Conversation not found." });

    return {
      detail: threadDetailSchema.parse({
        ...threadMetadata(row),
        knowledge: JSON.parse(row.knowledge),
      }),
      resolved: resolvedSelectionSchema.parse(JSON.parse(row.resolved_selection)),
    };
  });

export const createThread = (
  owner: string,
  input: { title: string; connectionId: string; knowledge: ThreadDetail["knowledge"] },
  resolved: ResolvedSelection,
) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;
    const id = randomUUID();
    yield* sql`INSERT INTO threads ${sql.insert({ id, owner, title: input.title, connection_id: input.connectionId, knowledge: JSON.stringify({ ...input.knowledge, matchedGuidelines: resolved.ids.length }), resolved_selection: JSON.stringify(resolved), updated_at: Date.now() })}`;

    return (yield* getThread(owner, id)).detail;
  });

export const bindThread = (owner: string, id: string, sessionId: string, connectionId: string) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;
    const thread = yield* getThread(owner, id);

    if (thread.detail.sessionId && thread.detail.sessionId !== sessionId)
      return yield* new AppError({
        status: 409,
        message: "This conversation already has a session. Reopen it from history.",
      });

    const rows =
      yield* sql`UPDATE threads SET session_id=${sessionId}, connection_id=${connectionId}, updated_at=${Date.now()}
    WHERE id=${id} AND owner=${owner} AND (session_id IS NULL OR session_id=${sessionId}) RETURNING id`;

    if (!rows.length)
      return yield* new AppError({
        status: 409,
        message: "Reopen this conversation from history.",
      });
  });

export const updateThread = (
  owner: string,
  id: string,
  input: { title?: string; archived?: boolean },
) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;
    yield* getThread(owner, id);

    if (input.title !== undefined)
      yield* sql`UPDATE threads SET title=${input.title} WHERE id=${id} AND owner=${owner}`;

    if (input.archived !== undefined)
      yield* sql`UPDATE threads SET archived=${Number(input.archived)} WHERE id=${id} AND owner=${owner}`;
  });

export const imageInputSchema = z.strictObject({
  filename: z.string().min(1).max(300),
  name: z.string().min(1).max(300),
  mediaType: z.enum(["image/png", "image/jpeg", "image/webp"]),
  data: z.string().max(4_194_400),
});

export const saveImage = (
  owner: string,
  threadId: string,
  input: z.infer<typeof imageInputSchema>,
) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;
    yield* getThread(owner, threadId);
    const prefix = `data:${input.mediaType};base64,`;

    if (!input.data.startsWith(prefix))
      return yield* new AppError({ status: 400, message: "Check the chart image format." });
    const bytes = Buffer.from(input.data.slice(prefix.length), "base64");

    if (!bytes.length || bytes.length > 3 * 1024 * 1024)
      return yield* new AppError({ status: 400, message: "Choose a chart image up to 3 MiB." });
    yield* sql`INSERT INTO images ${sql.insert({ thread_id: threadId, filename: input.filename, name: input.name, media_type: input.mediaType, bytes })} ON CONFLICT(thread_id, filename) DO NOTHING`;
  });

export const getImage = (owner: string, threadId: string, filename: string) =>
  Effect.gen(function* () {
    const sql = yield* SqlClient.SqlClient;
    yield* getThread(owner, threadId);

    const rows = yield* sql<{
      bytes: Uint8Array;
      media_type: string;
    }>`SELECT bytes, media_type FROM images WHERE thread_id=${threadId} AND filename=${filename}`;

    if (!rows[0]) return yield* new AppError({ status: 404, message: "Chart image not found." });

    return rows[0];
  });
