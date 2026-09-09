import { JSDOM } from "jsdom";
import { describe, expect, it } from "vite-plus/test";

import { renderGuidelineCitations } from "../src/lib/guideline-citations";
import { summarizeGuidelineReferences } from "../src/og/references";

describe("guideline citations", () => {
  it("keeps each reference's macro scope when rendering a shared bibliography", () => {
    const references = [
      '@string{venue="Alpha"}@article{a,title={First},author={Doe, Jane},year={2020},journal=venue}',
      '@string{venue="Beta"}@article{b,title={Second},author={Doe, Jane},year={2020},journal=venue}',
    ];
    const result = renderGuidelineCitations(["[@a; @b]"], references);
    const dom = new JSDOM(result.bodies[0] + result.bibliographyHtml);
    expect(dom.window.document.getElementById("ref-a")?.textContent).toContain("Alpha");
    expect(dom.window.document.getElementById("ref-b")?.textContent).toContain("Beta");
    expect(
      dom.window.document.querySelector('[data-citekey="a"]')?.getAttribute("title"),
    ).toContain("Alpha");
    expect(summarizeGuidelineReferences(references).map((reference) => reference.meta)).toEqual([
      "Doe, 2020 · Alpha",
      "Doe, 2020 · Beta",
    ]);
    dom.window.close();
  });

  it("disambiguates grouped and repeated citations across sections and links each source", () => {
    const result = renderGuidelineCitations(
      ["Evidence [@a; @b].", "Reason [@a]."],
      [
        "@article{a,title={Alpha},author={Doe, Jane},year={2020},journal={Journal}}",
        "@article{b,title={Beta},author={Doe, Jane},year={2020},journal={Journal}}",
      ],
    );
    const dom = new JSDOM(result.bodies.join("\n") + result.bibliographyHtml);
    const document = dom.window.document;
    expect(result.citedKeys).toEqual(["a", "b"]);
    expect(document.body.textContent).toContain("Evidence (Doe, 2020a; 2020b).");
    expect(document.body.textContent).toContain("Reason (Doe, 2020a).");
    const links = [...document.querySelectorAll<HTMLAnchorElement>("a.citation")];
    expect(links.map((link) => link.dataset.citekey)).toEqual(["a", "b", "a"]);
    for (const link of links) {
      const target = document.getElementById(decodeURIComponent(link.hash.slice(1)));
      expect(target?.textContent).toBe(link.title);
    }
    expect(document.querySelectorAll(".csl-entry")).toHaveLength(2);
    dom.window.close();
  });

  it("renders source links safely and reports unknown citation keys", () => {
    const result = renderGuidelineCitations(
      ["[@web; @missing]"],
      [
        "@misc{web,title={<script>alert(1)</script>},author={Doe, Jane},year={2020},url={https://example.com/reference}}",
      ],
    );
    const dom = new JSDOM(result.bodies[0] + result.bibliographyHtml);
    const document = dom.window.document;
    expect(document.querySelector("script")).toBeNull();
    expect(document.querySelector(".citation--missing")?.textContent).toBe("@missing");
    expect(document.querySelector(".citation--missing")?.getAttribute("title")).toBe(
      "Missing reference: missing",
    );
    const source = document.querySelector<HTMLAnchorElement>(".csl-entry a");
    expect(source?.href).toBe("https://example.com/reference");
    expect(source?.rel).toBe("noreferrer");
    dom.window.close();
  });

  it("keeps uncited content unchanged and omits its bibliography", () => {
    expect(renderGuidelineCitations(["Ordinary [link](https://example.com)."], [])).toEqual({
      bodies: ["Ordinary [link](https://example.com)."],
      citedKeys: [],
      bibliographyHtml: undefined,
    });
  });
});

describe("Open Graph reference summaries", () => {
  it("resolves bibliography macros and names for the two displayed sources", () => {
    const summaries = summarizeGuidelineReferences([
      `
      @string{venue = "Journal of Charts"}
      @article{a, title={Charts and {Nested} Titles}, author={Doe, Jane}, year={2020}, journal=venue}
      @article{b, title={Second}, author={Roe, John}, year={2021}, journal=venue}
      @article{c, title={Third}, year={2022}}
    `,
    ]);
    expect(summaries).toEqual([
      { title: "Charts and Nested Titles", meta: "Doe, 2020 · Journal of Charts" },
      { title: "Second", meta: "Roe, 2021 · Journal of Charts" },
    ]);
  });
});
