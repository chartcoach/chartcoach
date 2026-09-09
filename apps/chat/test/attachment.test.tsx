import { expect, it } from "vite-plus/test";
import { readAttachment } from "../chat/attachment";

it("rejects image formats the model upload path cannot accept", async () => {
  const file = new File(["<svg/>"], "chart.svg", { type: "image/svg+xml" });
  await expect(readAttachment(file)).rejects.toThrow("Choose a PNG, JPEG, or WebP chart image.");
});

it("rejects images above the model-visible attachment bound before decoding", async () => {
  const file = new File([new Uint8Array(3 * 1024 * 1024 + 1)], "chart.png", {
    type: "image/png",
  });
  await expect(readAttachment(file)).rejects.toThrow("Choose an image of 3 MiB or smaller.");
});
