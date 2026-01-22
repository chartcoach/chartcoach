---
id: enforce-noticeable-differences-based-on-mark-size-to-avoid-confusable-colors
title: Enforce noticeable differences between categorical colors based on mark size
bibliography: references.bib
description: Apply a conservative noticeable-difference threshold so categorical colors
  remain distinguishable for small marks.
labels:
- chart:map
- task:discriminate
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:intermediate
---

## Filter out colors that are not noticeably different at the intended mark size <!-- role: advice -->

Before selecting categorical palette colors, enforce a conservative noticeable-difference threshold based on the intended mark size, and reject candidate colors that fall within that indistinguishable neighborhood.

## Why size-aware noticeable-difference filtering reduces confusion <!-- role: reason -->

Color discriminability depends on the visual angle of marks; what is distinguishable at large sizes can be confusable at small sizes, so size-aware filtering prevents near-neighbor colors from entering the palette.

**Mechanism:** A noticeable-difference function provides a minimum interval in color space required to discriminate marks more than 50% of the time for a given size; removing neighbors after each selection preserves spacing relative to the mark scale.

**Evidence:** The model enforces a lower discriminability bound by sampling only noticeably different colors using a size-based difference function with a conservative visual angle and additional safety margin, and it removes indiscriminable neighbors after sampling each color [@gramazioColorgoricalCreatingDiscriminable2017a]. This constraint is part of the tool’s minimum assertions to maintain discriminability in visualization contexts [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** This is a pre-filter; you can still optimize with perceptual distance or name difference after.

## When this applies <!-- role: context -->

- **User Goal:** Ensure categories remain distinguishable in the actual chart, not just as swatches.
- **Task:** Identify and compare colored marks where marks can be small or dense.
- **Data:** Categorical.
- **Chart Setting:** Maps with small regions, dense scatterplots, small legends, or compact dashboards.
- **Audience:** General users performing quick identification.
- **Success Criterion:** Reduced confusions attributable to near-neighbor colors at the intended scale.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You can guarantee large mark sizes and ample separation in the final rendering. **Why:** The conservative threshold may unnecessarily limit palette options.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Smaller feasible palette size, because more colors are filtered out as “too close.” **Risk:** You may exhaust available colors for large palettes under other constraints. **Mitigation:** Reduce category count per view or relax other filters (like hue restrictions) if needed.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Validating palette distinctness only with large swatches. **Why it fails:** Mark-size effects can make near-neighbor colors confusable in the actual chart.
- **Mistake:** Adding new colors without removing indistinguishable neighbors. **Why it fails:** Subsequent picks can drift into confusable regions, collapsing the effective distance.

## Quick tests <!-- role: check -->

**Failure Sign:** Two categories look distinct in the legend but merge in small marks on the chart. **Quick Check:** Render the palette on the smallest marks you expect and look for pairs that become hard to tell apart. **Stronger Test:** Run a short discrimination task using the smallest marks and the most similar color pair.

## What to do instead <!-- role: fix -->

- Increase mark size or reduce density so colors can be discriminated with the current palette.
- Remove or merge categories to reduce the palette size requirement under the size-aware threshold.
- Regenerate the palette with a stricter minimum separation if confusions persist.
- Use additional encodings (e.g., shape) for categories that remain confusable at small sizes.
