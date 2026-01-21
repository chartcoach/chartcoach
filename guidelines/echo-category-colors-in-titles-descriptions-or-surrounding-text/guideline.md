---
id: echo-category-colors-in-titles-descriptions-or-surrounding-text
title: Echo Category Colors in Nearby Text
bibliography: references.bib
description: Reuse category colors in titles, descriptions, or surrounding article
  text so readers can learn and recall what each color means.
labels:
- chart:multi
- task:explain
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- component:title
- component:caption
---

## The Rule <!-- role: advice -->

Reuse your category colors in the text around the visualization (title/description or surrounding article text) to restate the color-to-category mapping.

## The Logic <!-- role: reason -->

Linking narrative text and visual encoding teaches readers what each color stands for and reminds them as they read, reducing reliance on a separate legend and helping readers who enter the graphic at different points. The post describes using colored category names in titles/descriptions and integrating color cues into surrounding text (often in scrollytelling).

- **The Principle:** Redundant encoding across chart and narrative to reinforce mappings
- **The Evidence:** [@muth_remind_colors_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand which categories correspond to which colors while reading an explanatory headline/caption or narrative
- **Data Type:** Multi-category visuals where readers benefit from explicit “what color means what” framing
- **Audience:** General readers, especially in article or scrollytelling contexts [@muth_remind_colors_2023]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your category color is blue and the surrounding text appears link-like (typical web styling).
- **Reason:** The post warns that blue text may be perceived as a hyperlink, potentially confusing readers about what is interactive versus what is a category cue. [@muth_remind_colors_2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** Added styling effort and potential redundancy if you also keep a traditional legend.
- **The Risk:** Colored text can dominate the design more than the chart itself or create confusion about links/interactivity. [@muth_remind_colors_2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Removing the legend entirely after adding colored title text, without ensuring readers are still reminded throughout the chart.
- **Why it fails:** Readers may start reading mid-chart or forget mappings; the post recommends keeping a key or direct labels as reinforcement even when using title-based cues. [@muth_remind_colors_2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Readers must rely on memory because neither the legend nor any colored textual cue is present near where they’re reading.
- **The Test:** Jump into the visualization halfway down: can you learn/confirm the color meanings from the nearby text (title/caption/overlay) without searching? [@muth_remind_colors_2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Color the category names (only) in the title or description to explicitly state the mapping.
- **Best Fix:** Combine colored text cues with a persistent or repeated legend/direct labels so the mapping is available no matter where readers start. [@muth_remind_colors_2023]
