---
id: avoid-stripeplots-density
title: Avoid Stripeplots for Density Visualization
bibliography: references.bib
description: Do not use stripeplots (gradient barcodes) for uncertainty on small screens
  as they lead to poor precision.
labels:
- chart:stripeplot
- task:avoid
- visual:opacity
- impact:readability
- data:density
- audience:mobile
---

## The Rule <!-- role: advice -->
Do not use stripeplots (linear heatmaps or barcode-like plots where density is encoded by stripe frequency or opacity) to visualize probability distributions on mobile or small screens.

## The Logic <!-- role: reason -->
Stripeplots make it difficult for users to estimate probability density and predictive intervals because they lack a clear spatial dimension (like height) to represent frequency.
*   **The Principle:** Opacity/Density Encoding efficiency. Opacity and linear density are less effective encodings than position or height for quantitative estimation.
*   **The Evidence:** In comparative studies, stripeplots had the highest estimation variance (lowest precision) and were rated the most difficult to use (Mean Ease of Use = 35/100 vs ~60/100 for others) [@kay_when_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the probability of an outcome falling within a range.
*   **Data Type:** Continuous probability distributions.
*   **Audience:** General users on mobile devices.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When vertical space is virtually non-existent (e.g., a 10-pixel high table row) and no other chart fits.
*   **Reason:** Stripeplots are extremely compact vertically. However, be aware that they function mostly as a binary "zone of possibility" rather than a precise density tool.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Vertical compactness. Stripeplots are flatter than density plots or dotplots.
*   **The Risk:** By avoiding stripeplots, you need more vertical screen real estate to show height-based encodings (dotplots/density plots).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding more stripes to smooth out the gradient.
*   **Why it fails:** This essentially turns the plot into a gradient plot, which users still find difficult to read for precise probability estimation compared to height-based plots [@kay_when_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart look like a fuzzy barcode or a linear gradient?
*   **The Test:** Ask a user to identify the "most likely" outcome. In a stripeplot, finding the mode (darkest/densest area) is significantly harder than finding the peak of a curve or the highest stack of dots.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to a standard density plot (area chart).
*   **Best Fix:** Switch to a quantile dotplot, which uses the same horizontal space but adds verticality to enable counting and precise estimation.
