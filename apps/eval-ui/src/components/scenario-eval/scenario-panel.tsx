import type { ScenarioSpec } from "@chartcoach/eval-ui/eval/schemas";

export function ScenarioPanel({ scenario }: { scenario: ScenarioSpec }) {
  return (
    <section className="min-w-0 px-1 pb-2 pt-1 lg:px-2">
      <div className="space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="text-xs font-semibold text-muted-foreground">Scenario</div>
        </div>

        <div className="grid gap-5 2xl:grid-cols-[420px_minmax(0,1fr)] 2xl:items-start">
          <div className="min-w-0 space-y-4">
            <div className="space-y-2">
              <h1 className="text-balance text-lg font-semibold leading-tight sm:text-xl">
                {scenario.title}
              </h1>
              {scenario.provenance?.source ? (
                <div className="text-xs text-muted-foreground">{scenario.provenance.source}</div>
              ) : null}
              <div className="text-sm text-muted-foreground text-pretty">
                <span className="font-semibold text-foreground">Task:</span> label each retrieved
                guideline with a primary bucket (hard/soft/not useful/N/A) and optionally add
                dimension ratings.
              </div>
            </div>

            <div className="space-y-4">
              <div>
                <div className="text-xs font-semibold text-muted-foreground">Designer intent</div>
                <div className="mt-2 whitespace-pre-wrap text-sm leading-relaxed text-pretty">
                  {scenario.designer_intent ?? "—"}
                </div>
              </div>

              {scenario.audience ||
              scenario.medium ||
              scenario.constraints ||
              scenario.domain ||
              scenario.risk_tolerance ||
              scenario.time_budget ? (
                <div>
                  <div className="text-xs font-semibold text-muted-foreground">Context</div>
                  <dl className="mt-2 grid gap-2 text-sm">
                    {scenario.audience ? (
                      <div className="grid grid-cols-[120px_minmax(0,1fr)] gap-2">
                        <dt className="font-medium text-muted-foreground">Audience</dt>
                        <dd className="min-w-0">{scenario.audience}</dd>
                      </div>
                    ) : null}
                    {scenario.medium ? (
                      <div className="grid grid-cols-[120px_minmax(0,1fr)] gap-2">
                        <dt className="font-medium text-muted-foreground">Medium</dt>
                        <dd className="min-w-0">{scenario.medium}</dd>
                      </div>
                    ) : null}
                    {scenario.constraints ? (
                      <div className="grid grid-cols-[120px_minmax(0,1fr)] gap-2">
                        <dt className="font-medium text-muted-foreground">Constraints</dt>
                        <dd className="min-w-0 whitespace-pre-wrap">{scenario.constraints}</dd>
                      </div>
                    ) : null}
                    {scenario.domain ? (
                      <div className="grid grid-cols-[120px_minmax(0,1fr)] gap-2">
                        <dt className="font-medium text-muted-foreground">Domain</dt>
                        <dd className="min-w-0">{scenario.domain}</dd>
                      </div>
                    ) : null}
                    {scenario.risk_tolerance ? (
                      <div className="grid grid-cols-[120px_minmax(0,1fr)] gap-2">
                        <dt className="font-medium text-muted-foreground">Risk</dt>
                        <dd className="min-w-0">{scenario.risk_tolerance}</dd>
                      </div>
                    ) : null}
                    {scenario.time_budget ? (
                      <div className="grid grid-cols-[120px_minmax(0,1fr)] gap-2">
                        <dt className="font-medium text-muted-foreground">Time</dt>
                        <dd className="min-w-0">{scenario.time_budget}</dd>
                      </div>
                    ) : null}
                  </dl>
                </div>
              ) : null}

              <div>
                <div className="text-xs font-semibold text-muted-foreground">Query</div>
                <div className="mt-2 whitespace-pre-wrap text-sm leading-relaxed text-pretty">
                  {scenario.query ?? "—"}
                </div>
              </div>
            </div>
          </div>

          <div className="min-w-0">
            {scenario.chart?.uri ? (
              <a
                href={scenario.chart.uri}
                target="_blank"
                rel="noopener noreferrer"
                className="block rounded-lg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                title="Open full-size chart image"
              >
                <img
                  src={scenario.chart.uri}
                  alt={`Chart for scenario: ${scenario.title}`}
                  width={1600}
                  height={900}
                  className="mx-auto max-h-[55vh] w-full rounded-lg object-contain"
                  loading="eager"
                  fetchPriority="high"
                  decoding="async"
                />
              </a>
            ) : null}
          </div>
        </div>
      </div>
    </section>
  );
}
