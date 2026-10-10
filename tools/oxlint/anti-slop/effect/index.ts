import { eslintCompatPlugin } from "vite-plus/lint/plugins";
import { noManualEffectErrorTagRule } from "./rules/no-manual-effect-error-tag.ts";
import { noManualTagComparisonRule } from "./rules/no-manual-tag-comparison.ts";
import { noManualTaggedConstructionRule } from "./rules/no-manual-tagged-construction.ts";
import { noServiceConstructorImportsRule } from "./rules/no-service-constructor-imports.ts";
import { preferEffectMatchRule } from "./rules/prefer-effect-match.ts";

export const antiSlopEffectPluginRules = {
  "no-manual-effect-error-tag": noManualEffectErrorTagRule,
  "no-manual-tag-comparison": noManualTagComparisonRule,
  "no-manual-tagged-construction": noManualTaggedConstructionRule,
  "no-service-constructor-imports": noServiceConstructorImportsRule,
  "prefer-effect-match": preferEffectMatchRule,
} as const;

export type AntiSlopEffectRuleName = keyof typeof antiSlopEffectPluginRules;

export default eslintCompatPlugin({
  meta: { name: "anti-slop-effect" },
  rules: antiSlopEffectPluginRules,
});
