import clsx from "clsx";
import type { ReactNode } from "react";

export type GuidelineCardLabelLink = {
  text: string;
  href?: string;
  filterValue?: string;
  title?: string;
};

export type GuidelineCardLabel = {
  family?: GuidelineCardLabelLink;
  value: GuidelineCardLabelLink;
};

export interface GuidelineLabelsProps {
  labels: GuidelineCardLabel[];
  labelsRemaining?: number;
  ariaLabel?: string;
  className?: string;
  variant?: "chip" | "record";
}

function renderLink(link: GuidelineCardLabelLink, className: string): ReactNode {
  const commonProps = {
    className,
    "data-filter-value": link.filterValue,
    title: link.title,
  };

  return link.href ? (
    <a {...commonProps} href={link.href}>
      {link.text}
    </a>
  ) : (
    <span {...commonProps}>{link.text}</span>
  );
}

export function GuidelineLabels({
  labels,
  labelsRemaining,
  ariaLabel = "Guideline labels",
  className,
  variant = "chip",
}: GuidelineLabelsProps) {
  if (!labels.length && !labelsRemaining) return null;

  if (variant === "record") {
    return (
      <ul className={clsx("guideline-record-fields", className)} aria-label={ariaLabel}>
        {labels.map((label, index) => (
          <li
            className="guideline-record-field"
            key={`${label.family?.text ?? "value"}-${label.value.text}-${index}`}
          >
            <span className="guideline-record-field__key">
              {label.family
                ? renderLink(label.family, "guideline-record-field__key-link")
                : "label"}
            </span>
            <span className="guideline-record-field__value">
              {renderLink(label.value, "guideline-record-field__value-link")}
            </span>
          </li>
        ))}
        {labelsRemaining ? (
          <li
            className="guideline-record-field guideline-record-field--more"
            aria-label={`${labelsRemaining} more labels`}
          >
            <span className="guideline-record-field__key">more</span>
            <span className="guideline-record-field__value">
              +{labelsRemaining.toLocaleString()}
            </span>
          </li>
        ) : null}
      </ul>
    );
  }

  return (
    <ul
      className={clsx("guideline-labels", "ccui-guideline-labels", className)}
      aria-label={ariaLabel}
    >
      {labels.map((label, index) => (
        <li
          className="guideline-label ccui-guideline-label"
          key={`${label.family?.text ?? "value"}-${label.value.text}-${index}`}
        >
          {label.family ? (
            <>
              {renderLink(label.family, "guideline-label__key")}
              <span className="guideline-label__sep">:</span>
              {renderLink(label.value, "guideline-label__value")}
            </>
          ) : (
            renderLink(label.value, "guideline-label__value")
          )}
        </li>
      ))}
      {labelsRemaining ? (
        <li
          className="guideline-label guideline-label--more ccui-guideline-label ccui-guideline-label--more"
          aria-label={`${labelsRemaining} more labels`}
        >
          +{labelsRemaining.toLocaleString()}
        </li>
      ) : null}
    </ul>
  );
}
