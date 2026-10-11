import { ArrowUpRight, ChevronDown } from "lucide-react";
import { Collapsible } from "radix-ui";
import { useState } from "react";
import * as stylex from "@stylexjs/stylex";
import type { EvidenceItem } from "../../chat/evidence";
import type { useEvidencePanel } from "../../chat/use-evidence-panel";
import { Collapse } from "../ui/collapse";
import { ui } from "../ui/ui";
import { GuidelineCard } from "../guideline-card";
import { styles } from "./evidence-panel.styles";

function GuidelineRows({ items }: { items: readonly EvidenceItem[] }) {
  return (
    <ul {...stylex.props(styles.rows)}>
      {items.map(({ guideline, stage }) => (
        <li key={guideline.id}>
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
            {stage === "read" ? <span {...stylex.props(styles.read)}>Read by agent</span> : null}
          </a>
        </li>
      ))}
    </ul>
  );
}

function EvidenceGroup({ title, items }: { title: string; items: readonly EvidenceItem[] }) {
  const [open, setOpen] = useState(false);

  if (!items.length) return null;

  return (
    <Collapsible.Root {...stylex.props(styles.group)} open={open} onOpenChange={setOpen}>
      <Collapsible.Trigger {...stylex.props(ui.button, ui.focus, styles.groupTrigger)}>
        {title} <span {...stylex.props(styles.count)}>{items.length}</span>
        <ChevronDown
          size={14}
          {...stylex.props(ui.chevron, !open && styles.closedChevron)}
          aria-hidden="true"
        />
      </Collapsible.Trigger>
      <Collapsible.Content forceMount>
        <Collapse open={open}>
          <GuidelineRows items={items} />
        </Collapse>
      </Collapsible.Content>
    </Collapsible.Root>
  );
}

export function EvidenceList({
  groups,
  busy,
}: {
  groups: ReturnType<typeof useEvidencePanel>["groups"];
  busy: boolean;
}) {
  const { primary, supporting, candidates } = groups;

  if (!groups.total)
    return (
      <p {...stylex.props(styles.empty)}>
        {busy
          ? "Matches will appear here as the agent explores the catalog."
          : "This conversation has not retrieved any guidelines."}
      </p>
    );

  return (
    <div {...stylex.props(styles.list)}>
      {primary.length ? (
        <section aria-label="Primary guidelines">
          <h3 {...stylex.props(styles.sectionTitle)}>
            Primary <span {...stylex.props(styles.sectionCount)}>{primary.length}</span>
          </h3>
          <div {...stylex.props(styles.cards)}>
            {primary.map(({ guideline }) => (
              <GuidelineCard key={guideline.id} guideline={guideline} />
            ))}
          </div>
        </section>
      ) : null}
      <EvidenceGroup title="Supporting" items={supporting} />
      {!primary.length ? (
        <section aria-label="Search results">
          <h3 {...stylex.props(styles.sectionTitle)}>From the catalog</h3>
          <GuidelineRows items={candidates.slice(0, 3)} />
          <EvidenceGroup title="More results" items={candidates.slice(3)} />
        </section>
      ) : (
        <EvidenceGroup title="Explored" items={candidates} />
      )}
    </div>
  );
}
