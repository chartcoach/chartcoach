import { Suspense, lazy } from 'react'

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

export function TanStackDevtoolsWidget() {
  if (!import.meta.env.DEV || !Devtools) return null

  return (
    <Suspense fallback={null}>
      <Devtools />
    </Suspense>
  )
}
