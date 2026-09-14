import assert from "node:assert/strict";

/** Exercise the production picker against records from the installed SDK. */
export async function verifyPicker(page, catalog, screenshot) {
  const sources = catalog.table("guideline_sources");
  const ids = (rows) => [...new Set(rows.map((row) => row.guideline_id))];
  const all = [...catalog].map((row) => row.id);
  const first = sources.find((row) => row.guideline_id === all[0]);
  assert.ok(first?.authors.length && first.source_type && first.year);
  const author = first.authors[0];
  const type = first.source_type;
  const year = Number(first.year);
  const results = page.getByRole("list", { name: "Matched guideline results" });
  const apply = page.getByRole("button", { name: "Use these guidelines", exact: true });
  const reset = page.getByRole("button", { name: "Select all", exact: true });
  const summary = page.locator('footer [role="status"]');

  async function selection(expected) {
    await page.waitForFunction(
      (count) => {
        const status = document.querySelector('footer [role="status"]');
        const error = document.querySelector('[role="alert"]');

        if (error?.textContent) throw new Error(error.textContent);

        return (
          status?.getAttribute("aria-busy") === "false" &&
          status.textContent === `${count.toLocaleString()} guidelines selected`
        );
      },
      expected.length,
      { timeout: 60_000 },
    );
    await results.locator(':scope[aria-busy="false"]').waitFor();
    const links = results.getByRole("link");

    if (expected.length) {
      await links.first().waitFor();

      const rendered = await links.evaluateAll((nodes) =>
        nodes.map((node) => new URL(node.href).searchParams.get("id")),
      );

      assert.ok(rendered.length > 0);

      for (const id of rendered) assert.ok(expected.includes(id), `Unexpected guideline: ${id}`);
      assert.equal(
        await results.getByRole("listitem").first().getAttribute("aria-setsize"),
        String(expected.length),
      );
    } else {
      await page.getByText("No guidelines match your selection.", { exact: true }).waitFor();
      assert.equal(await links.count(), 0);
    }
  }

  async function chooseAuthor(choice) {
    await page.getByRole("button", { name: /Browse authors/ }).click();
    const search = page.getByRole("searchbox", { name: "Find an author" });

    await search.waitFor();
    assert.equal(await search.evaluate((element) => document.activeElement === element), true);
    assert.equal(
      await search.evaluate((element) => getComputedStyle(element.parentElement).outlineWidth),
      "2px",
    );
    await search.fill(author);
    await page
      .getByRole("combobox", { name: `Filter author ${author}`, exact: true })
      .selectOption(choice);
    await page.getByRole("button", { name: "Close author picker" }).click();
  }

  const parquet = "**/eve/v1/catalog/*/entries.parquet";
  await page.route(parquet, (route) => route.abort());
  const guidelines = page.getByRole("button", { name: "Guidelines", exact: true });

  await guidelines.click();
  await guidelines.locator(':scope[aria-current="page"]').waitFor();
  assert.equal(await page.locator("[aria-current]").count(), 1);
  assert.equal(await guidelines.getAttribute("aria-current"), "page");
  await page.getByRole("button", { name: "Retry", exact: true }).waitFor();
  await page.unroute(parquet);
  await page.getByRole("button", { name: "Retry", exact: true }).click();
  await page.getByRole("button", { name: "Retry", exact: true }).waitFor({ state: "hidden" });
  await selection(all);
  await page.getByRole("button", { name: "How filters work", exact: true }).click();
  await page.getByRole("heading", { name: "How filters work", exact: true }).waitFor();
  await page.getByText("Guidelines can cite more than one source.", { exact: false }).waitFor();
  await page.getByRole("button", { name: "How filters work", exact: true }).click();
  await apply.locator(":scope:disabled").waitFor();
  await page.screenshot({ path: screenshot, fullPage: true, animations: "disabled" });

  // Exercise the virtual list beyond its first batch on the full release.
  if (all.length > 100) {
    await results.evaluate((element) => {
      element.scrollTop = element.scrollHeight;
    });
    await results.locator('[aria-posinset="101"]').waitFor();
    await selection(all);
  }

  const fromInput = page.getByRole("spinbutton", { name: "From", exact: true });
  const toInput = page.getByRole("spinbutton", { name: "Through", exact: true });
  const firstYear = Number(await fromInput.getAttribute("min"));
  const lastYear = Number(await toInput.getAttribute("max"));

  if (lastYear - firstYear >= 10) {
    const start = firstYear + 2;
    const end = lastYear - 4;
    const shift = 2;
    await fromInput.fill(String(start));
    await toInput.fill(String(end));
    await selection(
      ids(sources.filter((row) => Number(row.year) >= start && Number(row.year) <= end)),
    );
    const range = page.locator('[title="Drag to move the selected year range"]');
    const bounds = await range.boundingBox();

    const trackWidth = await range.evaluate(
      (element) => element.parentElement?.getBoundingClientRect().width,
    );

    assert.ok(bounds && trackWidth);
    await page.mouse.move(bounds.x + bounds.width / 2, bounds.y + bounds.height / 2);
    await page.mouse.down();
    await page.mouse.move(
      bounds.x + bounds.width / 2 + (trackWidth * shift) / (lastYear - firstYear),
      bounds.y + bounds.height / 2,
      { steps: 4 },
    );
    await page.mouse.up();
    await page.waitForFunction(
      ([from, to]) =>
        document.querySelector('[name="yearFrom"]')?.value === String(from) &&
        document.querySelector('[name="yearTo"]')?.value === String(to),
      [start + shift, end + shift],
    );
    await selection(
      ids(
        sources.filter(
          (row) => Number(row.year) >= start + shift && Number(row.year) <= end + shift,
        ),
      ),
    );
    await reset.click();
    await selection(all);
  }

  const popup = page.waitForEvent("popup");
  const link = results.getByRole("link").first();
  const target = new URL(await link.getAttribute("href"), page.url()).searchParams.get("id");
  await link.click();
  const detail = await popup;
  await detail.getByRole("heading", { name: catalog.get(target).title, exact: true }).waitFor();
  await detail.close();

  await chooseAuthor("include");
  const authored = ids(sources.filter((row) => row.authors.includes(author)));
  await selection(authored);
  await chooseAuthor("exclude");
  await selection(all.filter((id) => !authored.includes(id)));
  await reset.click();
  await selection(all);

  const sourceType = page.getByRole("checkbox", { name: `Source type ${type}`, exact: true });
  await sourceType.check();
  await selection(ids(sources.filter((row) => row.source_type === type)));
  await page.getByRole("spinbutton", { name: "From", exact: true }).fill(String(year));
  await page.getByRole("spinbutton", { name: "Through", exact: true }).fill(String(year));
  await chooseAuthor("include");
  await selection(
    ids(
      sources.filter(
        (row) =>
          row.source_type === type && Number(row.year) === year && row.authors.includes(author),
      ),
    ),
  );

  await page.getByRole("spinbutton", { name: "From", exact: true }).fill(String(year + 1));
  await page
    .getByText("The first year must be at or before the last year.", { exact: true })
    .waitFor();
  await apply.locator(":scope:disabled").waitFor();
  await reset.click();
  await selection(all);

  // An empty scope must prevent chat submission, then recover by selecting all.
  await fromInput.fill(String(lastYear + 1));
  await selection([]);
  await apply.click();
  await apply.waitFor({ state: "hidden" });
  await page
    .getByText("No guidelines selected. Open Guidelines to broaden your selection.", {
      exact: true,
    })
    .waitFor();
  assert.equal(await page.getByRole("button", { name: /send/i }).isEnabled(), false);
  await page.getByRole("button", { name: "Guidelines", exact: true }).click();
  await selection([]);
  await reset.click();
  await selection(all);

  await page.setViewportSize({ width: 390, height: 844 });
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
  await page.screenshot({
    path: screenshot.replace(".png", "-mobile.png"),
    fullPage: true,
    animations: "disabled",
  });

  // Applying a source filter carries real browser SQL into the next chat turn.
  await sourceType.check();
  const selected = ids(sources.filter((row) => row.source_type === type));
  await selection(selected);
  await apply.click();
  await apply.waitFor({ state: "hidden" });
  await page.getByRole("button", { name: "Open sidebar", exact: true }).click();
  await page.getByRole("button", { name: "Guidelines", exact: true }).click();
  await selection(selected);
  assert.equal(await sourceType.isChecked(), true);
  await apply.locator(":scope:disabled").waitFor();
  await page.getByRole("button", { name: "Back to chat", exact: true }).click();
  await summary.waitFor({ state: "hidden" });
  await page.setViewportSize({ width: 1280, height: 900 });

  return selected;
}
