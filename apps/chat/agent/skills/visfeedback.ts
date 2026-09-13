import { defineSkill } from "eve/skills";
import markdown from "@chartcoach/skills/visfeedback?raw";
import { parseSkill } from "../skill-source";

export default defineSkill(parseSkill(markdown));
