import { useEffect, useRef, useState, type ReactNode } from "react";

type GuidelineStoryProps = {
  guidelineCount: number;
};

type StoryStep = {
  eyebrow: string;
  title: string;
  body: string;
  file: string;
  artifact: (guidelineCount: number) => ReactNode;
};

const steps: StoryStep[] = [
  {
    eyebrow: "Markdown",
    title: "Start with a guideline file",
    body: "Frontmatter gives the record an id, title, and labels. Section comments mark roles the loaders can parse.",
    file: "entries/direct-labels/guideline.md",
    artifact: () => <MarkdownArtifact />,
  },
  {
    eyebrow: "Rendered",
    title: "Render it for inspection",
    body: "The same record becomes a human-facing page with labels, sections, citations, and copyable source.",
    file: "guidelines/direct-labels",
    artifact: () => <RenderedArtifact />,
  },
  {
    eyebrow: "Object",
    title: "Read it as a typed object",
    body: "The loaders return a stable `Guideline` shape for JavaScript, Python, search, and site code.",
    file: "Guideline",
    artifact: () => <ObjectArtifact />,
  },
  {
    eyebrow: "Retrieval",
    title: "Retrieve the relevant parts",
    body: "Search returns the record and the section roles that match the chart task.",
    file: "catalog.find",
    artifact: () => <RetrievalArtifact />,
  },
  {
    eyebrow: "Skills",
    title: "Let skills use it automatically",
    body: "Agent workflows load the catalog, choose a task-specific skill, and keep cited guideline sections in the response.",
    file: "skills/",
    artifact: () => <SkillsArtifact />,
  },
  {
    eyebrow: "Catalog",
    title: "Scale the same shape",
    body: "The catalog is many records with one representation, so each surface can index, cite, and inspect the same fields.",
    file: "Catalog",
    artifact: (guidelineCount) => <CatalogArtifact guidelineCount={guidelineCount} />,
  },
];

export function GuidelineStory({ guidelineCount }: GuidelineStoryProps) {
  const [activeIndex, setActiveIndex] = useState(0);
  const stepRefs = useRef<Array<HTMLDivElement | null>>([]);
  const activeStep = steps[activeIndex] ?? steps[0]!;

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => {
            const aDistance = Math.abs(a.boundingClientRect.top - 96);
            const bDistance = Math.abs(b.boundingClientRect.top - 96);
            return aDistance - bDistance;
          })[0];

        if (!visible) return;
        const nextIndex = Number((visible.target as HTMLElement).dataset.storyIndex);
        if (Number.isFinite(nextIndex)) setActiveIndex(nextIndex);
      },
      {
        rootMargin: "-18% 0px -58% 0px",
        threshold: [0, 0.2, 0.45, 0.7],
      },
    );

    stepRefs.current.forEach((node) => {
      if (node) observer.observe(node);
    });

    return () => observer.disconnect();
  }, []);

  function selectStep(index: number) {
    setActiveIndex(index);
    stepRefs.current[index]?.scrollIntoView({ block: "start", behavior: "smooth" });
  }

  return (
    <section className="relative z-10 border-t border-border px-0 py-[clamp(5rem,11vh,7rem)]">
      <div className="mx-auto w-[min(100%-3rem,var(--container-content))]">
        <div className="grid min-w-0 grid-cols-[minmax(0,1fr)] gap-x-8 gap-y-12 lg:grid-cols-12 lg:items-start">
          <div className="min-w-0 lg:col-span-5">
            <p className="m-0 font-mono text-[0.75rem] font-semibold uppercase tracking-[0.16em] text-muted">
              Representation
            </p>
            <h2 className="m-0 mt-5 max-w-[41rem] text-[2.5rem] font-semibold leading-[1.02] tracking-normal text-fg sm:text-[3.25rem] lg:text-[4.25rem] xl:text-[4.75rem]">
              One record, many surfaces
            </h2>
          </div>

          <p className="m-0 min-w-0 max-w-[36rem] text-pretty text-[1.0625rem] leading-[1.65] text-muted lg:col-start-7 lg:col-end-13 lg:pt-9 xl:text-[1.1875rem]">
            ChartCoach keeps one readable record and lets the site, loaders, search index, and
            agent skills use the same source.
          </p>

          <div className="hidden lg:col-start-1 lg:col-end-6 lg:row-start-2 lg:block">
            {steps.map((step, index) => (
              <div
                key={step.title}
                ref={(node) => {
                  stepRefs.current[index] = node;
                }}
                data-story-index={index}
                className="flex h-[26.25rem] flex-col"
              >
                <StoryControl
                  step={step}
                  index={index}
                  isActive={index === activeIndex}
                  onSelect={() => selectStep(index)}
                />
              </div>
            ))}
          </div>

          <div className="hidden lg:col-start-7 lg:col-end-13 lg:row-start-2 lg:block lg:self-stretch">
            <div className="sticky top-24">
              <ArtifactFrame step={activeStep} stepNumber={activeIndex + 1}>
                {activeStep.artifact(guidelineCount)}
              </ArtifactFrame>
            </div>
          </div>

          <div className="grid min-w-0 grid-cols-[minmax(0,1fr)] gap-10 lg:hidden">
            {steps.map((step, index) => (
              <div key={step.title} className="grid min-w-0 grid-cols-[minmax(0,1fr)] gap-4">
                <StoryControl
                  step={step}
                  index={index}
                  isActive
                  onSelect={() => undefined}
                  compact
                />
                <ArtifactFrame step={step} stepNumber={index + 1}>
                  {step.artifact(guidelineCount)}
                </ArtifactFrame>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

function StoryControl({
  step,
  index,
  isActive,
  onSelect,
  compact = false,
}: {
  step: StoryStep;
  index: number;
  isActive: boolean;
  onSelect: () => void;
  compact?: boolean;
}) {
  return (
    <div
      className={[
        compact ? "flex min-w-0 flex-col gap-4" : "sticky top-24 flex min-w-0 flex-col gap-4 pb-14",
        "transition-opacity duration-300 motion-reduce:transition-none",
        isActive ? "opacity-100" : "opacity-40",
      ].join(" ")}
    >
      <button
        type="button"
        className="group flex min-w-0 cursor-pointer flex-wrap items-center gap-4 bg-transparent p-0 text-left outline-none focus-visible:rounded-md focus-visible:ring-2 focus-visible:ring-fg/30 focus-visible:ring-offset-4 focus-visible:ring-offset-bg"
        onClick={onSelect}
        aria-current={isActive ? "step" : undefined}
      >
        <span
          className={[
            "flex h-6 w-6 shrink-0 items-center justify-center rounded border font-mono text-[0.75rem] leading-none",
            isActive ? "border-fg text-fg" : "border-muted/50 text-muted",
          ].join(" ")}
          aria-hidden="true"
        >
          {index + 1}
        </span>
        <span className="text-[1rem] leading-6 text-fg">{step.title}</span>
        <span className="rounded-full bg-surface-muted px-3 py-1 font-mono text-[0.6875rem] font-medium text-muted">
          {step.eyebrow.toLowerCase()}
        </span>
      </button>
      <p className="m-0 min-w-0 pl-10 text-[1rem] leading-[1.55] text-muted">{step.body}</p>
    </div>
  );
}

function ArtifactFrame({
  step,
  stepNumber,
  children,
}: {
  step: StoryStep;
  stepNumber: number;
  children: ReactNode;
}) {
  return (
    <div className="relative min-w-0 rounded-xl bg-bg p-3 shadow-[inset_0_0_0_1px_var(--color-border),0_24px_80px_color-mix(in_srgb,var(--color-fg)_8%,transparent)]">
      <div className="flex flex-col gap-1">
        <div className="px-3 py-2 font-mono text-[0.8125rem] font-semibold text-fg">
          catalog/
        </div>
        <div className="flex w-full min-w-0 items-center justify-between gap-3 rounded-md bg-surface-muted px-3 py-2.5 text-left">
          <span className="min-w-0 truncate font-mono text-[0.8125rem] text-fg">{step.file}</span>
          <span className="shrink-0 font-mono text-[0.6875rem] uppercase tracking-[0.16em] text-muted">
            {String(stepNumber).padStart(2, "0")} {step.eyebrow}
          </span>
        </div>
      </div>
      <div className="mt-4">{children}</div>
    </div>
  );
}

function CodePanel({ children }: { children: ReactNode }) {
  return (
    <pre
      className="m-0 min-w-0 max-w-full whitespace-pre-wrap break-words rounded-lg border border-border bg-code-bg p-5 font-mono text-[0.8125rem] leading-6 text-code-fg"
      style={{ overflow: "visible" }}
    >
      <code>{children}</code>
    </pre>
  );
}

function Line({ children = "\u00a0" }: { children?: ReactNode }) {
  return (
    <>
      {children}
      {"\n"}
    </>
  );
}

function T({
  kind,
  children,
}: {
  kind: "comment" | "key" | "string" | "keyword" | "fn" | "plain" | "number";
  children: ReactNode;
}) {
  const classes = {
    comment: "text-muted",
    key: "text-[#0550ae] dark:text-[#79c0ff]",
    string: "text-[#0a3069] dark:text-[#a5d6ff]",
    keyword: "text-[#cf222e] dark:text-[#ff7b72]",
    fn: "text-[#8250df] dark:text-[#d2a8ff]",
    plain: "text-code-fg",
    number: "text-[#116329] dark:text-[#7ee787]",
  } satisfies Record<typeof kind, string>;

  return <span className={classes[kind]}>{children}</span>;
}

function MarkdownArtifact() {
  return (
    <CodePanel>
      <Line>
        <T kind="comment">---</T>
      </Line>
      <Line>
        <T kind="key">id</T>: <T kind="string">direct-labels</T>
      </Line>
      <Line>
        <T kind="key">title</T>: <T kind="string">Use direct labels</T>
      </Line>
      <Line>
        <T kind="key">labels</T>:
      </Line>
      <Line>
        {"  "}- <T kind="string">chart:bar</T>
      </Line>
      <Line>
        {"  "}- <T kind="string">task:compare</T>
      </Line>
      <Line>
        {"  "}- <T kind="string">quality:readability</T>
      </Line>
      <Line>
        <T kind="comment">---</T>
      </Line>
      <Line />
      <Line>
        <T kind="plain">## Label marks directly </T>
        <T kind="comment">{"<!-- role: advice -->"}</T>
      </Line>
      <Line />
      <Line>Place labels next to compared values.</Line>
      <Line />
      <Line>
        <T kind="plain">## Check the chart </T>
        <T kind="comment">{"<!-- role: check -->"}</T>
      </Line>
      <Line />
      <Line>Can each value be read without a legend?</Line>
    </CodePanel>
  );
}

function RenderedArtifact() {
  const sections = [
    {
      role: "advice",
      title: "Label marks directly",
      body: "Place labels next to compared values when the chart has only a few categories.",
    },
    {
      role: "check",
      title: "Check the chart",
      body: "Can each value be read without matching color to a legend?",
    },
  ];

  return (
    <article className="rounded-lg border border-border bg-bg p-5">
      <div className="flex flex-wrap gap-2">
        {["chart:bar", "task:compare", "quality:readability"].map((label) => (
          <span
            key={label}
            className="rounded-full border border-border bg-surface-muted px-2.5 py-1 font-mono text-[0.6875rem] text-muted"
          >
            {label}
          </span>
        ))}
      </div>
      <h3 className="m-0 mt-5 text-[1.625rem] font-semibold leading-tight tracking-normal text-fg">
        Use direct labels
      </h3>
      <p className="m-0 mt-2 text-[0.9375rem] leading-[1.6] text-muted">
        Label marks directly when space permits.
      </p>
      <div className="mt-5 grid gap-3">
        {sections.map((section) => (
          <section key={section.role} className="rounded-md border border-border bg-surface-muted p-4">
            <div className="flex items-center gap-2">
              <span className="rounded border border-border bg-bg px-2 py-0.5 font-mono text-[0.6875rem] uppercase tracking-[0.12em] text-muted">
                {section.role}
              </span>
              <h4 className="m-0 text-[0.9375rem] font-semibold leading-snug text-fg">
                {section.title}
              </h4>
            </div>
            <p className="m-0 mt-3 text-[0.875rem] leading-[1.55] text-muted">{section.body}</p>
          </section>
        ))}
      </div>
    </article>
  );
}

function ObjectArtifact() {
  return (
    <CodePanel>
      <Line>{"{"}</Line>
      <Line>
        {"  "}
        <T kind="key">"id"</T>: <T kind="string">"direct-labels"</T>,
      </Line>
      <Line>
        {"  "}
        <T kind="key">"title"</T>: <T kind="string">"Use direct labels"</T>,
      </Line>
      <Line>
        {"  "}
        <T kind="key">"labels"</T>: [<T kind="string">"chart:bar"</T>, <T kind="string">"task:compare"</T>],
      </Line>
      <Line>
        {"  "}
        <T kind="key">"sections"</T>: [
      </Line>
      <Line>
        {"    "}{"{"} <T kind="key">"role"</T>: <T kind="string">"advice"</T>, <T kind="key">"content"</T>: <T kind="string">"Place labels..."</T> {"}"},
      </Line>
      <Line>
        {"    "}{"{"} <T kind="key">"role"</T>: <T kind="string">"check"</T>, <T kind="key">"content"</T>: <T kind="string">"Can each value..."</T> {"}"}
      </Line>
      <Line>
        {"  "}]
      </Line>
      <Line>{"}"}</Line>
    </CodePanel>
  );
}

function RetrievalArtifact() {
  return (
    <CodePanel>
      <Line>
        <T kind="comment">$</T> <T kind="fn">chartcoach</T> catalog find <T kind="string">"bar chart legend lookup"</T>
      </Line>
      <Line />
      <Line>
        <T kind="comment">1.</T> <T kind="string">direct-labels</T> <T kind="comment">score 0.91</T>
      </Line>
      <Line>
        {"   "}
        <T kind="key">roles</T>: <T kind="string">advice</T>, <T kind="string">reason</T>, <T kind="string">check</T>
      </Line>
      <Line />
      <Line>
        <T kind="keyword">Answer</T>
      </Line>
      <Line>Label each bar at its value when space permits.</Line>
      <Line>
        <T kind="comment">Source: direct-labels, advice</T>
      </Line>
    </CodePanel>
  );
}

function SkillsArtifact() {
  const skills = [
    {
      name: "VisFeedback",
      body: "Critique a chart and cite the guideline sections behind each issue.",
    },
    {
      name: "VisRec",
      body: "Recommend chart types and encodings from task, data, and audience constraints.",
    },
    {
      name: "Discuss",
      body: "Answer visualization design questions before a chart exists.",
    },
    {
      name: "Contribute",
      body: "Draft a catalog issue when a missing guideline appears during work.",
    },
  ];

  return (
    <div className="rounded-lg border border-border bg-bg p-4">
      <div className="grid gap-2 sm:grid-cols-2">
        {skills.map((skill) => (
          <article key={skill.name} className="rounded-md border border-border bg-surface-muted p-4">
            <div className="flex items-center justify-between gap-3">
              <h3 className="m-0 text-[0.9375rem] font-semibold leading-snug text-fg">
                {skill.name}
              </h3>
              <span className="rounded border border-border bg-bg px-2 py-0.5 font-mono text-[0.625rem] uppercase tracking-[0.12em] text-muted">
                skill
              </span>
            </div>
            <p className="m-0 mt-3 text-[0.8125rem] leading-[1.55] text-muted">{skill.body}</p>
          </article>
        ))}
      </div>
      <div className="mt-4">
        <CodePanel>
        <Line>
          <T kind="fn">ChartCoach</T> skill
        </Line>
        <Line>
          {"  "}loads <T kind="string">catalog/</T>
        </Line>
        <Line>
          {"  "}selects <T kind="string">workflow skill</T>
        </Line>
        <Line>
          {"  "}returns <T kind="string">cited sections</T>
        </Line>
        </CodePanel>
      </div>
    </div>
  );
}

function CatalogArtifact({ guidelineCount }: { guidelineCount: number }) {
  return (
    <div className="grid gap-4">
      <div className="grid grid-cols-3 overflow-hidden rounded-lg border border-border text-center">
        <Metric label="records" value={guidelineCount.toLocaleString()} />
        <Metric label="fields" value="7" />
        <Metric label="shape" value="1" />
      </div>
      <CodePanel>
        <Line>
          <T kind="keyword">import</T> {"{ "}
          <T kind="fn">Catalog</T>
          {" }"} <T kind="keyword">from</T> <T kind="string">"@chartcoach/catalog"</T>
        </Line>
        <Line />
        <Line>
          <T kind="keyword">const</T> catalog = <T kind="keyword">new</T> <T kind="fn">Catalog</T>(records)
        </Line>
        <Line>catalog.require(<T kind="string">"direct-labels"</T>).sections</Line>
        <Line>catalog.labels()</Line>
      </CodePanel>
    </div>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <div className="border-r border-border bg-surface-muted p-4 last:border-r-0">
      <p className="m-0 text-[1.5rem] font-semibold leading-none text-fg">{value}</p>
      <p className="m-0 mt-2 font-mono text-[0.6875rem] uppercase tracking-[0.14em] text-muted">
        {label}
      </p>
    </div>
  );
}
