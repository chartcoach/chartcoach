import { queryOptions } from "@tanstack/react-query";

import {
  getEvalScenarioBundle,
  getEvalScenarios,
} from "@chartcoach/eval-ui/eval/server/eval.server";

export const scenariosQueryOptions = queryOptions({
  queryKey: ["eval", "scenarios"],
  queryFn: async () => await getEvalScenarios(),
});

export const scenarioBundleQueryOptions = (scenarioId: string) =>
  queryOptions({
    queryKey: ["eval", "scenario", scenarioId],
    queryFn: async () => await getEvalScenarioBundle({ data: { scenarioId } }),
  });
