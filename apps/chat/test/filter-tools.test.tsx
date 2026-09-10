import { afterAll, beforeAll, expect, it, vi } from "vite-plus/test";
import type { ToolContext } from "eve/tools";
import { routeAuth } from "eve/channels/auth";
import { catalogRouteAuth, reviewRouteAuth } from "../agent/auth";
import { getCatalogMetadata } from "../lib/catalog/metadata";
import type { ResolvedSelection } from "../lib/catalog/selection";
import readGuidelines from "../agent/tools/read_guidelines";
import searchGuidelines from "../agent/tools/search_guidelines";
import queryCatalog from "../agent/tools/query_catalog";
import describeCatalog from "../agent/tools/describe_catalog";

let selection: ResolvedSelection;

beforeAll(async () => {
  selection = {
    catalogId: (await getCatalogMetadata()).catalogId,
    ids: [],
  };
});
afterAll(() => vi.unstubAllEnvs());

function context(toolName: string): ToolContext {
  const caller = {
    authenticator: "test",
    principalId: "reviewer",
    principalType: "user",
    attributes: { "chartcoach.selection": JSON.stringify(selection) },
  };
  return {
    abortSignal: new AbortController().signal,
    session: {
      id: "review",
      turn: { id: "turn", sequence: 2 },
      auth: {
        initiator: caller,
        current: {
          ...caller,
          attributes: {
            "chartcoach.selection": JSON.stringify({
              ...selection,
              ids: ["axis-labels"],
            }),
          },
        },
      },
    },
    toolName,
    callId: "call",
    async getSandbox() {
      throw new Error("Unexpected sandbox request.");
    },
    getSkill() {
      throw new Error("Unexpected skill request.");
    },
    async getToken() {
      throw new Error("Unexpected token request.");
    },
    requireAuth() {
      throw new Error("Unexpected authentication request.");
    },
  };
}

it("rejects reads outside the initiating review filters even when a later caller broadens them", async () => {
  await expect(
    readGuidelines.execute({ ids: ["axis-labels"] }, context("read_guidelines")),
  ).rejects.toThrow("outside this review's catalog filters");
});

it.each(["vector", "keyword", "hybrid"] as const)(
  "returns an empty %s search within an empty review scope",
  async (method) => {
    await expect(
      searchGuidelines.execute({ query: "legend labels", method }, context("search_guidelines")),
    ).resolves.toEqual({ method, query: "legend labels", matches: [] });
  },
);

it("scopes native SQL rows and verifies projected candidate IDs against the same scope", async () => {
  const count = await queryCatalog.execute(
    { sql: "SELECT count(*)::INTEGER AS count FROM main.guidelines", limit: 20 },
    context("query_catalog"),
  );
  expect(count).toMatchObject({ rows: [[0]], matches: [] });
  const literal = await queryCatalog.execute(
    { sql: "SELECT 'axis-labels' AS id", limit: 20 },
    context("query_catalog"),
  );
  expect(literal).toMatchObject({ rows: [["axis-labels"]], matches: [] });
});

it("describes the physically scoped SQL tables", async () => {
  const result = await describeCatalog.execute({}, context("describe_catalog"));
  expect(result).toMatchObject({
    tables: [
      { name: "guidelines", rows: 0 },
      { name: "sections", rows: 0 },
      { name: "guideline_labels", rows: 0 },
      { name: "references", rows: 0 },
      { name: "guideline_references", rows: 0 },
      { name: "guideline_sources", rows: 0 },
    ],
  });
});

it("rejects malformed selection headers through native route authentication", async () => {
  vi.stubEnv("EVE_DEV", "1");
  const response = await routeAuth(
    new Request("http://localhost/eve/v1/session", {
      method: "POST",
      headers: { "x-chartcoach-selection": "%invalid" },
    }),
    reviewRouteAuth,
  );
  expect(response).toBeInstanceOf(Response);
  if (!(response instanceof Response)) throw new Error("Expected authentication rejection.");
  expect(response.status).toBe(403);
  expect(await response.json()).toMatchObject({ code: "invalid_catalog_selection" });
});

it("preserves fail-closed production authentication for catalog and review routes", async () => {
  vi.stubEnv("EVE_DEV", "");
  vi.stubEnv("VERCEL", "");
  vi.stubEnv("NODE_ENV", "production");
  for (const policy of [catalogRouteAuth, reviewRouteAuth]) {
    const response = await routeAuth(new Request("http://localhost/eve/v1/catalog"), policy);
    expect(response).toBeInstanceOf(Response);
    if (!(response instanceof Response)) throw new Error("Expected authentication rejection.");
    expect(response.status).toBe(401);
  }
});
