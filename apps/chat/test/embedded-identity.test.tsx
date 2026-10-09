import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { expect, it, vi } from "vite-plus/test";

it("issues a partitioned cross-site browser cookie when embedding is configured", async () => {
  vi.stubEnv("CHARTCOACH_EMBED_ORIGINS", "*");
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-embedded-identity-"));
  const { createAppRuntime } = await import("../lib/app/runtime");
  const { browserIdentity } = await import("../lib/app/identity");
  const runtime = createAppRuntime(directory);

  try {
    const identity = await runtime.runPromise(
      browserIdentity(new Request("http://127.0.0.1:4273/eve/v1/preferences"), true),
    );

    expect(identity?.cookie).toContain(
      "HttpOnly; SameSite=None; Max-Age=31536000; Secure; Partitioned",
    );
  } finally {
    await runtime.dispose();
    await rm(directory, { recursive: true, force: true });
    vi.unstubAllEnvs();
  }
});
