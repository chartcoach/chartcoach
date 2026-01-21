---
id: discretize-bars-into-small-countable-segments-for-small-values
title: Discretize Bars into Small Countable Segments for Small Values
bibliography: references.bib
description: For small numeric ranges, break bars into a few discrete units (stacked
  items) to improve short-term recall.
labels:
- chart:bar
- task:recall
- visual:length
- impact:memorability
- data:categorical
- audience:general
- encoding:stacked-segmentation
- source:haroz-chi2015
---

## The Rule <!-- role: advice -->

When values are small (about 1–5), represent magnitude with a small stack of discrete items (or otherwise segment a bar into a few units) instead of a single stretched bar.

## The Logic <!-- role: reason -->

Small discrete counts can be encoded quickly and precisely (subitizing), and stacking redundantly encodes magnitude as both height and number—improving working-memory recall for small ranges.

- **The Principle:** Redundant encoding + efficient small-number perception
- **The Evidence:** Stacked representations reduced recall error vs stretched representations in Exp. 1 and in the 1–5 condition of Exp. 2; the benefit disappeared at larger ranges [@harozISOTYPEVisualizationWorking2015a].

## Where to Apply <!-- role: context -->

- **User Goal:** Memorize a small set of values after a brief glance
- **Data Type:** Categorical values with small magnitudes (≈1–5) and limited categories (e.g., 3 bars)
- **Audience:** General audiences, especially in glanceable graphics

## When to Break It <!-- role: exceptions -->

- **Scenario:** Values extend beyond ~5 items per bar (e.g., ranges like 2–10 or 3–15)
- **Reason:** The stacking advantage diminished and disappeared as ranges increased in Exp. 2, consistent with the loss of precise small-number processing [@harozISOTYPEVisualizationWorking2015a].

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual clutter than a single clean bar; more marks to render
- **The Risk:** At higher values, stacks become hard to discern in limited space, undermining readability [@harozISOTYPEVisualizationWorking2015a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using very large stacks (many tiny icons) to represent large values
- **Why it fails:** The measured benefit is tied to small counts; beyond that, counting/estimation becomes noisy and the advantage disappears [@harozISOTYPEVisualizationWorking2015a].

## How to Check <!-- role: check -->

- **Visual Sign:** Bars are divided into a manageable number of segments (not dozens)
- **The Test:** If typical bars require more than ~5 segments, expect the memory benefit to vanish; compare a stretched version vs segmented version on recall error [@harozISOTYPEVisualizationWorking2015a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce segmentation so each bar uses only a few units (or revert to stretched bars when values are larger).
- **Best Fix:** Use stacking/segmentation only for low ranges where units stay within ~1–5 per category; otherwise use a standard length encoding [@harozISOTYPEVisualizationWorking2015a].
