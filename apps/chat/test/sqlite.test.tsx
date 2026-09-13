import { SqlClient } from "@effect/sql";
import { Deferred, Effect, Fiber, FiberStatus, ManagedRuntime, Stream } from "effect";
import { expect, it } from "vite-plus/test";
import { sqliteLayer } from "../lib/app/sqlite";

it("round-trips SQLite values and rolls back failed transactions through Effect", async () => {
  const runtime = ManagedRuntime.make(sqliteLayer(":memory:"));

  try {
    await runtime.runPromise(
      Effect.gen(function* () {
        const sql = yield* SqlClient.SqlClient;
        yield* sql`CREATE TABLE values_test (id INTEGER PRIMARY KEY, text TEXT, bytes BLOB, optional TEXT)`;
        const bytes = new Uint8Array([0, 1, 255]);
        expect(
          yield* sql`INSERT INTO values_test (text, bytes, optional) VALUES (${"labels"}, ${bytes}, ${null})`
            .raw,
        ).toMatchObject({ changes: 1, lastInsertRowid: 1 });
        expect(yield* sql`SELECT text, bytes, optional FROM values_test`).toEqual([
          { text: "labels", bytes, optional: null },
        ]);
        expect(yield* sql`SELECT id, id FROM values_test`.values).toEqual([[1, 1]]);
        expect(
          yield* sql`SELECT ${9007199254740993n} AS value`.pipe(
            Effect.provideService(SqlClient.SafeIntegers, true),
          ),
        ).toEqual([{ value: 9007199254740993n }]);
        expect(yield* sql`SELECT id FROM values_test`).toEqual([{ id: 1 }]);
        expect(
          Array.from(yield* Stream.runCollect(sql`SELECT text FROM values_test`.stream)),
        ).toEqual([{ text: "labels" }]);
        yield* sql
          .withTransaction(
            Effect.gen(function* () {
              yield* sql`INSERT INTO values_test (text) VALUES (${"rolled back"})`;

              return yield* Effect.fail("cancel write");
            }),
          )
          .pipe(Effect.catchAll(() => Effect.void));
        expect(yield* sql`SELECT text FROM values_test`).toEqual([{ text: "labels" }]);
      }),
    );
  } finally {
    await runtime.dispose();
  }
});

it("isolates concurrent queries and releases a cancelled transaction's connection", async () => {
  const runtime = ManagedRuntime.make(sqliteLayer(":memory:"));

  try {
    await runtime.runPromise(
      Effect.gen(function* () {
        const sql = yield* SqlClient.SqlClient;
        yield* sql`CREATE TABLE writes (name TEXT)`;
        const entered = yield* Deferred.make<void>();

        const transaction = yield* Effect.fork(
          sql.withTransaction(
            Effect.gen(function* () {
              yield* sql`INSERT INTO writes VALUES (${"inside"})`;
              yield* Deferred.succeed(entered, undefined);
              yield* Effect.never;
            }),
          ),
        );

        yield* Deferred.await(entered);
        const outside = yield* Effect.fork(sql`INSERT INTO writes VALUES (${"outside"})`);
        yield* Effect.yieldNow();
        expect(FiberStatus.isSuspended(yield* Fiber.status(outside))).toBe(true);
        yield* Fiber.interrupt(transaction);
        yield* Fiber.join(outside);
        expect(yield* sql`SELECT name FROM writes`).toEqual([{ name: "outside" }]);
      }).pipe(Effect.timeout("5 seconds")),
    );
  } finally {
    await runtime.dispose();
  }
});
