import { BookOpen, ChevronDown, X } from "lucide-react";
import { Collapsible, Dialog } from "radix-ui";
import { useEvidencePanel } from "../../chat/use-evidence-panel";
import type { EvidenceItem } from "../../chat/evidence";
import { EvidenceList } from "./evidence-list";
import { Collapse } from "../ui/collapse";
import * as stylex from "@stylexjs/stylex";
import { motionScope } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";
import { styles } from "./evidence-panel.styles";

export function EvidencePanel({
  items,
  active = items.length > 0,
  busy = false,
}: {
  items: readonly EvidenceItem[];
  active?: boolean;
  busy?: boolean;
}) {
  const {
    groups,
    primaryCount,
    summary,
    expanded,
    setExpanded,
    sheetOpen,
    setSheetOpen,
    mobileTrigger,
    desktopTrigger,
    restoreFocus,
  } = useEvidencePanel(items, busy);

  if (!active) return null;

  return (
    <aside {...stylex.props(styles.panel)} aria-label="Guideline evidence">
      <Collapsible.Root
        {...stylex.props(motionScope, styles.desktop)}
        open={expanded}
        onOpenChange={setExpanded}
      >
        <Collapsible.Trigger
          ref={desktopTrigger}
          {...stylex.props(ui.button, ui.focus, styles.header)}
          aria-label="Guidelines for this answer"
        >
          <span>Guidelines</span>
          <span {...stylex.props(styles.count)}>{items.length}</span>
          <ChevronDown
            size={15}
            {...stylex.props(ui.chevron, !expanded && styles.closedChevron)}
            aria-hidden="true"
          />
        </Collapsible.Trigger>
        <Collapsible.Content forceMount>
          <Collapse open={expanded}>
            <div {...stylex.props(styles.scroll)}>
              <p {...stylex.props(styles.summary)} role="status">
                {summary}
              </p>
              <EvidenceList groups={groups} busy={busy} />
            </div>
          </Collapse>
        </Collapsible.Content>
      </Collapsible.Root>

      <Dialog.Root open={sheetOpen} onOpenChange={setSheetOpen}>
        <Dialog.Trigger
          ref={mobileTrigger}
          {...stylex.props(ui.button, ui.focus, styles.mobileTrigger)}
        >
          <BookOpen size={16} {...stylex.props(ui.icon)} aria-hidden="true" />
          <span>Guidelines</span>
          <span {...stylex.props(styles.mobileSummary)}>
            {primaryCount ? `${primaryCount} primary` : `${items.length} found`}
          </span>
          <ChevronDown size={14} {...stylex.props(ui.icon)} aria-hidden="true" />
        </Dialog.Trigger>
        <Dialog.Portal>
          <Dialog.Overlay {...stylex.props(styles.overlay)} />
          <Dialog.Content
            aria-modal="true"
            {...stylex.props(motionScope, styles.sheet)}
            onCloseAutoFocus={restoreFocus}
          >
            <header {...stylex.props(styles.sheetHeader)}>
              <div>
                <Dialog.Title {...stylex.props(styles.sheetTitle)}>Guidelines</Dialog.Title>
                <Dialog.Description {...stylex.props(styles.sheetDescription)}>
                  {summary}
                </Dialog.Description>
              </div>
              <Dialog.Close
                {...stylex.props(ui.button, ui.quietButton, ui.focus)}
                aria-label="Close guidelines"
              >
                <X size={18} aria-hidden="true" />
              </Dialog.Close>
            </header>
            <div {...stylex.props(styles.sheetScroll)}>
              <EvidenceList groups={groups} busy={busy} />
            </div>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </aside>
  );
}
