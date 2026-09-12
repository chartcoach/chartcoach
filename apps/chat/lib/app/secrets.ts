import {
  createCipheriv,
  createDecipheriv,
  createHmac,
  randomBytes,
  timingSafeEqual,
} from "node:crypto";
import { readFile, writeFile, mkdir, link, unlink } from "node:fs/promises";
import { join } from "node:path";
import { Effect, Redacted } from "effect";

export class Secrets extends Effect.Service<Secrets>()("Secrets", {
  effect: (directory: string) =>
    Effect.gen(function* () {
      yield* Effect.promise(() => mkdir(directory, { recursive: true, mode: 0o700 }));
      const path = join(directory, "credentials.key");

      const key = yield* Effect.tryPromise(async () => {
        const temporary = join(directory, `credentials-${randomBytes(12).toString("hex")}.key`);
        await writeFile(temporary, randomBytes(32), { flag: "wx", mode: 0o600 });

        try {
          await link(temporary, path);
        } catch (error) {
          if (!(error instanceof Error && "code" in error && error.code === "EEXIST")) throw error;
        } finally {
          await unlink(temporary);
        }

        const bytes = await readFile(path);

        if (bytes.length !== 32) throw new Error("Invalid credential encryption key.");

        return bytes;
      });

      return {
        seal: (value: Redacted.Redacted<string>, owner: string) => {
          const nonce = randomBytes(12);
          const cipher = createCipheriv("aes-256-gcm", key, nonce);
          cipher.setAAD(Buffer.from(owner));

          const bytes = Buffer.concat([
            cipher.update(Redacted.value(value), "utf8"),
            cipher.final(),
          ]);

          return Buffer.concat([nonce, cipher.getAuthTag(), bytes]).toString("base64");
        },
        open: (value: string, owner: string) => {
          const bytes = Buffer.from(value, "base64");
          const cipher = createDecipheriv("aes-256-gcm", key, bytes.subarray(0, 12));
          cipher.setAAD(Buffer.from(owner));
          cipher.setAuthTag(bytes.subarray(12, 28));

          return Redacted.make(
            Buffer.concat([cipher.update(bytes.subarray(28)), cipher.final()]).toString("utf8"),
          );
        },
        sign: (value: string) => createHmac("sha256", key).update(value).digest("hex"),
        verify: (value: string, signature: string) => {
          const expected = createHmac("sha256", key).update(value).digest();
          const actual = Buffer.from(signature, "hex");

          return actual.length === expected.length && timingSafeEqual(actual, expected);
        },
      };
    }),
}) {}
