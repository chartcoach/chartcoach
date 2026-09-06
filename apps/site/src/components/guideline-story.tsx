import { useEffect, useLayoutEffect, useRef, useState } from "react";
import {
  ArtifactFrame,
  DesktopArtifactStack,
  DesktopStoryControl,
  MobileStoryControl,
} from "./guideline-story/story-layout";
import { StoryArtifact } from "./guideline-story/artifacts";
import { steps } from "./guideline-story/story-steps";

const useBrowserLayoutEffect = globalThis.window === undefined ? useEffect : useLayoutEffect;

export function GuidelineStory() {
  const [activeIndex, setActiveIndex] = useState(0);
  const activeIndexRef = useRef(activeIndex);
  const stepRefs = useRef<Array<HTMLDivElement | null>>([]);

  useBrowserLayoutEffect(() => {
    activeIndexRef.current = activeIndex;
  }, [activeIndex]);

  useEffect(() => {
    let frame = 0;

    const update = () => {
      frame = 0;
      const targetY = window.innerHeight * (activeIndexRef.current === 0 ? 0.18 : 0.32);
      let nextIndex = activeIndexRef.current;
      let nextDistance = Number.POSITIVE_INFINITY;

      stepRefs.current.forEach((node, index) => {
        if (!node) return;
        const rect = node.getBoundingClientRect();
        if (rect.bottom < 0 || rect.top > window.innerHeight) return;
        const distance = Math.abs(rect.top - targetY);
        if (distance < nextDistance) {
          nextDistance = distance;
          nextIndex = index;
        }
      });

      setActiveIndex((currentIndex) => (currentIndex === nextIndex ? currentIndex : nextIndex));
    };

    const schedule = () => {
      if (frame) return;
      frame = window.requestAnimationFrame(update);
    };

    window.addEventListener("scroll", schedule, { passive: true });
    window.addEventListener("resize", schedule);

    return () => {
      if (frame) window.cancelAnimationFrame(frame);
      window.removeEventListener("scroll", schedule);
      window.removeEventListener("resize", schedule);
    };
  }, []);

  function selectStep(index: number) {
    setActiveIndex(index);
    stepRefs.current[index]?.scrollIntoView({ block: "center", behavior: "smooth" });
  }

  return (
    <section className="relative z-10 border-t border-border px-0 py-[clamp(5rem,11vh,7rem)]">
      <div className="mx-auto w-[min(100%-3rem,var(--container-content))]">
        <div className="grid min-w-0 grid-cols-[minmax(0,1fr)] gap-x-8 gap-y-12 lg:grid-cols-12 lg:items-start">
          <div className="min-w-0 lg:col-span-6">
            <p className="m-0 font-mono text-[0.75rem] font-semibold uppercase tracking-[0.16em] text-muted">
              Representation
            </p>
            <h2 className="m-0 mt-5 max-w-[43rem] text-balance text-[2.25rem] font-semibold leading-[1.04] tracking-normal text-fg sm:text-[2.9rem] lg:text-[3.45rem] xl:text-[3.85rem]">
              <span className="whitespace-nowrap">Human-readable</span>,{" "}
              <span className="whitespace-nowrap">agent-actionable</span>{" "}
              <span className="whitespace-nowrap">visualization guidelines</span>
            </h2>
          </div>

          <p className="m-0 min-w-0 max-w-[36rem] text-pretty text-[1.0625rem] leading-[1.65] text-muted lg:col-start-7 lg:col-end-13 lg:pt-9 xl:text-[1.1875rem]">
            chartcoach represents each visualization design guideline as a catalog entry that people
            can author and read while agents can query it. The same entry carries sources, roles,
            labels, formats, and contribution paths.
          </p>

          <div className="hidden lg:col-start-1 lg:col-end-7 lg:row-start-2 lg:block lg:pb-64">
            {steps.map((step, index) => (
              <div
                key={step.title}
                ref={(node) => {
                  stepRefs.current[index] = node;
                }}
                data-story-index={index}
                className={["flex flex-col", index === 0 ? "h-[34rem]" : "h-[28rem]"].join(" ")}
              >
                <DesktopStoryControl
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
              <DesktopArtifactStack steps={steps} activeIndex={activeIndex} />
            </div>
          </div>

          <div className="grid min-w-0 grid-cols-[minmax(0,1fr)] gap-10 lg:hidden">
            {steps.map((step, index) => (
              <div key={step.title} className="grid min-w-0 grid-cols-[minmax(0,1fr)] gap-4">
                <MobileStoryControl step={step} index={index} />
                <ArtifactFrame step={step} header="metadata">
                  <StoryArtifact id={step.artifact} active />
                </ArtifactFrame>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
