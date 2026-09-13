import { MessagePrimitive, groupPartByType } from "@assistant-ui/react";
import type { EveDynamicToolPart } from "eve/react";
import { ChevronRight } from "lucide-react";
import { useId, useState } from "react";
import type { MessageView } from "../../chat/evidence";
import { ToolActivity, toolPresentation } from "./tool-activity";
import { Collapse } from "../ui/collapse";
import * as stylex from "@stylexjs/stylex";
import { colors, media, motion } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";
import { ProgressLabel, ProgressMark } from "./progress";
import { progressLabels, progressPhase } from "../../chat/progress";

const groupActivity = groupPartByType({ "tool-call": ["group-activity"] });

export function Activity({ view }: { view: MessageView }) {
  const id = useId();
  const [open, setOpen] = useState(false);

  const tools = view.message.parts.filter(
    (part): part is EveDynamicToolPart =>
      part.type === "dynamic-tool" && part.toolName !== "present_answer",
  );

  const phase = progressPhase(view);
  const running = phase !== "complete";

  const active = running
    ? tools.findLast(
        (part) =>
          part.state === "input-streaming" ||
          part.state === "input-available" ||
          (part.state === "output-available" && part.partial),
      )
    : undefined;

  const latest = running ? (active ?? tools.at(-1)) : undefined;
  const action = latest ? toolPresentation(latest, view.guidelines) : undefined;
  const ActionIcon = action?.icon;
  const actionText = action ? `${action.label}${action.context ? ` · ${action.context}` : ""}` : "";
  const byId = new Map(tools.map((part) => [part.toolCallId, part]));

  if (!tools.length && !running) return null;

  return (
    <div {...stylex.props(styles.root, ui.appear)} data-state={open ? "open" : "closed"}>
      <button
        type="button"
        {...stylex.props(ui.button, ui.focus, styles.summary, !running && styles.settledSummary)}
        aria-expanded={open}
        aria-controls={id}
        aria-label={`${progressLabels[phase]}${tools.length ? `, ${tools.length} ${tools.length === 1 ? "action" : "actions"}` : ""}${action ? `. ${active ? "Current" : "Latest"}: ${actionText}` : ""}`}
        aria-disabled={!tools.length}
        onClick={() => {
          if (tools.length) setOpen((current) => !current);
        }}
      >
        <ProgressMark running={running} />
        <span role="status" aria-live="polite" aria-atomic="true">
          <ProgressLabel phase={phase} />
        </span>
        <span {...stylex.props(styles.count, !tools.length && styles.pendingControls)}>
          {tools.length} {tools.length === 1 ? "action" : "actions"}
        </span>
        <ChevronRight
          size={14}
          {...stylex.props(
            ui.chevron,
            styles.chevron,
            open && styles.open,
            !tools.length && styles.pendingControls,
          )}
          aria-hidden="true"
        />
        <span {...stylex.props(styles.actionSlot, !running && styles.settled)}>
          {action && ActionIcon ? (
            <span
              key={latest!.toolCallId}
              {...stylex.props(styles.action, ui.appear)}
              title={`${active ? "Current" : "Latest"} action: ${actionText}`}
            >
              <ActionIcon size={13} {...stylex.props(ui.icon)} aria-hidden="true" />
              <span {...stylex.props(styles.actionText)}>{actionText}</span>
            </span>
          ) : null}
        </span>
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
    display: "grid",
    gridTemplateColumns: "24px minmax(0, 1fr) 8ch 12px",
    width: "min(100%, 400px)",
    alignItems: "center",
    alignContent: "center",
    gap: 8,
    transitionProperty: "width, row-gap",
    transitionDuration: { default: motion.disclosure, [media.reducedMotion]: "0ms" },
    transitionTimingFunction: motion.easeOut,
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
  count: { fontVariantNumeric: "tabular-nums", textAlign: "right" },
  settledSummary: { width: "min(100%, 176px)", rowGap: 0 },
  actionSlot: {
    gridColumn: "2 / -1",
    height: 20,
    minWidth: 0,
    overflow: "hidden",
    transitionProperty: "height",
    transitionDuration: { default: motion.disclosure, [media.reducedMotion]: "0ms" },
    transitionTimingFunction: motion.easeOut,
  },
  settled: { height: 0 },
  action: { display: "flex", alignItems: "center", gap: 6, minWidth: 0, lineHeight: "20px" },
  actionText: { overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" },
  pendingControls: { visibility: "hidden" },
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
