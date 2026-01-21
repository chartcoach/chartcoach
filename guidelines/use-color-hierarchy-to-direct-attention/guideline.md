---
id: use-color-hierarchy-to-direct-attention
title: Create a Color Hierarchy to Direct Attention
bibliography: references.bib
description: Use saturation, darkness, and gray/desaturation to make the most important
  data visually dominant and everything else recede.
labels:
- chart:general
- task:emphasize
- visual:color
- impact:clarity
- data:general
- audience:general
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

Decide what you want readers to notice first, then assign colors to create a clear hierarchy: use saturated/high-contrast colors for the most important items and gray or desaturated/transparent versions for everything else.

## The Logic <!-- role: reason -->

Color is a primary attention cue: readers’ eyes are drawn first to the highest-contrast, most saturated colors, and only later to gray, low-saturation, or low-contrast marks. By pushing non-priority data into gray or less saturated/less opaque variants, you reduce visual competition so the key categories or values “win” attention.

- **The Principle:** Visual salience and hierarchy through contrast and saturation
- **The Evidence:** [@muth_emphasize_color_2023]

## Where to Apply <!-- role: context -->

This advice is designed for moments where attention needs to be guided rather than evenly distributed.

- **User Goal:** Spot the main takeaway quickly (what matters first/second/last), while still keeping supporting context visible.
- **Data Type:** Any chart/map/table where multiple marks compete (categorical series, multiple lines, many groups, or highlighted ranges/values).
- **Audience:** Especially useful for general audiences or time-constrained readers scanning for the key point. [@muth_emphasize_color_2023]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Every category is equally important and must be distinguishable without labels (e.g., many categories that readers must compare individually).\
  **Reason:** Turning most categories gray or too similar can remove necessary differentiation; readers may not be able to tell groups apart. [@muth_emphasize_color_2023]
- **Scenario:** You intend gray to mean an actual data category with equal narrative importance to other categories.\
  **Reason:** Gray is commonly read as “background/other/less important,” so using it as a peer category miscommunicates priority. [@muth_emphasize_color_2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** De-emphasized categories become harder to read and compare (sometimes intentionally unlabeled or visually subdued).
- **The Risk:** If you overdo de-emphasis, readers may miss secondary insights you still want them to find; if you underdo it, the hierarchy collapses and nothing stands out. [@muth_emphasize_color_2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating gray as just another category color because you “ran out of colors.”\
  **Why it fails:** Gray carries a strong learned meaning of “less important/other,” so it warps the narrative importance of that category. [@muth_emphasize_color_2023]
- **The Wrong Fix:** Using a different hue to de-emphasize a group (e.g., bright blue for important items and dark blue as a “secondary” hue).\
  **Why it fails:** A hue change implies a categorical change, not “same category but less important,” so it creates a misleading grouping. [@muth_emphasize_color_2023]
- **The Wrong Fix:** Reducing saturation in a way that shifts the color character (e.g., turning red into a brownish tone) rather than creating a clearly “same but quieter” version.\
  **Why it fails:** The subdued marks no longer read as related to the highlighted marks, weakening the intended grouping. [@muth_emphasize_color_2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Your “most important” series/segment doesn’t immediately pop; multiple elements compete equally; or de-emphasized items look like separate categories due to hue changes.
- **The Test:** Squint at the chart: the first thing you notice should be the intended highlight; if not, your hierarchy is too weak or mis-specified. [@muth_emphasize_color_2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Make all non-essential categories gray (or a clearly less saturated/less opaque version of the highlight color), then re-color only the few items you want noticed first. [@muth_emphasize_color_2023]
- **Best Fix:** Build multiple hierarchy levels with color: (1) most important = darkest/most saturated/highest contrast; (2) next = lighter/less saturated; (3) supporting = dark gray; (4) background = light gray—ensuring de-emphasis uses gray/desaturation rather than introducing new hues. [@muth_emphasize_color_2023]
