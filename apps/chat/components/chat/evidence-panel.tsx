import { ChevronDown } from "lucide-react";
import { Accordion, Collapsible } from "radix-ui";
import { useId, useRef, useState } from "react";
import type { EvidenceItem } from "../../chat/evidence";
import { GuidelineCard } from "./guideline-card";
import { Collapse } from "../ui/collapse";
import * as stylex from "@stylexjs/stylex";
import { colors, media, motionScope } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

const styles = stylex.create({
  panel: {
    display: { default: "block", [media.desktop]: "flex" },
    flexDirection: "column",
    gridRow: 1,
    gridColumn: { default: "auto", [media.desktop]: 2 },
    minWidth: 0,
    minHeight: 0,
    borderBottomWidth: { default: 1, [media.desktop]: 0 },
    borderBottomStyle: "solid",
    borderBottomColor: colors.border,
    borderLeftWidth: { default: 0, [media.desktop]: 1 },
    borderLeftStyle: "solid",
    borderLeftColor: colors.border,
    backgroundColor: colors.background,
    position: { default: "relative", [media.desktop]: "static" },
  },
  emptyPanel: { display: { default: null, [media.narrow]: "none" } },
  header: {
    display: { default: "flex", [media.desktop]: "block" },
    alignItems: "center",
    gap: 12,
    paddingInline: { default: 18, [media.desktop]: 28 },
    paddingTop: { default: 0, [media.desktop]: 28 },
    paddingBottom: 0,
  },
  title: {
    display: { default: "none", [media.desktop]: "flex" },
    alignItems: "center",
    gap: 8,
    margin: 0,
    fontSize: 15,
    fontWeight: 600,
    letterSpacing: "-0.02em",
  },
  overview: {
    display: { default: "none", [media.desktop]: "block" },
    marginTop: 6,
    marginBottom: 0,
    marginInline: 0,
    fontSize: 12,
    color: colors.muted,
  },
  toggle: {
    display: { default: "flex", [media.desktop]: "none" },
    alignItems: "center",
    gap: 12,
    width: "100%",
    minHeight: 48,
    paddingBlock: 8,
    paddingInline: 0,
    borderWidth: 0,
    backgroundColor: "transparent",
    color: colors.foreground,
    fontSize: 13,
    textAlign: "left",
  },
  primaryToggle: { width: "auto", marginLeft: "auto", gap: 8 },
  mobilePrimaryTitle: {
    display: { default: "block", [media.desktop]: "none" },
    margin: 0,
    fontSize: 12,
    fontWeight: 500,
    color: colors.muted,
  },
  progress: {
    marginLeft: "auto",
    fontSize: 12,
    color: colors.muted,
    fontVariantNumeric: "tabular-nums",
  },
  muted: { fontSize: 12, color: colors.muted },
  count: { marginLeft: 6, fontVariantNumeric: "tabular-nums", color: colors.muted },
  content: {
    display: "block",
    paddingTop: 0,
    paddingInline: { default: 18, [media.desktop]: 28 },
    paddingBottom: { default: 16, [media.desktop]: 28 },
    overflowY: { default: "auto", [media.desktop]: "visible" },
    overflowX: "hidden",
    maxHeight: {
      default: "min(42dvh, max(0px, calc(100dvh - 460px)))",
      [media.shortNarrow]: "calc(100dvh - 124px)",
      [media.desktop]: "none",
    },
    scrollbarWidth: "thin",
    scrollbarColor: `${colors.scrollThumb} transparent`,
    overscrollBehaviorY: "contain",
    position: { default: "absolute", [media.desktop]: "static" },
    top: { default: "100%", [media.desktop]: "auto" },
    left: { default: 0, [media.desktop]: "auto" },
    right: { default: 0, [media.desktop]: "auto" },
    zIndex: { default: 5, [media.desktop]: "auto" },
    backgroundColor: { default: colors.surface, [media.desktop]: "transparent" },
    borderBottomWidth: { default: 1, [media.desktop]: 0 },
    borderBottomStyle: "solid",
    borderBottomColor: colors.border,
    boxShadow: { default: "0 8px 16px #00000012", [media.desktop]: "none" },
  },
  body: {
    minHeight: 0,
    minWidth: 0,
    flex: { default: null, [media.desktop]: 1 },
    overflowY: { default: "visible", [media.desktop]: "auto" },
    scrollbarWidth: "thin",
    scrollbarColor: `${colors.scrollThumb} transparent`,
    overscrollBehaviorY: "contain",
  },
  primaryTitle: {
    display: { default: "none", [media.desktop]: "block" },
    marginTop: { default: 0, [media.desktop]: 22 },
    marginBottom: 8,
    marginInline: { default: 18, [media.desktop]: 28 },
    fontSize: 12,
    fontWeight: 500,
    color: colors.muted,
  },
  primaryCards: {
    display: "grid",
    gridAutoFlow: { default: "column", [media.desktop]: "row" },
    gridAutoColumns: {
      default: 200,
      "@media (max-width: 719px) and (max-height: 700px)": 160,
      [media.desktop]: "auto",
    },
    gridTemplateColumns: { default: "none", [media.desktop]: "minmax(0, 1fr)" },
    gap: 12,
    paddingInline: { default: 18, [media.desktop]: 28 },
    paddingBottom: { default: 12, [media.desktop]: 0 },
    overflowX: { default: "auto", [media.desktop]: "visible" },
    scrollbarWidth: "thin",
    scrollbarColor: `${colors.scrollThumb} transparent`,
    overscrollBehaviorX: "contain",
  },
  contentClosed: { display: { default: "none", [media.desktop]: "block" } },
  empty: { fontSize: 13, color: colors.muted, marginBlock: 20, marginInline: 0 },
  sectionTitle: {
    marginTop: 22,
    marginBottom: 8,
    marginInline: 0,
    fontSize: 12,
    fontWeight: 500,
    color: colors.muted,
  },
  rowSeparated: { borderTopWidth: 1, borderTopStyle: "solid", borderTopColor: colors.border },
  rowHeader: { margin: 0 },
  trigger: {
    display: "flex",
    alignItems: "center",
    gap: 12,
    width: "100%",
    minHeight: 48,
    borderWidth: 0,
    backgroundColor: "transparent",
    textAlign: "left",
    color: {
      default: colors.foreground,
      ":hover": { default: null, [media.hover]: colors.accentText },
    },
    paddingBlock: 14,
    paddingInline: 0,
    fontSize: 14,
    fontWeight: 450,
    lineHeight: 1.5,
  },
  rowTitle: { flex: 1, overflowWrap: "anywhere" },
  chevron: { marginLeft: "auto", color: colors.muted },
  chevronOpen: { transform: "rotate(180deg)" },
  preview: { paddingTop: 2, paddingBottom: 16, paddingInline: 0 },
  group: {
    marginTop: 18,
    borderTopWidth: 1,
    borderTopStyle: "solid",
    borderTopColor: colors.border,
  },
  groupTrigger: {
    paddingTop: 14,
    paddingBottom: 8,
    fontSize: 12,
    fontWeight: 400,
    color: { default: colors.muted, ":hover": { default: null, [media.hover]: colors.accentText } },
  },
});

function GuidelineRow({
  item: { guideline, stage },
  selected,
  separated,
}: {
  item: EvidenceItem;
  selected: string;
  separated: boolean;
}) {
  const [visited, setVisited] = useState(false);
  return (
    <Accordion.Item {...stylex.props(separated && styles.rowSeparated)} value={guideline.id}>
      <Accordion.Header {...stylex.props(styles.rowHeader)}>
        <Accordion.Trigger
          {...stylex.props(ui.button, ui.focus, styles.trigger)}
          aria-label={`Preview ${guideline.title}`}
          onClick={() => setVisited(true)}
        >
          <span {...stylex.props(styles.rowTitle)}>{guideline.title}</span>
          {stage === "read" ? <span {...stylex.props(styles.muted)}>Read</span> : null}
          <ChevronDown
            {...stylex.props(
              ui.chevron,
              styles.chevron,
              selected === guideline.id && styles.chevronOpen,
            )}
            size={14}
            aria-hidden="true"
          />
        </Accordion.Trigger>
      </Accordion.Header>
      <Accordion.Content forceMount aria-hidden={selected !== guideline.id}>
        <Collapse open={selected === guideline.id}>
          <div {...stylex.props(styles.preview)}>
            {visited ? <GuidelineCard guideline={guideline} /> : null}
          </div>
        </Collapse>
      </Accordion.Content>
    </Accordion.Item>
  );
}

function GuidelineRows({ items, selected }: { items: readonly EvidenceItem[]; selected: string }) {
  return items.map((item, index) => (
    <GuidelineRow key={item.guideline.id} item={item} selected={selected} separated={index > 0} />
  ));
}

function EvidenceGroup({
  title,
  items,
  selected,
}: {
  title: string;
  items: readonly EvidenceItem[];
  selected: string;
}) {
  const [open, setOpen] = useState(false);
  if (!items.length) return null;
  return (
    <Collapsible.Root {...stylex.props(styles.group)} open={open} onOpenChange={setOpen}>
      <Collapsible.Trigger
        {...stylex.props(ui.button, ui.focus, styles.trigger, styles.groupTrigger)}
      >
        {title} <span {...stylex.props(styles.count)}>{items.length}</span>
        <ChevronDown
          {...stylex.props(ui.chevron, styles.chevron, open && styles.chevronOpen)}
          size={14}
          aria-hidden="true"
        />
      </Collapsible.Trigger>
      <Collapsible.Content forceMount>
        <Collapse open={open}>
          <GuidelineRows items={items} selected={selected} />
        </Collapse>
      </Collapsible.Content>
    </Collapsible.Root>
  );
}

export function EvidencePanel({
  items,
  active = items.length > 0,
  busy = false,
}: {
  items: readonly EvidenceItem[];
  active?: boolean;
  busy?: boolean;
}) {
  const [open, setOpen] = useState(false);
  const [selected, setSelected] = useState("");
  const toggle = useRef<HTMLButtonElement>(null);
  const id = useId();
  if (!active) return null;
  const primary = items.filter((item) => item.stage === "primary");
  const supporting = items.filter((item) => item.stage === "supporting");
  const candidates = [
    ...items.filter((item) => item.stage === "read"),
    ...items.filter((item) => item.stage === "matched"),
  ];
  const readCount = items.filter((item) => item.stage !== "matched").length;
  const progress = primary.length
    ? `${primary.length} primary`
    : `${items.length} found · ${readCount} read`;
  return (
    <aside
      {...stylex.props(motionScope, styles.panel, !items.length && styles.emptyPanel)}
      aria-label="Guideline evidence"
      data-open={open}
      data-empty={!items.length}
      onKeyDown={(event) => {
        if (event.key === "Escape" && open) {
          event.preventDefault();
          setOpen(false);
          toggle.current?.focus();
        }
      }}
    >
      <header {...stylex.props(styles.header)}>
        <h2 {...stylex.props(styles.title)}>Guidelines</h2>
        <p {...stylex.props(styles.overview)}>
          {busy ? progress : primary.length ? "Used in this answer" : "From this search"}
        </p>
        {primary.length ? (
          <h2 {...stylex.props(styles.mobilePrimaryTitle)}>
            Primary <span {...stylex.props(styles.count)}>{primary.length}</span>
          </h2>
        ) : null}
        <button
          {...stylex.props(
            ui.button,
            ui.focus,
            styles.toggle,
            primary.length > 0 && styles.primaryToggle,
          )}
          ref={toggle}
          type="button"
          aria-expanded={open}
          aria-controls={id}
          aria-label={primary.length ? "More guidelines" : undefined}
          onClick={() => setOpen(!open)}
        >
          {primary.length ? "More" : "Guidelines"}
          <span {...stylex.props(styles.progress)}>
            {primary.length ? supporting.length + candidates.length : progress}
          </span>
          <ChevronDown
            {...stylex.props(ui.chevron, open && styles.chevronOpen)}
            size={16}
            aria-hidden="true"
          />
        </button>
      </header>
      <div {...stylex.props(styles.body)}>
        {primary.length ? (
          <section aria-label="Primary guidelines">
            <h3 {...stylex.props(styles.primaryTitle)}>
              Primary <span {...stylex.props(styles.count)}>{primary.length}</span>
            </h3>
            <div {...stylex.props(styles.primaryCards)}>
              {primary.map(({ guideline }) => (
                <GuidelineCard key={guideline.id} guideline={guideline} compact />
              ))}
            </div>
          </section>
        ) : null}
        <div {...stylex.props(styles.content, !open && styles.contentClosed)} id={id}>
          {!items.length ? (
            <p {...stylex.props(styles.empty)}>
              {busy ? "Searching the catalog…" : "No guidelines retrieved."}
            </p>
          ) : null}
          <Accordion.Root type="single" collapsible value={selected} onValueChange={setSelected}>
            <EvidenceGroup title="Supporting" items={supporting} selected={selected} />
            {busy && !primary.length ? (
              <section aria-label="Search results">
                <h3 {...stylex.props(styles.sectionTitle)}>Search results</h3>
                <GuidelineRows items={candidates.slice(0, 3)} selected={selected} />
                <EvidenceGroup
                  title="More results"
                  items={candidates.slice(3)}
                  selected={selected}
                />
              </section>
            ) : (
              <EvidenceGroup title="Explored" items={candidates} selected={selected} />
            )}
          </Accordion.Root>
        </div>
      </div>
    </aside>
  );
}
