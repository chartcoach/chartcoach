import { Suspense, lazy, useSyncExternalStore } from 'react'

const Devtools = import.meta.env.DEV
  ? lazy(async () => {
      const [
        { TanStackDevtools },
        { TanStackRouterDevtoolsPanel },
        { ReactQueryDevtoolsPanel },
      ] = await Promise.all([
        import('@tanstack/react-devtools'),
        import('@tanstack/react-router-devtools'),
        import('@tanstack/react-query-devtools'),
      ])

      function DevtoolsInner() {
        return (
          <TanStackDevtools
            config={{ position: 'bottom-right' }}
            plugins={[
              {
                name: 'TanStack Router',
                render: <TanStackRouterDevtoolsPanel />,
              },
              {
                name: 'TanStack Query',
                render: <ReactQueryDevtoolsPanel />,
              },
            ]}
          />
        )
      }

      return { default: DevtoolsInner }
    })
  : null

function subscribe(callback: () => void) {
  if (typeof window === 'undefined') return () => {}

  window.addEventListener('resize', callback, { passive: true })
  window.addEventListener('orientationchange', callback, { passive: true })

  return () => {
    window.removeEventListener('resize', callback)
    window.removeEventListener('orientationchange', callback)
  }
}

function getSnapshot() {
  if (typeof window === 'undefined') return true
  return window.innerWidth >= 1024
}

export function TanStackDevtoolsWidget() {
  if (!import.meta.env.DEV || !Devtools) return null

  const show = useSyncExternalStore(subscribe, getSnapshot, () => true)
  if (!show) return null

  return (
    <Suspense fallback={null}>
      <Devtools />
    </Suspense>
  )
}
