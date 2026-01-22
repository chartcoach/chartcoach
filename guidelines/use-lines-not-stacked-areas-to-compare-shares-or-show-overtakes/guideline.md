---
id: use-lines-not-stacked-areas-to-compare-shares-or-show-overtakes
title: Use line charts instead of stacked area charts to compare shares or show one
  overtaking another
bibliography: references.bib
description: Stacked areas are weak for comparing components; use lines to compare
  shares and emphasize crossings.
labels:
- chart:area
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:foundational
---

## Use line charts for comparing shares and highlighting overtakes <!-- role: advice -->

Use a line chart instead of a stacked area chart when your main goal is to compare the size of different shares with each other or to show that one share overtook another.

## Moving baselines make within-stack comparisons unreliable <!-- role: reason -->

In stacked areas, only the bottom series has a consistent baseline; all other series float on top of changing totals, which makes comparing their magnitudes and detecting crossings harder than with lines on a shared baseline.

**Mechanism:** A shared baseline supports direct visual comparison of vertical position; stacked offsets turn comparisons into mental subtraction.

**Evidence:** Area charts are described as not the best choice for comparing different shares with each other, and line charts are recommended when the goal is to emphasize that one share overtook another; lines also allow showing only the relevant shares [@muth_area_charts_2018].

**Notes:** Showing fewer series can sharpen the comparison without changing the underlying question.

## When this applies <!-- role: context -->

- **User Goal:** Decide which of two or more shares is larger at different times.
- **Task:** Compare shares directly; identify crossings/overtakes.
- **Data:** Time series of proportions or components where relative ordering matters.
- **Chart Setting:** Explanatory charts where a specific comparison is the headline.
- **Audience:** Readers who need a clear “which is bigger” answer.
- **Success Criterion:** Readers can quickly and correctly identify the crossing point and relative ordering.

## When not to follow this <!-- role: exceptions -->

**Break it when:** The primary message is the evolution of the total together with composition, not comparisons between specific components. **Why:** The stacked area form is aligned with total+composition reading rather than cross-component comparison [@muth_area_charts_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose the immediate part-to-whole framing that stacked areas provide. **Risk:** Too many lines can create clutter and make matching labels to series difficult. **Mitigation:** Limit the chart to the few shares needed to answer the overtaking/comparison question [@muth_area_charts_2018].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a full stacked area chart to argue that one group became larger than another. **Why it fails:** The series sit on different, shifting baselines, obscuring direct comparison and the timing of an overtake [@muth_area_charts_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** You need to point out the overtake with heavy explanation because it is not visually obvious. **Quick Check:** If the key sentence contains “overtook,” “surpassed,” or “became larger than,” try lines. **Stronger Test:** Plot just the two relevant shares as lines and confirm the crossing reads instantly [@muth_area_charts_2018].

## What to do instead <!-- role: fix -->

- Replace the stacked area chart with a line chart to compare shares on a common baseline [@muth_area_charts_2018].
- Show only the two or three shares involved in the key comparison instead of all components [@muth_area_charts_2018].
- Add direct labels and a brief annotation at the crossing point to support fast reading [@muth_area_charts_2018].
