---
id: replace-numeric-color-key-labels-with-directional-labels-when-appropriate
title: "Use Directional Labels Instead of Numbers When Numbers Don\u2019t Help"
bibliography: references.bib
description: When exact units and values add confusion, label quantitative color keys
  with simple direction (e.g., less/more) rather than numbers.
labels:
- chart:map
- task:understand
- visual:color
- impact:clarity
- data:quantitative
- audience:novice
- complexity:intermediate
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

If the exact values and units are not essential (or are hard to explain), label the color key with directional text like “less/more” or “worse/better” instead of numbers.

## The Logic <!-- role: reason -->

Numbers can add cognitive load when the metric is complex and doesn’t materially improve understanding; directional labels communicate the intended takeaway (trend/direction) with less friction. Muth notes that omitting values can be sufficient and is more common than readers might expect [@muth_color_keys_2023].

- **The Principle:** Reduce unnecessary precision to improve comprehension
- **The Evidence:** [@muth_color_keys_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Grasping directionality or relative intensity rather than exact measurement
- **Data Type:** Quantitative scales where the metric needs extensive explanation or is secondary to the story
- **Audience:** Broad audiences and quick-scan contexts

## When to Break It <!-- role: exceptions -->

- **Scenario:** Readers must interpret exact thresholds or compare precise values (especially in static graphics)
- **Reason:** Removing numbers prevents precise reading and can undermine the chart’s usefulness for exact interpretation [@muth_color_keys_2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Numerical precision and explicit units
- **The Risk:** Some readers may question what “more” means without at least minimal numeric anchors elsewhere [@muth_color_keys_2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping confusing units and dense numbers “just in case”
- **Why it fails:** The legend becomes harder to parse, and the added detail doesn’t help most readers reach the intended takeaway [@muth_color_keys_2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend is text-heavy and still doesn’t clarify what the colors mean to a non-expert.
- **The Test:** Ask: “Do readers need these numbers to understand the message?” If not, switch to directional labeling [@muth_color_keys_2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace most labels with “less ↔ more” (or equivalent), keeping only minimal anchors if needed.
- **Best Fix:** Redesign the key as a clearly directional guide (possibly with an arrow) that matches the intended interpretation of the visualization [@muth_color_keys_2023].
