// @vitest-environment jsdom
import { expect, it } from "vite-plus/test";
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
  expect(card.getAttribute("href")).toBe("/guideline?id=labels");
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

  expect(source.getAttribute("href")).toBe("/guideline?id=contrast");
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
  expect(result.getAttribute("href")).toBe("/guideline?id=labels");
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
