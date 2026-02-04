import { describe, expect, it } from "vitest";

import type { GuidelineRating } from "@chartcoach/eval-ui/eval/guideline-ratings";
import type { ScenarioSetRating } from "@chartcoach/eval-ui/eval/set-ratings";
import { makeEvalDataSignature } from "@chartcoach/eval-ui/eval/eval-data-sync-metadata";

function makeGuidelineRating(i: number): GuidelineRating {
  return {
    id: `g-${i}`,
    scenarioId: `s-${i % 3}`,
    guidelineId: `guideline-${i % 11}`,
    bucket: i % 4 === 0 ? "hard_constraint" : i % 4 === 1 ? "soft_constraint" : i % 4 === 2 ? "not_useful" : "not_applicable",
    actionability: ((i % 5) + 1) as 1 | 2 | 3 | 4 | 5,
    createdAt: new Date(0).toISOString(),
    updatedAt: new Date(i).toISOString(),
  };
}

function makeSetRating(i: number): ScenarioSetRating {
  return {
    id: `set-${i}`,
    scenarioId: `s-${i % 3}`,
    strategyId: `strategy-${i % 7}`,
    sufficiency: ((i % 5) + 1) as 1 | 2 | 3 | 4 | 5,
    createdAt: new Date(0).toISOString(),
    updatedAt: new Date(i).toISOString(),
  };
}

describe("makeEvalDataSignature", () => {
  it("stays constant-size for large rating sets", () => {
    const guidelineRatings = Array.from({ length: 5_000 }, (_, i) => makeGuidelineRating(i));
    const setRatings = Array.from({ length: 2_000 }, (_, i) => makeSetRating(i));
    const signature = makeEvalDataSignature({ guidelineRatings, setRatings });
    expect(signature.length).toBeLessThan(200);
  });

  it("is stable regardless of input order", () => {
    const guidelineRatings = [makeGuidelineRating(2), makeGuidelineRating(1), makeGuidelineRating(3)];
    const setRatings = [makeSetRating(2), makeSetRating(1), makeSetRating(3)];
    expect(makeEvalDataSignature({ guidelineRatings, setRatings })).toEqual(
      makeEvalDataSignature({
        guidelineRatings: [...guidelineRatings].reverse(),
        setRatings: [...setRatings].reverse(),
      }),
    );
  });

  it("changes when set ratings change", () => {
    const guidelineRatings = [makeGuidelineRating(1), makeGuidelineRating(2)];
    const setRatingsA = [makeSetRating(1), makeSetRating(2)];
    const setRatingsB = [...setRatingsA];
    setRatingsB[0] = { ...setRatingsB[0], harm: 5 };
    expect(makeEvalDataSignature({ guidelineRatings, setRatings: setRatingsA })).not.toEqual(
      makeEvalDataSignature({ guidelineRatings, setRatings: setRatingsB }),
    );
  });
});

