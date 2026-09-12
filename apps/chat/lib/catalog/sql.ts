import { StatementType, type DuckDBInstance, type DuckDBResult } from "@duckdb/node-api";

export const sqlTimeoutMs = 5_000;

export async function withSelect<T>(
  db: DuckDBInstance,
  sql: string,
  consume: (result: DuckDBResult) => Promise<T>,
  signal?: AbortSignal,
): Promise<T> {
  const connection = await db.connect();
  let timedOut = false;
  const abort = () => connection.interrupt();

  const timeout = setTimeout(() => {
    timedOut = true;
    connection.interrupt();
  }, sqlTimeoutMs);

  signal?.addEventListener("abort", abort, { once: true });

  try {
    signal?.throwIfAborted();
    await connection.run("BEGIN TRANSACTION READ ONLY");
    const statements = await connection.extractStatements(sql);

    if (statements.count !== 1) throw new Error("Submit exactly one SELECT query.");
    const prepared = await statements.prepare(0);

    try {
      if (prepared.statementType !== StatementType.SELECT)
        throw new Error("Submit a SELECT query. Catalog SQL is read-only.");

      if (prepared.parameterCount) throw new Error("Include literal values in the SQL query.");
      const value = await consume(await prepared.stream());
      signal?.throwIfAborted();

      if (timedOut) throw new Error("SQL exceeded 5 seconds. Narrow the query and try again.");

      return value;
    } finally {
      prepared.destroySync();
    }
  } catch (error) {
    signal?.throwIfAborted();

    if (timedOut) throw new Error("SQL exceeded 5 seconds. Narrow the query and try again.");
    throw error;
  } finally {
    clearTimeout(timeout);
    signal?.removeEventListener("abort", abort);
    connection.interrupt();
    connection.closeSync();
  }
}
