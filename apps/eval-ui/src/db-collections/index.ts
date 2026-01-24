import { createCollection, localStorageCollectionOptions } from '@tanstack/react-db'
import { z } from 'zod'

const RelevanceRatingSchema = z.object({
  id: z.string().min(1),
  scenarioId: z.string().min(1),
  guidelineId: z.string().min(1),
  relevance: z.number().int().min(1).max(5),
  createdAt: z.string().min(1),
  updatedAt: z.string().min(1),
})

export type RelevanceRating = z.infer<typeof RelevanceRatingSchema>

export const relevanceRatingsCollection = createCollection(
  localStorageCollectionOptions({
    storageKey: 'chartcoach/eval-ui/relevance-ratings/v1',
    getKey: (rating) => rating.id,
    schema: RelevanceRatingSchema,
  }),
)

export function makeRelevanceRatingId(scenarioId: string, guidelineId: string) {
  return `${scenarioId}::${guidelineId}`
}

export function upsertRelevanceRating({
  scenarioId,
  guidelineId,
  relevance,
  now = new Date().toISOString(),
}: {
  scenarioId: string
  guidelineId: string
  relevance: number
  now?: string
}) {
  const id = makeRelevanceRatingId(scenarioId, guidelineId)

  if (relevanceRatingsCollection.state.has(id)) {
    relevanceRatingsCollection.update(id, (draft) => {
      draft.relevance = relevance
      draft.updatedAt = now
    })
    return
  }

  relevanceRatingsCollection.insert({
    id,
    scenarioId,
    guidelineId,
    relevance,
    createdAt: now,
    updatedAt: now,
  })
}

export function deleteRelevanceRating({
  scenarioId,
  guidelineId,
}: {
  scenarioId: string
  guidelineId: string
}) {
  const id = makeRelevanceRatingId(scenarioId, guidelineId)
  if (relevanceRatingsCollection.state.has(id)) {
    relevanceRatingsCollection.delete(id)
  }
}
