---
id: use-filled-shapes-for-color-discriminability
title: Use Filled Shapes When Encoding Data with Color
bibliography: references.bib
description: Prioritize filled geometric marks over unfilled outlines or stick figures
  to ensure color differences are perceptible.
labels:
- chart:scatterplot
- visual:color
- visual:shape
- task:distinguish
- impact:clarity
- data:multivariate
---

## The Rule <!-- role: advice -->
When designing scatterplots that use color hue to distinguish categories, use **filled shapes** (e.g., solid circles, solid squares) rather than unfilled outlines or thin line-based symbols (e.g., crosses, plus signs).

## The Logic <!-- role: reason -->
The ability to discriminate between different colors depends heavily on the spatial area and density of the mark. Thin outlines or symbols made of lines (like crosses) have insufficient visual mass to allow accurate color differentiation.
*   **The Principle:** Visual Saliency and Color Discriminability.
*   **The Evidence:** Research collated by [@zeng_review_2023] highlights that "color hue (CH) is generally more discriminable with filled shapes than with unfilled ones." Original experiments by [@smart_measuring_2019] demonstrated that participants could more accurately identify color differences on dense, filled shapes compared to unfilled shapes or "modified Quantitative Texton Sequences" (mQTons) like stars or asterisks.

## Where to Apply <!-- role: context -->
This advice applies to multiclass scatterplots where color is a primary encoding channel.
*   **User Goal:** Distinguishing between different categories (nominal data) encoded by color hue.
*   **Data Type:** Multivariate data involving nominal categories and quantitative axes.
*   **Audience:** Analytical users needing to rapidly identify group membership.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dealing with severe occlusion (overplotting).
*   **Reason:** Filled shapes can obscure data points underneath them. In high-density plots, unfilled shapes might be necessary to see the distribution density, though this sacrifices color legibility [@smart_measuring_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "outline" aesthetic which can sometimes feel lighter or more precise.
*   **The Risk:** In dense datasets, filled shapes increase the likelihood of occlusion, where data points hide one another completely.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using hollow circles or "plus" signs to encode categories while simultaneously coloring them to encode a second variable.
*   **Why it fails:** The lines are too thin for the eye to reliably register the color hue, leading to errors in category identification [@smart_measuring_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the colors look washed out or indistinguishable at a glance? Do you have to squint to see if a "plus" sign is blue or green?
*   **The Test:** Step back from the screen. If the color of the mark becomes ambiguous while the position is still visible, the mark has insufficient density.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the mark style from `hollow` or `stroke` to `fill`.
*   **Best Fix:** Use solid circles or squares. If distinguishing categories is difficult with color alone, use redundant encoding (shape + color), but ensure the shapes chosen are solid (e.g., solid circle vs. solid square) rather than solid vs. outline.
