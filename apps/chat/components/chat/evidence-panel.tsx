import { BookOpen, ChevronDown, X } from "lucide-react";
import { Collapsible, Dialog } from "radix-ui";
import type { Ref } from "react";
import { useEvidencePanel } from "../../chat/use-evidence-panel";
import { useContentScroll } from "../../chat/use-content-scroll";
import type { EvidenceItem } from "../../chat/evidence";
import { EvidenceList } from "./evidence-list";
import { Collapse } from "../ui/collapse";
import * as stylex from "@stylexjs/stylex";
import { ui } from "../ui/ui";
import { styles } from "./evidence-panel.styles";

export function EvidencePanel({
  ref,
  items,
  active = items.length > 0,
  busy = false,
}: {
  ref?: Ref<HTMLElement>;
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

  const desktopScroll = useContentScroll();
  const sheetScroll = useContentScroll();

  if (!active) return null;

  return (
    <aside ref={ref} {...stylex.props(styles.panel)} aria-label="Guideline evidence">
      <Collapsible.Root
        {...stylex.props(styles.desktop)}
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
            <div ref={desktopScroll.viewportRef} {...stylex.props(styles.scroll)}>
              <div>
                <p {...stylex.props(styles.summary)} role="status">
                  {summary}
                </p>
                <EvidenceList groups={groups} busy={busy} />
              </div>
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
            {...stylex.props(styles.sheet)}
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
            <div ref={sheetScroll.viewportRef} {...stylex.props(styles.sheetScroll)}>
              <div>
                <EvidenceList groups={groups} busy={busy} />
              </div>
            </div>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </aside>
  );
}
