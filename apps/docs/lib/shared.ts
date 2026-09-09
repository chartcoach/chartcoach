export const appName = "chartcoach";
export const siteOrigin = "https://chartcoach.dev";
const canonicalDocsOrigin = "https://docs.chartcoach.dev";
const docsOriginEnv = "CHARTCOACH_DOCS_URL";
const productionBranch = "main";

type EnvMap = Record<string, string | undefined>;

function normalizeOrigin(value: string) {
  return new URL(value).origin;
}

export function isPreviewDeployment(env: EnvMap = process.env) {
  return env.CF_PAGES === "1" && env.CF_PAGES_BRANCH !== productionBranch;
}

function resolveDocsOrigin(env: EnvMap = process.env) {
  const value = env[docsOriginEnv] || (isPreviewDeployment(env) ? env.CF_PAGES_URL : undefined);
  return normalizeOrigin(value ?? canonicalDocsOrigin);
}

export const docsOrigin = resolveDocsOrigin();
export const docsRoute = "/";
export const docsContentRoute = "/llms.mdx/docs";

export const gitConfig = {
  user: "chartcoach",
  repo: "chartcoach",
  branch: "main",
};
