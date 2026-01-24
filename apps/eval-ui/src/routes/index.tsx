import { createFileRoute, redirect } from '@tanstack/react-router'
import { useQuery } from '@tanstack/react-query'
import { useEffect, useMemo, useState } from 'react'
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

const AUTO_ADVANCE_KEY = 'chartcoach/eval-ui/prefs/auto-advance/v1'
const COMPACT_MODE_KEY = 'chartcoach/eval-ui/prefs/compact-mode/v1'

function usePersistedBoolean(key: string, defaultValue: boolean) {
  const [value, setValue] = useState(() => {
    if (typeof window === 'undefined') return defaultValue
    try {
      const raw = window.localStorage.getItem(key)
      if (raw === null) return defaultValue
      return raw === '1'
    } catch {
      return defaultValue
    }
  })

  useEffect(() => {
    if (typeof window === 'undefined') return
    try {
      window.localStorage.setItem(key, value ? '1' : '0')
    } catch {
      // ignore quota / privacy errors
    }
  }, [key, value])

  return [value, setValue] as const
}

function guidelineDomId(guidelineId: string) {
  return `guideline-${encodeURIComponent(guidelineId)}`
}

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

  const guidelines = activeStrategy?.guidelines ?? []
  const guidelineIds = useMemo(
    () => guidelines.map((g) => g.entry.guideline.id),
    [guidelines],
  )

  const [autoAdvance, setAutoAdvance] = usePersistedBoolean(AUTO_ADVANCE_KEY, true)
  const [compactMode, setCompactMode] = usePersistedBoolean(COMPACT_MODE_KEY, false)

  const [activeGuidelineId, setActiveGuidelineId] = useState<string | undefined>(undefined)

  useEffect(() => {
    if (!guidelineIds.length) {
      setActiveGuidelineId(undefined)
      return
    }

    if (activeGuidelineId && guidelineIds.includes(activeGuidelineId)) return
    setActiveGuidelineId(guidelineIds[0])
  }, [activeGuidelineId, guidelineIds])

  const ratedCount = activeStrategy
    ? activeStrategy.guidelines.reduce((count, g) => {
        const guidelineId = g.entry.guideline.id
        return getRating(guidelineId) ? count + 1 : count
      }, 0)
    : 0

  const totalGuidelines = guidelines.length
  const progress = totalGuidelines ? ratedCount / totalGuidelines : 0

  function scrollToGuideline(nextGuidelineId: string, behavior: ScrollBehavior = 'smooth') {
    if (typeof document === 'undefined') return
    const el = document.getElementById(guidelineDomId(nextGuidelineId))
    if (!el) return

    el.scrollIntoView({ block: 'center', behavior })
    if ('focus' in el) {
      ;(el as HTMLElement).focus({ preventScroll: true })
    }
  }

  function findNextGuidelineId(direction: 1 | -1) {
    if (!guidelineIds.length) return
    const current = activeGuidelineId ?? guidelineIds[0]
    const idx = guidelineIds.indexOf(current)
    const base = idx === -1 ? 0 : idx
    const next = (base + direction + guidelineIds.length) % guidelineIds.length
    return guidelineIds[next]
  }

  function findNextUnratedId(fromGuidelineId?: string) {
    if (!guidelineIds.length) return
    const startId = fromGuidelineId ?? activeGuidelineId ?? guidelineIds[0]
    const startIdx = guidelineIds.indexOf(startId)
    const start = startIdx === -1 ? 0 : startIdx

    for (let i = start + 1; i < guidelineIds.length; i++) {
      const id = guidelineIds[i]
      if (!getRating(id)) return id
    }

    for (let i = 0; i < start; i++) {
      const id = guidelineIds[i]
      if (!getRating(id)) return id
    }

    return
  }

  function onSelectScenario(nextScenarioId: string) {
    navigate({
      to: '/',
      search: {
        scenarioId: nextScenarioId,
        strategyId: selectedStrategyId,
      },
    })
    setActiveGuidelineId(undefined)
  }

  function onSelectStrategy(nextStrategyId: string) {
    if (!activeScenarioId) return

    navigate({
      to: '/',
      search: { scenarioId: activeScenarioId, strategyId: nextStrategyId },
      replace: true,
    })
    setActiveGuidelineId(undefined)
  }

  function onRateGuideline(guidelineId: string, relevance: number) {
    if (!activeScenarioId) return

    upsertRelevanceRating({
      scenarioId: activeScenarioId,
      guidelineId,
      relevance,
    })

    setActiveGuidelineId(guidelineId)

    if (autoAdvance) {
      const nextUnrated = findNextUnratedId(guidelineId)
      if (nextUnrated) {
        setActiveGuidelineId(nextUnrated)
        requestAnimationFrame(() => scrollToGuideline(nextUnrated))
      }
    }
  }

  function onClearGuideline(guidelineId: string) {
    if (!activeScenarioId) return
    deleteRelevanceRating({ scenarioId: activeScenarioId, guidelineId })
    setActiveGuidelineId(guidelineId)
  }

  function onJumpToNextUnrated() {
    const next = findNextUnratedId()
    if (!next) return
    setActiveGuidelineId(next)
    scrollToGuideline(next)
  }

  useEffect(() => {
    function isEditableTarget(target: EventTarget | null) {
      if (!(target instanceof HTMLElement)) return false
      const tag = target.tagName.toLowerCase()
      if (tag === 'input' || tag === 'textarea' || tag === 'select') return true
      return Boolean(target.isContentEditable)
    }

    function handleKeyDown(event: KeyboardEvent) {
      if (event.metaKey || event.ctrlKey || event.altKey) return
      if (isEditableTarget(event.target)) return
      if (!activeScenarioId) return
      if (!guidelineIds.length) return

      const currentGuidelineId = activeGuidelineId ?? guidelineIds[0]
      if (!currentGuidelineId) return

      if (event.key === 'j') {
        const next = findNextGuidelineId(1)
        if (!next) return
        event.preventDefault()
        setActiveGuidelineId(next)
        scrollToGuideline(next)
        return
      }

      if (event.key === 'k') {
        const prev = findNextGuidelineId(-1)
        if (!prev) return
        event.preventDefault()
        setActiveGuidelineId(prev)
        scrollToGuideline(prev)
        return
      }

      if (event.key === 'n' || event.key === 'N') {
        const next = findNextUnratedId()
        if (!next) return
        event.preventDefault()
        setActiveGuidelineId(next)
        scrollToGuideline(next)
        return
      }

      if (event.key === 'c' || event.key === 'C') {
        event.preventDefault()
        onClearGuideline(currentGuidelineId)
        return
      }

      const number = Number(event.key)
      if (number >= 1 && number <= 5) {
        event.preventDefault()
        onRateGuideline(currentGuidelineId, number)
        return
      }

      if (event.key === '[' || event.key === ']') {
        const idx = scenarios.findIndex((s) => s.id === activeScenarioId)
        if (idx === -1) return
        const nextIdx =
          event.key === '['
            ? Math.max(0, idx - 1)
            : Math.min(scenarios.length - 1, idx + 1)
        const nextScenario = scenarios[nextIdx]
        if (!nextScenario || nextScenario.id === activeScenarioId) return
        event.preventDefault()
        onSelectScenario(nextScenario.id)
      }
    }

    window.addEventListener('keydown', handleKeyDown, { passive: false })
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [
    activeGuidelineId,
    activeScenarioId,
    guidelineIds,
    scenarios,
    autoAdvance,
  ])

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
        <div className="grid gap-6 lg:grid-cols-[280px_minmax(0,1fr)]">
          <div className="hidden lg:block lg:sticky lg:top-[var(--app-header-height)] lg:self-start">
            <ScenarioSidebar
              scenarios={scenarios}
              selectedScenarioId={activeScenarioId}
              onSelect={onSelectScenario}
            />
          </div>

          <main id="main" tabIndex={-1} className="min-w-0">
            <div className="lg:hidden">
              <div className="rounded-xl border bg-card p-4">
                <label
                  htmlFor="scenario-select"
                  className="text-xs font-semibold text-muted-foreground"
                >
                  Scenario
                </label>
                <select
                  id="scenario-select"
                  value={activeScenarioId}
                  onChange={(e) => onSelectScenario(e.currentTarget.value)}
                  className="mt-2 w-full rounded-md border bg-background px-3 py-2 text-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                >
                  {scenarios.map((s) => (
                    <option key={s.id} value={s.id}>
                      {s.title}
                    </option>
                  ))}
                </select>
              </div>
            </div>

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
              <div className="grid gap-8">
                <div className="grid gap-4">
                  <header className="flex flex-wrap items-start justify-between gap-3">
                    <div className="space-y-1">
                      <h1 className="text-balance text-xl font-semibold leading-tight tracking-tight sm:text-2xl">
                        {activeScenario.title}
                      </h1>
                      {activeScenario.provenance?.source ? (
                        <div className="text-xs text-muted-foreground">
                          {activeScenario.provenance.source}
                        </div>
                      ) : null}
                    </div>
                    <div className="flex items-center gap-2">
                      <button
                        type="button"
                        onClick={() => setCompactMode((v) => !v)}
                        className="rounded-md border bg-background px-3 py-1.5 text-xs font-medium hover:bg-muted focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                      >
                        {compactMode ? 'Show details' : 'Compact'}
                      </button>
                    </div>
                  </header>

                  {!compactMode ? (
                    <>
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
                              width={1600}
                              height={900}
                              className="mx-auto max-h-80 w-auto max-w-full rounded-lg object-contain sm:max-h-96 lg:max-h-[28rem]"
                              loading="eager"
                              fetchPriority="high"
                              decoding="async"
                            />
                          </a>
                        </section>
                      ) : null}

                      <section className="rounded-xl border bg-card p-5">
                        <div className="space-y-5 lg:space-y-0 lg:grid lg:grid-cols-2 lg:gap-6">
                          <div>
                            <div className="text-xs font-semibold text-muted-foreground">
                              Query
                            </div>
                            <div className="mt-2 max-w-prose whitespace-pre-wrap text-sm leading-relaxed">
                              {activeScenario.query ?? '—'}
                            </div>
                          </div>

                          <div>
                            <div className="text-xs font-semibold text-muted-foreground">
                              Designer intent
                            </div>
                            <div className="mt-2 max-w-prose whitespace-pre-wrap text-sm leading-relaxed">
                              {activeScenario.designer_intent ?? '—'}
                            </div>
                          </div>
                        </div>
                      </section>
                    </>
                  ) : null}
                </div>

                <section className="space-y-4">
                    <div className="sticky top-[var(--app-header-height)] z-40 -mx-4 bg-background/90 px-4 pb-4 pt-3 backdrop-blur lg:-mx-0 lg:rounded-xl lg:border lg:bg-background/70 lg:px-5 lg:pt-4">
                    <div className="flex flex-wrap items-end justify-between gap-3">
                      <div className="space-y-1">
                        <h2 className="text-sm font-semibold">
                          Retrieved guidelines
                        </h2>
                        <div className="text-xs text-muted-foreground">
                          1–5 rate · N next unrated · J/K next/prev · C clear · [ / ] scenarios
                        </div>
                      </div>

                      {totalGuidelines ? (
                        <div className="flex items-center gap-2">
                          <div className="h-2 w-28 overflow-hidden rounded-full bg-muted">
                            <div
                              className="h-full bg-foreground/60"
                              style={{ width: `${Math.min(100, Math.round(progress * 100))}%` }}
                            />
                          </div>
                          <div className="text-xs tabular-nums text-muted-foreground">
                            Rated {ratedCount}/{totalGuidelines}
                          </div>
                        </div>
                      ) : null}
                    </div>

                    <div className="mt-3 flex flex-wrap items-center justify-between gap-3">
                      <StrategyPicker
                        strategies={strategies}
                        selectedStrategyId={selectedStrategyId}
                        onSelect={onSelectStrategy}
                      />

                      <div className="flex flex-wrap items-center gap-2">
                        <button
                          type="button"
                          onClick={onJumpToNextUnrated}
                          disabled={!findNextUnratedId()}
                          className="rounded-md border bg-background px-3 py-1.5 text-xs font-medium hover:bg-muted focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60 disabled:opacity-50 disabled:hover:bg-background"
                        >
                          Next unrated
                        </button>

                        <label className="flex items-center gap-2 rounded-md border bg-background px-3 py-1.5 text-xs text-muted-foreground hover:bg-muted">
                          <input
                            type="checkbox"
                            checked={autoAdvance}
                            onChange={(e) => setAutoAdvance(e.currentTarget.checked)}
                            className="h-4 w-4 accent-foreground focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                          />
                          Auto-advance
                        </label>
                      </div>
                    </div>
                  </div>

                  {activeStrategy?.guidelines?.length ? (
                    <div className="space-y-4">
                      {activeStrategy.guidelines.map((g) => (
                        <GuidelineCard
                          key={g.entry.guideline.id}
                          scenarioId={activeScenarioId}
                          result={g}
                          rating={getRating(g.entry.guideline.id)?.relevance}
                          isActive={g.entry.guideline.id === activeGuidelineId}
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
