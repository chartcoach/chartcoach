import { createHash, randomUUID } from "node:crypto";
import { Effect } from "effect";
import { Secrets } from "./secrets";

const cookieName = "chartcoach_browser";
export const browserIdentity = (request: Request, create = false) =>
  Effect.gen(function* () {
    const secrets = yield* Secrets;
    const cookie = request.headers
      .get("cookie")
      ?.split(";")
      .map((value) => value.trim())
      .find((value) => value.startsWith(`${cookieName}=`))
      ?.slice(cookieName.length + 1);
    const [id, signature] = cookie?.split(".") ?? [];
    if (id && /^[a-f0-9-]{36}$/.test(id) && signature && secrets.verify(id, signature))
      return { id, cookie: undefined };
    if (!create) return undefined;
    const next = randomUUID();
    const secure =
      new URL(request.url).protocol === "https:" ||
      request.headers.get("x-forwarded-proto") === "https";
    return {
      id: next,
      cookie: `${cookieName}=${next}.${secrets.sign(next)}; Path=/; HttpOnly; SameSite=Strict; Max-Age=31536000${secure ? "; Secure" : ""}`,
    };
  });

export function ownerId(
  principal: { principalId: string; authenticator: string },
  browser: string,
) {
  return createHash("sha256")
    .update(JSON.stringify([principal.authenticator, principal.principalId, browser]))
    .digest("hex");
}
