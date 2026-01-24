import { queryOptions } from '@tanstack/react-query'

import { getEvalScenarioBundle, getEvalScenarios } from './server/eval.server'
import {
  readCachedScenarioBundle,
  readCachedScenarios,
  writeCachedScenarioBundle,
  writeCachedScenarios,
} from './offline-cache'

function isClientOffline() {
  return typeof navigator !== 'undefined' && navigator && navigator.onLine === false
}

export const scenariosQueryOptions = queryOptions({
  queryKey: ['eval', 'scenarios'],
  networkMode: 'always',
  queryFn: async () => {
    const cached = readCachedScenarios()
    if (isClientOffline()) {
      if (cached) return cached
      throw new Error('Offline and no cached scenarios are available yet.')
    }

    try {
      const scenarios = await getEvalScenarios()
      writeCachedScenarios(scenarios)
      return scenarios
    } catch (error) {
      if (cached) return cached
      throw error
    }
  },
})

export const scenarioBundleQueryOptions = (scenarioId: string) =>
  queryOptions({
    queryKey: ['eval', 'scenario', scenarioId],
    networkMode: 'always',
    queryFn: async () => {
      const cached = readCachedScenarioBundle(scenarioId)
      if (isClientOffline()) {
        if (cached) return cached
        throw new Error(
          'Offline and this scenario is not cached yet. Open it once while online to cache it.',
        )
      }

      try {
        const bundle = await getEvalScenarioBundle({ data: { scenarioId } })
        writeCachedScenarioBundle(bundle)
        return bundle
      } catch (error) {
        if (cached) return cached
        throw error
      }
    },
  })
