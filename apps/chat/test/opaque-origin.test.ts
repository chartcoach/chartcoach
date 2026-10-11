import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { runInNewContext } from "node:vm";
import { test } from "node:test";

const source = await readFile(new URL("../browser/opaque-origin.ts", import.meta.url), "utf8");

await test("keeps Next navigation and workspace fetches authenticated inside an opaque frame", async () => {
  const calls: { input: RequestInfo; init?: RequestInit }[] = [];

  const frame = {
    origin: "null",
    location: new URL("https://chat.example/chat/c3666202-50b1-449c-ac0c-9d458e936f92"),
    URL,
    Request,
    fetch: async (input: RequestInfo, init?: RequestInit) => {
      calls.push({ input, init });

      return new Response();
    },
  };

  runInNewContext(source, frame);
  await frame.fetch("/guidelines", { credentials: "same-origin", headers: { rsc: "1" } });
  await frame.fetch("/eve/v1/threads");
  await frame.fetch("https://other.example/catalog", { credentials: "omit" });
  assert.equal(calls[0]?.init?.credentials, "include");
  assert.deepEqual(calls[0]?.init?.headers, { rsc: "1" });
  assert.equal(calls[1]?.init?.credentials, "include");
  assert.equal(calls[2]?.init?.credentials, "omit");
});
