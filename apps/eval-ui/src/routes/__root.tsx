import {
  HeadContent,
  Scripts,
  createRootRouteWithContext,
} from '@tanstack/react-router'

import { TanStackDevtoolsWidget } from '@chartcoach/eval-ui/integrations/tanstack-devtools'
import { AgentationWidget } from '@chartcoach/eval-ui/integrations/agentation'
import { ServiceWorkerRegistration } from '@chartcoach/eval-ui/components/service-worker'

import appCss from '../styles.css?url'

import type { QueryClient } from '@tanstack/react-query'

interface MyRouterContext {
  queryClient: QueryClient
}

export const Route = createRootRouteWithContext<MyRouterContext>()({
  head: () => ({
    meta: [
      {
        charSet: 'utf-8',
      },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1',
      },
      {
        name: 'color-scheme',
        content: 'light dark',
      },
      {
        name: 'theme-color',
        content: '#0f172a',
      },
      {
        name: 'description',
        content:
          'ChartCoach eval UI for human relevance ratings of retrieved visualization guidelines.',
      },
      {
        name: 'robots',
        content: 'noindex, nofollow',
      },
      {
        title: 'ChartCoach · Guideline Relevance Eval',
      },
    ],
    links: [
      {
        rel: 'stylesheet',
        href: appCss,
      },
      { rel: 'icon', href: '/favicon.ico' },
      { rel: 'apple-touch-icon', href: '/logo192.png' },
      { rel: 'manifest', href: '/manifest.json' },
    ],
  }),

  shellComponent: RootDocument,
})

function RootDocument({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <HeadContent />
        <script
          dangerouslySetInnerHTML={{
            __html: `(function(){try{var key='chartcoach:eval-ui:theme';var pref=localStorage.getItem(key)||'system';var m=window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)');var dark=pref==='dark'||(pref==='system'&&m&&m.matches);document.documentElement.classList.toggle('dark',!!dark);}catch(e){}})();`,
          }}
        />
      </head>
      <body>
        <a
          href="#main"
          onClick={() => {
            document.getElementById('main')?.focus()
          }}
          className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-50 focus:rounded-md focus:bg-background focus:px-3 focus:py-2 focus:text-sm focus:shadow focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
        >
          Skip to main content
        </a>
        <ServiceWorkerRegistration />
        {children}
        <AgentationWidget />
        <TanStackDevtoolsWidget />
        <Scripts />
      </body>
    </html>
  )
}
