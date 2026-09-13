import { openCatalog } from "@chartcoach/catalog";
import { registerCatalog } from "@chartcoach/catalog/duckdb-wasm";
import { AsyncDuckDB, VoidLogger, getPlatformFeatures } from "@duckdb/duckdb-wasm";
import { Coordinator, wasmConnector } from "@uwdata/mosaic-core";

async function stage<T>(name: string, operation: () => Promise<T>): Promise<T> {
  try {
    return await operation();
  } catch (cause) {
    throw new Error(`${name}: ${cause instanceof Error ? cause.message : String(cause)}`, {
      cause,
    });
  }
}

export async function openBrowserCatalog(
  catalogId: string,
  signal: AbortSignal,
  onFailure: (error: Error) => void,
) {
  signal = AbortSignal.any([signal, AbortSignal.timeout(60_000)]);
  signal.throwIfAborted();
  const features = await getPlatformFeatures();
  signal.throwIfAborted();

  if (!features.wasmExceptions)
    throw new Error(
      "Catalog exploration needs WebAssembly exception handling. Update your browser and try again.",
    );
  const worker = new Worker("/duckdb/duckdb-browser-eh.worker.js");
  const db = new AsyncDuckDB(new VoidLogger(), worker);
  const interrupted = Promise.withResolvers<never>();
  let coordinator: Coordinator | undefined;
  let closed = false;
  let ready = false;

  const close = () => {
    if (closed) return;
    closed = true;

    try {
      coordinator?.clear();
    } finally {
      worker.removeEventListener("error", failed);
      worker.removeEventListener("messageerror", failed);
      // This owner disposes the entire in-memory database, including unresponsive connections.
      worker.terminate();
    }
  };

  function failed(event: Event) {
    if (closed) return;

    const error = new Error("The local catalog worker stopped. Retry to reload it.", {
      cause: event instanceof ErrorEvent ? (event.error ?? event.message) : event,
    });

    close();
    interrupted.reject(error);

    if (ready) onFailure(error);
  }

  const abort = () => {
    close();
    interrupted.reject(signal.reason);
  };

  worker.addEventListener("error", failed);
  worker.addEventListener("messageerror", failed);
  signal.addEventListener("abort", abort, { once: true });

  try {
    const catalogPromise = stage("Loading catalog records", () =>
      openCatalog(new URL(`/eve/v1/catalog/${catalogId}/release.json`, location.origin), {
        signal,
      }),
    );

    const [catalog] = await Promise.race([
      Promise.all([
        catalogPromise,
        stage("Starting DuckDB", () => db.instantiate("/duckdb/duckdb-eh.wasm")),
      ]),
      interrupted.promise,
    ]);

    const connection = await Promise.race([db.connect(), interrupted.promise]);
    await Promise.race([
      (async () => {
        await stage("Registering catalog tables", () => registerCatalog(connection, catalog));
        await stage("Opening Parquet", async () =>
          db.registerFileBuffer(
            "entries.parquet",
            await catalog.artifact("entries.parquet", { signal }),
          ),
        );
        await stage("Reading Parquet", () =>
          connection.query(
            "CREATE TABLE catalog_entries AS SELECT id, title, description FROM read_parquet('entries.parquet')",
          ),
        );
      })(),
      interrupted.promise,
    ]);
    signal.throwIfAborted();
    coordinator = new Coordinator(wasmConnector({ duckdb: db, connection }), {
      logger: null,
      preagg: { enabled: false },
    });
    ready = true;

    return { coordinator, close };
  } catch (error) {
    close();
    throw error;
  } finally {
    signal.removeEventListener("abort", abort);
  }
}
