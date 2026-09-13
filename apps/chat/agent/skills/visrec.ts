import { defineSkill } from "eve/skills";
import markdown from "@chartcoach/skills/visrec?raw";
import { parseSkill } from "../skill-source";

export default defineSkill(parseSkill(markdown));
