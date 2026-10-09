import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { parseSkill } from "../agent/skill-source.ts";

// SAFETY: Eve compilation emits instruction, skill, and tool records in its agent manifest.
const manifest = JSON.parse(
  await readFile(
    new URL("../.output/.eve/compile/compiled-agent-manifest.json", import.meta.url),
    "utf8",
  ),
) as {
  instructions: { role: string; content: string }[];
  skills: { name: string; markdown: string; description: string }[];
  tools: { name: string }[];
};

const core = parseSkill(
  await readFile(new URL("../../../skills/core/SKILL.md", import.meta.url), "utf8"),
);

assert.ok(
  manifest.instructions.some(
    (entry) => entry.role === "system" && entry.content.includes(core.markdown),
  ),
  "Built system instructions contain the canonical core skill",
);

for (const name of ["discuss", "visfeedback", "visrec"]) {
  const compiled = manifest.skills.find((entry) => entry.name === name);

  const canonical = parseSkill(
    await readFile(new URL(`../../../skills/${name}/SKILL.md`, import.meta.url), "utf8"),
  );

  assert.equal(compiled?.markdown, canonical.markdown, `${name} instructions match their source`);
  assert.equal(
    compiled?.description,
    canonical.description,
    `${name} description matches its source`,
  );
}

assert.ok(manifest.tools.some((entry) => entry.name === "load_skill"));

assert.ok(manifest.tools.some((entry) => entry.name === "present_answer"));

console.log("Verified canonical skills in the compiled agent.");
