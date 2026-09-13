import { mkdtemp, readFile, rm, stat } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { expect, it } from "vite-plus/test";
import { Redacted } from "effect";
import { createAppRuntime } from "../lib/app/runtime";
import {
  deleteConnection,
  listConnections,
  resolveConnection,
  saveConnection,
} from "../lib/app/connections";
import {
  bindThread,
  createThread,
  getThread,
  listThreads,
  saveImage,
  getImage,
  updateThread,
} from "../lib/app/threads";
import { browserIdentity, ownerId } from "../lib/app/identity";
import { emptyCatalogFilters } from "../shared/catalog-filters";

it("persists encrypted connections and isolates their keys by owner", async () => {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-app-store-"));
  let runtime = createAppRuntime(directory);

  try {
    const saved = await runtime.runPromise(
      saveConnection("alice", {
        provider: "openai",
        name: "Work",
        model: "vision-model",
        contextWindow: 32_000,
        apiKey: "test-secret-not-for-a-provider",
      }),
    );

    expect(saved).toMatchObject({
      provider: "openai",
      model: "vision-model",
      contextWindow: 32_000,
      managed: false,
    });
    expect(JSON.stringify(saved)).not.toContain("test-secret");
    await expect(runtime.runPromise(resolveConnection("bob", saved.id))).rejects.toThrow(
      "Choose an available",
    );
    await runtime.runPromise(deleteConnection("bob", saved.id));
    await runtime.dispose();
    expect(
      (await readFile(join(directory, "chat.sqlite"))).includes(
        Buffer.from("test-secret-not-for-a-provider"),
      ),
    ).toBe(false);
    expect((await stat(join(directory, "credentials.key"))).mode & 0o777).toBe(0o600);
    runtime = createAppRuntime(directory);
    expect(
      Redacted.value((await runtime.runPromise(resolveConnection("alice", saved.id))).key),
    ).toBe("test-secret-not-for-a-provider");
    await expect(
      runtime.runPromise(
        saveConnection("alice", { ...saved, id: saved.id, provider: "anthropic" }),
      ),
    ).rejects.toThrow("Enter the API key again");
    await runtime.runPromise(deleteConnection("alice", saved.id));
    expect(
      (await runtime.runPromise(listConnections("alice"))).filter((item) => !item.managed),
    ).toEqual([]);
  } finally {
    await runtime.dispose();
    await rm(directory, { recursive: true, force: true });
  }
});

it("restores a conversation's selection and image after reopening SQLite", async () => {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-history-"));
  let runtime = createAppRuntime(directory);
  const catalogId = "a".repeat(64);

  const knowledge = {
    filters: emptyCatalogFilters(catalogId),
    selection: { catalogId, sql: "SELECT id FROM catalog_entries" },
    matchedGuidelines: 1,
  };

  const png = await readFile(new URL("../public/examples/bicycle-trips.png", import.meta.url));

  try {
    const thread = await runtime.runPromise(
      createThread(
        "alice",
        { title: "Bicycle comparison", connectionId: "server", knowledge },
        { catalogId, ids: ["axis-labels"] },
      ),
    );

    await runtime.runPromise(bindThread("alice", thread.id, "session-a", "server"));
    await expect(
      runtime.runPromise(bindThread("alice", thread.id, "session-b", "server")),
    ).rejects.toThrow("already has a session");
    await runtime.runPromise(
      saveImage("alice", thread.id, {
        filename: "chart.png",
        name: "My chart",
        mediaType: "image/png",
        data: `data:image/png;base64,${png.toString("base64")}`,
      }),
    );
    await runtime.runPromise(
      updateThread("alice", thread.id, { title: "Revised title", archived: true }),
    );
    await runtime.dispose();
    runtime = createAppRuntime(directory);
    expect((await runtime.runPromise(getThread("alice", thread.id))).detail).toMatchObject({
      title: "Revised title",
      sessionId: "session-a",
      archived: true,
      knowledge,
    });
    expect(
      Buffer.from((await runtime.runPromise(getImage("alice", thread.id, "chart.png"))).bytes),
    ).toEqual(png);
    expect(await runtime.runPromise(listThreads("bob"))).toEqual([]);
    await expect(runtime.runPromise(getThread("bob", thread.id))).rejects.toThrow(
      "Conversation not found",
    );
    await expect(runtime.runPromise(getImage("bob", thread.id, "chart.png"))).rejects.toThrow(
      "Conversation not found",
    );
  } finally {
    await runtime.dispose();
    await rm(directory, { recursive: true, force: true });
  }
});

it("uses a signed browser cookie and combines it with authenticated identity", async () => {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-identity-"));
  const runtime = createAppRuntime(directory);

  try {
    const identity = await runtime.runPromise(
      browserIdentity(new Request("https://chat.example/eve/v1/preferences"), true),
    );

    expect(identity?.cookie).toContain("HttpOnly; SameSite=Strict");
    expect(identity?.cookie).toContain("Secure");
    const cookie = identity!.cookie!.split(";")[0];

    const restored = await runtime.runPromise(
      browserIdentity(new Request("https://chat.example", { headers: { cookie } })),
    );

    expect(restored?.id).toBe(identity?.id);
    expect(
      await runtime.runPromise(
        browserIdentity(
          new Request("https://chat.example", {
            headers: { cookie: cookie.slice(0, -1) + (cookie.endsWith("0") ? "1" : "0") },
          }),
        ),
      ),
    ).toBeUndefined();
    expect(ownerId({ principalId: "alice", authenticator: "test" }, identity!.id)).not.toBe(
      ownerId({ principalId: "bob", authenticator: "test" }, identity!.id),
    );
  } finally {
    await runtime.dispose();
    await rm(directory, { recursive: true, force: true });
  }
});
