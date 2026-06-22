import { useLayoutEffect, useRef, useState, type ReactNode } from "react";
import { StoryArtifact } from "./artifacts";
import type { StoryStep } from "./types";

const STACK_HEADER_HEIGHT = 64;
const STACK_HEADER_GAP = 0;
const STACK_HEADER_STEP = STACK_HEADER_HEIGHT + STACK_HEADER_GAP;

type ArtifactHeaderMode = "full" | "metadata";

export function DesktopArtifactStack({
  steps,
  activeIndex,
}: {
  steps: readonly StoryStep[];
  activeIndex: number;
}) {
  const [activeHeight, setActiveHeight] = useState(0);
  const activeFrameRef = useRef<HTMLDivElement | null>(null);
  const stackOffset = activeIndex * STACK_HEADER_STEP;

  useLayoutEffect(() => {
    const activeArtifact = activeFrameRef.current;
    if (!activeArtifact) return;

    const updateHeight = () => {
      setActiveHeight(activeArtifact.offsetHeight);
    };

    updateHeight();
    const observer = new ResizeObserver(updateHeight);
    observer.observe(activeArtifact);

    return () => observer.disconnect();
  }, [activeIndex]);

  return (
    <div
      data-story-artifact-frame
      className="relative min-w-0 transition-[height] duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] motion-reduce:transition-none"
      style={{
        height: activeHeight > 0 ? `${activeHeight + stackOffset}px` : undefined,
      }}
    >
      {steps.map((step, index) => {
        const isActive = index === activeIndex;
        const isStacked = index < activeIndex;
        const isUpcoming = index > activeIndex;
        const translateY = isActive
          ? stackOffset
          : isStacked
            ? index * STACK_HEADER_STEP
            : stackOffset + 28;

        return (
          <div
            key={step.title}
            ref={isActive ? activeFrameRef : undefined}
            aria-hidden={!isActive}
            data-story-artifact={index}
            className="absolute left-0 right-0 top-0 min-w-0 origin-top transition-[opacity,transform,filter] duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] motion-reduce:transition-none"
            style={{
              zIndex: isActive ? 30 : 10 + index,
              filter: isUpcoming ? "blur(1px)" : "none",
              opacity: isActive || isStacked ? 1 : 0,
              pointerEvents: isActive ? "auto" : "none",
              transform: `translateY(${translateY}px)`,
            }}
          >
            {isStacked ? (
              <StackedArtifactHeader step={step} first={index === 0} />
            ) : (
              <ArtifactFrame step={step} joinedTop={activeIndex > 0}>
                <StoryArtifact id={step.artifact} active={isActive} />
              </ArtifactFrame>
            )}
          </div>
        );
      })}
    </div>
  );
}

export function DesktopStoryControl({
  step,
  index,
  isActive,
  onSelect,
}: {
  step: StoryStep;
  index: number;
  isActive: boolean;
  onSelect: () => void;
}) {
  return (
    <div
      className={[
        "sticky top-24 flex min-w-0 flex-col gap-4 pb-14 transition-opacity duration-300 motion-reduce:transition-none",
        isActive ? "opacity-100" : "opacity-38",
      ].join(" ")}
    >
      <StoryControlButton
        step={step}
        index={index}
        isActive={isActive}
        onSelect={onSelect}
      />
      <p className="m-0 min-w-0 pl-10 text-[1rem] leading-[1.55] text-muted">{step.body}</p>
    </div>
  );
}

export function MobileStoryControl({
  step,
  index,
}: {
  step: StoryStep;
  index: number;
}) {
  return (
    <div className="flex min-w-0 flex-col gap-4 opacity-100 transition-opacity duration-300 motion-reduce:transition-none">
      <StoryControlLabel step={step} index={index} />
      <p className="m-0 min-w-0 pl-10 text-[1rem] leading-[1.55] text-muted">{step.body}</p>
    </div>
  );
}

export function ArtifactFrame({
  step,
  children,
  joinedTop = false,
  header = "full",
}: {
  step: StoryStep;
  children: ReactNode;
  joinedTop?: boolean;
  header?: ArtifactHeaderMode;
}) {
  const flushArtifact =
    step.artifact === "markdown" || step.artifact === "structured" || step.artifact === "access";

  return (
    <article
      className={[
        "relative min-w-0 overflow-hidden border border-border bg-bg shadow-[0_28px_90px_color-mix(in_srgb,var(--color-fg)_10%,transparent)]",
        joinedTop ? "rounded-b-2xl border-t-0" : "rounded-2xl",
      ].join(" ")}
    >
      <ActiveArtifactHeader step={step} header={header} />
      <div className={["relative min-w-0 bg-bg", flushArtifact ? "p-0" : "p-5 sm:p-6"].join(" ")}>
        {children}
      </div>
    </article>
  );
}

function ActiveArtifactHeader({
  step,
  header,
}: {
  step: StoryStep;
  header: ArtifactHeaderMode;
}) {
  return <StoryArtifactHeader step={step} expanded header={header} />;
}

function StackedArtifactHeader({ step, first }: { step: StoryStep; first: boolean }) {
  return (
    <StoryArtifactHeader
      step={step}
      className={[
        "border-x border-border bg-bg",
        first ? "rounded-t-2xl border-t" : "",
      ].join(" ")}
    />
  );
}

function StoryArtifactHeader({
  step,
  expanded = false,
  header = "full",
  className = "",
}: {
  step: StoryStep;
  expanded?: boolean;
  header?: ArtifactHeaderMode;
  className?: string;
}) {
  const showIntent = header === "full";

  return (
    <div
      data-story-surface-header
      className={[
        "flex min-h-16 min-w-0 items-center gap-4 px-5 py-4 sm:h-16 sm:px-6 sm:py-0",
        showIntent ? "justify-end sm:justify-between" : "justify-end",
        expanded ? "bg-bg" : "border-b border-border bg-surface-muted/45",
        className,
      ].join(" ")}
    >
      {showIntent ? (
        <p className="m-0 hidden min-w-0 text-[1rem] font-semibold leading-snug text-fg sm:block">
          {step.surface.intent}
        </p>
      ) : null}
      <div className="min-w-0 text-right sm:shrink-0">
        <p className="m-0 font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.14em] text-muted">
          {step.surface.form}
        </p>
        <p className="m-0 mt-1 font-mono text-[0.75rem] leading-snug text-muted">
          {step.surface.detail}
        </p>
      </div>
    </div>
  );
}

function StoryControlLabel({
  step,
  index,
}: {
  step: StoryStep;
  index: number;
}) {
  return (
    <div className="flex min-w-0 flex-wrap items-center gap-4 text-left">
      <StoryControlContent step={step} index={index} active />
    </div>
  );
}

function StoryControlButton({
  step,
  index,
  isActive,
  onSelect,
}: {
  step: StoryStep;
  index: number;
  isActive: boolean;
  onSelect: () => void;
}) {
  return (
    <button
      type="button"
      className="group flex min-w-0 cursor-pointer flex-wrap items-center gap-4 bg-transparent p-0 text-left outline-none focus-visible:rounded-md focus-visible:ring-2 focus-visible:ring-fg/30 focus-visible:ring-offset-4 focus-visible:ring-offset-bg"
      onClick={onSelect}
      aria-current={isActive ? "step" : undefined}
    >
      <StoryControlContent step={step} index={index} active={isActive} />
    </button>
  );
}

function StoryControlContent({
  step,
  index,
  active,
}: {
  step: StoryStep;
  index: number;
  active: boolean;
}) {
  return (
    <>
      <span
        className={[
          "flex h-6 w-6 shrink-0 items-center justify-center rounded border font-mono text-[0.75rem] leading-none transition-colors",
          active ? "border-fg text-fg" : "border-muted/50 text-muted",
        ].join(" ")}
        aria-hidden="true"
      >
        {index + 1}
      </span>
      <span className="min-w-0 text-[1rem] font-medium leading-6 text-fg">{step.title}</span>
      <span className="font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.14em] text-muted">
        {step.eyebrow}
      </span>
    </>
  );
}
