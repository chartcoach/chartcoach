const DEVICE_ID_STORAGE_KEY = 'chartcoach/eval-ui/device-id/v1'

export function getDeviceId() {
  if (typeof window === 'undefined') return 'server'

  try {
    const existing = window.localStorage.getItem(DEVICE_ID_STORAGE_KEY)
    if (existing) return existing

    const next =
      typeof crypto !== 'undefined' && 'randomUUID' in crypto
        ? crypto.randomUUID()
        : `${Date.now()}-${Math.random().toString(16).slice(2)}`

    window.localStorage.setItem(DEVICE_ID_STORAGE_KEY, next)
    return next
  } catch {
    return 'unknown'
  }
}

