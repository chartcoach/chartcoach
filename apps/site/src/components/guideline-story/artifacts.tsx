import { useState, type CSSProperties, type ReactNode } from "react";
import { Bot, ExternalLink, MessageSquare, Quote, Search } from "lucide-react";
import githubIconUrl from "@/assets/icons/github.svg?url";
import { EXTERNAL_HREFS, externalHrefLabel } from "@/lib/routes";
import {
  jsonLines,
  markdownLines,
  pythonLines,
  shellLines,
  typescriptLines,
} from "./code-examples";
import { CodeWindow, DenseCodeWindow } from "./code-window";
import { EmbeddingCanvas } from "./embedding-canvas";
import { guidelineRoleSections } from "./role-sections";
import type { StoryArtifactId } from "./types";

const githubIconStyle = {
  mask: `url("${githubIconUrl}") center / contain no-repeat`,
  WebkitMask: `url("${githubIconUrl}") center / contain no-repeat`,
} as CSSProperties;

const accessListings = [
  { id: "py", label: "Python", title: "main.py", language: "py", lines: pythonLines },
  { id: "ts", label: "TS", title: "main.ts", language: "ts", lines: typescriptLines },
  { id: "cli", label: "CLI", title: "terminal", language: "sh", lines: shellLines },
] as const;

const skillStages = [
  { icon: Search, label: "retrieve", value: "guideline" },
  { icon: Quote, label: "cite", value: "source" },
  { icon: MessageSquare, label: "answer", value: "advice" },
] as const;

const improveSteps = [
  ["01", "missing guidance", "The chart issue needs a new guideline."],
  [
    "02",
    "propose guideline entry",
    "Draft the issue with source references, context, and proposed labels.",
  ],
  ["03", "community review", "Review the proposed guideline entry in the catalog repository."],
] as const;

export function StoryArtifact({ id, active }: { id: StoryArtifactId; active: boolean }) {
  switch (id) {
    case "markdown":
      return <MarkdownArtifact />;
    case "source":
      return <SourceArtifact />;
    case "structured":
      return <StructuredArtifact />;
    case "embedding":
      return <EmbeddingCanvas active={active} />;
    case "access":
      return <AccessArtifact />;
    case "skills":
      return <SkillsArtifact />;
    case "improve":
      return <ImproveArtifact />;
  }
}

function MarkdownArtifact() {
  return <CodeWindow title="guideline.md" language="markdown" lines={markdownLines} />;
}

function SourceArtifact() {
  return (
    <article className="min-w-0 overflow-hidden">
      <div className="pb-6">
        <h3 className="m-0 text-[1.35rem] font-semibold leading-tight tracking-normal text-fg">
          Use direct labels
        </h3>
        <div className="mt-3 flex flex-wrap gap-2">
          {["chart:bar", "task:compare", "quality:readability"].map((label) => (
            <span
              key={label}
              className="rounded-full border border-border bg-surface-muted px-2.5 py-1 font-mono text-[0.6875rem] text-muted"
            >
              {label}
            </span>
          ))}
        </div>
      </div>

      <div className="grid gap-x-5 gap-y-4 border-y border-border py-5 sm:grid-cols-2">
        {guidelineRoleSections.map((section) => (
          <GuidelineSection key={section.role} role={section.role} title={section.title}>
            {section.text}
          </GuidelineSection>
        ))}
      </div>

      <div className="pt-6">
        <p className="m-0 font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.14em] text-muted">
          references
        </p>
        <p className="m-0 mt-2 text-[0.9375rem] font-semibold leading-snug text-fg">
          Lisa Charlotte Muth
        </p>
        <p className="m-0 mt-1 text-[0.875rem] leading-[1.55] text-muted">
          What to consider when using text in data visualizations. Datawrapper Blog, 2022.
        </p>
      </div>
    </article>
  );
}

function StructuredArtifact() {
  return <DenseCodeWindow title="guideline.json" language="json" lines={jsonLines} wrap />;
}

function AccessArtifact() {
  const [activeListingId, setActiveListingId] = useState<(typeof accessListings)[number]["id"]>(
    accessListings[0].id,
  );
  const activeListing =
    accessListings.find((listing) => listing.id === activeListingId) ?? accessListings[0];

  return (
    <div className="bg-code-bg">
      <div className="sm:hidden">
        <div
          className="grid grid-cols-3 gap-1 border-b border-border bg-bg/68 p-1"
          role="tablist"
          aria-label="Python API, TypeScript API, and CLI examples"
        >
          {accessListings.map((listing) => {
            const selected = activeListing.id === listing.id;
            return (
              <button
                key={listing.id}
                type="button"
                role="tab"
                aria-selected={selected}
                onClick={() => setActiveListingId(listing.id)}
                className={[
                  "min-w-0 rounded-md px-2.5 py-2 font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.1em] transition-colors",
                  selected
                    ? "bg-bg text-fg shadow-[0_1px_2px_color-mix(in_srgb,var(--color-fg)_8%,transparent)]"
                    : "text-muted hover:bg-bg/72 hover:text-fg",
                ].join(" ")}
              >
                {listing.label}
              </button>
            );
          })}
        </div>
        <DenseCodeWindow {...activeListing} />
      </div>
      <div className="hidden sm:block">
        {accessListings.map((listing, index) => (
          <div key={listing.title} className={index === 0 ? undefined : "border-t border-border"}>
            <DenseCodeWindow {...listing} />
          </div>
        ))}
      </div>
    </div>
  );
}

function SkillsArtifact() {
  return (
    <div className="grid gap-5">
      <div className="flex min-w-0 flex-wrap items-center justify-between gap-3">
        <p className="m-0 min-w-0 break-words font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.14em] text-muted">
          chartcoach/skills
        </p>
        <span className="rounded-full border border-border bg-surface-muted px-2.5 py-1 font-mono text-[0.625rem] font-semibold uppercase leading-none tracking-[0.12em] text-muted">
          skill run
        </span>
      </div>

      <div className="rounded-lg bg-surface-muted px-4 py-4 sm:px-5">
        <div className="flex min-w-0 items-center gap-3">
          <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-border bg-bg text-muted">
            <Bot className="h-4 w-4" aria-hidden="true" />
          </span>
          <p className="m-0 min-w-0 break-words font-mono text-[1rem] font-semibold leading-snug text-fg">
            evaluate chart
          </p>
        </div>
      </div>

      <div className="grid gap-3 sm:grid-cols-3">
        {skillStages.map(({ icon: Icon, label, value }, index) => (
          <div
            key={label}
            className={[
              "relative grid min-h-28 gap-4 rounded-lg border border-border bg-bg p-4",
              index < skillStages.length - 1
                ? "sm:after:absolute sm:after:left-full sm:after:top-1/2 sm:after:block sm:after:h-px sm:after:w-3 sm:after:bg-border"
                : "",
            ].join(" ")}
          >
            <div className="flex items-start justify-between gap-3">
              <Icon className="h-4 w-4 text-muted" aria-hidden="true" />
              <span className="font-mono text-[0.625rem] font-semibold uppercase leading-none tracking-[0.12em] text-muted">
                {String(index + 1).padStart(2, "0")}
              </span>
            </div>
            <div>
              <p className="m-0 font-mono text-[0.625rem] font-semibold uppercase tracking-[0.14em] text-muted">
                {label}
              </p>
              <p className="m-0 mt-2 text-[1rem] font-semibold leading-snug text-fg">{value}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function ImproveArtifact() {
  const repositoryLabel = externalHrefLabel(EXTERNAL_HREFS.catalogRepository);
  const repositoryBreakIndex = repositoryLabel.lastIndexOf("/") + 1;
  const repositoryLabelStart = repositoryLabel.slice(0, repositoryBreakIndex);
  const repositoryLabelEnd = repositoryLabel.slice(repositoryBreakIndex);

  return (
    <div className="grid gap-6">
      <a
        href={EXTERNAL_HREFS.catalogRepository}
        className="group grid min-w-0 gap-2 rounded-lg outline-none focus-visible:ring-2 focus-visible:ring-fg/30 focus-visible:ring-offset-4 focus-visible:ring-offset-bg"
        target="_blank"
        rel="noreferrer"
        aria-label="Open the chartcoach catalog repository on GitHub"
      >
        <span className="block font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.14em] text-muted">
          catalog repository
        </span>
        <span className="flex min-w-0 items-start justify-between gap-4">
          <span className="flex min-w-0 items-start gap-3">
            <span
              className="mt-1 block h-4 w-4 shrink-0 bg-current text-fg"
              style={githubIconStyle}
              aria-hidden="true"
            />
            <span className="min-w-0 break-normal font-mono text-[0.9375rem] font-semibold leading-snug text-fg underline decoration-border underline-offset-4 transition-colors group-hover:text-accent group-hover:decoration-accent sm:text-[1rem]">
              {repositoryLabelStart}
              {repositoryLabelEnd ? (
                <>
                  <wbr />
                  {repositoryLabelEnd}
                </>
              ) : null}
            </span>
          </span>
          <ExternalLink
            className="h-4 w-4 shrink-0 text-muted transition-colors group-hover:text-accent"
            aria-hidden="true"
          />
        </span>
      </a>

      <div className="grid gap-4 sm:grid-cols-3">
        {improveSteps.map(([number, label, body]) => (
          <div key={label} className="grid gap-3">
            <span className="font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.14em] text-muted">
              {number}
            </span>
            <h3 className="m-0 text-[1rem] font-semibold leading-snug text-fg">{label}</h3>
            <p className="m-0 break-words text-[0.875rem] leading-[1.55] text-muted">{body}</p>
          </div>
        ))}
      </div>

      <div className="rounded-lg border border-border bg-surface-muted/70 px-4 py-3.5 shadow-[0_1px_0_color-mix(in_srgb,var(--color-fg)_4%,transparent)]">
        <div className="flex min-w-0 flex-col gap-3 sm:flex-row sm:items-start">
          <span
            className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full border-2 border-[#1f883d] text-[#1f883d]"
            aria-hidden="true"
          >
            <span className="h-1.5 w-1.5 rounded-full bg-current" />
          </span>
          <span className="min-w-0 flex-1">
            <span className="block break-words text-[0.9375rem] font-semibold leading-snug text-fg">
              Add guideline for missing chart guidance
            </span>
            <span className="mt-1 block break-words text-[0.75rem] leading-snug text-muted">
              opened in catalog repository
            </span>
          </span>
          <span className="w-fit shrink-0 rounded-full border border-[#1f883d]/45 bg-[#1f883d]/10 px-2 py-0.5 font-mono text-[0.625rem] font-semibold uppercase tracking-[0.1em] text-[#1f883d]">
            review
          </span>
        </div>
      </div>
    </div>
  );
}

function GuidelineSection({
  role,
  title,
  children,
}: {
  role: string;
  title: string;
  children: ReactNode;
}) {
  return (
    <section className="grid min-w-0 gap-2">
      <p className="m-0 font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.14em] text-muted">
        {role}
      </p>
      <div>
        <h4 className="m-0 text-[0.9375rem] font-semibold leading-snug text-fg">{title}</h4>
        <p className="m-0 mt-1 text-[0.875rem] leading-[1.55] text-muted">{children}</p>
      </div>
    </section>
  );
}
