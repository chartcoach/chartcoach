---
id: do-not-use-new-hues-to-deemphasize
title: De-Emphasize Without Introducing New Hues
bibliography: references.bib
description: Keep de-emphasized data in the same hue (or gray) so it reads as less
  important, not as a different category.
labels:
- chart:general
- task:deemphasize
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

When de-emphasizing data, do not introduce a new hue; instead use gray or a less saturated/less opaque version of the same hue.

## The Logic <!-- role: reason -->

A hue change is typically read as a category change. If you want readers to interpret marks as belonging to the same category set but with different priority, keep hue constant and adjust saturation/opacity/brightness to signal importance levels.

- **The Principle:** Hue encodes categorical difference; saturation/contrast encodes priority
- **The Evidence:** [@muth_emphasize_color_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand which items are primary vs secondary without misreading groups as different categories.
- **Data Type:** Multi-series charts (especially scatterplots and line charts) where some series are labeled/important and others are supporting context.
- **Audience:** Readers accustomed to gray/low-saturation as “background,” especially in news-style data graphics. [@muth_emphasize_color_2023]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You truly need to communicate a categorical distinction between groups (not importance).\
  **Reason:** In that case, a new hue is appropriate because the message is “different kind,” not “same kind but less important.” [@muth_emphasize_color_2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less ability to uniquely identify many secondary categories at a glance if they share a hue or sit in gray.
- **The Risk:** If labeling/interaction is absent, readers may struggle to distinguish among multiple de-emphasized series. [@muth_emphasize_color_2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a darker/lighter second hue (e.g., bright blue vs dark blue) to indicate “less important.”\
  **Why it fails:** Readers can interpret it as two categories, not one category with two priority levels. [@muth_emphasize_color_2023]
- **The Wrong Fix:** Mixing hue shifts with saturation changes inconsistently across series.\
  **Why it fails:** The hierarchy becomes ambiguous: is the difference category, priority, or both? [@muth_emphasize_color_2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Secondary items look like they form a separate group purely because their hue differs.
- **The Test:** Ask: “If I removed labels, would a viewer think these are different categories?” If yes due to hue, you broke the rule. [@muth_emphasize_color_2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Recolor de-emphasized marks using the exact same hue as the highlight and reduce saturation or opacity. [@muth_emphasize_color_2023]
- **Best Fix:** Establish a consistent hierarchy system: one hue per true category, and importance controlled only by saturation/opacity/gray—applied uniformly across the chart. [@muth_emphasize_color_2023]
