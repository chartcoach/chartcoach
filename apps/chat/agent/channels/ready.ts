import { readFile } from "node:fs/promises";
import { defineChannel, GET } from "eve/channels";
import { routeAuth } from "eve/channels/auth";
import { z } from "zod";
import { Effect } from "effect";
import { SqlClient } from "@effect/sql";
import { runApp } from "../../lib/app/runtime";
import { accessRouteAuth } from "../auth";
import { sandboxBackend } from "../sandbox";
import { settings } from "../../runtime/settings";

const planSchema = z.array(
  z.object({
    templateKey: z.string(),
    seedFiles: z.array(z.object({ path: z.string(), content: z.string() })),
  }),
);

let ready: Promise<void[]> | undefined;

async function provision() {
  const path = process.env.CHARTCOACH_SANDBOX_PLAN;

  if (!path) throw new Error("Start the packaged application with chartcoach chat.");
  const plan = planSchema.parse(JSON.parse(await readFile(path, "utf8")));

  for (const template of plan) {
    await sandboxBackend.prewarm({
      templateKey: template.templateKey,
      runtimeContext: { appRoot: settings.storage.dataDir },
      seedFiles: template.seedFiles.map((file) => ({
        path: file.path,
        content: Buffer.from(file.content, "base64"),
      })),
    });
  }
}

export default defineChannel({
  routes: [
    GET("/eve/v1/ready", async (request) => {
      const auth = await routeAuth(request, accessRouteAuth);

      if (auth instanceof Response) return auth;
      await (ready ??= Promise.all([
        provision(),
        runApp(
          Effect.gen(function* () {
            const sql = yield* SqlClient.SqlClient;
            yield* sql`SELECT 1`;
          }),
        ),
      ]));

      return Response.json({ ok: true });
    }),
  ],
});
