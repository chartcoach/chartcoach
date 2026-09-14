import assert from "node:assert/strict";

export async function verifyModelSettings(page, screenshot) {
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
  await page.getByRole("button", { name: "Cancel", exact: true }).click();
  await page.getByRole("button", { name: "Close model settings", exact: true }).click();
}
