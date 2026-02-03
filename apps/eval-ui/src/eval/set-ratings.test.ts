import { describe, expect, it } from "vitest";

import { SetRatingsExportV1Schema } from "@chartcoach/eval-ui/eval/set-ratings";

describe("SetRatingsExportV1Schema", () => {
  it("accepts a minimal export payload", () => {
    const parsed = SetRatingsExportV1Schema.parse({
      format: "chartcoach.set-ratings.v1",
      exportedAt: new Date(0).toISOString(),
      ratings: [
        {
          id: "r1",
          scenarioId: "s1",
          strategyId: "hybrid-rrf@v1",
          createdAt: new Date(0).toISOString(),
          updatedAt: new Date(0).toISOString(),
        },
      ],
    });

    expect(parsed.ratings).toHaveLength(1);
    expect(parsed.ratings[0]?.sufficiency).toBeUndefined();
  });
});

