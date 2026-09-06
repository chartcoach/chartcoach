import { describe, expect, it } from "vite-plus/test";

import { Catalog, CatalogError, type GuidelineInput } from "@chartcoach/catalog";
import operations from "../../../fixtures/catalog-contract/operations.json";
import { parseCatalogManifest } from "../src/catalog/manifest";
import { fixtureCatalog, releaseFixtureUrl } from "./catalog-testkit";

describe("catalog operations", () => {
  it("matches the shared query, read, citation, and description records", async () => {
    const catalog = await fixtureCatalog();

    expect(
      catalog.query({
        contains: operations.query_cases[0].options.contains,
        limit: operations.query_cases[0].options.limit,
      }),
    ).toEqual(operations.query_cases[0].records);
    expect(
      catalog.query({
        ids: operations.query_cases[1].options.ids,
        limit: operations.query_cases[1].options.limit,
      }),
    ).toEqual(operations.query_cases[1].records);
    expect(catalog.read({ ids: ["direct-labels"], sourceDetail: "minimal" })).toEqual(
      operations.read.records,
    );
    expect(catalog.read({ ids: ["direct-labels"], sourceDetail: "full" })).toEqual(
      operations.read_full.records,
    );
    expect(catalog.cite({ ids: ["direct-labels"] })).toEqual(operations.cite.records);

    const pending = catalog.describe();
    expect(pending).toBeInstanceOf(Promise);
    const info = await pending;
    expect({
      release_digest: info.release_digest,
      entries_digest: info.entries_digest,
      manifest_digest: info.manifest_digest,
      section_roles: info.section_roles,
      label_families: info.label_families,
      profiles: info.profiles,
      profile: info.profile,
    }).toEqual(operations.description);
    expect(info.resolved_location).toBe(releaseFixtureUrl.toString());
  });

  it("keeps operation results immutable and preserves empty-selection semantics", async () => {
    const catalog = await fixtureCatalog();
    const query = catalog.query({ ids: [] });
    const read = catalog.read({ ids: [] });
    const citations = catalog.cite({ ids: [] });
    const noSources = catalog.read({ ids: ["direct-labels"], sourceDetail: "none" })[0]!;

    expect(query).toHaveLength(catalog.length);
    expect(read).toEqual([]);
    expect(citations).toEqual([]);
    expect(noSources.sources).toEqual([]);
    expect(Object.hasOwn(noSources, "references")).toBe(false);
    expect(Object.isFrozen(query)).toBe(true);
    expect(Object.isFrozen(query[0])).toBe(true);
    expect(Object.isFrozen(query[0]?.labels)).toBe(true);
    expect(Object.isFrozen(read)).toBe(true);
    expect(Object.isFrozen(citations)).toBe(true);
    expect(Object.isFrozen(await catalog.describe())).toBe(true);
  });

  it("requires one options object for every operation", async () => {
    const catalog = await fixtureCatalog();

    // @ts-expect-error The runtime rejects the positional form used by plain JavaScript callers.
    expect(() => catalog.query(["direct-labels"])).toThrow("Query options must be an object");
    // @ts-expect-error The runtime rejects the positional form used by plain JavaScript callers.
    expect(() => catalog.read(["direct-labels"])).toThrow("Read options must be an object");
    // @ts-expect-error The runtime rejects the positional form used by plain JavaScript callers.
    expect(() => catalog.cite(["direct-labels"])).toThrow("Citation options must be an object");
    // @ts-expect-error The runtime rejects the positional form used by plain JavaScript callers.
    await expect(catalog.describe([])).rejects.toThrow("Description options must be an object");
  });

  it("applies exact labels and prefixes conjunctively", () => {
    const catalog = new Catalog(
      [
        guideline("both", ["chart:line", "task:compare"]),
        guideline("chart", ["chart:line"]),
        guideline("task", ["task:compare"]),
      ],
      operationManifest(),
    );

    expect(catalog.query({ labels: ["chart:line", "task:compare"] }).map(({ id }) => id)).toEqual([
      "both",
    ]);
    expect(catalog.query({ labelPrefixes: ["chart:", "task:"] }).map(({ id }) => id)).toEqual([
      "both",
    ]);
    for (const query of [
      () => catalog.query({ ids: ["missing"] }),
      () => catalog.query({ labels: ["chart:missing"] }),
      () => catalog.query({ labelPrefixes: ["missing:"] }),
    ]) {
      try {
        query();
        throw new Error("query unexpectedly succeeded");
      } catch (error) {
        expect(error).toBeInstanceOf(CatalogError);
        if (error instanceof CatalogError) expect(error.code).toBe("lookup");
      }
    }
  });

  it("deduplicates equivalent references and rejects conflicting keys", () => {
    const equivalent = new Catalog(
      [
        guideline("first", [], operations.bibliography.equivalent[0]),
        guideline("second", [], operations.bibliography.equivalent[1]),
      ],
      operationManifest(),
    );
    expect(
      equivalent
        .cite({ ids: ["first", "second"] })
        .map((record) => record.sources[0]?.reference_id),
    ).toEqual(["shared2024", "shared2024"]);

    const conflicting = new Catalog(
      [
        guideline("first", [], operations.bibliography.conflicting[0]),
        guideline("second", [], operations.bibliography.conflicting[1]),
      ],
      operationManifest(),
    );
    expect(() => conflicting.cite({ ids: ["first"] })).toThrow(
      "Conflicting BibTeX definitions for reference id: shared2024",
    );
  });

  it("matches the Python entries digest for supplementary-plane ids", async () => {
    const catalog = new Catalog(operations.identity.records, operationManifest());

    expect((await catalog.describe()).entries_digest).toBe(operations.identity.entries_digest);
  });
});

function operationManifest() {
  return parseCatalogManifest(`# Catalog

## Section Roles

### advice

Actionable guidance.

## Label Families

### chart

Chart labels such as \`chart:line\`.

### task

Task labels such as \`task:compare\`.
`);
}

function guideline(id: string, labels: readonly string[], reference?: string): GuidelineInput {
  return {
    id,
    title: id,
    description: `${id} description.`,
    labels,
    sections: [{ role: "advice", title: "Advice", content: `${id} advice.` }],
    references: reference ? [reference] : [],
  };
}
