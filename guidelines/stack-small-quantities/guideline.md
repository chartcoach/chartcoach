---
id: stack-small-quantities
title: Stack Elements for Small Values
bibliography: references.bib
description: Represent small values by stacking discrete elements rather than stretching
  a single shape to improve memory and precision.
labels:
- chart:isotype
- chart:bar
- visual:shape
- task:estimate
- audience:general
- impact:recall
---

## The Rule <!-- role: advice -->
Represent data values as stacks of discrete items (pictographs or simple shapes) rather than single continuous stretched bars, specifically when the values are small (less than 5).

## The Logic <!-- role: reason -->
Breaking a length-defined object into a few smaller items allows the user to employ "subitizing"—the visual system's ability to instantly and precisely enumerate small quantities (typically 1-4 items). [@haroz_isotype_2015] found that stacking reduced error relative to stretched bars for small numbers because it allows redundant encoding: users can judge the height *and* count the objects.

*   **The Principle:** Subitizing and Redundant Encoding
*   **The Evidence:** Experiment 1 and 2 in [@haroz_isotype_2015] showed significantly lower error rates for stacked charts compared to stretched charts in the 1–5 value range.

## Where to Apply <!-- role: context -->
*   **User Goal:** Memorizing or quickly extracting exact values.
*   **Data Type:** Discrete integers with a small range (1–5).
*   **Audience:** General audiences or situations where working memory is taxed.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Large Data Ranges (Values > 5)
*   **Reason:** The benefits of stacking disappear when the number of items exceeds the subitizing limit (approx. 4–5). For ranges like 3–15, [@haroz_isotype_2015] found no memory benefit to stacking, and visual clutter may increase.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity and clean lines. Stacks create more visual noise than a solid bar.
*   **The Risk:** If the stack height becomes too high, users are forced to count or estimate, negating the speed advantage of subitizing.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Stretching a single icon (e.g., a tall, stretched human figure) to represent a larger value.
*   **Why it fails:** Neurath explicitly argued against this, and [@haroz_isotype_2015] confirms that stretched representations are less memorable for small values than stacked ones.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there single bars representing numbers like 3 or 4?
*   **The Test:** Count the items in the stack. If you can see the number "at a glance" without mentally counting "one, two, three...", the stack is effective.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add white "gridlines" over a solid bar to break it into discrete, countable chunks.
*   **Best Fix:** Replace the solid bar with a stack of distinct, simple shapes or icons (ISOTYPE style) corresponding to the integer value.
