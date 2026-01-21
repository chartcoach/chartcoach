---
id: do-not-expect-open-vs-closed-benefits-in-homogeneous-separate-plots
title: Do Not Rely on Open vs. Closed Shape Differences in Homogeneous Separate Plots
bibliography: references.bib
description: In side-by-side homogeneous plots, open vs. closed symbol choice alone
  may not improve speed or accuracy.
labels:
- chart:scatter
- task:compare
- visual:shape
- impact:clarity
- data:categorical
- audience:general
- source:paper
---

## The Rule <!-- role: advice -->

When each plot is homogeneous (one symbol type per plot), do not assume that choosing open vs. closed symbols will materially improve performance.

## The Logic <!-- role: reason -->

Open/closed advantages show up most strongly when viewers must **discriminate symbols within the same display**; in the paper’s baseline side-by-side (separate-plot) tasks, target feature (open vs. closed) generally did not affect response times and showed limited/complex effects in errors.

- **The Principle:** Category interference requires competing items; without competition, the benefit can disappear.
- **The Evidence:** Experiment 3 separate-plot displays showed no significant RT effects of target feature across tasks, with performance dominated by task and difficulty rather than open/closed category [@burlinsonOpenVsClosed2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing two separate panels (e.g., which panel has higher average y, more points, or the linear relationship).
- **Data Type:** Small multiples or side-by-side plots where each panel uses one symbol type.
- **Audience:** General.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You will later combine categories into a single mixed-symbol panel or expect viewers to switch attention between multiple symbol types within one plot.
- **Reason:** The same paper shows open/closed category effects emerging when heterogeneous symbols co-occur and must be selectively processed [@burlinsonOpenVsClosed2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to invest effort in other encodings or layout decisions (since shape family alone may not help here).
- **The Risk:** Over-optimizing symbol family in homogeneous panels can distract from more impactful design choices for those tasks.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Spending design effort swapping open to closed symbols in separate plots expecting a speed boost.
- **Why it fails:** The paper’s separate-plot results suggest task type and difficulty dominate, with little consistent RT advantage from open vs. closed shape choice alone [@burlinsonOpenVsClosed2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** Changing symbols between open and closed does not change how quickly users answer when each panel contains only one symbol type.
- **The Test:** A/B test symbol family while keeping everything else identical; if RT/accuracy do not move, this rule applies.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep your current symbol family and focus on making the task easier (e.g., reduce difficulty/delta or simplify the comparison structure).
- **Best Fix:** If symbol discrimination is important, move from separate homogeneous plots to a design where symbol categories must be discriminated within the same view—where open/closed differences are evidenced to matter [@burlinsonOpenVsClosed2018a].
