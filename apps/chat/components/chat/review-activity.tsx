import {
  ChainOfThoughtByIndicesProvider,
  ChainOfThoughtPrimitive,
  useAuiState,
} from "@assistant-ui/react";
import { ChevronRight } from "lucide-react";
import { useId } from "react";
import type { MessageView } from "../../chat/evidence";
import { ToolActivity } from "./tool-activity";
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

function ActivityDisclosure({ view }: { view: MessageView }) {
  const id = useId();
  const collapsed = useAuiState((state) => state.chainOfThought.collapsed);
  const tools = view.message.parts.filter((part) => part.type === "dynamic-tool");
  const active = tools.findLast(
    (part) =>
      part.state !== "output-error" &&
      part.state !== "output-denied" &&
      (part.state !== "output-available" || part.partial),
  );
  const running = !view.complete && !view.failed && !view.stopped;
  const label = running
    ? active
      ? (runningLabels.get(active.toolName) ?? "Working")
      : "Preparing feedback"
    : "Review activity";
  const byId = new Map(tools.map((part) => [part.toolCallId, part]));
  return (
    <ChainOfThoughtPrimitive.Root
      {...stylex.props(styles.root)}
      data-state={collapsed ? "closed" : "open"}
    >
      <ChainOfThoughtPrimitive.AccordionTrigger
        {...stylex.props(ui.button, ui.focus, styles.summary)}
        aria-expanded={!collapsed}
        aria-controls={id}
      >
        {running ? <LoadingMark /> : null}
        <span>{label}</span>
        <span {...stylex.props(styles.count)}>
          {tools.length} {tools.length === 1 ? "action" : "actions"}
        </span>
        <ChevronRight
          size={14}
          {...stylex.props(ui.chevron, styles.chevron, !collapsed && styles.open)}
          aria-hidden="true"
        />
      </ChainOfThoughtPrimitive.AccordionTrigger>
      <Collapse id={id} open={!collapsed}>
        <div {...stylex.props(styles.body)}>
          <ChainOfThoughtPrimitive.Parts>
            {({ part }) => {
              const original = part.type === "tool-call" ? byId.get(part.toolCallId) : undefined;
              return original ? (
                <ToolActivity part={original} stopped={view.stopped} failed={view.failed} />
              ) : null;
            }}
          </ChainOfThoughtPrimitive.Parts>
        </div>
      </Collapse>
    </ChainOfThoughtPrimitive.Root>
  );
}

const styles = stylex.create({
  root: { marginTop: 12, marginBottom: 22, marginInline: 0, fontSize: 13 },
  summary: {
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

export function ReviewActivity({ view }: { view: MessageView }) {
  const parts = useAuiState((state) => state.message.parts);
  const startIndex = parts.findIndex((part) => part.type === "tool-call");
  const endIndex = parts.findLastIndex((part) => part.type === "tool-call");
  if (startIndex < 0) return null;
  return (
    <ChainOfThoughtByIndicesProvider startIndex={startIndex} endIndex={endIndex}>
      <ActivityDisclosure view={view} />
    </ChainOfThoughtByIndicesProvider>
  );
}
