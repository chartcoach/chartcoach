import type { GuidelineCardLabel } from "./GuidelineCard";
import { GuidelineLabels } from "./GuidelineLabels";
import type { GuidelineDetailSection } from "./GuidelineSectionCard";

export interface GuidelineDetailViewProps {
  id: string;
  title: string;
  description?: string;
  labels: GuidelineCardLabel[];
  sections: GuidelineDetailSection[];
  bibliographyHtml?: string;
  referencesBib?: string;
}

export function GuidelineDetailView({
  title,
  description,
  labels,
  sections,
  bibliographyHtml,
  referencesBib,
}: GuidelineDetailViewProps) {
  return (
    <div className="guideline-detail-view">
      <div className="guideline-detail-view__intro">
        <h1 className="guideline-detail-view__title">{title}</h1>
        {description ? <p className="guideline-detail-view__description">{description}</p> : null}
      </div>

      {labels.length ? (
        <section
          className="guideline-detail-block guideline-detail-block--labels"
          aria-label="Guideline labels"
        >
          <div className="guideline-detail-block__header">
            <span className="guideline-detail-block__title">labels</span>
          </div>
          <GuidelineLabels labels={labels} className="guideline-detail-view__labels" />
        </section>
      ) : null}

      {sections.length ? (
        <div className="guideline-article">
          {sections.map((section, index) => (
            <section className="guideline-article-section" key={`${section.role}-${index}`}>
              <div className="guideline-article-section__header">
                <p className="guideline-article-section__role">{section.role}</p>
                <h2 className="guideline-article-section__title">{section.title}</h2>
              </div>
              <div
                className="guideline-article-section__body"
                dangerouslySetInnerHTML={{ __html: section.html }}
              />
            </section>
          ))}
        </div>
      ) : null}

      {bibliographyHtml ? (
        <section className="guideline-detail-block guideline-detail-block--references">
          <div className="guideline-detail-block__header">
            <span className="guideline-detail-block__title">references</span>
          </div>
          <div className="bibliography" dangerouslySetInnerHTML={{ __html: bibliographyHtml }} />

          {referencesBib ? (
            <details className="bibtex-details">
              <summary>BibTeX</summary>
              <pre>
                <code>{referencesBib}</code>
              </pre>
            </details>
          ) : null}
        </section>
      ) : null}
    </div>
  );
}
