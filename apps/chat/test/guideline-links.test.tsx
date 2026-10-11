import { Catalog } from "@chartcoach/catalog";
import { afterEach, expect, it, vi } from "vite-plus/test";

// The runtime snapshots deployment settings when its module is loaded.
vi.stubEnv("CHARTCOACH_GUIDELINE_URL_TEMPLATE", "https://guidance.example/entries/{id}");

vi.stubEnv("CHARTCOACH_GUIDELINE_IMAGE_URL_TEMPLATE", "https://images.example/{id}.png");

const { getCatalog } = await import("../lib/catalog/open");

const { readGuidelines } = await import("../lib/retrieval/read");

const { guidelineCards } = await import("../lib/retrieval/cards");

const { withCatalogScope } = await import("../lib/catalog/scope");

afterEach(() => vi.unstubAllEnvs());

it("returns the same encoded deployment destination through read and search cards", async () => {
  const fixture = await getCatalog();

  const catalog = new Catalog(
    [{ ...fixture.guidelines[0]!, id: "labels/path?detail" }],
    fixture.manifest,
  );

  const result = await readGuidelines(["labels/path?detail"], { catalog });
  expect(result.citations[0]?.url).toBe("https://guidance.example/entries/labels%2Fpath%3Fdetail");
  expect(result.citations[0]?.guideline_citation).toContain(
    "(https://guidance.example/entries/labels%2Fpath%3Fdetail)",
  );
  expect(result.citations[0]?.sources.length).toBeGreaterThan(0);

  const cards = await withCatalogScope({ catalog }, async (scope) =>
    guidelineCards(scope, ["labels/path?detail"]),
  );

  expect(cards[0]).toMatchObject({
    url: "https://guidance.example/entries/labels%2Fpath%3Fdetail",
    imageURL: "https://images.example/labels%2Fpath%3Fdetail.png",
  });
});
