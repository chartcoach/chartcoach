---
id: avoid-superfluous-imagery
title: Eliminate Superfluous Background Images
bibliography: references.bib
description: Avoid using decorative background images that do not encode data, as
  they distract users and increase error rates.
labels:
- chart:bar
- visual:embellishment
- impact:clarity
- impact:memory
- risk:distraction
---

## The Rule <!-- role: advice -->
Do not place decorative images or illustrations in the background of your chart if they do not directly represent the data values.

## The Logic <!-- role: reason -->
While some embellishments can be helpful, purely decorative background imagery acts as a distraction. In Experiment 1, [@haroz_isotype_2015] found that a "superfluous" condition—a bar chart with a background image relevant to the category but irrelevant to the quantity—resulted in 45% higher error rates compared to standard charts. It diverts attention away from the data encoding.

*   **The Principle:** Selective Attention and Distraction
*   **The Evidence:** Experiment 1 in [@haroz_isotype_2015] demonstrated a dramatic increase in recall error when superfluous imagery was present. Experiment 4 showed it also slowed down processing speed.

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurately perceiving and remembering data.
*   **Data Type:** Any quantitative chart.
*   **Audience:** All audiences, particularly where precision matters.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** No clear exceptions found in this study for quantitative tasks.
*   **Reason:** The study specifically isolated "superfluous" imagery and found it universally detrimental to performance (memory and speed) in the tasks tested.

## The Price <!-- role: costs -->
*   **The Sacrifice:** "Visual flair" or artistic decoration that might be intended to set a mood.
*   **The Risk:** The chart may look "dry" or "boring" to a designer accustomed to magazine-style infographics.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing a faint watermark of the subject (e.g., a watermark of a dog behind a chart about dogs).
*   **Why it fails:** Even if low contrast, the visual complexity interferes with the memory encoding of the actual data bars [@haroz_isotype_2015].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there an image in the chart area that does not get taller/wider as the data changes?
*   **The Test:** Remove the image. If the data is still fully readable, the image was superfluous.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Delete the background layer.
*   **Best Fix:** If you want to include thematic imagery, use the image *as* the data (e.g., a stacked ISOTYPE chart) rather than as decoration behind it.
