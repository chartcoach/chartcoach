import { Link } from '@tanstack/react-router'

import type { ScenarioSpec } from '@chartcoach/eval-ui/eval/schemas'
import { cn } from '@chartcoach/eval-ui/lib/utils'

export type ScenarioProgressSummary = {
  isLoading: boolean
  rated: number
  total: number | null
  statusLabel: string
  percent: number | null
  strategyBreakdown?: Array<{
    label: string
    rated: number
    total: number
    percent: number
  }>
}

function ProgressBar({
  percent,
  tone = 'neutral',
}: {
  percent: number
  tone?: 'neutral' | 'success' | 'warning'
}) {
  const clamped = Math.min(100, Math.max(0, percent))
  const barClass =
    tone === 'success'
      ? 'bg-emerald-500'
      : tone === 'warning'
        ? 'bg-amber-500'
        : 'bg-foreground/70'

  return (
    <div className="h-2 w-full overflow-hidden rounded-full bg-muted">
      <div className={cn('h-full transition-[width]', barClass)} style={{ width: `${clamped}%` }} />
    </div>
  )
}

export function ScenarioCard({
  scenario,
  progress,
}: {
  scenario: ScenarioSpec
  progress: ScenarioProgressSummary
}) {
  const tone =
    progress.percent === null
      ? 'neutral'
      : progress.percent >= 100
        ? 'success'
        : progress.percent > 0
          ? 'warning'
          : 'neutral'

  return (
    <Link
      to="/scenarios/$scenarioId"
      params={{ scenarioId: scenario.id }}
      className="group block rounded-xl border bg-card p-5 transition-colors hover:bg-card focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
    >
      <div className="space-y-2">
        <div className="flex items-start justify-between gap-3">
          <div className="min-w-0">
            <div className="text-xs font-semibold text-muted-foreground">Scenario</div>
            <h2 className="mt-1 text-balance text-base font-semibold leading-snug group-hover:underline group-hover:underline-offset-4">
              {scenario.title}
            </h2>
            {scenario.provenance?.source ? (
              <div className="mt-1 text-xs text-muted-foreground">
                {scenario.provenance.source}
              </div>
            ) : null}
          </div>

          <div className="shrink-0 text-right">
            {progress.isLoading ? (
              <div className="h-5 w-14 animate-pulse rounded bg-muted" />
            ) : (
              <div className="text-xs font-semibold text-muted-foreground">
                {progress.total === null ? '—' : `${progress.rated}/${progress.total}`}
              </div>
            )}
            <div className="mt-1 text-[11px] text-muted-foreground">{progress.statusLabel}</div>
          </div>
        </div>

        {scenario.chart?.uri ? (
          <div className="mt-3 overflow-hidden rounded-lg">
            <img
              src={scenario.chart.uri}
              alt={`Chart for scenario: ${scenario.title}`}
              className="h-32 w-full object-cover"
              loading="lazy"
              decoding="async"
            />
          </div>
        ) : null}

        <div className="mt-3 space-y-2">
          {progress.isLoading ? (
            <div className="space-y-2">
              <div className="h-2 w-full animate-pulse rounded-full bg-muted" />
              <div className="h-2 w-2/3 animate-pulse rounded-full bg-muted" />
            </div>
          ) : progress.percent === null ? (
            <ProgressBar percent={0} tone="neutral" />
          ) : (
            <ProgressBar percent={progress.percent} tone={tone} />
          )}

          {progress.strategyBreakdown?.length && !progress.isLoading ? (
            <div className="grid gap-1.5">
              {progress.strategyBreakdown.map((s) => (
                <div key={s.label} className="flex items-center gap-2">
                  <div className="w-28 truncate text-[11px] text-muted-foreground">
                    {s.label}
                  </div>
                  <div className="min-w-0 flex-1">
                    <ProgressBar
                      percent={Math.round(s.percent)}
                      tone={s.percent >= 100 ? 'success' : s.percent > 0 ? 'warning' : 'neutral'}
                    />
                  </div>
                  <div className="w-12 text-right text-[11px] text-muted-foreground tabular-nums">
                    {s.rated}/{s.total}
                  </div>
                </div>
              ))}
            </div>
          ) : null}
        </div>

        <div className="mt-3 space-y-2">
          {scenario.designer_intent ? (
            <div className="line-clamp-3 text-xs text-muted-foreground">
              <span className="font-semibold text-foreground/80">Designer intent:</span>{' '}
              {scenario.designer_intent}
            </div>
          ) : null}
          {scenario.query ? (
            <div className="line-clamp-2 text-xs text-muted-foreground">
              <span className="font-semibold text-foreground/80">Query:</span> {scenario.query}
            </div>
          ) : null}
        </div>
      </div>
    </Link>
  )
}
