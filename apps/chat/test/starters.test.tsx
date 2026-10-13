// @vitest-environment jsdom
import {
  AssistantRuntimeProvider,
  useExternalStoreRuntime,
  type AssistantRuntime,
  type ThreadMessage,
} from "@assistant-ui/react";
import { act, useLayoutEffect, useRef } from "react";
import { createRoot, type Root } from "react-dom/client";
import { afterEach, beforeEach, expect, it, vi } from "vite-plus/test";
import { useChartAttachments } from "../chat/use-chart-attachments";
import { Starters } from "../components/chat/starters";
import { starters } from "../shared/starters";

let root: Root;

const submit = vi.fn(async () => {});

const reportError = vi.fn();

function ExampleChat({ disabled = false }: { disabled?: boolean }) {
  const runtimeRef = useRef<AssistantRuntime>(undefined);
  const attachments = useChartAttachments(runtimeRef, disabled, reportError);

  const runtime = useExternalStoreRuntime<ThreadMessage>({
    messages: [],
    suggestions: starters.map(({ prompt, title }) => ({ prompt, title })),
    isDisabled: disabled || attachments.reading,
    onNew: submit,
    adapters: { attachments: attachments.adapter },
  });

  useLayoutEffect(() => {
    runtimeRef.current = runtime;
  }, [runtime]);

  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <Starters disabled={disabled || attachments.reading} onImage={attachments.uploadExample} />
    </AssistantRuntimeProvider>
  );
}

beforeEach(() => {
  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  vi.stubGlobal(
    "Image",
    class {
      async decode() {}
    },
  );
  vi.stubGlobal(
    "fetch",
    vi.fn(async () => new Response(new Uint8Array([1, 2, 3]))),
  );
  const container = document.createElement("div");
  document.body.append(container);
  root = createRoot(container);
});

afterEach(async () => {
  await act(async () => root.unmount());
  document.body.replaceChildren();
  vi.unstubAllGlobals();
  vi.clearAllMocks();
});

it.each(starters)("submits $title with its chart after the image is ready", async (starter) => {
  const decoding = Promise.withResolvers<void>();
  const decoded = Promise.withResolvers<void>();
  vi.stubGlobal(
    "Image",
    class {
      decode() {
        decoding.resolve();

        return decoded.promise;
      }
    },
  );
  await act(async () => root.render(<ExampleChat />));

  const button = Array.from(document.querySelectorAll("button")).find((item) =>
    item.textContent?.includes(starter.title),
  )!;

  await act(async () => {
    button.click();
    await decoding.promise;
  });
  expect(submit).not.toHaveBeenCalled();
  await act(async () => {
    decoded.resolve();
    await decoded.promise;
  });
  await vi.waitFor(() => expect(submit).toHaveBeenCalledTimes(1));
  expect(submit).toHaveBeenCalledWith(
    expect.objectContaining({
      content: [{ type: "text", text: starter.prompt }],
      attachments: [
        expect.objectContaining({
          name: starter.image.split("/").at(-1),
          content: [
            expect.objectContaining({
              type: "file",
              mimeType: "image/png",
              data: "data:image/png;base64,AQID",
            }),
          ],
        }),
      ],
    }),
  );
});

it("reports an example image failure before submitting a message", async () => {
  vi.stubGlobal(
    "fetch",
    vi.fn(async () => new Response(null, { status: 503 })),
  );
  await act(async () => root.render(<ExampleChat />));
  await act(async () => document.querySelector<HTMLButtonElement>("button")!.click());
  expect(reportError).toHaveBeenCalledWith(
    "Could not load the example chart. Try again or upload your own.",
  );
  expect(submit).not.toHaveBeenCalled();
});

it("keeps examples disabled while the chat is unavailable", async () => {
  await act(async () => root.render(<ExampleChat disabled />));
  await act(async () => document.querySelector<HTMLButtonElement>("button")!.click());
  expect(fetch).not.toHaveBeenCalled();
  expect(submit).not.toHaveBeenCalled();
});
