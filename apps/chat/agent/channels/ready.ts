import { defineChannel, GET } from "eve/channels";
import { routeAuth } from "eve/channels/auth";
import { Effect } from "effect";
import { SqlClient } from "@effect/sql";
import { runApp } from "../../lib/app/runtime";
import { accessRouteAuth } from "../auth";

let ready: Promise<void> | undefined;

export default defineChannel({
  routes: [
    GET("/eve/v1/ready", async (request) => {
      const auth = await routeAuth(request, accessRouteAuth);

      if (auth instanceof Response) return auth;
      await (ready ??= runApp(
        Effect.gen(function* () {
          const sql = yield* SqlClient.SqlClient;
          yield* sql`SELECT 1`;
        }),
      ));

      return Response.json({ ok: true });
    }),
  ],
});
