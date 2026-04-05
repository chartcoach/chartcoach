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

export type GuidelineDetailSection = {
  role: string;
  title: string;
  html: string;
};
