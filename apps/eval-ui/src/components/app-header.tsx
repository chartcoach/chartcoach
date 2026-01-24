import { useLiveQuery } from '@tanstack/react-db'

import { relevanceRatingsCollection } from '@chartcoach/eval-ui/db-collections'
import type { RelevanceRating } from '@chartcoach/eval-ui/db-collections'
import { useOnlineStatus } from '@chartcoach/eval-ui/eval/use-online-status'
import { downloadRelevanceRatingsExport } from '@chartcoach/eval-ui/lib/export-relevance-ratings'

export function AppHeader() {
  const isOnline = useOnlineStatus()

  const { data } = useLiveQuery(
    (q) =>
      q
        .from({ rating: relevanceRatingsCollection })
        .select(({ rating }) => ({
          ...rating,
        })),
    [],
  )

  const ratings = (data ?? []) as RelevanceRating[]
  const ratingCount = ratings.length

  function onClear() {
    const ok = window.confirm(
      'Clear all saved ratings from this browser?\n\nThis cannot be undone.',
    )
    if (!ok) return
    relevanceRatingsCollection.utils.clearStorage()
    window.location.reload()
  }

  function onExport() {
    if (ratingCount === 0) return
    downloadRelevanceRatingsExport(ratings)
  }

  return (
    <header className="sticky top-0 z-50 border-b bg-background/80 backdrop-blur">
      <div className="mx-auto flex h-14 max-w-[1400px] items-center justify-between gap-4 px-4 lg:px-6">
        <div className="min-w-0">
          <div className="truncate text-sm font-semibold tracking-tight">
            ChartCoach · Guideline Relevance Eval
          </div>
          <div className="truncate text-xs text-muted-foreground">
            Rate retrieved guideline relevance (Likert 1–5). Saved locally.
          </div>
        </div>
        <div className="flex shrink-0 items-center gap-2">
          {!isOnline ? (
            <div className="rounded-full border px-2 py-1 text-xs text-muted-foreground">
              Offline
            </div>
          ) : null}
          <button
            type="button"
            onClick={onExport}
            disabled={ratingCount === 0}
            className="rounded-md border bg-background px-3 py-1.5 text-xs font-medium hover:bg-muted disabled:opacity-50 disabled:hover:bg-background"
          >
            Export <span className="tabular-nums">({ratingCount})</span>
          </button>
          <button
            type="button"
            onClick={onClear}
            className="rounded-md border bg-background px-3 py-1.5 text-xs font-medium hover:bg-muted"
          >
            Clear ratings
          </button>
        </div>
      </div>
    </header>
  )
}
