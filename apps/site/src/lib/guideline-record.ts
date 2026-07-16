import type { Guideline } from "@chartcoach/catalog";

export type GuidelineRecord = {
  id: string;
  title: string;
  description: string;
  labels: string[];
  body: string;
  sections: {
    role: string;
    title: string;
    content: string;
  }[];
  references: string[];
};

export function createGuidelineRecord(guideline: Guideline): GuidelineRecord {
  return {
    id: guideline.id,
    title: guideline.title,
    description: guideline.description,
    labels: [...guideline.labels],
    body: guideline.body,
    sections: guideline.sections.map((section) => ({
      role: section.role,
      title: section.title,
      content: section.content,
    })),
    references: [...guideline.references],
  };
}

export function serializeGuidelineRecord(record: GuidelineRecord): string {
  return `${JSON.stringify(record, null, 2)}\n`;
}
