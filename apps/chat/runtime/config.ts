import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { platformDirectories } from "@chartcoach/catalog/node/paths";
import { apiKeySchema } from "../shared/model.ts";

import { configSchema, type Config, type ConfigInput } from "./schema.ts";
import { readEnvironment } from "./environment.ts";

export type Environment = Record<string, string | undefined>;

export class ConfigurationError extends Error {}

function readConfigFile(path: string, optional = false): ConfigInput {
  let contents: string;

  try {
    contents = readFileSync(path, "utf8");
  } catch (error) {
    if (optional && error instanceof Error && "code" in error && error.code === "ENOENT") return {};
    throw new ConfigurationError(
      `Cannot read configuration ${path}. Check the path and permissions.`,
    );
  }

  try {
    return resolvePaths(parseConfig(JSON.parse(contents)), dirname(path));
  } catch (error) {
    if (error instanceof ConfigurationError) throw error;
    throw new ConfigurationError(`Invalid JSON in ${path}.`);
  }
}

function resolvePaths(config: Config, base: string) {
  config.storage.dataDir = resolve(base, config.storage.dataDir);
  config.storage.cacheDir = resolve(base, config.storage.cacheDir);

  if (!URL.canParse(config.catalog.source))
    config.catalog.source = resolve(base, config.catalog.source);

  if (config.server.passwordFile)
    config.server.passwordFile = resolve(base, config.server.passwordFile);

  return config;
}

function parseConfig(value: ConfigInput): Config {
  const result = configSchema.safeParse(value);

  if (!result.success)
    throw new ConfigurationError(
      `Invalid configuration: ${result.error.issues.map((issue) => issue.path.join(".") || "root").join(", ")}. Run chartcoach chat --help for flags and defaults.`,
    );

  return result.data;
}

function defined<T extends object>(values: T): Partial<T> {
  // SAFETY: filtering entries preserves their keys and value types and only omits properties.
  return Object.fromEntries(
    Object.entries(values).filter(([, value]) => value !== undefined),
  ) as Partial<T>;
}

function merge(base: ConfigInput, extra: ConfigInput): ConfigInput {
  return {
    ...base,
    ...defined(extra),
    catalog: { ...base.catalog, ...defined(extra.catalog ?? {}) },
    model: { ...base.model, ...defined(extra.model ?? {}) },
    server: { ...base.server, ...defined(extra.server ?? {}) },
    storage: { ...base.storage, ...defined(extra.storage ?? {}) },
  };
}

interface ConfigOptions {
  environment?: Environment;
  cwd?: string;
  overrides?: ConfigInput;
  configFile?: string;
  userConfig?: string;
}

export function loadConfig({
  environment = process.env,
  cwd = process.cwd(),
  overrides = {},
  configFile = environment.CHARTCOACH_CONFIG,
  userConfig = resolve(platformDirectories().config, "chat", "config.json"),
}: ConfigOptions = {}): Config {
  if (environment.CHARTCOACH_RUNTIME_CONFIG) {
    try {
      return parseConfig(JSON.parse(environment.CHARTCOACH_RUNTIME_CONFIG));
    } catch {
      throw new ConfigurationError("Invalid internal runtime configuration.");
    }
  }

  const file = configFile ? resolve(cwd, configFile) : userConfig;
  const config = readConfigFile(file, !configFile);
  let e: ReturnType<typeof readEnvironment>;

  try {
    e = readEnvironment(environment);
  } catch (error) {
    throw new ConfigurationError(
      error instanceof Error ? error.message : "Invalid environment configuration.",
    );
  }

  const values = {
    catalog: {
      source: e.CHARTCOACH_CATALOG,
      profile: e.CHARTCOACH_CATALOG_PROFILE,
    },
    model: {
      provider: e.CHARTCOACH_PROVIDER,
      model: e.CHARTCOACH_MODEL,
      baseURL: e.CHARTCOACH_BASE_URL,
      apiKeyEnv: e.CHARTCOACH_API_KEY_ENV,
      auth: e.CHARTCOACH_MODEL_AUTH,
      contextWindow: e.CHARTCOACH_CONTEXT_WINDOW,
    },
    server: {
      host: e.CHARTCOACH_HOST,
      port: e.CHARTCOACH_PORT,
      open: e.CHARTCOACH_OPEN,
      publicURL: e.CHARTCOACH_PUBLIC_URL,
      username: e.CHARTCOACH_USERNAME,
      passwordEnv: e.CHARTCOACH_PASSWORD_ENV,
      passwordFile: e.CHARTCOACH_PASSWORD_FILE,
      embedOrigins: list(e.CHARTCOACH_EMBED_ORIGINS),
    },
    storage: {
      dataDir: e.CHARTCOACH_DATA_DIR,
      cacheDir: e.CHARTCOACH_CACHE_DIR,
    },
    modelOrigins: list(e.CHARTCOACH_MODEL_ORIGINS),
    tracing: e.CHARTCOACH_TRACING,
  };

  const result = parseConfig(merge(merge(config, values), overrides));

  resolvePaths(result, cwd);

  if (result.model.auth === "none" && result.model.provider !== "compatible")
    throw new ConfigurationError("--model-auth none requires --provider compatible.");

  if (result.model.baseURL && result.model.provider !== "compatible")
    throw new ConfigurationError("--base-url requires --provider compatible.");

  if (result.model.model && result.model.provider === "compatible" && !result.model.baseURL)
    throw new ConfigurationError(
      "Set --base-url or CHARTCOACH_BASE_URL for an OpenAI-compatible connection.",
    );

  if (result.server.publicURL && new URL(result.server.publicURL).pathname !== "/")
    throw new ConfigurationError(
      "--public-url or CHARTCOACH_PUBLIC_URL must be an origin, without a path.",
    );
  result.modelOrigins = [...new Set(result.modelOrigins.map((value) => new URL(value).origin))];
  result.server.embedOrigins = result.server.embedOrigins.includes("*")
    ? ["*"]
    : [...new Set(result.server.embedOrigins.map((value) => new URL(value).origin))];

  return result;
}

function list(value: string | undefined) {
  return value
    ?.split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

const providerKeyNames = {
  openai: "OPENAI_API_KEY",
  anthropic: "ANTHROPIC_API_KEY",
  google: "GEMINI_API_KEY",
  compatible: "OPENAI_API_KEY",
};

export function modelKey(config: Config, environment: Environment = process.env) {
  if (config.model.auth === "none") return "";
  const name = config.model.apiKeyEnv ?? providerKeyNames[config.model.provider];

  const value = environment[name];

  if (!value) return undefined;
  const key = apiKeySchema.safeParse(value);

  if (!key.success)
    throw new ConfigurationError(`Invalid ${name}. Use one API key without spaces or line breaks.`);

  return key.data;
}

function serverPassword(config: Config, environment: Environment = process.env) {
  if (!config.server.passwordFile) return environment[config.server.passwordEnv];

  try {
    return readFileSync(config.server.passwordFile, "utf8").trimEnd();
  } catch {
    throw new ConfigurationError(
      "Cannot read the password file. Check --password-file or CHARTCOACH_PASSWORD_FILE and its permissions.",
    );
  }
}

export function embedKey(environment: Environment = process.env) {
  const value = environment.CHARTCOACH_EMBED_KEY;

  if (!value) return undefined;

  if (!/^[\x21-\x7e]{16,}$/.test(value))
    throw new ConfigurationError(
      "Invalid CHARTCOACH_EMBED_KEY. Use at least 16 printable characters without spaces.",
    );

  return value;
}

function isLocalHost(host: string) {
  return host === "127.0.0.1" || host === "::1";
}

export function validateStartup(config: Config, environment: Environment = process.env) {
  const password = serverPassword(config, environment);

  const publicHost = config.server.publicURL
    ? new URL(config.server.publicURL).hostname
    : undefined;

  const publicAccess =
    publicHost !== undefined && !["localhost", "127.0.0.1", "[::1]"].includes(publicHost);

  if ((!isLocalHost(config.server.host) || publicAccess) && !password)
    throw new ConfigurationError(
      "Network listening requires a password. Set CHARTCOACH_PASSWORD or pass --password-file.",
    );

  // Embedded frames keep the browser cookie only when it is SameSite=None, which requires Secure.
  if (
    config.server.embedOrigins.length > 0 &&
    publicAccess &&
    new URL(config.server.publicURL!).protocol !== "https:"
  )
    throw new ConfigurationError(
      "Embedding requires an HTTPS --public-url or CHARTCOACH_PUBLIC_URL.",
    );

  if (embedKey(environment) && config.server.embedOrigins.length === 0)
    throw new ConfigurationError("CHARTCOACH_EMBED_KEY requires CHARTCOACH_EMBED_ORIGINS.");

  if (config.model.model && config.model.auth !== "none" && !modelKey(config, environment))
    throw new ConfigurationError(
      `Set ${config.model.apiKeyEnv ?? providerKeyNames[config.model.provider]} for the configured model, or omit the model and connect in the browser.`,
    );

  return password;
}
