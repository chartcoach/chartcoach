// @vitest-environment jsdom
import { act } from "react";
import { createRoot } from "react-dom/client";
import { expect, it, vi } from "vite-plus/test";
import type { EvidenceItem } from "../chat/evidence";
import { EvidencePanel } from "../components/chat/evidence-panel";
import { renderDocument } from "./render-document";

it("shows primary guideline cards before opening the remaining evidence", () => {
  const page = renderDocument(
    <EvidencePanel
      items={[
        {
          stage: "primary",
          guideline: {
            id: "labels",
            title: "Label series directly",
            url: "https://chartcoach.dev/guidelines/labels",
            imageURL: "https://chartcoach.dev/guidelines/labels/og.png",
          },
        },
        {
          stage: "supporting",
          guideline: {
            id: "contrast",
            title: "Keep labels legible",
            url: "https://chartcoach.dev/guidelines/contrast",
          },
        },
      ]}
    />,
  );

  const primary = page.querySelector('section[aria-label="Primary guidelines"]')!;
  const card = primary.querySelector<HTMLAnchorElement>('a[aria-label="Label series directly"]')!;
  expect(card.getAttribute("href")).toBe("https://chartcoach.dev/guidelines/labels");
  expect(card.querySelector("img")?.getAttribute("src")).toBe(
    "https://chartcoach.dev/guidelines/labels/og.png",
  );
  expect(card.textContent).toContain("Label series directly");
  expect(card.closest("[inert]")).toBeNull();
  expect(
    page
      .querySelector('button[aria-label="Guidelines for this answer"]')
      ?.getAttribute("aria-expanded"),
  ).toBe("true");
  expect(page.querySelector('button[aria-haspopup="dialog"]')?.textContent).toContain("1 primary");

  const supporting = Array.from(page.querySelectorAll("button")).find(
    (button) => button.textContent?.trim() === "Supporting 1",
  )!;

  expect(supporting.getAttribute("aria-expanded")).toBe("false");

  const source = page.querySelector<HTMLAnchorElement>(
    'a[aria-label="Read guideline: Keep labels legible"]',
  )!;

  expect(source.getAttribute("href")).toBe("https://chartcoach.dev/guidelines/contrast");
  expect(source.closest("[inert]")).not.toBeNull();
});

it("shows live candidates with catalog descriptions without presenting them as primary evidence", () => {
  const page = renderDocument(
    <EvidencePanel
      busy
      items={[
        {
          stage: "matched",
          guideline: {
            id: "labels",
            title: "Label series directly",
            description: "Place each name beside its series.",
            url: "https://chartcoach.dev/guidelines/labels",
          },
        },
      ]}
    />,
  );

  expect(page.querySelector('[role="status"]')?.textContent).toBe("1 found · 0 read");
  const result = page.querySelector<HTMLAnchorElement>('section[aria-label="Search results"] a')!;
  expect(result.textContent).toContain("Place each name beside its series.");
  expect(result.getAttribute("href")).toBe("https://chartcoach.dev/guidelines/labels");
  expect(result.closest("[inert]")).toBeNull();
});

it("distinguishes waiting for retrieval from an empty result", () => {
  expect(
    renderDocument(<EvidencePanel items={[]} active busy />).querySelector('[role="status"]')
      ?.textContent,
  ).toBe("Finding relevant guidance…");
  expect(
    renderDocument(<EvidencePanel items={[]} active />).querySelector('[role="status"]')
      ?.textContent,
  ).toBe("No guidelines retrieved yet");
  expect(renderDocument(<EvidencePanel items={[]} />).body.childElementCount).toBe(0);
});

it("keeps a guideline that leaves the shortlist in place until it has collapsed", async () => {
  vi.useFakeTimers();
  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  vi.stubGlobal("matchMedia", () => ({ matches: false }));
  vi.stubGlobal(
    "ResizeObserver",
    class {
      observe() {}
      disconnect() {}
    },
  );

  const candidate = (id: string, stage: EvidenceItem["stage"] = "matched"): EvidenceItem => ({
    stage,
    guideline: { id, title: `Guideline ${id}`, url: `https://chartcoach.dev/guidelines/${id}` },
  });

  const container = document.createElement("div");
  document.body.append(container);
  const root = createRoot(container);

  const shortlist = () =>
    Array.from(
      container.querySelectorAll('section[aria-label="Search results"] > ul > li'),
      (row) => [row.querySelector("a")?.getAttribute("aria-label"), row.hasAttribute("inert")],
    );

  try {
    await act(async () =>
      root.render(<EvidencePanel busy items={["a", "b", "c", "d"].map((id) => candidate(id))} />),
    );
    // Reading a match moves it ahead of the shortlist it pushes "c" out of.
    await act(async () =>
      root.render(
        <EvidencePanel
          busy
          items={[candidate("d", "read"), ...["a", "b", "c"].map((id) => candidate(id))]}
        />,
      ),
    );

    expect(shortlist()).toEqual([
      ["Read guideline: Guideline d", false],
      ["Read guideline: Guideline a", false],
      ["Read guideline: Guideline b", false],
      ["Read guideline: Guideline c", true],
    ]);

    await act(async () => vi.runAllTimers());

    expect(shortlist()).toEqual([
      ["Read guideline: Guideline d", false],
      ["Read guideline: Guideline a", false],
      ["Read guideline: Guideline b", false],
    ]);
  } finally {
    await act(async () => root.unmount());
    container.remove();
    vi.useRealTimers();
    vi.unstubAllGlobals();
  }
});
