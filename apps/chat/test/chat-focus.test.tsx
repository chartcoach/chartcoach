// @vitest-environment jsdom
import { act, useRef } from "react";
import { createRoot, type Root } from "react-dom/client";
import { afterEach, beforeEach, expect, it, vi } from "vite-plus/test";
import { useChatFocus } from "../chat/use-chat-focus";

let root: Root;

function Conversation({
  loading,
  disabled,
  version = 0,
}: {
  loading: boolean;
  disabled: boolean;
  version?: number;
}) {
  const message = useRef<HTMLTextAreaElement>(null);
  const heading = useRef<HTMLHeadingElement>(null);
  useChatFocus("chat", loading, disabled, message, heading);

  return (
    <>
      <h1 ref={heading} tabIndex={-1}>
        Conversation
      </h1>
      {!loading ? <textarea key={version} ref={message} disabled={disabled} /> : null}
      <button>Other control</button>
    </>
  );
}

beforeEach(() => {
  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  vi.stubGlobal("matchMedia", () => ({ matches: true }));
  const container = document.createElement("div");
  document.body.append(container);
  root = createRoot(container);
});

afterEach(async () => {
  await act(async () => root.unmount());
  document.body.replaceChildren();
  vi.unstubAllGlobals();
});

it("waits for saved transcript catch-up before focusing, then preserves later user focus", async () => {
  await act(async () => root.render(<Conversation loading disabled />));
  await act(async () => root.render(<Conversation loading={false} disabled />));
  expect(document.activeElement).toBe(document.body);
  await act(async () => root.render(<Conversation loading={false} disabled={false} />));
  expect(document.activeElement).toBe(document.querySelector("textarea"));
  const other = document.querySelector("button")!;
  other.focus();
  await act(async () => root.render(<Conversation loading={false} disabled />));
  await act(async () => root.render(<Conversation loading={false} disabled={false} />));
  expect(document.activeElement).toBe(other);
});

it("focuses the mobile conversation heading instead of opening the software keyboard", async () => {
  vi.stubGlobal("matchMedia", () => ({ matches: false }));
  await act(async () => root.render(<Conversation loading={false} disabled={false} />));
  expect(document.activeElement).toBe(document.querySelector("h1"));
});

it("preserves a focus the user chooses while a saved conversation reconnects", async () => {
  await act(async () => root.render(<Conversation loading disabled />));
  const other = document.querySelector("button")!;
  other.focus();
  await act(async () => root.render(<Conversation loading={false} disabled />));
  await act(async () => root.render(<Conversation loading={false} disabled={false} />));
  expect(document.activeElement).toBe(other);
});

it("restores lost composer focus after the first accepted turn relocates it", async () => {
  await act(async () => root.render(<Conversation loading={false} disabled={false} />));
  await act(async () => root.render(<Conversation loading={false} disabled version={1} />));
  expect(document.activeElement).toBe(document.body);
  await act(async () => root.render(<Conversation loading={false} disabled={false} version={1} />));
  expect(document.activeElement).toBe(document.querySelector("textarea"));
});

it("preserves another chosen control when the first accepted turn relocates the composer", async () => {
  await act(async () => root.render(<Conversation loading={false} disabled={false} />));
  const other = document.querySelector("button")!;
  other.focus();
  await act(async () => root.render(<Conversation loading={false} disabled version={1} />));
  await act(async () => root.render(<Conversation loading={false} disabled={false} version={1} />));
  expect(document.activeElement).toBe(other);
});
