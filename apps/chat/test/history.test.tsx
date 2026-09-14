import {
  AssistantRuntimeProvider,
  useExternalStoreRuntime,
  type ThreadMessage,
} from "@assistant-ui/react";
import { renderToStaticMarkup } from "react-dom/server";
import { expect, it } from "vite-plus/test";
import { HistoryPanel } from "../components/chat/history";

function Navigation({
  disabled,
  collapsed = false,
  view = "chat",
}: {
  disabled: boolean;
  collapsed?: boolean;
  view?: "chat" | "guidelines";
}) {
  const runtime = useExternalStoreRuntime<ThreadMessage>({
    messages: [],
    onNew: async () => {},
    adapters: {
      threadList: {
        threadId: "revenue",
        threads: [
          { id: "revenue", title: "Monthly revenue", status: "regular" },
          { id: "labels", title: "Labels and legends", status: "regular" },
        ],
        onSwitchToNewThread: async () => {},
        onSwitchToThread: async () => {},
      },
    },
  });

  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <HistoryPanel
        disabled={disabled}
        navigation={{
          desktop: true,
          desktopOpen: !collapsed,
          open: !collapsed,
          setOpen: () => {},
          closeOnSelect: () => {},
          searchInput: { current: null },
          openSearch: () => {},
          searchOpen: true,
          closeSearch: () => {},
          view,
          showGuidelines: () => {},
          showChat: () => {},
        }}
      />
    </AssistantRuntimeProvider>
  );
}

it.each([false, true])("keeps conversations readable with navigation disabled=%s", (disabled) => {
  const html = renderToStaticMarkup(<Navigation disabled={disabled} />);
  expect(html).toContain('aria-label="Conversations"');
  expect(html).toContain('aria-label="Search conversations"');
  expect(html).toContain("New chat");
  expect(html).toContain('aria-label="Guidelines"');
  expect(html).toContain("Monthly revenue");
  expect(html).toContain("Labels and legends");
  const options = html.match(/<button[^>]*aria-label="Options for Monthly revenue"[^>]*>/)?.[0];
  expect(options).toBeDefined();
  expect(options?.includes('disabled=""')).toBe(disabled);
});

it("keeps new chat and search in the collapsed conversation rail", () => {
  const html = renderToStaticMarkup(<Navigation disabled={false} collapsed />);
  expect(html).toContain('aria-label="Conversation shortcuts"');
  expect(html).toContain('aria-label="New chat"');
  expect(html).toContain('aria-label="Search conversations"');
  expect(html).toContain('aria-label="Guidelines"');
});

it.each([false, true])("selects Guidelines alone with collapsed=%s", (collapsed) => {
  const html = renderToStaticMarkup(
    <Navigation disabled={false} collapsed={collapsed} view="guidelines" />,
  );

  expect(html.match(/aria-current=/g)).toHaveLength(1);
  expect(html).toContain('aria-label="Guidelines" aria-current="page"');
});
