import { z } from "zod";

export const workflowSchema = z.enum(["visfeedback", "visrec", "discuss"]);

export type Workflow = z.infer<typeof workflowSchema>;

export const workflows: Record<Workflow, { label: string; description: string }> = {
  visfeedback: { label: "Review", description: "Assess an existing chart" },
  visrec: { label: "Recommend", description: "Plan a chart from a brief" },
  discuss: { label: "Discuss", description: "Explore a choice or tradeoff" },
};
