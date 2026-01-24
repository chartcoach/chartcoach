import type { RelevanceRating } from '@chartcoach/eval-ui/db-collections'

type RelevanceRatingsExportV1 = {
  format: 'chartcoach.relevance-ratings.v1'
  exportedAt: string
  ratings: RelevanceRating[]
}

function normalizeExportFilenameTimestamp(date: Date) {
  return date.toISOString().replaceAll(':', '').replaceAll('.', '-')
}

export function createRelevanceRatingsExport(
  ratings: RelevanceRating[],
  exportedAt: Date = new Date(),
): RelevanceRatingsExportV1 {
  const sortedRatings = [...ratings].sort((a, b) => {
    if (a.scenarioId !== b.scenarioId) return a.scenarioId.localeCompare(b.scenarioId)
    if (a.guidelineId !== b.guidelineId)
      return a.guidelineId.localeCompare(b.guidelineId)
    return a.id.localeCompare(b.id)
  })

  return {
    format: 'chartcoach.relevance-ratings.v1',
    exportedAt: exportedAt.toISOString(),
    ratings: sortedRatings,
  }
}

export function serializeRelevanceRatingsExport(payload: RelevanceRatingsExportV1) {
  return JSON.stringify(payload, null, 2)
}

export function downloadJsonFile(filename: string, json: string) {
  const blob = new Blob([json], { type: 'application/json;charset=utf-8' })
  const url = URL.createObjectURL(blob)

  const link = document.createElement('a')
  link.href = url
  link.download = filename
  link.rel = 'noreferrer'

  document.body.appendChild(link)
  link.click()
  link.remove()

  URL.revokeObjectURL(url)
}

export function downloadRelevanceRatingsExport(
  ratings: RelevanceRating[],
  exportedAt: Date = new Date(),
) {
  const payload = createRelevanceRatingsExport(ratings, exportedAt)
  const json = serializeRelevanceRatingsExport(payload)
  const filename = `chartcoach-relevance-ratings-${normalizeExportFilenameTimestamp(exportedAt)}.json`
  downloadJsonFile(filename, json)
  return { filename, count: payload.ratings.length }
}
