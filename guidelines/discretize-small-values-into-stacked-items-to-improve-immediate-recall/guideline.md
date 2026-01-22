---
id: discretize-small-values-into-stacked-items-to-improve-immediate-recall
title: Discretize small values into stacked items to improve immediate value recall
bibliography: references.bib
description: Breaking a bar into a small countable stack reduces recall error for
  small numeric ranges.
labels:
- chart:bar
- task:recall
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- encoding:stacked-items
---

## Use stacked discrete items for small numeric values when recall matters <!-- role: advice -->

When values are small, represent them as a stack of discrete items rather than as a single stretched bar to improve immediate recall. Keep the stack sizes within a small countable range.

## Small discrete quantities can be encoded more precisely than continuous extent in memory <!-- role: reason -->

For small numerosities, viewers can quickly and accurately represent “how many items” while also getting a redundant length cue, supporting more precise working-memory encoding during brief viewing.

**Mechanism:** Discretizing creates a redundant encoding (number of items plus overall height), which can strengthen memory for the value when the number of items remains small.

**Evidence:** In a brief glance-and-recall task with values in the 1–5 range, stacked representations produced lower recall error than stretched representations, for both simple shapes and pictographs [@harozISOTYPEVisualizationWorking2015a]. When the value ranges increased (up to 10 and 15), the advantage of stacking over stretching disappeared, consistent with the benefit being limited to small stacks [@harozISOTYPEVisualizationWorking2015a].

**Notes:** The improvement is about stacking vs stretching, not about whether the marks are pictographs versus simple shapes.

## Charts with small ranges where recall precision is important <!-- role: context -->

- **User Goal:** Remember specific values after a brief look.
- **Task:** Encode and recall multiple category values.
- **Data:** Small integer-like ranges (especially up to about 5).
- **Chart Setting:** Static charts, quick glances, or memory-demanding presentations.
- **Audience:** General users; variable working-memory performance.
- **Success Criterion:** Reduced absolute recall error.

## When not to rely on stacking <!-- role: exceptions -->

**Break it when:** Values routinely exceed a small countable range (e.g., stacks would exceed ~5 items). **Why:** The stacking benefit disappeared for larger ranges in the tested memory task, so extra items add clutter without a recall advantage [@harozISOTYPEVisualizationWorking2015a].

## Costs of discretizing values <!-- role: costs -->

**Sacrifice:** You give up visual simplicity and may spend more space per mark. **Risk:** Large stacks become visually dense and hard to parse, reducing legibility. **Mitigation:** Constrain stacking to small ranges and avoid forcing large values into many discrete units.

## Common implementation failures <!-- role: mistakes -->

- **Mistake:** Using stacks for large values that require many items. **Why it fails:** The stacking advantage vanished as ranges increased, so the added complexity is not compensated by better recall [@harozISOTYPEVisualizationWorking2015a].
- **Mistake:** Assuming the benefit depends on pictographs. **Why it fails:** The stacking benefit appeared for simple shapes as well as pictographs [@harozISOTYPEVisualizationWorking2015a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users misremember values that differ by 1–2 units even in small ranges. **Quick Check:** Try a stacked version with 1–5 items and rerun a brief hide-and-recall test; error should drop if stacking is helping. **Stronger Test:** Compare stacked vs stretched with representative value ranges; if most values exceed small stacks, do not discretize.

## What to do instead <!-- role: fix -->

- Use a standard stretched bar encoding when typical values exceed small stack sizes.
- Use stacking only for the low end of the scale where stacks remain small and legible.
- Reduce the numeric range shown per chart (e.g., separate panels) if stacking is desired for recall.
- Keep the discrete segmentation visually clear so individual items are distinguishable.
