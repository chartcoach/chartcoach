import { readFileSync } from "node:fs";
import { describe, expect, it } from "vite-plus/test";
import instructions from "../agent/instructions";
import discuss from "../agent/skills/discuss";
import visfeedback from "../agent/skills/visfeedback";
import visrec from "../agent/skills/visrec";
import { parseSkill } from "../agent/skill-source";

describe("canonical agent skills", () => {
  it("keeps the core instructions in every model call", () => {
    const core = readFileSync(new URL("../../../skills/core/SKILL.md", import.meta.url), "utf8");
    expect(instructions.content).toContain(parseSkill(core).markdown);
  });

  it("loads the canonical workflow documents and their routing descriptions", () => {
    for (const [name, definition] of Object.entries({ discuss, visfeedback, visrec })) {
      const canonical = readFileSync(
        new URL(`../../../skills/${name}/SKILL.md`, import.meta.url),
        "utf8",
      );
      expect(canonical).toContain(`description: ${definition.description}`);
      expect(canonical.slice(canonical.indexOf("\n---", 4) + 4).trim()).toBe(definition.markdown);
    }
  });
});
