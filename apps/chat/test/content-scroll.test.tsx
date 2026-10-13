// @vitest-environment jsdom
import { act, useState } from "react";
import { createRoot, type Root } from "react-dom/client";
import { afterEach, beforeEach, expect, it, vi } from "vite-plus/test";
import { useContentScroll } from "../chat/use-content-scroll";

let root: Root;

let contentHeight: number;

let viewportHeight: number;

let resize: () => void;

let time: number;

let frames: Map<number, FrameRequestCallback>;

let nextFrame: number;

let disconnect: ReturnType<typeof vi.fn>;

let disclosureTop: number;

let disclosureHeight: number;

function Reader({
  initial = "bottom",
  mounted = true,
}: {
  initial?: "top" | "bottom";
  mounted?: boolean;
}) {
  const { viewportRef, atLatest, scrollToLatest } = useContentScroll(initial);
  const [open, setOpen] = useState(false);

  return (
    <>
      {mounted ? (
        <div ref={viewportRef} role="region" aria-label="Content">
          <div>
            <div data-disclosure="evidence">
              <button aria-expanded={open} onClick={() => setOpen(!open)}>
                Evidence
              </button>
              <div hidden={!open}>New guideline evidence</div>
            </div>
            <button aria-expanded="false" aria-controls="pending" aria-disabled="true">
              Activity
            </button>
            <div id="pending" hidden />
          </div>
        </div>
      ) : null}
      {!atLatest ? <button onClick={scrollToLatest}>Latest response</button> : null}
    </>
  );
}

const viewport = () => document.querySelector<HTMLDivElement>('[aria-label="Content"]')!;

const render = (element = <Reader />) => act(async () => root.render(element));

const notifyResize = () => act(async () => resize());

const touch = (type: "touchstart" | "touchmove", clientY: number) => {
  const event = new Event(type);
  Object.defineProperty(event, "touches", { value: [{ clientY }] });
  viewport().dispatchEvent(event);
};

async function advance(count = 1) {
  await act(async () => {
    for (let index = 0; index < count; index++) {
      time += 16;
      const pending = [...frames.values()];
      frames.clear();

      for (const callback of pending) callback(time);
    }
  });
}

beforeEach(() => {
  contentHeight = 700;
  viewportHeight = 300;
  disclosureTop = 260;
  disclosureHeight = 220;
  time = 0;
  nextFrame = 0;
  frames = new Map();
  disconnect = vi.fn();
  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  vi.stubGlobal("matchMedia", () => ({ matches: false }));
  vi.stubGlobal("requestAnimationFrame", (callback: FrameRequestCallback) => {
    frames.set(++nextFrame, callback);

    return nextFrame;
  });
  vi.stubGlobal("cancelAnimationFrame", (id: number) => frames.delete(id));
  vi.spyOn(performance, "now").mockImplementation(() => time);
  vi.stubGlobal(
    "ResizeObserver",
    class {
      constructor(callback: () => void) {
        resize = callback;
      }
      observe() {}
      disconnect = disconnect;
    },
  );
  // jsdom has no layout engine. Supply the geometry a browser reports as content grows.
  vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockImplementation(() => viewportHeight);
  vi.spyOn(HTMLElement.prototype, "scrollHeight", "get").mockImplementation(() => contentHeight);
  vi.spyOn(HTMLElement.prototype, "getBoundingClientRect").mockImplementation(function (
    this: HTMLElement,
  ) {
    const isViewport = this.getAttribute("role") === "region";
    const isDisclosure = this.dataset.disclosure === "evidence";
    const top = isViewport ? 0 : isDisclosure ? disclosureTop - viewport().scrollTop : 0;
    const height = isViewport ? viewportHeight : isDisclosure ? disclosureHeight : contentHeight;
    const bottom = top + height;

    return {
      top,
      bottom,
      left: 0,
      right: 320,
      width: 320,
      height,
      x: 0,
      y: 0,
      toJSON() {},
    };
  });
  const container = document.createElement("div");
  document.body.append(container);
  root = createRoot(container);
});

afterEach(async () => {
  await act(async () => root.unmount());
  document.body.replaceChildren();
  vi.restoreAllMocks();
  vi.unstubAllGlobals();
});

it("opens a saved conversation at its latest content and follows streamed growth smoothly", async () => {
  await render();
  expect(viewport().scrollTop).toBe(400);
  contentHeight = 1000;
  await notifyResize();
  await advance();
  expect(viewport().scrollTop).toBeGreaterThan(400);
  expect(viewport().scrollTop).toBeLessThan(700);
  await advance(40);
  expect(viewport().scrollTop).toBe(700);
});

it("starts observing content that mounts after the reader", async () => {
  await render(<Reader mounted={false} />);
  expect(document.querySelector('[aria-label="Content"]')).toBeNull();
  await render(<Reader />);
  expect(viewport().scrollTop).toBe(400);
  contentHeight = 1000;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(700);
});

it("pauses following when the reader scrolls back and resumes from Latest response", async () => {
  await render();
  await act(async () => {
    viewport().scrollTop = 100;
    viewport().dispatchEvent(new Event("scroll"));
  });
  contentHeight = 1000;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(100);

  const latest = Array.from(document.querySelectorAll("button")).find(
    (button) => button.textContent === "Latest response",
  )!;

  await act(async () => latest.click());
  await advance(40);
  expect(viewport().scrollTop).toBe(700);
});

it("cancels a pending scroll when an upward wheel gesture arrives", async () => {
  await render();
  contentHeight = 1000;
  await notifyResize();
  await act(async () => viewport().dispatchEvent(new WheelEvent("wheel", { deltaY: -40 })));
  await advance(40);
  expect(viewport().scrollTop).toBe(400);
  await act(async () => {
    viewport().scrollTop = 350;
    viewport().dispatchEvent(new Event("scroll"));
  });
  contentHeight = 1200;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(350);
});

it("keeps following after a tap and pauses when a touch gesture scrolls upward", async () => {
  await render();
  await act(async () => touch("touchstart", 100));
  contentHeight = 1000;
  await notifyResize();
  await advance();
  expect(viewport().scrollTop).toBeGreaterThan(400);

  await act(async () => touch("touchmove", 140));
  const pausedAt = viewport().scrollTop;
  contentHeight = 1200;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(pausedAt);
});

it("reveals expanded evidence while the reader is away from the latest content", async () => {
  await render(<Reader initial="top" />);
  expect(viewport().scrollTop).toBe(0);
  await act(async () =>
    Array.from(document.querySelectorAll("button"))
      .find((button) => button.textContent === "Evidence")!
      .click(),
  );
  contentHeight = 1000;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(192);

  contentHeight = 1200;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(192);
});

it("lets an explicit latest request supersede a pending disclosure reveal", async () => {
  await render(<Reader initial="top" />);

  const evidence = document.querySelector<HTMLButtonElement>(
    '[data-disclosure="evidence"] button',
  )!;

  const latest = Array.from(document.querySelectorAll("button")).find(
    (button) => button.textContent === "Latest response",
  )!;

  await act(async () => {
    evidence.click();
    latest.click();
  });
  contentHeight = 1000;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(700);
});

it("continues following when an unavailable disclosure is clicked", async () => {
  await render();
  await act(async () =>
    Array.from(document.querySelectorAll("button"))
      .find((button) => button.textContent === "Activity")!
      .click(),
  );
  contentHeight = 1000;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(700);
});

it("keeps the start of an expanded disclosure visible when it is taller than the viewport", async () => {
  disclosureTop = 80;
  disclosureHeight = 500;
  await render(<Reader initial="top" />);
  await act(async () =>
    Array.from(document.querySelectorAll("button"))
      .find((button) => button.textContent === "Evidence")!
      .click(),
  );
  contentHeight = 1000;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(68);
});

it("keeps the latest content visible when the keyboard reduces the viewport", async () => {
  await render();
  viewportHeight = 180;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(520);
});

it("continues following after streamed content temporarily shrinks", async () => {
  await render();
  contentHeight = 1000;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(700);

  contentHeight = 700;
  await act(async () => {
    viewport().scrollTop = 400;
    viewport().dispatchEvent(new Event("scroll"));
  });
  await notifyResize();
  contentHeight = 1000;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(700);
});

it("continues following after a taller viewport clamps its scroll position", async () => {
  await render();
  viewportHeight = 500;
  await act(async () => {
    viewport().scrollTop = 200;
    viewport().dispatchEvent(new Event("scroll"));
  });
  await notifyResize();
  contentHeight = 900;
  await notifyResize();
  await advance(40);
  expect(viewport().scrollTop).toBe(400);
});

it("respects reduced motion when following new content", async () => {
  vi.stubGlobal("matchMedia", () => ({ matches: true }));
  await render();
  contentHeight = 1000;
  await notifyResize();
  await advance();
  expect(viewport().scrollTop).toBe(700);
});

it("finishes following when the browser quantizes scroll positions", async () => {
  await render();
  let scrollTop = viewport().scrollTop;
  Object.defineProperty(viewport(), "scrollTop", {
    configurable: true,
    get: () => scrollTop,
    set: (value: number) => {
      scrollTop = Math.floor(value);
    },
  });
  contentHeight = 1000;
  await notifyResize();
  await advance(80);
  expect(viewport().scrollTop).toBe(700);
  expect(frames.size).toBe(0);
});

it("releases resize observation and pending animation when the reader closes", async () => {
  await render();
  contentHeight = 1000;
  await notifyResize();
  expect(frames.size).toBe(1);
  await act(async () => root.render(null));
  expect(frames.size).toBe(0);
  expect(disconnect).toHaveBeenCalledOnce();
});
