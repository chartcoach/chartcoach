import { useEffect, useMemo, useRef, useState } from 'react'

import type { RelevanceRating } from '@chartcoach/eval-ui/eval/relevance-ratings'
import { getDeviceId } from '@chartcoach/eval-ui/eval/device-id'
import { uploadRelevanceRatingsExport } from '@chartcoach/eval-ui/eval/server/relevance-ratings-sync.server'
import { useOnlineStatus } from '@chartcoach/eval-ui/eval/use-online-status'
import { createRelevanceRatingsExport } from '@chartcoach/eval-ui/lib/export-relevance-ratings'

type SyncStatus = 'idle' | 'queued' | 'syncing' | 'synced' | 'error' | 'disabled'

const LAST_SIGNATURE_STORAGE_KEY =
  'chartcoach/eval-ui/sync/relevance-ratings/v1:last-signature'
const LAST_SUCCESS_AT_STORAGE_KEY =
  'chartcoach/eval-ui/sync/relevance-ratings/v1:last-success-at'
const LAST_SUCCESS_KEY_STORAGE_KEY =
  'chartcoach/eval-ui/sync/relevance-ratings/v1:last-success-key'

function getLocalStorageItem(key: string) {
  if (typeof window === 'undefined') return null
  try {
    return window.localStorage.getItem(key)
  } catch {
    return null
  }
}

function setLocalStorageItem(key: string, value: string) {
  if (typeof window === 'undefined') return
  try {
    window.localStorage.setItem(key, value)
  } catch {
    // ignore quota / privacy errors
  }
}

function makeRatingsSignature(ratings: RelevanceRating[]) {
  const rows = [...ratings]
    .sort((a, b) => a.id.localeCompare(b.id))
    .map((r) => [r.id, r.scenarioId, r.guidelineId, r.relevance, r.createdAt, r.updatedAt])
  return JSON.stringify(rows)
}

export function useAutoUploadRelevanceRatings(ratings: RelevanceRating[]) {
  const isOnline = useOnlineStatus()

  const ratingCount = ratings.length
  const signature = useMemo(() => makeRatingsSignature(ratings), [ratings])

  const ratingsRef = useRef(ratings)
  const signatureRef = useRef(signature)
  useEffect(() => {
    ratingsRef.current = ratings
    signatureRef.current = signature
  }, [ratings, signature])

  const [status, setStatus] = useState<SyncStatus>('idle')
  const [message, setMessage] = useState<string | null>(null)
  const [lastSuccessAt, setLastSuccessAt] = useState<string | null>(() =>
    getLocalStorageItem(LAST_SUCCESS_AT_STORAGE_KEY),
  )
  const [lastSuccessKey, setLastSuccessKey] = useState<string | null>(() =>
    getLocalStorageItem(LAST_SUCCESS_KEY_STORAGE_KEY),
  )

  const uploadTimerIdRef = useRef<number | null>(null)
  const messageTimerIdRef = useRef<number | null>(null)
  const inFlightRef = useRef(false)
  const lastFailureAtRef = useRef<number | null>(null)

  function clearUploadTimer() {
    if (uploadTimerIdRef.current === null) return
    window.clearTimeout(uploadTimerIdRef.current)
    uploadTimerIdRef.current = null
  }

  function clearMessageTimer() {
    if (messageTimerIdRef.current === null) return
    window.clearTimeout(messageTimerIdRef.current)
    messageTimerIdRef.current = null
  }

  function notify(nextMessage: string) {
    setMessage(nextMessage)
    clearMessageTimer()
    messageTimerIdRef.current = window.setTimeout(() => {
      setMessage(null)
      messageTimerIdRef.current = null
    }, 5000)
  }

  async function uploadNow() {
    if (typeof window === 'undefined') return
    if (!isOnline) return
    if (inFlightRef.current) return

    const lastSignature = getLocalStorageItem(LAST_SIGNATURE_STORAGE_KEY)
    const currentSignature = signatureRef.current
    const currentRatings = ratingsRef.current

    if (currentRatings.length === 0) return
    if (lastSignature === currentSignature) return

    const lastFailureAt = lastFailureAtRef.current
    if (lastFailureAt && Date.now() - lastFailureAt < 30_000) {
      return
    }

    inFlightRef.current = true
    setStatus('syncing')

    try {
      const exportPayload = createRelevanceRatingsExport(currentRatings)
      const result = await uploadRelevanceRatingsExport({
        data: {
          deviceId: getDeviceId(),
          export: exportPayload,
        },
      })

      setLocalStorageItem(LAST_SIGNATURE_STORAGE_KEY, currentSignature)
      setLocalStorageItem(LAST_SUCCESS_AT_STORAGE_KEY, new Date().toISOString())
      setLocalStorageItem(LAST_SUCCESS_KEY_STORAGE_KEY, result.key)

      setLastSuccessAt(getLocalStorageItem(LAST_SUCCESS_AT_STORAGE_KEY))
      setLastSuccessKey(result.key)
      lastFailureAtRef.current = null

      setStatus('synced')
      notify('Synced')
    } catch (error) {
      lastFailureAtRef.current = Date.now()

      const message =
        error instanceof Error ? error.message : 'Failed to sync ratings.'

      if (message.toLowerCase().includes('not configured')) {
        setStatus('disabled')
        notify('Sync disabled')
        return
      }

      setStatus('error')
      notify('Sync failed')
    } finally {
      inFlightRef.current = false
    }
  }

  useEffect(() => {
    if (typeof window === 'undefined') return
    return () => {
      clearUploadTimer()
      clearMessageTimer()
    }
  }, [])

  useEffect(() => {
    if (typeof window === 'undefined') return
    if (status === 'disabled') return

    clearUploadTimer()

    if (ratingCount === 0) {
      setStatus('idle')
      return
    }

    const lastSignature = getLocalStorageItem(LAST_SIGNATURE_STORAGE_KEY)
    const needsSync = lastSignature !== signature

    if (!needsSync) {
      if (lastSignature) setStatus('synced')
      return
    }

    if (!isOnline) {
      setStatus('queued')
      return
    }

    setStatus('queued')
    uploadTimerIdRef.current = window.setTimeout(() => {
      void uploadNow()
    }, 2500)
  }, [signature, ratingCount, isOnline, status])

  return {
    status,
    message,
    lastSuccessAt,
    lastSuccessKey,
  }
}

