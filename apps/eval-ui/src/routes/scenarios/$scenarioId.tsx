import { createFileRoute, redirect } from "@tanstack/react-router";
import { useQuery } from "@tanstack/react-query";
import { useEffect, useMemo, useState } from "react";
import { z } from "zod";

import { AppHeader } from "@chartcoach/eval-ui/components/app-header";
import { ScenarioPanel } from "@chartcoach/eval-ui/components/scenario-eval/scenario-panel";
import { StrategyTabs } from "@chartcoach/eval-ui/components/scenario-eval/strategy-tabs";
import { GuidelineDeck } from "@chartcoach/eval-ui/components/scenario-eval/guideline-deck";
import { SetRatingPanel } from "@chartcoach/eval-ui/components/scenario-eval/set-rating-panel";
import { deleteGuidelineRating, upsertGuidelineRating } from "@chartcoach/eval-ui/db-collections";
import type { ScenarioSpec } from "@chartcoach/eval-ui/eval/schemas";
import {
  scenarioBundleQueryOptions,
  scenariosQueryOptions,
} from "@chartcoach/eval-ui/eval/queries";
import { useScenarioRatings } from "@chartcoach/eval-ui/eval/hooks/use-scenario-ratings";
import { useScenarioSetRatings } from "@chartcoach/eval-ui/eval/hooks/use-scenario-set-ratings";

export const Route = createFileRoute("/scenarios/$scenarioId")({
  validateSearch: z.object({
    strategyId: z.string().optional(),
  }),
  ssr: false,
  loader: async ({ context, params }) => {
    const scenarioId = params.scenarioId;
    let scenarios: ScenarioSpec[];
    try {
      scenarios = await context.queryClient.ensureQueryData(scenariosQueryOptions);
    } catch (error) {
      console.warn("[eval-ui] Failed to prefetch scenarios (route loader).", error);
      return;
    }

    const exists = scenarios.some((s) => s.id === scenarioId);
    if (!exists) {
      throw redirect({ to: "/" });
    }

    try {
      await context.queryClient.ensureQueryData(scenarioBundleQueryOptions(scenarioId));
    } catch (error) {
      console.warn(
        `[eval-ui] Failed to prefetch scenario bundle for scenarioId=${scenarioId} (route loader).`,
        error,
      );
      // component renders a dedicated error state
    }
  },
  component: ScenarioEvalPage,
});

function ScenarioEvalPage() {
  const navigate = Route.useNavigate();
  const { scenarioId } = Route.useParams();
  const { strategyId } = Route.useSearch();

  const bundleQuery = useQuery({
    ...scenarioBundleQueryOptions(scenarioId),
    enabled: Boolean(scenarioId),
  });

  const bundle = bundleQuery.data;
  const activeScenario = bundle?.scenario;
  const strategies = bundle?.strategies ?? [];

  const hasStrategy = Boolean(strategyId && strategies.some((s) => s.strategyId === strategyId));
  const selectedStrategyId = hasStrategy ? strategyId : strategies[0]?.strategyId;
  const activeStrategy = strategies.find((s) => s.strategyId === selectedStrategyId);

  const { getRating } = useScenarioRatings(scenarioId);
  const { getRating: getSetRating } = useScenarioSetRatings(scenarioId);

  const guidelines = activeStrategy?.guidelines ?? [];
  const guidelineIds = useMemo(() => guidelines.map((g) => g.entry.guideline.id), [guidelines]);

  const [activeGuidelineId, setActiveGuidelineId] = useState<string | undefined>(undefined);

  useEffect(() => {
    if (!guidelineIds.length) {
      setActiveGuidelineId(undefined);
      return;
    }

    if (activeGuidelineId && guidelineIds.includes(activeGuidelineId)) return;
    setActiveGuidelineId(guidelineIds[0]);
  }, [activeGuidelineId, guidelineIds]);

  function onSelectStrategy(nextStrategyId: string) {
    navigate({
      to: "/scenarios/$scenarioId",
      params: { scenarioId },
      search: { strategyId: nextStrategyId },
      replace: true,
    });
    setActiveGuidelineId(undefined);
  }

  function onRateGuideline(guidelineId: string, patch: Parameters<typeof upsertGuidelineRating>[0]["patch"]) {
    if (!scenarioId) return;

    upsertGuidelineRating({
      scenarioId,
      guidelineId,
      patch,
    });

    setActiveGuidelineId(guidelineId);
  }

  function onClearGuideline(guidelineId: string) {
    if (!scenarioId) return;
    deleteGuidelineRating({ scenarioId, guidelineId });
    setActiveGuidelineId(guidelineId);
  }

  return (
    <>
      <AppHeader />

      <div className="mx-auto w-full max-w-none px-4 py-6 lg:px-6">
        <main id="main" tabIndex={-1} className="min-w-0">
          {bundleQuery.isLoading ? (
            <div className="rounded-xl border bg-card p-6 text-sm text-muted-foreground">
              Loading scenario…
            </div>
          ) : bundleQuery.isError ? (
            <div className="rounded-xl border bg-card p-6 text-sm text-red-600">
              {bundleQuery.error instanceof Error
                ? bundleQuery.error.message
                : "Failed to load scenario."}
            </div>
          ) : !activeScenario ? (
            <div className="rounded-xl border bg-card p-6 text-sm text-muted-foreground">
              Scenario not found.
            </div>
          ) : (
            <div className="space-y-6 lg:grid lg:min-h-[calc(100dvh-var(--app-header-height,0px)-3rem)] lg:grid-cols-[minmax(0,1fr)_560px] lg:items-stretch lg:gap-6 lg:space-y-0 [@media(min-width:2400px)]:grid-cols-[minmax(0,1fr)_1080px]">
              <div className="lg:sticky lg:top-[calc(var(--app-header-height,0px)+1.5rem)] lg:self-start">
                <ScenarioPanel scenario={activeScenario} />
              </div>

              <section className="min-w-0">
                <StrategyTabs
                  strategies={strategies}
                  selectedStrategyId={selectedStrategyId}
                  onSelectStrategy={onSelectStrategy}
                />

                {activeStrategy?.guidelines?.length ? (
                  <>
                    <GuidelineDeck
                      scenarioId={scenarioId}
                      guidelines={activeStrategy.guidelines}
                      activeGuidelineId={activeGuidelineId}
                      getRating={getRating}
                      onRate={onRateGuideline}
                      onClear={onClearGuideline}
                    />
                    {selectedStrategyId ? (
                      <SetRatingPanel
                        scenarioId={scenarioId}
                        strategyId={selectedStrategyId}
                        rating={getSetRating(selectedStrategyId)}
                      />
                    ) : null}
                  </>
                ) : (
                  <div className="mt-4 p-2 text-sm text-muted-foreground">No guidelines.</div>
                )}
              </section>
            </div>
          )}
        </main>
      </div>
    </>
  );
}
