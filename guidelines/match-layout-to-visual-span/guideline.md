---
id: match-layout-to-visual-span
title: Separate Charts for Global Tasks, Superpose for Local Tasks
bibliography: references.bib
description: Choose spatial arrangements based on whether the user compares whole
  sets (global) or specific items (local).
labels:
- chart:bar
- chart:line
- task:compare
- visual:layout
- impact:efficiency
---

## The Rule <!-- role: advice -->
Determine the "Visual Span" of the user's task before choosing a layout:
*   If the task is **Global** (comparing means, ranges, or overall shapes), **separate** the charts spatially (e.g., Stacked Small Multiples).
*   If the task is **Focal** (comparing individual item deltas or spotting outliers), **superpose** (overlay) the charts in the same space.

## The Logic <!-- role: reason -->
There is no single "best" arrangement for visual comparison; it depends on the scope of visual attention required.
*   **The Principle:** **Focal vs. Global Proxies.** Superposition minimizes the distance between specific items, optimizing for **focal proxies** (like neighbor deltas). Separation preserves the visual integrity of the whole shape, optimizing for **global proxies** (like hull areas or centroids).
*   **The Evidence:** In "Biggest Mean" tasks (global), superposition performed worst because it obscured global shapes. In "Biggest Delta" tasks (focal), superposition performed best because it highlighted local differences. Performance flips entirely based on the task scope [@jardine_perceptual_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** Designing a dashboard or report where the analytic questions are known (e.g., "Are sales generally higher?" vs. "Which specific month had the biggest drop?").
*   **Data Type:** Multi-series data (bar or line charts).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to do **both** global and focal tasks with high frequency on the same view.
*   **Reason:** You may need to provide interactive transitions or toggle views, as no single static view optimizes for both proxies simultaneously.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot rely on a "one-size-fits-all" default layout. You must understand the user's analytic intent.
*   **The Risk:** Choosing the wrong layout for the task (e.g., stacking charts for a delta comparison) significantly degrades human perceptual precision.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using "Mirrored" charts (back-to-back) for general comparison.
*   **Why it fails:** While mirroring works for finding correlations (symmetry detection), it performs poorly for both Mean and Range comparisons compared to simple vertical stacking [@jardine_perceptual_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Check the intersection of marks. Are distinct series sharing the same pixels?
*   **The Test:** If they share pixels (Superposed), is the user looking for *differences between specific points*? If yes, keep it. If they are looking for *overall averages*, separate them.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If the task is unclear, provide small multiples (Stacked/Adjacent) as the safer default for general data comprehension, as superposition creates occlusion that hinders global summary.
*   **Best Fix:** Explicitly design different views for different questions: A superposed view for "Difference Detection" and a small-multiple view for "Trend/Summary Comparison."
