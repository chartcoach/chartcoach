import { useMemo } from "react";
import { eq, useLiveQuery } from "@tanstack/react-db";

import {
  setRatingsCollection,
  type ScenarioSetRating,
} from "@chartcoach/eval-ui/db-collections";

export function useScenarioSetRatings(scenarioId: string | undefined) {
  const enabled = Boolean(scenarioId);

  const { data } = useLiveQuery(
    (q) =>
      q
        .from({ rating: setRatingsCollection })
        .where(({ rating }) =>
          enabled ? eq(rating.scenarioId, scenarioId!) : eq(rating.scenarioId, "__disabled__"),
        )
        .select(({ rating }) => ({
          ...rating,
        })),
    [scenarioId],
  );

  const ratings = (data ?? []) as ScenarioSetRating[];

  const byStrategyId = useMemo(() => {
    const map = new Map<string, ScenarioSetRating>();
    for (const r of ratings) {
      map.set(r.strategyId, r);
    }
    return map;
  }, [ratings]);

  function getRating(strategyId: string) {
    return byStrategyId.get(strategyId);
  }

  return { ratings, getRating };
}

