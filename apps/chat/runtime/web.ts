import next from "next";
import { addAbortListener } from "node:events";

/** Serve the packaged App Router with its own production configuration. */
export async function prepareWeb(directory: string, signal: AbortSignal) {
  signal.throwIfAborted();
  const app = next({ dev: false, dir: directory });
  const preparation = app.prepare();
  const aborted = Promise.withResolvers<never>();
  using _listener = addAbortListener(signal, () => aborted.reject(signal.reason));

  try {
    await Promise.race([preparation, aborted.promise]);
    signal.throwIfAborted();
  } catch (error) {
    if (signal.aborted) {
      // Preparation cannot be interrupted by Next. Release a late server while
      // allowing the caller to stop its worker and release the workspace now.
      void preparation
        .then(
          () => app.close(),
          () => app.close(),
        )
        .catch(() => {});
    } else {
      await app.close();
    }

    throw error;
  }

  return {
    handle: app.getRequestHandler(),
    close: () => app.close(),
  };
}
