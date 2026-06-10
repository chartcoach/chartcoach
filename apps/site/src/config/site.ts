import { existsSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

import type { AstroIntegration, AstroUserConfig } from "astro";
import tailwindcss from "@tailwindcss/vite";

export const monorepoRoot = fileURLToPath(new URL("../../../..", import.meta.url));
const siteSourceRoot = fileURLToPath(new URL("..", import.meta.url));
const repoEnvPath = join(monorepoRoot, ".env");

export const LOCAL_SITE_URL = "http://localhost:4321/";
export const SITE_URL_ENV = "CHARTCOACH_SITE_URL";

export type SiteUrlSource = "env" | "local";

export type SiteRuntimeConfig = {
  siteUrl: string;
  siteUrlSource: SiteUrlSource;
};

type EnvMap = Record<string, string | undefined>;
type SiteRuntimeOptions = {
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

function getEnv(options: SiteRuntimeOptions = {}) {
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
): { url: string; source: SiteUrlSource } {
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

export function getSiteRuntimeConfig(options: SiteRuntimeOptions = {}): SiteRuntimeConfig {
  const siteUrl = resolveConfiguredUrl(getEnv(options), SITE_URL_ENV, LOCAL_SITE_URL);

  return {
    siteUrl: siteUrl.url,
    siteUrlSource: siteUrl.source,
  };
}

export function createSiteUrlLogger(siteUrl: string, source: SiteUrlSource): AstroIntegration {
  return {
    name: "chartcoach:site-url",
    hooks: {
      "astro:config:setup": ({ logger }) => {
        logger.info(`site url resolved (${siteUrl}) [${source}]`);
      },
    },
  };
}

export const siteViteConfig = {
  envDir: monorepoRoot,
  plugins: [tailwindcss()],
  server: {
    fs: {
      allow: [monorepoRoot],
    },
  },
  ssr: {
    noExternal: ["@chartcoach/catalog"],
  },
  resolve: {
    conditions: ["source", "module", "browser", "development|production"],
    alias: {
      "@": siteSourceRoot,
    },
  },
} satisfies NonNullable<AstroUserConfig["vite"]>;
