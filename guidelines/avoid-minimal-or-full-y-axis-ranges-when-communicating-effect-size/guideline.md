---
id: avoid-minimal-or-full-y-axis-ranges-when-communicating-effect-size
title: "Avoid minimal-fit and full-scale y-axis ranges when the graph\u2019s purpose\
  \ is effect-size communication"
bibliography: references.bib
description: Do not rely on either data-tight y-axis ranges or full possible ranges
  when readers must assess effect magnitude from the graphic.
labels:
- chart:bar
- chart:line
- task:estimate
- visual:position
- impact:trust
- impact:clarity
- data:quantitative
- audience:novice
- custom:axis-range
---

## Avoid the two axis extremes for effect-size reading tasks <!-- role: advice -->

Avoid setting the y-axis to the minimum range that fits the data or to the full possible range when the intent is for readers to judge effect size from the plot. Use an intermediate, SD-referenced range instead of either extreme.

## Extreme scaling causes systematic magnitude bias in opposite directions <!-- role: reason -->

Minimal-fit axes amplify visual differences, encouraging overestimation; full-range axes compress differences, encouraging underestimation. Because viewers rely on the graphic’s visual impression, these extremes shift judgments even when the underlying data are unchanged.

**Mechanism:** Changing only the y-axis range changes perceived magnitude, which alters categorical judgments of effect size and reduces the ability to discriminate among small/medium/large effects.

**Evidence:** In controlled experiments using identical data plotted with different y-axis ranges, minimal-fit axes produced a strong bias toward judging effects as larger, while full-range axes produced a strong bias toward judging effects as smaller; SD-based intermediate ranges reduced bias and improved sensitivity [@wittGraphConstruction2019]. The direction held across bar and line graphs, and also when error bars were present [@wittGraphConstruction2019].

**Notes:** Minimal-fit axes sometimes appear to improve “detecting any effect,” but this can reflect bias (inflation) rather than genuinely better discrimination of magnitudes among nonzero effects [@wittGraphConstruction2019].

## When you are designing for magnitude interpretation (not just visibility) <!-- role: context -->

- **User Goal:** Read effect magnitude from the plot with reasonable calibration.
- **Task:** Discriminate among multiple nonzero effect sizes (e.g., small vs medium vs large).
- **Data:** Two-condition mean differences or trend endpoints that imply an effect size.
- **Chart Setting:** Static presentation where the plot is expected to carry the magnitude message.
- **Audience:** Readers likely to rely on visual impression rather than computing effect sizes.
- **Success Criterion:** Reduced over- and underestimation bias plus improved sensitivity to differences in effect size.

## When an extreme axis range can be justified <!-- role: exceptions -->

- **Break it when:** The communicative goal is explicitly to show the outcome’s absolute position on a meaningful full scale (e.g., emphasizing proximity to ceiling/floor), not to help viewers judge standardized effect magnitude. **Why:** Full-range scaling supports absolute-scale interpretation even though it impairs effect-size discrimination [@wittGraphConstruction2019].
- **Break it when:** The plot is purely exploratory for analysts who will compute effect sizes from numbers rather than infer them visually. **Why:** Visual calibration is less critical when the graphic is not used to make magnitude judgments [@wittGraphConstruction2019].

## Tradeoffs of avoiding extremes <!-- role: costs -->

**Sacrifice:** You may reduce immediate emphasis (from minimal-fit zoom) or reduce full-scale context (from full-range axes). **Risk:** An intermediate range can be misread as “zoomed in” if not clearly labeled and contextualized. **Mitigation:** Make the axis limits explicit and, when relevant, describe the SD-based span in the caption [@wittGraphConstruction2019].

## Frequent axis-range anti-patterns <!-- role: mistakes -->

- **Mistake:** Using minimal-fit y-axes because they “make the effect visible.” **Why it fails:** Visibility can come at the cost of systematically inflated magnitude impressions [@wittGraphConstruction2019].
- **Mistake:** Defaulting to a full 0–max range to avoid accusations of exaggeration. **Why it fails:** It systematically compresses differences and biases judgments toward null/small effects [@wittGraphConstruction2019].

## Tests to detect whether you are at an extreme <!-- role: check -->

**Failure Sign:** The same mean difference looks “dramatic” in one version and “tiny” in another version of the same plot. **Quick Check:** Replot the same data with minimal-fit, full-range, and an SD-based intermediate range; if judgments would plausibly change, the axis is doing persuasive work. **Stronger Test:** Ask readers to categorize effect size from each version and look for directional bias shifts (inflation with minimal-fit; deflation with full-range) [@wittGraphConstruction2019].

## Better options than extreme axis settings <!-- role: fix -->

- Use an SD-based intermediate axis span centered on the grand mean so visual differences better correspond to standardized effect size [@wittGraphConstruction2019].
- If absolute-scale context is important, supplement an SD-based plot with a second full-range panel rather than forcing the effect-size reading task onto the full-range view [@wittGraphConstruction2019].
- If you must use a minimal-fit axis, add explicit contextual cues (e.g., report effect size numerically) so the magnitude is not inferred only from the zoomed visual [@wittGraphConstruction2019].
- Keep axis scaling consistent across related plots when comparison across plots is required, adjusting spans only enough to keep all key plotted elements visible [@wittGraphConstruction2019].
