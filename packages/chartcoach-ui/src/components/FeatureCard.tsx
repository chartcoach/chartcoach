import type { ReactNode } from "react";
import { BookOpen, Quote, Shapes, Tags } from "lucide-react";

const ICONS = {
  book: BookOpen,
  quote: Quote,
  shapes: Shapes,
  tags: Tags,
} as const;

export type FeatureCardIcon = keyof typeof ICONS;

export interface FeatureCardProps {
  href: string;
  title: string;
  description: string;
  icon: FeatureCardIcon;
  inlineCode?: string;
}

export function FeatureCard({ href, title, description, icon, inlineCode }: FeatureCardProps) {
  const Icon = ICONS[icon];
  let descriptionNode: ReactNode = description;
  if (inlineCode) {
    const marker = `{${inlineCode}}`;
    const parts = description.split(marker);
    if (parts.length === 2) {
      descriptionNode = (
        <>
          {parts[0]}
          <code className="cc-feature__link">{inlineCode}</code>
          {parts[1]}
        </>
      );
    }
  }

  return (
    <a className="cc-feature ccui-feature-card" href={href}>
      <span className="cc-feature__icon" aria-hidden="true">
        <Icon size="1.1rem" />
      </span>
      <span className="cc-feature__content">
        <span className="cc-feature__title">{title}</span>
        <span className="cc-feature__desc">{descriptionNode}</span>
      </span>
    </a>
  );
}
