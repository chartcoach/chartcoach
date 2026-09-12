// @vitest-environment jsdom
import { act, type ReactNode } from "react";
import { createRoot, type Root } from "react-dom/client";
import { afterEach, beforeEach, expect, it, vi } from "vite-plus/test";
import { ConnectionForm } from "../components/settings/connection-form";
import { emptyConnection } from "../chat/use-connection-form";
import { Dropzone } from "../components/chat/dropzone";

let root: Root;

beforeEach(() => {
  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  const container = document.createElement("div");
  document.body.append(container);
  root = createRoot(container);
});

afterEach(async () => {
  await act(async () => root.unmount());
  document.body.replaceChildren();
  vi.unstubAllGlobals();
  vi.restoreAllMocks();
});

const render = (element: ReactNode) => act(async () => root.render(element));

async function fill(name: string, value: string) {
  await act(async () => {
    const input = document.querySelector<HTMLInputElement>(`input[name="${name}"]`)!;
    Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, "value")!.set!.call(input, value);
    input.dispatchEvent(new Event("input", { bubbles: true }));
  });
}

async function click(text: string) {
  await act(async () => {
    const button = Array.from(document.querySelectorAll("button")).find(
      (item) => (item.getAttribute("aria-label") ?? item.textContent)?.trim() === text,
    );

    expect(button).toBeDefined();
    button!.click();
  });
}

it("focuses the invalid credential field before a connection can be saved", async () => {
  const save = vi.fn(async () => {});
  await render(
    <ConnectionForm
      initial={emptyConnection("openai")}
      pending={false}
      origins={[]}
      onSave={save}
      onCancel={() => {}}
    />,
  );
  await fill("apiKey", "invalid key");
  await fill("model", "vision-model");
  await click("Save and use");
  const input = document.querySelector<HTMLInputElement>('input[name="apiKey"]')!;
  expect(document.activeElement).toBe(input);
  expect(input.getAttribute("aria-invalid")).toBe("true");
  expect(document.getElementById(input.getAttribute("aria-describedby")!)?.textContent).toContain(
    "no spaces or line breaks",
  );
  expect(save).not.toHaveBeenCalled();
  await fill("apiKey", "valid-test-key");
  await click("Save and use");
  expect(save).toHaveBeenCalledWith(
    expect.objectContaining({
      provider: "openai",
      model: "vision-model",
      apiKey: "valid-test-key",
    }),
  );
});

it("discards model discovery results when the provider changes", async () => {
  const response = Promise.withResolvers<Response>();
  let signal: AbortSignal | null | undefined;
  vi.stubGlobal(
    "fetch",
    vi.fn((_input: RequestInfo | URL, init?: RequestInit) => {
      signal = init?.signal;

      return response.promise;
    }),
  );
  await render(
    <ConnectionForm
      initial={emptyConnection("openai")}
      pending={false}
      origins={[]}
      onSave={async () => {}}
      onCancel={() => {}}
    />,
  );
  await fill("apiKey", "test-key");
  await click("Load models");
  await click("Gemini");
  expect(signal?.aborted).toBe(true);
  await act(async () =>
    response.resolve(Response.json([{ id: "old-model", name: "Old provider model" }])),
  );
  expect(document.querySelectorAll("datalist option")).toHaveLength(0);
  expect(document.querySelector<HTMLInputElement>('input[name="apiKey"]')!.value).toBe("");
  expect(document.querySelector<HTMLInputElement>('input[name="name"]')!.value).toBe("Gemini");
});

it("honors the current upload gate while retaining one global drop subscription", async () => {
  const onFiles = vi.fn();
  const chart = new File(["chart"], "chart.png", { type: "image/png" });

  const drop = async () => {
    const event = new Event("drop", { cancelable: true });
    Object.defineProperty(event, "dataTransfer", { value: { types: ["Files"], files: [chart] } });
    await act(async () => {
      window.dispatchEvent(event);
    });

    return event;
  };

  await render(
    <Dropzone disabled={false} hasAttachment={false} onFiles={onFiles}>
      Chat
    </Dropzone>,
  );
  expect((await drop()).defaultPrevented).toBe(true);
  expect(onFiles).toHaveBeenCalledExactlyOnceWith([chart]);
  await render(
    <Dropzone disabled hasAttachment onFiles={onFiles}>
      Chat
    </Dropzone>,
  );
  expect((await drop()).defaultPrevented).toBe(true);
  expect(onFiles).toHaveBeenCalledTimes(1);
  await render(null);
  expect((await drop()).defaultPrevented).toBe(false);
});
