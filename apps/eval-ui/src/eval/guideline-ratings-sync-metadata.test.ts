import { describe, expect, it } from "vitest";

import type { GuidelineRating } from "@chartcoach/eval-ui/eval/guideline-ratings";
import { makeRatingsSignature } from "@chartcoach/eval-ui/eval/guideline-ratings-sync-metadata";

function makeRating(i: number): GuidelineRating {
  return {
    id: `r-${i}`,
    scenarioId: `s-${i % 3}`,
    guidelineId: `g-${i % 7}`,
    bucket: i % 3 === 0 ? "hard_constraint" : i % 3 === 1 ? "soft_constraint" : "not_useful",
    actionability: ((i % 5) + 1) as 1 | 2 | 3 | 4 | 5,
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
    ratingsB[0] = { ...ratingsB[0], bucket: "not_applicable" };
    expect(makeRatingsSignature(ratingsA)).not.toEqual(makeRatingsSignature(ratingsB));
  });
});
