---
id: use-opacity-to-create-pastel-deemphasis
title: De-Emphasize with Opacity Instead of Hue Changes
bibliography: references.bib
description: Reduce emphasis by making colors less opaque, producing lighter pastel
  versions that preserve category identity.
labels:
- chart:general
- task:deemphasize
- visual:color
- impact:focus
- data:categorical
- audience:general
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

To make a category less prominent while keeping it recognizable, lower its opacity (increase transparency) rather than switching hues.

## The Logic <!-- role: reason -->

Lower opacity keeps hue consistent while reducing visual weight; it also often produces a brighter pastel look that can be preferable to simply reducing saturation, which can make colors look muddy or shift character. This supports a clear priority gradient without inventing new categories.

- **The Principle:** Priority via reduced visual weight while preserving hue identity
- **The Evidence:** [@muth_emphasize_color_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** See multiple categories, but understand that some matter more than others.
- **Data Type:** Charts with a small-to-moderate number of categories where all remain distinct hues, but secondary ones should recede (e.g., a few lines/bars/dots).
- **Audience:** Readers who need a quick “what matters most” cue without losing the ability to distinguish categories. [@muth_emphasize_color_2023]

## When to Break It <!-- role: exceptions -->

- **Scenario:** De-emphasized elements must remain highly legible against the background (e.g., very thin lines or small marks that disappear when made transparent).\
  **Reason:** Reduced opacity can make marks too faint to see, undermining comprehension. [@muth_emphasize_color_2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** Lower-importance marks become harder to see and compare precisely.
- **The Risk:** If opacity is reduced too far, users may think the data is missing or disabled rather than intentionally de-emphasized. [@muth_emphasize_color_2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a different hue for secondary categories instead of lowering opacity.\
  **Why it fails:** Hue implies categorical difference rather than lower importance. [@muth_emphasize_color_2023]
- **The Wrong Fix:** Lowering saturation in a way that changes the perceived color family (e.g., red turning brownish).\
  **Why it fails:** The mark no longer reads as the same “kind” of data—category identity gets weaker. [@muth_emphasize_color_2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Secondary marks either vanish or look like a separate category because the color shifted.
- **The Test:** Compare highlight vs secondary side-by-side: if the secondary no longer clearly matches the highlight hue family (just quieter), adjust. [@muth_emphasize_color_2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase opacity of the de-emphasized marks until they’re clearly visible but still lighter than the highlight. [@muth_emphasize_color_2023]
- **Best Fix:** Use a deliberate stepped hierarchy (e.g., 100% opacity for primary, ~80% for secondary, ~30% for tertiary) while keeping hues constant within each category. (In hex RGBA notation, opacity can be expressed by appending an alpha value to the 6-digit hex color, as described in the article.) [@muth_emphasize_color_2023]
