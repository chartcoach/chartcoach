import { existsSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

import type { AstroIntegration, AstroUserConfig } from "astro";
import tailwindcss from "@tailwindcss/vite";

const monorepoRoot = fileURLToPath(new URL("../../../..", import.meta.url));

const siteSourceRoot = fileURLToPath(new URL("..", import.meta.url));

const repoEnvPath = join(monorepoRoot, ".env");

const LOCAL_SITE_URL = "http://localhost:4321/";

const SITE_URL_ENV = "CHARTCOACH_SITE_URL";

const CF_PAGES_ENV = "CF_PAGES";

const CF_PAGES_BRANCH_ENV = "CF_PAGES_BRANCH";

const CF_PAGES_URL_ENV = "CF_PAGES_URL";

const PORTLESS_URL_ENV = "PORTLESS_URL";

const PRODUCTION_BRANCH = "main";

export type SiteUrlSource = "env" | "cloudflare" | "portless" | "local";

export type SiteRuntimeConfig = {
  siteUrl: string;
  siteUrlSource: SiteUrlSource;
  isPreviewDeployment: boolean;
};

type EnvMap = Record<string, string | undefined>;

type SiteRuntimeOptions = {
  env?: EnvMap;
};

type SiteUrlResolution = {
  url: string;
  source: SiteUrlSource;
};

type SiteViteConfig = NonNullable<AstroUserConfig["vite"]>;

let repoEnvLoaded = false;

export function loadRepoEnvFile(envPath = repoEnvPath) {
  if (envPath === repoEnvPath && repoEnvLoaded) return;

  if (existsSync(envPath)) process.loadEnvFile(envPath);

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

function isCloudflarePreview(env: EnvMap) {
  return env[CF_PAGES_ENV] === "1" && env[CF_PAGES_BRANCH_ENV] !== PRODUCTION_BRANCH;
}

function resolveConfiguredUrl(env: EnvMap): SiteUrlResolution {
  const value = env[SITE_URL_ENV];

  if (value) {
    return {
      url: normalizeUrl(value),
      source: "env",
    };
  }

  const cloudflareUrl = env[CF_PAGES_URL_ENV];

  if (cloudflareUrl) {
    return {
      url: normalizeUrl(cloudflareUrl),
      source: "cloudflare",
    };
  }

  const portlessUrl = env[PORTLESS_URL_ENV];

  if (portlessUrl) {
    return {
      url: normalizeUrl(portlessUrl),
      source: "portless",
    };
  }

  return {
    url: normalizeUrl(LOCAL_SITE_URL),
    source: "local",
  };
}

export function getSiteRuntimeConfig(options: SiteRuntimeOptions = {}): SiteRuntimeConfig {
  const env = getEnv(options);
  const siteUrl = resolveConfiguredUrl(env);

  return {
    siteUrl: siteUrl.url,
    siteUrlSource: siteUrl.source,
    isPreviewDeployment: isCloudflarePreview(env),
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
} satisfies SiteViteConfig;
