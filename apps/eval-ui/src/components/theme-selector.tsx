import { Moon, Monitor, Sun } from 'lucide-react'
import { useEffect, useMemo, useState } from 'react'

type ThemeMode = 'system' | 'light' | 'dark'

const STORAGE_KEY = 'chartcoach:eval-ui:theme'

function getSystemPrefersDark() {
  if (typeof window === 'undefined') return false
  return window.matchMedia?.('(prefers-color-scheme: dark)')?.matches ?? false
}

function readStoredTheme(): ThemeMode {
  if (typeof window === 'undefined') return 'system'
  const raw = window.localStorage.getItem(STORAGE_KEY)
  if (raw === 'light' || raw === 'dark' || raw === 'system') return raw
  return 'system'
}

function applyTheme(theme: ThemeMode) {
  if (typeof document === 'undefined') return
  const prefersDark = getSystemPrefersDark()
  const isDark = theme === 'dark' || (theme === 'system' && prefersDark)
  document.documentElement.classList.toggle('dark', isDark)
}

export function ThemeSelector() {
  const [theme, setTheme] = useState<ThemeMode>('system')

  useEffect(() => {
    const stored = readStoredTheme()
    setTheme(stored)
    applyTheme(stored)
  }, [])

  useEffect(() => {
    applyTheme(theme)
    window.localStorage.setItem(STORAGE_KEY, theme)
  }, [theme])

  useEffect(() => {
    if (theme !== 'system') return
    const media = window.matchMedia?.('(prefers-color-scheme: dark)')
    if (!media) return
    const onChange = () => applyTheme('system')
    media.addEventListener?.('change', onChange)
    return () => media.removeEventListener?.('change', onChange)
  }, [theme])

  const label = useMemo(() => {
    if (theme === 'system') return getSystemPrefersDark() ? 'Auto (Dark)' : 'Auto (Light)'
    return theme === 'dark' ? 'Dark' : 'Light'
  }, [theme])

  const Icon = theme === 'dark' ? Moon : theme === 'light' ? Sun : Monitor

  return (
    <label className="inline-flex items-center gap-2 text-xs text-muted-foreground">
      <span className="sr-only">Theme</span>
      <div className="relative">
        <span className="pointer-events-none absolute left-2 top-1/2 -translate-y-1/2 text-muted-foreground">
          <Icon className="size-4" aria-hidden="true" />
        </span>
        <select
          className="h-8 rounded-md border bg-background py-0 pl-8 pr-8 text-xs text-foreground"
          aria-label={`Theme (${label})`}
          value={theme}
          onChange={(e) => setTheme(e.currentTarget.value as ThemeMode)}
        >
          <option value="system">Auto</option>
          <option value="light">Light</option>
          <option value="dark">Dark</option>
        </select>
      </div>
    </label>
  )
}
