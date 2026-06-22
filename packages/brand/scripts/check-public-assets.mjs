import { findBrandAssetDrift, publicBrandTargets, relativeToRepo } from "./public-brand-assets.mjs";

let hasDrift = false;

for (const target of publicBrandTargets) {
  const drift = await findBrandAssetDrift(target);
  const messages = [
    drift.missing.length > 0 ? `missing: ${drift.missing.join(", ")}` : "",
    drift.changed.length > 0 ? `changed: ${drift.changed.join(", ")}` : "",
    drift.extra.length > 0 ? `extra: ${drift.extra.join(", ")}` : "",
  ].filter(Boolean);

  if (messages.length === 0) continue;

  hasDrift = true;
  console.error(`${relativeToRepo(target)} does not match packages/brand/assets/brand`);
  for (const message of messages) console.error(`  ${message}`);
}

if (hasDrift) {
  console.error("Run `pnpm --dir packages/brand sync:assets` to update public copies.");
  process.exitCode = 1;
} else {
  console.log("public brand assets match packages/brand/assets/brand");
}
