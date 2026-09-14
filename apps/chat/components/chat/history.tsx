import {
  ThreadListPrimitive,
  ThreadListItemPrimitive,
  ThreadListItemMorePrimitive,
  useAui,
  useAuiState,
} from "@assistant-ui/react";
import { Dialog } from "radix-ui";
import {
  Archive,
  ArrowLeft,
  BookOpen,
  MoreHorizontal,
  Pencil,
  Search,
  SquarePen,
  X,
} from "lucide-react";
import { useEffect, useRef, useState, type RefObject, type ReactNode } from "react";
import * as stylex from "@stylexjs/stylex";
import type { useNavigation } from "../../chat/use-navigation";
import { styles } from "./history.styles";
import { historyRowScope } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

export function HistoryPanel({
  navigation,
  disabled,
  guidelineCount,
}: {
  navigation: ReturnType<typeof useNavigation>;
  disabled: boolean;
  guidelineCount?: number;
}) {
  return (
    <>
      <aside
        id="conversation-sidebar"
        aria-label="Conversations"
        aria-hidden={!navigation.desktop}
        inert={!navigation.desktop}
        {...stylex.props(styles.dock, !navigation.desktopOpen && styles.collapsed)}
      >
        <div {...stylex.props(styles.inner, !navigation.desktopOpen && styles.innerClosed)}>
          {navigation.desktop && navigation.desktopOpen ? (
            <HistoryList
              disabled={disabled}
              onOpen={navigation.closeOnSelect}
              searchInput={navigation.searchInput}
              searchVisible={navigation.searchOpen}
              onSearchClose={navigation.closeSearch}
              chatActive={navigation.view === "chat"}
              guidelines={<GuidelinesLink navigation={navigation} count={guidelineCount} />}
            />
          ) : navigation.desktop ? (
            <nav {...stylex.props(styles.rail)} aria-label="Conversation shortcuts">
              <ThreadListPrimitive.New
                {...stylex.props(ui.button, ui.quietButton, ui.focus)}
                disabled={disabled}
                aria-label="New chat"
                title="New chat"
                onClick={navigation.closeOnSelect}
              >
                <SquarePen size={18} />
              </ThreadListPrimitive.New>
              <button
                {...stylex.props(ui.button, ui.quietButton, ui.focus)}
                type="button"
                onClick={navigation.openSearch}
                aria-label="Search conversations"
                title="Search conversations"
              >
                <Search size={18} />
              </button>
              <GuidelinesLink navigation={navigation} count={guidelineCount} compact />
            </nav>
          ) : null}
        </div>
      </aside>
      <Dialog.Root open={!navigation.desktop && navigation.open} onOpenChange={navigation.setOpen}>
        <Dialog.Portal>
          <Dialog.Overlay {...stylex.props(styles.overlay)} />
          <Dialog.Content
            id="conversation-drawer"
            {...stylex.props(styles.drawer)}
            onCloseAutoFocus={(event) => {
              event.preventDefault();
              document
                .querySelector<HTMLButtonElement>('[aria-controls="conversation-drawer"]')
                ?.focus();
            }}
          >
            <header {...stylex.props(styles.drawerHeader)}>
              <Dialog.Title {...stylex.props(styles.title)}>Your conversations</Dialog.Title>
              <Dialog.Description {...stylex.props(ui.srOnly)}>
                Find a previous conversation or start a new chat.
              </Dialog.Description>
              <Dialog.Close
                {...stylex.props(ui.button, ui.quietButton, ui.focus)}
                aria-label="Close sidebar"
              >
                <X size={18} />
              </Dialog.Close>
            </header>
            <HistoryList
              disabled={disabled}
              onOpen={navigation.closeOnSelect}
              searchInput={navigation.searchInput}
              searchVisible
              chatActive={navigation.view === "chat"}
              guidelines={<GuidelinesLink navigation={navigation} count={guidelineCount} />}
            />
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </>
  );
}

function GuidelinesLink({
  navigation,
  count,
  compact = false,
}: {
  navigation: ReturnType<typeof useNavigation>;
  count?: number;
  compact?: boolean;
}) {
  return (
    <button
      type="button"
      {...stylex.props(
        ui.button,
        ui.quietButton,
        ui.focus,
        styles.guidelines,
        navigation.view === "guidelines" && styles.guidelinesActive,
        compact && styles.guidelinesCompact,
      )}
      onClick={navigation.showGuidelines}
      aria-label="Guidelines"
      aria-current={navigation.view === "guidelines" ? "page" : undefined}
      title={compact ? "Guidelines" : undefined}
    >
      <BookOpen size={18} aria-hidden="true" />
      {!compact ? (
        <>
          Guidelines
          {count !== undefined ? (
            <span {...stylex.props(styles.guidelineCount)}>{count.toLocaleString()}</span>
          ) : null}
        </>
      ) : null}
    </button>
  );
}

function HistoryList({
  disabled,
  onOpen,
  searchInput,
  searchVisible,
  onSearchClose,
  chatActive,
  guidelines,
}: {
  disabled: boolean;
  onOpen: () => void;
  searchInput: RefObject<HTMLInputElement | null>;
  searchVisible: boolean;
  onSearchClose?: () => void;
  chatActive: boolean;
  guidelines: ReactNode;
}) {
  const [search, setSearch] = useState("");
  const [archived, setArchived] = useState(false);
  const items = useAuiState((state) => state.threads.threadItems);
  const loading = useAuiState((state) => state.threads.isLoading);

  const ids = useAuiState((state) =>
    archived ? state.threads.archivedThreadIds : state.threads.threadIds,
  );

  const visibleIds = new Set(ids);
  const query = search.trim().toLowerCase();

  const hasMatches = items.some(
    (item) => visibleIds.has(item.id) && (item.title ?? "").toLowerCase().includes(query),
  );

  return (
    <ThreadListPrimitive.Root {...stylex.props(styles.list)}>
      <div {...stylex.props(styles.controls)}>
        <NewChatButton disabled={disabled} selected={chatActive} onOpen={onOpen} />
        {guidelines}
        {searchVisible ? (
          <label {...stylex.props(styles.search)}>
            <Search size={15} aria-hidden="true" {...stylex.props(styles.searchIcon)} />
            <input
              ref={searchInput}
              type="search"
              name="conversation-search"
              autoComplete="off"
              aria-label="Search conversations"
              placeholder="Search chats"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              onKeyDown={(event) => {
                if (event.key === "Escape" && onSearchClose) {
                  event.preventDefault();
                  setSearch("");
                  onSearchClose();
                  document
                    .querySelector<HTMLButtonElement>('button[aria-label="Search conversations"]')
                    ?.focus();
                }
              }}
              {...stylex.props(ui.focus, styles.input, styles.searchInput)}
            />
          </label>
        ) : null}
        <div {...stylex.props(styles.section)}>
          <h2 {...stylex.props(styles.sectionTitle)}>
            {archived ? "Archived chats" : "Your chats"}
          </h2>
          <button
            type="button"
            {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.archiveToggle)}
            onClick={() => setArchived(!archived)}
            aria-label={archived ? "Back to chats" : "Show archived chats"}
            title={archived ? "Back to chats" : "Archived chats"}
          >
            {archived ? <ArrowLeft size={15} /> : <Archive size={15} />}
          </button>
        </div>
      </div>
      <div {...stylex.props(styles.scroll)}>
        {loading ? (
          <p {...stylex.props(styles.empty)} role="status">
            Loading conversations…
          </p>
        ) : !hasMatches ? (
          <p {...stylex.props(styles.empty)}>
            {query
              ? "No chats match your search."
              : archived
                ? "No archived chats."
                : "Your conversations will appear here after your first message."}
          </p>
        ) : null}
        <ThreadListPrimitive.Items archived={archived}>
          {() => (
            <HistoryItem
              query={query}
              disabled={disabled}
              chatActive={chatActive}
              onOpen={onOpen}
            />
          )}
        </ThreadListPrimitive.Items>
      </div>
    </ThreadListPrimitive.Root>
  );
}

function NewChatButton({
  disabled,
  selected,
  onOpen,
}: {
  disabled: boolean;
  selected: boolean;
  onOpen: () => void;
}) {
  const active = useAuiState((state) => state.threads.newThreadId === state.threads.mainThreadId);

  return (
    <ThreadListPrimitive.New
      {...stylex.props(ui.button, ui.focus, styles.newThread)}
      disabled={disabled}
      data-active={selected && active ? "true" : undefined}
      aria-current={selected && active ? "page" : undefined}
      onClick={onOpen}
    >
      <SquarePen size={17} aria-hidden="true" /> New chat
    </ThreadListPrimitive.New>
  );
}

function HistoryItem({
  query,
  disabled,
  chatActive,
  onOpen,
}: {
  query: string;
  disabled: boolean;
  chatActive: boolean;
  onOpen: () => void;
}) {
  const title = useAuiState((state) => state.threadListItem.title ?? "New chat");
  const archived = useAuiState((state) => state.threadListItem.status === "archived");
  const active = useAuiState((state) => state.threads.mainThreadId === state.threadListItem.id);
  const [editing, setEditing] = useState(false);

  if (!title.toLowerCase().includes(query)) return null;

  return (
    <ThreadListItemPrimitive.Root
      {...stylex.props(styles.item, historyRowScope)}
      data-active={chatActive && active ? "true" : undefined}
      aria-current={chatActive && active ? "page" : undefined}
    >
      {editing ? (
        <RenameConversation title={title} onDone={() => setEditing(false)} />
      ) : (
        <>
          <ThreadListItemPrimitive.Trigger
            {...stylex.props(styles.open, ui.focus)}
            disabled={disabled}
            onClick={onOpen}
            title={title}
          >
            <ThreadListItemPrimitive.Title />
          </ThreadListItemPrimitive.Trigger>
          <ThreadListItemMorePrimitive.Root sharedFocusGroup>
            <ThreadListItemMorePrimitive.Trigger
              {...stylex.props(ui.button, ui.focus, styles.more)}
              disabled={disabled}
              aria-label={`Options for ${title}`}
            >
              <MoreHorizontal size={16} />
            </ThreadListItemMorePrimitive.Trigger>
            <ThreadListItemMorePrimitive.Content
              {...stylex.props(styles.menu)}
              side="bottom"
              align="end"
              sideOffset={4}
            >
              <ThreadListItemMorePrimitive.Item
                {...stylex.props(styles.menuItem)}
                onSelect={() => setEditing(true)}
              >
                <Pencil size={15} />
                Rename
              </ThreadListItemMorePrimitive.Item>
              {archived ? (
                <ThreadListItemPrimitive.Unarchive asChild>
                  <ThreadListItemMorePrimitive.Item {...stylex.props(styles.menuItem)}>
                    <Archive size={15} />
                    Restore
                  </ThreadListItemMorePrimitive.Item>
                </ThreadListItemPrimitive.Unarchive>
              ) : (
                <ThreadListItemPrimitive.Archive asChild>
                  <ThreadListItemMorePrimitive.Item {...stylex.props(styles.menuItem)}>
                    <Archive size={15} />
                    Archive
                  </ThreadListItemMorePrimitive.Item>
                </ThreadListItemPrimitive.Archive>
              )}
            </ThreadListItemMorePrimitive.Content>
          </ThreadListItemMorePrimitive.Root>
        </>
      )}
    </ThreadListItemPrimitive.Root>
  );
}

function RenameConversation({ title, onDone }: { title: string; onDone: () => void }) {
  const aui = useAui();
  const [draft, setDraft] = useState(title);
  const input = useRef<HTMLInputElement>(null);
  useEffect(() => input.current?.select(), []);

  return (
    <form
      {...stylex.props(styles.rename)}
      onSubmit={(event) => {
        event.preventDefault();

        if (draft.trim()) {
          aui.threadListItem().rename(draft.trim());
          onDone();
        }
      }}
    >
      <input
        ref={input}
        {...stylex.props(styles.input, ui.focus)}
        value={draft}
        onChange={(event) => setDraft(event.target.value)}
        onKeyDown={(event) => {
          if (event.key === "Escape") {
            event.stopPropagation();
            onDone();
          }
        }}
        aria-label="Conversation title"
        name="title"
        autoComplete="off"
        maxLength={160}
        required
      />
      <button {...stylex.props(ui.button, ui.quietButton, ui.focus)} type="submit">
        Save
      </button>
    </form>
  );
}
