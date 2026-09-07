import { ArtifactFrame, StoryText } from "./guideline-story/story-layout";
import { StoryArtifact } from "./guideline-story/artifacts";
import { steps } from "./guideline-story/story-steps";

export function GuidelineStory() {
  return (
    <section id="guideline-story" className="guideline-story" aria-labelledby="story-title">
      <div className="mx-auto w-[min(100%-3rem,var(--container-content))]">
        <div className="story-intro">
          <div>
            <p className="m-0 font-mono text-xs font-semibold uppercase tracking-[0.14em] text-muted">
              Representation
            </p>
            <h2 id="story-title" className="story-title">
              <span className="whitespace-nowrap">Human-readable,</span>{" "}
              <span className="whitespace-nowrap">agent-actionable</span> visualization guidelines
            </h2>
          </div>
          <p className="m-0 max-w-[54rem] text-pretty text-base leading-relaxed text-muted sm:text-lg">
            chartcoach represents each visualization design guideline as a catalog entry that people
            can author and read while agents can query it. The same entry carries sources, roles,
            labels, formats, and contribution paths.
          </p>
        </div>
        <div className="story-grid">
          {steps.map((step, index) => (
            <div key={step.artifact} id={`story-${step.artifact}`} className="story-step">
              <div className="story-narrative">
                <StoryText step={step} index={index} />
              </div>
              <div className="story-panel" data-story-artifact={step.artifact}>
                <ArtifactFrame step={step}>
                  <StoryArtifact id={step.artifact} />
                </ArtifactFrame>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
