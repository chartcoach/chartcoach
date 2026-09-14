import assert from "node:assert/strict";

export async function verifyModelSettings(page, screenshot, customBaseURL) {
  await page.getByRole("button", { name: "Model settings", exact: true }).click();
  await page.getByRole("button", { name: "Add a connection", exact: true }).click();
  await page.getByRole("button", { name: "OpenAI compatible", exact: true }).click();

  const provider = page.getByRole("combobox", { name: "Compatible provider", exact: true });

  await provider.click();
  const options = page.getByRole("option");

  assert.equal(await options.count(), 11);
  assert.ok((await options.locator("svg").count()) >= 10);
  await page.getByRole("option", { name: "OpenRouter", exact: true }).click();
  await page.getByRole("textbox", { name: "Connection name", exact: true }).waitFor();
  assert.equal(
    await page.getByRole("textbox", { name: "Connection name", exact: true }).inputValue(),
    "OpenRouter",
  );
  assert.equal(
    await page.getByRole("textbox", { name: "API base URL", exact: true }).inputValue(),
    "https://openrouter.ai/api/v1",
  );
  assert.match(await provider.innerText(), /OpenRouter/);
  await provider.click();
  await page.screenshot({ path: screenshot, fullPage: true, animations: "disabled" });
  await page.getByRole("option", { name: "Custom endpoint", exact: true }).click();
  assert.equal(
    await page.getByRole("textbox", { name: "Connection name", exact: true }).inputValue(),
    "OpenAI compatible",
  );
  assert.equal(
    await page.getByRole("textbox", { name: "API base URL", exact: true }).inputValue(),
    "",
  );
  await page.getByRole("textbox", { name: "API base URL", exact: true }).fill(customBaseURL);
  await page.getByRole("combobox", { name: "Model", exact: true }).fill("package-test-model");
  const authentication = page.getByRole("combobox", { name: "Authentication", exact: true });

  assert.ok(
    (await authentication.evaluate((element) => element.getBoundingClientRect().width)) <= 360,
  );

  const arrow = await authentication.evaluate((element) => {
    const control = element.getBoundingClientRect();
    const icon = element.parentElement.querySelector("svg").getBoundingClientRect();

    return {
      inset: control.right - icon.right,
      center: (control.top + control.bottom - icon.top - icon.bottom) / 2,
    };
  });

  assert.equal(arrow.inset, 12);
  assert.equal(arrow.center, 0);
  await authentication.selectOption("none");
  assert.match(await provider.innerText(), /Custom endpoint/);
  await page.getByRole("button", { name: "Save and use", exact: true }).click();
  await page.getByRole("dialog").waitFor({ state: "hidden" });
}
