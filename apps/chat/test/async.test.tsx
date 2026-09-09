import { expect, it } from "vite-plus/test";
import { waitFor } from "../lib/async";

it("cancels one caller while another receives the shared result", async () => {
  const pending = Promise.withResolvers<string>();
  const controller = new AbortController();
  const stopped = waitFor(pending.promise, controller.signal);
  const continuing = waitFor(pending.promise, new AbortController().signal);
  controller.abort(new Error("Review stopped"));
  await expect(stopped).rejects.toThrow("Review stopped");
  pending.resolve("catalog ready");
  await expect(continuing).resolves.toBe("catalog ready");
});

it("observes initialization failures after the caller has cancelled", async () => {
  const pending = Promise.withResolvers<string>();
  const controller = new AbortController();
  const stopped = waitFor(pending.promise, controller.signal);
  controller.abort();
  await expect(stopped).rejects.toMatchObject({ name: "AbortError" });
  pending.reject(new Error("Catalog unavailable"));
  await Promise.resolve();
});

it("preserves an already-cancelled signal even when initialization settles", async () => {
  const signal = AbortSignal.abort(new Error("Review stopped"));
  await expect(waitFor(Promise.resolve("catalog ready"), signal)).rejects.toThrow("Review stopped");
  await expect(waitFor(Promise.reject(new Error("Catalog unavailable")), signal)).rejects.toThrow(
    "Review stopped",
  );
});

it("returns initialization failures to active callers", async () => {
  await expect(
    waitFor(Promise.reject(new Error("Catalog unavailable")), new AbortController().signal),
  ).rejects.toThrow("Catalog unavailable");
});
