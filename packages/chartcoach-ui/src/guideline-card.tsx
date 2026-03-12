import type { ReactNode } from "react";

type GuidelineCardLabelLink = {
  text: string;
  href?: string;
  filterValue?: string;
  title?: string;
};

export type GuidelineCardLabel = {
  family?: GuidelineCardLabelLink;
  value: GuidelineCardLabelLink;
};

export type GuidelineCardProps = {
  as?: "li" | "article" | "div";
  className?: string;
  dataLabels?: string;

  title: ReactNode;
  href?: string;
  description?: ReactNode;

  meta?: ReactNode;
  actions?: ReactNode;
  children?: ReactNode;

  labels?: GuidelineCardLabel[];
  labelsRemaining?: number;
  labelsAriaLabel?: string;
};

function renderLabelLink(link: GuidelineCardLabelLink, className: string) {
  if (link.href) {
    return (
      <a
        className={className}
        href={link.href}
        data-filter-value={link.filterValue}
        title={link.title}
      >
        {link.text}
      </a>
    );
  }

  return (
    <span className={className} data-filter-value={link.filterValue} title={link.title}>
      {link.text}
    </span>
  );
}

export function GuidelineCard({
  as = "article",
  className,
  dataLabels,
  title,
  href,
  description,
  meta,
  actions,
  children,
  labels,
  labelsRemaining,
  labelsAriaLabel = "Guideline labels",
}: GuidelineCardProps) {
  const Tag = as;

  const titleNode = href ? (
    <a className="guideline-card__title" href={href}>
      {title}
    </a>
  ) : (
    <div className="guideline-card__title">{title}</div>
  );

  return (
    <Tag
      className={["guideline-card", className].filter(Boolean).join(" ")}
      data-labels={dataLabels}
    >
      <div className="guideline-card__header">
        <div className="guideline-card__content">
          {meta ? <div className="guideline-card__meta">{meta}</div> : null}
          {titleNode}
          {description ? <p className="guideline-card__desc">{description}</p> : null}

          {labels?.length ? (
            <ul className="guideline-labels" aria-label={labelsAriaLabel}>
              {labels.map((label, idx) => (
                <li
                  key={`${label.family?.text ?? "value"}:${label.value.text}:${idx}`}
                  className="guideline-label"
                >
                  {label.family ? (
                    <>
                      {renderLabelLink(label.family, "guideline-label__key")}
                      <span className="guideline-label__sep">:</span>
                      {renderLabelLink(label.value, "guideline-label__value")}
                    </>
                  ) : (
                    renderLabelLink(label.value, "guideline-label__value")
                  )}
                </li>
              ))}
              {labelsRemaining ? (
                <li
                  className="guideline-label guideline-label--more"
                  aria-label={`${labelsRemaining} more labels`}
                >
                  +{labelsRemaining.toLocaleString()}
                </li>
              ) : null}
            </ul>
          ) : null}
        </div>

        {actions ? <div className="guideline-card__actions">{actions}</div> : null}
      </div>

      {children ? <div className="guideline-card__body">{children}</div> : null}
    </Tag>
  );
}
