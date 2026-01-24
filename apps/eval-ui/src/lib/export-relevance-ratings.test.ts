import { describe, expect, it } from 'vitest'

import type { RelevanceRating } from '@chartcoach/eval-ui/db-collections'

import {
  createRelevanceRatingsExport,
  serializeRelevanceRatingsExport,
} from './export-relevance-ratings'

describe('export relevance ratings', () => {
  it('includes format metadata and stable ordering', () => {
    const exportedAt = new Date('2026-01-23T00:00:00.000Z')

    const ratings: RelevanceRating[] = [
      {
        id: 'b::z',
        scenarioId: 'b',
        guidelineId: 'z',
        relevance: 1,
        createdAt: '2026-01-23T00:00:01.000Z',
        updatedAt: '2026-01-23T00:00:02.000Z',
      },
      {
        id: 'a::b',
        scenarioId: 'a',
        guidelineId: 'b',
        relevance: 5,
        createdAt: '2026-01-23T00:00:03.000Z',
        updatedAt: '2026-01-23T00:00:04.000Z',
      },
      {
        id: 'a::a',
        scenarioId: 'a',
        guidelineId: 'a',
        relevance: 3,
        createdAt: '2026-01-23T00:00:05.000Z',
        updatedAt: '2026-01-23T00:00:06.000Z',
      },
    ]

    const payload = createRelevanceRatingsExport(ratings, exportedAt)

    expect(payload.format).toBe('chartcoach.relevance-ratings.v1')
    expect(payload.exportedAt).toBe('2026-01-23T00:00:00.000Z')
    expect(payload.ratings.map((r) => r.id)).toEqual(['a::a', 'a::b', 'b::z'])
  })

  it('serializes to valid JSON', () => {
    const payload = createRelevanceRatingsExport([], new Date('2026-01-23T00:00:00.000Z'))
    const json = serializeRelevanceRatingsExport(payload)
    expect(JSON.parse(json)).toEqual(payload)
  })
})
