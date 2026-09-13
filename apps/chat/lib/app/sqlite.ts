import { DatabaseSync, type SQLInputValue, type StatementSync } from "node:sqlite";
import * as Reactivity from "@effect/experimental/Reactivity";
import * as Client from "@effect/sql/SqlClient";
import type { Connection } from "@effect/sql/SqlConnection";
import { SqlError } from "@effect/sql/SqlError";
import * as Statement from "@effect/sql/Statement";
import { Effect, Layer, Stream } from "effect";
import { z } from "zod";

const parameters = z.array(
  z.union([
    z.null(),
    z.string(),
    z.number(),
    z.bigint(),
    z.custom<NodeJS.ArrayBufferView>((value) => ArrayBuffer.isView(value)),
  ]),
);

export function sqliteLayer(filename: string) {
  return Layer.scoped(
    Client.SqlClient,
    Effect.gen(function* () {
      const db = yield* Effect.acquireRelease(
        Effect.try({
          try: () => new DatabaseSync(filename),
          catch: (cause) => new SqlError({ cause, message: "Could not open the chat database." }),
        }),
        (database) => Effect.sync(() => database.close()),
      );

      yield* Effect.try({
        try: () => db.exec("PRAGMA journal_mode = WAL"),
        catch: (cause) =>
          new SqlError({ cause, message: "Could not configure the chat database." }),
      });

      const statement = <A>(
        sql: string,
        params: readonly unknown[],
        run: (prepared: StatementSync, values: SQLInputValue[]) => A,
      ) =>
        Effect.gen(function* () {
          const safeIntegers = yield* Client.SafeIntegers;

          return yield* Effect.try({
            try: () => {
              const prepared = db.prepare(sql);
              prepared.setReadBigInts(safeIntegers);

              return run(prepared, parameters.parse(params));
            },
            catch: (cause) =>
              new SqlError({ cause, message: "Could not execute the SQLite query." }),
          });
        });

      const execute: Connection["execute"] = (sql, params, transformRows) => {
        const rows = statement(sql, params, (prepared, values) => prepared.all(...values));

        return transformRows ? Effect.map(rows, transformRows) : rows;
      };

      const connection: Connection = {
        execute,
        executeUnprepared: execute,
        executeRaw: (sql, params) =>
          statement(sql, params, (prepared, values) =>
            prepared.columns().length ? prepared.all(...values) : prepared.run(...values),
          ),
        executeValues: (sql, params) =>
          statement(sql, params, (prepared, values) => {
            prepared.setReturnArrays(true);

            // Node's declarations do not reflect the setReturnArrays return type.
            return z.array(z.array(z.unknown())).parse(prepared.all(...values));
          }),
        executeStream: (sql, params, transformRows) =>
          Stream.unwrap(Effect.map(execute(sql, params, transformRows), Stream.fromIterable)),
      };

      const semaphore = yield* Effect.makeSemaphore(1);

      const acquirer = Effect.acquireRelease(Effect.interruptible(semaphore.take(1)), () =>
        semaphore.release(1),
      ).pipe(Effect.as(connection));

      return yield* Client.make({
        acquirer,
        compiler: Statement.makeCompilerSqlite(),
        spanAttributes: [["db.system.name", "sqlite"]],
      });
    }),
  ).pipe(Layer.provide(Reactivity.layer));
}
