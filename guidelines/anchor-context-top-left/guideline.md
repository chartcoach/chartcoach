---
id: anchor-context-top-left
title: Anchor Context in the Top-Left
bibliography: references.bib
description: Attention heatmaps confirm a systematic bias toward the leftmost parts
  of visualizations, specifically titles and headers.
labels:
- visual:layout
- visual:position
- impact:hierarchy
- audience:general
---

## The Rule <!-- role: advice -->
Position your visualization's primary title and essential headers in the top-left quadrant of the layout.

## The Logic <!-- role: reason -->
Analysis of average attention maps across different image types (visualizations, web pages, and natural images) reveals distinct viewing biases.
*   **The Principle:** **Left-Header Bias.** While natural images often trigger a "center bias" (looking at the middle), visualizations and web pages trigger a systematic bias where attention is concentrated in the top-left.
*   **The Evidence:** [@kim_bubbleview_2017] notes that comparison of click maps and eye fixations reveals "increased attention in the leftmost parts of visualizations and webpages, corresponding to the titles and headers" (see Figure 17 and Section 7). This confirms that users are conditioned to seek context in this specific location.

## Where to Apply <!-- role: context -->
*   **User Goal:** Orientation and initial processing of the display.
*   **Data Type:** Dashboards, static infographics, and web-based visualizations.
*   **Audience:** Users reading left-to-right languages.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** **Right-to-Left (RTL) Languages.**
*   **Reason:** Readers of RTL languages (e.g., Arabic, Hebrew) will naturally scan starting from the right; the layout should be mirrored.
*   **Scenario:** **Strong Central Visuals.**
*   **Reason:** If the visualization is a single, dominant image (like a map or a photo) without heavy titling, the "center bias" observed in natural scenes may take over, drawing the eye to the middle first.

## The Price <!-- role: costs -->
*   **The Sacrifice:** **Symmetry.** Centered titles often look more "balanced" artistically but may be less efficient for scanning.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** **Bottom-Aligned Context.** Placing the chart title or critical explanatory text below the chart (common in academic figures).
*   **Why it fails:** Users scan the top-left first for orientation. Placing context at the bottom forces a scan path that crosses the complex data before the user knows what they are looking at.

## How to Check <!-- role: check -->
*   **Visual Sign:** Draw a cross over your visualization to divide it into four quadrants.
*   **The Test:** Does the top-left quadrant contain the text necessary to understand the rest of the image?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Left-align your chart titles rather than centering them.
*   **Best Fix:** Ensure the top-left corner contains the "What, Where, and When" of the data, establishing the context before the eye moves to the graphical elements.
