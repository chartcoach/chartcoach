// @vitest-environment jsdom
import { act } from "react";
import { createRoot, type Root } from "react-dom/client";
import {
  AppRouterContext,
  type AppRouterInstance,
} from "next/dist/shared/lib/app-router-context.shared-runtime";
import {
  PathnameContext,
  PathParamsContext,
} from "next/dist/shared/lib/hooks-client-context.shared-runtime";
import { afterEach, beforeEach, expect, it, vi } from "vite-plus/test";
import { useWorkspace } from "../chat/use-workspace";
import { emptyCatalogFilters } from "../shared/catalog-filters";
import { defaultGuidelineLinks } from "../shared/guideline-links";
import type { ThreadDetail } from "../shared/threads";

const firstId = "c3666202-50b1-449c-ac0c-9d458e936f92";

const secondId = "c58db75e-d8ea-44d6-a2e7-7391a34697bd";

const catalogId = "a".repeat(64);

function savedThread(id = firstId): ThreadDetail {
  return {
    id,
    title: "Monthly revenue",
    connectionId: "server",
    sessionId: null,
    createdAt: 1,
    updatedAt: 1,
    archived: false,
    guidelines: {
      filters: emptyCatalogFilters(catalogId),
      selection: { catalogId, sql: "SELECT id FROM catalog_entries" },
      matchedGuidelines: 24,
    },
  };
}

let root: Root;

let workspace: ReturnType<typeof useWorkspace>;

let router: AppRouterInstance;

let threadResponse: ReturnType<typeof Promise.withResolvers<Response>>;

function Workspace() {
  workspace = useWorkspace();

  return workspace.loading ? <p>Loading workspace</p> : <textarea aria-label="Draft" />;
}

function navigate(id?: string) {
  return act(async () =>
    root.render(
      <AppRouterContext value={router}>
        <PathnameContext value={id ? `/chat/${id}` : "/"}>
          <PathParamsContext value={id ? { threadId: id } : {}}>
            <Workspace />
          </PathParamsContext>
        </PathnameContext>
      </AppRouterContext>,
    ),
  );
}

beforeEach(() => {
  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  const container = document.createElement("div");
  document.body.append(container);
  root = createRoot(container);
  router = {
    back: vi.fn(),
    forward: vi.fn(),
    refresh: vi.fn(),
    push: vi.fn(),
    replace: vi.fn(),
    prefetch: vi.fn(),
    bfcacheId: "workspace",
  };
  threadResponse = Promise.withResolvers<Response>();
  vi.stubGlobal("fetch", (input: RequestInfo | URL) => {
    const path = input instanceof Request ? input.url : input.toString();

    if (path === "/eve/v1/preferences")
      return Promise.resolve(
        Response.json({
          connections: [],
          allowedOrigins: [],
          tracing: false,
          guidelines: defaultGuidelineLinks,
        }),
      );

    if (path === "/eve/v1/threads") return Promise.resolve(Response.json([]));

    return threadResponse.promise;
  });
});

afterEach(async () => {
  await act(async () => root.unmount());
  document.body.replaceChildren();
  vi.unstubAllGlobals();
});

it("keeps the initiating composer mounted while a new conversation URL commits", async () => {
  await navigate();
  const input = document.querySelector("textarea")!;
  input.value = "Chart draft";
  const key = workspace.key;
  await act(async () => workspace.adoptThread(savedThread()));
  expect(workspace.loading).toBe(false);
  expect(document.querySelector("textarea")).toBe(input);
  expect(input.value).toBe("Chart draft");
  await navigate(firstId);
  expect(workspace.loading).toBe(false);
  expect(workspace.active?.id).toBe(firstId);
  expect(workspace.key).toBe(key);
  expect(document.querySelector("textarea")).toBe(input);
});

it("keeps the reset composer visible while returning to the new-chat URL", async () => {
  await navigate();
  await act(async () => workspace.adoptThread(savedThread()));
  await navigate(firstId);
  const input = document.querySelector("textarea");
  const key = workspace.key;
  await act(async () => {
    workspace.clearThread();
    workspace.newChat();
  });
  expect(workspace.loading).toBe(false);
  expect(document.querySelector("textarea")).toBe(input);
  await navigate();
  expect(workspace.active).toBeUndefined();
  expect(workspace.key).toBe(key);
  expect(document.querySelector("textarea")).toBe(input);
});

it("still loads a directly opened saved conversation before revealing its composer", async () => {
  await navigate(firstId);
  expect(workspace.loading).toBe(true);
  expect(document.querySelector("textarea")).toBeNull();
  await act(async () => threadResponse.resolve(Response.json(savedThread())));
  expect(workspace.loading).toBe(false);
  expect(workspace.active?.id).toBe(firstId);
  expect(document.querySelector("textarea")).not.toBeNull();
});

it("loads an unrelated destination if navigation interrupts conversation creation", async () => {
  await navigate();
  await act(async () => workspace.adoptThread(savedThread()));
  await navigate(secondId);
  expect(workspace.loading).toBe(true);
  await act(async () => threadResponse.resolve(Response.json(savedThread(secondId))));
  expect(workspace.loading).toBe(false);
  expect(workspace.active?.id).toBe(secondId);
});

it("clears saved conversation state when browser navigation returns to the landing page", async () => {
  await navigate();
  await act(async () => workspace.adoptThread(savedThread()));
  await navigate(firstId);
  const key = workspace.key;
  await navigate();
  expect(workspace.loading).toBe(false);
  expect(workspace.active).toBeUndefined();
  expect(workspace.key).not.toBe(key);
});

it("adopts a quick new message using the route that committed while its save was pending", async () => {
  await navigate();
  await act(async () => workspace.adoptThread(savedThread()));
  await navigate(firstId);
  await act(async () => {
    workspace.clearThread();
    workspace.newChat();
  });
  const adopt = workspace.adoptThread;
  const key = workspace.key;
  await navigate();
  await act(async () => adopt(savedThread(secondId)));
  expect(workspace.loading).toBe(false);
  expect(workspace.active?.id).toBe(secondId);
  expect(workspace.key).toBe(key);
  await navigate(secondId);
  expect(workspace.active?.id).toBe(secondId);
  expect(workspace.key).toBe(key);
});
