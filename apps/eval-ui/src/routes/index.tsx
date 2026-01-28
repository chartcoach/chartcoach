import { createFileRoute } from "@tanstack/react-router";
import { useQueries, useQuery } from "@tanstack/react-query";
import { useLiveQuery } from "@tanstack/react-db";
import { useMemo } from "react";

import { AppHeader } from "@chartcoach/eval-ui/components/app-header";
import { ScenarioCard } from "@chartcoach/eval-ui/components/scenario-card";
import { relevanceRatingsCollection } from "@chartcoach/eval-ui/db-collections";
import {
  scenarioBundleQueryOptions,
  scenariosQueryOptions,
} from "@chartcoach/eval-ui/eval/queries";

export const Route = createFileRoute("/")({
  ssr: false,
  loader: async ({ context }) => {
    try {
      await context.queryClient.ensureQueryData(scenariosQueryOptions);
    } catch (error) {
      console.warn("[eval-ui] Failed to prefetch scenarios (route loader).", error);
      // component renders a dedicated error state
    }
  },
  component: LandingPage,
});

function LandingPage() {
  const scenariosQuery = useQuery(scenariosQueryOptions);
  const scenarios = scenariosQuery.data ?? [];

  const { data: ratingsData } = useLiveQuery(
    (q) =>
      q.from({ rating: relevanceRatingsCollection }).select(({ rating }) => ({
        scenarioId: rating.scenarioId,
        guidelineId: rating.guidelineId,
      })),
    [],
  );

  const ratingsByScenarioId = useMemo(() => {
    const byScenario = new Map<string, Set<string>>();
    for (const row of ratingsData ?? []) {
      const key = row.scenarioId as string;
      const existing = byScenario.get(key);
      const next = existing ?? new Set<string>();
      next.add(row.guidelineId as string);
      if (!existing) byScenario.set(key, next);
    }
    return byScenario;
  }, [ratingsData]);

  const bundleQueries = useQueries({
    queries: scenarios.map((scenario) => ({
      ...scenarioBundleQueryOptions(scenario.id),
      enabled: scenarios.length > 0,
      staleTime: 60_000,
    })),
  });

  const bundleByScenarioId = useMemo(() => {
    const map = new Map<string, (typeof bundleQueries)[number]["data"]>();
    scenarios.forEach((scenario, index) => {
      map.set(scenario.id, bundleQueries[index]?.data);
    });
    return map;
  }, [bundleQueries, scenarios]);

  if (scenariosQuery.isLoading) {
    return (
      <div className="mx-auto max-w-350 p-6 text-sm text-muted-foreground">Loading scenarios…</div>
    );
  }

  if (scenariosQuery.isError) {
    const message =
      scenariosQuery.error instanceof Error
        ? scenariosQuery.error.message
        : "Failed to load scenarios.";

    return <div className="mx-auto max-w-350 p-6 text-sm text-red-600">{message}</div>;
  }

  return (
    <>
      <AppHeader />

      <div className="mx-auto w-full max-w-350 px-4 py-10 lg:px-6 2xl:max-w-450">
        <main id="main" tabIndex={-1} className="min-w-0">
          <header className="space-y-3">
            <h1 className="text-balance text-2xl font-semibold sm:text-3xl">
              Guideline relevance evaluation
            </h1>
            <p className="max-w-prose text-sm text-muted-foreground text-pretty lg:max-w-240">
              Pick a scenario to start. Your task on each scenario page is to rate how relevant the
              listed visualization guidelines are for the scenario and the chart.
            </p>
          </header>

          {scenarios.length ? (
            <section className="mt-8">
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {scenarios.map((scenario, index) => {
                  const bundleQuery = bundleQueries[index];
                  const bundle = bundleByScenarioId.get(scenario.id);
                  const ratedIds = ratingsByScenarioId.get(scenario.id) ?? new Set();

                  if (!bundleQuery || bundleQuery.isLoading) {
                    return (
                      <ScenarioCard
                        key={scenario.id}
                        scenario={scenario}
                        progress={{
                          isLoading: true,
                          rated: ratedIds.size,
                          total: null,
                          percent: null,
                          statusLabel: ratedIds.size ? "In progress" : "Not started",
                        }}
                      />
                    );
                  }

                  if (bundleQuery.isError) {
                    const message =
                      bundleQuery.error instanceof Error
                        ? bundleQuery.error.message.toLowerCase()
                        : "";

                    const statusLabel = message.includes("offline")
                      ? ratedIds.size
                        ? "Offline (open once online)"
                        : "Offline"
                      : "Load failed";

                    return (
                      <ScenarioCard
                        key={scenario.id}
                        scenario={scenario}
                        progress={{
                          isLoading: false,
                          rated: ratedIds.size,
                          total: null,
                          percent: null,
                          statusLabel,
                        }}
                      />
                    );
                  }

                  const unionIds = new Set<string>();
                  const strategyBreakdown =
                    bundle?.strategies?.map((strategy) => {
                      const ids = strategy.guidelines.map((g) => g.entry.guideline.id);
                      ids.forEach((id) => unionIds.add(id));
                      const rated = ids.reduce(
                        (count, id) => (ratedIds.has(id) ? count + 1 : count),
                        0,
                      );
                      const total = ids.length;
                      return {
                        label: strategy.strategyName,
                        rated,
                        total,
                        percent: total ? (rated / total) * 100 : 0,
                      };
                    }) ?? [];

                  const totalUnique = unionIds.size;
                  const ratedUnique = [...unionIds].reduce(
                    (count, id) => (ratedIds.has(id) ? count + 1 : count),
                    0,
                  );
                  const percent = totalUnique ? Math.round((ratedUnique / totalUnique) * 100) : 0;

                  const statusLabel =
                    totalUnique === 0
                      ? "No guidelines"
                      : percent >= 100
                        ? "Done"
                        : ratedUnique === 0
                          ? "Not started"
                          : `${Math.max(0, totalUnique - ratedUnique)} left`;

                  return (
                    <ScenarioCard
                      key={scenario.id}
                      scenario={scenario}
                      progress={{
                        isLoading: false,
                        rated: ratedUnique,
                        total: totalUnique,
                        percent,
                        statusLabel,
                        strategyBreakdown,
                      }}
                    />
                  );
                })}
              </div>
            </section>
          ) : (
            <div className="mt-8 rounded-xl border bg-card p-6 text-sm text-muted-foreground">
              No scenarios found.
            </div>
          )}
        </main>
      </div>
    </>
  );
}
