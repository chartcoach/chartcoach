import { cp, readFile, writeFile } from "node:fs/promises";
import { basename, join } from "node:path";
import { z } from "zod";

const artifactsSchema = z.object({
  kind: z.literal("eve-sandbox-prepared-artifacts"),
  version: z.literal(2),
  entries: z
    .array(
      z.object({
        nodeId: z.string(),
        providerName: z.literal("just-bash"),
        artifact: z.object({ templateRootPath: z.string() }),
      }),
    )
    .min(1),
});

// Eve embeds prepared artifacts in this bootstrap before Nitro bundles it.
// Preserve the prepared filesystem while replacing build-machine paths.
export async function relocateSandboxTemplates(bootstrapPath: string, directory: string) {
  const source = await readFile(bootstrapPath, "utf8");
  const declaration = /const sandboxPreparedArtifacts = ([\s\S]*?);\n/.exec(source);

  if (!declaration) throw new Error("Eve's build is missing prepared sandbox artifacts.");
  const artifacts = artifactsSchema.parse(JSON.parse(declaration[1]));

  for (const entry of artifacts.entries) {
    const original = entry.artifact.templateRootPath;
    const key = basename(original);

    if (!/^[a-f0-9]{24}$/.test(key)) throw new Error("Invalid Eve sandbox template key.");
    await cp(original, join(directory, key), { recursive: true });
    entry.artifact.templateRootPath = `.eve/sandbox-cache/just-bash/templates/${key}`;
  }

  await writeFile(
    bootstrapPath,
    source.replace(
      declaration[0],
      `const sandboxPreparedArtifacts = ${JSON.stringify(artifacts)};\n`,
    ),
  );
}
