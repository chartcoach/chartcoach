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
        threadId: "c3666202-50b1-449c-ac0c-9d458e936f92",
        threads: [
          {
            id: "c3666202-50b1-449c-ac0c-9d458e936f92",
            title: "Monthly revenue",
            status: "regular",
          },
          {
            id: "c58db75e-d8ea-44d6-a2e7-7391a34697bd",
            title: "Labels and legends",
            status: "regular",
          },
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
          guidelinesHref: "/guidelines",
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
  expect(html).toContain('href="/"');
  expect(html).toContain('href="/guidelines"');

  const conversation = html.match(
    /<a[^>]*href="\/chat\/c3666202-50b1-449c-ac0c-9d458e936f92"[^>]*>/,
  )?.[0];

  expect(conversation).toBeDefined();
  expect(conversation).toContain(`aria-disabled="${disabled}"`);
  expect(conversation?.includes('tabindex="-1"')).toBe(disabled);
  expect(html).toContain('href="/chat/c58db75e-d8ea-44d6-a2e7-7391a34697bd"');
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
