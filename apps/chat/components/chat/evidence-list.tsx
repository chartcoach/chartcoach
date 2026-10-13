import { ArrowUpRight, ChevronDown } from "lucide-react";
import { Collapsible } from "radix-ui";
import { useEffect, useMemo, useState } from "react";
import * as stylex from "@stylexjs/stylex";
import type { EvidenceItem } from "../../chat/evidence";
import type { useEvidencePanel } from "../../chat/use-evidence-panel";
import { useListMotion, useListPresence } from "../ui/use-list-motion";
import { Collapse } from "../ui/collapse";
import { motion } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";
import { GuidelineCard } from "../guideline-card";
import { styles } from "./evidence-panel.styles";

const evidenceKey = (item: EvidenceItem) => item.guideline.id;

/** Holds the last items a section showed until it has collapsed. */
function useHeld<T>(items: readonly T[]) {
  const [held, setHeld] = useState(items);
  const emptied = !items.length && held.length > 0;

  if (items.length && items !== held) setHeld(items);

  useEffect(() => {
    if (!emptied) return;

    const timer = setTimeout(() => setHeld([]), parseFloat(motion.move) + 40);

    return () => clearTimeout(timer);
  }, [emptied]);

  return items.length ? items : held;
}

function GuidelineRows({ items }: { items: readonly EvidenceItem[] }) {
  const entries = useListPresence(items, evidenceKey);
  const list = useListMotion<HTMLUListElement>();

  return (
    <ul ref={list} {...stylex.props(styles.rows)}>
      {entries.map(({ key, item: { guideline, stage }, leaving }) => (
        <li
          key={key}
          data-motion-key={key}
          data-motion-leaving={leaving || undefined}
          inert={leaving}
        >
          <a
            {...stylex.props(ui.focus, styles.row)}
            href={guideline.url}
            target="_blank"
            rel="noopener noreferrer"
            aria-label={`Read guideline: ${guideline.title}`}
          >
            <span {...stylex.props(styles.rowHeading)}>
              <span {...stylex.props(styles.rowTitle)}>{guideline.title}</span>
              <ArrowUpRight
                size={14}
                {...stylex.props(ui.icon, styles.rowArrow)}
                aria-hidden="true"
              />
            </span>
            {guideline.description ? (
              <span {...stylex.props(styles.description)}>{guideline.description}</span>
            ) : null}
            <Collapse open={stage === "read"} live>
              <span {...stylex.props(styles.read)}>Read by agent</span>
            </Collapse>
          </a>
        </li>
      ))}
    </ul>
  );
}

function GuidelineCards({ items }: { items: readonly EvidenceItem[] }) {
  const entries = useListPresence(items, evidenceKey);
  const list = useListMotion<HTMLDivElement>();

  return (
    <div ref={list} {...stylex.props(styles.cards)}>
      {entries.map(({ key, item: { guideline }, leaving }) => (
        <div
          key={key}
          data-motion-key={key}
          data-motion-leaving={leaving || undefined}
          inert={leaving}
          {...stylex.props(stylex.defaultMarker())}
        >
          <div {...stylex.props(styles.card)}>
            <GuidelineCard guideline={guideline} />
          </div>
        </div>
      ))}
    </div>
  );
}

function EvidenceGroup({ title, items }: { title: string; items: readonly EvidenceItem[] }) {
  const [open, setOpen] = useState(false);
  const shown = useHeld(items);

  return (
    <Collapse open={items.length > 0} live>
      <Collapsible.Root {...stylex.props(styles.group)} open={open} onOpenChange={setOpen}>
        <Collapsible.Trigger {...stylex.props(ui.button, ui.focus, styles.groupTrigger)}>
          {title} <span {...stylex.props(styles.count)}>{shown.length}</span>
          <ChevronDown
            size={14}
            {...stylex.props(ui.chevron, !open && styles.closedChevron)}
            aria-hidden="true"
          />
        </Collapsible.Trigger>
        <Collapsible.Content forceMount>
          <Collapse open={open}>
            <GuidelineRows items={shown} />
          </Collapse>
        </Collapsible.Content>
      </Collapsible.Root>
    </Collapse>
  );
}

/**
 * Sections stay mounted and collapse when they empty, so the panel reshapes
 * smoothly as search results arrive and the answer promotes its evidence.
 */
export function EvidenceList({
  groups,
  busy,
}: {
  groups: ReturnType<typeof useEvidencePanel>["groups"];
  busy: boolean;
}) {
  const { primary, supporting, candidates } = groups;
  const answered = primary.length > 0;
  const cited = useHeld(primary);
  const found = useHeld(answered ? [] : candidates);
  const [top, more] = useMemo(() => [found.slice(0, 3), found.slice(3)], [found]);

  return (
    <div {...stylex.props(styles.list)}>
      <Collapse open={!groups.total} live>
        <p {...stylex.props(styles.empty)}>
          {busy
            ? "Matches will appear here as the agent explores the catalog."
            : "This conversation has not retrieved any guidelines."}
        </p>
      </Collapse>
      <Collapse open={answered} live>
        <section aria-label="Primary guidelines">
          <h3 {...stylex.props(styles.sectionTitle)}>
            Primary <span {...stylex.props(styles.sectionCount)}>{cited.length}</span>
          </h3>
          <GuidelineCards items={cited} />
        </section>
      </Collapse>
      <EvidenceGroup title="Supporting" items={supporting} />
      <Collapse open={!answered && candidates.length > 0} live>
        <section aria-label="Search results">
          <h3 {...stylex.props(styles.sectionTitle)}>From the catalog</h3>
          <GuidelineRows items={top} />
          <EvidenceGroup title="More results" items={more} />
        </section>
      </Collapse>
      <EvidenceGroup title="Explored" items={answered ? candidates : []} />
    </div>
  );
}
