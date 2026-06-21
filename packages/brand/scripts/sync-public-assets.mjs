import { copyBrandAssets, publicBrandTargets, relativeToRepo } from "./public-brand-assets.mjs";

for (const target of publicBrandTargets) {
  await copyBrandAssets(target);
  console.log(`synced ${relativeToRepo(target)}`);
}
