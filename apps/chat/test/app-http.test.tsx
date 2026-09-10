import { expect, it } from "vite-plus/test";
import { Effect } from "effect";
import { z } from "zod";
import { checkOrigin, readJson } from "../lib/app/http";
import { connectionInputSchema } from "../shared/preferences";

it("rejects cross-origin credential mutations including same-site subdomains", () => {
  expect(() =>
    checkOrigin(
      new Request("https://chat.example/settings", {
        headers: { origin: "https://other.example", "sec-fetch-site": "same-site" },
      }),
    ),
  ).toThrow("Open these settings");
  expect(() =>
    checkOrigin(
      new Request("https://chat.example/settings", { headers: { "sec-fetch-site": "cross-site" } }),
    ),
  ).toThrow("Open these settings");
  expect(() =>
    checkOrigin(
      new Request("http://127.0.0.1/settings", {
        headers: { origin: "https://chat.example", "x-forwarded-host": "chat.example" },
      }),
    ),
  ).not.toThrow();
});

it("rejects keys containing header control characters before provider access", async () => {
  const request = new Request("https://chat.example/settings", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      provider: "openai",
      name: "Work",
      model: "vision",
      apiKey: "private\nkey",
    }),
  });
  await expect(Effect.runPromise(readJson(request, connectionInputSchema))).rejects.toThrow(
    "Check the submitted fields",
  );
});

it("bounds credential request bytes before parsing and keeps bad input private", async () => {
  const request = (body: string) =>
    new Request("https://chat.example/settings", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body,
    });
  await expect(
    Effect.runPromise(
      readJson(
        request(JSON.stringify({ key: "sensitive-value" })),
        z.object({ key: z.string() }),
        10,
      ),
    ),
  ).rejects.toThrow("too large");
  const malformed = Effect.runPromise(
    readJson(request("sensitive-value"), z.object({ key: z.string() })),
  );
  await expect(malformed).rejects.toThrow("Check the submitted fields");
  await expect(malformed).rejects.not.toThrow("sensitive-value");
});
