---
id: do-not-expect-permuting-line-graphs-to-improve-average-judgments
title: Do Not Expect Line-Graph Permutation to Improve Average Judgments
bibliography: references.bib
description: Shuffling x-order within time windows of a line graph does not significantly
  improve accuracy for selecting the maximum-average window.
labels:
- chart:line
- task:compare
- task:select
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- technique:permutation
- task:aggregate-judgment
- source:correll-chi-2012
---

## The Rule <!-- role: advice -->

Do not rely on permuting (shuffling) the x-order of points within time windows of a line graph as a way to help users choose the window with the highest average.

## The Logic <!-- role: reason -->

The study tested “1D permuted” line graphs (within-month horizontal shuffling) intended to break shape continuity. This manipulation did not yield a significant improvement for line graphs, unlike the clear benefit observed for permuted colorfields. This suggests that, for this task, line graphs do not gain the same perceptual-averaging advantage from permutation [@correllComparingAveragesTime2012a].

- **The Principle:** Shape/position encodings do not automatically become easier to average by disrupting continuity.
- **The Evidence:** No overall significant main effect of permutation (F(1,1921)=2.2769, p=0.1315) and the reported benefit of permutation was specific to the colorfield case via interaction effects [@correllComparingAveragesTime2012a].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which predefined time window has the highest average from a line graph.
- **Data Type:** Dense time series with window boundaries (e.g., monthly bins) where designers might consider disrupting lines to aid averaging.
- **Audience:** General users under time pressure, performing aggregate comparison rather than detailed tracing [@correllComparingAveragesTime2012a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have a different, non-average task where breaking temporal continuity is explicitly desired (the paper does not establish benefits for other tasks).
- **Reason:** The paper’s evidence is specific to the maximum-average window task; it does not claim permutation is never useful, only that it did not improve this task for line graphs [@correllComparingAveragesTime2012a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose meaningful temporal continuity and recognizable trends.
- **The Risk:** You pay the interpretability cost without getting accuracy gains on the target aggregate task [@correllComparingAveragesTime2012a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Make the line more ‘average-able’ by scrambling it.”
- **Why it fails:** The experiment found no significant advantage for permuted line graphs on the average-judgment task, so the added disruption is not justified for this purpose [@correllComparingAveragesTime2012a].

## How to Check <!-- role: check -->

- **Visual Sign:** The line looks jagged and discontinuous within each window but users still struggle on close-call months.
- **The Test:** A/B test ordered vs within-window permuted line graphs on the maximum-average selection task; expect little to no improvement based on the study’s results [@correllComparingAveragesTime2012a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Revert to an ordered line graph if you need temporal continuity for other reasons.
- **Best Fix:** If the core task is window-average comparison, switch to a colorfield (optionally permuted within windows) rather than trying to “repair” a line graph via permutation [@correllComparingAveragesTime2012a].
