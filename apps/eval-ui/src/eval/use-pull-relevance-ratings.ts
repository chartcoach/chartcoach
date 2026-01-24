import { queryOptions, useQuery } from '@tanstack/react-query'
import { useEffect, useMemo, useRef } from 'react'

import {
  mergeRelevanceRatings,
  relevanceRatingsCollection,
} from '@chartcoach/eval-ui/db-collections'
import type { RelevanceRatingsExportV1 } from '@chartcoach/eval-ui/eval/relevance-ratings'
import { getDeviceId } from '@chartcoach/eval-ui/eval/device-id'
import {
  SYNC_LAST_SIGNATURE_STORAGE_KEY,
  SYNC_LAST_SUCCESS_AT_STORAGE_KEY,
  SYNC_LAST_SUCCESS_KEY_STORAGE_KEY,
  getLocalStorageItem,
  makeRatingsSignature,
  setLocalStorageItem,
} from '@chartcoach/eval-ui/eval/relevance-ratings-sync-metadata'
import { useOnlineStatus } from '@chartcoach/eval-ui/eval/use-online-status'
import { downloadLatestRelevanceRatingsExport } from '@chartcoach/eval-ui/eval/server/relevance-ratings-sync.server'

type PullStatus = 'idle' | 'pulling' | 'synced' | 'error' | 'disabled'

function latestRatingsExportQueryOptions(deviceId: string) {
  return queryOptions({
    queryKey: ['eval', 'relevance-ratings', 'latest-export', deviceId],
    networkMode: 'online',
    queryFn: async () =>
      await downloadLatestRelevanceRatingsExport({
        data: { deviceId },
      }),
    staleTime: 30_000,
  })
}

export function usePullRelevanceRatingsFromS3() {
  const isOnline = useOnlineStatus()
  const deviceId = useMemo(() => getDeviceId(), [])
  const lastImportedKeyRef = useRef<string | null>(null)

  const query = useQuery({
    ...latestRatingsExportQueryOptions(deviceId),
    enabled: isOnline,
    retry: 1,
  })

  useEffect(() => {
    if (!query.data?.found) return
    if (lastImportedKeyRef.current === query.data.key) return
    lastImportedKeyRef.current = query.data.key

    mergeRelevanceRatings(query.data.export.ratings)

    const lastSignature = getLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY)
    if (lastSignature) return

    const remoteSignature = makeRatingsSignature(query.data.export.ratings)
    const localSignature = makeRatingsSignature([
      ...relevanceRatingsCollection.state.values(),
    ])

    if (remoteSignature !== localSignature) return

    setLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY, localSignature)
    setLocalStorageItem(SYNC_LAST_SUCCESS_AT_STORAGE_KEY, query.data.export.exportedAt)
    setLocalStorageItem(SYNC_LAST_SUCCESS_KEY_STORAGE_KEY, query.data.key)
  }, [query.data])

  const pulledExport: RelevanceRatingsExportV1 | null =
    query.data?.found ? query.data.export : null

  const status: PullStatus =
    query.isError && query.error instanceof Error
      ? query.error.message.toLowerCase().includes('not configured')
        ? 'disabled'
        : 'error'
      : query.isFetching
        ? 'pulling'
        : pulledExport
          ? 'synced'
          : 'idle'

  return {
    status,
    isOnline,
    exportedAt: pulledExport?.exportedAt ?? null,
    key: query.data?.found ? query.data.key : null,
    error: query.isError ? query.error : null,
  }
}
