import { addAbortListener } from "node:events";

// Cancel this caller's wait while shared initialization remains available to other callers.
export async function waitFor<T>(pending: Promise<T>, signal?: AbortSignal): Promise<T> {
  if (!signal) return pending;
  const { promise, resolve, reject } = Promise.withResolvers<T>();
  const listener = addAbortListener(signal, () => reject(signal.reason));
  pending.then(resolve, reject);

  try {
    const result = await promise;
    signal.throwIfAborted();

    return result;
  } finally {
    listener[Symbol.dispose]();
  }
}
