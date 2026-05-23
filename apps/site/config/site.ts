import { existsSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

import type { AstroIntegration, AstroUserConfig } from "astro";
import tailwindcss from "@tailwindcss/vite";

export const monorepoRoot = fileURLToPath(new URL("../../..", import.meta.url));
const siteSourceRoot = fileURLToPath(new URL("../src", import.meta.url));
const repoEnvPath = join(monorepoRoot, ".env");

export const DEFAULT_SITE_URL = "https://chartcoach.github.io/";

export type SiteUrlSource = "env" | "default";

export type SiteRuntimeConfig = {
  siteUrl: string;
  siteUrlSource: SiteUrlSource;
  enableAgentationReview: boolean;
};

type EnvMap = Record<string, string | undefined>;
type SiteRuntimeOptions = {
  env?: EnvMap;
  argv?: readonly string[];
};

type ProcessWithLoadEnvFile = typeof process & {
  loadEnvFile?: (path?: string) => void;
};

export function loadRepoEnvFile(envPath = repoEnvPath) {
  const loadEnvFile = (process as ProcessWithLoadEnvFile).loadEnvFile;
  if (typeof loadEnvFile === "function" && existsSync(envPath)) loadEnvFile(envPath);
}

export function resolveSiteUrl(env: EnvMap = process.env) {
  if (!env.SITE_URL) {
    return undefined;
  }
  return new URL(env.SITE_URL).toString();
}

export function isAgentationReviewEnabled({
  env = process.env,
  argv = process.argv,
}: SiteRuntimeOptions = {}) {
  return env.PUBLIC_ENABLE_AGENTATION === "true" || argv.some((arg) => /(?:^|\/)dev$/.test(arg));
}

export function getSiteRuntimeConfig(options: SiteRuntimeOptions = {}): SiteRuntimeConfig {
  const envSiteUrl = resolveSiteUrl(options.env);

  return {
    siteUrl: envSiteUrl ?? DEFAULT_SITE_URL,
    siteUrlSource: envSiteUrl ? "env" : "default",
    enableAgentationReview: isAgentationReviewEnabled(options),
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
  resolve: {
    conditions: ["source", "module", "browser", "development|production"],
    alias: {
      "@": siteSourceRoot,
    },
  },
} satisfies NonNullable<AstroUserConfig["vite"]>;
