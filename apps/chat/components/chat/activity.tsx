import { MessagePrimitive, groupPartByType } from "@assistant-ui/react";
import type { EveDynamicToolPart } from "eve/react";
import { ChevronRight } from "lucide-react";
import { useId, useState } from "react";
import type { MessageView } from "../../chat/evidence";
import { ToolActivity, skillActivity } from "./tool-activity";
import { Collapse } from "../ui/collapse";
import * as stylex from "@stylexjs/stylex";
import { colors, media } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";
import { LoadingMark } from "../ui/loading-mark";

const runningLabels = new Map([
  ["search_guidelines", "Searching guidelines"],
  ["read_guidelines", "Reading guidelines and sources"],
  ["describe_catalog", "Inspecting the catalog"],
  ["query_catalog", "Querying the catalog"],
]);

const groupActivity = groupPartByType({ "tool-call": ["group-activity"] });

export function Activity({ view }: { view: MessageView }) {
  const id = useId();
  const [open, setOpen] = useState(false);
  const tools = view.message.parts.filter(
    (part): part is EveDynamicToolPart =>
      part.type === "dynamic-tool" && part.toolName !== "present_answer",
  );
  const presentation = view.message.parts.findLast(
    (part) => part.type === "dynamic-tool" && part.toolName === "present_answer",
  );
  const active = tools.findLast(
    (part) =>
      part.state !== "output-error" &&
      part.state !== "output-denied" &&
      (part.state !== "output-available" || part.partial),
  );
  const running =
    !view.complete && !view.failed && !view.stopped && (!view.answer || view.drafting);
  const label = running
    ? presentation?.type === "dynamic-tool" && presentation.state === "output-error"
      ? "Refining the answer"
      : presentation?.type === "dynamic-tool" &&
          (presentation.state === "input-streaming" || presentation.state === "input-available")
        ? "Writing the answer"
        : active
          ? (skillActivity(active)?.label ?? runningLabels.get(active.toolName) ?? "Working")
          : "Preparing a response"
    : "Activity";
  const byId = new Map(tools.map((part) => [part.toolCallId, part]));
  if (!tools.length) return null;
  return (
    <div {...stylex.props(styles.root)} data-state={open ? "open" : "closed"}>
      <button
        type="button"
        {...stylex.props(ui.button, ui.focus, styles.summary)}
        aria-expanded={open}
        aria-controls={id}
        onClick={() => setOpen((current) => !current)}
      >
        {running ? <LoadingMark /> : null}
        <span>{label}</span>
        <span {...stylex.props(styles.count)}>
          {tools.length} {tools.length === 1 ? "action" : "actions"}
        </span>
        <ChevronRight
          size={14}
          {...stylex.props(ui.chevron, styles.chevron, open && styles.open)}
          aria-hidden="true"
        />
      </button>
      <Collapse id={id} open={open}>
        <div {...stylex.props(styles.body)}>
          <MessagePrimitive.GroupedParts groupBy={groupActivity} indicator="never">
            {({ part, children }) => {
              if (part.type === "group-activity") return children;
              const original = part.type === "tool-call" ? byId.get(part.toolCallId) : undefined;
              return original ? (
                <ToolActivity part={original} stopped={view.stopped} failed={view.failed} />
              ) : null;
            }}
          </MessagePrimitive.GroupedParts>
        </div>
      </Collapse>
    </div>
  );
}

const styles = stylex.create({
  root: { marginTop: 12, marginBottom: 22, marginInline: 0, fontSize: 13 },
  summary: {
    maxWidth: "100%",
    whiteSpace: "normal",
    textAlign: "left",
    display: "inline-flex",
    alignItems: "center",
    gap: 8,
    minHeight: 44,
    paddingBlock: 4,
    paddingInline: 0,
    borderWidth: 0,
    color: {
      default: colors.muted,
      ":hover": { default: null, [media.hover]: colors.accentText },
    },
    backgroundColor: "transparent",
    fontSize: 12,
  },
  count: { fontVariantNumeric: "tabular-nums" },
  chevron: { width: 12, height: 12 },
  open: { transform: "rotate(90deg)" },
  body: {
    marginTop: 8,
    paddingBlock: 8,
    paddingInline: 12,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: colors.border,
    borderRadius: 6,
    backgroundColor: colors.surface,
  },
});
