import { queryOptions } from '@tanstack/react-query'

import {
  scenarioBundlesCacheCollection,
  scenariosCacheCollection,
} from '@chartcoach/eval-ui/db-collections/eval-cache'
import { getEvalScenarioBundle, getEvalScenarios } from './server/eval.server'

function isClientOffline() {
  return typeof navigator !== 'undefined' && navigator && navigator.onLine === false
}

function readCachedScenarios() {
  const docs = [...scenariosCacheCollection.state.values()]
  if (!docs.length) return

  return docs
    .slice()
    .sort((a, b) => a.index - b.index)
    .map((doc) => doc.scenario)
}

function writeCachedScenarios(scenarios: Awaited<ReturnType<typeof getEvalScenarios>>) {
  const cachedAt = new Date().toISOString()
  const ids = new Set<string>()

  scenarios.forEach((scenario, index) => {
    ids.add(scenario.id)
    const doc = { id: scenario.id, index, cachedAt, scenario }

    if (scenariosCacheCollection.state.has(doc.id)) {
      scenariosCacheCollection.update(doc.id, (draft) => {
        Object.assign(draft, doc)
      })
    } else {
      scenariosCacheCollection.insert(doc)
    }
  })

  for (const existingId of scenariosCacheCollection.state.keys()) {
    if (!ids.has(existingId)) {
      scenariosCacheCollection.delete(existingId)
    }
  }
}

function readCachedScenarioBundle(scenarioId: string) {
  const doc = scenarioBundlesCacheCollection.state.get(scenarioId)
  return doc?.bundle
}

function writeCachedScenarioBundle(bundle: Awaited<ReturnType<typeof getEvalScenarioBundle>>) {
  const cachedAt = new Date().toISOString()
  const doc = { id: bundle.scenario.id, cachedAt, bundle }

  if (scenarioBundlesCacheCollection.state.has(doc.id)) {
    scenarioBundlesCacheCollection.update(doc.id, (draft) => {
      Object.assign(draft, doc)
    })
  } else {
    scenarioBundlesCacheCollection.insert(doc)
  }
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
