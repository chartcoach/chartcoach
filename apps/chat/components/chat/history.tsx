import {
  ThreadListPrimitive,
  ThreadListItemPrimitive,
  useAui,
  useAuiState,
} from "@assistant-ui/react";
import { Dialog } from "radix-ui";
import { Archive, History, Pencil, Plus, X } from "lucide-react";
import { useState } from "react";
import * as stylex from "@stylexjs/stylex";
import { colors, media } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

export function HistoryPanel({ disabled }: { disabled: boolean }) {
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");
  const [archived, setArchived] = useState(false);
  const items = useAuiState((state) => state.threads.threadItems);
  const ids = useAuiState((state) =>
    archived ? state.threads.archivedThreadIds : state.threads.threadIds,
  );
  const visibleIds = new Set(ids);
  const hasMatches = items.some(
    (item) =>
      visibleIds.has(item.id) &&
      (item.title ?? "").toLowerCase().includes(search.trim().toLowerCase()),
  );
  return (
    <Dialog.Root open={open} onOpenChange={setOpen}>
      <Dialog.Trigger
        {...stylex.props(ui.button, ui.quietButton, ui.focus)}
        disabled={disabled}
        aria-label="Conversation history"
      >
        <History size={18} />
      </Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay {...stylex.props(styles.overlay)} />
        <Dialog.Content {...stylex.props(styles.panel)}>
          <header {...stylex.props(styles.header)}>
            <div>
              <Dialog.Title {...stylex.props(styles.title)}>Your conversations</Dialog.Title>
              <Dialog.Description {...stylex.props(styles.description)}>
                Revisit a chart or continue a design discussion.
              </Dialog.Description>
            </div>
            <Dialog.Close
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              aria-label="Close history"
            >
              <X size={18} />
            </Dialog.Close>
          </header>
          <ThreadListPrimitive.Root {...stylex.props(styles.body)}>
            <ThreadListPrimitive.New
              {...stylex.props(ui.button, ui.outlineButton, ui.focus, styles.newThread)}
              onClick={() => setOpen(false)}
            >
              <Plus size={16} />
              New conversation
            </ThreadListPrimitive.New>
            <label {...stylex.props(styles.search)}>
              <span {...stylex.props(ui.srOnly)}>Search conversations</span>
              <input
                {...stylex.props(ui.focus, styles.input)}
                type="search"
                placeholder="Search conversations"
                value={search}
                onChange={(event) => setSearch(event.target.value)}
              />
            </label>
            <div {...stylex.props(styles.tabs)}>
              <button
                {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.tab)}
                aria-pressed={!archived}
                onClick={() => setArchived(false)}
              >
                Recent
              </button>
              <button
                {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.tab)}
                aria-pressed={archived}
                onClick={() => setArchived(true)}
              >
                Archived
              </button>
            </div>
            {!hasMatches ? (
              <p {...stylex.props(styles.description)}>
                {search.trim()
                  ? "No conversations match your search."
                  : archived
                    ? "No archived conversations."
                    : "Your conversations will appear here after your first message."}
              </p>
            ) : null}
            <ThreadListPrimitive.Items archived={archived}>
              {() => <HistoryItem search={search} onOpen={() => setOpen(false)} />}
            </ThreadListPrimitive.Items>
          </ThreadListPrimitive.Root>
          <p {...stylex.props(styles.footer)}>
            History is saved on this server and linked to this browser.
          </p>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}

function HistoryItem({ search, onOpen }: { search: string; onOpen: () => void }) {
  const aui = useAui();
  const title = useAuiState((state) => state.threadListItem.title ?? "New conversation");
  const archived = useAuiState((state) => state.threadListItem.status === "archived");
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState(title);
  if (!title.toLowerCase().includes(search.trim().toLowerCase())) return null;
  return (
    <ThreadListItemPrimitive.Root {...stylex.props(styles.item)}>
      {editing ? (
        <form
          onSubmit={(event) => {
            event.preventDefault();
            aui.threadListItem().rename(draft);
            setEditing(false);
          }}
        >
          <input
            {...stylex.props(styles.input, ui.focus)}
            value={draft}
            onChange={(event) => setDraft(event.target.value)}
            aria-label="Conversation title"
            maxLength={160}
            required
          />
          <button {...stylex.props(ui.button, ui.quietButton, ui.focus)}>Save</button>
        </form>
      ) : (
        <>
          <ThreadListItemPrimitive.Trigger
            {...stylex.props(styles.open, ui.focus)}
            onClick={onOpen}
          >
            <ThreadListItemPrimitive.Title />
          </ThreadListItemPrimitive.Trigger>
          <button
            {...stylex.props(ui.button, ui.quietButton, ui.focus)}
            aria-label={`Rename ${title}`}
            onClick={() => setEditing(true)}
          >
            <Pencil size={14} />
          </button>
          {archived ? (
            <ThreadListItemPrimitive.Unarchive
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              aria-label={`Restore ${title}`}
            >
              <Archive size={14} />
            </ThreadListItemPrimitive.Unarchive>
          ) : (
            <ThreadListItemPrimitive.Archive
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              aria-label={`Archive ${title}`}
            >
              <Archive size={14} />
            </ThreadListItemPrimitive.Archive>
          )}
        </>
      )}
    </ThreadListItemPrimitive.Root>
  );
}

const styles = stylex.create({
  overlay: { position: "fixed", inset: 0, zIndex: 40, backgroundColor: "#00000045" },
  panel: {
    position: "fixed",
    top: 0,
    left: 0,
    bottom: 0,
    zIndex: 41,
    width: "min(380px, 100vw)",
    backgroundColor: colors.background,
    color: colors.foreground,
    display: "flex",
    flexDirection: "column",
    outline: "none",
    borderRightWidth: 1,
    borderRightStyle: "solid",
    borderRightColor: colors.border,
  },
  header: { padding: 24, display: "flex", gap: 12, alignItems: "flex-start" },
  title: { fontSize: 20, fontWeight: 550, letterSpacing: "-0.025em", margin: 0 },
  description: {
    fontSize: 13,
    color: colors.muted,
    marginTop: 8,
    marginBottom: 0,
    lineHeight: 1.6,
  },
  body: { paddingInline: 18, flex: 1, minHeight: 0, overflowY: "auto", scrollbarWidth: "thin" },
  newThread: {
    width: "100%",
    color: colors.accentText,
    marginBottom: 18,
  },
  tab: {
    borderBottomWidth: 2,
    borderBottomStyle: "solid",
    borderBottomColor: { default: "transparent", ":is([aria-pressed=true])": colors.accent },
    borderRadius: 0,
  },
  search: { display: "block", marginBottom: 12 },
  input: {
    minHeight: 44,
    width: "100%",
    fontSize: { default: 14, [media.mobile]: 16 },
    color: colors.foreground,
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: colors.border,
    borderRadius: 6,
    padding: 10,
  },
  tabs: { display: "flex", gap: 12, marginBottom: 12 },
  item: {
    display: "flex",
    alignItems: "center",
    borderRadius: 6,
    backgroundColor: { default: "transparent", "[data-active]": colors.surface },
    paddingInline: 4,
    marginBottom: 4,
  },
  open: {
    flex: 1,
    minWidth: 0,
    minHeight: 44,
    padding: 10,
    textAlign: "left",
    fontSize: 13,
    color: colors.foreground,
    borderWidth: 0,
    backgroundColor: "transparent",
    cursor: "pointer",
    overflow: "hidden",
    textOverflow: "ellipsis",
    whiteSpace: "nowrap",
  },
  footer: {
    padding: 24,
    margin: 0,
    color: colors.muted,
    fontSize: 12,
    borderTopWidth: 1,
    borderTopStyle: "solid",
    borderTopColor: colors.border,
  },
});
