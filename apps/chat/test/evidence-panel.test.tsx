import { renderToStaticMarkup } from "react-dom/server";
import { expect, it } from "vite-plus/test";
import { EvidencePanel } from "../components/chat/evidence-panel";

it("shows primary guideline images before opening the remaining evidence", () => {
  const html = renderToStaticMarkup(
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
  expect(html).toContain('aria-label="Primary guidelines"');
  expect(html).toMatch(/<a[^>]+aria-label="Label series directly"/);
  expect(html.match(/<img\b/g)).toHaveLength(1);
  expect(html).toContain("More guidelines");
  const remainingId = html.match(/aria-controls="([^"]+)"/)?.[1];
  expect(remainingId).toBeDefined();
  expect(html.indexOf('aria-label="Label series directly"')).toBeLessThan(
    html.indexOf(`id="${remainingId}"`),
  );
});
