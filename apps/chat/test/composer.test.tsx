// @vitest-environment jsdom
import {
  AssistantRuntimeProvider,
  useExternalStoreRuntime,
  type ThreadMessage,
} from "@assistant-ui/react";
import { act, useRef, type ReactNode } from "react";
import { createPortal } from "react-dom";
import { createRoot } from "react-dom/client";
import { expect, it, vi } from "vite-plus/test";
import { Composer } from "../components/chat/composer";
import { renderDocument } from "./render-document";

function NativeComposer({
  running,
  tracing = false,
  modelControl,
  keepExpanded,
}: {
  running: boolean;
  tracing?: boolean;
  modelControl?: ReactNode;
  keepExpanded?: boolean;
}) {
  const runtime = useExternalStoreRuntime<ThreadMessage>({
    messages: [],
    isRunning: running,
    onNew: async () => {},
    onCancel: async () => {},
  });

  const input = useRef<HTMLTextAreaElement>(null);

  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <Composer
        onUpload={() => {}}
        messageInput={input}
        busy={running}
        disabled={running}
        reading={false}
        tracing={tracing}
        modelControl={modelControl}
        keepExpanded={keepExpanded}
      />
    </AssistantRuntimeProvider>
  );
}

it("uses the native composer send gate for an empty draft", () => {
  const page = renderDocument(<NativeComposer running={false} />);
  const composer = page.querySelector('[aria-label="Message composer"]')!;
  expect(
    composer.querySelector<HTMLButtonElement>('button[aria-label="Send message"]')?.disabled,
  ).toBe(true);
  const input = composer.querySelector("textarea")!;
  expect(input.disabled).toBe(false);

  const descriptions = input
    .getAttribute("aria-describedby")!
    .split(/\s+/)
    .map((id) => page.getElementById(id)?.textContent);

  expect(descriptions).toEqual([
    expect.stringContaining("PNG"),
    expect.stringContaining("AI provider"),
  ]);
});

it("exposes cancellation while the runtime is running", () => {
  const page = renderDocument(<NativeComposer running />);
  expect(
    page.querySelector<HTMLButtonElement>('button[aria-label="Stop response"]')?.disabled,
  ).toBe(false);
  expect(page.querySelector("textarea")?.disabled).toBe(true);
});

it("names the provider and active tracing beside the composer", () => {
  const traced = renderDocument(<NativeComposer running={false} tracing />);
  const notice = traced.getElementById("message-privacy")!;
  expect(notice.textContent).toBe("Sent to your AI provider · Tracing on");
  expect(
    renderDocument(<NativeComposer running={false} />).getElementById("message-privacy")
      ?.textContent,
  ).toBe("Sent to your AI provider");
});

it("opens the full tracing explanation and restores focus when dismissed", async () => {
  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  const container = document.createElement("div");
  document.body.append(container);
  const root = createRoot(container);

  try {
    await act(async () => root.render(<NativeComposer running={false} tracing />));

    const trigger = Array.from(document.querySelectorAll("button")).find((button) =>
      button.textContent?.includes("Sent to your AI provider"),
    )!;

    trigger.focus();
    await act(async () => trigger.click());
    const details = document.querySelector('[role="dialog"]')!;
    expect(details.textContent).toContain(
      "Conversation tracing is enabled to improve chartcoach and may include messages, images, and responses.",
    );
    const link = details.querySelector<HTMLAnchorElement>("a")!;
    expect(link.textContent).toBe("self-hosting chartcoach with tracing disabled");
    expect(link.href).toBe("https://docs.chartcoach.dev/");
    await act(async () =>
      document
        .querySelector<HTMLButtonElement>('button[aria-label="Close privacy details"]')!
        .click(),
    );
    // Radix restores focus after the popover unmounts.
    await vi.waitFor(() => expect(document.activeElement).toBe(trigger));
  } finally {
    await act(async () => root.unmount());
    container.remove();
    vi.unstubAllGlobals();
  }
});

async function mountComposer(modelControl?: ReactNode) {
  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  const container = document.createElement("div");
  document.body.append(container);
  const root = createRoot(container);
  await act(async () =>
    root.render(<NativeComposer running={false} modelControl={modelControl} />),
  );

  return {
    composer: container.querySelector<HTMLElement>('[aria-label="Message composer"]')!,
    input: container.querySelector("textarea")!,
    unmount: async () => {
      await act(async () => root.unmount());
      container.remove();
      vi.unstubAllGlobals();
    },
  };
}

it("collapses an idle empty composer and expands it for editing or a draft", async () => {
  const { composer, input, unmount } = await mountComposer();

  try {
    expect(composer.dataset.state).toBe("collapsed");
    await act(async () => input.focus());
    expect(composer.dataset.state).toBe("expanded");
    await act(async () => input.blur());
    expect(composer.dataset.state).toBe("collapsed");

    await act(async () => {
      input.focus();
      Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, "value")!.set!.call(
        input,
        "Should the axis start at zero?",
      );
      input.dispatchEvent(new Event("input", { bubbles: true }));
    });
    await act(async () => input.blur());
    expect(composer.dataset.state).toBe("expanded");
  } finally {
    await unmount();
  }
});

it("stays expanded while focus is inside a portaled composer control", async () => {
  // Radix dialogs, such as model settings, render their content outside the composer form.
  const { composer, input, unmount } = await mountComposer(
    createPortal(<button type="button">Choose model</button>, document.body),
  );

  try {
    await act(async () => input.focus());

    const control = Array.from(document.querySelectorAll("button")).find(
      (button) => button.textContent === "Choose model",
    )!;

    await act(async () => control.focus());
    expect(composer.dataset.state).toBe("expanded");
    await act(async () => control.blur());
    expect(composer.dataset.state).toBe("collapsed");
  } finally {
    await unmount();
  }
});

it("keeps the model control row open when the caller requires it", () => {
  const page = renderDocument(<NativeComposer running={false} keepExpanded />);
  expect(page.querySelector<HTMLElement>('[aria-label="Message composer"]')?.dataset.state).toBe(
    "expanded",
  );
});
