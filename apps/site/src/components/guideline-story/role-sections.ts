export const guidelineRoleSections = [
  {
    role: "advice",
    title: "Label marks directly",
    text: "Place labels next to compared values.",
  },
  {
    role: "reason",
    title: "Why it works",
    text: "Direct labels reduce legend lookup work.",
  },
  {
    role: "context",
    title: "Where it applies",
    text: "Use this for a small number of bars or series.",
  },
  {
    role: "exceptions",
    title: "When to keep a legend",
    text: "Keep a legend when labels would crowd marks.",
  },
  {
    role: "costs",
    title: "Trade-off",
    text: "Labels use plot space and may need manual placement.",
  },
  {
    role: "mistakes",
    title: "Common mistake",
    text: "Label only the marks readers need to compare in a dense chart.",
  },
  {
    role: "check",
    title: "Check the chart",
    text: "Can each value be read without matching color to a legend?",
  },
  {
    role: "fix",
    title: "Fix",
    text: "Move labels beside marks and remove the legend.",
  },
] as const;

export type GuidelineRole = (typeof guidelineRoleSections)[number]["role"];

export const guidelineRoles = guidelineRoleSections.map((section) => section.role);
