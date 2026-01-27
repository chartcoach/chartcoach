import { describe, expect, it } from "vitest";

import type { RelevanceRating } from "@chartcoach/eval-ui/eval/relevance-ratings";
import { makeRatingsSignature } from "@chartcoach/eval-ui/eval/relevance-ratings-sync-metadata";

function makeRating(i: number): RelevanceRating {
  return {
    id: `r-${i}`,
    scenarioId: `s-${i % 3}`,
    guidelineId: `g-${i % 7}`,
    relevance: ((i % 5) + 1) as 1 | 2 | 3 | 4 | 5,
    createdAt: new Date(0).toISOString(),
    updatedAt: new Date(i).toISOString(),
  };
}

describe("makeRatingsSignature", () => {
  it("stays constant-size for large rating sets", () => {
    const ratings = Array.from({ length: 10_000 }, (_, i) => makeRating(i));
    const signature = makeRatingsSignature(ratings);
    expect(signature.length).toBeLessThan(200);
  });

  it("is stable regardless of input order", () => {
    const ratings = [makeRating(2), makeRating(1), makeRating(3)];
    expect(makeRatingsSignature(ratings)).toEqual(makeRatingsSignature([...ratings].reverse()));
  });

  it("changes when any rating changes", () => {
    const ratingsA = [makeRating(1), makeRating(2)];
    const ratingsB = [...ratingsA];
    ratingsB[0] = { ...ratingsB[0], relevance: 5 };
    expect(makeRatingsSignature(ratingsA)).not.toEqual(makeRatingsSignature(ratingsB));
  });
});

