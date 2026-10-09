import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { parseEnv } from "node:util";
import { ConfigurationError } from "./config";

export function loadEnvironmentFile(path = process.env.CHARTCOACH_ENV_FILE) {
  try {
    const values = parseEnv(readFileSync(resolve(path ?? ".env"), "utf8"));

    for (const [name, value] of Object.entries(values)) process.env[name] ??= value;
  } catch (error) {
    if (!path && error instanceof Error && "code" in error && error.code === "ENOENT") return;
    throw new ConfigurationError(
      "Cannot read --env-file or CHARTCOACH_ENV_FILE. Check its path and permissions.",
    );
  }
}
