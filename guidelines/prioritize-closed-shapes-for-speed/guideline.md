---
id: prioritize-closed-shapes-for-speed
title: Use closed shapes for faster target identification
bibliography: references.bib
description: Closed shapes (circles, squares) are processed faster and more accurately
  than open shapes (crosses, asterisks).
labels:
- chart:scatterplot
- visual:shape
- impact:speed
- impact:accuracy
- audience:general
---

## The Rule <!-- role: advice -->
When speed and accuracy are paramount, or when selecting a symbol for a single primary data category, choose a "closed" shape (one that bounds a region, like a circle, square, or triangle) rather than an "open" shape (like an asterisk, plus sign, or cross).

## The Logic <!-- role: reason -->
Closed shapes represent a stronger perceptual category that the human visual system processes more efficiently than open shapes.
*   **The Principle:** Attentional Selection and Pre-attentive Processing.
*   **The Evidence:** Across flanker tasks and same/different discrimination tasks, participants responded significantly faster and more accurately when the target was a closed shape compared to an open shape. For example, closed shapes were identified faster (mean 668 ms) than open shapes (mean 689 ms) in discrimination tasks [@burlinson_open_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapid identification of data points or searching for a specific class in a display.
*   **Data Type:** Large datasets where processing time matters.
*   **Visual Density:** Cluttered scatterplots. The performance advantage of closed shapes (and the interference caused by open shapes) is particularly evident in high-load, cluttered displays [@burlinson_open_2018].

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The background is extremely visually busy or has a texture that mimics closed shapes.
*   **Reason:** While not explicitly tested in this paper, standard figure-ground theory suggests contrast is key. However, within the scope of this specific paper, the closed-shape advantage was robust across standard black-on-white and white-on-black displays.

## The Price <!-- role: costs -->
*   **The Risk:** Over-plotting. Closed shapes (especially if filled, though the paper focused on topology) geographically occupy more pixel space than the thin lines of open shapes, potentially leading to more overlap in extremely dense areas.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using complex open symbols (like a 5-point asterisk) to try to make a point "stand out."
*   **Why it fails:** The study indicates that open shapes generally result in longer response times and higher error rates compared to simple closed shapes like triangles or squares [@burlinson_open_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is your primary data series represented by a Plus, Cross, or Asterisk?
*   **The Test:** Review the shapes assigned to your most critical variables. Are they composed of unbounded line segments?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Swap the symbol for the primary category to a Circle or Square.
*   **Best Fix:** If you have multiple categories, assign the closed shape to the highest priority class and open shapes to lower priority or background classes.
