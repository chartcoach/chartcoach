import {
  GuidelineLabels,
  type GuidelineCardLabel,
  type GuidelineCardLabelLink,
} from "./GuidelineLabels";

export type { GuidelineCardLabel, GuidelineCardLabelLink };

export interface GuidelineCardProps {
  href: string;
  title: string;
  description?: string;
  dataLabels?: string;
  labels: GuidelineCardLabel[];
  labelsRemaining?: number;
}

export function GuidelineCard({
  href,
  title,
  description,
  dataLabels,
  labels,
  labelsRemaining,
}: GuidelineCardProps) {
  return (
    <li className="guideline-card ccui-guideline-card" data-labels={dataLabels}>
      <div className="guideline-card__content">
        <a className="guideline-card__title" href={href}>
          {title}
        </a>
        {description ? <p className="guideline-card__desc">{description}</p> : null}
        {labels.length || labelsRemaining ? (
          <GuidelineLabels
            labels={labels}
            labelsRemaining={labelsRemaining}
            className="guideline-card__labels"
          />
        ) : null}
      </div>
    </li>
  );
}
