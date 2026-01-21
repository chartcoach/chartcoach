---
id: limit-font-sizes-to-keep-charts-tidy
title: Limit the Number of Font Sizes
bibliography: references.bib
description: Use only a small set of clearly distinct font sizes to avoid messy, noisy
  typography.
labels:
- chart:general
- task:design
- visual:text
- impact:clarity
- data:general
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use as few font sizes as possible—especially for labels and annotations—aiming for two clearly distinct levels, and use boldness within a size to emphasize.

## The Logic <!-- role: reason -->

Too many font sizes create visual noise and weaken hierarchy. A small, consistent set of sizes keeps the chart orderly while still enabling emphasis through weight and contrast.

- **The Principle:** Consistency reduces visual clutter
- **The Evidence:** [@muth_text_in_data_visualizations_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Scan labels/annotations quickly without typographic distraction
- **Data Type:** Charts with multiple annotations and labels
- **Audience:** All, especially general readers who rely on clean hierarchy cues [@muth_text_in_data_visualizations_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need a special display size for a single headline-style annotation that acts like a mini-title.
  - **Reason:** One intentional exception can work if it’s clearly a different role and not repeated inconsistently [@muth_text_in_data_visualizations_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer “degrees” of emphasis via size.
- **The Risk:** If you rely only on size for hierarchy, limiting sizes may force you to use weight/color more deliberately [@muth_text_in_data_visualizations_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Creating a new font size for each annotation to make it fit a space.
  - **Why it fails:** Produces a messy, unstructured look and unclear priority [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Using tiny sizes to squeeze in detail.
  - **Why it fails:** Readability drops; detail still won’t be read [@muth_text_in_data_visualizations_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Labels look like they come from multiple unrelated systems; nothing aligns visually.
- **The Test:** Count distinct font sizes used for annotations/labels; if it’s more than two (excluding title/metadata), simplify [@muth_text_in_data_visualizations_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Standardize annotations/labels to two sizes (e.g., small gray + slightly larger dark) and use bold to emphasize words.
- **Best Fix:** Redesign label placement and wording so text fits without needing new sizes; move secondary detail to tooltips or notes [@muth_text_in_data_visualizations_2022].
