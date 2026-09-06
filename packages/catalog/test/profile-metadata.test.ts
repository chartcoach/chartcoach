import { describe, expect, it } from "vite-plus/test";

import { parseProfileMetadata, type JsonObject } from "@chartcoach/catalog";
import fixture from "../../../fixtures/catalog-contract/profile.json";

describe("profile metadata", () => {
  it("parses the shared profile contract into immutable values", () => {
    const profile = parseProfileMetadata(fixture);

    expect(profile.dimensions).toBe(4);
    expect(profile.embedding_functions[0].source_column).toBe("text");
    expect(profile.lancedb_version).toBe("0.38.0");
    expect(Object.isFrozen(profile)).toBe(true);
    expect(Object.isFrozen(profile.embedding_functions)).toBe(true);
    expect(Object.isFrozen(profile.embedding_functions[0].model)).toBe(true);
  });

  it("rejects invalid closed-contract fields", () => {
    expect(() => parseProfileMetadata({ ...fixture, dimensions: true })).toThrow(
      "positive safe integer",
    );
    expect(() => parseProfileMetadata({ ...fixture, distance_metric: "manhattan" })).toThrow(
      "cosine, l2, or dot",
    );
    expect(() => parseProfileMetadata({ ...fixture, extra: true })).toThrow("unsupported fields");
    expect(() =>
      parseProfileMetadata({
        ...fixture,
        embedding_functions: [
          { ...fixture.embedding_functions[0], model: { temperature: Number.POSITIVE_INFINITY } },
        ],
      }),
    ).toThrow("finite JSON number");
  });

  it("rejects literal secrets and nested variable references", () => {
    const binding = fixture.embedding_functions[0];

    expect(() =>
      parseProfileMetadata({
        ...fixture,
        embedding_functions: [{ ...binding, model: { api_key: "secret" } }],
      }),
    ).toThrow("registry variable");
    expect(() =>
      parseProfileMetadata({
        ...fixture,
        embedding_functions: [{ ...binding, model: { options: { key: "$var:key" } } }],
      }),
    ).toThrow("invalid variable");
  });

  it("rejects persisted authentication data", () => {
    const binding = fixture.embedding_functions[0];
    function parse(model: JsonObject) {
      return parseProfileMetadata({
        ...fixture,
        embedding_functions: [{ ...binding, model }],
      });
    }

    expect(() => parse({ endpoint_url: "https://user:password@example.test/v1" })).toThrow(
      /credentials|authentication|empty/,
    );
    expect(() => parse({ endpoint_url: "https://example.test/v1?token=" })).toThrow(
      /credentials|authentication|empty/,
    );
    expect(() =>
      parse({ options: { endpoint_url: "https://example.test/v1?access_key=secret" } }),
    ).toThrow(/credentials|authentication|empty/);
    expect(() => parse({ options: [{ headers: { access_key: "secret" } }] })).toThrow(
      /credentials|authentication|empty/,
    );
    expect(() => parse({ default_headers: { "X-Custom": "value" } })).toThrow(
      /credentials|authentication|empty/,
    );
  });
});
