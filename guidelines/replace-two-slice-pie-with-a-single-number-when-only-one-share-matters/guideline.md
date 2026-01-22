---
id: replace-two-slice-pie-with-a-single-number-when-only-one-share-matters
title: Replace two-slice pie charts with a single number when only one share matters
bibliography: references.bib
description: If a pie chart has only two slices, consider stating the key percentage
  in text instead of charting.
labels:
- chart:pie
- task:communicate
- visual:text
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Replace a two-slice pie with the one meaningful percentage in text <!-- role: advice -->

If your pie chart would show only two values, state the single meaningful share as a number instead of using a pie chart. Treat the other slice as the implied remainder to 100%.

## Why two-slice pies add little information <!-- role: reason -->

With only two categories, the chart often encodes one value plus its complement, so the visualization can be redundant compared with a clearly written percentage.

**Mechanism:** When one slice fully determines the other (100% minus the stated value), the chart contributes little beyond the numeric statement.

**Evidence:** Two-value pies are described as effectively communicating one value and its difference from 100%, and the recommendation is to consider mentioning the one number instead of showing a chart [@muth_pie_charts_2018].

**Notes:** This applies when the communication goal is simply the magnitude of one share, not when the categorical framing itself needs emphasis.

## When the data is just a share and its remainder <!-- role: context -->

- **User Goal:** Learn a single percentage (e.g., approval rate, share saying “yes”).
- **Task:** Read one value, not compare multiple categories.
- **Data:** Two categories that sum to 100%.
- **Chart Setting:** Articles or reports where space is limited and the point can be made in a sentence.
- **Audience:** General audiences who benefit from direct statements.
- **Success Criterion:** The reader retains the key percentage without needing a legend or chart reading.

## When a two-slice visual may still be warranted <!-- role: exceptions -->

**Break it when:** The communication requires showing the explicit split as a visual object (the two categories themselves are both central). **Why:** A single number can under-emphasize that the result is a complete partition of a whole [@muth_pie_charts_2018].

## Tradeoffs of removing the chart <!-- role: costs -->

**Sacrifice:** You lose a visual cue that reinforces “part of a whole.” **Risk:** Readers may not immediately infer the complement category if it is not stated. **Mitigation:** Add a short phrase that names the remainder (e.g., “the rest did not”).

## Common redundant charting patterns <!-- role: mistakes -->

**Mistake:** Drawing a two-slice pie that restates a single percentage already given in the text. **Why it fails:** It adds chart ink without adding new information beyond the implied remainder [@muth_pie_charts_2018].

## Quick checks for redundancy <!-- role: check -->

**Failure Sign:** One slice is “everything else,” “no,” or “not X,” and the story focuses on the “yes” share. **Quick Check:** If removing the chart would not change the reader’s ability to answer the main question, use text instead. **Stronger Test:** Replace the chart with one sentence and ask if any decision-relevant information was lost.

## What to do instead <!-- role: fix -->

- Write the key percentage directly in the narrative or as a prominent callout.
- If you must visualize, use a compact annotated number that includes “out of 100%” framing.
- If you need to compare the same two-slice split across groups, switch to a stacked bar chart.
