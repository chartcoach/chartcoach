// @vitest-environment jsdom
import {
  AssistantRuntimeProvider,
  useExternalStoreRuntime,
  type ThreadMessage,
} from "@assistant-ui/react";
import { useRef } from "react";
import { expect, it } from "vite-plus/test";
import { Composer } from "../components/chat/composer";
import { renderDocument } from "./render-document";

function NativeComposer({ running }: { running: boolean }) {
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
