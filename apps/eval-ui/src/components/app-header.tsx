import { useEffect, useRef } from 'react'

import { useLiveQuery } from '@tanstack/react-db'

import {
  clearRelevanceRatings,
  relevanceRatingsCollection,
} from '@chartcoach/eval-ui/db-collections'
import type { RelevanceRating } from '@chartcoach/eval-ui/db-collections'
import { useAutoUploadRelevanceRatings } from '@chartcoach/eval-ui/eval/use-auto-upload-relevance-ratings'
import { useOnlineStatus } from '@chartcoach/eval-ui/eval/use-online-status'
import { downloadRelevanceRatingsExport } from '@chartcoach/eval-ui/lib/export-relevance-ratings'

const SHORTCUTS_HELP = [
  { keys: '1–5', desc: 'rate active guideline' },
  { keys: 'N', desc: 'next unrated' },
  { keys: 'J / K', desc: 'next / previous guideline' },
  { keys: 'C', desc: 'clear rating' },
  { keys: '[ / ]', desc: 'prev / next scenario' },
]

export function AppHeader() {
  const headerRef = useRef<HTMLElement | null>(null)
  const isOnline = useOnlineStatus()

  useEffect(() => {
    const header = headerRef.current
    if (!header) return

    const root = document.documentElement
    const update = () => {
      const height = Math.ceil(header.getBoundingClientRect().height)
      root.style.setProperty('--app-header-height', `${height}px`)
    }

    update()

    const onResize = () => update()
    window.addEventListener('resize', onResize)

    if (typeof ResizeObserver === 'undefined') {
      return () => window.removeEventListener('resize', onResize)
    }

    const ro = new ResizeObserver(() => update())
    ro.observe(header)

    return () => {
      ro.disconnect()
      window.removeEventListener('resize', onResize)
    }
  }, [])

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

  const sync = useAutoUploadRelevanceRatings(ratings)

  function onClear() {
    const ok = window.confirm(
      'Clear all saved ratings from this browser?\n\nThis cannot be undone.',
    )
    if (!ok) return
    clearRelevanceRatings()
    window.location.reload()
  }

  function onExport() {
    if (ratingCount === 0) return
    downloadRelevanceRatingsExport(ratings)
  }

  return (
    <header
      ref={headerRef}
      className="sticky top-0 z-50 border-b bg-background/80 backdrop-blur"
    >
      <div className="mx-auto flex max-w-[1400px] flex-col gap-2 px-4 py-3 sm:flex-row sm:items-center sm:justify-between lg:px-6">
        <div className="min-w-0">
          <div className="truncate text-sm font-semibold tracking-tight">
            ChartCoach · Guideline Relevance Eval
          </div>
          <div className="truncate text-xs text-muted-foreground">
            Shortcuts: {SHORTCUTS_HELP.map((s) => `${s.keys} ${s.desc}`).join(' · ')}
          </div>
        </div>
        <div className="flex shrink-0 flex-wrap items-center justify-end gap-2">
          {sync.message ? (
            <div
              className="rounded-full border px-2 py-1 text-xs text-muted-foreground"
              title={sync.lastSuccessAt ? `Last synced: ${sync.lastSuccessAt}` : undefined}
            >
              {sync.message}
            </div>
          ) : sync.status === 'syncing' ? (
            <div className="rounded-full border px-2 py-1 text-xs text-muted-foreground">
              Syncing…
            </div>
          ) : sync.status === 'queued' ? (
            <div className="rounded-full border px-2 py-1 text-xs text-muted-foreground">
              Sync queued
            </div>
          ) : sync.status === 'error' ? (
            <div className="rounded-full border px-2 py-1 text-xs text-red-600">
              Sync failed
            </div>
          ) : sync.status === 'disabled' ? (
            <div className="rounded-full border px-2 py-1 text-xs text-muted-foreground">
              Sync disabled
            </div>
          ) : null}
          {!isOnline ? (
            <div className="rounded-full border px-2 py-1 text-xs text-muted-foreground">
              Offline
            </div>
          ) : null}
          <button
            type="button"
            onClick={onExport}
            disabled={ratingCount === 0}
            className="rounded-md border bg-background px-3 py-1.5 text-xs font-medium hover:bg-muted focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60 disabled:opacity-50 disabled:hover:bg-background"
          >
            Download <span className="tabular-nums">({ratingCount})</span>
          </button>
          <button
            type="button"
            onClick={onClear}
            className="rounded-md border bg-background px-3 py-1.5 text-xs font-medium hover:bg-muted focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
          >
            Clear ratings
          </button>
        </div>
      </div>
    </header>
  )
}
