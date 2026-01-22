---
id: keep-color-keys-within-view-to-prevent-forgetting
title: Keep the color key within one screen of the data visualization
bibliography: references.bib
description: Ensure readers can always re-check what colors mean by keeping the color
  key close to the colored data.
labels:
- chart:multiple
- task:decode
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:layout
---

## Keep the color key within one screen of the colored data <!-- role: advice -->

Keep the color key close enough that readers never need to scroll more than about one screen to see it while looking at the data.

## Why proximity to the key supports color decoding <!-- role: reason -->

When the key is far away, readers must remember arbitrary color-category mappings while scanning the chart; this increases effort and makes misreads more likely. Keeping the key in view reduces “lookup” friction and supports continuous checking while reading.

**Mechanism:** Shortening the visual and memory distance between colored marks and their explanation lowers cognitive load and speeds up correct category identification.

**Evidence:** Readers often need to consult the legend repeatedly while interpreting a visualization, so placing it far away makes understanding slower and more error-prone [@muth_remind_colors_2023]. Keeping the key on the same page (print) or within roughly one screen (digital) prevents readers from losing the mapping as they explore longer charts [@muth_remind_colors_2023].

**Notes:** This is especially important in tall/long visualizations where readers scroll through multiple sections.

## When “keep the key close” applies <!-- role: context -->

- **User Goal:** Understand what each color-coded series/region/category represents while reading.
- **Task:** Decode categories from color while scanning across multiple marks or sections.
- **Data:** Categorical (multiple groups encoded by distinct colors).
- **Chart Setting:** Long/tall charts, multi-panel pieces, print layouts, or any view where the legend could scroll offscreen.
- **Audience:** General audiences and first-time readers of the chart.
- **Success Criterion:** Readers can correctly name categories from color without interrupting their reading flow.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Categories are directly labeled on the marks so readers don’t need a legend to decode colors. **Why:** A separate always-visible key becomes redundant and competes for space and attention.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Space for the data display and room for other annotations. **Risk:** Repeating or pinning the key can create visual clutter or crowd mobile layouts. **Mitigation:** Keep the key compact and prioritize legibility over decorative styling.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Showing the color key only once at the top (or far away) in a long visualization. **Why it fails:** Readers forget mappings and must scroll back and forth, breaking comprehension and flow.

## Quick tests <!-- role: check -->

**Failure Sign:** You find yourself scrolling to re-check colors while reading your own chart. **Quick Check:** Start at any point in the visualization and see whether the key is visible without scrolling more than one screen. **Stronger Test:** Ask someone to interpret a mid-chart data point’s category without letting them scroll to hunt for the key.

## What to do instead <!-- role: fix -->

- Make the color key sticky so it remains visible while readers scroll.
- Repeat the same color key at natural breakpoints (e.g., above each panel or section).
- Re-layout the chart into smaller panels so each panel can carry its own nearby key.
- If space is extremely limited, replace the key with direct labels on the marks.
