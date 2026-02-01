import { useMemo } from "react";
import { eq, useLiveQuery } from "@tanstack/react-db";

import {
  guidelineRatingsCollection,
  type GuidelineRating,
} from "@chartcoach/eval-ui/db-collections";

export function useScenarioRatings(scenarioId: string | undefined) {
  const enabled = Boolean(scenarioId);

  const { data } = useLiveQuery(
    (q) =>
      q
        .from({ rating: guidelineRatingsCollection })
        .where(({ rating }) =>
          enabled ? eq(rating.scenarioId, scenarioId!) : eq(rating.scenarioId, "__disabled__"),
        )
        .select(({ rating }) => ({
          ...rating,
        })),
    [scenarioId],
  );

  const ratings = (data ?? []) as GuidelineRating[];

  const byGuidelineId = useMemo(() => {
    const map = new Map<string, GuidelineRating>();
    for (const r of ratings) {
      map.set(r.guidelineId, r);
    }
    return map;
  }, [ratings]);

  function getRating(guidelineId: string) {
    return byGuidelineId.get(guidelineId);
  }

  return { ratings, getRating };
}
