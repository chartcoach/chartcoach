import { existsSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

import type { AstroIntegration, AstroUserConfig } from "astro";

export const monorepoRoot = fileURLToPath(new URL("../../../..", import.meta.url));
const docsSourceRoot = fileURLToPath(new URL("..", import.meta.url));
const repoEnvPath = join(monorepoRoot, ".env");

export const LOCAL_SITE_URL = "http://localhost:4321/";
export const LOCAL_DOCS_URL = "http://localhost:4322/";
export const SITE_URL_ENV = "CHARTCOACH_SITE_URL";
export const DOCS_URL_ENV = "CHARTCOACH_DOCS_URL";
export const DOCS_EDIT_BASE_URL_ENV = "CHARTCOACH_DOCS_EDIT_BASE_URL";
export const REPOSITORY_URL_ENV = "CHARTCOACH_REPOSITORY_URL";

export type DocsUrlSource = "env" | "local";

export type DocsRuntimeConfig = {
  docsUrl: string;
  docsUrlSource: DocsUrlSource;
  editLinkBaseUrl?: string;
  repositoryUrl?: string;
};

export type DocsLinks = {
  siteUrl: string;
  repositoryUrl?: string;
};

type EnvMap = Record<string, string | undefined>;
type DocsRuntimeOptions = {
  env?: EnvMap;
};

type ProcessWithLoadEnvFile = typeof process & {
  loadEnvFile?: (path?: string) => void;
};

let repoEnvLoaded = false;

export function loadRepoEnvFile(envPath = repoEnvPath) {
  if (envPath === repoEnvPath && repoEnvLoaded) return;

  const loadEnvFile = (process as ProcessWithLoadEnvFile).loadEnvFile;
  if (typeof loadEnvFile === "function" && existsSync(envPath)) loadEnvFile(envPath);
  if (envPath === repoEnvPath) repoEnvLoaded = true;
}

function getEnv(options: DocsRuntimeOptions = {}) {
  if (options.env) return options.env;
  loadRepoEnvFile();
  return process.env;
}

function normalizeUrl(value: string) {
  return new URL(value).toString();
}

function resolveConfiguredUrl(
  env: EnvMap,
  envName: string,
  localDefault: string,
): { url: string; source: DocsUrlSource } {
  const value = env[envName];
  if (value) {
    return {
      url: normalizeUrl(value),
      source: "env",
    };
  }

  return {
    url: normalizeUrl(localDefault),
    source: "local",
  };
}

function resolveOptionalUrl(env: EnvMap, envName: string) {
  const value = env[envName];
  if (!value) {
    return undefined;
  }
  return normalizeUrl(value);
}

export function getDocsRuntimeConfig(options: DocsRuntimeOptions = {}): DocsRuntimeConfig {
  const env = getEnv(options);
  const docsUrl = resolveConfiguredUrl(env, DOCS_URL_ENV, LOCAL_DOCS_URL);

  return {
    docsUrl: docsUrl.url,
    docsUrlSource: docsUrl.source,
    editLinkBaseUrl: resolveOptionalUrl(env, DOCS_EDIT_BASE_URL_ENV),
    repositoryUrl: resolveOptionalUrl(env, REPOSITORY_URL_ENV),
  };
}

export function getDocsLinks(options: DocsRuntimeOptions = {}): DocsLinks {
  const env = getEnv(options);
  return {
    siteUrl: resolveConfiguredUrl(env, SITE_URL_ENV, LOCAL_SITE_URL).url,
    repositoryUrl: resolveOptionalUrl(env, REPOSITORY_URL_ENV),
  };
}

export function createDocsUrlLogger(docsUrl: string, source: DocsUrlSource): AstroIntegration {
  return {
    name: "chartcoach:docs-url",
    hooks: {
      "astro:config:setup": ({ logger }) => {
        logger.info(`docs url resolved (${docsUrl}) [${source}]`);
      },
    },
  };
}

export const docsViteConfig = {
  envDir: monorepoRoot,
  server: {
    fs: {
      allow: [monorepoRoot],
    },
  },
  resolve: {
    conditions: ["source", "module", "browser", "development|production"],
    alias: {
      "@": docsSourceRoot,
    },
  },
} satisfies NonNullable<AstroUserConfig["vite"]>;
