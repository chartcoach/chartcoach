// @vitest-environment jsdom
import {
  useExternalStoreRuntime,
  type AssistantRuntime,
  type ThreadMessage,
} from "@assistant-ui/react";
import { act, useLayoutEffect, useRef } from "react";
import { createRoot, type Root } from "react-dom/client";
import { afterEach, expect, it, vi } from "vite-plus/test";
import { useChartAttachments } from "../chat/use-chart-attachments";

let root: Root;

let attachments: ReturnType<typeof useChartAttachments>;

const reportError = vi.fn<(message: string | undefined) => void>();

function UploadComposer() {
  const runtimeRef = useRef<AssistantRuntime>(undefined);
  attachments = useChartAttachments(runtimeRef, false, reportError);

  const runtime = useExternalStoreRuntime<ThreadMessage>({
    messages: [],
    onNew: async () => {},
    adapters: { attachments: attachments.adapter },
  });

  useLayoutEffect(() => {
    runtimeRef.current = runtime;
  }, [runtime]);

  return (
    <textarea ref={attachments.messageInput} disabled={attachments.reading} aria-label="Message" />
  );
}

afterEach(async () => {
  await act(async () => root.unmount());
  document.body.replaceChildren();
  vi.unstubAllGlobals();
  vi.clearAllMocks();
});

async function renderComposer() {
  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  const container = document.createElement("div");
  document.body.append(container);
  root = createRoot(container);
  await act(async () => root.render(<UploadComposer />));
}

it("focuses the enabled composer after a delayed image finishes decoding", async () => {
  const decoding = Promise.withResolvers<void>();
  const decoded = Promise.withResolvers<void>();

  class ChartImage {
    src = "";

    decode() {
      decoding.resolve();

      return decoded.promise;
    }
  }

  vi.stubGlobal("Image", ChartImage);
  await renderComposer();
  const input = document.querySelector("textarea")!;
  let upload: Promise<void>;
  await act(async () => {
    upload = attachments.upload([new File(["chart"], "chart.png", { type: "image/png" })]);
    await decoding.promise;
  });
  expect(input.disabled).toBe(true);
  await act(async () => {
    decoded.resolve();
    await upload;
  });
  expect(input.disabled).toBe(false);
  expect(document.activeElement).toBe(input);
});

it.each([
  {
    name: "an unsupported format",
    file: new File(["<svg/>"], "chart.svg", { type: "image/svg+xml" }),
    message: "Choose a PNG, JPEG, or WebP chart image.",
  },
  {
    name: "an oversized image",
    file: new File([new Uint8Array(3 * 1024 * 1024 + 1)], "chart.png", { type: "image/png" }),
    message: "Choose an image of 3 MiB or smaller.",
  },
])("returns focus to the composer after immediately rejecting $name", async ({ file, message }) => {
  await renderComposer();
  const outside = document.createElement("button");
  document.body.append(outside);
  outside.focus();
  await act(async () => attachments.upload([file]));
  const input = document.querySelector("textarea")!;
  expect(input.disabled).toBe(false);
  expect(reportError).toHaveBeenCalledWith(message);
  expect(document.activeElement).toBe(input);
});
