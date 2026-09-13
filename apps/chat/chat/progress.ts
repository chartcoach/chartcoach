import type { MessageView } from "./evidence";

export const progressLabels = {
  preparing: "Starting your conversation",
  starting: "Understanding your request",
  choosing: "Choosing guidance",
  exploring: "Exploring guidelines",
  writing: "Writing your answer",
  refining: "Refining your answer",
  complete: "Activity",
} as const;

export type ProgressPhase = keyof typeof progressLabels;

export function progressPhase(view: MessageView): ProgressPhase {
  if (view.complete || view.failed || view.stopped || (view.answer && !view.drafting))
    return "complete";
  const tools = view.message.parts.filter((part) => part.type === "dynamic-tool");
  const presentation = tools.findLast((part) => part.toolName === "present_answer");

  if (presentation?.state === "output-error") return "refining";

  if (presentation) return "writing";

  if (tools.some((part) => part.toolName !== "load_skill")) return "exploring";

  if (tools.some((part) => part.state === "output-available" && !part.partial)) return "exploring";

  return tools.length ? "choosing" : "starting";
}
