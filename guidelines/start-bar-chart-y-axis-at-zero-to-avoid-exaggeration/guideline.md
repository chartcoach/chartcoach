---
id: start-bar-chart-y-axis-at-zero-to-avoid-exaggeration
title: Start Bar Chart Axes at Zero
bibliography: references.bib
description: Avoid message exaggeration in bar charts by not truncating the quantitative
  axis.
labels:
- chart:bar
- task:compare
- visual:position
- impact:integrity
- data:quantitative
- audience:general
- distortion:truncated-axis
---

## The Rule <!-- role: advice -->

Start the quantitative axis of bar charts at zero; do not truncate the axis range to magnify differences.

## The Logic <!-- role: reason -->

Bar lengths are visually compared from a shared baseline; truncating the axis changes the apparent magnitude of differences and leads viewers to overstate “how much bigger” one value is than another, even when the data labels are present.

- **The Principle:** Baseline-dependent magnitude comparison
- **The Evidence:** In Pandey et al.’s study, truncated-axis bar charts produced significantly higher “how much” judgments than the control (non-truncated) version (Mann–Whitney U, p = 0.0003), indicating message exaggeration/understatement at the message level [@pandeyHowDeceptiveAre2015].

## Where to Apply <!-- role: context -->

- **User Goal:** Judge how much one category exceeds another (degree of difference).
- **Data Type:** Categorical comparisons with quantitative values.
- **Audience:** General audiences reading journalistic/advocacy/business-style graphics.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your chart’s goal is not magnitude comparison but showing small fluctuations around a stable level.
- **Reason:** The paper’s evidence targets deception risk for “how much” judgments; it does not evaluate legitimate analytical use cases for zoomed-in scales [@pandeyHowDeceptiveAre2015].

## The Price <!-- role: costs -->

- **The Sacrifice:** Small differences may look visually subtle.
- **The Risk:** Viewers may miss modest but meaningful changes if the scale spans a wide range.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a truncated axis but adding numeric labels and assuming that prevents misinterpretation.
- **Why it fails:** The study included accurate numbers on charts, yet viewers were still significantly swayed by the visual distortion [@pandeyHowDeceptiveAre2015].

## How to Check <!-- role: check -->

- **Visual Sign:** The first tick mark on the quantitative axis is above zero and bars appear to “start in mid-air.”
- **The Test:** Ask: “Would the perceived difference shrink materially if the axis started at 0?” If yes, you’ve created exaggeration risk.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reset the quantitative axis minimum to 0.
- **Best Fix:** If you must show fine variation, provide an additional, clearly separated view (e.g., a second panel) while keeping the primary bar chart baseline at zero to preserve message integrity [@pandeyHowDeceptiveAre2015].
