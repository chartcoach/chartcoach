import { z } from "zod";

export const workflowSchema = z.enum(["visfeedback", "visrec", "discuss"]);
export const modeSchema = z.enum(["auto", ...workflowSchema.options]);
export type Workflow = z.infer<typeof workflowSchema>;
export type Mode = z.infer<typeof modeSchema>;

export const modes: Record<Mode, { label: string; description: string }> = {
  auto: { label: "Auto", description: "Choose how to help from your question" },
  visfeedback: { label: "Review", description: "Assess an existing chart" },
  visrec: { label: "Recommend", description: "Plan a chart from a brief" },
  discuss: { label: "Discuss", description: "Explore a choice or tradeoff" },
};
