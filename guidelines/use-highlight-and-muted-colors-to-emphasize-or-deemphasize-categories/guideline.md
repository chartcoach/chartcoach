---
id: use-highlight-and-muted-colors-to-emphasize-or-deemphasize-categories
title: Highlight Key Values and Gray Out Non-Data Categories
bibliography: references.bib
description: Use color emphasis to draw attention to important categories/ranges and
  de-emphasize 'others' or 'no data' with muted tones like gray.
labels:
- chart:general
- task:focus-attention
- visual:color
- impact:focus
- impact:clarity
- data:categorical
- data:quantitative
- audience:general
- complexity:practical
- source:datawrapper
---

## The Rule <!-- role: advice -->

Within any color scale, **highlight** the category or value range you want readers to notice most, and **de-emphasize** non-essential categories like “others” or “no data” by rendering them in muted colors (often gray). [@muth_which_color_scale_2021]

## The Logic <!-- role: reason -->

Color intensity and saturation act as attention signals: a standout color pulls focus, while muted tones recede, helping readers separate “story-critical” elements from contextual or missing-data elements. [@muth_which_color_scale_2021]

- **The Principle:** Attentional hierarchy through color emphasis vs. suppression.
- **The Evidence:** [@muth_which_color_scale_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly find what matters (a featured country, a critical threshold, a specific value like 0%).
- **Data Type:** Any—categorical palettes (highlight one group) or quantitative scales (highlight a special bin/range); includes explicit “no data” categories. [@muth_which_color_scale_2021]
- **Audience:** General audiences scanning quickly. [@muth_which_color_scale_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task requires equal-weight comparison across all categories or bins.
- **Reason:** Highlighting introduces visual bias that can distort neutral comparison. [@muth_which_color_scale_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** A highlighted element may appear more important than warranted, even if the data difference is small.
- **The Risk:** Over-highlighting (too many “key” colors) destroys hierarchy and makes the chart noisy. [@muth_which_color_scale_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using bright colors for “no data” or “other.”
- **Why it fails:** It steals attention from actual data and confuses the meaning of the visualization. [@muth_which_color_scale_2021]
- **The Wrong Fix:** Highlighting multiple categories at once with equally strong colors.
- **Why it fails:** Nothing stands out; the intended focus is lost. [@muth_which_color_scale_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Your eye lands first on “no data/other,” or you can’t tell what the chart wants you to notice.
- **The Test:** Look away and glance back for one second: if the first thing you notice isn’t the intended highlight, your emphasis is misassigned. [@muth_which_color_scale_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert “no data/other” to a neutral gray and reserve saturated colors for real data and the main highlight. [@muth_which_color_scale_2021]
- **Best Fix:** Reduce highlights to a single focal element/range and ensure the rest of the palette supports it with clearly subordinate, quieter colors. [@muth_which_color_scale_2021]
