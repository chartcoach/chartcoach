import clsx from "clsx";

export interface GuidelineDetailSection {
  role: string;
  title: string;
  html: string;
}

export interface GuidelineSectionCardProps {
  section: GuidelineDetailSection;
  index: number;
}

function formatRole(role: string): string {
  return role.replaceAll(/[-_]+/g, " ");
}

export function GuidelineSectionCard({ section, index }: GuidelineSectionCardProps) {
  const roleClass = `guideline-section-card--${section.role.replaceAll(/[^a-z0-9_-]+/gi, "-").toLowerCase()}`;

  return (
    <article className={clsx("guideline-section-card", roleClass)}>
      <div className="guideline-section-card__row guideline-section-card__row--top">
        <span className="guideline-section-card__key">role</span>
        <span className="guideline-section-card__role">{formatRole(section.role)}</span>
        <span className="guideline-section-card__index">s{index + 1}</span>
      </div>
      <div className="guideline-section-card__row guideline-section-card__row--stack">
        <span className="guideline-section-card__key">heading</span>
        <h2 className="guideline-section-card__title">{section.title}</h2>
      </div>
      <div className="guideline-section-card__row guideline-section-card__row--stack">
        <span className="guideline-section-card__key">content</span>
        <div
          className="guideline-section-card__body"
          dangerouslySetInnerHTML={{ __html: section.html }}
        />
      </div>
    </article>
  );
}
