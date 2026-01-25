import { Suspense, lazy, useEffect, useState } from 'react'

const AgentationDev = import.meta.env.DEV
  ? lazy(async () => {
      const { Agentation } = await import('agentation')

      function AgentationInner() {
        return <Agentation />
      }

      return { default: AgentationInner }
    })
  : null

export function AgentationWidget() {
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    setMounted(true)
  }, [])

  if (!import.meta.env.DEV || !AgentationDev || !mounted) return null

  return (
    <Suspense fallback={null}>
      <AgentationDev />
    </Suspense>
  )
}

