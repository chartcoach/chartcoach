import { createFileRoute, redirect } from '@tanstack/react-router'
import { useQuery } from '@tanstack/react-query'
import { z } from 'zod'

import { AppHeader } from '@chartcoach/eval-ui/components/app-header'
import { GuidelineCard } from '@chartcoach/eval-ui/components/guideline-card'
import { ScenarioSidebar } from '@chartcoach/eval-ui/components/scenario-sidebar'
import { StrategyPicker } from '@chartcoach/eval-ui/components/strategy-picker'
import {
  deleteRelevanceRating,
  upsertRelevanceRating,
} from '@chartcoach/eval-ui/db-collections'
import type { ScenarioSpec } from '@chartcoach/eval-ui/eval/schemas'
import {
  scenarioBundleQueryOptions,
  scenariosQueryOptions,
} from '@chartcoach/eval-ui/eval/queries'
import { useScenarioRatings } from '@chartcoach/eval-ui/eval/use-scenario-ratings'

export const Route = createFileRoute('/')({
  validateSearch: z.object({
    scenarioId: z.string().optional(),
    strategyId: z.string().optional(),
  }),
  ssr: false,
  loaderDeps: ({ search }) => ({
    scenarioId: search.scenarioId,
    strategyId: search.strategyId,
  }),
  loader: async ({ context, deps }) => {
    let scenarios: ScenarioSpec[]
    try {
      scenarios = await context.queryClient.ensureQueryData(scenariosQueryOptions)
    } catch {
      return
    }

    const scenarioId = deps.scenarioId ?? scenarios[0]?.id
    if (!scenarioId) return

    if (!deps.scenarioId) {
      throw redirect({
        to: '/',
        search: { scenarioId, strategyId: deps.strategyId },
      })
    }

    try {
      await context.queryClient.ensureQueryData(scenarioBundleQueryOptions(scenarioId))
    } catch {
      // component renders a dedicated error state
    }
  },
  component: EvalApp,
})

function EvalApp() {
  const navigate = Route.useNavigate()
  const { scenarioId, strategyId } = Route.useSearch()

  const scenariosQuery = useQuery(scenariosQueryOptions)
  const scenarios = scenariosQuery.data ?? []

  const activeScenarioId = scenarioId ?? scenarios[0]?.id

  const bundleQuery = useQuery({
    ...scenarioBundleQueryOptions(activeScenarioId ?? ''),
    enabled: Boolean(activeScenarioId),
  })

  const bundle = bundleQuery.data
  const activeScenario = bundle?.scenario
  const strategies = bundle?.strategies ?? []

  const hasStrategy = Boolean(
    strategyId && strategies.some((s) => s.strategyId === strategyId),
  )
  const selectedStrategyId = hasStrategy ? strategyId : strategies[0]?.strategyId
  const activeStrategy = strategies.find((s) => s.strategyId === selectedStrategyId)

  const { getRating } = useScenarioRatings(activeScenarioId)

  const ratedCount = activeStrategy
    ? activeStrategy.guidelines.reduce((count, g) => {
        const guidelineId = g.entry.guideline.id
        return getRating(guidelineId) ? count + 1 : count
      }, 0)
    : 0

  function onSelectScenario(nextScenarioId: string) {
    navigate({
      to: '/',
      search: {
        scenarioId: nextScenarioId,
        strategyId: selectedStrategyId,
      },
    })
  }

  function onSelectStrategy(nextStrategyId: string) {
    if (!activeScenarioId) return

    navigate({
      to: '/',
      search: { scenarioId: activeScenarioId, strategyId: nextStrategyId },
      replace: true,
    })
  }

  function onRateGuideline(guidelineId: string, relevance: number) {
    if (!activeScenarioId) return

    upsertRelevanceRating({
      scenarioId: activeScenarioId,
      guidelineId,
      relevance,
    })
  }

  function onClearGuideline(guidelineId: string) {
    if (!activeScenarioId) return
    deleteRelevanceRating({ scenarioId: activeScenarioId, guidelineId })
  }

  if (scenariosQuery.isLoading) {
    return (
      <div className="mx-auto max-w-[1400px] p-6 text-sm text-muted-foreground">
        Loading scenarios…
      </div>
    )
  }

  if (scenariosQuery.isError) {
    const message =
      scenariosQuery.error instanceof Error
        ? scenariosQuery.error.message
        : 'Failed to load scenarios.'

    return (
      <div className="mx-auto max-w-[1400px] p-6 text-sm text-red-600">
        {message}
      </div>
    )
  }

  if (!activeScenarioId) {
    return (
      <div className="mx-auto max-w-[1400px] p-6 text-sm text-muted-foreground">
        No scenarios found.
      </div>
    )
  }

  return (
    <>
      <AppHeader />

      <div className="mx-auto max-w-[1400px] px-4 py-8 lg:px-6">
        <div className="grid gap-8 lg:grid-cols-[280px_minmax(0,1fr)]">
          <div className="lg:sticky lg:top-20 lg:self-start">
            <ScenarioSidebar
              scenarios={scenarios}
              selectedScenarioId={activeScenarioId}
              onSelect={onSelectScenario}
            />
          </div>

          <main className="min-w-0">
            {bundleQuery.isLoading ? (
              <div className="rounded-xl border bg-card p-6 text-sm text-muted-foreground">
                Loading scenario…
              </div>
            ) : bundleQuery.isError ? (
              <div className="rounded-xl border bg-card p-6 text-sm text-red-600">
                {bundleQuery.error instanceof Error
                  ? bundleQuery.error.message
                  : 'Failed to load scenario.'}
              </div>
            ) : !activeScenario ? (
              <div className="rounded-xl border bg-card p-6 text-sm text-muted-foreground">
                Scenario not found.
              </div>
            ) : (
              <div className="space-y-8">
                <header className="space-y-2">
                  <h1 className="text-balance text-2xl font-semibold leading-tight tracking-tight">
                    {activeScenario.title}
                  </h1>
                  <div className="flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
                    <span className="font-mono">{activeScenario.id}</span>
                    {activeScenario.provenance?.source ? (
                      <>
                        <span aria-hidden="true">·</span>
                        <span>{activeScenario.provenance.source}</span>
                      </>
                    ) : null}
                  </div>
                </header>

                {activeScenario.chart?.uri ? (
                  <section className="rounded-xl border bg-card p-4">
                    <a
                      href={activeScenario.chart.uri}
                      target="_blank"
                      rel="noreferrer"
                      className="block rounded-lg focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                      title="Open full-size chart image"
                    >
                      <img
                        src={activeScenario.chart.uri}
                        alt={`Chart for scenario: ${activeScenario.title}`}
                        className="h-auto w-full rounded-lg"
                        loading="lazy"
                        decoding="async"
                      />
                    </a>
                  </section>
                ) : null}

                <section className="rounded-xl border bg-card p-5">
                  <div className="space-y-5">
                    <div>
                      <div className="text-xs font-semibold text-muted-foreground">
                        Query
                      </div>
                      <div className="mt-2 max-w-prose whitespace-pre-wrap text-sm leading-relaxed">
                        {activeScenario.query ?? '—'}
                      </div>
                    </div>

                    <div className="border-t pt-5">
                      <div className="text-xs font-semibold text-muted-foreground">
                        Designer intent
                      </div>
                      <div className="mt-2 max-w-prose whitespace-pre-wrap text-sm leading-relaxed">
                        {activeScenario.designer_intent ?? '—'}
                      </div>
                    </div>
                  </div>
                </section>

                <section className="space-y-4">
                  <div className="flex flex-wrap items-end justify-between gap-3">
                    <div className="space-y-1">
                      <h2 className="text-sm font-semibold">
                        Retrieved guidelines
                      </h2>
                      <div className="text-xs text-muted-foreground">
                        Dummy results · ratings shared across strategies for this scenario.
                      </div>
                    </div>
                    {activeStrategy ? (
                      <div className="text-xs tabular-nums text-muted-foreground">
                        Rated {ratedCount}/{activeStrategy.guidelines.length}
                      </div>
                    ) : null}
                  </div>

                  <StrategyPicker
                    strategies={strategies}
                    selectedStrategyId={selectedStrategyId}
                    onSelect={onSelectStrategy}
                  />

                  {activeStrategy?.guidelines?.length ? (
                    <div className="space-y-4">
                      {activeStrategy.guidelines.map((g) => (
                        <GuidelineCard
                          key={g.entry.guideline.id}
                          scenarioId={activeScenarioId}
                          result={g}
                          rating={getRating(g.entry.guideline.id)?.relevance}
                          onRate={onRateGuideline}
                          onClear={onClearGuideline}
                        />
                      ))}
                    </div>
                  ) : (
                    <div className="rounded-xl border bg-card p-6 text-sm text-muted-foreground">
                      No guidelines.
                    </div>
                  )}
                </section>
              </div>
            )}
          </main>
        </div>
      </div>
    </>
  )
}
