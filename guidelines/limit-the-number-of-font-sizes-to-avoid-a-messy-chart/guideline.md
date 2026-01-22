---
id: limit-the-number-of-font-sizes-to-avoid-a-messy-chart
title: Limit the number of font sizes to avoid a messy chart
bibliography: references.bib
description: Use only a small set of clearly distinct font sizes and rely on weight
  for emphasis within a level.
labels:
- chart:general
- task:scan
- visual:text
- impact:clarity
- data:general
- audience:novice
- complexity:basic
---

## Keep font sizes to a small, consistent set <!-- role: advice -->

Use only a few font sizes with clearly separated roles, and emphasize within a level using boldness rather than introducing many new sizes. Aim for clean hierarchy instead of granular typographic variation.

## Too many sizes create visual noise <!-- role: reason -->

When many text sizes appear, the chart can look chaotic and readers lose a stable sense of what matters. A small set of sizes makes hierarchy legible and improves the overall tidiness of the design.

**Mechanism:** Consistency reduces visual clutter and makes typographic signals easier to interpret.

**Evidence:** Using lots of different font sizes can quickly look messy; a limited hierarchy (for example, two levels for labels/annotations) keeps the visualization cleaner [@muth_text_in_data_visualizations_2022].

**Notes:** Weight and color can provide emphasis without adding additional size steps.

## Apply when multiple labels and annotations are present <!-- role: context -->

- **User Goal:** Scan text without distraction and understand importance levels.
- **Task:** Read titles, labels, and annotations in a clear order.
- **Data:** Any; especially charts with several annotations or many labels.
- **Chart Setting:** Static charts where typography must carry hierarchy alone.
- **Audience:** General audiences; readers sensitive to clutter.
- **Success Criterion:** The chart looks orderly and hierarchy is obvious.

## When more size levels may be necessary <!-- role: exceptions -->

**Break it when:** The visualization includes fundamentally different text roles that must be strongly separated (for example, a headline-style callout and small-print legal notes). **Why:** A larger size range can be required to prevent critical text from competing with minor details.

## Trade nuance for consistency <!-- role: costs -->

**Sacrifice:** Finer-grained differentiation among many annotation types. **Risk:** If roles are too compressed, readers may not distinguish primary from secondary notes. **Mitigation:** Use contrast and weight to separate importance while keeping sizes limited.

## Typical failure modes <!-- role: mistakes -->

**Mistake:** Introducing a new font size for each new label or note. **Why it fails:** The chart gains noise and loses a coherent hierarchy.

## Quick checks <!-- role: check -->

**Failure Sign:** The text feels “busy,” with many subtly different sizes. **Quick Check:** Count distinct font sizes; if you can’t easily list their purposes, there are too many. **Stronger Test:** Remove color temporarily; if hierarchy becomes unclear, size usage may be inconsistent.

## What to do instead <!-- role: fix -->

- Consolidate labels and annotations into two or three size roles and apply them consistently.
- Use bold to emphasize keywords within annotations rather than changing size.
- De-emphasize secondary text with lighter color instead of smaller-and-smaller sizes.
- Remove or move low-priority text to make the remaining hierarchy clearer.
