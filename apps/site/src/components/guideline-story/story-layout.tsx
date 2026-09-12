import type { ReactNode } from "react";
import type { StoryStep } from "./types";

export function StoryText({ step, index }: { step: StoryStep; index: number }) {
  return (
    <div className="story-copy">
      <span className="story-number" aria-hidden="true">
        {index + 1}
      </span>
      <div className="min-w-0">
        <p className="m-0 font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.12em] text-muted">
          {step.eyebrow}
        </p>
        <h3
          id={`story-heading-${step.artifact}`}
          className="m-0 mt-2 text-xl font-semibold leading-snug text-fg"
        >
          <a
            href={`#story-${step.artifact}`}
            className="rounded-sm text-inherit no-underline focus-visible:outline-2 focus-visible:outline-offset-4"
          >
            {step.title}
          </a>
        </h3>
      </div>
      <p className="col-start-2 m-0 text-base leading-relaxed text-muted">{step.body}</p>
    </div>
  );
}

export function ArtifactFrame({ step, children }: { step: StoryStep; children: ReactNode }) {
  const flush = ["markdown", "structured", "access", "embedding"].includes(step.artifact);

  return (
    <article className="story-artifact">
      <header className="story-artifact-header">
        <span className="font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.12em] text-muted">
          {step.surface.form}
        </span>
        <span className="font-mono text-xs text-muted">{step.surface.detail}</span>
      </header>
      <div
        className={`story-artifact-body${flush ? "" : " p-5 sm:p-6"}`}
        role="region"
        aria-labelledby={`story-heading-${step.artifact}`}
      >
        {children}
      </div>
    </article>
  );
}
