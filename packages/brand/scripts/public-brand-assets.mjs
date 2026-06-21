import { readdir, readFile, rm, mkdir, copyFile } from "node:fs/promises";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = dirname(fileURLToPath(import.meta.url));

export const packageRoot = resolve(scriptDir, "..");
export const repoRoot = resolve(packageRoot, "../..");
export const sourceBrandDir = join(packageRoot, "assets", "brand");
export const publicBrandTargets = [
  join(repoRoot, "apps/site/public/brand"),
  join(repoRoot, "apps/docs/public/brand"),
];

export const relativeToRepo = (path) => relative(repoRoot, path);

export const listBrandFiles = async (dir) => {
  const entries = await readdir(dir, { withFileTypes: true });

  return entries
    .filter((entry) => entry.isFile() && !entry.name.startsWith("."))
    .map((entry) => entry.name)
    .sort((a, b) => a.localeCompare(b));
};

export const copyBrandAssets = async (targetDir) => {
  const files = await listBrandFiles(sourceBrandDir);
  await rm(targetDir, { recursive: true, force: true });
  await mkdir(targetDir, { recursive: true });

  await Promise.all(
    files.map((file) => copyFile(join(sourceBrandDir, file), join(targetDir, file))),
  );
};

export const findBrandAssetDrift = async (targetDir) => {
  const sourceFiles = await listBrandFiles(sourceBrandDir);
  const targetFiles = await listBrandFiles(targetDir).catch(() => []);
  const sourceSet = new Set(sourceFiles);
  const targetSet = new Set(targetFiles);
  const missing = sourceFiles.filter((file) => !targetSet.has(file));
  const extra = targetFiles.filter((file) => !sourceSet.has(file));
  const changed = [];

  for (const file of sourceFiles) {
    if (!targetSet.has(file)) continue;

    const [sourceBytes, targetBytes] = await Promise.all([
      readFile(join(sourceBrandDir, file)),
      readFile(join(targetDir, file)),
    ]);

    if (!sourceBytes.equals(targetBytes)) changed.push(file);
  }

  return { changed, extra, missing };
};
